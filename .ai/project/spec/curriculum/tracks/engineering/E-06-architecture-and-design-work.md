# E-06 · Architecture and design work

- **Where it sits:** Engineering track
- **Who:** Required: architects and tech leads · Recommended: developers, DevOps · Optional: QA
- **Delivery:** Track session 3 or self-serve
- **Time:** 20 min

AI widens the set of options an architect can examine in an hour. Choosing among them, and writing down why, remains human work and becomes the best context an agent can be given.

## Outcomes

A participant can:

- Use an assistant to explore design options without delegating the decision.
- Record a decision in a form that both people and agents can use.
- Describe what makes a codebase easy for agents to work in.

## Topics

### Required

- Use AI to widen options, not to choose: alternatives, trade-offs, failure modes. The architect decides and records the reasoning.
- Codebase comprehension: maps, dependency explanations, "where is this handled". Verify against the code.
- Record decisions in short decision records. They are documentation for people and context for agents.
- Put design constraints in a file agents read: boundaries, patterns to follow, patterns that are forbidden.

### Recommended

- Diagrams as code (Mermaid, PlantUML, C4), generated and then reviewed.
- Reviewing a design by asking for the strongest objection, and a first-pass threat model.
- Agent-friendly codebases: clear module boundaries, fast tests, consistent conventions, small files. These help people equally.
- Migrations and large refactors: plan, slice, verify each slice.
- Technology choices supported by cited research, with dates checked.

### Optional

- Architecture fitness checks in CI.
- Legacy modernization playbooks.
- Context across several repositories.

## Checkpoint

> The assistant recommends option B with confidence. What do you ask it next?

## Practice

For a small design question, get three options with trade-offs, pick one, and write the decision record in ten lines.

## Read more

[Coding agents](../../resources/R-01-further-reading.md#coding-agents).

---

← [E-05 Verification, testing and QA](E-05-verification-testing-and-qa.md) · [Curriculum index](../../README.md) · [E-07 Security for AI-assisted development](E-07-security-for-ai-assisted-development.md) →
