# Skills register

One row per project skill in `.claude/skills/`. The hashes of the third-party files are in `THIRD_PARTY_NOTICES.md`.

| Skill | Purpose | Source | Version or commit | Licence | Owner | Reviewed |
|---|---|---|---|---|---|---|
| `lesson-writing` | Write or revise a French lesson from its module card, with slides and full speaker notes | Written here | Added in `b62321f3b8e94a79b33be464e803263cce239cfb` | CC BY 4.0 (repository) | Author | 2026-11-10 |
| `canadian-french` | Check French deliverables: OQLF typography, terminology, anglicisms, inclusive writing | Written here; quotes OQLF pages (listed in its references) | Added in `b62321f3b8e94a79b33be464e803263cce239cfb` | CC BY 4.0 (repository); OQLF quotations with attribution | Author | 2026-11-10 |
| `slop-check` | Check text and visuals for machine-made patterns against `DESIGN.md` section 11 | Written here; includes pinned files from miqdadbadjuber/anti-slop in `references/upstream/` | Added in `b62321f3b8e94a79b33be464e803263cce239cfb`; upstream files at `41b85ede0257f39bfcffedf3f58c3c59bcc8530d` (release 3.2.28) | CC BY 4.0 (repository); upstream files MIT | Author | 2026-11-10 |
| `visual-design` | Diagrams, README images, slide and page layout, contrast, from `DESIGN.md` | Written here | Added in `b62321f3b8e94a79b33be464e803263cce239cfb` | CC BY 4.0 (repository) | Author | 2026-11-10 |
| `session-handoff` | End-of-session routine: state update, handoff, suggested commit message (user-invoked) | Written here | Added in `b62321f3b8e94a79b33be464e803263cce239cfb` | CC BY 4.0 (repository) | Author | 2026-11-10 |
| `publish` | Build decks and PDF textbooks from manifests, render and inspect every slide or page | Written here; uses `tools/` | Added in `e71ea173b96bfa19391e67dad52cdf59962788dc` | CC BY 4.0 (repository); `tools/` scripts MIT | Author | 2026-11-10 |
| `grilling` | Interview the author in rounds to settle a decision or complete a specification | mattpocock/skills, `skills/productivity/grilling/` | `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` | MIT | Author | 2026-11-10 |
| `writing-for-agents` | Write and prune agent-facing documents: `AGENTS.md`, `CLAUDE.md`, skills | mattpocock/skills, `skills/productivity/writing-for-agents/` | `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` | MIT | Author | 2026-11-10 |

## Rules

- **Source:** "written here" for skills authored in this repository. Otherwise, the upstream repository and path.
- **Version or commit:** for third-party files, the full commit hash of the pinned copy. Third-party skills are copies pinned to a commit, never self-updating plugins. For skills written here, the commit that added them.
- **Owner:** the role that keeps the skill current. It is the author unless stated otherwise.
- **Reviewed:** the date someone last read the whole skill, scripts included.
- **When something changes:** after initialization, adding, updating or removing a skill needs the author's approval, because `.claude/` is locked. Each such change updates this file and the notices in the same step.
- **Limit:** at most eight skill folders, unless the author approves more. Fewer skills means less context spent and fewer conflicts.
