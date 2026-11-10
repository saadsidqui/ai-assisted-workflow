# DESIGN.md

The design direction for everything a learner or reader sees: slides, handouts, lessons, textbooks and the README. The checks for machine-made patterns filter against this file. Decision 0003 chose the direction; this file makes it specific.

## 1. Principles

- **Wayfinding.** The program is drawn as a transit map. The common core is the trunk, each track is a line, and the overlays are connections. Every slide, chapter and handout shows where the reader is on the line.
- **Colour identifies; it never decorates.** Each artifact uses exactly one track colour. Signal yellow marks checkpoints and nothing else. Colour is never the only cue: every coloured element also carries a text label.
- **One idea per slide, one idea per paragraph.** The words do the work; the layout gives them room.
- **Plain and exact.** No ornament without a function. When a choice has no reason that fits in one line, it goes.
- **Dials** (in the terms of the anti-slop catalogue): ENERGY 1, RHYTHM 2, MOTION 1. The layouts are calm and vary with the content, and nothing moves.
- **Design read:** training slides and study books for a mixed workplace audience, in a wayfinding and signage visual language, with the dials above.
- **Identity motif:** the stop map, a line in the track colour with one stop per segment or chapter.

## 2. Colour

### 2.1 Tokens

The TOML block below is the single source for the tools in `tools/`; the tables restate the same values. Ratios use the WCAG 2.x relative-luminance formula and were computed by script on 2026-11-10.

```toml
[color.light]
paper = "#FFFFFF"
surface = "#F1F3F6"
ink = "#15181D"
muted = "#4D5562"
rule = "#808896"
signal = "#F2C200"

[color.light.track]
core = "#0B5CAD"
engineering = "#00735A"
product-experience = "#B04A00"
business-people = "#9B3F78"

[color.dark]
paper = "#14171C"
surface = "#1E232A"
ink = "#ECEFF3"
muted = "#A9B1BD"
rule = "#6B7380"
signal = "#F2C200"

[color.dark.track]
core = "#6AA6F0"
engineering = "#3CC29C"
product-experience = "#F59A5E"
business-people = "#E08DC0"
```

Light theme (default for slides; the only theme for handouts and textbooks):

| Token | Hex | On paper | On surface | Use |
|---|---|---|---|---|
| `paper` | `#FFFFFF` | n/a | n/a | Background |
| `surface` | `#F1F3F6` | n/a | n/a | Panels: example artifacts, practice and re-verify boxes |
| `ink` | `#15181D` | 17.79 | 16.01 | All body text and titles |
| `muted` | `#4D5562` | 7.52 | 6.77 | Secondary text: captions, labels, slide numbers, running heads |
| `rule` | `#808896` | 3.57 | 3.21 | Lines and box outlines only, never text |
| `signal` | `#F2C200` | fill | fill | Checkpoint fill; `ink` on it: 10.58 |
| `core` | `#0B5CAD` | 6.67 | 6.00 | Core line; `paper` text on it: 6.67 |
| `engineering` | `#00735A` | 5.83 | 5.25 | Engineering line; `paper` text on it: 5.83 |
| `product-experience` | `#B04A00` | 5.49 | 4.94 | Product and experience line; `paper` text on it: 5.49 |
| `business-people` | `#9B3F78` | 6.22 | 5.60 | Business and people line; `paper` text on it: 6.22 |

Dark theme (README images on dark pages; optional deck theme for dim rooms):

| Token | Hex | On paper | On surface | Use |
|---|---|---|---|---|
| `paper` | `#14171C` | n/a | n/a | Background |
| `surface` | `#1E232A` | n/a | n/a | Panels |
| `ink` | `#ECEFF3` | 15.57 | 13.70 | Body text and titles |
| `muted` | `#A9B1BD` | 8.31 | 7.31 | Secondary text |
| `rule` | `#6B7380` | 3.75 | 3.30 | Lines and outlines only |
| `signal` | `#F2C200` | fill | fill | Checkpoint fill; dark `paper` as text on it: 10.69 |
| `core` | `#6AA6F0` | 7.12 | 6.26 | Dark `paper` text on it: 7.12 |
| `engineering` | `#3CC29C` | 8.03 | 7.06 | Dark `paper` text on it: 8.03 |
| `product-experience` | `#F59A5E` | 8.27 | 7.27 | Dark `paper` text on it: 8.27 |
| `business-people` | `#E08DC0` | 7.48 | 6.58 | Dark `paper` text on it: 7.48 |

