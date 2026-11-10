# E-07 · Security for AI-assisted development

- **Where it sits:** Engineering track
- **Who:** Required: developers, architects and tech leads, DevOps · Recommended: QA
- **Delivery:** Engineering track, session 5; also usable self-serve
- **Time:** 20 min

AI-assisted development adds new ways in: content that carries instructions, dependencies that do not exist, and extensions that run with the developer's access.

## Outcomes

A participant can:

- Name the untrusted inputs an agent reads during ordinary work.
- Explain the combination of capabilities that makes data theft possible, and how to break it.
- Apply supply-chain thinking to skills, plugins and connectors.

## Topics

### Required

- Generated code gets the same security review as any other code, and often needs it: injection, missing authorization checks, unsafe defaults, secrets in source.
- Dependencies: confirm that a suggested package exists and is the intended one, and check its licence and version. Invented and look-alike package names are a known attack path.
- Prompt injection in development: a README, an issue, a pull request comment, a web page, dependency documentation and tool output are all untrusted input to an agent.
- The dangerous combination: access to private data, exposure to untrusted content, and a way to send data out. Remove one of the three.
- Secrets hygiene ([E-03.4](repo-setup/E-03.4-ignore-rules-and-secrets.md)), and no production credentials for agents.

### Recommended

- Third-party skills, plugins, connectors and hooks are a supply chain: review, pin, least privilege.
- Integrations read-only by default, with separate tokens for agents.
- A security review step before a pull request, and static analysis and secret scanning in CI regardless.
- Licence and intellectual property: similarity of generated code to existing code, and client contract constraints.
- A known path for reporting a leaked secret or leaked code.

### Optional

- Threat modelling an agent workflow.
- The OWASP lists for LLM and agentic applications, for teams building AI features.
- How sandboxes are escaped.

## Checkpoint

> Which of these does an agent treat as instructions: your prompt, the instruction file, an issue comment, a web page it fetched? Which should it?

## Practice

Give an agent a sample issue that contains a planted instruction. Observe what it does, then repeat with tighter permissions.

## Re-verify before each delivery

- Current attack patterns and the OWASP list editions.

## Read more

[Security, privacy and governance](../../resources/R-01-further-reading.md#security-privacy).

---

← [E-06 Architecture and design work](E-06-architecture-and-design-work.md) · [Curriculum index](../../README.md) · [E-08 Automation and operations](E-08-automation-and-operations.md) →
