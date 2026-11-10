@AGENTS.md

# Claude Code

What is specific to Claude Code. Every working rule is in `AGENTS.md`, imported above.

## Project skills

None yet. Phase 3 of the initialization plan adds them here, one line each on when to use it.

## Routing

For decks, PDF textbooks and any document output, use the project skill `publish` once it exists. Do not use an account-level document skill such as `pptx` or `pdf`.

## Memory

Auto memory under `~/.claude/` stays on this machine and is not the project's memory. Anything the project must remember goes in `.ai/project/`: `state.md`, a decision record or a knowledge note.

## Hard boundaries

Restated from `AGENTS.md`, which stays authoritative:

- Never run a git command that changes the index, the history or the branches.
- Never read, list, search or write `.ai/prompts/`.
