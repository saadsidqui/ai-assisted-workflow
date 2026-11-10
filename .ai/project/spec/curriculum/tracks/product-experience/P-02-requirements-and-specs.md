# P-02 · Requirements and specs

- **Where it sits:** Product and experience track
- **Who:** Required: PM / PO, analysts · Recommended: architects and tech leads, QA, designers
- **Delivery:** Product and experience track, session 1; also usable self-serve
- **Time:** 25 min

A requirement is now read by an engineer, a tester and a coding agent. Vague acceptance criteria used to cost a clarification meeting; now they produce a confident wrong implementation.

## Outcomes

A participant can:

- Draft and refine user stories with testable acceptance criteria.
- Use an assistant to find gaps in a requirement.
- Write a specification that an engineer or a coding agent can execute.

## Topics

### Required

- Draft and refine user stories and acceptance criteria. AI is strong at finding gaps: edge cases, ambiguity, missing roles, unstated assumptions.
- Acceptance criteria are testable (given, when, then, or a checklist). They become the definition of done for the agent and for QA.
- Traceability: every requirement points to a source or to a named decision. Assumptions are marked as assumptions.
- Product decisions and priorities stay with the accountable person.
- An executable specification states the outcome, scope, out-of-scope, constraints, acceptance criteria and examples.

### Recommended

- The interview pattern: the assistant questions you until the requirement is complete.
- Splitting oversized stories.
- A checklist prompt for non-functional requirements.
- A consistency check against the glossary and earlier decisions.
- A review of the specification by a fresh session with no prior context.
- Handing the specification to engineering as a file in the repository ([E-04](../engineering/E-04-specs-and-context-engineering.md)).

### Optional

- Requirement templates packaged as skills.
- Tracker integrations.
- Scoring requirement quality.

## Checkpoint

> "The export should be fast." Rewrite it so that a tester and an agent would both know when it is done.

## Practice

The product workshop ([S-02](../../session/S-02-workshop.md)): from a fictional brief to three stories with acceptance criteria.

## Read more

[Working method and prompting](../../resources/R-01-further-reading.md#working-method), [Coding agents](../../resources/R-01-further-reading.md#coding-agents).

---

← [P-01 Discovery and synthesis](P-01-discovery-and-synthesis.md) · [Curriculum index](../../README.md) · [P-03 Planning, delivery and reporting](P-03-planning-delivery-and-reporting.md) →
