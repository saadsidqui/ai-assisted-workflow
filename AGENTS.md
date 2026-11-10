# AGENTS.md

Working rules for any coding agent in this repository. Read this file in full at the start of every session.

## The project

This repository holds a training program on working well with AI assistance. It has two parts: a common session of 90 to 120 minutes for a mixed audience, and track sessions for engineering, product and experience, and business and people roles.

The deliverables are written in Canadian French: lessons with full speaker notes, workshop packs, handouts, and slide decks and PDF textbooks built on demand. Everything else is in English. The work proceeds in small steps, and the author reviews and commits each one.

## Map

| Path | What it holds |
|---|---|
| `.ai/project/state.md` | Lifecycle stage, current focus, next steps, open questions |
| `.ai/project/spec/` | The specification: what is taught and how deliverables are judged. Start at its `README.md` |
| `.ai/project/spec/module-map.md` | Module ID → card → lesson path → session deck → textbook |
| `.ai/project/decisions/` | Dated decision records; an accepted record is never edited |
| `.ai/project/handoffs/` | One note per work session, written from `TEMPLATE.md` |
| `.ai/project/knowledge/` | Curated, dated facts worth keeping across sessions |
| `.ai/project/skills-register.md` | Every project skill with its source, commit, licence and owner |
| `DESIGN.md` | Visual and editorial direction, tokens, French typography, patterns to avoid |
| `templates/` | Templates for French deliverables, starting with `lesson.md` |
| `lessons/` | One French lesson per module, at the same relative path as its card under `spec/curriculum/` |
| `sessions/`, `workshops/`, `handouts/`, `resources/`, `decks/`, `books/` | Other French deliverables, and the manifests for decks and PDF textbooks (created on first use) |
| `assets/` | Fonts, diagram sources, README images |
| `tools/` | Build and check scripts (MIT licence) |
| `build/` | Generated output; ignored by git and never committed |
| `.claude/skills/` | Project skills for Claude Code; see `CLAUDE.md` |

While the stage is `init`, some of these paths do not exist yet. The initialization plan says which step creates each one. The plan is `.ai/project/init-plan.md`; after the lock it moves to `.ai/project/decisions/0001-initialization-plan.md`.

## When sources disagree

The higher source wins:

1. The author's instruction in the current conversation.
2. This file, then `CLAUDE.md` for what is specific to Claude Code.
3. Accepted decision records; a newer record supersedes an older one.
4. `DESIGN.md`, for anything visual or editorial.
5. The specification; for a module's content, its own card.
6. `state.md` and the latest handoff.
7. Knowledge notes.
8. Existing deliverables.

If you notice a disagreement, stop and ask (see below); never resolve it silently.

## Session routine

At the start:

1. Read `.ai/project/state.md`, the most recent file in `.ai/project/handoffs/`, and, while the stage is `init`, the initialization plan.
2. Run `git status -- . ':(exclude).ai/prompts'`. If changes from the previous step are still uncommitted, ask whether to continue or wait, and add nothing until the author answers.

At the end of a session, or when context runs low:

1. Update `state.md`: current focus, next steps, open questions.
2. Write `.ai/project/handoffs/YYYY-MM-DD-<slug>.md` from `TEMPLATE.md`.
3. Give the author a suggested commit message.

## Working loop

1. Read the module card, its row in `module-map.md`, the template, and the parts of `DESIGN.md` the task touches.
2. State the plan: which files change and which checks you will run.
3. Make one small change.
4. Run the quality gates that apply.
5. Report in this format, then stop for review:

```text
Batch <n>: <name>
Files:             one line per file created, changed or moved, with its purpose
Checks:            what you verified and the result
Decisions I made:  small choices taken without asking
Open questions:    anything the author must answer
Suggested commit message: subject (imperative, ≤ 72 characters), a blank line, then a 2–5 line body
Next:              what the following step will do
Waiting for:       the author's review and commit
```

## Git

The author owns the index, the history and the branches, and makes every commit.

- Never run `git add`, `commit`, `push`, `pull`, `merge`, `rebase`, `reset`, `restore`, `checkout`, `switch`, `stash`, `tag`, `clean`, `mv`, `rm`, `config` or `remote`, by any route.
- Read-only git commands are allowed. Every one that lists files or shows content (`status`, `diff`, `log`, `show`, `ls-files`) ends with `-- . ':(exclude).ai/prompts'`.
- Move or delete files with ordinary file operations, and only when the approved plan or task says so.
- Suggested commit messages follow Conventional Commits, `type(scope): summary`: imperative, at most 72 characters, no attribution trailer.
  - Types are `feat` (new deliverable or capability), `fix`, `docs` (governance, specification, README), `build` (tools, dependencies), `refactor`, `style` and `chore`. The scope is a module ID such as `C-04`, or an area: `init`, `spec`, `design`, `skills`, `tools`.

