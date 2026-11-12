# Open decisions

Content and program decisions not yet taken. Each has a proposal and the point by which it has to be settled. When the author decides one, the decision goes into a decision record, the affected card is updated with the author's approval, and the entry here is marked decided with the record's number.

## Problems found in the specification

### OD-01 · Segment 4 timing (P1)

- **Problem:** [S-01](curriculum/session/S-01-run-of-show.md) gives segment 4 ten minutes in the 120-minute booking. Its modules add up to twelve: C-06 5, C-07 5, X-02 2.
- **Proposal:** count X-02's single slide inside C-07's five minutes. That slide is where C-07's data rule points ("where it lives"), so C-07 becomes 3 + 2 and the segment stays at ten minutes. The other option is to raise segment 4 to twelve minutes and take two from the unallocated margin.
- **Settle by:** when C-07 and X-02 are written.
- **Status:** open.

### OD-02 · Two names for one loop (P2)

- **Problem:** [C-04](curriculum/core/C-04-working-loop-and-prompting.md) teaches eight steps: Frame, Give context, Ask, Inspect, Iterate, Verify, Approve, Capture. [S-02](curriculum/session/S-02-workshop.md) says the workshop practises "the same loop" but uses six differently named steps: Frame, Ask, Inspect, Iterate, Verify, Share. A novice room will see two methods.
- **Proposal:** rename the workshop steps after the loop: Frame, Give context and ask, Inspect, Iterate, Verify, Approve. The approval step asks whether you would send the result. Keep "Share" as the debrief, and let debrief question 1 cover Capture.
- **Settle by:** before the C-04 lesson.
- **Status:** open.

### OD-03 · E-06 delivery line (P3)

- **Problem:** [E-06](curriculum/tracks/engineering/E-06-architecture-and-design-work.md) says "Track session 3 or self-serve". Engineering session 3 does not include it, and the track page lists it as self-serve.
- **Proposal:** change the card's delivery line to "Self-serve or dedicated session", matching E-08 and E-09.
- **Settle by:** when E-06 is written.
- **Status:** open.

### OD-04 · Pack A trap needs code execution (P4)

- **Problem:** pack A's trap is found by running a test, but the common session's setup is "a browser and the approved assistant, nothing to install", in a plain chat window.
- **Proposal:** add to the bug report an input and its expected output that the obvious fix gets wrong. Participants then find the trap by tracing the fix against the report, without running anything. Running the test becomes an extra for rooms whose approved tool can execute code.
- **Settle by:** when the S-02 packs are built.
- **Status:** open.

### OD-05 · Checkpoint minutes (P6)

- **Problem:** the track pages count each checkpoint inside its module's minutes. S-01 counts core checkpoints as separate rows.
- **Proposal:** a lesson's front matter `minutes` follows its card's "Time" line. The lesson's own timing table always shows the checkpoint as its own row, so both conventions read the same way. The lesson template (initialization, Batch 5) follows this proposal unless the author decides otherwise.
- **Settle by:** Batch 5.
- **Status:** settled on 2026-11-11 (decision 0017).

### OD-06 · Glossary candidates to check first (P8)

- **Problem:** some candidates in [R-02](curriculum/resources/R-02-glossary-seed.md) look doubtful and need checking in the Grand dictionnaire terminologique: "rédactique" for prompt engineering, "point d'ancrage" for hook, "ajustement fin" for fine-tuning. R-02's terminology policy is also still "to confirm".
- **Proposal:** check every candidate when the glossary is built, starting with these three, and have the author confirm the policy.
- **Settle by:** the glossary (build order, step 2).
- **Status:** settled on 2026-11-10 (decision 0014).

## Backlog items in suggestions.md

Most items in [`suggestions.md`](suggestions.md) are already reflected in the cards, even where they carry no "(in the outline)" marker:

- A.4 to A.7 and A.12;
- B.3, B.4, B.6, B.10, B.11, B.13 and B.15 to B.17;
- C.1 to C.5.

D.1 to D.3 and D.5 to D.8 are covered by `AGENTS.md` and the curriculum conventions, and section E matches the cards. The remaining items need the author's accept or drop.

### OD-07 · Backlog items to accept or drop

| Item | Where it stands | Proposal |
|---|---|---|
| A.11 Name the worry early | B-05 covers role concerns; the S-01 welcome does not | Accept: two minutes inside the welcome segment, with no change to the timing |
| B.12 Evaluation literacy | Partly in C-06 (optional) and P-04 (required: critique against criteria) | Accept as covered; no change |
| C.6 Specification to shipped change, in pairs | Not in the cards | Keep as "later" |
| C.7 Agent security for engineers | Not in the cards | Keep as "later" |
| C.8 Automation and unattended agents | Not in the cards | Keep as "later" |
| D.4 Owner and refresh routine for the snapshot | Not in the cards | See OD-10 |

- **Settle by:** before the S-01 presenter guide is written (for A.11).
- **Status:** open.

## Program decisions that can wait

### OD-08 · Do track textbooks include the core?

- **Proposal:** yes. Each track textbook starts with the core lessons as Part I, so it stands alone as the brief for the textbooks asks.
- **Settle by:** before the first track textbook.
- **Status:** open.

### OD-09 · First track to build

- **Proposal:** R-03 says to start with the track that has the most participants. That depends on the delivery, so the author names the track when the core is done.
- **Settle by:** build order, step 9.
- **Status:** open.

### OD-10 · Who owns the landscape snapshot

- **Proposal:** the owner is the presenter of record for each delivery. The snapshot is refreshed within the week before each delivery and at least once a quarter.
- **Settle by:** before the C-02 lesson.
- **Status:** settled on 2026-11-11 (decision 0018).

### OD-11 · The fictional engagement

- **Proposal:** define the invented client, project, stages and artifacts in an interview with the author, using the `grilling` skill, before the core lessons.
- **Settle by:** build order, step 3.
- **Status:** settled on 2026-11-10 (decision 0016).

### OD-12 · A mark for the program

- **Proposal:** none. The name is set in the chosen typeface as a wordmark. Revisit only if the author wants a logo.
- **Settle by:** any time.
- **Status:** open.

### OD-13 · Release naming for built outputs

- **Proposal:** one GitHub release per delivery, named after its date and session. The author creates releases and tags.
- **Settle by:** the first delivery.
- **Status:** settled on 2026-11-11 (decision 0021): no built file is published, and each delivery's two archives are named after its date and session.

### OD-14 · Where demonstration recordings live

- **Proposal:** outside git, as release assets or in storage the author chooses. The lesson links to the recording and dates it.
- **Settle by:** the C-04 lesson.
- **Status:** settled on 2026-11-11 (decision 0021): outside git, where the delivering organization chooses, with the link in the delivery file.

### OD-15 · Native-speaker review of the French

- **Proposal:** a named role reviews against the glossary before the first delivery and after any large change. The review is recorded in the lesson's front matter.
- **Settle by:** before the first delivery.
- **Status:** open.

### OD-16 · Reference repository for the engineering labs

- **Proposal:** a separate, synthetic repository for the E-03 labs and the E-05 prepared pull request, so that lab work never runs inside this repository's rules.
- **Settle by:** before the engineering track lessons.
- **Status:** open.

### OD-17 · Allow rules for build commands

- **Proposal:** once `tools/` exists, consider allow rules for the build commands to reduce permission prompts. This is a convenience, not a control, and it needs the author's approval because it changes `.claude/settings.json`.
- **Settle by:** any time after initialization, Phase 3.
- **Status:** open.