On GitHub's page backgrounds, the light tokens sit on `#FFFFFF` (as above). The dark tokens sit on `#0D1117`: `ink` 16.41, `muted` 8.75, `core` 7.50, `engineering` 8.46, `product-experience` 8.71, `business-people` 7.88, `rule` 3.96.

The track hues are derived from the Okabe–Ito colour-blind-safe set and darkened (light theme) or lightened (dark theme) until they meet the targets below.

### 2.2 Targets and rules

- Body text and titles: at least 7:1 against their background.
- Any other text, including coloured text at large sizes: at least 4.5:1.
- Lines, outlines and diagram marks that carry meaning: at least 3:1.
- One track colour per artifact.
  - A common-session deck uses `core`.
  - A track deck, handout or textbook uses its track's colour.
  - An overlay takes the colour of the session or book it appears in.
  - The one exception is the program map in the README and in textbook front matter. It shows the whole network, so each line keeps its own colour.
- The track colour appears on these elements, with no others:
  - the stop map;
  - section and chapter-opener fields;
  - diagram lines;
  - at most one emphasized label per slide.
- Signal yellow fills checkpoint bands and checkpoint boxes and nothing else.
- The ink is a near-black (`#15181D`), not pure black. It softens the glare of black on white on a projector, and keeps 17.79:1.

## 3. Typography

### 3.1 Families

| Role | Family | Licence | Notes |
|---|---|---|---|
| Everything | Atkinson Hyperlegible Next | SIL Open Font License 1.1 (confirmed from `OFL.txt`, 2026-11-10) | Designed for legibility; distinct forms for easily confused characters |
| Code, commands, file names | Atkinson Hyperlegible Mono | Same | Same skeleton as the text face |

- **Weights:** Regular (400) for text, SemiBold (600) for headings and labels, Bold (700) for slide and chapter titles.
- **Italic:** for titles of works and for an English term at first mention where the glossary says so. Never for emphasis.
- **Emphasis:** bold, used sparingly for a key word.
- **Files:** in `assets/fonts/`, static weights Regular, Italic, SemiBold and Bold for Next, Regular and Bold for Mono.
- **Coverage, checked on 2026-11-10:** the files cover « », U+00A0, ’, the curly quotes, the dashes, œ and Œ, and every accented letter used in French. They allow installable embedding (fsType 0). They have no U+202F, which this project does not use.

### 3.2 Surviving on a machine where nothing can be installed

- **PDF textbooks and handouts:** the fonts are embedded in every PDF.
- **Decks:** a deck must open with its intended metrics in LibreOffice (the main target) and in PowerPoint, on a machine where no font can be installed. Two candidates, settled by a test in initialization, Phase 3:
  1. Atkinson Hyperlegible Next embedded in the `.pptx`. Adopted only if both applications honour the embedded font.
  2. A metric-compatible pair: the deck names Arial, which LibreOffice renders with Liberation Sans. Adopted if the embedding test fails. It must be confirmed that Liberation Sans ships with LibreOffice installs.
- **README images:** the SVG text uses the stack `"Atkinson Hyperlegible Next", "Atkinson Hyperlegible", Verdana, Arial, sans-serif`. Layouts keep at least 20 % horizontal slack so that a substituted font still fits.

### 3.3 Sizes

