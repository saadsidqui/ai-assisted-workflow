# Curriculum outline

An outline of what to teach about working with AI assistance, to whom, and how much of it is essential. It is a planning document in English. The lessons, handouts and slides built from it are written in Canadian French.

It contains 36 module cards, a session design and a resource list. Each card is one small file, so a topic can be updated, reordered or dropped without touching the others.

## How it is organized

| Folder | What it holds |
|---|---|
| [`session/`](session/S-01-run-of-show.md) | The run of show for the common session and the hands-on workshop design |
| [`core/`](core/C-01-mental-model-and-vocabulary.md) | Eight modules for everyone; the common session is built from them |
| [`tracks/engineering/`](tracks/engineering/README.md) | Developers, architects and tech leads, QA, DevOps |
| [`tracks/product-experience/`](tracks/product-experience/README.md) | PM / PO, analysts, designers |
| [`tracks/business-people/`](tracks/business-people/README.md) | Management, HR, business development, others |
| [`overlays/`](overlays/X-01-working-in-a-client-environment.md) | Topics that cut across tracks: client work, local rules, the end-to-end map |
| [`resources/`](resources/R-01-further-reading.md) | Further reading, a glossary seed, the list of assets to build |

Three tracks cover every role. Each track page has a table that shows the tier per role, so a QA engineer and a DevOps engineer can each see their own path through the same track.

## Tiers

- **Required**: the role should not do this kind of work with AI without it.
- **Recommended**: most people in the role benefit; teach it if there is time.
- **Optional**: for interest, or for a specific need.

Tiers apply twice. The tables below give the tier of each *module* per track. Inside a module, the *topics* are sorted into the same three tiers, which tells the presenter what to keep when time is short.

An asterisk means the tier shown is the highest in that track and does not apply to every role in it; the track page gives the tier for each role. ENG, PX and BIZ are the engineering, product and experience, and business and people tracks. A dot means the module is not aimed at that track.

## Common core

Everyone attends one session of 90 to 120 minutes ([S-01](session/S-01-run-of-show.md)) with a hands-on exercise ([S-02](session/S-02-workshop.md)). Only the required topics of each core module are taught in the session; the rest is reference material.

| Module | In the core session | ENG | PX | BIZ | Time |
|---|---|---|---|---|---|
| [C-01 Mental model and vocabulary](core/C-01-mental-model-and-vocabulary.md) | Segment 1 | Required | Required | Required | 12 min |
| [C-02 Landscape snapshot](core/C-02-landscape-snapshot.md) | Segment 2 | Required | Required | Required | 4 min in session, 15 min full |
| [C-03 Task fit and limits](core/C-03-task-fit-and-limits.md) | Segment 2 | Required | Required | Required | 6 min |
| [C-04 The working loop and prompting](core/C-04-working-loop-and-prompting.md) | Segment 3 | Required | Required | Required | 10 min |
| [C-05 Context](core/C-05-context.md) | Segment 3 | Required | Required | Required | 5 min |
| [C-06 Gates and human review](core/C-06-gates-and-human-review.md) | Segment 4 | Required | Required | Required | 5 min |
| [C-07 Data, security and responsible use](core/C-07-data-security-and-responsible-use.md) | Segment 4 | Required | Required | Required | 5 min |
| [C-08 From assistant to agent](core/C-08-from-assistant-to-agent.md) | Segment 6 | Required | Required | Required | 3 min in session, 15 min full |

## Engineering track

Role-by-role tiers and session plan: [track page](tracks/engineering/README.md). Repo setup overview: [repo-setup](tracks/engineering/repo-setup/README.md).

| Module | ENG | PX | BIZ | Time |
|---|---|---|---|---|
| [E-01 Coding assistants and agents: ways of working](tracks/engineering/E-01-coding-assistants-and-agents.md) | Required | · | · | 20 min |
| [E-02 The safe change loop and git](tracks/engineering/E-02-safe-change-loop-and-git.md) | Required | · | · | 25 min |
| [E-03.1 Structure and instruction files](tracks/engineering/repo-setup/E-03.1-structure-and-instruction-files.md) | Required* | · | · | 20 min |
| [E-03.2 Permissions and modes](tracks/engineering/repo-setup/E-03.2-permissions-and-modes.md) | Required* | · | · | 25 min |
| [E-03.3 Sandboxing and isolation](tracks/engineering/repo-setup/E-03.3-sandboxing-and-isolation.md) | Required* | · | · | 20 min |
| [E-03.4 Ignore rules and secrets](tracks/engineering/repo-setup/E-03.4-ignore-rules-and-secrets.md) | Required | · | · | 15 min |
| [E-03.5 Skills: choosing and writing them](tracks/engineering/repo-setup/E-03.5-skills.md) | Recommended | · | · | 25 min |
| [E-03.6 Memory, knowledge, specs, state and handoffs](tracks/engineering/repo-setup/E-03.6-memory-knowledge-specs-state-handoffs.md) | Required* | Optional* | · | 25 min |
| [E-04 Specs and context engineering for code](tracks/engineering/E-04-specs-and-context-engineering.md) | Required* | Recommended* | · | 25 min |
| [E-05 Verification, testing and QA](tracks/engineering/E-05-verification-testing-and-qa.md) | Required* | · | · | 25 min |
| [E-06 Architecture and design work](tracks/engineering/E-06-architecture-and-design-work.md) | Required* | · | · | 20 min |
| [E-07 Security for AI-assisted development](tracks/engineering/E-07-security-for-ai-assisted-development.md) | Required* | · | · | 20 min |
| [E-08 Automation and operations](tracks/engineering/E-08-automation-and-operations.md) | Required* | · | · | 25 min |
| [E-09 Extending agents: connectors, sub-agents and teams](tracks/engineering/E-09-extending-agents.md) | Recommended* | · | · | 25 min |

