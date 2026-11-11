# Handoff: R-01 in the build order, and the C-02 and C-03 lessons

- Date: 2026-11-11
- Stage: build

## Goal

Close the open questions of the previous session, then write C-02 (the landscape snapshot) after settling OD-10 and the points the card leaves open, and C-03 (task fit and limits).

## Done

- **Decision 0017** was already marked `accepted` by the author (commit `24808af`).
- **R-01 placed in the build order:** it is a sub-step of step 4, after the core lessons and before step 5. It is a sub-step rather than a new step 5 because renumbering would make OD-09's "build order, step 9" in `open-decisions.md` (locked, not covered by the approval) point at the wrong step.
- **C-02 settled:** the author approved four points "as recommended" on 2026-11-11. They are recorded in decision 0018, which the author then accepted:
  - OD-10: the presenter of record owns the snapshot;
  - `minutes: 4`, with the full version as learner text;
  - a blank « Approuvé ici » column on the map;
  - two or three public examples per category, each checked on a vendor page.
- **C-02 written,** `lessons/core/C-02-landscape-snapshot.md`, titled « Ce qui existe aujourd’hui » (title confirmed by the author):
  - 4 minutes and 3 slides, with the show of hands on the map slide;
  - learner text: the seven categories, each answering the three questions, with dated examples;
  - the examples come from the brief: Kevin's first rule and Isabelle's request for proposals.
- **Vendor pages** were opened on 2026-11-11 for 17 products; the URLs are in the lesson's re-verify list.
  - openai.com returned HTTP 403, even to a generic browser user agent (no personal data in it). At the author's request the fetch was retried, and OpenAI's documentation at learn.chatgpt.com loaded. ChatGPT and Codex were added from it (batch 4e).
  - The Microsoft 365 Copilot product page timed out; the Microsoft Learn pages were used instead.
- **After batch 4d:** the author accepted decision 0018, confirmed the title « Ce qui existe aujourd’hui », approved the OD-10 status change, and kept « interface de programmation d’application (API) » as written.

- **C-03 settled:** the author approved two points "as recommended" on 2026-11-11, recorded in decision 0019 (`proposed`):
  - a core practice of one or two minutes runs in the room; a longer one goes to the textbook;
  - C-03's green task is kept for after the session or the track workshop, and S-02 does not change.
- **C-03 written,** `lessons/core/C-03-task-fit-and-limits.md`, titled « Où l’assistant aide, et où il échoue » (title not yet confirmed):
  - 9 minutes (6 + 3 for checkpoint 2) and 8 slides; 1 minute of silent practice;
  - units: three zones, five questions, help is not decide;
  - the checkpoint tasks come from the brief: the requirements list (green), the decision to respond (red), the staff summary (yellow, meant to divide the room);
  - the examples avoid the planted traps of packs A, B and C (availability code, the deadline conflict, a delivery date for Hélène).

## Files changed

Batch 4c (R-01 in the build order):

- `.ai/project/handoffs/2026-11-11-landscape-snapshot.md`: this handoff.
- `.ai/project/state.md`: focus, next steps and open questions.

Batch 4d (C-02):

- `lessons/core/C-02-landscape-snapshot.md`: new, `status: review`, `native_review: pending`.
- `.ai/project/decisions/0018-landscape-snapshot.md`: new, proposed.
- `resources/fictional-engagement.md`: C-02 listed among the uses of stages 1 and 4.
- `.ai/project/state.md`, this handoff.

Batch 4e (follow-ups to C-02):

- `lessons/core/C-02-landscape-snapshot.md`: ChatGPT and Codex added to the examples and to the re-verify list; the OpenAI note removed. The GitHub Copilot agent mode stays mentioned in the text, but leaves the list of agent examples.
- `.ai/project/knowledge/vendor-pages.md`: new note on which vendor pages can be read automatically.
- `.ai/project/state.md`, this handoff.

Batch 4f (C-03):

- `lessons/core/C-03-task-fit-and-limits.md`: new, `status: review`, `native_review: pending`.
- `.ai/project/decisions/0019-core-practice-in-the-room.md`: new, proposed.
- `resources/fictional-engagement.md`: C-03 listed among the uses of stages 1, 2, 3, 4 and 6.
- `.ai/project/state.md`, this handoff.

Locked files changed (stage `build` only), each with the author's approval quoted and dated:

- `.ai/project/spec/open-decisions.md`: OD-10 status "settled on 2026-11-11 (decision 0018)". Approval: "3. Yes", 2026-11-11.

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

- **`tools/check_lesson.py` on C-03:** every check passes. Spoken words: 551 for 5 talk minutes (range 468 to 632). The timing table, timing marks and minutes all total 9.
- **Slide word limits on C-03:** every slide within `DESIGN.md` 4.2 (concept slides at most 25 words; the checkpoint question 6 words, with three short tasks under it, as the card puts the tasks on screen).
- **`tools/check_french.py`:** C-03 0 hits; the brief keeps its known F16 hit.
- **`canadian-french` on C-03:** glossary forms at first mention (assistant virtuel, dépôt, révision humaine, revue de code, demande de fusion, IA spelled out); « fait la leçon », which means to lecture someone, replaced.
- **`slop-check` on C-03 (text):** one aphorism-like sentence rewritten; no clusters found. The visual pass waits for the first deck build.

## Open questions

1. Accept decision 0019.
2. Confirm the C-03 title « Où l’assistant aide, et où il échoue ».

## Next step

Start the session routine and ask the open questions above. Then C-04 (the working loop and prompting) with `lesson-writing`: it carries the running example (Marc-André's staff summary) and checkpoint 3. Show the plan before writing.