| Context | Title | Body | Minimum |
|---|---|---|---|
| Slide (16:9) | 40 pt Bold (44 pt on title and section slides) | 28 pt | 18 pt for anything on a slide, slide numbers included |
| Textbook (US Letter) | Chapter 26 pt; section 17 pt; subsection 13 pt | 11 pt, leading 1.45 | Captions and running heads 9 pt |
| Handout (US Letter) | 20 pt | 11 pt, leading 1.4 | 9 pt |

- Text is aligned left, ragged right, never justified.
- Textbook lines hold at most about 75 characters.
- French hyphenation is on in textbooks and off on slides.

## 4. Slide system

### 4.1 Grid

- **Format:** 16:9, 13.333 × 7.5 in.
- **Grid:** 12 columns, 0.25 in gutters, 0.6 in left and right margins, 0.5 in top and bottom margins.
- **Stop map:** in the top-right zone, within the margins, at most 5 columns wide.
  - It is a 4 pt line in the track colour with one stop per segment of the session.
  - Past stops are filled. Future stops are hollow, with a 3 pt outline.
  - The current stop is larger and filled, with its label beneath it in `ink`, 18 pt SemiBold.
- **Slide number:** bottom right, `muted`, 18 pt.
- **Nothing else on the slide frame:** no logo, no footer bar, no decorative furniture.
- **Backgrounds:** light theme by default. The dark theme swaps the tokens and changes nothing else.

### 4.2 Slide types

| Type | Layout | Word limit |
|---|---|---|
| `title` | `paper` background. The session's full route map runs across the lower half. Session title at 44 pt, subtitle at 28 pt, date in full | Title ≤ 10 words |
| `section` | Full-bleed track-colour field. Title in `paper` at 44 pt. The route map in `paper`, with the arriving stop marked | Title ≤ 8 words |
| `concept` | Title written as a statement; then either at most 4 short lines or one diagram, never both | Title ≤ 10 words; body ≤ 25 words |
| `example` | Title, then the example artifact in a `surface` panel (an email, a chat turn, a code excerpt, a table) with at most two annotations in `muted` | Excerpt ≤ 60 words at ≥ 22 pt |
| `checkpoint` | Full-width `signal` band across the middle. The label "Point de contrôle" at 20 pt SemiBold, then the question at 36 pt in `ink` | Question ≤ 20 words |
| `exercise` | Numbered steps, each with its minutes, because they are a real sequence. A large area for the timer on the right | ≤ 6 steps, each ≤ 8 words |
| `recap` | The route map with every stop filled; under the stops, at most 4 statements, each tied to the stop it came from | ≤ 4 statements, each ≤ 12 words |

- **One idea per slide.** If a slide needs a second idea, it becomes two slides.
- **Lists on slides:** keyword items take no final punctuation. Items that are full sentences end with a period.
- **Speaker notes** go in the notes pane, never on the slide. A slide never repeats its notes word for word.
- **Common-session deck:** about 30 content slides, 35 at most (from S-01).
- **Motion:** no transitions, no animations, no builds.

## 5. Diagrams and imagery

### 5.1 Diagrams

- **Forms allowed:** a line map (stations on a line), a flow (boxes and arrows), a simple table, a two-axis sort. Nothing three-dimensional, isometric or decorative.
- **Size:** at most 7 nodes. Square corners. Stroke 3 pt at slide scale, with solid arrowheads.
- **Labels:** every node and every coloured line has a text label, in sentence case. A connector is labelled when its meaning is not obvious.
- **Colour:** `ink` and `rule`, plus the artifact's track colour. Signal yellow only for a checkpoint.
- **Source:** an SVG in `assets/diagrams/<module ID>-<slug>.svg`, with the text kept as text. Decks and PDFs use a rendering of it. README images need a light and a dark variant.
- **Alt text:** every diagram has alt text that states what the diagram shows, not what it looks like.

### 5.2 Imagery

- **Photographs:** none by default.
- **Screenshots:** only real, dated (inside C-02 or a "re-verify" list), cropped to what matters, and never edited to show something the product does not do.
- **Never:**
  - generated images of people;
  - stock photographs;
  - imagery that stands for "AI": sparkles, magic wands, robots, brains, glowing orbs, circuit boards;
  - logos of real organizations, other than a public tool named where a card's topics require it.
