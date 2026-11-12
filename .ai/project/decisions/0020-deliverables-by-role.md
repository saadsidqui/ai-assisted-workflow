# 0020. Deliverables by role: learner and presenter

- Date: 2026-11-11
- Status: accepted
- Supersedes: none

## Context

Until now, the same outputs served everyone: a deck with speaker notes, and a textbook that leaves out the slides and the notes. The presenter had no document of their own. Their material (run of show, checklists, timing, re-verify lists, answer keys) was spread over S-01, S-02 and every lesson.

The two roles need different things:

- The learner needs a pleasant study book that follows good practice in instructional design and is easy to read. They need none of the presenter's material.
- The presenter needs efficiency: checklists, the schedule, notes and instructions, in a form usable in a room, standing, at some distance from a page or a screen.

The author settled the points below on 2026-11-11, after an evaluation in conversation.

## Decision

1. **One source per module.** A lesson stays one self-contained Markdown file. It holds the learner text, the slides, the speaker notes and the presenter sections, and every deliverable is built from it. Lessons are not split by role.
2. **Deliverables by role:**

   | Role | Deliverable | Format | Built from |
   |---|---|---|---|
   | Learner | Textbook | PDF | Learner text of the lessons |
   | Learner | Slides | PDF, no speaker notes | The deck |
   | Learner | Handouts and the participant page of each workshop pack | PDF | `handouts/`, `workshops/` |
   | Presenter | Deck | PPTX with speaker notes | Slide regions and notes |
   | Presenter | Presenter guide | PDF | Presenter sections and notes of the lessons, the guide's own sources, the workshop facilitator guide |
   | Presenter | Presenter copies of the workshop packs | PDF | `workshops/` |

   Learners never receive a PPTX: it is the one format where speaker notes can travel unseen.
3. **The presenter guide replaces the separate S-01 guide.** It holds:
   - a run sheet for the session;
   - preparation checklists (a week before, the day before, in the room);
   - every re-verify item of the lessons used, with its last-checked date;
   - one chapter per segment, with each slide shown small, its notes, the timing and the stage directions set apart, cut markers and checkpoint boxes with their answer keys;
   - the workshop facilitator guide and the presenter copies of the packs;
   - an after-session checklist.

   It does not repeat the learner text. Its French sources (checklists, front matter) live in `guides/`.
4. **Writing rule for lessons:**
   - The learner text speaks only to the reader. Anything about the room (minutes in session, what the presenter does, the protocol) goes in the speaker notes or in the « Déroulement » section.
   - Answer keys go under their own heading, « Corrigé ». The textbook places them at the end of the chapter; the presenter guide shows them in the checkpoint or practice box.
5. **Leak checks:**
   - `tools/check_lesson.py` flags room-facing phrases in the learner text.
   - Before learner outputs are handed over, their text is searched for traces of speaker notes and stage directions.
6. **When learners receive the books** is a build setting:
   - `after` (the default): « Corrigé » sections stay at the end of each chapter.
   - `before`: they move to an appendix, the front matter speaks of the session to come, and the presenter guide states automatically that participants may have read the checkpoints and the demonstration in advance.
7. **Page format:** US Letter by default, with ISO A4 available as a build setting. Page geometry is derived from the format, never fixed in the code. Slides stay 16:9.
8. **The presenter is named « la personne qui présente »** in every French deliverable. The glossary records the term and the brief is aligned with it.
9. **Design:** the two roles may share one visual direction or not. The design is revised separately: samples first, then a decision by the author.

## Consequences

- `deliverables.md` defines the learner slides, the presenter guide and the role of each output.
- The lesson template, the `lesson-writing` skill and `check_lesson.py` gain the writing rule, the « Corrigé » heading and the leak check (planned next).
- C-01 to C-04 are revised to the writing rule; their changed passages need a new native-speaker review.
- New builders are needed: learner slides, presenter guide.
- In `before` mode, the books can still reveal what the session lets people discover (the C-04 demonstration, the C-03 vote). The mode moves answer keys and warns the presenter; it does not rewrite the units.
