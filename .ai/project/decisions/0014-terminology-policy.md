# 0014. Terminology policy and first renderings

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

The R-02 card proposed a terminology policy "to confirm" and flagged three doubtful candidates (OD-06). A check of the Grand dictionnaire terminologique (GDT) on 2026-11-10 found:

- OQLF terms for several concepts the card proposed to keep in English ("prompt", "prompt engineering", "user story");
- no entry for two others ("hook" in its software sense, "fine-tuning");
- a collision: the card's rendering of "gate", "point de contrôle", is already the label of every lesson's checkpoint section.

Termium Plus, the second source named in the `canadian-french` skill, refuses automated reading.

## Decision

1. The terminology policy, which replaces the card's draft:
   1. Where the GDT has a preferred term for the concept, use it, and give the English term once, in italics, at first mention.
   2. Where it has none, use plain French if an everyday word says it exactly.
   3. Otherwise keep the English term, in italics at first mention.
   4. Product names, file names, commands and settings are never translated.
   5. One term, one rendering. Where the GDT gives several preferred terms, the glossary picks one.
2. Terms are checked in the GDT only. A term with no GDT entry is recorded as "no GDT record" with the search date. The author or the native reviewer checks Termium Plus when a choice depends on it.
3. "Gate" is rendered "point d’approbation". "Point de contrôle" stays the label of the lesson checkpoint.
4. "Brief", in its task sense (C-04), is rendered "consigne", with "brief" at first mention. The brief skeleton is the "gabarit de consigne". The other senses, "project brief" and "decision brief", are separate terms.
5. These renderings follow from the policy:
   - "requête" (prompt), "rédaction de requêtes" (prompting), "rédactique" (prompt engineering);
   - "infiltration de requête" (prompt injection);
   - "structuration contextuelle" (context engineering);
   - "récit utilisateur" (user story);
   - "hook" and "fine-tuning" kept in English.

## Consequences

- The glossary, `resources/R-02-glossary.md`, restates the policy in French and records each term with its GDT entry and the date it was checked.
- OD-06 is settled.
- Lessons say "requête" where a card says "prompt", "récit utilisateur" where it says "user story", and "point d’approbation" where it says "gate".
- Renaming the lesson checkpoint is ruled out.
