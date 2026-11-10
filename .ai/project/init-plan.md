# Initialization plan

- Status: approved by the author on 2026-11-10; Phase 2 in progress
- Date: 2026-11-10
- Stage: init

This file is the resume point while the stage is `init`. If a session starts without context, read this file from top to bottom, then the progress log at the end. Nothing here is learner-facing; it is written in English.

## 0. Inputs and decisions already taken

Inputs: the curriculum outline (`.ai/project/seed/curriculum/`, 36 module cards plus S-01, S-02, R-01 to R-03) and `.ai/project/seed/suggestions.md`.

Decisions from the Phase 0 questions (each becomes a decision record in Batch 2b):

| # | Decision |
|---|---|
| Q1 | Visual direction **A · Wayfinding**, with a dark variant |
| Q2 | `README.md` is fully bilingual (English, then French) |
| Q3 | Lesson tree: English directory and file names that match the card file names; French content |
| Q4 | Presenter-only material (speaker notes, run of show, presenter copies of packs) is in French |
| Q5 | Build toolchain: a Python virtual environment with python-pptx (decks) and WeasyPrint (PDF from Markdown via HTML); LibreOffice renders previews |
| Q6 | Built decks and PDFs are ignored by git and attached to a GitHub release when a delivery is scheduled |
| Q7 | Suggested commit messages follow Conventional Commits, with no attribution trailer |
| Q8 | Scripts are MIT-licensed (SPDX header plus `LICENSES/MIT.txt`); everything else is CC BY 4.0 |
| Q9 | The seed's text about the human-owned prompt folder is kept as is; that folder is out of scope |
| Q10 | Every git read command an agent runs excludes `.ai/prompts/` with a pathspec; no settings change |
| Q11 | Product names may appear where a card's topics require them; version numbers, release numbers and dated behaviour stay in C-02, "re-verify" lists and dated resource lists |
| Q12 | The curriculum outline is the specification; `suggestions.md` is a backlog, and each item the cards do not already reflect gets an accept/drop entry in the open-decisions list |
| Q13 | During the move, only the sentences that refer to documents outside the repository are rewritten so each stands alone. There are **seven**, not six as reported in Phase 0: C-02 line 8, X-03 line 8, and `suggestions.md` lines 13, 20, 21, 29, 30 |
| Q14 | Seed problems P1 to P4 and P6 become open decisions with a proposed fix, resolved when the affected lesson is written |
| Q15 | Decks must work in LibreOffice (main target) and in PowerPoint; the author can test in PowerPoint on request |
| Q16 | The dark variant applies to README images and to an optional dark deck theme; PDFs and handouts are light only |

Confirmed on 2026-11-10 (section 10): Q9 does not stop the seed from moving into `spec/` as section 7.2 of the brief requires; it means its statements about the prompt folder are not edited.

## 1. Directory tree

Paths marked *(first use)* are created by the batch that first needs them, not during setup.

```text
.
├── AGENTS.md                     Working rules for any coding agent; single source of rules
├── CLAUDE.md                     Imports AGENTS.md; Claude Code specifics only
├── DESIGN.md                     Visual and editorial direction (Wayfinding), tokens, patterns to avoid
├── README.md                     Bilingual hub page: English, then French
├── LICENSE                       CC BY 4.0 legal code, official text
├── LICENSES/MIT.txt              MIT licence for scripts that carry an SPDX header
├── THIRD_PARTY_NOTICES.md        Every third-party item: source, version or commit, licence, path
├── .gitignore                    What git does not track (not an access control)
├── .claude/
│   ├── settings.json             Unchanged
│   └── skills/<name>/SKILL.md    Project skills, one folder each (8 at lock, section 6)
├── .ai/
│   ├── project/
│   │   ├── state.md              Stage line, current focus, next steps, open questions
│   │   ├── init-plan.md          This file; becomes decision 0001 at lock (section 9)
│   │   ├── skills-register.md    One row per skill: purpose, source, commit, licence, owner, review date
│   │   ├── spec/
│   │   │   ├── README.md         Entry point to the specification (replaces seed/README.md)
│   │   │   ├── deliverables.md   Deliverable types and the definition of done for each
│   │   │   ├── build-order.md    Production order, extending R-03 with tooling and textbooks
│   │   │   ├── module-map.md     ID → card → lesson path → session deck → textbook(s)
│   │   │   ├── open-decisions.md Open content and program decisions, each with a proposal
│   │   │   ├── suggestions.md    Moved from the seed; backlog of proposals
│   │   │   └── curriculum/       Moved from the seed; module cards unchanged except Q13
│   │   ├── decisions/            README.md (format) and NNNN-slug.md records
│   │   ├── handoffs/             TEMPLATE.md and YYYY-MM-DD-slug.md, one per work session
│   │   └── knowledge/            README.md and dated topic notes
│   └── prompts/                  Human-owned; agents never read, list, search or write it
├── templates/
│   └── lesson.md                 Lesson template: French headings, English guidance in comments
├── lessons/                      One French lesson per module; paths mirror spec/curriculum/
│   ├── core/
│   ├── tracks/engineering/
│   ├── tracks/engineering/repo-setup/
│   ├── tracks/product-experience/
│   ├── tracks/business-people/
│   └── overlays/
├── sessions/                     Presenter guide for the common session, from S-01 (first use)
├── workshops/                    S-02 facilitator guide, packs A/B/C with presenter copies, track versions (first use)
├── handouts/                     One-page handouts listed in R-03 (first use)
├── resources/                    Further reading (R-01), glossary (R-02), fictional engagement brief (first use)
├── decks/<session>.toml          Deck manifests: which lessons make each session deck (Phase 3)
├── books/<book>/                 Textbook manifest and French front and back matter: core, engineering,
│                                 product-experience, business-people (Phase 3, first use)
├── assets/
│   ├── fonts/                    Open-licensed font files with their licence (Phase 3)
│   ├── diagrams/                 SVG sources for lesson and textbook diagrams (first use)
│   └── readme/                   README images, light and dark (Batch 4)
├── tools/                        Build and check scripts (MIT); pinned requirements.txt (Phase 3)
└── build/                        Generated decks, PDFs and previews (ignored)
```

