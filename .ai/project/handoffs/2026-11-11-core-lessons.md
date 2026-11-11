# Handoff: Core lessons, starting with C-01

- Date: 2026-11-11
- Stage: build

## Goal

Build order step 4: write the core lessons one at a time with `lesson-writing`, starting with C-01. Settle what blocked the first lesson (OD-05) and close the follow-ups from steps 2 and 3.

## Done

- **Step 3 closed.**
  - The author accepted decision 0016 and recorded the native review of the glossary and the brief (commit `7f9b974`).
  - At the author's request, `native_review` now reads "done 2026-11-11" in both files, as the template expects.
- **OD-05 settled** by decision 0017, which is still `proposed` and waits for the author to mark it `accepted`:
  - a core lesson's `minutes` is the card's figure plus its S-01 checkpoint row;
  - a track or overlay lesson keeps the card's figure, checkpoint included;
  - C-01's card sort runs two minutes in the room.
  - The rule is now stated in `templates/lesson.md`, `lesson-writing/SKILL.md` and `references/card-to-lesson.md`.
- **C-01 written,** `lessons/core/C-01-mental-model-and-vocabulary.md`, titled « Une image juste et les bons mots » (confirmed by the author):
  - 15 minutes and 10 slides;
  - three units: a plausible continuation, the four words, what the assistant knows;
  - the examples come from the brief.
- **Date typography (F22).**
  - New check F22 in `typography-checks.md`: a plain space inside a date.
  - The glossary's dates now use non-breaking spaces. The French half of the README had none to fix.
- **R-01 placement agreed:** the author said yes to building R-01 (further reading) right after the core lessons. It is not yet written into `build-order.md`.

## Files changed

Batch 4a (C-01 and lesson minutes):

- `lessons/core/C-01-mental-model-and-vocabulary.md`: new, `status: review`, `native_review: pending`.
- `.ai/project/decisions/0017-lesson-minutes-and-checkpoints.md`: new, proposed.
- `resources/fictional-engagement.md`: `native_review`; C-01 listed among the uses of stages 1 and 4.
- `resources/R-02-glossary.md`: `native_review`.
- `.ai/project/state.md`, this handoff.

Batch 4b (dates, F22):

- `resources/R-02-glossary.md`: non-breaking spaces inside every date.
- `tools/check_french.py` (docstring) and `tools/README.md`: "F1 to F22".

Locked files changed, each with the author's approval quoted and dated:

- `templates/lesson.md`: the guide line for `minutes` states decision 0017. Approval: "1. Approved as recommended", 2026-11-11.
- `.ai/project/spec/open-decisions.md`: OD-05 status "settled on 2026-11-11 (decision 0017)". Approval: "1. Yes", 2026-11-11.
- `.claude/skills/lesson-writing/SKILL.md` (step 2) and `.claude/skills/lesson-writing/references/card-to-lesson.md` (Time row): the decision 0017 wording. Approval: "2. Yes", 2026-11-11.
- `.claude/skills/canadian-french/references/typography-checks.md`: row F22 added. Approval: "5. Approved as suggested", 2026-11-11. The suggestion was a separate batch that fixes the dates and adds F22.

## Checks run and results

- **`tools/check_lesson.py` on C-01:** every check passes. Spoken words: 1,031 for 10 talk minutes (range 935 to 1,265). The timing table, timing marks and minutes all total 15.
- **`tools/check_french.py` (22 checks):**
  - C-01, the glossary and the French half of the README: 0 hits;
  - the brief: one known F16 hit on the company name in its title, which F16 exempts.
  - A self-test confirms that F22 flags « 10 novembre » with a plain space and passes a non-breaking one.
- **`canadian-french` on C-01:**
  - glossary forms at first mention;
  - « outil » used only in its C-01 sense;
  - épicène wording (three generics corrected);
  - GDT checks for two optional-topic terms: « banc d'essai » means a testbed, so the lesson says « tests de performance publiés »; « plongement » follows the GDT record « plongement de mots ».
- **`slop-check` on C-01:** one T4/T11 sentence rewritten and the T5 bold lead-ins removed. The visual pass waits for the first deck build.

## Open questions

1. Decision 0017 is `proposed`. The author marks it `accepted` (or not) in the next commit.
2. Add R-01 to `.ai/project/spec/build-order.md` as a step right after the core lessons. The author agreed to the placement on 2026-11-11, but the file is locked and was not named. Ask for the approval that names it.

## Next step

1. Start the session routine. `git status` should show this session's changes committed; if not, ask the author.
2. Ask the open questions above.
3. C-02, the landscape snapshot: settle OD-10 (who owns the snapshot) with the author first, then write the lesson with `lesson-writing`. Show the plan before writing.
