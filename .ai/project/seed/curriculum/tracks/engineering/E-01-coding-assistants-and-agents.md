# E-01 · Coding assistants and agents: ways of working

- **Where it sits:** Engineering track
- **Who:** Required: all engineering roles
- **Delivery:** Engineering track, session 1; also usable self-serve
- **Time:** 20 min

"Using AI to code" covers four different ways of working with very different risks. Picking the right one for the task is the first engineering judgment call.

## Outcomes

A participant can:

- Choose a working mode and a level of autonomy for a given task.
- Name good first uses in their own codebase.
- State what remains the engineer's responsibility.

## Topics

### Required

- Four working modes: inline completion, chat in the IDE, agentic tools in the terminal or IDE that read, edit and run commands, and cloud or background agents that work on a branch and open a pull request.
- Choose autonomy per task: its size, its risk, and how well you can specify and verify it.
- Good first uses: explaining unfamiliar code, finding where something is handled, tests for existing behaviour, small bounded changes, refactoring with tests in place, documentation, review preparation.
- The engineer owns architecture, correctness, security, maintainability and licence compliance.
- Never merge code you cannot explain.
- On client work, the client decides which tools may see which code ([X-01](../../overlays/X-01-working-in-a-client-environment.md)).

### Recommended

- Default rhythm: explore, plan, implement, verify. Use a read-only or plan mode for the first two.
- Model and effort choice per task, with awareness of cost and rate limits.
- Parallel sessions: when they help and when they only create review debt.
- Unfamiliar and legacy codebases: let the agent map the code first, then verify the map against the code.
- Learning with the tool: ask for explanations and be quizzed. "Explain it back" before accepting applies most to junior engineers.

### Optional

- Remote and cloud sessions, and picking work up from another device.
- Browser and computer use for interface testing.
- Voice input.

## Checkpoint

> Three tasks on screen (rename across a module, new endpoint with business rules, production incident). Which mode for each, and why?

## Practice

In a sample repository, ask an agent to explain one module and list its entry points. Verify two of its claims in the code.

## Re-verify before each delivery

- Product feature names and plan limits.

## Read more

[Coding agents](../../resources/R-01-further-reading.md#coding-agents).

---

[Curriculum index](../../README.md) · [E-02 The safe change loop and git](E-02-safe-change-loop-and-git.md) →
