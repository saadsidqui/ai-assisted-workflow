# Repo setup for AI

Six short modules on preparing a repository so that a coding agent can work in it safely and pick up where the last session stopped. They can be taught as two lab sessions or read one at a time.

One idea ties them together: **instructions guide, configuration enforces, isolation contains.** An instruction file tells an agent what you want. A permission rule decides what the tool will let it do. A sandbox limits what can happen when both of those fail. Each layer covers a gap the others leave.

| Module | What it settles | Layer |
|---|---|---|
| [E-03.1 Structure and instruction files](E-03.1-structure-and-instruction-files.md) | How an agent learns what this repository is and how to work in it | Guide |
| [E-03.2 Permissions and modes](E-03.2-permissions-and-modes.md) | What the agent is allowed to do, and what needs your approval | Enforce |
| [E-03.3 Sandboxing and isolation](E-03.3-sandboxing-and-isolation.md) | What can happen if something goes wrong anyway | Contain |
| [E-03.4 Ignore rules and secrets](E-03.4-ignore-rules-and-secrets.md) | What is tracked, what is private, and what the agent must not read | Enforce |
| [E-03.5 Skills: choosing and writing them](E-03.5-skills.md) | How recurring procedures are packaged, and how third-party ones are vetted | Guide |
| [E-03.6 Memory, knowledge, specs, state and handoffs](E-03.6-memory-knowledge-specs-state-handoffs.md) | Where the project's memory lives between sessions | Guide |

## A reference layout

One workable layout, to adapt to the repository and the tools in use. It is an example, not a standard.

```text
repository/
├── AGENTS.md              shared working instructions, read by most coding agents
├── CLAUDE.md              one line importing AGENTS.md, plus Claude-only notes
├── DESIGN.md              design constraints and decisions agents must respect
├── README.md              for people
├── .gitignore             what git does not track (not an access control)
├── .claude/
│   ├── settings.json      shared permission rules, committed
│   └── skills/            project skills, one folder each with a SKILL.md
└── .ai/
    ├── project/
    │   ├── spec/          what to build and how success is judged
    │   ├── state.md       where things stand, what is next
    │   ├── decisions/     dated records of what was chosen and why
    │   ├── handoffs/      one note per work session
    │   └── knowledge/     curated, non-sensitive facts
    └── prompts/           private and local: ignored by git and read-denied
```

Tool-specific folders keep the names the tool expects. Claude Code loads project skills from `.claude/skills/` and does not read a generic `.agents/` or `.ai/skills/` folder, so skills live where the tool looks for them.

## Order of work for a new repository

1. Write the instruction file and keep it short ([E-03.1](E-03.1-structure-and-instruction-files.md)).
2. Set permissions narrow, then widen from experience ([E-03.2](E-03.2-permissions-and-modes.md)).
3. Sort files into committed, ignored and unreadable ([E-03.4](E-03.4-ignore-rules-and-secrets.md)).
4. Decide the isolation level the repository needs ([E-03.3](E-03.3-sandboxing-and-isolation.md)).
5. Create the project directory and the handoff habit ([E-03.6](E-03.6-memory-knowledge-specs-state-handoffs.md)).
6. Add a skill only when a procedure has been explained twice ([E-03.5](E-03.5-skills.md)).
7. Lock the governance files once setup is confirmed, and change them only with explicit approval ([E-03.6](E-03.6-memory-knowledge-specs-state-handoffs.md)).

---

[Engineering track](../README.md) · [Curriculum index](../../../README.md)
