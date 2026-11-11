# 0019. Practice in core lessons

- Date: 2026-11-11
- Status: accepted
- Supersedes: none

## Context

Some core cards ask for a practice that S-01 gives no slot to. C-03 asks participants to write down one task of each colour, and segment 2 has no practice row. C-06 asks for a three-minute search for planted errors inside a five-minute card. Decision 0017 settled only C-01's practice (two minutes in the room).

C-03's card also says the green task is reused "in the workshop". The common-session workshop (S-02) uses prepared packs, and its design principles allow synthetic material only.

The author approved both points as proposed on 2026-11-11.

## Decision

1. **Short practice runs in the room.** A core practice of one or two minutes runs in the room, inside the card's time. It has its own "Pratique" row in the timing table, and the talk minutes shrink by as much.
2. **Longer practice goes to the textbook.** A core practice that does not fit becomes an individual exercise in the lesson's "Pratique" section, for the textbook and for after the session. It has no row in the timing table. The speaker notes point to it in one sentence.
3. **C-03:** one minute of silent writing in the room.
4. **C-03's green task:** participants keep it to try with the working loop after the session, or in their track workshop. S-02 does not change.

## Consequences

- C-03 has 9 minutes: 5 of talk, 3 for the checkpoint and 1 for the practice.
- C-06's practice will be placed under this rule when its lesson is written.
- `check_lesson.py` already counts only the rows the table has, so no tool change is needed.
