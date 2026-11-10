#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Saad Sidqui
"""Build a PowerPoint deck from lessons and a deck manifest, following DESIGN.md.

Usage:
    .venv/bin/python tools/build_deck.py decks/SESSION.toml [--theme light|dark] [--fonts arial|atkinson]
                                          [--out build/decks] [--strict]

The manifest format is described in .claude/skills/publish/references/manifests.md.
Fonts follow DESIGN.md section 3.2: Arial by default (Liberation Sans in LibreOffice).
Writes build/decks/SESSION.pptx, then prints a summary and any word-limit warnings.
With --strict, a warning makes the exit status 1.
"""
import argparse
import re
import subprocess
import sys
import tomllib
from pathlib import Path

from markdown_it import MarkdownIt
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from check_contrast import load_tokens  # noqa: E402  (DESIGN.md tokens, single source)
from render_preview import font_environment, soffice  # noqa: E402

# Geometry from DESIGN.md section 4.1 and .claude/skills/visual-design/references/layouts.md (inches).
SLIDE_W, SLIDE_H = 13.333, 7.5
MARGIN_X, MARGIN_Y, GUTTER = 0.6, 0.5, 0.25
COLUMN = (SLIDE_W - 2 * MARGIN_X - 11 * GUTTER) / 12
CONTENT_W = SLIDE_W - 2 * MARGIN_X
FONT_SETS = {
    "atkinson": {"text": "Atkinson Hyperlegible Next", "semibold": "Atkinson Hyperlegible Next SemiBold",
                 "mono": "Atkinson Hyperlegible Mono"},
    "arial": {"text": "Arial", "semibold": None, "mono": "Courier New"},
}
# Word limits from DESIGN.md section 4.2.
TITLE_LIMITS = {"title": 10, "section": 8, "concept": 10, "example": 10, "checkpoint": 20, "exercise": 10, "recap": 10}
BODY_LIMITS = {"concept": 25, "example": 60}
NO_TABLE_STYLE = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"  # built-in "No Style, No Grid"

FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
SLIDE_RE = re.compile(r"<!-- slide: (\w+) -->\n(.*?)<!-- /slide -->", re.S)
NOTES_RE = re.compile(r"<details><summary>Notes de présentation</summary>\n\n(.*?)\n\n</details>", re.S)
WORD_RE = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿŒœ’'-]+")
MD = MarkdownIt("commonmark").enable("table")


def col_x(n):
    return MARGIN_X + (n - 1) * (COLUMN + GUTTER)


def span(k):
    return k * COLUMN + (k - 1) * GUTTER


def rgb(hex_colour):
    return RGBColor.from_string(hex_colour.lstrip("#"))


def count_words(text):
    return len(WORD_RE.findall(text))


def inline_runs(token):
    runs, bold, italic = [], False, False
    for child in token.children or []:
        if child.type == "strong_open":
            bold = True
        elif child.type == "strong_close":
            bold = False
        elif child.type == "em_open":
            italic = True
        elif child.type == "em_close":
            italic = False
        elif child.type == "text":
            runs.append((child.content, bold, italic, False))
        elif child.type == "code_inline":
            runs.append((child.content, bold, italic, True))
        elif child.type in ("softbreak", "hardbreak"):
            runs.append((" ", bold, italic, False))
    return runs


def blocks(markdown):
    """Turn the Markdown body of a slide region into paragraphs, list items, tables, code and images."""
    out, kinds, table, row = [], [], None, None
    for token in MD.parse(markdown):
        kind = token.type
        if kind == "bullet_list_open":
            kinds.append("bullet")
        elif kind == "ordered_list_open":
            kinds.append("number")
        elif kind in ("bullet_list_close", "ordered_list_close"):
            kinds.pop()
        elif kind == "table_open":
            table = []
        elif kind == "table_close":
            out.append({"kind": "table", "rows": table})
            table = None
        elif kind == "tr_open":
            row = []
        elif kind == "tr_close":
            table.append(row)
        elif kind in ("fence", "code_block"):
            out.append({"kind": "code", "runs": [(token.content.rstrip("\n"), False, False, True)]})
        elif kind == "inline":
            if table is not None:
                row.append(inline_runs(token))
                continue
            images = [c for c in token.children or [] if c.type == "image"]
            if images:
                out.extend({"kind": "image", "src": c.attrGet("src"), "alt": c.content} for c in images)
                continue
            out.append({"kind": kinds[-1] if kinds else "para", "runs": inline_runs(token)})
    return out


