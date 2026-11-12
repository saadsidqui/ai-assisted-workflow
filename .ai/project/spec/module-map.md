# Module map

Every module ID with its card, its lesson, the session deck it belongs to and the textbooks that include it.

## Rules

- **Paths.** A lesson has the same relative path under `lessons/` as its card has under [`curriculum/`](curriculum/README.md). One ID, one card, one lesson, one group of slides.
- **Session decks.** The session deck column comes from the track pages:
  - "Common" is the common session (S-01);
  - ENG, PX and BIZ followed by a number are the suggested track sessions;
  - "Self-serve" modules have no session deck.
- **Textbooks.** The textbook column comes from each track page's module table and its "from other tracks and overlays" table.
  - Every textbook also carries the workshop material, handouts, glossary and further reading for its audience; its manifest in `books/` lists them.
  - Whether track textbooks also include the core lessons is open decision OD-08.

## Modules

| ID | Module | Path | Session deck | Textbooks |
|---|---|---|---|---|
| C-01 | Mental model and vocabulary | `core/C-01-mental-model-and-vocabulary.md` | Common | Core |
| C-02 | Landscape snapshot | `core/C-02-landscape-snapshot.md` | Common | Core |
| C-03 | Task fit and limits | `core/C-03-task-fit-and-limits.md` | Common | Core |
| C-04 | The working loop and prompting | `core/C-04-working-loop-and-prompting.md` | Common | Core |
| C-05 | Context | `core/C-05-context.md` | Common | Core |
| C-06 | Gates and human review | `core/C-06-gates-and-human-review.md` | Common | Core |
| C-07 | Data, security and responsible use | `core/C-07-data-security-and-responsible-use.md` | Common | Core |
| C-08 | From assistant to agent | `core/C-08-from-assistant-to-agent.md` | Common | Core |
| E-01 | Coding assistants and agents: ways of working | `tracks/engineering/E-01-coding-assistants-and-agents.md` | ENG 1 | ENG |
| E-02 | The safe change loop and git | `tracks/engineering/E-02-safe-change-loop-and-git.md` | ENG 1 | ENG |
| E-03.1 | Structure and instruction files | `tracks/engineering/repo-setup/E-03.1-structure-and-instruction-files.md` | ENG 2 | ENG |
| E-03.2 | Permissions and modes | `tracks/engineering/repo-setup/E-03.2-permissions-and-modes.md` | ENG 2 | ENG |
| E-03.3 | Sandboxing and isolation | `tracks/engineering/repo-setup/E-03.3-sandboxing-and-isolation.md` | ENG 3 | ENG |
| E-03.4 | Ignore rules and secrets | `tracks/engineering/repo-setup/E-03.4-ignore-rules-and-secrets.md` | ENG 3 | ENG |
| E-03.5 | Skills: choosing and writing them | `tracks/engineering/repo-setup/E-03.5-skills.md` | ENG 4 | ENG |
| E-03.6 | Memory, knowledge, specs, state and handoffs | `tracks/engineering/repo-setup/E-03.6-memory-knowledge-specs-state-handoffs.md` | ENG 3 | ENG, PX |
| E-04 | Specs and context engineering for code | `tracks/engineering/E-04-specs-and-context-engineering.md` | ENG 4 | ENG, PX |
| E-05 | Verification, testing and QA | `tracks/engineering/E-05-verification-testing-and-qa.md` | ENG 5 | ENG |
| E-06 | Architecture and design work | `tracks/engineering/E-06-architecture-and-design-work.md` | Self-serve | ENG |
| E-07 | Security for AI-assisted development | `tracks/engineering/E-07-security-for-ai-assisted-development.md` | ENG 5 | ENG |
| E-08 | Automation and operations | `tracks/engineering/E-08-automation-and-operations.md` | Self-serve | ENG |
| E-09 | Extending agents: connectors, sub-agents and teams | `tracks/engineering/E-09-extending-agents.md` | Self-serve | ENG |
| P-01 | Discovery and synthesis | `tracks/product-experience/P-01-discovery-and-synthesis.md` | PX 1 | PX |
| P-02 | Requirements and specs | `tracks/product-experience/P-02-requirements-and-specs.md` | PX 1 | PX, ENG |
| P-03 | Planning, delivery and reporting | `tracks/product-experience/P-03-planning-delivery-and-reporting.md` | PX 2 | PX |
| P-04 | Design and prototyping | `tracks/product-experience/P-04-design-and-prototyping.md` | PX 2 | PX |
| P-05 | Content and UX writing | `tracks/product-experience/P-05-content-and-ux-writing.md` | PX 3 | PX |
| P-06 | Data and analysis | `tracks/product-experience/P-06-data-and-analysis.md` | PX 3 | PX, BIZ |
| B-01 | Communications and documents | `tracks/business-people/B-01-communications-and-documents.md` | BIZ 1 | BIZ |
| B-02 | Research and decision briefs | `tracks/business-people/B-02-research-and-decision-briefs.md` | BIZ 1 | BIZ, PX |
| B-03 | People operations | `tracks/business-people/B-03-people-operations.md` | BIZ 2 | BIZ |
| B-04 | Business development | `tracks/business-people/B-04-business-development.md` | BIZ 2 | BIZ |
| B-05 | Leading adoption | `tracks/business-people/B-05-leading-adoption.md` | BIZ leadership | BIZ, ENG |
| X-01 | Working in a client environment | `overlays/X-01-working-in-a-client-environment.md` | ENG 2, PX 1, BIZ 1 | ENG, PX, BIZ |
| X-02 | Jurisdiction and policy pack | `overlays/X-02-jurisdiction-and-policy-pack.md` | Common (one slide) | Core, ENG, PX, BIZ |
| X-03 | End-to-end engagement map | `overlays/X-03-end-to-end-engagement-map.md` | ENG 5, PX 2, BIZ 2 | ENG, PX, BIZ |

## Session and resource cards

These cards are not modules. They map to other deliverables, described in [`deliverables.md`](deliverables.md).

| ID | Card | Deliverable |
|---|---|---|
| S-01 | [`session/S-01-run-of-show.md`](curriculum/session/S-01-run-of-show.md) | `guides/common-session/`: sources of the presenter guide for the common session (decision 0020) |
| S-02 | [`session/S-02-workshop.md`](curriculum/session/S-02-workshop.md) | `workshops/S-02-workshop.md`: facilitator guide, with the packs and track versions beside it |
| R-01 | [`resources/R-01-further-reading.md`](curriculum/resources/R-01-further-reading.md) | `resources/R-01-further-reading.md`: further reading |
| R-02 | [`resources/R-02-glossary-seed.md`](curriculum/resources/R-02-glossary-seed.md) | `resources/R-02-glossary.md`: the glossary |
| R-03 | [`resources/R-03-asset-backlog.md`](curriculum/resources/R-03-asset-backlog.md) | None: it stays in the specification, extended by `deliverables.md` |
