---
name: slop-check
description: Check a deliverable, text or visual, for patterns that mark it as machine-made, against DESIGN.md section 11 and the pinned anti-slop catalogue. Use before reporting any lesson, handout, workshop pack, deck, textbook page, diagram or README change as done, or when asked whether text or a visual looks generated. Not for writing new content, and not for typography alone (canadian-french).
---

# Slop check

A filter, not a style guide. `DESIGN.md` gives the direction; this skill finds what departs from it in ways that read as machine-made.

## Sources, in this order

1. **`DESIGN.md` section 11:** the named patterns V1 to V26 (visual) and T1 to T21 (text, in English and French). Always read it.
2. **[fr-patterns.md](references/fr-patterns.md):** more French examples and detection hints, keyed to the T numbers.
3. **Pinned upstream catalogue** in `references/upstream/`: miqdadbadjuber/anti-slop, commit `41b85ede0257f39bfcffedf3f58c3c59bcc8530d`, MIT, files unmodified.
   - For visuals, read `antislop-core.md` lines 129 to 220 (Part 1, warning signs) and 406 to 479 (Purpose-Gate rules).
   - For English text, read `antislop-copywriting.md` lines 21 to 383.
   - Set aside everything else in those files: the "during or after" mode question, the settings file in the home directory, the audit-file location, the install and update instructions, and the web-only rules (R-03, R-24, R-26, R-27, R-32, R-35, R-39, R-40). This repository's deliverables are slides, documents and diagrams, not web interfaces.
   - If `references/upstream/` is missing, check against sources 1 and 2 only, and say so in the report.

## Procedure

1. **Name the artifact and its language.** French or English text, slide images, page images, an SVG, or the README.
2. **Text pass.** Read the whole text once for meaning, then scan for each T pattern.
   - Mark clusters: one isolated tell is weak evidence, and several together are strong.
   - Apply "what not to flag": polished grammar, a single "however", one short emphatic sentence.
3. **Visual pass.** You need images.
   - Render decks and pages with the `publish` skill, and SVGs as `visual-design` explains.
   - Look at each image fresh, not at the code that made it, and scan for each V pattern.
   - Check every coloured element: it must carry a label and serve a function in `DESIGN.md`.
4. **Direction check.** Confirm the artifact still matches the dials (ENERGY 1, RHYTHM 2, MOTION 1), uses a single track colour (the program map excepted), and keeps the stop map as its identity motif.
5. **Report** every finding as a row: location (file and line, or slide and page number) | pattern ID | evidence (the exact words or the element) | proposed fix.
6. **Fix within the task.** A fix removes or rewrites the pattern. It never adds a fact, a number, a name or a source that was not already there. If the fix needs information that is missing, report it instead.

## What is not slop here

These are deliberate choices in `DESIGN.md`, not patterns to flag:

- the signal-yellow checkpoint band;
- numbered steps on an exercise slide, because they are a real sequence;
- the program map's several colours;
- the near-black ink;
- a recap with up to four statements, when the card asks for takeaways.

A requested pattern that `DESIGN.md` does not allow goes to the author: name it, name the rule, and ask.

## Acceptance check

- [ ] Every finding has a location, a pattern ID, its evidence and a proposed fix.
- [ ] Clusters are identified, and isolated hits are judged in context.
- [ ] No fix adds information that was not in the source.
- [ ] The report says which sources were used, and whether the upstream files were present.
- [ ] The visual pass was made on rendered images, never only on source code.
