# 0004. Build toolchain and compatibility target

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

Decks and PDF textbooks are generated on demand from Markdown lessons. The toolchain should rely on widely available tools, keep installs few and pinned, and run the same on any machine that builds the project.

## Decision

1. **Environment:** a Python virtual environment in an ignored `.venv/`, with dependencies pinned in `tools/requirements.txt`.
2. **Decks:** python-pptx builds editable decks with speaker notes.
3. **Textbooks:** WeasyPrint builds the PDFs from Markdown rendered to HTML.
4. **Previews:** LibreOffice renders decks and pages to images for visual review.
5. **Compatibility:** decks must work in LibreOffice, the main target, and in PowerPoint. The author can test in PowerPoint on request.
6. **Installation:** the author installs every dependency.

## Consequences

- python-pptx cannot embed fonts, so the deck font rule in `DESIGN.md` depends on a test made during initialization, Phase 3.
- Build scripts live in `tools/` under the MIT licence (decision 0007).
- Pandoc with Typst, Anthropic's document skills, and a Node toolchain were considered and not chosen.
