# E-05 · Verification, testing and QA

- **Where it sits:** Engineering track
- **Who:** Required: developers, QA · Recommended: architects and tech leads, DevOps
- **Delivery:** Engineering track, session 5; also usable self-serve
- **Time:** 25 min

Agents produce more code faster than teams can review. Verification becomes the constraint, and quality roles gain importance.

## Outcomes

A participant can:

- Use tests as evidence while knowing what they do not prove.
- Spot the common ways an agent makes tests pass without fixing anything.
- Describe how the QA role shifts in AI-assisted delivery.

## Topics

### Required

- Tests, types, linters and builds are evidence, not proof. Read failures yourself.
- Watch for a "fix" that weakens the test: assertions that check nothing, behaviour mocked away, tests deleted or skipped, expected values hard-coded.
- Derive tests from the specification, not from the implementation the agent just wrote.
- AI code review is an additional reviewer. Human review remains for intent, design and security.
- QA focus moves toward test design, risk-based coverage, exploratory testing and acceptance against the specification.

### Recommended

- Generate test cases and edge cases from acceptance criteria. Generate synthetic test data, never production data.
- Verify interfaces with browser automation and screenshots.
- Reviewing an AI-heavy pull request: read the diff top-down, run it, and look for what is absent.
- A reliable regression suite is the safety net for agent refactors. Flaky tests mislead agents as they mislead people.
- A good bug report is also a good agent input: steps to reproduce, expected and actual.

### Optional

- Mutation testing.
- Evaluation sets for AI features inside the product.
- Automated review bots and managing their noise.

## Checkpoint

> The agent changed a test and the implementation in the same commit. What do you check?

## Practice

Review a prepared pull request in which one test was quietly weakened. Find it.

## Read more

[Coding agents](../../resources/R-01-further-reading.md#coding-agents).

---

← [E-04 Specs and context engineering for code](E-04-specs-and-context-engineering.md) · [Curriculum index](../../README.md) · [E-06 Architecture and design work](E-06-architecture-and-design-work.md) →
