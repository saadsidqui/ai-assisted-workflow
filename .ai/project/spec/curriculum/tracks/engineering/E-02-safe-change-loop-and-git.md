# E-02 · The safe change loop and git

- **Where it sits:** Engineering track
- **Who:** Required: all engineering roles
- **Delivery:** Engineering track, session 1; also usable self-serve
- **Time:** 25 min

Git is what makes agent work reviewable and reversible. The loop below is the engineering form of the core working loop, with the human keeping the commit.

## Outcomes

A participant can:

- Take a change from task statement to human commit through the loop.
- Read a full diff before accepting it.
- Keep a rollback path at every step.

## Topics

### Required

- The loop: clean working tree, branch, state the task and its acceptance criteria, the agent explores and proposes a plan, a small change, run the checks, read the full diff, revise, the human commits.
- Small, reviewable diffs. One concern per change.
- The human owns commit and push, unless the team has explicitly delegated them under stated conditions.
- Read commands before they run. Know the destructive ones: hard resets, cleans, force pushes, recursive deletes, migrations.
- Commits are the checkpoints. A tool's own rewind feature is a convenience; git is the record.
- A "done" claim is a hypothesis. Ask for evidence: test output, a run, a screenshot.

### Recommended

- One working tree per agent. Use worktrees for parallel work.
- Commit messages and pull request descriptions drafted by the tool and reviewed by you. Attribution trailers follow team and client policy.
- Review generated files, configuration changes and lockfiles with the same attention as source.
- Know when to discard an attempt and restart with a better brief.
- Limits on pull request size, and a label for AI-heavy changes if the team wants one.

### Optional

- Stacked pull requests.
- Bisecting a regression introduced by an agent.
- Automated issue-to-pull-request flows ([E-08](E-08-automation-and-operations.md)).

## Checkpoint

> The agent reports that all tests pass. What do you look at before you believe it?

## Practice

The engineering workshop ([S-02](../../session/S-02-workshop.md)) runs this loop once on a prepared repository.

## Re-verify before each delivery

- Tool-specific checkpoint and rewind features.

## Read more

[Coding agents](../../resources/R-01-further-reading.md#coding-agents).

---

← [E-01 Coding assistants and agents: ways of working](E-01-coding-assistants-and-agents.md) · [Curriculum index](../../README.md) · [E-04 Specs and context engineering for code](E-04-specs-and-context-engineering.md) →
