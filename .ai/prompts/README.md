# Running the init prompt

Notes for you, not for Claude. This folder is ignored by git and read-denied to Claude by your `.claude/settings.json`, so nothing here reaches the repository or the session unless you paste it.

## What the archive adds

Unzipped at the repository root, it adds two things and overwrites nothing:

| Path | What it is | Tracked by git |
|---|---|---|
| `.ai/project/seed/` | The curriculum outline (46 files), the suggestions and a short index. Claude reads it as the specification. | Yes |
| `.ai/prompts/` | `00-init.md` (the prompt) and this file | No (ignored) |

## Before you start

1. Unzip at the repository root.
2. Commit the seed, so that everything Claude does afterwards shows up as a clean diff:
   `git add .ai/project/seed && git commit -m "Add curriculum seed"`
3. Update Claude Code and check the version: `claude update`, then `claude --version`. Reading `AGENTS.md` natively needs 2.1.277 or later, and from 2.1.283 auto mode is the default for interactive sessions on every plan.
4. Model and effort come from your `.claude/settings.json` (`claude-opus-5-5`, `high`). Nothing to do.

## Start

From the repository root:

```bash
claude "$(cat .ai/prompts/00-init.md)"
```

Your shell reads the file and passes its text; Claude never opens the folder. An `@.ai/prompts/00-init.md` mention will not work, because your deny rule blocks it. Pasting the file's contents as the first message works too.

Launch from the root every time. Your rules use `./` paths, which Claude Code resolves against the directory it was started in. Started from a subfolder, `Read(./.ai/prompts/**)` would no longer cover the real folder.

Auto mode: current versions start interactive sessions in it. If yours does not, start with `claude --permission-mode auto "$(cat .ai/prompts/00-init.md)"`. Setting `"defaultMode": "auto"` in the project's `.claude/settings.json` has no effect; Claude Code only honours it in `~/.claude/settings.json`.

## What happens

| Stop | Claude has done | You do |
|---|---|---|
| End of Phase 0 | Read everything, written nothing. Reports what it found and asks its questions, including two or three visual directions. | Answer. Pick a direction. |
| End of Phase 1 | Written one file: `.ai/project/init-plan.md` | Read it in your editor. Reply with approval or changes. |
| After each batch in Phase 2 (five batches) | Written a few files and reported, with a suggested commit message | `git diff`, commit, reply `next` |
| End of Phase 3 | Written the project skills you approved and listed the commands for third-party ones | Install what you accept, commit, reply `next` |
| End of Phase 4 | Checked everything, run a cold-start test, written the first handoff | Reply `lock`, then commit |

If the conversation is interrupted, `claude --continue` picks it up. If you start fresh instead, pass the prompt again and add: "Resume from `.ai/project/init-plan.md`; do not repeat finished phases." The prompt has Claude keep a progress note in that file for this purpose.

## Your settings file, as it stands

I left `.claude/settings.json` untouched and added no locks. Five things worth knowing about how it behaves:

1. **Commits and pushes are not blocked by any rule.** The auto mode documentation lists nothing that blocks a plain commit (local operations in the working directory are allowed), and it allows a push to the repository's own remote by default. Your ownership of commits rests on three things: the prompt states it (the classifier treats a boundary you state as a reason to block), `AGENTS.md` will carry it (and is reloaded after compaction), and the repository has no remote yet. By your criterion that is enough today. The day you add a remote, this is the one lock I would reconsider:

   ```json
   "deny": ["Bash(git push *)"]
   ```

   It stops the usual spelling of the command. Claude Code's documentation is explicit that a rule on command text is not a security boundary.

2. **The post-init lock is a rule Claude follows, not a barrier.** It lives in `AGENTS.md` and is backed by your review of every diff. `.claude/` already gets extra scrutiny as a protected path in every mode. If you ever want the lock enforced, add edit-deny rules for the governance files (adjust the specification path to what the plan settles on); they bind Claude only, and you keep editing the files yourself:

   ```json
   "deny": [
     "Edit(/AGENTS.md)", "Edit(/CLAUDE.md)", "Edit(/DESIGN.md)",
     "Edit(/README.md)", "Edit(/LICENSE)", "Edit(/.claude/**)",
     "Edit(/.ai/project/spec/**)"
   ]
   ```

3. **The deny rule on `.ai/prompts/` covers Claude's file tools and the shell commands Claude Code recognizes** (`cat`, `head`, `sed`, redirections). It does not cover every possible subprocess. The prompt also tells Claude to stay out. That is adequate for prompt files; do not keep credentials there.

4. **The sandbox is off.** If you turn it on later, Mint 22.x needs `bubblewrap` and `socat`, and, like other Ubuntu 24.04 derivatives, an AppArmor profile for `bwrap` before user namespaces work. The sandboxing page in the Claude Code documentation has the profile.

5. **Auto memory is on by default and lives under `~/.claude/projects/`, outside the repository.** The prompt tells Claude not to record the neutrality reasoning anywhere, memory included. To be certain nothing from this conversation is kept there, start the session with `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in front of the command.

## One documentation discrepancy

Claude Code's release notes for 2.1.277 say it reads `AGENTS.md` when no `CLAUDE.md` exists. Its memory documentation page still says it reads `CLAUDE.md` and not `AGENTS.md`. The prompt sidesteps the question: a `CLAUDE.md` that imports `AGENTS.md` works under either description.

## After init

A build session starts with a normal request, for example "Write the lesson for C-01". `AGENTS.md` tells the session what to read first, how to work and when to stop. Keep later prompts in this folder if you want them out of the repository.