## Stop and ask

Stop and ask the author, instead of deciding, when:

1. A requirement is missing or ambiguous in a way that changes what you would write.
2. Two sources disagree: the author, the specification, a decision record, `DESIGN.md`, the repository or the settings.
3. You would create, move, delete or change a file that the task or plan does not cover, or any locked file.
4. You think a permission rule, an ignore rule or anything under `.claude/` should change.
5. You would install something, run code that came from a third party, or download anything other than reading a page.
6. The choice is one of taste the author will live with: a name people will see, the visual direction, the voice, the structure of the lesson tree.
7. The action is destructive or hard to undo.
8. A tool call was blocked. Say what was blocked and why you wanted it; never look for another route to the same result.
9. The licence or origin of third-party material is unclear.

Small, reversible choices inside the task, such as the wording of a sentence or the order of sections, are yours. Make them and list them under "Decisions I made". When nothing above applies and the task is unfinished, keep working; never end a turn by offering to continue.

How to ask: every question in one message, numbered, each with your recommended answer and what changes with the answer. Then end the turn and wait.

## Lifecycle and lock

`state.md` holds the stage on its own line: `Stage: init` during setup, then `Stage: build` once the author confirms setup is complete. From `build` onward, these paths are locked:

`AGENTS.md`, `CLAUDE.md`, `DESIGN.md`, `README.md`, `LICENSE`, `LICENSES/**`, `THIRD_PARTY_NOTICES.md`, `.gitignore`, `.claude/**`, `.ai/project/spec/**`, `.ai/project/decisions/README.md` and every accepted decision record, `.ai/project/skills-register.md`, `.ai/project/handoffs/TEMPLATE.md`, `templates/**`, `assets/fonts/**`.

- Before editing a locked file, stop. Say which file, what would change and why, and show the proposed change.
- Proceed only when the author approves in the conversation, naming the file. An approval covers that change and nothing else, and does not carry over to another session.
- Record each approved change in the handoff.

Everything else stays writable: `state.md`, handoffs, knowledge notes, the deliverables, `assets/` other than fonts, and `tools/`. A new decision record may be added with `Status: proposed`; only the author makes it `accepted`. A change to `tools/requirements.txt` installs something, so it needs approval first.

The lock is a rule you follow, not a technical barrier. It is backed by the author's review of every diff before commit.

## Content rules

- **Language.** Learner- and presenter-facing deliverables are in Canadian French. Everything else is in English: instruction files, specifications, state, handoffs, decision records, knowledge notes, file and directory names, code, and messages to the author.
- **Terms in French text.** The glossary decides which terms stay in English and how the rest are rendered. The glossary is `resources/R-02-glossary.md`; until it exists, use the candidates in the spec's R-02 card, which still need confirming.
- **Neutrality.** Content is organization-neutral: no real employer, client, team, internal product or private person appears. Write "the organization", "your team", "the client". The only person named is the author, as copyright holder.
- **Examples.** Examples and practice material are fictional and synthetic.
- **No invention.** Do not invent facts, statistics, quotations, testimonials, references or sources. A statement that needs a source you could not open is left out or flagged.
- **Product names.** Public AI tools, vendors, standards and sources may be named where a card's topics require it. Version numbers, release numbers and dated product behaviour appear only in C-02 (landscape snapshot), in "re-verify" lists and in dated resource lists.
- **Third-party material.** It keeps its own licence, is copied only when that licence allows it, and is listed in `THIRD_PARTY_NOTICES.md`.
- **No sensitive data.** No secrets, personal data, details of a particular machine (operating system, installed versions, security settings, other devices) or conversation transcripts go in any file, including state, handoffs and knowledge notes.

## Quality gates

Before you report a deliverable as done, check each item that applies and report the result:

1. It covers its card: the outcomes, every required topic and the checkpoint. Recommended and optional topics appear only as reference.
2. It follows its template and `DESIGN.md`: structure, slide types, word limits, tokens.
3. Text and visuals pass the check against the patterns to avoid in `DESIGN.md`.
4. French text passes the Canadian French check: glossary terms, typography, anglicisms.
5. Speaker notes are written in full sentences, at about 110 words per planned minute, with timing marks and transitions.
6. Every product fact is dated or sits in C-02 or a "re-verify" list. Every link was opened.
7. Accessibility holds: the contrast targets are met, meaning is never carried by colour alone, and alt text is present.
8. Built decks and PDFs were rendered and every slide or page image inspected. Outputs stay in `build/`.
9. The `status` in the front matter is updated, and native-speaker review is flagged as pending until it is done.

## Off limits

`.ai/prompts/` belongs to the author. Never read, list, search or write it, by any tool or command, and never pass a path inside it to a command. Git read commands exclude it with the pathspec above.
