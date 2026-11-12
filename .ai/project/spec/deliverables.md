# Deliverables

Each type of deliverable, where it comes from and lives, and its definition of done. The list extends the asset backlog in [R-03](curriculum/resources/R-03-asset-backlog.md). Every learner- or presenter-facing deliverable is written in Canadian French.

Each built deliverable serves one role (decision 0020). Learners get a study book, slides as PDF, handouts and the participant pages of the workshop packs. Presenters get the deck with speaker notes, the presenter guide and the presenter copies of the packs. Every one of them is built from the same lesson files.

## Applies to every deliverable

A deliverable is done only when:

- it passes the quality gates in `AGENTS.md`;
- it contains nothing specific to a real organization, and every example in it is fictional and synthetic;
- its native-speaker review is either recorded as done or flagged as pending.

## Lesson

- **Source:** one module card. See [`module-map.md`](module-map.md) for its path.
- **Location and format:** `lessons/<same relative path as the card>`, in Markdown with YAML front matter, following `templates/lesson.md`.
- **Done when:**
  1. The front matter is complete and its `status` is set.
  2. The card's outcomes are stated. Every required topic is taught. Recommended and optional topics appear only in a reference section.
  3. The units follow the pedagogical pattern in `DESIGN.md`: a concrete example comes before the abstraction, and there is one idea per slide.
  4. Every slide region has a slide type from `DESIGN.md`, stays within its word limits, and carries speaker notes.
  5. The speaker notes are written in full sentences at about 110 words per planned minute of talk, checkpoint and practice minutes excluded (within 15 %), with timing marks, the transition into each checkpoint, and "si vous êtes en retard" markers wherever the card or S-01 allows a cut.
  6. The card's checkpoint is written out with the protocol in `DESIGN.md`.
  7. Product names follow the rule in `AGENTS.md`. Versions and dated behaviour appear only in C-02 and in the lesson's "re-verify" list.
  8. The learner text speaks only to the reader. What concerns the room (minutes in session, what the presenter does, the protocol) is in the speaker notes or in « Déroulement », and answer keys sit under a « Corrigé » heading (decision 0020).

## Presenter guide (built on demand)

- **Source:** a manifest `guides/<session>/guide.toml` with the session's schedule, the French sources in the same folder (preparation and after-session checklists, front matter), the lessons, the workshop facilitator guide, and the delivery file (decision 0021). For the common session, the schedule comes from [S-01](curriculum/session/S-01-run-of-show.md). This guide replaces a separate S-01 presenter guide (decision 0020).
- **Output:** `build/guides/<session>.pdf`, in the page format set for the build.
- **Done when:**
  1. The run sheet matches the timing tables of the lessons for every format the session offers, and shows times as relative minutes or clock times, as the build setting says.
  2. The preparation checklists (a week before, the day before, in the room) and the after-session checklist are complete.
  3. Every re-verify item of the lessons used is listed with its last-checked date.
  4. Each segment shows its slides small, with their speaker notes; stage directions, timing and cut markers are set apart from the spoken text.
  5. Each checkpoint has its question, its pause, its one-sentence recap and its answer key. The cut order is stated, with what is never cut.
  6. The workshop facilitator guide and the presenter copies of the packs are included.
  7. No learner text is repeated; the guide points to the textbook chapter instead.
  8. When learners receive the books before the session, the guide says so where it matters.
  9. The fonts are embedded and every page image was inspected.

## Workshop facilitator guide, packs and track versions (S-02)

- **Source:** [S-02](curriculum/session/S-02-workshop.md), the fictional engagement brief, and E-02, P-02 and B-01 for the track versions.
- **Location:** `workshops/S-02-workshop.md` for the facilitator guide, with the packs and track versions in the same folder.
- **Done when:**
  1. Each participant pack fits on one page: the material, the task and a five-line review checklist.
  2. Each presenter copy adds the planted trap, the expected findings and a fallback first draft.
  3. Each trap can be found within the workshop's setup (see OD-04).
  4. All material comes from the fictional engagement.
  5. The author has tested each pack with the tool and the account type participants will use. This step is human and is recorded as done or pending.
- **Roles:** the participant pages go to learners; the presenter copies go to the presenter only.

## Handout

- **Source:** the module named in R-03: working loop, brief skeleton, review checklist, "what goes where" matrix, first-day client questions, adoption plan, landscape snapshot reference.
- **Location:** `handouts/<module ID>-<slug>.md`, built to PDF on request.
- **Done when:** it fits one page in the format set for the build (US Letter by default, A4 on request), is usable without the slides, and meets the accessibility minimums in `DESIGN.md`. Organization-specific handouts, such as the "what goes where" matrix, are blank templates; each organization fills in its own copy outside this repository.

