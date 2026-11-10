---
name: session-handoff
description: End-of-session routine. Updates .ai/project/state.md, writes the session's handoff from the template, and gives a suggested commit message.
disable-model-invocation: true
argument-hint: "[what the next session should start with]"
---

# Session handoff

Run this at the end of a work session, or when context is running low. The aim: a session that knows nothing about this one can continue from the files alone.

## Procedure

1. **Collect the facts from the repository, not from memory.**
   - `git status -- . ':(exclude).ai/prompts'`
   - `git diff --stat -- . ':(exclude).ai/prompts'`
   - `git log --format='%h %s' -10 -- . ':(exclude).ai/prompts'`
2. **List what happened in this session:**
   - the goal;
   - what was completed;
   - every file created, changed, moved or deleted, and why;
   - every check run and its result, including failures;
   - the open questions, each with a recommended answer;
   - the next step. If the author passed an argument, it shapes this step.
3. **Locked files** (stage `build` only). For each locked file changed, quote the author's approval as given, with its date. If a locked file changed without an approval in this session, say so plainly at the top of the handoff.
4. **Write** `.ai/project/handoffs/YYYY-MM-DD-<slug>.md` from `.ai/project/handoffs/TEMPLATE.md`.
   - Use today's date and a short slug for the work.
   - If that file name already exists, add `-2`, `-3` and so on.
   - Point to files, commits and decision records instead of restating them.
5. **Update** `.ai/project/state.md`: current focus, next steps, open questions, last updated. Leave the `Stage:` line alone unless the author changed the stage.
6. **Screen both files.** Remove any secret, any personal data, any detail of a particular machine (operating system, installed versions, security settings, other devices) and any transcript.
7. **Give the author a suggested commit message:** Conventional Commits, a subject of at most 72 characters, a blank line, then a 2 to 5 line body, no trailer.

## Acceptance check

- [ ] All six parts of the template are filled: goal, done, files changed, checks run and results, open questions, next step.
- [ ] Every locked-file change carries its quoted approval, or is flagged at the top.
- [ ] `state.md` reflects the handoff, and its `Stage:` line is unchanged unless the author changed it.
- [ ] Neither file contains a secret, personal data, machine details or a transcript.
- [ ] The suggested commit message follows the convention.
