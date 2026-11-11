# Handoff: Fictional engagement brief

- Date: 2026-11-10
- Stage: build

## Goal

Build order step 3: settle OD-11 with the author using `grilling`, then write the fictional engagement brief, `resources/fictional-engagement.md`.

## Done

- **OD-11 settled in two rounds of `grilling`** and confirmed by the author ("Yes to all as suggested by you"). The answers are decision 0016, `Status: proposed`, for the author to accept.
- **Brief written:**
  - the client (Location Pavois) and the project;
  - ten characters;
  - the client's three rules on AI;
  - the nine X-03 stages, with dates, approvals and the exercise placed at each one, each with its prepared starting point;
  - the shared story for P-02 and E-02;
  - the running example of the common session;
  - the context paragraph for the packs.
- **Glossary (R-02):** seven X-03 stage and artifact terms added, each checked in the GDT, with 8 excluded terms and 8 index rows. A section of program part names was also added, which decision 0012 required and the glossary lacked. The glossary now has 60 entries, 45 excluded terms and 68 index rows.
- **The client's name:** a web search found no company called "Location Pavois". « Ombelle » was rejected because an event venue in France uses it. The Quebec business registry (REQ) was not checked.

## Files changed

- `resources/fictional-engagement.md`: new, `status: review`, `native_review: pending`.
- `resources/R-02-glossary.md`:
  - seven entries: demande d’offres de services, document de passation, notes de mise à jour, occasion d’affaires, offre de services, réunion de démarrage, synthèse de découverte;
  - 8 rows in the excluded-terms table and 8 in the index;
  - the table of part names (decision 0012);
  - the maintainer comment.
- `.ai/project/decisions/0016-fictional-engagement.md`: new, proposed.
- `.ai/project/state.md`: focus and next steps.
- `.ai/project/handoffs/2026-11-10-fictional-engagement.md`: this file.

Locked files changed, each with the author's approval quoted and dated:

- `.ai/project/spec/open-decisions.md`: OD-11 status set to "settled on 2026-11-10 (decision 0016)". The question named this file, with the recommended answer "Yes, and the edit to `.ai/project/spec/open-decisions.md` is approved." The author answered "Yes to all as suggested by you", 2026-11-10.

## Checks run and results

- **`tools/check_french.py`:**
  - the glossary has 0 hits;
  - the brief has 1 hit, F16 on « Mandat fictif : Location Pavois ». The capitals are on a company name, which F16 exempts.
- **GDT:** every record linked from the new entries was opened on 2026-11-10 (20 records in all, including those checked for the brief's job titles and ordinary words). Discovery brief and handover document have no GDT record; rule 2 applies.
- **`canadian-french` passes on the brief:**
  - no excluded term in a wrong sense;
  - no listed anglicism;
  - « outil » not used;
  - épicène wording;
  - every sentence outside lists is 22 words or fewer, after three were shortened.
- **`slop-check` on the brief and the new entries:** no cluster.
  - Bold appears only in the glossary's record fields.
  - The guillemets mention terms.
  - The figures are facts of the fiction.
- **Front matter** of both files parses as YAML.
- **Relative links:** 551 resolve. The one false positive is a regex in a code span in `typography-checks.md`, already present before this batch.

## Open questions

1. The glossary and the README write dates with ordinary spaces (« 10 novembre 2026 »), but `DESIGN.md` section 9 asks for non-breaking spaces, and no F-check catches it. The brief follows `DESIGN.md`. Recommended: a separate small batch that fixes the dates in the glossary and the README and adds a check F22 (the README and `typography-checks.md` are locked).

## Next step

Build order step 4: the core lessons C-01 to C-08, with X-02's segment 4 slide, using the `lesson-writing` skill. The running example and every exercise fact come from `resources/fictional-engagement.md`.
