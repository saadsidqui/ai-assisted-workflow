# E-04 · Specs and context engineering for code

- **Where it sits:** Engineering track
- **Who:** Required: developers, architects and tech leads · Recommended: QA, DevOps, PM / PO, analysts
- **Delivery:** Engineering track, session 4; also usable self-serve
- **Time:** 25 min

With capable agents, the quality of the result is bounded by the specification and by what is in the context window. This is where product and engineering meet.

## Outcomes

A participant can:

- Write a task specification an agent can execute and check.
- Keep a session's context clean across a multi-step task.
- Use planning before implementation for anything non-trivial.

## Topics

### Required

- A workable specification states the outcome, the constraints, the acceptance criteria and what is out of scope.
- Give the agent a way to check its own work: a test, a command, an expected output. This is the largest single improvement available.
- Point at the relevant files and at an example to follow instead of describing them.
- For anything non-trivial, plan first, review the plan, then implement.
- Context is finite. One task per session, and a fresh session between unrelated tasks. Long sessions drift.

### Recommended

- The interview pattern: have the agent question you until the specification is complete, then write it to a file.
- Sub-agents for exploration, so the main context stays clean, and a fresh-context reviewer for the result.
- What survives compaction and what does not: the root instruction file is reloaded, things said only in conversation may be lost. Write decisions down.
- Slice work into vertical steps that can each be verified, tracked in a checklist the agent keeps up to date.
- The specification lives in the repository and is linked from the ticket.

### Optional

- Specification-driven frameworks.
- Work that spans many sessions.
- Several agents on one specification.

## Checkpoint

> This task description produced the wrong change. What would you add: an acceptance check, a pointer to an example, or an out-of-scope line?

## Practice

Turn a one-line ticket into a specification with three acceptance criteria and one verification command. Compare the agent's result with and without it.

## Re-verify before each delivery

- Planning-mode names and compaction behaviour per tool.

## Read more

[Coding agents](../../resources/R-01-further-reading.md#coding-agents), [Working method and prompting](../../resources/R-01-further-reading.md#working-method).

---

← [E-02 The safe change loop and git](E-02-safe-change-loop-and-git.md) · [Curriculum index](../../README.md) · [E-05 Verification, testing and QA](E-05-verification-testing-and-qa.md) →