def regions(text):
    body = FRONT_RE.sub("", text, count=1)
    for kind, inner in SLIDE_RE.findall(body):
        heading = re.search(r"^### (.+)$", inner, re.M)
        notes = NOTES_RE.search(inner)
        rest = re.sub(r"^### .+$", "", NOTES_RE.sub("", inner), count=1, flags=re.M)
        title = re.sub(r"[*_`]", "", heading.group(1)).strip() if heading else ""
        yield {"kind": kind, "title": title, "body": blocks(rest), "notes": notes.group(1).strip() if notes else ""}


class Deck:
    def __init__(self, meta, theme, fonts):
        self.c = load_tokens()[theme]
        self.track = self.c["track"][meta["track"]]
        self.fonts = FONT_SETS[fonts]
        self.stops = list(meta.get("stops", []))
        self.prs = Presentation()
        self.prs.slide_width, self.prs.slide_height = Inches(SLIDE_W), Inches(SLIDE_H)
        self.prs.core_properties.title = meta["title"]
        self.prs.core_properties.language = "fr-CA"
        self.layout = self.prs.slide_layouts[5]  # "Title Only": every slide has a real title for screen readers
        self.number = 0
        self.warnings = []
        self.with_notes = 0
        self.lesson_dir = ROOT

    # Text -----------------------------------------------------------------------------------------
    def style(self, run, size, colour, weight="regular", italic=False, mono=False):
        font = run.font
        if mono:
            font.name = self.fonts["mono"]
        elif weight == "semibold" and self.fonts["semibold"]:
            font.name = self.fonts["semibold"]
        else:
            font.name = self.fonts["text"]
        font.size = Pt(size)
        font.bold = weight == "bold" or (weight == "semibold" and not self.fonts["semibold"])
        font.italic = italic
        font.color.rgb = rgb(colour)
        run._r.get_or_add_rPr().set("lang", "fr-CA")

    def bullet(self, paragraph, kind, colour):
        p_pr = paragraph._p.get_or_add_pPr()
        p_pr.set("marL", str(int(Inches(0.45))))
        p_pr.set("indent", str(-int(Inches(0.35))))
        clr = OxmlElement("a:buClr")
        srgb = OxmlElement("a:srgbClr")
        srgb.set("val", colour.lstrip("#"))
        clr.append(srgb)
        p_pr.append(clr)
        bu_font = OxmlElement("a:buFont")
        bu_font.set("typeface", self.fonts["text"])
        p_pr.append(bu_font)
        if kind == "bullet":
            mark = OxmlElement("a:buChar")
            mark.set("char", "•")
        else:
            mark = OxmlElement("a:buAutoNum")
            mark.set("type", "arabicPeriod")
        p_pr.append(mark)

    def fill_text(self, frame, paragraphs, size, colour, weight="regular", anchor=MSO_ANCHOR.TOP,
                  align=PP_ALIGN.LEFT, space_after=10, line_spacing=1.1):
        frame.word_wrap = True
        frame.auto_size = MSO_AUTO_SIZE.NONE
        frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
        frame.vertical_anchor = anchor
        for index, para in enumerate(paragraphs):
            p = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
            p.alignment = align
            p.space_after = Pt(space_after)
            p.line_spacing = line_spacing
            for text, bold, italic, mono in para["runs"]:
                run = p.add_run()
                run.text = text
                self.style(run, size, colour, "bold" if bold else weight, italic, mono)
            if para.get("kind") in ("bullet", "number"):
                self.bullet(p, para["kind"], colour)

    def textbox(self, slide, x, y, w, h, paragraphs, size, colour, **kw):
        box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        self.fill_text(box.text_frame, paragraphs, size, colour, **kw)
        return box

    # Shapes ---------------------------------------------------------------------------------------
    @staticmethod
    def flat(shape):
        """Drop the default shape style: its theme effect reference draws a shadow in LibreOffice (DESIGN.md V11)."""
        style = shape._element.find(qn("p:style"))
        if style is not None:
            shape._element.remove(style)
        return shape

    def rect(self, slide, x, y, w, h, fill=None, line=None, line_pt=1.0):
        shape = self.flat(slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)))
        if fill:
            shape.fill.solid()
            shape.fill.fore_color.rgb = rgb(fill)
        else:
            shape.fill.background()
        if line:
            shape.line.color.rgb = rgb(line)
            shape.line.width = Pt(line_pt)
        else:
            shape.line.fill.background()
        return shape

    def stop_map(self, slide, x, y, w, current, line, label, hollow, labels="current", all_filled=False):
        if not self.stops:
            return
        cy = y + 0.15
        connector = self.flat(slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x), Inches(cy), Inches(x + w), Inches(cy)))
        connector.line.color.rgb = rgb(line)
        connector.line.width = Pt(4)
        n = len(self.stops)
        xs = [x + w / 2] if n == 1 else [x + w * i / (n - 1) for i in range(n)]
        for index, sx in enumerate(xs, 1):
            here = index == current
            radius = 0.14 if here else 0.09
            dot = self.flat(slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(sx - radius), Inches(cy - radius),
                                                   Inches(2 * radius), Inches(2 * radius)))
            dot.fill.solid()
            dot.fill.fore_color.rgb = rgb(line if (all_filled or index <= current) else hollow)
            dot.line.color.rgb = rgb(line)
            dot.line.width = Pt(3)
            if labels == "all" or (labels == "current" and here):
                width = 2.4 if labels == "current" else max(1.1, min(2.4, w / max(n - 1, 1) - 0.1))
                if n > 1 and index == 1:  # first stop: the label starts at the stop
                    left, align = sx - radius, PP_ALIGN.LEFT
                elif n > 1 and index == n:  # last stop: the label ends at the stop
                    left, align = sx + radius - width, PP_ALIGN.RIGHT
                else:
                    left, align = sx - width / 2, PP_ALIGN.CENTER
                left = min(max(left, MARGIN_X - 0.1), SLIDE_W - MARGIN_X + 0.1 - width)
                self.textbox(slide, left, cy + 0.2, width, 0.4, [{"runs": [(self.stops[index - 1], False, False, False)]}],
                             18, label, weight="semibold", align=align, space_after=0)

    # Slides ---------------------------------------------------------------------------------------
    def new_slide(self, background, title, x, y, w, h, size, colour, anchor=MSO_ANCHOR.TOP):
        slide = self.prs.slides.add_slide(self.layout)
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = rgb(background)
        self.number += 1
        holder = slide.shapes.title
        holder.left, holder.top, holder.width, holder.height = Inches(x), Inches(y), Inches(w), Inches(h)
        holder.text_frame.text = ""
        self.fill_text(holder.text_frame, [{"runs": [(title, False, False, False)]}], size, colour, "bold", anchor,
                       space_after=0, line_spacing=0.95)  # Atkinson's tall line box would push a 2-line title into the body
        return slide

    def finish(self, slide, notes, number_colour=None, numbered=True):
        if numbered:
            self.textbox(slide, SLIDE_W - MARGIN_X - 0.8, 6.75, 0.8, 0.35, [{"runs": [(str(self.number), False, False, False)]}],
                         18, number_colour or self.c["muted"], align=PP_ALIGN.RIGHT, space_after=0)
        if notes:
            slide.notes_slide.notes_text_frame.text = notes
            self.with_notes += 1

    def warn(self, where, message):
        self.warnings.append(f"{where}: {message}")

    def picture(self, slide, block, x, y, w, h):
        source = (self.lesson_dir / block["src"]).resolve()
        if source.suffix.lower() == ".svg":  # SVG to PDF, then 300 dpi PNG: a direct PNG export is too coarse
            out = ROOT / "build" / "deck-assets"
            out.mkdir(parents=True, exist_ok=True)
            env = font_environment()
            pdf = soffice(source, "pdf", out, env)
            subprocess.run(["pdftoppm", "-png", "-r", "300", "-singlefile", str(pdf), str(out / source.stem)],
                           check=True, env=env, timeout=300)
            source = out / f"{source.stem}.png"
        pic = slide.shapes.add_picture(str(source), Inches(x), Inches(y))
        scale = min(Inches(w) / pic.width, Inches(h) / pic.height)  # fit inside the body zone, keep the ratio
        pic.width, pic.height = int(pic.width * scale), int(pic.height * scale)
        pic._element.nvPicPr.cNvPr.set("descr", block["alt"])

    def title_slide(self, meta):
        c = self.c
        slide = self.new_slide(c["paper"], meta["title"], MARGIN_X, 1.6, span(11), 1.2, 44, c["ink"])
        if meta.get("subtitle"):
            self.textbox(slide, MARGIN_X, 2.85, span(11), 0.7, [{"runs": [(meta["subtitle"], False, False, False)]}], 28, c["ink"])
        self.stop_map(slide, MARGIN_X + 0.4, 4.4, CONTENT_W - 0.8, 0, self.track, c["ink"], c["paper"], labels="all")
        if meta.get("date"):
            self.textbox(slide, MARGIN_X, 6.2, span(8), 0.5, [{"runs": [(meta["date"], False, False, False)]}], 20, c["muted"])
        self.finish(slide, meta.get("notes", ""), numbered=False)

    def add(self, region, stop, where):
        c, kind, title = self.c, region["kind"], region["title"]
        if count_words(title) > TITLE_LIMITS.get(kind, 10):
            self.warn(where, f"{kind} title has {count_words(title)} words (limit {TITLE_LIMITS.get(kind, 10)})")
        body_text = " ".join(t for b in region["body"] for t, *_ in b.get("runs", []))
        if kind in BODY_LIMITS and count_words(body_text) > BODY_LIMITS[kind]:
            self.warn(where, f"{kind} body has {count_words(body_text)} words (limit {BODY_LIMITS[kind]})")

        if kind == "section":
            slide = self.new_slide(self.track, title, MARGIN_X, 2.6, span(11), 1.5, 44, c["paper"])
            self.stop_map(slide, MARGIN_X + 0.4, 4.6, CONTENT_W - 0.8, stop, c["paper"], c["paper"], self.track)
            self.finish(slide, region["notes"], number_colour=c["paper"])
            return
        if kind == "title":
            self.title_slide({"title": title, "notes": region["notes"]})
            return
        if kind == "checkpoint":
            slide = self.new_slide(c["paper"], title, MARGIN_X, 3.05, CONTENT_W, 2.1, 36, c["ink"])
            band = self.rect(slide, 0, 2.2, SLIDE_W, 3.2, fill=c["signal"])
            slide.shapes._spTree.remove(band._element)
            slide.shapes._spTree.insert(2, band._element)  # keep the band behind the title text
            self.textbox(slide, MARGIN_X, 2.45, CONTENT_W, 0.45, [{"runs": [("Point de contrôle", False, False, False)]}],
                         20, c["ink"], weight="semibold", space_after=0)
            self.stop_map(slide, col_x(8), MARGIN_Y, span(5), stop, self.track, c["ink"], c["paper"])
            self.finish(slide, region["notes"])
            return
        if kind == "recap":
            slide = self.new_slide(c["paper"], title, MARGIN_X, 1.3, span(9), 1.3, 40, c["ink"])
            self.stop_map(slide, MARGIN_X + 0.4, 2.8, CONTENT_W - 0.8, 0, self.track, c["ink"], c["paper"],
                          labels="none", all_filled=True)
            items = [b for b in region["body"] if b["kind"] in ("bullet", "number", "para")]
            if len(items) > 4:
                self.warn(where, f"recap has {len(items)} statements (limit 4)")
            for b in items:
                if count_words(" ".join(t for t, *_ in b["runs"])) > 12:
                    self.warn(where, "a recap statement is longer than 12 words")
            self.textbox(slide, MARGIN_X, 3.7, CONTENT_W, 2.7, items, 24, c["ink"])
            self.finish(slide, region["notes"])
            return

        slide = self.new_slide(c["paper"], title, MARGIN_X, 1.3, span(9), 1.3, 40, c["ink"])
        self.stop_map(slide, col_x(8), MARGIN_Y, span(5), stop, self.track, c["ink"], c["paper"])
        body = region["body"]
        if kind == "example":
            self.rect(slide, MARGIN_X, 2.95, CONTENT_W, 3.65, fill=c["surface"])
            text_blocks = [b for b in body if b["kind"] in ("para", "bullet", "number", "code")]
            tables = [b for b in body if b["kind"] == "table"]
            y = 3.2
            if text_blocks:
                height = 1.4 if tables else 3.3
                self.textbox(slide, MARGIN_X + 0.3, y, CONTENT_W - 0.6, height, text_blocks, 22, c["ink"])
                y += height + 0.1
            for table in tables[:1]:
                self.table(slide, table, MARGIN_X + 0.3, y, CONTENT_W - 0.6, 6.3 - y)
        elif kind == "exercise":
            steps = [b for b in body if b["kind"] in ("number", "bullet", "para")]
            if len(steps) > 6:
                self.warn(where, f"exercise has {len(steps)} steps (limit 6)")
            for b in steps:
                if count_words(" ".join(t for t, *_ in b["runs"])) > 8:
                    self.warn(where, "an exercise step is longer than 8 words")
            self.textbox(slide, MARGIN_X, 2.95, span(7), 3.65, steps, 28, c["ink"])
            self.rect(slide, col_x(9), 2.95, span(4), 3.5, line=c["rule"], line_pt=1)
        else:  # concept, and any other content slide
            images = [b for b in body if b["kind"] == "image"]
            lines = [b for b in body if b["kind"] in ("para", "bullet", "number", "code")]
            if images and lines:
                self.warn(where, "concept slide has both a diagram and text lines (choose one)")
            if images:
                self.picture(slide, images[0], MARGIN_X, 2.95, CONTENT_W, 3.6)
            else:
                if len(lines) > 4:
                    self.warn(where, f"concept slide has {len(lines)} lines (limit 4)")
                self.textbox(slide, MARGIN_X, 2.95, CONTENT_W, 3.65, lines, 28, c["ink"])
        self.finish(slide, region["notes"])

    def table(self, slide, block, x, y, w, h):
        rows, cols = len(block["rows"]), max(len(r) for r in block["rows"])
        frame = slide.shapes.add_table(rows, cols, Inches(x), Inches(y), Inches(w), Inches(min(h, 0.55 * rows)))
        tbl = frame.table
        tbl_pr = tbl._tbl.tblPr
        style = tbl_pr.find(qn("a:tableStyleId"))
        if style is None:
            style = OxmlElement("a:tableStyleId")
            tbl_pr.append(style)
        style.text = NO_TABLE_STYLE
        for r, row in enumerate(block["rows"]):
            for k in range(cols):
                cell = tbl.cell(r, k)
                cell.fill.background()
                runs = row[k] if k < len(row) else []
                cell.text_frame.text = ""
                self.fill_text(cell.text_frame, [{"runs": runs}], 22, self.c["ink"], "bold" if r == 0 else "regular", space_after=0)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--theme", choices=["light", "dark"])
    parser.add_argument("--fonts", choices=sorted(FONT_SETS), default="arial")  # DESIGN.md section 3.2
    parser.add_argument("--out", type=Path, default=ROOT / "build" / "decks")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    manifest = tomllib.loads(args.manifest.read_text(encoding="utf-8"))
    meta = manifest["deck"]
    deck = Deck(meta, args.theme or meta.get("theme", "light"), args.fonts)
    deck.title_slide(meta)
    for part in manifest.get("part", []):
        lesson = (ROOT / part["lesson"]).resolve()
        deck.lesson_dir = lesson.parent
        for index, region in enumerate(regions(lesson.read_text(encoding="utf-8")), 1):
            deck.add(region, int(part.get("stop", 0)), f"{lesson.name} slide {index}")
    args.out.mkdir(parents=True, exist_ok=True)
    target = args.out / f"{args.manifest.stem}.pptx"
    deck.prs.save(target)
    print(target)
    print(f"{deck.number} slides, {deck.with_notes} with speaker notes, fonts: {args.fonts}, theme: {args.theme or meta.get('theme', 'light')}")
    for warning in deck.warnings:
        print(f"WARN  {warning}")
    sys.exit(1 if args.strict and deck.warnings else 0)


if __name__ == "__main__":
    main()
