#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Saad Sidqui
"""Build a PDF textbook from lessons and a book manifest, following DESIGN.md.

Usage:
    .venv/bin/python tools/build_book.py books/BOOK/book.toml [--out build/books]

The manifest format is described in .claude/skills/publish/references/manifests.md.
The textbook keeps the learner text of each lesson. It leaves out the slide regions, the
speaker notes, the timing table and the re-verify list, which are for the presenter.
Writes build/books/BOOK.pdf, with the repository's fonts embedded.
"""
import argparse
import html
import re
import sys
import tomllib
from pathlib import Path

import yaml
from markdown_it import MarkdownIt
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from check_contrast import load_tokens  # noqa: E402  (DESIGN.md tokens, single source)

FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
SLIDE_RE = re.compile(r"<!-- slide: \w+ -->\n.*?<!-- /slide -->\n?", re.S)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
PRESENTER_SECTIONS = {"Déroulement", "À revérifier avant chaque prestation"}
CALLOUTS = {"Point de contrôle": "checkpoint", "Pratique": "practice"}
MD = MarkdownIt("commonmark", {"html": True}).enable("table")
FONT_DIR = "assets/fonts"


def learner_part(path):
    text = path.read_text(encoding="utf-8")
    front = FRONT_RE.match(text)
    meta = yaml.safe_load(front.group(1)) if front else {}
    body = text[front.end():] if front else text
    body = COMMENT_RE.sub("", SLIDE_RE.sub("", body))
    sections = re.split(r"(?m)^(?=## )", body)
    kept = [s for s in sections if not (s.startswith("## ") and s[3:].split("\n", 1)[0].strip() in PRESENTER_SECTIONS)]
    return meta or {}, "".join(kept)


def wrap_callouts(fragment):
    out = []
    for piece in re.split(r"(?=<h2>)", fragment):
        heading = re.match(r"<h2>(.*?)</h2>", piece)
        kind = CALLOUTS.get(html.unescape(heading.group(1))) if heading else None
        out.append(f'<section class="callout {kind}">{piece}</section>' if kind else piece)
    return "".join(out)


def stop_map(labels, current, line, label, hollow):
    n, width, cy = len(labels), 460, 22
    left, right = 16, width - 16
    xs = [(left + right) / 2] if n == 1 else [left + (right - left) * i / (n - 1) for i in range(n)]
    parts = [f'<svg class="stops" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 64" role="img" '
             f'aria-label="{html.escape(labels[current - 1])}">',
             f'<line x1="{left}" y1="{cy}" x2="{right}" y2="{cy}" stroke="{line}" stroke-width="4"/>']
    for index, x in enumerate(xs, 1):
        radius = 9 if index == current else 6
        fill = line if index <= current else hollow
        parts.append(f'<circle cx="{x:.1f}" cy="{cy}" r="{radius}" fill="{fill}" stroke="{line}" stroke-width="3"/>')
        if index == current:
            anchor = "start" if index == 1 and n > 1 else "end" if index == n and n > 1 else "middle"
            parts.append(f'<text x="{x:.1f}" y="{cy + 32}" text-anchor="{anchor}" font-family="Atkinson Hyperlegible Next" '
                         f'font-size="15" font-weight="600" fill="{label}">{html.escape(labels[index - 1])}</text>')
    parts.append("</svg>")
    return "".join(parts)


