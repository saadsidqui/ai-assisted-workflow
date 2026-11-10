# Engineering track

For developers, architects, technical leads, QA and DevOps. The track assumes the common core and goes from the first agent-assisted change to a repository that is set up for agents and a team that can verify what they produce. Repo setup has its own folder because it is the part that changes most often and is most often taught on its own.

All eight core modules are required for everyone and come first: see the [curriculum index](../../README.md).

## Modules by role

Required means the role should not work with AI on this kind of task without it. Recommended means most people in the role benefit. Optional is for interest or a specific need.

| Module | Developers | Architects and tech leads | QA | DevOps | Time |
|---|---|---|---|---|---|
| [E-01 Coding assistants and agents: ways of working](E-01-coding-assistants-and-agents.md) | Required | Required | Required | Required | 20 min |
| [E-02 The safe change loop and git](E-02-safe-change-loop-and-git.md) | Required | Required | Required | Required | 25 min |
| [E-03.1 Structure and instruction files](repo-setup/E-03.1-structure-and-instruction-files.md) | Required | Required | Recommended | Required | 20 min |
| [E-03.2 Permissions and modes](repo-setup/E-03.2-permissions-and-modes.md) | Required | Required | Recommended | Required | 25 min |
| [E-03.3 Sandboxing and isolation](repo-setup/E-03.3-sandboxing-and-isolation.md) | Recommended | Required | Optional | Required | 20 min |
| [E-03.4 Ignore rules and secrets](repo-setup/E-03.4-ignore-rules-and-secrets.md) | Required | Required | Required | Required | 15 min |
| [E-03.5 Skills: choosing and writing them](repo-setup/E-03.5-skills.md) | Recommended | Recommended | Recommended | Recommended | 25 min |
| [E-03.6 Memory, knowledge, specs, state and handoffs](repo-setup/E-03.6-memory-knowledge-specs-state-handoffs.md) | Required | Required | Recommended | Recommended | 25 min |
| [E-04 Specs and context engineering for code](E-04-specs-and-context-engineering.md) | Required | Required | Recommended | Recommended | 25 min |
| [E-05 Verification, testing and QA](E-05-verification-testing-and-qa.md) | Required | Recommended | Required | Recommended | 25 min |
| [E-06 Architecture and design work](E-06-architecture-and-design-work.md) | Recommended | Required | Optional | Recommended | 20 min |
| [E-07 Security for AI-assisted development](E-07-security-for-ai-assisted-development.md) | Required | Required | Recommended | Required | 20 min |
| [E-08 Automation and operations](E-08-automation-and-operations.md) | Optional | Recommended | Optional | Required | 25 min |
| [E-09 Extending agents: connectors, sub-agents and teams](E-09-extending-agents.md) | Optional | Recommended | Optional | Recommended | 25 min |

## From other tracks and overlays

| Module | Developers | Architects and tech leads | QA | DevOps |
|---|---|---|---|---|
| [P-02 Requirements and specs](../product-experience/P-02-requirements-and-specs.md) | · | Recommended | Recommended | · |
| [B-05 Leading adoption](../business-people/B-05-leading-adoption.md) | · | Optional | · | · |
| [X-01 Working in a client environment](../../overlays/X-01-working-in-a-client-environment.md) | Required | Required | Required | Required |
| [X-02 Jurisdiction and policy pack](../../overlays/X-02-jurisdiction-and-policy-pack.md) | Required | Required | Required | Required |
| [X-03 End-to-end engagement map](../../overlays/X-03-end-to-end-engagement-map.md) | Recommended | Recommended | Recommended | Recommended |

## Suggested sessions

Each session is planned inside its booking with at least ten minutes left unallocated for questions and a slower pace. Module minutes come from the module cards and include each module's checkpoint.

### Session 1 · Working with coding agents

- Modules: [E-01](E-01-coding-assistants-and-agents.md), [E-02](E-02-safe-change-loop-and-git.md) (45 min)
- Practice: Workshop: one small change through the safe change loop ([S-02](../../session/S-02-workshop.md)). (25 min)
- Planned: 70 min of a 90-minute booking, with 20 min unallocated

### Session 2 · Repo setup: instructions and permissions

- Modules: [E-03.1](repo-setup/E-03.1-structure-and-instruction-files.md), [E-03.2](repo-setup/E-03.2-permissions-and-modes.md) (45 min)
- Overlay: [X-01](../../overlays/X-01-working-in-a-client-environment.md) (10 min)
- Practice: Lab: write an instruction file and a permission set for a sample repository, then try to break your own rules. (20 min)
- Planned: 75 min of a 90-minute booking, with 15 min unallocated

### Session 3 · Repo setup: secrets, isolation, project memory

- Modules: [E-03.4](repo-setup/E-03.4-ignore-rules-and-secrets.md), [E-03.3](repo-setup/E-03.3-sandboxing-and-isolation.md), [E-03.6](repo-setup/E-03.6-memory-knowledge-specs-state-handoffs.md) (60 min)
- Practice: Lab: write a handoff; a neighbour starts a fresh session from it. (15 min)
- Planned: 75 min of a 90-minute booking, with 15 min unallocated

### Session 4 · Skills and specs

- Modules: [E-03.5](repo-setup/E-03.5-skills.md), [E-04](E-04-specs-and-context-engineering.md) (50 min)
- Practice: Lab: one small skill, and one ticket turned into a specification with a verification command. (20 min)
- Planned: 70 min of a 90-minute booking, with 20 min unallocated

### Session 5 · Verification and security

- Modules: [E-05](E-05-verification-testing-and-qa.md), [E-07](E-07-security-for-ai-assisted-development.md) (45 min)
- Overlay: [X-03](../../overlays/X-03-end-to-end-engagement-map.md) (10 min)
- Practice: Exercise: review a prepared pull request in which a test was quietly weakened. (15 min)
- Planned: 70 min of a 90-minute booking, with 20 min unallocated

## Self-serve

Not scheduled; read when the need arises: [E-06 Architecture and design work](E-06-architecture-and-design-work.md), [E-08 Automation and operations](E-08-automation-and-operations.md), [E-09 Extending agents: connectors, sub-agents and teams](E-09-extending-agents.md).

The repo setup modules have their own overview: [repo-setup](repo-setup/README.md).

---

[Curriculum index](../../README.md)
