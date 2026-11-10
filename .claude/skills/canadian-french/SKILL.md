---
name: canadian-french
description: Check or correct Canadian French in deliverables. Covers OQLF typography (spaces, quotation marks, numbers, money, dates, times, headings, lists), terminology against the glossary, anglicisms with their OQLF sources, inclusive writing and register. Use on any French file in lessons/, sessions/, workshops/, handouts/, resources/ or books/, and on the French half of README.md, before it is reported done. Not for English files, code, or file and product names.
---

# Canadian French

French deliverables are written in French from the start. This skill checks them against the usage of the Office québécois de la langue française (OQLF), as recorded in `DESIGN.md` section 9, and against the project glossary.

## Scope

- **Checked:** French prose, headings, slide text, speaker notes, table cells, alt text.
- **Not checked:**
  - code and commands;
  - file and directory names;
  - URLs;
  - product names;
  - YAML keys;
  - English passages quoted on purpose.

## Procedure

1. **Read the rules:** `DESIGN.md` sections 7 and 9, then [typography-checks.md](references/typography-checks.md), [anglicisms.md](references/anglicisms.md) and [terminology.md](references/terminology.md).
2. **Typography pass.** Run every check in `typography-checks.md`. Its patterns find the mechanical errors: straight apostrophes, missing non-breaking spaces, a space before ; ! ?, English quotation marks, "9:00", "$25", "25%", decimal points, capitalized months, Title Case headings, headings ending in a period or colon, dashes. Read every hit in context before changing it: a pattern can match inside code or a quotation.
3. **Terminology pass.** Every technical term must have its glossary rendering, and one term keeps one rendering in a file and across files.
   - **Policy:** apply the terminology policy of decision 0014 (see `terminology.md`).
   - **Missing term:** a term the glossary does not have is flagged for the glossary, with a candidate checked in the Grand dictionnaire terminologique (GDT). It is never invented.
   - **Names of the program's parts:** decision 0012.
4. **Anglicism pass.** Look for every entry of `anglicisms.md`, in all its inflected forms.
   - **Listed words:** propose the recommended form and cite the source URL.
   - **Words not listed:** check the BDL or GDT and add the result to `anglicisms.md` with its date and URL. If nothing confirms it, report it as "suspected" and do not change it.
5. **Inclusive writing pass** (`DESIGN.md` section 7, OQLF rédaction épicène):
   - neutral designations and épicène terms first;
   - full doublets for determinate persons;
   - abbreviated doublets only in tables or forms, and only with parentheses or brackets;
   - no point médian and no « iel ».
6. **Register pass:**
   - participants are addressed as « vous »;
   - the active voice, and sentences of about 20 words or fewer;
   - one idea per paragraph;
   - no word-for-word calque of an English sentence.
7. **Report, then fix.** Report each finding as: location, rule, current text, proposed text, source. Fix what the task covers. List anything that changes meaning, rather than fixing it.

## Rules

- A rule is applied only if `DESIGN.md` section 9 or a dated OQLF source supports it. Taste is not a rule.
- An OQLF option is applied the way `DESIGN.md` chose it. For example: no space before ; ! ?, and no grouping of four-digit numbers.
- A correction never changes the facts, the order of ideas or the meaning.
- Non-breaking spaces are real characters: U+00A0, never `&nbsp;`, in Markdown and in slide text.

## Acceptance check

- [ ] Every typography check in `typography-checks.md` was run, and each remaining hit has a reason.
- [ ] Every technical term matches the glossary, or is flagged with a GDT-checked candidate.
- [ ] Every anglicism reported carries an OQLF source URL, or is marked "suspected".
- [ ] Inclusive writing follows `DESIGN.md` section 7.
- [ ] No correction changed meaning. Changes and proposals are listed separately.

When `tools/check_french.py` exists, run it for the typography pass and report its output.
