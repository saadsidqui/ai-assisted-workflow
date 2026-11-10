---
name: publish
description: Build a PowerPoint deck or a PDF textbook from lessons and a manifest, then render and inspect every slide or page. Use when asked for a deck, slides, a textbook, a PDF, or a preview of a built output, and when writing or checking a manifest in decks/ or books/. Not for writing lesson content (lesson-writing) or designing a single diagram (visual-design).
---

# Publish

Decks and textbooks are built on demand from the lessons. They go to `build/`, which git ignores. They are never committed; the author attaches them to a release.

## Manifests

Deck, `decks/SESSION.toml`:

```toml
[deck]
title = "…"            # French, shown on the title slide
subtitle = "…"
track = "core"         # core | engineering | product-experience | business-people
theme = "light"        # light | dark (dark is for dim rooms)
date = "10 novembre 2026"
stops = ["…", "…"]     # one label per session segment, shown in the stop map

[[part]]               # one per lesson, in session order
lesson = "lessons/core/C-01-mental-model-and-vocabulary.md"
stop = 2               # which stop of `stops` this lesson is (1-based)
```

Textbook, `books/BOOK/book.toml` (BOOK: core, engineering, product-experience, business-people):

```toml
[book]
title = "…"
subtitle = "…"
track = "core"
lang = "fr-CA"
program_map = true     # program map on the cover

[[chapter]]            # in reading order; `lesson` for lessons, `file` for front or back matter
lesson = "lessons/core/C-01-mental-model-and-vocabulary.md"
```

Chapter membership follows `.ai/project/spec/module-map.md`. Whether track books include the core is OD-08.

## Procedure

1. **Check the manifest:**
   - every path exists;
   - deck stops match the session's segments (S-01 or the track page);
   - book chapters match the module map.
2. **Check every lesson** it lists, with `tools/check_lesson.py` and `tools/check_french.py`. Fix or report a failing lesson before building; never build around it.
3. **Build:**
   - deck: `.venv/bin/python tools/build_deck.py decks/SESSION.toml`
   - textbook: `.venv/bin/python tools/build_book.py books/BOOK/book.toml`
4. **Warnings:** fix each word-limit warning in the lesson, or report it.
5. **Render:** `python3 tools/render_preview.py build/decks/SESSION.pptx` (or the PDF).
6. **Inspect every image.** Look for:
   - overflow, clipping and overlap;
   - margins;
   - that the stop map marks the right stop;
   - shadows or edge stripes;
   - contrast.

   For PDFs, also check:
   - the table of contents' page numbers;
   - the running heads;
   - that no speaker notes or slides leaked in;
   - that `pdffonts` shows every font embedded.

   Then run the `slop-check` visual pass on the images.
7. **Report:**
   - output paths, and slide or page counts;
   - notes coverage (the deck builder prints it);
   - warnings and inspection findings;
   - what is left for the author: a PowerPoint check, and the release.

## Rules

- **Fonts:** `DESIGN.md` section 3.2 decides them. Decks use Arial by default, which renders as Liberation Sans in LibreOffice.
- **Generated files:** never edit a `.pptx` or `.pdf` by hand. Fix the lesson or the builder.
- **Git:** never commit outputs, and never create releases or tags.
- **Other skills:** account-level document skills are not used (`CLAUDE.md`).

## Acceptance check

- [ ] Every lesson in the manifest passed both checkers before the build.
- [ ] The build ran, every slide carries notes (the title slide excepted), and the warnings are resolved or reported.
- [ ] Every rendered slide or page image was inspected; findings are listed.
- [ ] For PDFs, every font is embedded, and no slide region, speaker note, timing table or re-verify list appears.
- [ ] Outputs are only in `build/`.
