# 0022. Relaxed timing and session formats

- Date: 2026-11-11
- Status: proposed
- Supersedes: 0017, 0019

## Context

The first four core lessons showed where the schedule was too tight:

- C-01: six cards sorted in two minutes;
- C-02: a seven-row map, the approved tools and a show of hands in four minutes;
- C-03: a vote on three tasks with a volunteer's explanation in three minutes, and one minute to write three tasks;
- C-04: a live demonstration with two waits for the tool inside ten minutes of talk;
- S-02: seventeen minutes for novices to sign in, generate twice and verify every fact;
- a seven-minute break, a five-minute welcome, a seven-minute recap.

The author's direction, given on 2026-11-11:

- Always err on the relaxed side, with ample room for interaction, examples and exercises.
- The 90-to-120-minute range is an ideal, not a requirement.
- The common session becomes two parts of 90 minutes. The two-hour version is dropped, and no required topic is cut.
- A 15-minute break goes in any session with more than about 100 minutes of content, and about every 90 minutes beyond three hours.
- C-06's practice comes back into the room.

Applied to every core module, the relaxed rules need about 166 minutes of planned time, which fits two parts of 90 minutes.

## Decision

1. **The common session has two parts of 90 minutes,** on the same day or on two days. It has no other format.
   - **Part 1:** the welcome, then segments 1 to 3 (C-01; C-03 and C-02; C-04 and C-05).
   - **Part 2:** a short re-entry, segment 4 (C-06, C-07, X-02), the workshop (S-02), C-08 and the recap.
   - Each part is planned at about 80 to 85 minutes, with at least 5 minutes unallocated.
   - On the same day, a 15-minute break separates the two parts.
   - Every required topic of every core module is taught in the room.
2. **A lesson's minutes** add up these rows:
   - **Talk:** the card's Time line, less the practice and checkpoint minutes it includes. The notes budget (110 words per minute) applies to these minutes only, so existing notes stay valid.
   - **« Questions et échanges »:** about 25 % of the talk minutes, rounded up to whole minutes. A row of its own, with no slide.
   - **Checkpoint:** 5 minutes for each of the session's main checkpoints, 6 for a vote over several items. A checkpoint that S-01 gives no row of its own (C-02, C-05, C-06, C-08, X-02) gets 2 to 3 minutes. Track lessons set at least 5 minutes per checkpoint.
   - **Practice:** every practice a card asks for runs in the room, at about one and a half times the card's minutes and at least 3 minutes. C-04's practice is the workshop, so its lesson has no practice row.
   - **« Attente de l’outil »:** for a live demonstration, about half of the demonstration's talk minutes. A row with no slide.
3. **Workshop:** about 32 minutes in the common session (frame 3, ask 5, inspect 5, iterate 7, verify 6, share 6). In a track session, about one and a half times the card's minutes.
4. **Breaks:** 15 minutes. A session with more than about 100 minutes of content has one. Beyond three hours, there is one about every 90 minutes. Each break sits at a segment boundary.
5. **Running late:** the presenter takes time first from « Questions et échanges », then from the workshop's share-out. A « Si vous êtes en retard » marker may shorten an activity (fewer cards, fewer items to vote on). It never removes a required topic.
6. **Track sessions** keep their modules and are re-timed with the same rules. Each is booked for what it needs, with a break when its content passes about 100 minutes.
7. **C-03's green task** is kept for after the session or for the track workshop. S-02 does not change for it (from decision 0019).
8. **Card Time lines** stay as they are. A lesson derives its minutes from them with the rules above.

## Consequences

- Decision 0017 (lesson minutes and checkpoint rows) and decision 0019 (practice in core lessons) are superseded; 0019's point on C-03's green task is kept as item 7.
- **Conventions:** `check_lesson.py` must accept rows with no slide, and must count talk minutes as the total less checkpoint, practice, exchanges and tool waits. `templates/lesson.md` and the `lesson-writing` skill state the rules; « version de 90 minutes » disappears from them.
- **Specification:** S-01 is rewritten as two parts, with no booking columns and a cut order that keeps every required topic. S-02 gets the 32-minute common-session workshop, and the track pages are re-timed.
- **Program description:** the curriculum index, `AGENTS.md` and the README describe the session as two parts of 90 minutes.
- **Lessons:** C-01 to C-04 are re-timed, and their « version de 90 minutes » markers are rewritten. Their speaker notes keep their word counts.
- **Participant time:** the common session now asks about three hours of each participant, against two before.
