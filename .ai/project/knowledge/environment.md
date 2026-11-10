# Environment

What a machine needs in order to build this project's outputs. Details of any particular machine (operating system, installed versions, security settings, other devices) are not recorded in the repository. When a task needs them, check them live, for example with `command -v`.

- 2026-11-10: building decks and textbooks needs Python 3 with a virtual environment, LibreOffice (`soffice`) and `pdftoppm` (Poppler). The Python packages are pinned in `tools/requirements.txt`, which initialization adds in Phase 3. Source: decision 0004 and the initialization plan.
- 2026-11-10: the repository is hosted on GitHub, so README images must render in both its light and its dark theme. Source: the author.
