# Skills register

One row per project skill in `.claude/skills/`.

| Skill | Purpose | Source | Version or commit | Licence | Owner | Reviewed |
|---|---|---|---|---|---|---|

The rows are added in initialization, Phase 3, together with:

- the hashes of the third-party files, checked after installation;
- the matching entries in `THIRD_PARTY_NOTICES.md`.

## Rules

- **Source:** "written here" for skills authored in this repository. Otherwise, the upstream repository and path.
- **Version or commit:** the full commit hash of the pinned copy. Third-party skills are copies pinned to a commit, never self-updating plugins.
- **Owner:** the role that keeps the skill current. It is the author unless stated otherwise.
- **Reviewed:** the date someone last read the whole skill, scripts included.
- **When something changes:** after initialization, adding, updating or removing a skill needs the author's approval, because `.claude/` is locked. Each such change updates this file and the notices in the same step.
