# 0017. Lesson minutes and checkpoint rows

- Date: 2026-11-11
- Status: accepted
- Supersedes: none

## Context

OD-05: the track pages count each checkpoint inside its module's minutes, while S-01 schedules each core checkpoint as a separate row after its segment. With the OD-05 proposal (`minutes` equals the card's "Time" line, checkpoint included), each core lesson would run three minutes shorter than S-01 schedules for its segment and checkpoint. The C-01 card also asks for a card-sort practice, and S-01's segment 1 has no practice slot.

## Decision

1. **Core lessons:** `minutes` is the card's "Time" line plus the checkpoint row that S-01 gives the segment. C-01 is 12 + 3 = 15 minutes. The lesson's timing table shows the checkpoint as its own row, so the lesson matches S-01 row for row.
2. **Track and overlay lessons:** `minutes` is the card's "Time" line, with the checkpoint inside it, as the track pages count it. The checkpoint still has its own row.
3. **C-01 practice:** two minutes in the room, inside the segment. The presenter shows each card and the room calls out its category. The textbook keeps it as an individual exercise.

## Consequences

- OD-05 is settled.
- `templates/lesson.md` states the rule in its guide comment (changed with the author's approval).
- The `lesson-writing` skill (`SKILL.md` and `references/card-to-lesson.md`) still says "the card's figure, as is" and needs the same change, with the author's approval.
- Where a core lesson includes a practice, its talk minutes shrink by that much, and its speaker notes with them.
