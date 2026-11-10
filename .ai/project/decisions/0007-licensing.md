# 0007. Licensing

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

The repository is licensed under CC BY 4.0. Creative Commons licences are not designed for software, and the build tooling adds scripts.

## Decision

1. **Default:** the repository is licensed under CC BY 4.0. `LICENSE` holds the official legal code.
2. **Scripts:** scripts are licensed under MIT. Each one carries `SPDX-License-Identifier: MIT`, and the MIT text is in `LICENSES/MIT.txt`.
3. **Third-party material:** it keeps its own stated licence and is listed in `THIRD_PARTY_NOTICES.md` with its source and version.

## Consequences

- The README's licence section states all three.
- A file copied from elsewhere is added only when its licence allows redistribution. If its licence or origin is unclear, the agent stops and asks.
