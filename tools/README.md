# Tools

Scripts that check and build the deliverables. Every script is licensed under MIT (`SPDX-License-Identifier: MIT`, text in `LICENSES/MIT.txt`). Output goes to `build/`, which git ignores.

## Setup

The author installs the Python dependencies, once, from the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r tools/requirements.txt
```

The versions are pinned in `tools/requirements.txt`, and the resolved set is in `tools/requirements.lock`. Previews also need LibreOffice (`soffice`) and Poppler (`pdftoppm`).

## Checkers

| Script | What it checks | Run with |
|---|---|---|
| `check_lesson.py` | A lesson against `templates/lesson.md`: front matter, sections, slide regions and notes, timing table and marks, notes budget (110 words per minute of talk, ±15 %) | `.venv/bin/python tools/check_lesson.py lessons/…/X-00-….md` |
| `check_french.py` | Typography checks F1 to F22 on French prose. The patterns are read from the `canadian-french` skill's `typography-checks.md` | `python3 tools/check_french.py FILE [--from-marker TEXT]` |
| `check_contrast.py` | WCAG contrast of every token pair in `DESIGN.md`, or of any two colours | `python3 tools/check_contrast.py --tokens`, or `python3 tools/check_contrast.py ink surface` |

Every checker exits with status 1 when something fails, so it can gate a step.

## Previews

`render_preview.py` turns SVG, PPTX, ODP and PDF files into PNG images in `build/preview/`, using LibreOffice and Poppler with the repository's fonts. Look at every image before reporting a visual deliverable as done.

```bash
python3 tools/render_preview.py assets/readme/program-map-light.svg
```

## Builders

| Script | What it builds | Run with |
|---|---|---|
| `build_deck.py` | A PowerPoint deck from `decks/SESSION.toml`: title, section, concept, example, checkpoint, exercise and recap slides, a stop map, speaker notes. Fonts follow `DESIGN.md` section 3.2 | `.venv/bin/python tools/build_deck.py decks/SESSION.toml [--theme dark]` |
| `build_book.py` | A PDF textbook (PDF/UA-1) from `books/BOOK/book.toml`: cover, table of contents, chapter openers, embedded fonts, learner text only | `.venv/bin/python tools/build_book.py books/BOOK/book.toml` |

The manifest formats and the full procedure are in the `publish` skill (`.claude/skills/publish/SKILL.md`).