### 1.1 Module ID to lesson file

Rule: a lesson has the same relative path under `lessons/` as its card has under `.ai/project/spec/curriculum/`. One ID, one card, one lesson, one group of slides.

| ID | Relative path of card and lesson |
|---|---|
| C-01 | `core/C-01-mental-model-and-vocabulary.md` |
| C-02 | `core/C-02-landscape-snapshot.md` |
| C-03 | `core/C-03-task-fit-and-limits.md` |
| C-04 | `core/C-04-working-loop-and-prompting.md` |
| C-05 | `core/C-05-context.md` |
| C-06 | `core/C-06-gates-and-human-review.md` |
| C-07 | `core/C-07-data-security-and-responsible-use.md` |
| C-08 | `core/C-08-from-assistant-to-agent.md` |
| E-01 | `tracks/engineering/E-01-coding-assistants-and-agents.md` |
| E-02 | `tracks/engineering/E-02-safe-change-loop-and-git.md` |
| E-03.1 | `tracks/engineering/repo-setup/E-03.1-structure-and-instruction-files.md` |
| E-03.2 | `tracks/engineering/repo-setup/E-03.2-permissions-and-modes.md` |
| E-03.3 | `tracks/engineering/repo-setup/E-03.3-sandboxing-and-isolation.md` |
| E-03.4 | `tracks/engineering/repo-setup/E-03.4-ignore-rules-and-secrets.md` |
| E-03.5 | `tracks/engineering/repo-setup/E-03.5-skills.md` |
| E-03.6 | `tracks/engineering/repo-setup/E-03.6-memory-knowledge-specs-state-handoffs.md` |
| E-04 | `tracks/engineering/E-04-specs-and-context-engineering.md` |
| E-05 | `tracks/engineering/E-05-verification-testing-and-qa.md` |
| E-06 | `tracks/engineering/E-06-architecture-and-design-work.md` |
| E-07 | `tracks/engineering/E-07-security-for-ai-assisted-development.md` |
| E-08 | `tracks/engineering/E-08-automation-and-operations.md` |
| E-09 | `tracks/engineering/E-09-extending-agents.md` |
| P-01 | `tracks/product-experience/P-01-discovery-and-synthesis.md` |
| P-02 | `tracks/product-experience/P-02-requirements-and-specs.md` |
| P-03 | `tracks/product-experience/P-03-planning-delivery-and-reporting.md` |
| P-04 | `tracks/product-experience/P-04-design-and-prototyping.md` |
| P-05 | `tracks/product-experience/P-05-content-and-ux-writing.md` |
| P-06 | `tracks/product-experience/P-06-data-and-analysis.md` |
| B-01 | `tracks/business-people/B-01-communications-and-documents.md` |
| B-02 | `tracks/business-people/B-02-research-and-decision-briefs.md` |
| B-03 | `tracks/business-people/B-03-people-operations.md` |
| B-04 | `tracks/business-people/B-04-business-development.md` |
| B-05 | `tracks/business-people/B-05-leading-adoption.md` |
| X-01 | `overlays/X-01-working-in-a-client-environment.md` |
| X-02 | `overlays/X-02-jurisdiction-and-policy-pack.md` |
| X-03 | `overlays/X-03-end-to-end-engagement-map.md` |

The session and resource cards are not modules; they map to other deliverables:

| ID | Card (under `spec/curriculum/`) | Deliverable |
|---|---|---|
| S-01 | `session/S-01-run-of-show.md` | `sessions/S-01-run-of-show.md` (presenter guide, French) |
| S-02 | `session/S-02-workshop.md` | `workshops/S-02-workshop.md` (facilitator guide) and the pack files beside it |
| R-01 | `resources/R-01-further-reading.md` | `resources/R-01-further-reading.md` (French) |
| R-02 | `resources/R-02-glossary-seed.md` | `resources/R-02-glossary.md` (French; built later) |
| R-03 | `resources/R-03-asset-backlog.md` | None: stays in the spec, extended by `spec/deliverables.md` |

`spec/module-map.md` (Batch 2b) repeats the first table and adds, per ID, the session deck it belongs to (from the track pages) and the textbook(s) that include it.

### 1.2 Lesson anatomy (finalized in the Batch 5 template)

A lesson file carries three layers, so that the textbook, the deck and the presenter each take what they need from one source:

1. **Learner text**: plain Markdown prose, read on GitHub and in the textbook.
2. **Slides**: regions marked with HTML comments, invisible on GitHub, parsed by the deck builder. The slide type is one of `title`, `section`, `concept`, `example`, `checkpoint`, `exercise`, `recap`.
3. **Speaker notes**: a collapsible `<details>` block inside each slide region. GitHub shows it folded; the deck builder puts it in the notes pane; the textbook leaves it out.

```markdown
<!-- slide: concept -->
### Titre de la diapositive, rédigé comme une affirmation
Contenu visible de la diapositive.
<details><summary>Notes de présentation</summary>

Texte intégral à dire, avec repères de temps.

</details>
<!-- /slide -->
```

YAML front matter holds `id`, `title`, `card`, `track`, `minutes`, `status` (`draft`, `review`, `ready`), `last_verified` and `glossary` terms. GitHub renders it as a table. Section order follows the pedagogical pattern in DESIGN.md: outcomes, then units of concept and example, then checkpoint, practice, recap, further reading, and the "re-verify" list.

