# 0010. Problems in the specification become open decisions

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

Reading the planning input turned up these problems:

- a timing that does not add up (segment 4 of S-01);
- two names for one working loop (C-04 and S-02);
- a delivery line that contradicts its track page (E-06);
- a workshop trap that needs code execution in a chat-only setup (S-02, pack A);
- two conventions for counting checkpoint minutes.

## Decision

Initialization does not fix these. Each one is recorded in `spec/open-decisions.md` with a proposed fix (OD-01 to OD-05) and is resolved when the affected lesson or pack is written. The author approves any change to a card.

## Consequences

Setup writes no content. Each fix lands next to the lesson it affects, where its effect can be checked.
