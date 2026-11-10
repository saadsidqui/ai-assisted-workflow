# Handoff: Terminology policy and glossary draft

- Date: 2026-11-10
- Stage: build

## Goal

Start build order step 2, the glossary (R-02): settle OD-06, then write the first batch of `resources/R-02-glossary.md`.

## Done

- **OD-06 settled with the author** (decision 0014). It covers the terminology policy (GDT first), *gate* → « point d’approbation », *brief* → « consigne », and GDT-only checking.
- **Batch 2a written:**
  - the glossary draft, with the policy in French;
  - ten entries (requête, rédaction de requêtes, rédactique, infiltration de requête, structuration contextuelle, récit utilisateur, point d’approbation, consigne, *hook*, *fine-tuning*);
  - the table of excluded terms.
- **GDT sources:** each GDT entry was opened on 2026-11-10, and the URLs are in the glossary.
- **Batch 2a** was committed as `e3118ff`.
- **Batch 2b written:** 34 more card terms and 4 additions (application, IA agentive, revue de code, énoncé de projet), all checked in the GDT. The glossary now has 48 entries and 29 excluded terms. The author settled the last four terms (*commit*/*push*, *accountability*, *handout*, *engagement*; decision 0015). The glossary has 53 entries and 37 excluded terms.

## Files changed

- `.ai/project/decisions/0014-terminology-policy.md`: new record, accepted by the author's answers to OD-06.
- `resources/R-02-glossary.md`: new, `status: draft`, `native_review: pending`; extended in batch 2b.
- `tools/check_french.py`: module IDs such as E-03.2 are masked before the checks, so F11 no longer reads them as decimals.
- `.ai/project/decisions/0015-glossary-terms-settled-by-the-author.md`: new record of the four answers.
- `.ai/project/state.md`: focus and next steps.
- `.ai/project/handoffs/2026-11-10-terminology-policy.md`: this file.

Locked files changed, each with the author's approval quoted and dated:

- `.claude/skills/canadian-french/references/terminology.md`: the policy section now points to decision 0014; the Termium Plus step now reads "record 'no GDT record' with the search date". Approval: "`.claude/skills/canadian-french/references/terminology.md` and `.ai/project/spec/open-decisions.md` approved", 2026-11-10.
- `.ai/project/spec/open-decisions.md`: OD-06 status set to "settled on 2026-11-10 (decision 0014)". Same approval, 2026-11-10.
- `.claude/skills/canadian-french/SKILL.md`: the terminology pass now says "apply the terminology policy of decision 0014 (see `terminology.md`)". Approval, given to the question that named this file: "1. As recommended", 2026-11-10.
- `README.md`: in the French half, « fiches » (handouts) became « documents d’accompagnement » in four places (lines 113, 121, 122, 144). Approval: "3. As recommended. Edits to locked files approved.", 2026-11-10.

## Checks run and results

- **`tools/check_french.py` on the glossary:** 0 hits. The first run had one F11 hit on a module ID; the checker was fixed for that. A self-test confirms that "3.5" is still flagged and that module IDs are not. The French half of the README still shows 0 hits.
- **Front matter:** parses as YAML.
- **`canadian-french` skill passes on the draft:**
  - no listed anglicism (« adresser une demande à » is the correct sense);
  - no designation of persons that needs inclusive writing;
  - three sentences run 21 to 22 words, within "about 20 on average".
- **Termium Plus** refuses automated reading (HTTP 403), which is why decision 0014 checks terms in the GDT only.

## Open questions

None. The four batch 2b questions were answered (decision 0015).

## Next step

Batch 2c: a definition and a workplace example for every entry, an English-to-French index, then the French and slop checks.
