@AGENTS.md

# Claude Code

What is specific to Claude Code. Every working rule is in `AGENTS.md`, imported above.

## Project skills

- `lesson-writing`: write or revise a lesson from its module card.
- `canadian-french`: check any French deliverable before it is reported done.
- `slop-check`: check text and visuals for machine-made patterns before they are reported done.
- `visual-design`: diagrams, README images, slide and page layout, contrast.
- `publish`: build and inspect decks and PDF textbooks. Use it instead of any account-level document skill, such as `pptx` or `pdf`.
- `grilling`: interview the author to settle an open decision or a gap in the specification.
- `writing-for-agents`: change `AGENTS.md`, `CLAUDE.md` or a skill (locked files: approval first).
- `/session-handoff`: run it at the end of every work session.

The register, with sources and versions, is `.ai/project/skills-register.md`.

## Memory

Auto memory under `~/.claude/` stays on this machine and is not the project's memory. Anything the project must remember goes in `.ai/project/`: `state.md`, a decision record or a knowledge note.

## Hard boundaries

Restated from `AGENTS.md`, which stays authoritative:

- Never run a git command that changes the index, the history or the branches.
- Never read, list, search or write `.ai/prompts/`.
