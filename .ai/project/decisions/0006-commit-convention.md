# 0006. Commit message convention

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

The agent suggests commit messages; the author makes every commit.

## Decision

1. **Format:** suggested messages follow Conventional Commits, `type(scope): summary`. The summary is imperative and at most 72 characters.
2. **Body:** a blank line follows the subject, then a body of two to five lines.
3. **Trailer:** none.
4. **Types:** `feat`, `fix`, `docs`, `build`, `refactor`, `style`, `chore`.
5. **Scope:** a module ID or an area: `init`, `spec`, `design`, `skills`, `tools`.

## Consequences

- History can be filtered by module ID or area.
- The blank line keeps git from folding the body into the subject, which happened to one commit before the rule was written down.
