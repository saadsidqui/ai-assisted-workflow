---
name: visual-design
description: Design or review a visual from DESIGN.md. Covers slide layouts, SVG diagrams, README images in light and dark, handout and textbook page design, colour choice and contrast. Use when creating or changing a diagram or image, choosing the layout for a slide type, deciding a page design, or checking contrast. Not for building a whole deck or textbook (publish) or for checking text (slop-check, canadian-french).
---

# Visual design

Every visual applies `DESIGN.md`. The direction is Wayfinding: the program drawn as a transit map, colour that identifies rather than decorates, the stop map as the identity motif, and no ornament without a function.

## Inputs

- `DESIGN.md` sections 1 to 6, 10 and 11.1. Its TOML block is the source of the colour tokens.
- [layouts.md](references/layouts.md): the slide grid and the slide types, as numbers.
- [render.md](references/render.md): how to render SVGs, decks and PDFs to images, and how to compute contrast.
- The artifact's track (from `.ai/project/spec/module-map.md`), which sets its single track colour.

## Procedure

1. **Name the job.** What must the reader understand or do after seeing the visual? If a sentence does that better, write the sentence and stop.
2. **Choose the form** from `DESIGN.md` section 5.1: line map, flow, simple table, two-axis sort.
   - At most 7 nodes, square corners, 3 pt strokes, solid arrowheads.
   - In SVG, size arrowheads with `markerUnits="userSpaceOnUse"`, so that they do not grow with the stroke width and crowd the labels.
   - A text label on every node and on every coloured line.
3. **Choose colour and theme.**
   - Colours are `ink` and `rule`, plus the artifact's one track colour. Signal yellow only for a checkpoint.
   - README images need a light variant and a dark variant, each with its own opaque background (`#FFFFFF` and `#0D1117`).
   - Slides and pages need the light theme; the dark deck theme is optional.
4. **Draw** as SVG in `assets/diagrams/<module ID>-<slug>.svg`, or `assets/readme/` for README images.
   - Text stays text, in sentence case, using the font stack from `DESIGN.md` section 3.2.
   - Set fonts with the attributes `font-family`, `font-size` and `font-weight` on the text elements, not with the CSS `font:` shorthand. LibreOffice's SVG import ignores the shorthand, so previews and builds would use the wrong face.
   - Leave at least 20 % horizontal slack, so a substituted font still fits.
   - Add `<title>`, `<desc>`, `role="img"` and `aria-labelledby`.
5. **Compute contrast** for every pair of text and background, and of mark and background, as described in `render.md`. Targets: text ≥ 7:1 for body, ≥ 4.5:1 for other text, ≥ 3:1 for meaningful marks.
6. **Render and look.** Render to PNG (`render.md`), then open the image and look at it as a reader would, not at the source.
   - Look for overlap, clipping, crowding, labels that are too small, and colour as the only cue.
   - Check both themes, on the backgrounds they will appear on.
7. **Write the alt text:** what the visual shows and what it means, in the artifact's language.
8. **Run the `slop-check` visual pass** on the rendered image.

## Slide and page design

- **Slide type:** pick it from `DESIGN.md` section 4.2, and use the positions in `layouts.md`.
- **Slide content:** one idea per slide. A slide that needs more space becomes two slides, never a smaller font.
- **Pages** follow `DESIGN.md` section 6. Callouts are filled boxes; never put a stripe on one edge.

## Acceptance check

- [ ] The form, node count, strokes and labels follow `DESIGN.md` section 5.1.
- [ ] Only `ink`, `rule`, one track colour and, for a checkpoint, `signal` are used. The program map is the only exception.
- [ ] Every contrast pair meets its target. Report the ratios.
- [ ] A rendered image was inspected in each theme the visual ships in, on its real background.
- [ ] Alt text is written. The SVG has `<title>` and `<desc>`.
- [ ] The `slop-check` visual pass found no V pattern, or each hit was resolved.
