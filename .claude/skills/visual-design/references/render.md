# Rendering and contrast

## Render to images

Use the repository's renderer:

```bash
python3 tools/render_preview.py assets/diagrams/EXAMPLE.svg build/decks/EXAMPLE.pptx
```

- **What it does:** an SVG becomes one PNG; a PPTX or ODP becomes a PDF and then one PNG per slide; a PDF becomes one PNG per page. Everything lands in `build/preview/`, which git ignores.
- **Fonts and profile:** LibreOffice runs with its own profile in `build/`. A fontconfig file in `build/` adds `assets/fonts/`, so previews use Atkinson Hyperlegible without installing anything.
- **SVG fonts:** LibreOffice's SVG import ignores the CSS `font:` shorthand. Set `font-family`, `font-size` and `font-weight` as attributes on the text elements, or the preview shows a fallback face.
- **README images:** each variant shipped in this repository has its own opaque background, so it previews as it is. An SVG with a transparent background would have to be previewed on both GitHub backgrounds, `#FFFFFF` and `#0D1117`.
- **Inspection:** open each PNG and look at it. Check overlap, clipping, text too close to an edge, labels that are hard to read, and colour carrying meaning alone.

## Contrast

Use the repository's checker. It reads the tokens from the TOML block in `DESIGN.md`:

```bash
python3 tools/check_contrast.py --tokens                 # every token pair DESIGN.md relies on
python3 tools/check_contrast.py ink surface              # two tokens (light theme by default)
python3 tools/check_contrast.py dark.core '#0D1117' --target 3
```

- Check every pair a visual uses: each text colour on each background it sits on, and each meaningful line or mark on its background.
- The targets are in `DESIGN.md` section 2.2: body text 7, other text 4.5, marks 3. The checker exits with status 1 when a pair falls short.
