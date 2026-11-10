# Decision records

Short, dated records of what was chosen and why. One decision, or one group of tightly linked decisions, per record.

## Rules

- **File name:** `NNNN-<slug>.md`, numbered in sequence from `0001`. A number is never reused. `0001` is the initialization plan, which moves here when initialization is locked.
- **Status:** `proposed` or `accepted`. An agent may draft a record as `proposed`; only the author makes it `accepted`.
- **Accepted records are never edited.** To change a decision, write a new record whose `Supersedes:` line names the old one. To find out whether a record still holds, search the folder for `Supersedes: NNNN`.
- **No index file.** The folder listing is the index.
- **Contents:** no secrets, no personal data, no conversation transcripts. State reasons in terms of the project.

## Format

```markdown
# NNNN. Title

- Date: YYYY-MM-DD
- Status: proposed | accepted
- Supersedes: NNNN | none

## Context

What made a decision necessary, in a few lines.

## Decision

What was chosen, stated so that it can be checked.

## Consequences

What follows from it, including what it rules out.
```