## Product and experience track

Role-by-role tiers and session plan: [track page](tracks/product-experience/README.md).

| Module | ENG | PX | BIZ | Time |
|---|---|---|---|---|
| [P-01 Discovery and synthesis](tracks/product-experience/P-01-discovery-and-synthesis.md) | · | Required | · | 20 min |
| [P-02 Requirements and specs](tracks/product-experience/P-02-requirements-and-specs.md) | Recommended* | Required* | · | 25 min |
| [P-03 Planning, delivery and reporting](tracks/product-experience/P-03-planning-delivery-and-reporting.md) | · | Required* | · | 20 min |
| [P-04 Design and prototyping](tracks/product-experience/P-04-design-and-prototyping.md) | · | Required* | · | 25 min |
| [P-05 Content and UX writing](tracks/product-experience/P-05-content-and-ux-writing.md) | · | Required* | · | 20 min |
| [P-06 Data and analysis](tracks/product-experience/P-06-data-and-analysis.md) | · | Required* | Optional* | 20 min |

## Business and people track

Role-by-role tiers and session plan: [track page](tracks/business-people/README.md).

| Module | ENG | PX | BIZ | Time |
|---|---|---|---|---|
| [B-01 Communications and documents](tracks/business-people/B-01-communications-and-documents.md) | · | · | Required | 20 min |
| [B-02 Research and decision briefs](tracks/business-people/B-02-research-and-decision-briefs.md) | · | Recommended* | Required* | 20 min |
| [B-03 People operations](tracks/business-people/B-03-people-operations.md) | · | · | Required* | 20 min |
| [B-04 Business development](tracks/business-people/B-04-business-development.md) | · | · | Required* | 20 min |
| [B-05 Leading adoption](tracks/business-people/B-05-leading-adoption.md) | Optional* | · | Required* | 25 min |

## Overlays

Short modules attached to track sessions. They carry what depends on the client, the place and the engagement.

| Module | In the core session | ENG | PX | BIZ | Time |
|---|---|---|---|---|---|
| [X-01 Working in a client environment](overlays/X-01-working-in-a-client-environment.md) | · | Required | Required | Required* | 10 min |
| [X-02 Jurisdiction and policy pack](overlays/X-02-jurisdiction-and-policy-pack.md) | One slide in segment 4 | Required | Required | Required | 2 min in session |
| [X-03 End-to-end engagement map](overlays/X-03-end-to-end-engagement-map.md) | · | Recommended | Required | Required* | 10 min |

## Session design and resources

- [S-01 Run of show](session/S-01-run-of-show.md): timing for a 120-minute and a 90-minute booking, checkpoints, what to cut.
- [S-02 Workshop](session/S-02-workshop.md): one exercise, three role packs, a planted trap in each.
- [R-01 Further reading](resources/R-01-further-reading.md): primary sources by topic.
- [R-02 Glossary seed](resources/R-02-glossary-seed.md): terms to define and how to render them in French.
- [R-03 Asset backlog](resources/R-03-asset-backlog.md): what has to be produced from this outline.

## Suggested rollout

1. Before anything: approved tools, accounts and the one-page data matrix are in place ([X-02](overlays/X-02-jurisdiction-and-policy-pack.md), [B-05](tracks/business-people/B-05-leading-adoption.md)).
2. The common session, for everyone.
3. Track sessions within two weeks, while the common session is fresh.
4. A leadership session on adoption ([B-05](tracks/business-people/B-05-leading-adoption.md)), ideally before the track sessions so that policy questions have answers.
5. Open office hours, and a short recurring update when the landscape snapshot ([C-02](core/C-02-landscape-snapshot.md)) is refreshed.

## Conventions

- Module IDs are stable. A module that is replaced keeps its ID; a retired ID is not reused.
- One module card becomes one French lesson file and one group of slides, with the same ID. Updating a topic means touching one card and its lesson.
- Product names and version numbers belong in [C-02](core/C-02-landscape-snapshot.md) and in each card's "Re-verify before each delivery" list. Everything else is written to survive a change of vendor.
- Examples are fictional and organization-neutral. Practice material is synthetic.
- A card's checkpoint is a question the presenter asks the room, with a pause, before moving on.
