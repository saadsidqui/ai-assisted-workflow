# Layouts

Numbers derived from `DESIGN.md` section 4.1 for a 16:9 slide of 13.333 × 7.5 in. Positions are in inches from the top-left corner. If `DESIGN.md` changes, recompute them from it. `DESIGN.md` wins over this file.

## Grid

- Left and right margins: 0.6. Top and bottom margins: 0.5.
- Content width: 13.333 − 1.2 = 12.133.
- 12 columns with 11 gutters of 0.25: column width (12.133 − 2.75) ÷ 12 ≈ 0.782.
- Column *n* (1 to 12) starts at x = 0.6 + (n − 1) × 1.032.

## Fixed zones

| Zone | x | y | Width | Height | Notes |
|---|---|---|---|---|---|
| Stop map | column 8 (x ≈ 7.82) | 0.5 | 5 columns (≈ 4.91) | 0.7 | 4 pt line; stop labels in `ink`, 18 pt SemiBold |
| Title | 0.6 | 1.3 | 9 columns (≈ 9.04) | 1.3 | 40 pt Bold, at most 2 lines |
| Body | 0.6 | 2.8 | 12 columns (12.133) | 3.9 | 28 pt; at most 4 short lines, or one diagram |
| Slide number | right edge at 12.733 | 6.75 | 0.8 | 0.3 | `muted`, 18 pt, right-aligned |

## Slide types

| Type | Layout |
|---|---|
| `title` | No stop map zone. Title at y 1.6, 44 pt. Subtitle under it at 28 pt. Full route map across y 4.4 to 5.6. Date at y 6.2 in `muted` |
| `section` | Full-bleed track-colour background. Title in `paper`, 44 pt, at y 2.6. Route map in `paper` across y 4.6 to 5.4, with the arriving stop marked |
| `concept` | Standard title and body zones. A diagram takes the whole body zone |
| `example` | Title zone, then a `surface` panel at x 0.6, y 2.7, width 12.133, height 3.9. The excerpt sits inside with 0.3 padding, at ≥ 22 pt. Up to two annotations in `muted` to the right, inside the panel |
| `checkpoint` | Stop map zone. `signal` band full width, y 2.2 to 5.4. Label "Point de contrôle" at 20 pt SemiBold at y 2.5, question at 36 pt below it, both in `ink`, from x 0.6 |
| `exercise` | Title zone. Numbered steps in columns 1 to 7, each step with its minutes. Timer area in columns 9 to 12 (an empty frame in `rule`, 1 pt) |
| `recap` | Title zone. Route map across y 2.8 to 3.4, every stop filled. Up to four statements under their stops, y 3.8 to 6.4, 24 pt |

## Pages

- **Textbook:** US Letter, 8.5 × 11 in. Margins: inner 1.0, outer 0.8, top 0.8, bottom 0.9. Text block width 6.7.
- **Chapter opener:** track-colour field from the top of the page to y 3.7.
- **Handout:** US Letter, margins 0.6. Small stop map at top right, 2.2 wide.
