# Handoff: deliverables by role, Phase 1

- Date: 2026-11-11
- Stage: build

## Goal

On the branch `deliverables-by-role`, made by the author for this work: evaluate deliverables tailored to each role (learner, presenter), then implement Phase 1 of the agreed plan, the decisions and the specification.

## Done

- **Evaluation**, in conversation, of:
  - deliverables by role;
  - build settings and delivery data;
  - packaging and releases;
  - a design revision;
  - the presenter's timing.
- **The author's answers,** 2026-11-11:
  - Lessons stay one self-contained source each; no split by role.
  - Learners get slides as PDF, never a PPTX.
  - Books go to learners after the session by default. `before` is a build setting, and in that mode the presenter guide warns automatically that participants may have read ahead.
  - The presenter is « la personne qui présente »; the presenter guide absorbs the S-01 guide.
  - Learner textbook: a pleasant study book, following good practice in instructional design. Presenter guide: efficiency, usable standing in a room; it repeats no learner text.
  - Schedule times are `relative` or `clock`, switched in `.env`. The start time lives in the delivery file. A committed `.env.example` documents the settings.
  - Pages are US Letter by default, with A4 as a setting.
  - The three fixes are approved: the writing rule, « Corrigé » headings, leak checks.
  - Delivery data goes in non-committed files, with a committed example.
  - Two archives per delivery, properly named. No built file is ever attached to a GitHub release; the project publishes sources only.
  - Design: revise it toward more energy, professional, with visuals and illustrations now and then. Samples come first, on existing core lessons, as real PPTX and PDF, including extra font weights as needed; then the author chooses.
  - Timing: err on the relaxed side. The main format stays 2 hours, with 2 × 90 minutes as an option. A 15-minute break goes in any session with more than about 100 minutes of content, and every 90 minutes or so beyond 3 hours. C-06's practice comes back into the room. The 90–120-minute range is an ideal, not a constraint.
  - Illustrations: staying geometric is not acceptable; the author asked for tools and solutions (see the plan, Phase 4). The author confirmed that local image generation is feasible on their machine.
  - No worktree: work happens directly on this branch.
- **Phase 1, implemented** (permission: "Implement up to phase 1. All locked files involved in that phase are approved for edits, for this phase."):
  - decision 0020, deliverables by role (`proposed`);
  - decision 0021, build configuration, delivery data and packaging (`proposed`, supersedes 0005);
  - the specification, `AGENTS.md`, the README and `.gitignore` aligned with both.

## Files changed

Batch 5a (Phase 1, decisions and specification):

- `.ai/project/decisions/0020-deliverables-by-role.md`: new, proposed.
- `.ai/project/decisions/0021-build-configuration-and-packaging.md`: new, proposed.
- `.ai/project/state.md`, this handoff.

Locked files changed under the Phase 1 permission quoted above, 2026-11-11:

- `.ai/project/spec/deliverables.md`:
  - roles in the introduction;
  - lesson item 8 (the writing rule);
  - the presenter guide as a built deliverable;
  - roles for workshop packs;
  - handouts in the configured page format;
  - deck for the presenter, never published;
  - new « Learner slides »;
  - textbook role and « Corrigé » placement;
  - new « Delivery packages »;
  - `guides/` manifests;
  - the recording's location.
- `.ai/project/spec/build-order.md`: step 5 (guide sources in `guides/common-session/`), steps 7 and 12 (learner slides and presenter guides), and the delivery file and archives before each delivery.
- `.ai/project/spec/module-map.md`: S-01's deliverable is now `guides/common-session/`. This file was not named in the plan's Phase 1 list; it was edited as part of the same change, and the author may object.
- `.ai/project/spec/open-decisions.md`: OD-13 and OD-14 settled by decision 0021.
- `.gitignore`: `deliveries/` (except `README.md` and `example.toml`), and a safety net for PDF, PPTX, ODP and ZIP files; the `build/` comment no longer mentions release assets.
- `AGENTS.md`: map rows for `guides/`, `deliveries/`, `build/` and `.env.example` (`sessions/` removed); a « Delivery data » content rule.
- `README.md`, both halves: textbooks and slides built by whoever delivers, sources only published; presenter guide; building a delivery.

