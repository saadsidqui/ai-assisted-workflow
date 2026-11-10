# 0003. Visual direction: Wayfinding

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

Slides, handouts, textbooks and the README need one visual direction that the pattern checks can filter against. Three directions were offered: Wayfinding, Red pencil and Poster.

## Decision

1. **Wayfinding.** The program is drawn as a transit map: the core is the trunk, the tracks are lines, the overlays are connections. Each slide shows where the audience is. Colour identifies; it never decorates.
2. **Typeface:** Atkinson Hyperlegible Next, with Atkinson Hyperlegible Mono.
3. **Track identification:** each track has one colour. A stop map, drawn in the track colour, and the track name identify the track. There is no coloured edge stripe on slides. That stripe is a catalogued machine-made pattern.
4. **Dark variant:** there is one, used for README images on dark themes and for an optional dark deck theme for dim rooms. PDFs and handouts are light only.
5. **Where the values live:** `DESIGN.md` holds the tokens, the computed contrast ratios and the rules.

## Consequences

- Each artifact uses a single track colour, which keeps every slide within a small palette.
- Fonts that cannot be installed on a presenter's machine must be embedded or replaced by a metric-compatible pair. Phase 3 of initialization tests which.
- Red pencil and Poster are not used.