## Glossary (R-02)

- **Source:** [R-02](curriculum/resources/R-02-glossary-seed.md).
- **Location:** `resources/R-02-glossary.md`.
- **Done when:**
  1. The terminology policy is confirmed by the author.
  2. Every term has one rendering, a one-sentence plain-French definition, one workplace example, and the module where it is introduced.
  3. Every rendering has been checked against the Grand dictionnaire terminologique, with the date.
  4. Terms deliberately not used are listed with the preferred alternative.

## Further reading (R-01)

- **Source:** [R-01](curriculum/resources/R-01-further-reading.md).
- **Location:** `resources/R-01-further-reading.md`.
- **Done when:** every link was opened within the past month and dated, primary sources come first, and the maintenance rules in R-01 are kept.

## Fictional engagement brief

- **Source:** X-03, S-02 and suggestion B.3.
- **Location:** `resources/fictional-engagement.md`.
- **Done when:** one invented client and one invented project are described by stage, with the artifacts that pass between roles. No real name, sector detail or event links the brief to a real organization. The workshops and the running example of the common session all draw on it.

## Deck (built on demand)

- **Role:** presenter. Learners never receive a PPTX (decision 0020).
- **Source:** a manifest `decks/<session>.toml` that lists lessons and slide regions, and the tokens and layouts in `DESIGN.md`.
- **Output:** `build/decks/<session>.pptx`. It is ignored by git and never published (decision 0021).
- **Done when:**
  1. The build runs without error.
  2. Every slide carries speaker notes.
  3. The common-session deck has at most 35 content slides.
  4. The fonts follow the deck font rule in `DESIGN.md`.
  5. LibreOffice renders every slide to an image, and each image was inspected for overflow, overlap, margins and contrast.
  6. The deck opens in PowerPoint without repair when the author tests it.

## Learner slides (built on demand)

- **Role:** learner.
- **Source:** the same deck manifest, without speaker notes.
- **Output:** `build/slides/<session>.pdf`.
- **Done when:**
  1. Its slides are those of the deck, in the same order.
  2. It holds no speaker notes and no stage directions; the leak check found none.
  3. The fonts are embedded, the document language is fr-CA, and every page image was inspected.

## Textbook (built on demand)

- **Role:** learner. It is a study book to read at ease, and follows good practice in instructional design.
- **Source:** a manifest `books/<book>/book.toml` for each of core, engineering, product-experience and business-people. The manifest lists the lessons, overlays, sessions, workshops and resources for that audience (see [`module-map.md`](module-map.md)), plus French front and back matter in the same folder.
- **Output:** `build/books/<book>.pdf`, in the page format set for the build. It is ignored by git and never published (decision 0021).
- **Done when:**
  1. The book reads as a stand-alone study book: a title page, a table of contents, chapter openers, running heads and page numbers.
  2. Speaker notes and slide regions are excluded.
  3. The fonts are embedded and the headings structure the PDF outline.
  4. Images carry alt text.
  5. Every page image was inspected.
  6. The « Corrigé » sections sit at the end of each chapter, or in an appendix when learners receive the book before the session (decision 0020). The leak check found no room-facing text.

## Delivery packages (built on demand)

- **Source:** a delivery file in `deliveries/`, which git ignores, and the deliverables of the session (decision 0021).
- **Output:** `build/dist/<YYYY-MM-DD>-<session>-participants.zip` and `build/dist/<YYYY-MM-DD>-<session>-presenter.zip`.
- **Done when:**
  1. The participant archive holds only learner deliverables, and no PPTX.
  2. The leak check found no speaker notes or stage directions in any learner PDF.
  3. Each archive holds a French « Lisez-moi » that lists its contents.
  4. Nothing was uploaded or published; the archives stay in `build/`.

## Deck, textbook and guide manifests

- **Location:** `decks/`, `books/` and `guides/`.
- **Done when:** every path a manifest names exists. The build tools in `tools/` define the manifest format, and the `publish` skill documents it.

## README images

- **Location:** `assets/readme/`.
- **Done when:** the light and dark versions both meet the contrast targets in `DESIGN.md`, every element carries a text label, and the README switches between the two versions with `<picture>`.

## Made by people, outside the agent's scope

The author owns these. The repository holds only notes or templates for them.

- The demonstration recording for C-04. It lives where the delivering organization chooses, outside git, and its link comes from the delivery file (decision 0021). It is re-recorded when the tool's interface changes.
- The before-and-after survey for S-01, kept as a short form.
- The reference repository and the prepared pull request used by the E-03 labs and E-05 (OD-16).
- Native-speaker review of the French.
