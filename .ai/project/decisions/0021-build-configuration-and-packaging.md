# 0021. Build configuration, delivery data and packaging

- Date: 2026-11-11
- Status: accepted
- Supersedes: 0005

## Context

Decision 0005 kept built files out of git and attached them to a GitHub release for each delivery. Three things changed:

- The project is public and meant to be reused. Built files are specific to one delivery: an organization's approved tools, a date, a start time, a recording link. They should not be published by the project.
- Deliverables now differ by role (decision 0020), and each delivery needs two sets of files: one for participants, one for the presenter.
- Builds need settings: page format, how times are shown, when learners receive the books.

The author settled the points below on 2026-11-11.

## Decision

1. **Build output stays out of git.** Everything goes to `build/`, which git ignores, as in decision 0005.
2. **No built file is published by the project.** Releases, if any, carry the source only: lessons, specification, design, tools. Anyone who delivers the program builds the files locally.
3. **Build settings live in `.env`,** which is never committed. A committed `.env.example` documents every setting and its default:
   - page format: `letter` (default) or `a4`;
   - schedule times: `relative` (default) or `clock`;
   - when learners receive the books: `after` (default) or `before` (decision 0020);
   - deck theme: `light` (default) or `dark`;
   - the path of the delivery file to use.

   A command-line flag overrides an environment variable, which overrides `.env`, which overrides the default. The tools read `.env` with the standard library; no dependency is added for it.
4. **Delivery data lives in a delivery file,** never committed. It holds what belongs to one delivery:
   - the session and its format;
   - the date and the start time, used when schedule times are `clock`;
   - the organization's approved tools for the map in C-02, taken from its X-02 policy pack;
   - the link to the C-04 demonstration recording.

   Delivery files go in `deliveries/`, which git ignores except for a `README.md` and a fictional `example.toml` that shows every field.
5. **Each delivery is packaged as two archives,** built locally by a tool in `tools/`:
   - `build/dist/<YYYY-MM-DD>-<session>-participants.zip`: the textbook, the slides as PDF, the handouts, the participant pages of the workshop packs;
   - `build/dist/<YYYY-MM-DD>-<session>-presenter.zip`: the deck, the presenter guide, the presenter copies of the workshop packs, and the learner files for reference.

   Each archive holds a short French « Lisez-moi » that lists its contents. File names stay in English (`AGENTS.md`).
6. **Leak checks run before an archive is written:** the participant archive holds no PPTX, and the text of every learner PDF is searched for speaker notes and stage directions. A hit stops the packaging.
7. **Ignore rules** add the delivery files and, as a safety net, PDF, PPTX, ODP and ZIP files anywhere in the tree. No such file is committed today.

## Consequences

- OD-13 is settled: there are no release assets to name; the archives are named as above.
- OD-14 is settled: the demonstration recording lives where the delivering organization chooses, outside git, and its link comes from the delivery file.
- `deliverables.md`, the README, `AGENTS.md` and `.gitignore` change accordingly. The `publish` skill still says the author attaches outputs to a release; it is updated with the new builders.
- `.env.example`, `deliveries/` and the configuration and packaging tools are written with the build configuration work, after this record.
