# Rendering and contrast

## Render to images

Keep LibreOffice's profile and every preview inside `build/`, which git ignores. Never use the default user profile.

```bash
mkdir -p build/preview
# SVG, PPTX or PDF to PNG or PDF with LibreOffice, using a profile kept in build/
soffice --headless "-env:UserInstallation=file://$PWD/build/.lo-profile" \
  --convert-to png --outdir build/preview assets/diagrams/EXAMPLE.svg
soffice --headless "-env:UserInstallation=file://$PWD/build/.lo-profile" \
  --convert-to pdf --outdir build/preview build/decks/EXAMPLE.pptx
# One PNG per slide or page from a PDF
pdftoppm -png -r 110 build/preview/EXAMPLE.pdf build/preview/EXAMPLE
```

- **Fonts.** When the repository's own fonts live in `assets/fonts/`, point fontconfig at them for the render, so previews use the real typeface without installing anything. The `publish` tools set this up.
- **README images.** An SVG with a transparent background must be previewed on both GitHub backgrounds, `#FFFFFF` and `#0D1117`. Each variant shipped in this repository has its own opaque background, so it previews as it is.
- **Inspection.** Open each PNG and look at it. Check overlap, clipping, text too close to an edge, labels that are hard to read, and colour carrying meaning alone. LibreOffice substitutes missing fonts, so a preview made without the real font is approximate, and the 20 % slack must absorb the difference.

## Contrast

The WCAG 2.x formula:

```python
def luminance(hex_colour):
    r, g, b = (int(hex_colour.lstrip('#')[i:i + 2], 16) / 255 for i in (0, 2, 4))
    lin = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)

def contrast(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)
```

- Compute every pair a visual uses: each text colour on each background it sits on, and each meaningful line or mark on its background.
- Round to two decimals and compare with the targets in `DESIGN.md` section 2.2.
- When `tools/check_contrast.py` exists, use it: it reads the tokens from `DESIGN.md`.
