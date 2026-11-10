# E-08 · Automation and operations

- **Where it sits:** Engineering track
- **Who:** Required: DevOps · Recommended: architects and tech leads · Optional: developers, QA
- **Delivery:** Self-serve or dedicated session
- **Time:** 25 min

The same agents run without a person watching: in CI, on a schedule, triggered by an issue. Unattended runs need tighter limits, because nobody is there to say no.

## Outcomes

A participant can:

- Describe the controls an unattended agent run needs.
- Route automated output through the same review gates as human work.
- Identify where hooks replace instructions.

## Topics

### Required

- Agents outside the editor: non-interactive runs, CI jobs, scheduled tasks, agents triggered by issues and pull requests.
- Unattended means nobody approves: narrow permissions, a sandbox, explicit allowlists, hard timeouts. Never a bypass mode on a shared runner that holds secrets.
- Output goes through the same gates: a pull request, review, checks. No direct pushes to protected branches.
- Cost and usage are visible: limits, budgets, and who pays.

### Recommended

- Hooks for steps that must always happen: format, lint, block protected paths, notify.
- Automation candidates: pull request review, triage, release notes, dependency updates.
- Infrastructure as code and runbooks: review the plan or diff, never apply automatically. Take care with sensitive data in logs during incident support.
- Observability: transcripts, metrics and audit trails.

### Optional

- Agent SDKs and custom harnesses.
- Orchestrating many agents.
- Self-hosted runners and their isolation.
- Evaluation pipelines.

## Checkpoint

> An agent runs nightly on the main repository. List the three limits you set before the first run.

## Practice

Configure a non-interactive run that drafts release notes from merged pull requests into a branch, with no write access anywhere else.

## Re-verify before each delivery

- Flags, action names and pricing models.

## Read more

[Coding agents](../../resources/R-01-further-reading.md#coding-agents), [Staying current](../../resources/R-01-further-reading.md#staying-current).

---

← [E-07 Security for AI-assisted development](E-07-security-for-ai-assisted-development.md) · [Curriculum index](../../README.md) · [E-09 Extending agents: connectors, sub-agents and teams](E-09-extending-agents.md) →