- **Icons:** none unless an icon carries meaning that a word next to it does not. When in doubt, use the word.

## 6. Documents

- **Textbook pages** (US Letter):
  - Margins: inner 1 in, outer 0.8 in, top 0.8 in, bottom 0.9 in.
  - Running heads: book title on even pages, chapter title on odd pages, in `muted` 9 pt.
  - Page numbers: on the outside at the bottom.
  - Widow and orphan control is on.
- **Chapter opener:** a track-colour field across the top third, with the chapter title in `paper` and a stop map in which the chapter's stop is labelled with its module ID.
- **Callouts:**
  - checkpoint: a `signal` fill with `ink` text;
  - practice: a `surface` fill;
  - "À revérifier": a `surface` fill with a 1 pt `rule` outline on all four sides.
  - Never an edge stripe on a box.
- **Handouts:** a single US Letter page, 0.6 in margins, a small stop map at top right, and no information that exists only in the slides.
- **README:**
  - Images switch between their light and dark variants with `<picture>` and `prefers-color-scheme`.
  - Each variant carries its own opaque background: `#FFFFFF` for light, `#0D1117` for dark. The media query follows the browser's colour preference, which can differ from the GitHub theme, so either variant must stay legible on either page.
  - At most four badges, coloured with the tokens.
  - Headings in sentence case. No emoji.

## 7. Editorial voice for the French deliverables

- **Register:** address participants as « vous ». Use plain language and the active voice. Sentences average 20 words or fewer. One idea per paragraph, and the important word comes first. The OQLF's guidance for slides asks for « simples, affirmatives, rédigées à la voix active » sentences and concise titles.
- **Vocabulary:** concrete verbs and the glossary's terms. Each term has one rendering throughout. Never translate a sentence word for word from English; write it in French.
- **Speaker notes:** the presenter is new to teaching and speaks slowly.
  - Notes are written as full sentences the presenter can say, at about 110 words per planned minute of talk (checkpoint and practice minutes excluded).
  - Stage directions go between square brackets: [Pause], [Passez à la diapositive suivante], [Attendez deux ou trois réponses].
  - Each segment opens with a timing mark, for example [12 min].
  - The transition into each checkpoint is written out word for word.
  - A « Si vous êtes en retard » marker names what to skip.
  - The notes add to the slide; they never read it aloud.
- **Inclusive writing:** follow the OQLF's rédaction épicène.
  - Prefer neutral designations and épicène terms.
  - Use full doublets for determinate persons.
  - Abbreviated doublets appear only in tables or forms, and then with parentheses or brackets.
  - No point médian and no neologisms such as « iel », which the OQLF advises against.

## 8. Pedagogical patterns

Every lesson follows the same sequence, so that a novice presenter always knows what comes next:

1. **Outcome.** What participants will be able to do, taken from the card.
2. **Concept, one idea at a time.** Each idea opens with a concrete example and is named only after the example has been seen.
3. **Example.** The running example of the session wherever it fits, so the room follows one story.
4. **Checkpoint.** One question to the room, a real pause (count slowly to seven before speaking), two or three answers, then a one-sentence recap. The question comes from the card.
5. **Practice.** A short task on synthetic material, with its minutes and its expected result.
6. **Recap.** Participants retrieve the point before the slide shows it: the presenter asks, then confirms. A recap never repeats an earlier slide word for word.

The lesson's timing table lists each checkpoint as its own row (OD-05). Recommended and optional topics go into a reference section at the end, not into the session.

## 9. Canadian French typography and usage

Confirmed on 2026-11-10 against the Banque de dépannage linguistique of the Office québécois de la langue française (Vitrine linguistique). The pages are listed in section 12. In the examples below, every space that must not break is a real non-breaking space (U+00A0).