## Checks run and results

- `git status` at the start: clean, on `deliverables-by-role`.
- `git ls-files` for PDF, PPTX, ODP and ZIP files: none committed, so the safety-net patterns hide nothing.
- `git check-ignore`:
  - ignored: `deliveries/x.toml`, `foo.pdf`, `build/dist/a.zip`, `.env`;
  - not ignored: `deliveries/example.toml`, `.env.example`.
- `tools/check_french.py` on the French half of the README: 0 hits. One wording change for épicène writing: « les personnes qui suivent la formation » instead of a doublet.

## The plan (Phases 2 to 7)

Each phase needs the author's permission, and each locked file needs an approval that names it.

1. **Phase 2, conventions:**
   - glossary entry « personne qui présente » (checked in the GDT); the brief's « la personne qui anime » aligned;
   - a shared lesson parser for `tools/`; in `check_lesson.py`, the leak check, « Corrigé » and timing rows without a slide;
   - the writing rule, « Corrigé » and the timing rows in `templates/lesson.md` and the `lesson-writing` skill;
   - C-01 to C-04 revised (their changed passages need a new native review);
   - S-01, S-02 and the three track pages re-timed;
   - `guides/` added to the `canadian-french` skill's scope.
2. **Phase 3, build settings:** `tools/config.py` (`.env` read with the standard library), `.env.example`, `deliveries/README.md` and `example.toml`, Letter or A4, learner slides as PDF, `after` and `before` modes, delivery data filled in at build time.
3. **Phase 4, design samples:**
   - a theme layer in the builders, kept afterwards;
   - pictograms (about 10, drawn in-house) and diagrams for C-01 to C-04;
   - a prototype presenter guide;
   - three directions (A Signalétique, B Éditorial, C Atelier illustré), each as real PPTX and PDF, rendered and inspected;
   - the author chooses.
4. **Phase 5:** `DESIGN.md` rewritten, a decision superseding 0003, the `visual-design` skill and `layouts.md` updated, unused themes removed.
5. **Phase 6:** the presenter guide builder, with a schedule manifest, formats and relative or clock times.
6. **Phase 7:** packaging, leak checks, the `publish` skill and `tools/README.md`.

**Illustration options for Phase 4,** each needing the author's approval to install or download. Licences must be confirmed on their source pages before use.

- **Local text-to-image generation:**
  - Hugging Face diffusers, or ComfyUI, in a separate environment outside `tools/requirements.txt`; images are committed as source assets with a provenance record.
  - Candidate models: FLUX.1 [schnell], Stable Diffusion XL, Stable Diffusion 3.5. FLUX.1 [dev] is out because of its non-commercial licence.
  - A palette-mapping script recolours images to the design tokens and checks contrast; optionally a small style LoRA for a house style, and vectorization to SVG (vtracer).
- **Composable human-drawn illustration kits** released under CC0, such as Open Peeps or Open Doodles (to confirm), recoloured to the tokens.
- **A commissioned illustrator** for a small signature set.

`DESIGN.md` 5.2 currently bans generated images of people and imagery that stands for "AI"; Phase 5 would revise the first rule, not the second.

## Open questions

1. **What the 2-hour main format teaches in the room.** With the relaxed rules, today's in-room content needs about 184 minutes. The 2-hour booking, with its 15-minute break (more than 100 minutes of content), leaves about 100 minutes of content. Recommended: the 2-hour format teaches C-01, C-03, C-04 (with C-05's point named during the demonstration), C-07 with X-02, the workshop, and C-02 as one slide. C-05, C-06 and C-08 are taught fully in the 2 × 90-minute format and are in the textbook. The alternative keeps every module in 2 hours with only partial relaxing.
2. Accept decisions 0020 and 0021.
3. The README's « Status » paragraph still says nothing is built yet, while four lessons exist. Update it in a later batch?
4. (Carried over) Does the native review of C-04 cover the glossary's « Étapes de la boucle de travail » table?

## Next step

Ask the open questions. Then write the timing decision, the third record of Phase 1, from the author's answer. Phase 2 starts only with the author's permission.
