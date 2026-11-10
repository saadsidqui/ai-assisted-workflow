# Claude Code

Facts checked against the Claude Code documentation and release notes. "Quoted" means the wording was read on the page; "summary" means it came from a summary of the page and was not seen word for word.

## Instruction files

- 2026-11-10: Claude Code reads `AGENTS.md` only when there is no `CLAUDE.md` in the working directory or above it. `CLAUDE.local.md` and `.claude/CLAUDE.md` count as a `CLAUDE.md` for this check. Quoted. Source: https://code.claude.com/docs/en/memory
- 2026-11-10: the behaviour above arrived in release 2.1.277 and can be changed under "Project instructions" in `/config`. Quoted. Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
- 2026-11-10: the documentation suggests a `CLAUDE.md` that imports `@AGENTS.md`. Imported files are "expanded and loaded into context alongside the CLAUDE.md that references them". Quoted. Source: memory page.
- 2026-11-10: "Project-root CLAUDE.md survives compaction: after `/compact`, Claude re-reads it from disk and re-injects it into the session." Nested `CLAUDE.md` files load again on demand. Quoted, from the section "Troubleshoot memory issues". Source: memory page.
- 2026-11-10: guidance: "target under 200 lines per CLAUDE.md file". Quoted. Source: memory page.
- 2026-11-10: auto memory lives in `~/.claude/projects/<project>/memory/`, per repository, shared across worktrees, and stays on the local machine. Quoted, except "local machine", which is summary. Source: memory page.

## Skills

- 2026-11-10: project skills load from `.claude/skills/<name>/SKILL.md`, in the starting directory and every parent up to the repository root. Quoted. Source: https://code.claude.com/docs/en/skills
- 2026-11-10: instruction files under `.agents/` are not read (quoted, memory page). The skills page lists the places skills load from, and `.agents/` is not among them (summary).
- 2026-11-10: "Keep `SKILL.md` under 500 lines. Move detailed reference material to separate files." Quoted, from the section "Add supporting files". Source: skills page.
- 2026-11-10: the `description` is what Claude uses to decide when to apply a skill. The `description` and `when_to_use` text together are truncated at 1,536 characters in the skill listing. Quoted. Source: skills page.
- 2026-11-10: `disable-model-invocation: true` stops Claude from loading a skill on its own; it is then run with `/name`. Quoted. Source: skills page.
- 2026-11-10: auto-compaction re-attaches skills already invoked, keeping the first 5,000 tokens of each, within 25,000 tokens in total. Quoted. Source: skills page.

## Permissions and settings

- 2026-11-10: rules are evaluated in this order: deny, then ask, then allow. An allow rule cannot carve an exception out of a deny rule. Quoted. Source: https://code.claude.com/docs/en/permissions
- 2026-11-10: Read and Edit deny rules also apply to file commands that Claude Code recognizes in Bash (such as `cat`, `head`, `tail`, `sed`, `tee`) and to redirection targets. They do not apply to a command that reads files without naming them. Bash rules match the command text. Quoted. Source: permissions page.
- 2026-11-10: a Bash command whose arguments named a read-denied path was denied, even though the path appeared only in an exclusion clause. Observed.
- 2026-11-10: writes to protected paths, including `.claude/` and `.git/`, are never auto-approved except in `bypassPermissions` mode. Allow rules do not pre-approve them. Quoted for the first sentence, summary for the second. Source: https://code.claude.com/docs/en/permission-modes
- 2026-11-10: in auto mode, a classifier reviews actions before they run. It sees user messages, tool calls and `CLAUDE.md` content. Summary; whether it expands `@` imports was not found. Source: permission-modes page.
- 2026-11-10: settings precedence, from highest to lowest: managed, command line, local project (`.claude/settings.local.json`), shared project (`.claude/settings.json`), user (`~/.claude/settings.json`). A project `effortLevel` therefore overrides a user one. Quoted. Source: https://code.claude.com/docs/en/settings
