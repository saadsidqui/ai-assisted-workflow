# S-02 · Hands-on workshop

- **Who:** everyone in the common session; longer versions in each track
- **Time:** 17 minutes in the common session (14 in the short version), 25 minutes in a track session
- **Setup required:** a browser and access to the approved assistant. Nothing to install.

Everyone practises the same loop ([C-04](../core/C-04-working-loop-and-prompting.md)) on material from their own kind of work. The exercise is built so that the verification step finds something, because a workshop where the first answer is perfect teaches the wrong lesson.

## Design principles

- **One loop, three packs.** The steps are identical for all roles. Only the input and the expected deliverable change.
- **A planted trap in every pack.** Each pack contains one gap or contradiction that an assistant will usually paper over with something plausible. Participants who verify find it. The debrief is about that moment.
- **Synthetic material only.** One fictional client and one fictional project are used across all packs and all track workshops, so that the tracks work on different stages of the same engagement ([X-03](../overlays/X-03-end-to-end-engagement-map.md)).
- **No dependence on a paid feature.** The exercise works in a plain chat window.
- **A fallback for every pack.** A pre-generated first draft is included, so the inspect and verify steps still work if the tool is down or someone cannot sign in.

## Steps

| Step | Minutes | What participants do |
|---|---|---|
| 1. Frame | 2 | Read the pack. Write one sentence: what is the deliverable and who is it for? |
| 2. Ask | 3 | Brief the assistant with the goal, the material and the format. Get a first draft. |
| 3. Inspect | 3 | Compare the draft with the pack. Note two weaknesses. |
| 4. Iterate | 4 | Give specific feedback or add missing context. Get a second draft. |
| 5. Verify | 3 | Check every fact, name and number against the pack. Find what was invented or blended. |
| 6. Share | 2 | Tell a neighbour one thing the assistant did well and one thing that needed you. |

## The three packs

| Pack | For | Input | Deliverable | Planted trap |
|---|---|---|---|---|
| A · Engineering | Developers, architects, QA, DevOps | A short function, a bug report, and a one-line coding convention | An explanation of the bug, a proposed fix and one test | The bug report describes a symptom that the obvious fix does not address. A test written from the fix passes; a test written from the report fails. |
| B · Product and experience | PM / PO, analysts, designers | Messy notes from a fictional discovery meeting | Decisions, actions, open questions, and two user stories with acceptance criteria | Two attendees state incompatible deadlines. A good result flags the conflict; a typical first draft picks one silently. |
| C · Business and people | Management, HR, business development, others | Bullet notes after a fictional client call, plus an earlier email | A client-ready follow-up message and a three-line internal summary | The notes do not contain a delivery date. A typical first draft includes one anyway. |

Each pack is one page: the material, the task, and a five-line review checklist. The presenter's copy adds the trap, the expected findings and the fallback draft.

## Debrief

Three questions, asked to the whole room:

1. What changed between your first and second draft, and what did you add to get there?
2. Who found something in the result that was not in the material?
3. Would you have sent the first draft?

The second question is the centre of the session. Give it time.

## Success criteria

A participant has succeeded when they:

- supplied the material instead of asking from memory,
- made at least one iteration with specific feedback,
- found the planted trap or another unsupported statement,
- can say who is accountable for the final result.

## Track versions

The 25-minute versions keep the same six steps and continue the same fictional engagement.

| Track | Exercise | Deliverable | Module |
|---|---|---|---|
| Engineering | A small, bounded change in a prepared sample repository, taken through the safe change loop | A reviewed diff, passing tests, a handoff note; the participant makes the commit | [E-02](../tracks/engineering/E-02-safe-change-loop-and-git.md) |
| Product and experience | From the fictional discovery brief to a backlog slice | Three stories with testable acceptance criteria, each traceable to the brief | [P-02](../tracks/product-experience/P-02-requirements-and-specs.md) |
| Business and people | From rough notes to client communication | A client-ready message and an internal summary, every claim checked | [B-01](../tracks/business-people/B-01-communications-and-documents.md) |

## Facilitation notes

- Test each pack with the exact tool and account type participants will use. Outputs differ between plans.
- Show the timer. Announce each step change.
- Pair people who are uncomfortable with the tool. Pairs also talk through the verification, which is the point.
- Do not rescue a weak first draft. The weak draft is the teaching material.
- If the room finds the trap quickly, ask how they would have found it in a ten-page document.

---

← [S-01 Run of show](S-01-run-of-show.md) · [Curriculum index](../README.md)
