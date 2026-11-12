# Project state

Stage: build

Last updated: 2026-11-11

## Current focus

Branch `deliverables-by-role`: deliverables tailored to each role (learner, presenter), build settings, packaging, a design revision and a relaxed timing model. The author approved a plan in seven phases (see the latest handoff); Phase 1 is complete once batch 5b is committed.
- Decisions 0020 (deliverables by role) and 0021 (build configuration and packaging) are accepted. Decision 0022 (relaxed timing; the common session as two parts of 90 minutes, every required topic taught) is `proposed`.
- Illustrations will come from local image generation with ComfyUI (option 1 only), installed with the author's approval in Phase 4.
- On the main line, C-01 to C-04 are written and native-reviewed; C-05 to C-08 resume after Phase 2.
- **Waiting for:** the author's review and commit of batch 5b, acceptance of decision 0022, and permission for Phase 2.
- **Latest handoff:** `.ai/project/handoffs/2026-11-11-deliverables-by-role.md`.

Initialization is complete and locked. The plan and its history are decision 0001.

## Next steps

1. **Phase 2, conventions** (needs permission; locked files need approvals that name them; the README « Status » fix is already approved for this phase):
   - glossary entry « personne qui présente », and the brief aligned;
   - shared lesson parser; `check_lesson.py` with the leak check, « Corrigé », and rows with no slide (decision 0022);
   - `templates/lesson.md` and the `lesson-writing` skill;
   - C-01 to C-04 revised and re-timed;
   - S-01 as two parts, S-02, the track pages, the curriculum index, `AGENTS.md` and the README re-timed;
   - `guides/` in the `canadian-french` skill's scope.
2. Phases 3 to 7: build settings, design samples (three directions, real PPTX and PDF, illustrations made with ComfyUI), the chosen design in `DESIGN.md`, the presenter guide builder, packaging.
3. Then C-05 to C-08 under the new conventions, and R-01.

## Open questions

None.

Content and program decisions that can wait are in `.ai/project/spec/open-decisions.md`.
