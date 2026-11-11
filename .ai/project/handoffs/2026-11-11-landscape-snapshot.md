# Handoff: R-01 in the build order, and the C-02 plan

- Date: 2026-11-11
- Stage: build

## Goal

Close the open questions of the previous session, then start C-02 (the landscape snapshot): settle OD-10 and the other points the card leaves open before writing.

## Done

- **Decision 0017** was already marked `accepted` by the author (commit `24808af`).
- **R-01 placed in the build order:** it is a sub-step of step 4, after the core lessons and before step 5. It is a sub-step rather than a new step 5 because renumbering would make OD-09's "build order, step 9" in `open-decisions.md` (locked, not covered by the approval) point at the wrong step.
- **C-02 planned, not written.** The questions in "Open questions" below were put to the author before any writing.

## Files changed

Batch 4c (R-01 in the build order):

- `.ai/project/handoffs/2026-11-11-landscape-snapshot.md`: this handoff.
- `.ai/project/state.md`: focus, next steps and open questions.

Locked files changed (stage `build` only), each with the author's approval quoted and dated:

- `.ai/project/spec/build-order.md`: R-01 added as a sub-step of step 4. Approval: "Approved to edit `.ai/project/spec/build-order.md` this time", 2026-11-11.

## Checks run and results

- `git status` at the start: clean, everything from the previous session committed.
- `git grep` for references to build-order step numbers: only OD-09 ("step 9") and past handoffs depend on the numbering; the sub-step keeps both valid.

## Open questions

The C-02 questions, as asked in the session (see `state.md`):

1. The lesson's length: 4 minutes in session, with the full version as learner text (recommended), or 15 minutes of slides and notes.
2. OD-10, the snapshot owner and refresh routine: accept the proposal (recommended), recorded in a new decision record.
3. How the organization's approved tools appear in an organization-neutral lesson.
4. Whether to name public products as examples in each category, each checked on its vendor page.

## Next step

Read the author's answers, record OD-10 in a decision record with `Status: proposed`, then show the C-02 unit plan and write the lesson with `lesson-writing`.
