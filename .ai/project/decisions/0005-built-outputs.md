# 0005. Built outputs are not committed

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

Decks and PDF textbooks are binary files rebuilt whenever their sources change.

## Decision

Build output goes to `build/`, which git ignores. When a delivery is scheduled, the author attaches the built files to a GitHub release.

## Consequences

- History stays text-only.
- Readers get built files from releases, not from the repository tree.
- Release naming is open decision OD-13.
