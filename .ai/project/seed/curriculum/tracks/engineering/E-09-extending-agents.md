# E-09 · Extending agents: connectors, sub-agents and teams

- **Where it sits:** Engineering track
- **Who:** Recommended: architects and tech leads, DevOps · Optional: developers, QA
- **Delivery:** Self-serve or advanced session
- **Time:** 25 min

Connectors, sub-agents and agent teams add reach and parallelism. Each one also adds trust decisions and review load, so they come after the fundamentals.

## Outcomes

A participant can:

- Explain what a connector protocol such as MCP provides and what it risks.
- Decide when a sub-agent or a second agent helps.
- Recognize when more agents only multiply review.

## Topics

### Required

- MCP is a standard way to connect an agent to external systems such as trackers, documents, databases and browsers. Each server is code with access: trust it deliberately, scope it, start read-only.
- A sub-agent works in its own context on a subtask such as exploration or review, and returns a summary.
- More agents help when the work is parallel, independent and verifiable. Otherwise they multiply what has to be reviewed.

### Recommended

- A command-line tool the agent can call is often simpler than a connector.
- Many connected tools consume context before any work starts.
- Orchestrator patterns and agent teams.
- Custom sub-agents with a restricted tool set.

### Optional

- Building a connector server.
- Plugins that bundle skills, hooks, agents and connectors.
- Evaluating an agent setup.

## Checkpoint

> You want the agent to read tickets from the tracker. Connector, command-line tool, or paste the ticket? What decides?

## Re-verify before each delivery

- Protocol versions, registries and product support.

## Read more

[Coding agents](../../resources/R-01-further-reading.md#coding-agents), [Skills worth studying](../../resources/R-01-further-reading.md#skills).

---

← [E-08 Automation and operations](E-08-automation-and-operations.md) · [Curriculum index](../../README.md)
