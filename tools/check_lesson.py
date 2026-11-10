#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Saad Sidqui
"""Check lesson files against templates/lesson.md and the lesson-writing acceptance check.

Usage:
    .venv/bin/python tools/check_lesson.py lessons/core/C-01-mental-model-and-vocabulary.md [...]

Prints one PASS, WARN or FAIL line per check. Exits with status 1 if any check fails.
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SLIDE_TYPES = {"title", "section", "concept", "example", "checkpoint", "exercise", "recap"}
FRONT_KEYS = ["id", "title", "card", "track", "minutes", "status", "last_verified", "native_review", "glossary"]
TRACKS = {"core", "engineering", "product-experience", "business-people", "overlays"}
STATUSES = {"draft", "review", "ready"}
REQUIRED_SECTIONS = ["Objectifs", "Déroulement", "Point de contrôle", "Récapitulatif",
                     "Pour aller plus loin", "À revérifier avant chaque prestation"]
WORDS_PER_MINUTE = 110
TOLERANCE = 0.15

FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
SLIDE_RE = re.compile(r"<!-- slide: (\w+) -->\n(.*?)<!-- /slide -->", re.S)
NOTES_RE = re.compile(r"<details><summary>Notes de présentation</summary>\n\n(.*?)\n\n</details>", re.S)
MARK_RE = re.compile(r"^\[(\d+(?:,\d+)?) min\]")
ROW_RE = re.compile(r"^\| (?P<step>[^|]+?) \| (?P<minutes>\d+(?:,\d+)?) \|", re.M)
WORD_RE = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿŒœ’'-]+")


def number(text):
    return float(text.replace(",", "."))


def spoken_words(notes):
    """Count the words a presenter says: stage directions in square brackets are left out."""
    return len(WORD_RE.findall(re.sub(r"\[[^\]]*\]", " ", notes)))


def section(body, title):
    match = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return match.group(1) if match else None


def check(path):
    results = []
    ok = lambda cond, msg, level="FAIL": results.append(("PASS" if cond else level, msg))
    text = path.read_text(encoding="utf-8")

    front = FRONT_RE.match(text)
    ok(front is not None, "front matter present")
    if not front:
        return results
    meta = yaml.safe_load(front.group(1)) or {}
    body = text[front.end():]
    missing = [k for k in FRONT_KEYS if k not in meta]
    ok(not missing, f"front matter keys complete{': missing ' + ', '.join(missing) if missing else ''}")
    ok(str(meta.get("id", "")) and path.name.startswith(f"{meta.get('id')}-"), f"id {meta.get('id')!r} matches the file name")
    ok(meta.get("track") in TRACKS, f"track {meta.get('track')!r} is one of {sorted(TRACKS)}")
    ok(meta.get("status") in STATUSES, f"status {meta.get('status')!r} is one of {sorted(STATUSES)}")
    card = ROOT / str(meta.get("card", ""))
    ok(card.is_file(), f"card {meta.get('card')!r} exists")
    review = str(meta.get("native_review", ""))
    ok(review == "pending" or re.fullmatch(r"done \d{4}-\d{2}-\d{2}", review), f"native_review {review!r} is 'pending' or 'done YYYY-MM-DD'")
    minutes = meta.get("minutes")
    ok(isinstance(minutes, (int, float)) and minutes > 0, f"minutes {minutes!r} is a positive number")
    minutes = float(minutes) if isinstance(minutes, (int, float)) else 0.0

    h1 = re.search(r"^# (.+)$", body, re.M)
    ok(h1 is not None, "lesson title (H1) present")
    if h1:
        ok(not re.search(r"\b[CEPBXST]-\d", h1.group(1)), "lesson title carries no module ID")
    ok("<!-- GUIDE" not in text, f"no GUIDE comment left ({text.count('<!-- GUIDE')} found)")
    for title in REQUIRED_SECTIONS:
        ok(section(body, title) is not None, f"section '{title}' present")
    ok(section(body, "Pratique") is not None, "section 'Pratique' present (only if the card has practice)", level="WARN")

    opens, closes = body.count("<!-- slide: "), body.count("<!-- /slide -->")
    ok(opens == closes and opens > 0, f"slide regions balanced ({opens} open, {closes} close)")
    marks, words = [], 0
    for kind, inner in SLIDE_RE.findall(body):
        ok(kind in SLIDE_TYPES, f"slide type {kind!r} is known")
        heading = re.search(r"^### (.+)$", inner, re.M)
        ok(heading is not None, f"{kind} slide has a ### heading")
        notes = NOTES_RE.search(inner)
        ok(notes is not None, f"{kind} slide has a notes block")
        if notes:
            mark = MARK_RE.match(notes.group(1).strip())
            ok(mark is not None, f"{kind} slide notes start with a timing mark")
            if mark:
                marks.append(number(mark.group(1)))
            words += spoken_words(notes.group(1))

    timing = section(body, "Déroulement") or ""
    rows = {m.group("step").strip(): number(m.group("minutes")) for m in ROW_RE.finditer(timing)}
    total_row = rows.pop("**Total**", None)
    ok("Point de contrôle" in rows, "timing table has its own checkpoint row")
    ok(total_row == minutes, f"timing table total {total_row} equals minutes {minutes}")
    ok(abs(sum(rows.values()) - minutes) < 1e-9, f"timing table rows add up to {sum(rows.values())} (minutes {minutes})")
    ok(abs(sum(marks) - minutes) < 1e-9, f"timing marks add up to {sum(marks)} (minutes {minutes})")

    talk = minutes - rows.get("Point de contrôle", 0) - rows.get("Pratique", 0)
    target = WORDS_PER_MINUTE * talk
    low, high = target * (1 - TOLERANCE), target * (1 + TOLERANCE)
    ok(low <= words <= high, f"spoken words in notes: {words}, target {target:.0f} for {talk:g} talk minutes (range {low:.0f} to {high:.0f})")
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("lessons", nargs="+", type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.lessons:
        print(f"== {path}")
        for level, message in check(path):
            print(f"{level:4s}  {message}")
            failed |= level == "FAIL"
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