| Point | Rule | Example | Source |
|---|---|---|---|
| Deux-points | Non-breaking space before, normal space after | Résultat : trois ébauches | 22039 |
| Point-virgule, ! and ? | No space before (the OQLF's choice; a narrow space is allowed but not used here) | Vraiment? Oui; c’est prévu! | 22039 |
| Guillemets | French « » with a non-breaking space inside; a quotation within a quotation uses “ ” then ‘ ’, without spaces | « Vérifiez la source. » | 22039, 23363 |
| Percent | Non-breaking space before % | 8 % | 22039 |
| Money | Symbol after the number, non-breaking space before it; k$ and M$ only in tables | 25,50 $ and 12 M$ (in a table) | 21584, 22039 |
| Large numbers | Groups of three with non-breaking spaces from five digits; four-digit numbers are not grouped (the OQLF leaves this optional; this is the choice made here) | 12 500 and 8000 | 25447 |
| Not grouped | Years, numbers used as identifiers, addresses | en 2026 and 10985, rue des Érables | 25447 |
| Decimal sign | Comma, no space after it, a zero before values under one | 3,5 and 0,6 | 21191 |
| Units | Non-breaking space between number and symbol | 25 cm | 21191, 24566 |
| Time, running text | The symbol h with a space on each side; 24-hour clock; minutes under ten take a zero | 9 h, 14 h 30 and 8 h 05 | 21242, 21516 |
| Time, schedules | An en dash between start and end, with spaces | 8 h 30 – 16 h 30 | 21516, 23376 |
| Time, numeric | The colon form only in technical tables, never in running text | 15:30 (horaire) | 21516 |
| Dates, running text | Day, month in letters, year; non-breaking spaces between them; « le » before the date in running text | le 10 novembre 2026 | 21242, 24566 |
| Dates, numeric | Year-month-day with hyphens, only in tables and forms | 2026-11-10 | 21640 |
| Titles of works | Capital on the first word and on proper nouns only; italics | *Guide du participant* | 21497 |
| Headings and slide titles | No final period; never end with a colon; capitals for a whole heading only if it has 4 or 5 words at most (not used here) | Vérifier avant d’envoyer | 23402, 23326, 24404 |
| Vertical lists | Introduced by a sentence ending in a colon. Items that continue that sentence start in lowercase and end with a semicolon or comma; autonomous items take a capital and a period. Every item starts with the same part of speech. No « et » before the last item | n/a | 25108 |
| Lists on slides | Keyword lists may drop the punctuation; full sentences keep normal punctuation | n/a | 24626, 25108 |
| Acronyms | No periods, capitals, no plural mark; spelled out at first use | les PME and l’IA | 24887, 21136 |
| Dash in running text | Allowed by the OQLF to set off a passage. This project's choice: use commas or parentheses instead, and keep the dash for schedules | n/a | 23378 |
| Inclusive writing | See section 7 | n/a | 23983, 25421 |

Three conventions used here are not stated on the OQLF pages that were read. The author confirmed them on 2026-11-10:

1. In a document's own headings and slide titles, capitals go on the first word and proper nouns only, as for titles of works.
2. Names of months and days take no capital in running text. This matches every OQLF example read.
3. A time range in running text is written « de 9 h à 17 h ». The OQLF example is « De 9 h à 13 h HNE ».

Other choices made here:
- the typographic apostrophe ’ in deliverables;
- « vous » to address participants.

## 10. Accessibility minimums

- **Contrast:** the targets in section 2.2, and never colour as the only carrier of meaning (WCAG 2.2, 1.4.1, 1.4.3, 1.4.6 and 1.4.11).
- **Sizes:** the minimums in section 3.3.
- **Reading order:** in decks, the title is the first object on every slide. Every picture has alt text.
- **Textbooks:** headings form the PDF outline, the document language is set to fr-CA, every image has alt text, and the reading order follows the visual order. Whether the PDF can also be tagged is tested in Phase 3.
- **Handouts:** each one makes sense without the slides, and no learner-facing information lives only in speaker notes.
- **Motion:** nothing moves, blinks or animates.
- **Links:** link text says where it goes; never « cliquez ici ».

## 11. Patterns to avoid

A pattern listed here is removed, or kept only with a written reason that the author has approved. Sources: the brief for this repository; anti-slop (core Part 1, rule numbers R-xx, and the copywriting skill); Anthropic's `frontend-design` and `pptx` skills (section 12).

### 11.1 Visual

| # | Pattern | Why it is out | Catalogued in |
|---|---|---|---|
| V1 | Gradient backgrounds, above all purple to blue, blue to cyan, purple to pink | The default "AI" colour treatment; no identity | Brief; anti-slop R-01 |
| V2 | Frosted-glass cards (glassmorphism) | Flattens hierarchy; a trend, not a function | Brief; R-10 |
| V3 | Emoji used as icons, bullets or heading decoration | Carries no information | Brief; anti-slop UI and copywriting |
| V4 | Sparkles, magic wands, robots, brains, glowing orbs, circuit boards | The stock vocabulary of "AI"; says nothing about the content | Brief; R-04 |
| V5 | Rows of three identical cards | Flattens content of different weight | Brief; R-14 |
| V6 | Numbered labels "01 / 02 / 03" on items that are not a sequence | Numbers claim an order that does not exist | Brief; `frontend-design` |
| V7 | Pill-shaped buttons, badges and labels | Radius as decoration | Brief; R-09, R-11 |
| V8 | Cream or beige backgrounds with italic serif accents | A current generated-design default | Brief; `frontend-design` |
| V9 | A coloured stripe along one edge of a slide, card or box | The most common generated-slide filler (decided: none) | anti-slop "Colored Left Stripe"; `pptx` |
| V10 | An accent line under titles | A hallmark of generated slides | `pptx` |
| V11 | Drop shadows and floating cards | Elevation with no hierarchy | R-12 |
| V12 | Glow on anything | Attention bid with nothing behind it | R-13 |
| V13 | Background grids, dot grids, blueprint lines | Texture without intent | R-07 |
| V14 | Bento grids and tile mosaics | A layout template, not a decision | R-05 |
| V15 | Fake terminal windows or fake app chrome | A costume instead of the real thing | R-05; anti-slop UI |
| V16 | Big-number stat callouts | Only with a real, sourced number, which this program rarely has | R-17; `pptx` lists them as an idea |
| V17 | An all-caps, widely tracked label above a heading ("eyebrow") | Template chrome that repeats the heading | R-06; `frontend-design` |
| V18 | Meta strings joined with middle dots (A · B · C) | Template chrome; an ID belongs in the stop map | `frontend-design` |
| V19 | One word of a headline set apart by colour, italics or bold | A generated-headline tell | `frontend-design` |
| V20 | An arrow appended to every link or action | Decoration posing as direction | R-08; `frontend-design` |
| V21 | Large monospace headings for a "technical" look | Typography as costume | R-06 |
| V22 | Decorative or pulsing status dots | A state indicator with no state | anti-slop UI |
| V23 | More than one track colour, or the accent spread over everything | The accent stops meaning anything | R-29 |
| V24 | Icons from one stock set used as decoration | The library look, not the content | R-04 |
| V25 | Centred body text, crowded slides, text that overflows its box | Unreadable when projected | `pptx` |
| V26 | Dark theme by default | Here, dark is an option for dim rooms, not the identity | R-21 |

### 11.2 Text, in English and in French

| # | Pattern | English example | French example | Catalogued in |
|---|---|---|---|---|
| T1 | Filler openers and temporal runways | "In today's fast-paced world" | « Dans le monde d’aujourd’hui », « À l’ère du numérique » | Brief; copywriting |
| T2 | Inflated claims and buzzwords | "revolutionary", "seamless", "game-changer", "unlock" | « révolutionnaire », « incontournable », « véritable levier », « changer la donne » | Brief; R-16 |
| T3 | Lists of three by reflex | "faster, smarter, better" | « plus vite, plus loin, plus fort » | Brief; copywriting |
| T4 | "Not this, but that" constructions | "It's not just a tool, it's a partner" | « Ce n’est pas un simple outil, c’est un partenaire » | Brief; copywriting |
| T5 | A bolded lead-in on every bullet | "**Speed:** it is faster" | « **Rapidité :** c’est plus rapide » | Brief; copywriting |
| T6 | Summaries that restate what was just said | "In summary, as we saw…" | « En résumé, comme nous l’avons vu… » | Brief; copywriting |
| T7 | Signposting instead of content | "Let's dive in", "Here's what you need to know" | « Plongeons dans le sujet », « Voici ce qu’il faut savoir » | Copywriting |
| T8 | Chatbot closers | "I hope this helps!" | « N’hésitez pas à… », « J’espère que cela vous aide » | Copywriting |
| T9 | Weasel attributions | "Experts agree" | « Les experts s’accordent à dire », « De nombreuses études montrent » | Copywriting |
| T10 | Theatrical takeaways | "Let that sink in." | « Le message est clair : », « Relisez bien cette phrase. » | Copywriting |
| T11 | Staccato fragments for drama | "No guessing. No waste." | « Pas de doute. Pas de perte. » | Copywriting |
| T12 | Aphorism formulas | "Data is the new oil" | « La donnée est le nouvel or noir » | Copywriting |
| T13 | Synonym cycling | "the tool… the solution… the platform" | « l’outil… la solution… la plateforme » | Copywriting |
| T14 | Stacked hedging | "could potentially" | « pourrait potentiellement » | Copywriting |
| T15 | Dashes as connectors in running text | "fast — and safe" | « rapide — et sûr » | R-02; this file, section 9 |
| T16 | Title Case in headings and list items | "How To Write A Brief" | Capitals on every word of a heading | Copywriting; OQLF practice (section 9) |
| T17 | Actorless passives, abstractions given human verbs | "Mistakes were made", "the data tells us" | « Des erreurs ont été commises », « les données nous disent » | Copywriting |
| T18 | Fake-candid openers | "Honestly?" | « Soyons honnêtes : » | Copywriting |
| T19 | Scare quotes and quotation marks used for emphasis | "a 'smart' assistant" | un assistant « intelligent » (as emphasis) | Copywriting |
| T20 | Invented specifics: numbers, testimonials, case studies, sources | "Trusted by 10,000 teams" | « Adopté par 10 000 équipes » | R-17, R-18, R-36; `AGENTS.md` |
| T21 | English typography in French text | "9:00", "$25", "25%", "10,000", "September" | 9:00, 25$, 25%, 10,000 | Section 9 |

Patterns that need judgment, not deletion: one short emphatic sentence, a single « cependant », polished grammar. Look for clusters (copywriting, "What NOT to flag").

## 12. Sources

Checked on 2026-11-10.

- **Office québécois de la langue française, Banque de dépannage linguistique.** The article number used in section 9, then the URL:
  - 22039 https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles
  - 24566 https://vitrinelinguistique.oqlf.gouv.qc.ca/24566/la-typographie/espacement/contextes-exigeant-une-espace-insecable
  - 25447 https://vitrinelinguistique.oqlf.gouv.qc.ca/25447/la-typographie/nombres/espacements-dans-les-nombres
  - 21584 https://vitrinelinguistique.oqlf.gouv.qc.ca/21584/la-typographie/nombres/ecriture-des-sommes-dargent
  - 21191 https://vitrinelinguistique.oqlf.gouv.qc.ca/21191/la-typographie/nombres/emploi-du-signe-decimal-et-indication-de-la-division-dans-les-unites-de-mesure
  - 21242 https://vitrinelinguistique.oqlf.gouv.qc.ca/21242/la-typographie/nombres/ecriture-des-dates-et-des-heures-dans-les-lettres-et-les-textes-courants
  - 21640 https://vitrinelinguistique.oqlf.gouv.qc.ca/21640/la-typographie/nombres/ecriture-des-dates
  - 21516 https://vitrinelinguistique.oqlf.gouv.qc.ca/21516/la-typographie/nombres/ecriture-des-heures
  - 21497 https://vitrinelinguistique.oqlf.gouv.qc.ca/21497/la-typographie/majuscules/emploi-de-la-majuscule-pour-des-types-de-denominations/majuscule-aux-titres-doeuvres-et-douvrages
  - 24404 https://vitrinelinguistique.oqlf.gouv.qc.ca/24404/la-typographie/division-des-textes/procedes-de-hierarchisation-des-titres-et-des-sous-titres
  - 23402 https://vitrinelinguistique.oqlf.gouv.qc.ca/23402/la-ponctuation/point/emplois-particuliers-du-point
  - 23326 https://vitrinelinguistique.oqlf.gouv.qc.ca/23326/la-ponctuation/deux-points/deux-points-dans-les-titres
  - 25108 https://vitrinelinguistique.oqlf.gouv.qc.ca/25108/banque-de-depannage-linguistique/la-ponctuation/enumeration-verticale
  - 23376 https://vitrinelinguistique.oqlf.gouv.qc.ca/23376/la-ponctuation/tiret/divers-emplois-du-tiret
  - 23378 https://vitrinelinguistique.oqlf.gouv.qc.ca/23378/la-ponctuation/tiret/le-tiret-dans-la-mise-en-valeur-dun-passage
  - 23363 https://vitrinelinguistique.oqlf.gouv.qc.ca/23363/la-ponctuation/guillemets/generalites-sur-les-guillemets
  - 24887 https://vitrinelinguistique.oqlf.gouv.qc.ca/24887/les-abreviations-et-les-symboles/les-sigles-et-les-acronymes/regles-decriture-des-sigles-et-acronymes
  - 21136 https://vitrinelinguistique.oqlf.gouv.qc.ca/21136/les-abreviations-et-les-symboles/les-sigles-et-les-acronymes/genre-et-nombre-des-sigles-et-acronymes
  - 24626 https://vitrinelinguistique.oqlf.gouv.qc.ca/24626/la-redaction-et-la-communication/presentation-assistee-par-ordinateur/conception-du-diaporama/redaction-du-texte-dun-diaporama
  - 23983 https://vitrinelinguistique.oqlf.gouv.qc.ca/23983/banque-de-depannage-linguistique/la-redaction-et-la-communication/feminisation-et-redaction-epicene/synthese-sur-la-feminisation-lexicale-et-la-redaction-epicene
  - 25421 https://vitrinelinguistique.oqlf.gouv.qc.ca/25421/banque-de-depannage-linguistique/la-redaction-et-la-communication/feminisation-et-redaction-epicene/redaction-epicene/redaction-epicene-et-autres-styles-decriture-dits-inclusifs
- **anti-slop,** miqdadbadjuber/anti-slop at commit `41b85ede0257f39bfcffedf3f58c3c59bcc8530d` (MIT): `skills/antislop/SKILL.md` (Part 1 and rules R-01 to R-40), `skills/antislop-copywriting/SKILL.md`, `skills/antislop-ui/SKILL.md`. Patterns are paraphrased here, not copied.
- **Anthropic skills,** anthropics/skills at commit `2c5958ecac7cee2b583967a2c4981d0f4a75c579` (Apache-2.0 per folder): `skills/frontend-design/SKILL.md` and `skills/pptx/SKILL.md`. Patterns are paraphrased here, not copied.
- **WCAG 2.2** (W3C), success criteria 1.4.1, 1.4.3, 1.4.6 and 1.4.11, listed in R-01.
- **Atkinson Hyperlegible Next and Mono:** googlefonts/atkinson-hyperlegible-next at `7925f50f649b3813257faf2f4c0b381011f434f1`, and googlefonts/atkinson-hyperlegible-next-mono at `154d50362016cc3e873eb21d242cd0772384c8f9`. SIL Open Font License 1.1; see `THIRD_PARTY_NOTICES.md`.
