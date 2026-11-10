# 0009. Seed moved into the specification folder

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

The specification must live in one place, without a duplicate. Seven sentences in the planning input referred to documents that are not in the repository: an earlier plan, earlier approaches, a brief and an audience request.

## Decision

1. **Move:** the planning input moved from `.ai/project/seed/` to `.ai/project/spec/` as plain file moves.
2. **Rewording:** seven sentences were reworded so that each stands alone, with its point unchanged:
   - C-02 line 8;
   - X-03 line 8;
   - `suggestions.md` lines 13, 20, 21, 29 and 30.
3. **Nothing else** in the planning input was edited.

## Consequences

- The specification can be read and checked without any outside document.
- Git shows the move as renames, with seven changed lines.