## 2. Outlines of the governance files

### 2.1 `AGENTS.md` (target ≤ 150 lines)

1. **The project**, four lines: a training program on working with AI assistance; a common session plus three tracks; deliverables in Canadian French, everything else in English; built in small reviewed steps.
2. **Map**: one line per location in section 1, with *(first use)* paths marked.
3. **Source of truth when files disagree**: the author's instruction in the current conversation; then `AGENTS.md` (and `CLAUDE.md` for Claude Code); then accepted decision records (newer over older); then `DESIGN.md` for anything visual or editorial; then the specification (a module card for its own module); then `state.md` and the latest handoff; then knowledge notes; then existing deliverables. A disagreement is itself a reason to stop and ask.
4. **Session routine**: at start, read `state.md`, the latest handoff, and `git status` (with the exclusion pathspec). If changes from the previous batch are uncommitted, ask before adding more. During stage `init`, follow the initialization plan. At end, update `state.md`, write a handoff from the template, and give a suggested commit message.
5. **Working loop for a task**: read the module card and its `module-map.md` row; state the plan (files and checks); make one small change; run the quality gates; report; stop for review.
6. **Report format**: the batch report block (files, checks, decisions made, open questions, suggested commit message, next, waiting for).
7. **Git**: the author owns the index, history and branches. The forbidden commands are listed by name (`add`, `commit`, `push`, `pull`, `merge`, `rebase`, `reset`, `restore`, `checkout`, `switch`, `stash`, `tag`, `clean`, `mv`, `rm`, `config`, `remote`). Read-only commands are allowed, and every one carries `-- . ':(exclude).ai/prompts'`. Files are moved or deleted with ordinary file operations, and only when the approved plan says so. Commit convention: `type(scope): imperative summary`, ≤ 72 characters; types `feat`, `fix`, `docs`, `build`, `refactor`, `style`, `chore`; scope is a module ID or an area; no trailer.
8. **Stop and ask**: the nine conditions of the brief, worded for ongoing work. How to ask: everything in one message, numbered, each with a recommended answer and what changes with the answer, then end the turn.
9. **Lifecycle and lock**: the stage line in `state.md`; the locked paths (section 3); the three-part rule; a note that the lock is a rule backed by the author's review, not a technical barrier.
10. **Content rules**:
    - Language policy, with the glossary deciding terms.
    - Content is organization-neutral: no real employer, client, team or private person appears.
    - Examples and practice material are fictional and synthetic.
    - No invented facts, statistics, quotations or testimonials.
    - The product-name rule from Q11.
    - Third-party material keeps its licence and is listed in the notices.
    - No secrets, personal data or transcripts in any file.
11. **Quality gates** before a deliverable is reported done:
    - It covers its card (outcomes, required topics, checkpoint).
    - It follows the template and `DESIGN.md`.
    - It passes `slop-check` for text and visuals, and `canadian-french`.
    - Speaker notes fit the budget of about 110 words per planned minute.
    - Facts and links are dated or checked.
    - Contrast and alt text meet the accessibility minimums.
    - Built outputs were rendered and inspected.
    - Front matter `status` is updated.
    - Native-speaker review is flagged as pending.
12. **Off limits**: `.ai/prompts/` is human-owned; never read, list, search or write it, by any tool.

### 2.2 `CLAUDE.md` (target ≤ 30 lines)

1. Line 1: `@AGENTS.md`.
2. **Project skills**: one line each saying when to use it (Batch 1 writes "none yet"; Phase 3 fills it).
3. **Routing**: for decks, PDFs and documents, use the project skill `publish`, not account-level document skills such as `pptx` or `pdf`.
4. **Memory**: auto memory under the home directory is local to this machine and is not the project's memory. Facts the project needs go in `.ai/project/` (state, decisions, knowledge).
5. **Two hard boundaries, restated** for the auto-mode classifier, which reads `CLAUDE.md` and may not expand imports: no git command that changes the index, history or branches; never read, list, search or write `.ai/prompts/`. `AGENTS.md` stays the authoritative text. This is a deliberate, two-line exception to "no duplication".
6. **Sub-agents**: only when the author asks, or for the cold-start test.

### 2.3 `DESIGN.md`

