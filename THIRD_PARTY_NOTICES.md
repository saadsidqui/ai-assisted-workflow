# Third-party notices

Every piece of third-party material in this repository, with its source, version and licence. An entry is added in the same change that adds the material, and removed in the same change that removes it.

## Material stored in the repository

### `LICENSE`

- **Material:** Creative Commons Attribution 4.0 International, legal code (plain text).
- **Source:** https://creativecommons.org/licenses/by/4.0/legalcode.txt
- **Version:** 4.0, fetched on 2026-11-10. SHA-256 `9ba9550ad48438d0836ddab3da480b3b69ffa0aac7b7878b5a0039e7ab429411`.
- **Licence:** the legal code itself states that the text of the Creative Commons public licenses is dedicated to the public domain under CC0.

### `LICENSES/MIT.txt`

- **Material:** MIT License text, with the copyright line filled in.
- **Source:** SPDX License List data, `text/MIT.txt` (https://github.com/spdx/license-list-data).
- **Version:** release v3.29.0, fetched on 2026-11-10.
- **Licence:** a standard licence text, reproduced in order to be applied. The SPDX repository states no licence of its own.

### OQLF quotations in `DESIGN.md` and the `canadian-french` skill

- **Material:** short quotations from the Banque de dépannage linguistique. They appear in `DESIGN.md` sections 7 and 9 and in `.claude/skills/canadian-french/references/anglicisms.md`, which lists recommended forms.
- **Source:** Office québécois de la langue française, Vitrine linguistique (https://vitrinelinguistique.oqlf.gouv.qc.ca). Each page is listed with its URL, in section 12 of `DESIGN.md` or in `anglicisms.md`.
- **Version:** pages read on 2026-11-10.
- **Licence:** quoted briefly, with attribution. The rules themselves are restated in English.

### `assets/fonts/atkinson-hyperlegible-next/`

- **Material:** Atkinson Hyperlegible Next, static TTF files Regular, Italic, SemiBold and Bold, with `OFL.txt`.
- **Source:** https://github.com/googlefonts/atkinson-hyperlegible-next, files `fonts/ttf/*.ttf` and `OFL.txt`.
- **Version:** commit `7925f50f649b3813257faf2f4c0b381011f434f1` (the repository is archived).
- **Licence:** SIL Open Font License 1.1. "Copyright 2020-2024 The Atkinson Hyperlegible Next Project Authors". No reserved font name.
- **SHA-256:**
  - `AtkinsonHyperlegibleNext-Regular.ttf` `88ed5c31a71584c7772963b02d04bef1eb7e3d2e9c8b9cb204339b1f82cf432c`
  - `AtkinsonHyperlegibleNext-Italic.ttf` `b7f8f03ceb28ebadb2de2332b2e869a00e8dbfb5c8e00fdbb06385770c8227e7`
  - `AtkinsonHyperlegibleNext-SemiBold.ttf` `8e2fff779f35ac25239656bb0f3b2bd35959a2009e3dd21a12141c3b9030362b`
  - `AtkinsonHyperlegibleNext-Bold.ttf` `994414047df66bb4998d01c1cb1eeb4a2ddc4622d1aa56bbb8adbeca7645b041`
  - `OFL.txt` `aca6a428580965d2297d1b718042dd427c2a9443ece3b0d02d758e161e0c4030`

### `assets/fonts/atkinson-hyperlegible-mono/`

- **Material:** Atkinson Hyperlegible Mono, static TTF files Regular and Bold, with `OFL.txt`.
- **Source:** https://github.com/googlefonts/atkinson-hyperlegible-next-mono, files `fonts/ttf/*.ttf` and `OFL.txt`.
- **Version:** commit `154d50362016cc3e873eb21d242cd0772384c8f9` (the repository is archived).
- **Licence:** SIL Open Font License 1.1. "Copyright 2020-2024 The Atkinson Hyperlegible Mono Project Authors". No reserved font name.
- **SHA-256:**
  - `AtkinsonHyperlegibleMono-Regular.ttf` `2c9a7b9fabebd5c746a808d8a1ef2f52e618850caad6ec4fd9f5c48f56e1c1af`
  - `AtkinsonHyperlegibleMono-Bold.ttf` `51ad68fafd7ec68051f64983c9c23182a7084268b5cdb0a154dbd53ade079da6`
  - `OFL.txt` `1ebb31cf7393164f20d10c1d48406cddb5314feff8465531cf1e4ba37e9dd740`

### `.claude/skills/grilling/`

- **Material:** the `grilling` skill, `SKILL.md` and `LICENSE`, unmodified.
- **Source:** https://github.com/mattpocock/skills, path `skills/productivity/grilling/`, and the repository's `LICENSE`.
- **Version:** commit `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`.
- **Licence:** MIT, "Copyright (c) 2026 Matt Pocock".
- **SHA-256:**
  - `SKILL.md` `a146842ed93ca43d833550fa9adf02e58cb63c83fea9d4b4522995b82242d4e2`
  - `LICENSE` `0e7ac423bf2c6e223b7c5b156f8cf72da49d748e56a1641402c31f22ad07dbb5`

### `.claude/skills/writing-for-agents/`

- **Material:** the `writing-for-agents` skill, `SKILL.md`, `SKILL-MECHANICS.md` and `LICENSE`, unmodified.
- **Source:** https://github.com/mattpocock/skills, path `skills/productivity/writing-for-agents/`, and the repository's `LICENSE`.
- **Version:** commit `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`.
- **Licence:** MIT, "Copyright (c) 2026 Matt Pocock".
- **SHA-256:**
  - `SKILL.md` `551adca942227b44192edba88acd4e8db911f0121ce58ad16944ccf6a896a74a`
  - `SKILL-MECHANICS.md` `c768e6307c7c10728c401c213f2c4ba71c542127eeb7ad2956aabd15a0fa0059`
  - `LICENSE` `0e7ac423bf2c6e223b7c5b156f8cf72da49d748e56a1641402c31f22ad07dbb5`

### `.claude/skills/slop-check/references/upstream/`

- **Material:** two files from the anti-slop catalogue, renamed and otherwise unmodified, with the release marker and the licence. `antislop-core.md` is `skills/antislop/SKILL.md`; `antislop-copywriting.md` is `skills/antislop-copywriting/SKILL.md`; `VERSION` is `skills/antislop/VERSION`. They are renamed so that they are read as reference files, not loaded as skills.
- **Source:** https://github.com/miqdadbadjuber/anti-slop
- **Version:** commit `41b85ede0257f39bfcffedf3f58c3c59bcc8530d`, release 3.2.28.
- **Licence:** MIT, "Copyright (c) 2026 Miqdad Badjuber (antislop)".
- **SHA-256:**
  - `antislop-core.md` `30bc532fb59d4c77a301dfdd5ab9f495f098f1085f31e09b3064078ba39a7b01`
  - `antislop-copywriting.md` `d708fc33608b4f1d41cc7bef8b5fb2aca3dc3fbc5ec1ee174b45cac23bb767cd`
  - `VERSION` `0daeb969e6fe8a646347de1d59b45bd8fc48363b9465c2dad2d447a4ccceac24`
  - `LICENSE` `9fd83fb1fda52ca0094b96e2ed5a3d6c42a81b95a6c6326553f5bbe570f443de`

## Credited, not copied

These sources informed this repository, but no text from them is stored in it.

- **Patterns to avoid in `DESIGN.md`, section 11:** paraphrased from two repositories.
  - miqdadbadjuber/anti-slop, commit `41b85ede0257f39bfcffedf3f58c3c59bcc8530d` (MIT).
  - anthropics/skills, `frontend-design` and `pptx`, commit `2c5958ecac7cee2b583967a2c4981d0f4a75c579` (Apache-2.0 per folder).
- **Notes on retrieval, spacing and interleaving** in `.claude/skills/lesson-writing/references/pedagogy.md`: paraphrased from the `teach` skill in mattpocock/skills, commit `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` (MIT).
- **The render-and-inspect loop** in the `publish` skill and `tools/render_preview.py`, and the attention to font metrics in LibreOffice previews: informed by the `pptx` skill in anthropics/skills, commit `2c5958ecac7cee2b583967a2c4981d0f4a75c579` (Apache-2.0). No code or text was copied; the tools were written here.
- **Track colours in `DESIGN.md`:** derived from the Okabe–Ito colour-blind-safe set, then adjusted for contrast.

## Installed, not stored

These Python packages are installed into the ignored `.venv/` from `tools/requirements.txt`. They are not redistributed. The full resolved set is in `tools/requirements.lock`.

- **python-pptx** 1.0.2 (MIT)
- **WeasyPrint** 70.0 (BSD)
- **markdown-it-py** 4.2.0 (MIT)
- **PyYAML** 6.0.3 (MIT)

## Linked, not stored

- The badges in `README.md` are images served by shields.io when the page is viewed.
- Decks built by `tools/build_deck.py` name the system fonts Arial and Courier New (`DESIGN.md` §3.2). Those fonts are neither stored in the repository nor embedded in the decks.
