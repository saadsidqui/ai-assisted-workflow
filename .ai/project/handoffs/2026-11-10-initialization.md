# Handoff: Repository initialization

- Date: 2026-11-10
- Stage: build (initialization locked on 2026-11-10)

## Goal

Set up the repository so that the training program can be built in small, reviewed steps: working rules, specification, design direction, front door, lesson tree, skills and tools. No program content.

## Done

The initialization plan is approved, and its progress log records every step (decision 0001, `.ai/project/decisions/0001-initialization-plan.md`). In short:

- **Phase 0 and 1:** the repository and the seed were read, the author's decisions were recorded (decisions 0002 to 0012), and the plan was approved (`469bcc6`).
- **Phase 2:**
  - working rules `AGENTS.md`, `CLAUDE.md`, `.gitignore` (`16004ea`);
  - the seed moved to `spec/` (`aab55a6`);
  - project memory (`5dcaf06`);
  - `DESIGN.md`, Wayfinding (`82b932d`);
  - README, licences, notices, program map (`bb1d50a`, fix `f11c329`);
  - lesson template and empty lesson tree (`e6d8fa7`).
- **Phase 3:**
  - five skills written here (`b62321f`);
  - pinned third-party skill files, fonts and the Python environment, installed by the author and verified (`c7165a0`);
  - checkers and renderer (`de9f90f`);
  - deck and textbook builders and the `publish` skill (`e71ea17`);
  - skills register and the skills section of `CLAUDE.md` (`0d78083`).
- **Phase 4:**
  - the "done means" checks were run;
  - the cold-start test was run with a fresh sub-agent;
  - its gaps were fixed;
  - this handoff was written;
  - all of it was committed as `4bbab4d`.
- **Lock:** the author confirmed initialization complete. The stage is `build`, and the plan is decision 0001.

## Files changed

Phase 4 changes, committed as `4bbab4d`:

- `README.md`: "each organization" became "the organization", in English and French (check 7).
- `AGENTS.md`:
  - the session start reads the most recent dated handoff;
  - the session end writes the handoff, then updates the state;
  - locked files count from stage `build`.
- `CLAUDE.md`: the author runs `/session-handoff`; otherwise the agent follows the routine in `AGENTS.md`.
- `.ai/project/spec/README.md`: "Nothing else changed" clarified.
- `.ai/project/init-plan.md` (now decision 0001): header status, a note on as-planned paths, the Phase 4 checks, progress entries.
- `.ai/project/state.md`: rewritten for Phase 4 and the lock.
- `.ai/project/handoffs/2026-11-10-initialization.md`: this file.
- `.ai/project/spec/suggestions.md`: suggestion D.5 reduced to its rule, at the author's request (decision 0013, recorded in `.ai/project/decisions/0013-suggestion-d5-reduced-to-rule.md`); `spec/README.md` notes it.

Lock changes, not yet committed:

- `.ai/project/init-plan.md` moved to `.ai/project/decisions/0001-initialization-plan.md`: numbered title, `Status: accepted`, the lock date, and a final progress entry. Its content is otherwise unchanged (plan, section 9).
- `.ai/project/state.md`: `Stage: build`; focus and next steps for the first content step.
- This handoff: the lock recorded.

Locked files changed: none. The lock was made at the author's word: "Lock", 2026-11-10.

## Checks run and results

- **Pass:** `CLAUDE.md` 29 lines, with `@AGENTS.md` on line 1; `AGENTS.md` 149 lines.
- **Pass:** the spec is only in `.ai/project/spec/`; 36 module cards; all 36 rows of the module map have a path with a lesson folder.
- **Pass:** the README carries the copyright line exactly, twice; `LICENSE` is identical to the official CC BY 4.0 legal code.
- **Pass:** every third-party file in the tree is listed in `THIRD_PARTY_NOTICES.md`; all 17 recorded SHA-256 values match.
- **Pass:** `.claude/settings.json` was last changed in the author's pre-init commit. `.ai/prompts/` was never read or written by the agent.
- **Pass:** no tracked file under the deliverable folders other than `.gitkeep`. Trials ran in a scratch area outside the repository.
- **Pass:** every batch is a separate commit, reviewed by the author first.
- **Neutrality:** no organization name, email or absolute path in any tracked file. The one seed sentence explaining why was removed at the author's request.
- **Cold start:** a fresh sub-agent answered all six questions from the files. The gaps it reported are fixed (see "Files changed").
- **Pass:** `state.md` shows `Stage: build`, and this handoff exists (check 11).

## Open questions

None for initialization. The question about suggestion D.5 was answered: reduced to its rule (decision 0013). Content decisions that can wait are in `.ai/project/spec/open-decisions.md`.

## Next step

Build order step 2, the glossary R-02. Settle OD-06 (the glossary candidates to check first) with the author before drafting `resources/R-02-glossary.md`. Then step 3, the fictional engagement brief (OD-11, with `grilling`).
