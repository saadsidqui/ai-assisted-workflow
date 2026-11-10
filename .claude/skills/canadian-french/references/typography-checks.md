# Typography checks

Mechanical checks for French text, each tied to a rule in `DESIGN.md` section 9. The patterns are Python regular expressions. Run them on French prose only, and never on code spans, fenced code, URLs or file names. Every hit is a candidate: read it in context before changing it.

`NB` is the non-breaking space U+00A0. `NNB` is the narrow non-breaking space U+202F, which this project does not use.

| # | Error | Pattern | Fix | Rule |
|---|---|---|---|---|
| F1 | Straight apostrophe | `[A-Za-zÀ-ÿ]'[A-Za-zÀ-ÿ]` | ’ (U+2019) | Apostrophe choice |
| F2 | Colon without a space or with a plain space | `[^\s\u00a0]:(?=\s|$)` and ` :(?=\s|$)` | NB before the colon | Deux-points |
| F3 | Space before ; ! ? | `[ \u00a0\u202f][;!?]` | Remove the space | Point-virgule, ! and ? |
| F4 | Plain space or no space inside the guillemets | `«(?!\u00a0)` and `(?<!\u00a0)»` | NB inside | Guillemets |
| F5 | English double quotation marks in French text | `"[^"\n]+"` and `“[^”\n]+”` at the first level | French guillemets | Guillemets |
| F6 | Percent without NB | `\d%` and `\d %` | `8NB%` | Percent |
| F7 | Dollar before the amount, or without NB | `\$\s?\d` and `\d ?\$` | `25NB$` | Money |
| F8 | Colon time in running text | `\b\d{1,2}:\d{2}\b` | `9NBh`, `14NBhNB30` | Time, running text (tables may keep it) |
| F9 | Hour symbol glued or with plain spaces | `\b\d{1,2}h\d{0,2}\b` and `\d h\b` | NB on both sides of h | Time, running text |
| F10 | Minutes under ten without a zero | `\bh\u00a0?[1-9]\b` | `8NBhNB05` | Time, running text |
| F11 | Decimal point | `\b\d+\.\d+\b` | Comma | Decimal sign (version numbers in re-verify lists excepted) |
| F12 | Comma as thousands separator | `\b\d{1,3},\d{3}\b` | NB groups | Large numbers (check: may be a decimal) |
| F13 | Five or more digits not grouped | `\b\d{5,}\b` | NB every three digits from the right | Large numbers (years, codes and identifiers excepted) |
| F14 | Capitalized month or day mid-sentence | `(?<=[a-zà-ÿ0-9,] )(Janvier|Février|Mars|Avril|Mai|Juin|Juillet|Août|Septembre|Octobre|Novembre|Décembre|Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche)\b` | Lowercase | Dates (author-confirmed convention) |
| F15 | Heading ends with a period or colon | `^#{1,6} .*[.:]\s*$` | Remove it | Headings |
| F16 | Title Case heading | heading line with two or more capitalized words after the first, other than proper nouns or acronyms | Sentence case | Headings (author-confirmed convention) |
| F17 | Em dash or en dash in running text | `\u2014` and ` \u2013 ` outside schedules | Comma, parentheses or colon | Dash choice |
| F18 | Abbreviated doublet with a period or point médian | `\w[.\u00b7]\w+([.\u00b7]s)?\b` (for example participant\u00b7e\u00b7s) | Full doublet or a neutral designation | Inclusive writing |
| F19 | Ordinal written with superscript markup, or "1st" | `1<sup>er</sup>` or `\b1st\b` | `1er` | Dates |
| F20 | Narrow non-breaking space used | `\u202f` | NB | This project uses NB only |
| F21 | Numeric date in running text | `\b\d{4}-\d{2}-\d{2}\b` outside tables and front matter | le 10 novembre 2026 | Dates, running text |

Notes:

- **Lists:** F2 does not apply to the colon that introduces a vertical list on its own line. That colon still takes NB before it.
- **Slides:** slide headings follow F15 and F16. Keyword lists on slides may drop final punctuation (`DESIGN.md` section 4.2).
- **Tables and schedules** may keep `15:30` and `8NBhNB30 – 16NBhNB30` (rules Time, numeric and Time, schedules).
