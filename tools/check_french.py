#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Saad Sidqui
"""Run the typography checks F1 to F21 on the French prose of Markdown files.

The patterns are read from .claude/skills/canadian-french/references/typography-checks.md,
which stays their single source. Every hit is a candidate to read in context.

Usage:
    python3 tools/check_french.py FILE [...] [--from-marker TEXT]

--from-marker starts the scan after the first line containing TEXT, for example
the French half of README.md: --from-marker '<a id="francais"></a>'.
Exits with status 1 if any hit is found.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCE = ROOT / ".claude/skills/canadian-french/references/typography-checks.md"
ROW_RE = re.compile(r"^\| (F\d+) \| (.+?) \| (.+?) \| .+? \| .+? \|$")
ALLOWED_IN_TABLES = {"F8", "F13", "F21"}      # schedules, identifiers and numeric dates may sit in tables
HEADINGS_ONLY = {"F15", "F16"}
NOT_IN_REVERIFY = {"F11"}                      # version numbers are allowed in the re-verify list
REVERIFY_HEADING = "À revérifier avant chaque prestation"


def load_patterns():
    patterns = {}
    for line in REFERENCE.read_text(encoding="utf-8").splitlines():
        match = ROW_RE.match(line)
        if not match:
            continue
        fid, label, cell = match.groups()
        compiled = []
        for code in re.findall(r"`([^`]+)`", cell):
            try:
                compiled.append(re.compile(code, re.M))
            except re.error:
                pass
        patterns[fid] = (label, compiled)
    return patterns


def clean(line):
    """Keep the prose of one Markdown line: drop code spans, URLs, link targets and HTML tags."""
    line = re.sub(r"`[^`]*`", " ", line)
    line = re.sub(r"<img\b[^>]*\balt=\"([^\"]*)\"[^>]*>", r" \1 ", line)
    line = re.sub(r"<[^>]+>", " ", line)
    line = re.sub(r"\]\([^)]*\)", "]", line)
    line = re.sub(r"https?://\S+", " ", line)
    return line


def prose_lines(text, marker):
    started = marker is None
    in_front = in_code = in_comment = False
    under_reverify = False
    for number, raw in enumerate(text.splitlines(), 1):
        if not started:
            started = marker in raw
            continue
        if number == 1 and raw == "---":
            in_front = True
            continue
        if in_front:
            in_front = raw != "---"
            continue
        if raw.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        line = raw
        if in_comment:
            if "-->" not in line:
                continue
            line, in_comment = line.split("-->", 1)[1], False
        line = re.sub(r"<!--.*?-->", " ", line)
        if "<!--" in line:
            line, in_comment = line.split("<!--", 1)[0], True
        if raw.startswith("## "):
            under_reverify = raw[3:].strip() == REVERIFY_HEADING
        yield number, raw, clean(line), raw.startswith("|"), raw.startswith("#"), under_reverify


def title_case(heading):
    words = re.findall(r"[A-Za-zÀ-ÿ’'-]+", heading.lstrip("#").strip())
    later = [w for w in words[1:] if len(w) > 1 and not w.isupper()]
    return sum(1 for w in later if w[0].isupper()) >= 2


def scan(path, patterns, marker):
    hits = []
    for number, raw, line, in_table, is_heading, under_reverify in prose_lines(path.read_text(encoding="utf-8"), marker):
        for fid, (label, compiled) in patterns.items():
            if fid in HEADINGS_ONLY and not is_heading:
                continue
            if fid in ALLOWED_IN_TABLES and in_table:
                continue
            if fid in NOT_IN_REVERIFY and under_reverify:
                continue
            if fid == "F16":
                if title_case(raw):
                    hits.append((number, fid, label, raw.strip()))
                continue
            target = raw if fid == "F15" else line
            spans = []
            for rx in compiled:
                for m in rx.finditer(target):
                    if any(m.start() < end and start < m.end() for start, end in spans):
                        continue  # one error matched by two patterns of the same check
                    spans.append(m.span())
                    hits.append((number, fid, label, m.group(0)))
    return hits


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--from-marker", default=None)
    args = parser.parse_args()
    patterns = load_patterns()
    total = 0
    for path in args.files:
        hits = scan(path, patterns, args.from_marker)
        total += len(hits)
        print(f"== {path}: {len(hits)} hit(s), {len(patterns)} checks loaded from {REFERENCE.relative_to(ROOT)}")
        for number, fid, label, found in hits:
            print(f"{path}:{number}: {fid} {label}: {found!r}")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