def stylesheet(c, track):
    faces = [("Atkinson Hyperlegible Next", "atkinson-hyperlegible-next/AtkinsonHyperlegibleNext", w, s, f)
             for w, s, f in ((400, "normal", "Regular"), (400, "italic", "Italic"), (600, "normal", "SemiBold"), (700, "normal", "Bold"))]
    faces += [("Atkinson Hyperlegible Mono", "atkinson-hyperlegible-mono/AtkinsonHyperlegibleMono", w, "normal", f)
              for w, f in ((400, "Regular"), (700, "Bold"))]
    font_css = "".join(f'@font-face {{ font-family: "{family}"; src: url({FONT_DIR}/{stem}-{file}.ttf); '
                       f"font-weight: {weight}; font-style: {style}; }}\n" for family, stem, weight, style, file in faces)
    return font_css + f"""
@page {{ size: letter; margin: 0.8in 0.8in 0.9in 1in; }}
@page :left {{ margin-left: 0.8in; margin-right: 1in;
  @top-left {{ content: string(booktitle); font: 9pt "Atkinson Hyperlegible Next"; color: {c['muted']}; }}
  @bottom-left {{ content: counter(page); font: 9pt "Atkinson Hyperlegible Next"; color: {c['muted']}; }} }}
@page :right {{ margin-left: 1in; margin-right: 0.8in;
  @top-right {{ content: string(chapter); font: 9pt "Atkinson Hyperlegible Next"; color: {c['muted']}; }}
  @bottom-right {{ content: counter(page); font: 9pt "Atkinson Hyperlegible Next"; color: {c['muted']}; }} }}
@page cover {{ @top-left {{ content: none; }} @top-right {{ content: none; }}
  @bottom-left {{ content: none; }} @bottom-right {{ content: none; }} }}
html {{ font-family: "Atkinson Hyperlegible Next"; font-size: 11pt; line-height: 1.45; color: {c['ink']}; }}
body {{ margin: 0; hyphens: auto; orphans: 2; widows: 2; }}
p, li, table {{ max-width: 5.7in; }}
p {{ margin: 0 0 0.6em; text-align: left; }}
h1 {{ font-size: 26pt; font-weight: 700; line-height: 1.15; margin: 0; string-set: chapter content(); }}
h2 {{ font-size: 17pt; font-weight: 600; line-height: 1.2; margin: 1.2em 0 0.4em; break-after: avoid; }}
h3 {{ font-size: 13pt; font-weight: 600; margin: 1em 0 0.3em; break-after: avoid; }}
a {{ color: {track}; text-decoration: underline; }}
code {{ font-family: "Atkinson Hyperlegible Mono"; font-size: 0.95em; }}
table {{ border-collapse: collapse; margin: 0.6em 0; }}
th, td {{ border-bottom: 1pt solid {c['rule']}; padding: 3pt 8pt 3pt 0; text-align: left; vertical-align: top; }}
th {{ font-weight: 600; }}
.cover {{ page: cover; break-after: page; }}
.cover h1 {{ font-size: 34pt; string-set: booktitle content(); margin-top: 1.2in; }}
.cover .subtitle {{ font-size: 17pt; font-weight: 600; color: {track}; margin: 0.15in 0 0.6in; }}
.cover svg {{ width: 100%; height: auto; }}
.toc {{ break-after: page; }}
.toc ol {{ list-style: none; padding: 0; max-width: 5.7in; }}
.toc li {{ margin: 0 0 0.35em; }}
.toc a {{ color: {c['ink']}; text-decoration: none; }}
.toc a::after {{ content: leader('.') target-counter(attr(href), page); }}
.chapter {{ break-before: page; }}
.opener {{ background: {track}; color: {c['paper']}; padding: 0.3in 0.35in 0.35in; margin: 0 0 0.35in; }}
.opener h1 {{ color: {c['paper']}; margin-top: 0.25in; }}
.opener svg.stops {{ width: 4.6in; height: auto; }}
.callout {{ padding: 0.12in 0.2in 0.05in; margin: 0.25in 0; break-inside: avoid; max-width: 5.7in; }}
.callout h2 {{ margin-top: 0.1em; }}
.checkpoint {{ background: {c['signal']}; }}
.practice {{ background: {c['surface']}; }}
"""


def build(manifest_path, out_dir):
    manifest = tomllib.loads(manifest_path.read_text(encoding="utf-8"))
    book = manifest["book"]
    c = load_tokens()["light"]
    track = c["track"][book["track"]]
    chapters = []
    for entry in manifest.get("chapter", []):
        path = (ROOT / (entry.get("lesson") or entry["file"])).resolve()
        meta, markdown = learner_part(path)
        chapters.append({"id": str(meta.get("id", "")), "lesson": "lesson" in entry, "markdown": markdown})
    labels = [ch["id"] for ch in chapters if ch["lesson"]]

    parts, toc, lesson_index = [], [], 0
    for number, chapter in enumerate(chapters, 1):
        rendered = MD.render(chapter["markdown"])
        heading = re.search(r"<h1>(.*?)</h1>", rendered, re.S)
        title = heading.group(1) if heading else f"Chapitre {number}"
        rendered = rendered.replace(heading.group(0), "", 1) if heading else rendered
        toc.append(f'<li><a href="#ch-{number}">{title}</a></li>')
        opener = f'<h1>{title}</h1>'
        if chapter["lesson"]:
            lesson_index += 1
            opener = stop_map(labels, lesson_index, c["paper"], c["paper"], track) + opener
        parts.append(f'<section class="chapter" id="ch-{number}"><div class="opener">{opener}</div>'
                     f'{wrap_callouts(rendered)}</section>')

    cover_map = ""
    if book.get("program_map", True):
        cover_map = (ROOT / "assets/readme/program-map-light.svg").read_text(encoding="utf-8")
    document = (f'<!DOCTYPE html><html lang="{book.get("lang", "fr-CA")}"><head><meta charset="utf-8">'
                f'<title>{html.escape(book["title"])}</title><style>{stylesheet(c, track)}</style></head><body>'
                f'<section class="cover"><h1>{html.escape(book["title"])}</h1>'
                f'<p class="subtitle">{html.escape(book.get("subtitle", ""))}</p>{cover_map}</section>'
                f'<nav class="toc"><h2>Table des matières</h2><ol>{"".join(toc)}</ol></nav>'
                f'{"".join(parts)}</body></html>')

    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{manifest_path.parent.name if manifest_path.name == 'book.toml' else manifest_path.stem}.pdf"
    page = HTML(string=document, base_url=str(ROOT))
    try:
        page.write_pdf(target, pdf_variant="pdf/ua-1")
        variant = "PDF/UA-1"
    except Exception as error:  # a document that cannot meet PDF/UA is still built, and the reason is reported
        page.write_pdf(target)
        variant = f"plain PDF (PDF/UA-1 failed: {error})"
    print(target)
    print(f"{len(chapters)} chapters, {variant}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--out", type=Path, default=ROOT / "build" / "books")
    args = parser.parse_args()
    build(args.manifest, args.out)


if __name__ == "__main__":
    main()
