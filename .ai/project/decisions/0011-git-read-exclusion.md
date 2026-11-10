# 0011. Git read commands exclude the human-owned folder

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

Git read commands such as `status`, `diff`, `show` and `log -p` print file names and contents from every tracked path. That includes `.ai/prompts/`, which agents must never read.

## Decision

1. **Pathspec:** every git command an agent runs that lists files or shows content ends with the pathspec `-- . ':(exclude).ai/prompts'`.
2. **Settings:** no permission rule or hook enforces this; the rule is an instruction.

## Consequences

- The rule lives in `AGENTS.md`, in the git section and the session routine.
- It relies on the agent following instructions and on the author's review. A hook could enforce it later if the author asks.
