# Handoff: R-01 in the build order, and the C-02 lesson

- Date: 2026-11-11
- Stage: build

## Goal

Close the open questions of the previous session, then write C-02 (the landscape snapshot) after settling OD-10 and the points the card leaves open.

## Done

- **Decision 0017** was already marked `accepted` by the author (commit `24808af`).
- **R-01 placed in the build order:** it is a sub-step of step 4, after the core lessons and before step 5. It is a sub-step rather than a new step 5 because renumbering would make OD-09's "build order, step 9" in `open-decisions.md` (locked, not covered by the approval) point at the wrong step.
- **C-02 settled:** the author approved four points "as recommended" on 2026-11-11. They are recorded in decision 0018 (`proposed`):
  - OD-10: the presenter of record owns the snapshot;
  - `minutes: 4`, with the full version as learner text;
  - a blank « Approuvé ici » column on the map;
  - two or three public examples per category, each checked on a vendor page.
- **C-02 written,** `lessons/core/C-02-landscape-snapshot.md`, titled « Ce qui existe aujourd’hui » (title not yet confirmed by the author):
  - 4 minutes and 3 slides, with the show of hands on the map slide;
  - learner text: the seven categories, each answering the three questions, with dated examples;
  - the examples come from the brief: Kevin's first rule and Isabelle's request for proposals.
- **Vendor pages** were opened on 2026-11-11 for 15 products; the URLs are in the lesson's re-verify list.
  - OpenAI's pages returned HTTP 403, so ChatGPT and Codex are left out.
  - The Microsoft 365 Copilot product page timed out; the Microsoft Learn pages were used instead.

## Files changed

Batch 4c (R-01 in the build order):

- `.ai/project/handoffs/2026-11-11-landscape-snapshot.md`: this handoff.
- `.ai/project/state.md`: focus, next steps and open questions.

Batch 4d (C-02):

- `lessons/core/C-02-landscape-snapshot.md`: new, `status: review`, `native_review: pending`.
- `.ai/project/decisions/0018-landscape-snapshot.md`: new, proposed.
- `resources/fictional-engagement.md`: C-02 listed among the uses of stages 1 and 4.
- `.ai/project/state.md`, this handoff.

Locked files changed (stage `build` only), each with the author's approval quoted and dated:

- `.ai/project/spec/build-order.md`: R-01 added as a sub-step of step 4. Approval: "Approved to edit `.ai/project/spec/build-order.md` this time", 2026-11-11.

## Checks run and results

- `git status` at the start: clean, everything from the previous session committed.
- `git grep` for references to build-order step numbers: only OD-09 ("step 9") and past handoffs depend on the numbering. The sub-step keeps both valid.
- **`tools/check_lesson.py` on C-02:** every check passes, with one expected WARN (no Pratique; the card has no practice). Spoken words: 295 for 3 talk minutes (range 280 to 379). The timing table, timing marks and minutes all total 4.
- **Slide word limits:** map 42 words before the presenter fills its seven cells (limit 60, at most 2 words per cell); concept slides 24 and 22 (limit 25).
- **`tools/check_french.py`:** C-02 0 hits. The brief has the one known F16 hit on its title.
- **`canadian-french` on C-02:**
  - « outil » replaced by « application » wherever it meant a product (glossary: « outil d’IA » is rejected, and C-01 teaches « outil » as what the application lets the model use);
  - first-mention English forms added (*connector*, *permissions*, *pull requests*, *workflows*, *release notes*, *agentic AI*);
  - TI, API and MCP spelled out;
  - the slide's questions agree with « application » (« sert-elle »).
- **`slop-check` on C-02 (text):**
  - one T7 opener removed;
  - a T4/T10 pair in the slide 2 notes rewritten;
  - a recommended topic (« l’abonnement compte autant que le produit ») removed from the taught text; it stays in « Pour aller plus loin ».
  - The visual pass waits for the first deck build.

## Open questions

1. Accept decision 0018.
2. Confirm the C-02 title « Ce qui existe aujourd’hui ».
3. Approve setting OD-10 to "settled on 2026-11-11 (decision 0018)" in `.ai/project/spec/open-decisions.md` (locked).
4. ChatGPT and Codex: add them to C-02 only after the author opens OpenAI's pages and confirms what they show.
5. « interface de programmation d’application (API) »: not in the glossary and not checked in the GDT.

## Next step

Start the session routine and ask the open questions above. Then C-03 (task fit and limits) with `lesson-writing`; its checkpoint is checkpoint 2 of the common session, which follows C-02 in segment 2.
