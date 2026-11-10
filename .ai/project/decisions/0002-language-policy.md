# 0002. Language policy

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

The program is delivered in Canadian French. The agents and the governance files work in English. The repository is read by learners, presenters and contributors.

## Decision

1. Learner-facing deliverables are written in Canadian French.
2. Presenter-only material is also in French: speaker notes, the run of show, and the presenter copies of workshop packs.
3. Everything else is in English: instruction files, specifications, state, handoffs, decision records, knowledge notes, code, and file and directory names.
4. Lesson files and directories use English names that match their module cards, prefixed with the module ID.
5. `README.md` is fully bilingual: English first, then a French version that mirrors it.

## Consequences

- A presenter never has to translate live.
- Each lesson path can be derived from its card path.
- `README.md` doubles in length and is reviewed in both languages.
- The glossary decides which technical terms stay in English inside French text.