1. **Principles**: wayfinding as the idea. The program is a map, each slide says where you are, and colour identifies, never decorates. Dials, in the anti-slop catalogue's terms: ENERGY 1, RHYTHM 2, MOTION 1.
2. **Colour tokens**: light and dark tables with computed WCAG ratios (values from Phase 0, re-computed by script), and a machine-readable TOML block that the build tools parse, so the tokens have one source. Usage rules:
   - one track colour per artifact (which keeps each slide within the catalogue's palette cap);
   - signal yellow only for checkpoints;
   - colour is never the only cue.
3. **Typography**:
   - Atkinson Hyperlegible Next and Atkinson Hyperlegible Mono (OFL; licence and glyph coverage for « », U+00A0 and U+202F to be verified on the files in Phase 3).
   - Projection sizes: title 40 to 44 pt, body at least 24 pt, nothing under 18 pt.
   - Line length, and paper size (US Letter, the Canadian default).
   - The deck font strategy: embedded fonts if the Phase 3 test proves they work in LibreOffice and PowerPoint; otherwise a metric-compatible pair available on both (candidate: Carlito in LibreOffice, Calibri in PowerPoint).
4. **Slide system**:
   - 16:9 at 13.333 × 7.5 in, with a grid and margins.
   - The seven slide types, with a layout for each.
   - Word limits per slide (title and body), one idea per slide.
   - The stop map as the identity motif.
   - Light theme by default, dark theme optional.
5. **Diagrams and imagery**:
   - Line-map and flow diagrams in SVG, with stroke widths and text labels on every element.
   - Screenshots only when real and dated.
   - No stock photography, no generated people, no robot, brain or sparkle imagery.
6. **Documents**: handout layout, the textbook page system (chapter openers in the track colour, running heads, checkpoint and practice callouts), README images in light and dark versions switched by `<picture>`.
7. **Editorial voice for French deliverables**:
   - Plain language, "vous", active voice, one idea per paragraph.
   - Speaker notes for a novice presenter: full sentences, timing marks, pauses, the exact transition into each checkpoint, "si vous êtes en retard" markers.
8. **Pedagogical patterns**:
   - outcome, concept, example, checkpoint, practice, recap;
   - a concrete example before the abstraction;
   - one running example through the common session;
   - the checkpoint protocol: question, real pause, two or three answers, a one-sentence recap.
9. **Canadian French typography and usage**: each rule is confirmed against the Office québécois de la langue française (Banque de dépannage linguistique, Grand dictionnaire terminologique), with the URL and date checked, or confirmed with the author. Covers:
   - spaces before punctuation and inside « »;
   - capitals in titles;
   - numbers, currency, times and dates;
   - abbreviations;
   - inclusive writing;
   - dashes.
10. **Accessibility minimums**: the projection contrast targets from Phase 0; meaning never carried by colour alone; alt text; reading order in PDFs; handouts usable without the slides.
11. **Patterns to avoid**: named visual and text patterns, each with a one-line reason and where it is catalogued. Sources: the brief's list, anti-slop (core Part 1 and copywriting), and the AI-design clusters in Anthropic's frontend-design and pptx skills. The list includes French equivalents of the text patterns and the specific choices this direction needs: no edge line (section 10), tinted near-black ink with its written reason, middle-dot separators, and dash connectors.
12. **Sources**, dated.

### 2.4 `README.md` (bilingual)

1. Title and a one-line description, then a link to the French version.
2. Restrained badges: licence, status ("in preparation"), language.
3. Program map image (Wayfinding line map, light and dark).
4. What the hub is and who it is for.
5. How the material is organized: common core, three tracks, overlays, resources (a table).
6. How to use it as a learner, as a presenter, as a contributor.
7. Status, stated plainly: nothing is built yet.
8. Licence:
   - CC BY 4.0 with a link;
   - the line `Copyright © 2026 [Saad Sidqui](https://saad.sidqui.ma).` exactly;
   - third-party material under its own licence (link to the notices);
   - scripts under MIT.
9. The French version mirrors sections 1 to 8, with the copyright line repeated unchanged.

### 2.5 Files under `.ai/project/`

- `state.md`: `Stage: init` on its own line; current focus; next steps; open questions; last updated.
- `spec/README.md`:
  - what the specification is and how to read a card;
  - precedence inside the spec (card over track page over index for a module's content);
  - links to the curriculum index, the module map, deliverables, build order, open decisions and the backlog.
  - It replaces `seed/README.md` and does not restate the curriculum's conventions; it points to them.
- `spec/deliverables.md`: one section per type (lesson, presenter guide, workshop facilitator guide, workshop pack with presenter copy, handout, glossary, further reading, fictional engagement brief, deck, textbook, README visuals). Each gives source, format, location, language and a checkable definition of done. Human-made items (demonstration recording, survey form) are listed with the author as owner.
- `spec/build-order.md`: R-03's order, extended with:
  - tooling before the first deck;
  - the core textbook after the core lessons and packs;
  - each track textbook after that track's lessons and overlays.
- `spec/module-map.md`: section 1.1 plus session deck and textbook membership.
- `spec/open-decisions.md`:
  - P1 to P4 and P6, each with a proposed fix;
  - the backlog items not yet reflected in the cards (accept or drop);
  - P8's glossary candidates;
  - the items in section 8 of this plan.
- `decisions/README.md`: the record format below, the numbering, and the immutability rule. There is no separate index: `ls decisions/` lists the records, and supersession is found by searching for `Supersedes:`.

  ```text
  # NNNN. Title
  Date: YYYY-MM-DD
  Status: proposed | accepted
  Supersedes: NNNN or none
  ## Context
  ## Decision
  ## Consequences
  ```
- `decisions/0002` to `0011`, one per group of Phase 0 decisions: language policy (Q2, Q3, Q4); visual direction (Q1, Q16); build toolchain and compatibility target (Q5, Q15); built outputs (Q6); commit convention (Q7); licensing (Q8); specification and backlog (Q11, Q12); seed amendments on the move (Q13); seed problems as open decisions (Q14); git read exclusion (Q10). Number 0001 is reserved for this plan.
- `handoffs/TEMPLATE.md`: goal; done; files changed (including any locked file changed, quoting the approval); checks run and results; open questions; next step.
- `knowledge/README.md`: what belongs (curated, dated facts with a source); what does not (secrets, personal data, transcripts); prune when stale.
- `knowledge/claude-code.md`: the facts verified on 2026-11-10, with quotes and URLs:
  - the `AGENTS.md` fallback and `@AGENTS.md` import;
  - the root `CLAUDE.md` is re-read after `/compact`;
  - "Keep `SKILL.md` under 500 lines";
  - settings precedence;
  - protected paths;
  - deny rules and Bash.
- `knowledge/environment.md`: the tools and versions found on this machine and what is missing (no personal data).
- `skills-register.md`: a table with name, purpose, source, version or commit, licence, owner and date reviewed (Batch 2b writes the header; Phase 3 fills it).

## 3. Lifecycle and lock

Stages: `init` now; after the author confirms in Phase 4, `build` (name confirmed on 2026-11-10). The lock applies in every stage after `init`.

Locked paths, relative to the repository root:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `DESIGN.md`
4. `README.md`
5. `LICENSE`
6. `LICENSES/**`
7. `THIRD_PARTY_NOTICES.md`
8. `.gitignore`
9. `.claude/**` (settings and every skill folder)
10. `.ai/project/spec/**`
11. `.ai/project/decisions/README.md` and every record whose status is `accepted`. A new record may be added as `proposed`; it becomes `accepted` only when the author says so.
12. `.ai/project/skills-register.md`
13. `.ai/project/handoffs/TEMPLATE.md`
14. `templates/**`
15. `assets/fonts/**`

Writable without approval:
- `.ai/project/state.md`;
- new handoffs and `knowledge/**`;
- every deliverable area (`lessons/`, `sessions/`, `workshops/`, `handouts/`, `resources/`, `decks/`, `books/`);
- `assets/` other than fonts;
- `tools/`.

A change of dependency in `tools/requirements.txt` still needs approval, because it installs something.

The rule written into `AGENTS.md`:

- Before editing a locked file, stop. Say which file, what would change and why, and show the proposed change.
- Proceed only when the author approves in the conversation, naming the file. An approval covers that change and nothing else, and does not carry over to another session.
- Record each approved change in the handoff.

This lock is a rule the agent follows, not a technical barrier. It is backed by the author's review of every diff before commit. No permission rule enforces it unless the author asks for one.

## 4. `.gitignore` (full proposed content)

```gitignore
# An ignore rule is not an access control: agents and tools can still read ignored files.

# Personal and local agent files
.claude/settings.local.json
CLAUDE.local.md
.claude/worktrees/

# Environment files
.env
.env.*
!.env.example

# Python tooling
.venv/
__pycache__/
*.py[cod]

# Built output: decks, PDFs, previews, tool caches (published as release assets, not committed)
/build/

# Office lock and temporary files
~$*
.~lock.*#
*.tmp

# Editors
.vscode/
.idea/
*.swp
*.swo
*~

# Operating systems
.DS_Store
Thumbs.db
desktop.ini
.directory
```

Tool caches (the LibreOffice profile and the fontconfig cache for the repository's fonts) are pointed at `build/` by the tools, so they need no rule of their own.

## 5. Changes to `.claude/settings.json`

None.

Risks considered and left to instructions:

| Risk | Why no rule |
|---|---|
| An agent runs a git command that changes the index or history | Stated in `AGENTS.md` and restated in `CLAUDE.md`, which the classifier reads; easy to undo; a deny rule that matches command text is easy to get around and adds little over your review |
| A git read command prints names or contents from `.ai/prompts/` | Q10: the exclusion pathspec in every git read command |
| A locked file is edited without approval | Section 3: rule plus review, by your choice |

I may propose allow rules for the build commands in Phase 3, to reduce prompts. That would be a convenience, not a risk control, and I will ask then.

## 6. Skills

### 6.1 Proposed set: 8 folders

| Folder | Covers | Source | Invocation |
|---|---|---|---|
| `slop-check` | Anti-slop review of text (English and French) and visuals | Written here; includes pinned anti-slop files as references | Model |
| `visual-design` | Diagrams, README images (light and dark), slide and page layout decisions, contrast checks, all from `DESIGN.md` | Written here | Model |
| `lesson-writing` | Lessons for a mixed audience and a novice presenter: one idea at a time, example before abstraction, checkpoints, full speaker notes | Written here | Model |
| `canadian-french` | Terminology against the glossary, OQLF typography, anglicisms, register | Written here | Model |
| `publish` | Decks (python-pptx) and textbooks (WeasyPrint) from lessons and manifests; LibreOffice previews; visual QA | Written here, with `tools/` | Model |
| `session-handoff` | End of session: state update, handoff from the template, suggested commit message | Written here | User only (`/session-handoff`) |
| `grilling` | Interview in rounds to complete a specification or an open decision | mattpocock/skills, pinned copy | Model |
| `writing-for-agents` | Writing and pruning `AGENTS.md`, `CLAUDE.md` and skills | mattpocock/skills, pinned copy | Model |

### 6.2 Third-party candidates

All candidate files were read as text in a scratch area outside the repository. Nothing was executed or installed. Commits are the heads on 2026-11-10.

**miqdadbadjuber/anti-slop**: MIT; single maintainer; very active (release 3.2.28, commit `41b85ede0257f39bfcffedf3f58c3c59bcc8530d`, 2026-11-10). Six skills, plugin manifests for seven agents, an `npx` installer (Node) that writes into agent folders, and an MCP contrast server (Python, launched by Node).

| Skill | What it is | Context cost | Fit, overlaps, conflicts | Verdict |
|---|---|---|---|---|
| `antislop` (core) | A filter, not a style guide: 40 rules in three tiers, the Part 1 pattern catalogue, a delivery gate. 700 lines, no scripts | ≈ 13,500 tokens | High for the catalogue and the purpose test. Low for its web-only rules (mobile, navigation, UI states, keyboard, Web Vitals). Conflicts: (1) asks a "during or after" mode question every session unless a settings file exists in the home directory, which it may write; (2) writes audit files to an `anti-slop/` folder; (3) its description says "load always"; (4) bans the em dash in all text; (5) caps the palette at 2–3 core colours plus 1 accent; (6) lists "Colored Left Stripe"; (7) exceeds the 500-line guidance | **Adopt in part**: an unmodified pinned copy as a reference file inside `slop-check`, not as a skill, read by line range. `slop-check` sets aside the mode question, the settings file, the audit path and the web-only rules; `DESIGN.md` settles (4) to (6) |
| `antislop-copywriting` | English prose tells with before and after, a "what not to flag" list, a draft-audit-final loop. 407 lines, no scripts | ≈ 7,000 tokens | High for English text. French needs equivalents, which `slop-check` adds | **Adopt in part**: reference file, as above |
| `antislop-ui` | Web UI depth: visual, layout, decoration, app and dashboard, motion, performance. 344 lines | ≈ 7,300 tokens | Its visual and decorative entries restate core Part 1 at length; the rest is web-specific | **Skip** |
| `antislop-human` | Web accessibility, with `contrast-check.py` and an MCP server (also MIT, from another author) | ≈ 4,000 tokens | Web-oriented; a small contrast script of our own covers our need | **Skip** (not adopted, so its scripts were listed but not read line by line) |
| `antislop-code`, `antislop-layoutmobile` | Code-comment hygiene; mobile layout | — | No fit | **Skip** |

**anthropics/skills**: maintained by Anthropic; commit `2c5958ecac7cee2b583967a2c4981d0f4a75c579` (2026-11-06, "Move Office skills to the Apache 2.0 license"). Every candidate folder carries an Apache-2.0 `LICENSE.txt` except `doc-coauthoring`, which has none; the repository has no top-level licence. Several of these skills are also available to you as account-level skills, outside the repository.

| Skill | What it is | Context cost | Fit, overlaps, conflicts | Verdict |
|---|---|---|---|---|
| `frontend-design` | Web design direction. Its list of current AI-design defaults: cream background with a serif and a clay accent; near-black with one acid accent; broadsheet hairlines; the SaaS card kit; template chrome such as all-caps eyebrows, middle-dot meta strings, spaced em-dash labels, tinted near-black, mono data labels and appended arrows. "Structure is information"; numbered markers only for real sequences. 71 lines, no scripts | ≈ 2,000 tokens | Medium as a skill (web pages); high as input to `DESIGN.md` | **Adopt in part**: its named patterns are paraphrased into `DESIGN.md` with credit; no copy |
| `canvas-design` | Posters and art from a "design philosophy"; 81 bundled OFL fonts; tells the agent to download fonts freely | ≈ 3,000 tokens | Low: we need diagrams that follow `DESIGN.md`, not art | **Skip** |
| `theme-factory` | Ten preset themes and a showcase PDF | small | Conflicts with one chosen direction | **Skip** |
| `pptx` | Creates decks with pptxgenjs (Node); scripts for thumbnails, slide duplication, cleanup, OOXML schema validation and a LibreOffice wrapper; needs markitdown, lxml and defusedxml | ≈ 5,000 tokens | Different generator from our python-pptx choice. Useful ideas: render with LibreOffice and inspect every slide; fonts that keep their metrics in LibreOffice (Arial, Calibri, Cambria and others; never Aptos); "no vertical sidebar stripes, no accent lines under titles". Your account-level copy can trigger on "deck", so `CLAUDE.md` routes deck work to `publish` | **Adopt in part**: ideas only, paraphrased into `publish` and `DESIGN.md`. SKILL.md read in full and the scripts listed; the scripts were not read line by line because nothing is copied or run |
| `doc-coauthoring` | Three-stage co-authoring workflow with sub-agent reader tests. 375 lines | ≈ 4,000 tokens | Overlaps `grilling`. Licence unclear (no file in the folder) | **Skip** |
| `skill-creator` | Skill authoring plus an evaluation harness (scripts, viewer, grader agents) | ≈ 8,000 tokens | Not needed at run time; already in your account | **Skip** copying; I may read its guidance while writing skills, without running its scripts |
| `pdf` (found, not listed) | PDF manipulation (pypdf and similar) | — | WeasyPrint chosen | **Skip** |

**mattpocock/skills**: MIT; single maintainer; widely used; commit `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` (2026-10-31; repository pushed 2026-11-09). Offered as a plugin or as copies; using both would duplicate every skill.

| Skill | What it is | Context cost | Fit, overlaps, conflicts | Verdict |
|---|---|---|---|---|
| `handoff` | User-invoked; writes a free-form handoff to the OS temp directory | tiny | Conflicts with `handoffs/` and the six-part template | **Skip**; `session-handoff` replaces it |
| `grilling` (and its alias `grill-me`) | Interview in rounds: a design tree, numbered questions with a recommended answer each, facts looked up by a sub-agent. 30 lines, no scripts | ≈ 500 tokens plus its description | High for open decisions and the fictional engagement brief; matches how questions are asked here. Its sub-agent step runs only when you invoke it | **Adopt** `grilling` as a pinned copy; skip the alias, since `/grilling` works |
| `teach` | Learner-side tutor that writes HTML lessons to `./lessons` | ≈ 2,500 tokens | Would collide with our `lessons/` path and format. Its notes on retrieval practice, spacing and equal-length quiz answers are useful | **Skip**; principles paraphrased into `lesson-writing` with credit |
| `writing-for-agents` | How to write agent-facing documents: context pointers, progressive disclosure, completion criteria, pruning no-ops, positive phrasing. 81 + 22 lines, no scripts | ≈ 3,400 tokens when used | High for governance files and skills, now and for later approved changes | **Adopt**, pinned copy |

**plugin87/ux-ui-agent-skills**: MIT; single maintainer; commit `f823acedc3ef4e9b2ba944a28fd86fe2abdde427` (2026-11-10).
- Size: about 2,700 files (2,148 under `design-systems/`) and 26 skills, with about 120 Node and Python gate scripts.
- What I read: `a11y-audit`, `critique` and `ux-writing`. Each checks for the full kit and falls back to "guidance-only mode" without it.
- Fit: aimed at web interfaces, Figma and components.
- **Skip**: too heavy, and it needs the whole kit.

**kaankiziltug/logo-design-skill**: MIT; single maintainer; commit `bbf31e521d765eb6d53242549bbee7c2e5bbd6bc` (2026-11-06).
- Contents: about 1,500 files, including a library of more than 1,400 real-world SVG logos with a trademark notice, and nine Python scripts for rendering, auditing and exporting.
- **Skip** unless you decide the program needs a mark (section 8). If so, review the library's trademark terms first, and prefer a plugin on your machine to a copy.

### 6.3 Skills written here

Each one gets:
- a folder under `.claude/skills/`;
- a `SKILL.md` of at most 150 lines with: a description that says what it does and when to use it; when not to use it; the procedure; an acceptance check;
- detail in `references/`.

Each is tried on a throwaway sample in the scratch area and not committed. The samples use a fictional, off-curriculum topic, so no program content is drafted.

| Skill | Not for | References | Acceptance check | Trial |
|---|---|---|---|---|
| `lesson-writing` | Building decks; editing the spec; translating English prose | Pedagogy patterns and the checkpoint protocol; speaker-note style for a novice presenter; how card fields map to lesson sections | Card outcomes and required topics covered; pattern order kept; every slide region has notes; notes within ±15 % of 110 words per planned minute; one running example | A short lesson excerpt on an off-topic fictional card |
| `canadian-french` | English files | Typography rules (pointing to `DESIGN.md`); anglicisms with OQLF links and dates; terminology policy (R-02) | No unchecked term; spacing and quotation marks correct; every flagged anglicism has a source | A planted-error paragraph |
| `slop-check` | Writing new content | `DESIGN.md` avoid list (primary); pinned anti-slop core and copywriting; French patterns written here | Every hit reported with location, pattern and fix; clusters noted; no fact added by a fix | A planted-slop paragraph in French and English, and a planted-slop slide image |
| `visual-design` | Building decks or books end to end | `DESIGN.md` tokens and layouts; the contrast script | Light and dark variants pass the contrast targets; text labels everywhere; no avoid-list pattern | A small SVG diagram, light and dark |
| `publish` | Writing content | Manifest format; build commands; QA checklist (overflow, overlap, margins, contrast, notes present) | The build runs; every slide or page image was inspected; outputs only in `build/` | A two-slide deck and a two-page PDF from the trial lesson |
| `session-handoff` | Mid-task notes | `handoffs/TEMPLATE.md`; the `state.md` format | All six parts filled; locked-file approvals quoted; suggested commit message | A dry run into the scratch area |

### 6.4 Installation

You install third-party files. I give the exact commands in Phase 3: `curl` from the pinned commits into the target paths, plus a `sha256sum -c` check. Then I re-read the installed files and compare them with these hashes of the files I reviewed:

| File (upstream path at the pinned commit) | Installs to | SHA-256 |
|---|---|---|
| anti-slop `LICENSE` | `.claude/skills/slop-check/references/upstream/LICENSE` | `9fd83fb1fda52ca0094b96e2ed5a3d6c42a81b95a6c6326553f5bbe570f443de` |
| anti-slop `skills/antislop/SKILL.md` | `…/upstream/antislop-core.md` (renamed, content unmodified) | `30bc532fb59d4c77a301dfdd5ab9f495f098f1085f31e09b3064078ba39a7b01` |
| anti-slop `skills/antislop/VERSION` | `…/upstream/VERSION` | `0daeb969e6fe8a646347de1d59b45bd8fc48363b9465c2dad2d447a4ccceac24` |
| anti-slop `skills/antislop-copywriting/SKILL.md` | `…/upstream/antislop-copywriting.md` | `d708fc33608b4f1d41cc7bef8b5fb2aca3dc3fbc5ec1ee174b45cac23bb767cd` |
| mattpocock `LICENSE` | `.claude/skills/grilling/LICENSE` and `.claude/skills/writing-for-agents/LICENSE` | `0e7ac423bf2c6e223b7c5b156f8cf72da49d748e56a1641402c31f22ad07dbb5` |
| mattpocock `skills/productivity/grilling/SKILL.md` | `.claude/skills/grilling/SKILL.md` | `a146842ed93ca43d833550fa9adf02e58cb63c83fea9d4b4522995b82242d4e2` |
| mattpocock `skills/productivity/writing-for-agents/SKILL.md` | `.claude/skills/writing-for-agents/SKILL.md` | `551adca942227b44192edba88acd4e8db911f0121ce58ad16944ccf6a896a74a` |
| mattpocock `skills/productivity/writing-for-agents/SKILL-MECHANICS.md` | `.claude/skills/writing-for-agents/SKILL-MECHANICS.md` | `c768e6307c7c10728c401c213f2c4ba71c542127eeb7ad2956aabd15a0fa0059` |

The core file is renamed so it is not mistaken for a skill. Every third-party file is listed in `THIRD_PARTY_NOTICES.md` and `skills-register.md`. Fonts and Python packages follow the same pattern in Phase 3: I write the pinned list, you install, I verify. The Python packages live in the ignored `.venv/` and are not redistributed.

### 6.5 Conflicts that `DESIGN.md` must settle

1. Wayfinding's left-edge track line is a catalogued tell: anti-slop calls it "Colored Left Stripe" (allowed only with a written purpose), and the `pptx` skill bans vertical edge stripes outright. Decided: no edge line; the stop map and the track name identify the track (section 10).
2. Four track colours against anti-slop's palette cap: settled by one track colour per artifact.
3. The em dash: anti-slop bans it. French typography uses dashes for asides, so the rule for French is confirmed against OQLF before it is written.
4. Tinted near-black ink (`#15181D`) is listed by frontend-design as a default. It is kept, with a written reason: it reduces glare on projectors.
5. Middle-dot separators in titles (the seed uses "C-01 · Title") are a listed tell; `DESIGN.md` picks the title format for French deliverables.

## 7. Batch plan

Each batch ends with a report and a stop. The next batch starts with `git status`.

| Batch | Files | Main checks |
|---|---|---|
| **1** Working rules | `AGENTS.md`, `CLAUDE.md`, `.gitignore` | Line counts (≤ 150, ≤ 30); `CLAUDE.md` line 1 is `@AGENTS.md`; neutrality scan; the human-owned folder appears only as off limits or excluded |
| **2a** Move the seed | `seed/curriculum/**` → `spec/curriculum/**`; `seed/suggestions.md` → `spec/suggestions.md`; `seed/README.md` → `spec/README.md` (unchanged in this batch); the seven Q13 sentences rewritten | 36 cards present; every relative link resolves; `git diff -M` shows renames, plus edits in the seven lines only |
| **2b** Project memory | `spec/README.md` (rewritten), `spec/deliverables.md`, `spec/build-order.md`, `spec/module-map.md`, `spec/open-decisions.md`, `state.md`, `decisions/README.md`, `decisions/0002…0011`, `handoffs/TEMPLATE.md`, `knowledge/README.md`, `knowledge/claude-code.md`, `knowledge/environment.md`, `skills-register.md`; delete `.ai/project/.gitkeep` | Every ID in the map has a card and a lesson path; links resolve; no secrets or personal data; dates present |
| **3** Design | `DESIGN.md` (OQLF pages read to confirm each French rule) | Ratios recomputed by script; every rule sourced and dated; avoid list named, not generic |
| **4** Front door | `README.md`, `LICENSE` (fetched from creativecommons.org; if the fetch fails, I stop and ask you to add it), `LICENSES/MIT.txt` (fetched from the SPDX licence list), `THIRD_PARTY_NOTICES.md`, `assets/readme/program-map-light.svg`, `assets/readme/program-map-dark.svg` | Copyright line byte-exact; legal text identical to the source; README readable in light and dark |
| **5** Lesson tree | `templates/lesson.md`; empty directories with `.gitkeep` under `lessons/` | Template follows section 1.2 and `DESIGN.md`; no lesson content |
| **3a** (Phase 3) Skills written here | `lesson-writing`, `canadian-french`, `slop-check` (without upstream files), `visual-design`, `session-handoff` | Trials run and reported; each `SKILL.md` ≤ 150 lines |
| **3b** You install | Commands for the pinned skill files, `tools/requirements.txt` and the font files; I verify hashes and content | Hashes match section 6.4; licences present |
| **3c** Publishing | `publish` skill; `tools/` scripts; manifest format; font test in LibreOffice (PowerPoint if you choose) | Trial deck and PDF built and inspected; `DESIGN.md` typography updated with the result |
| **3d** Registers | `skills-register.md`, the skills section of `CLAUDE.md`, `THIRD_PARTY_NOTICES.md` | Every third-party item listed with source, version and licence |
| **Phase 4** | Section 9 checks of the brief; cold-start test; first handoff; report | As the brief describes; lock on your word |

## 8. Open decisions that can wait

These go into `spec/open-decisions.md` in Batch 2b.

1. Whether each track textbook includes the core lessons, so it stands alone (recommended), or points to the core book.
2. Which track's lessons come first (R-03 says the track with the most participants).
3. The fictional engagement: client, project, stages (`grilling` suits this).
4. The role that owns the landscape snapshot (C-02) and its refresh trigger.
5. P1 to P4, P6 and P8, and the accept or drop list for the backlog.
6. Whether the program needs a mark (default: no; a wordmark set in the chosen typeface).
7. How releases are named when built outputs are published.
8. Where demonstration recordings live (not in git).
9. Who reviews the French as a native speaker, and when.
10. Allow rules for build commands (a convenience), once `tools/` exists.

## 9. After the lock

At lock, this file moves to `.ai/project/decisions/0001-initialization-plan.md` with `Status: accepted` and the lock date. Its content is otherwise unchanged, including the progress log, which becomes the history of initialization. `state.md` and the first handoff point to it. `AGENTS.md` refers to "the initialization plan (decision 0001)", so it stays true after the move.

## 10. Questions answered before Phase 2 (2026-11-10)

1. **Q9 reading**: confirmed. The seed moves into `spec/`, only the seven Q13 sentences change, and the seed's statements about the prompt folder are not edited.
2. **Edge line**: dropped. The stop map (track colour plus position) and the track name identify the track.
3. **Stage name after lock**: `build`.
4. **Skill folder names**: approved as listed in section 6.1.

## Progress log

- 2026-11-10 Phase 0 complete: repository and seed read; answers to Q1 to Q16 recorded in section 0.
- 2026-11-10 Phase 1: this plan written. Section 10 questions answered (seed moves to `spec/`; no edge line; stage `build`; skill names approved). Waiting for the author's review and approval of the whole plan.
- 2026-11-10 Phase 1 approved; plan committed as `469bcc6`. Batch 1 (`AGENTS.md`, `CLAUDE.md`, `.gitignore`) started.
- 2026-11-10 Batch 1 committed as `16004ea`. Batch 2a (move the seed to `spec/`, rewrite the seven sentences) started.
- 2026-11-10 Batch 2a committed as `aab55a6`. The author approved a one-line `AGENTS.md` change (blank line between commit subject and body), made in Batch 2b. Batch 2b (project memory) started.
- 2026-11-10 Batch 2b committed as `5dcaf06`, after a fix the author asked for: `knowledge/environment.md` lists build requirements only, and `AGENTS.md` forbids recording details of a particular machine. The author confirmed that a commit counts as acceptance of the records it contains. Batch 3 (`DESIGN.md`) started.
