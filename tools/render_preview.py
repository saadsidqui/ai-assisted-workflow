#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Saad Sidqui
"""Render SVG, PPTX, ODP and PDF files to PNG images for visual review.

Usage:
    python3 tools/render_preview.py FILE [...] [--dpi 110] [--out build/preview]

- SVG becomes one PNG.
- PPTX and ODP become a PDF, then one PNG per slide.
- PDF becomes one PNG per page.

LibreOffice runs headless with its own profile in build/.lo-profile. A fontconfig file in
build/fontconfig adds assets/fonts to the system fonts, so previews use the repository's
typefaces without installing anything. All output stays in build/, which git ignores.
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"


def font_environment():
    conf_dir = BUILD / "fontconfig"
    (conf_dir / "cache").mkdir(parents=True, exist_ok=True)
    conf = conf_dir / "fonts.conf"
    conf.write_text(
        '<?xml version="1.0"?>\n<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n<fontconfig>\n'
        '  <include ignore_missing="yes">/etc/fonts/fonts.conf</include>\n'
        f"  <dir>{ROOT / 'assets' / 'fonts'}</dir>\n"
        f"  <cachedir>{conf_dir / 'cache'}</cachedir>\n"
        "</fontconfig>\n",
        encoding="utf-8",
    )
    env = dict(os.environ)
    env["FONTCONFIG_FILE"] = str(conf)
    return env


def soffice(source, fmt, outdir, env):
    profile = (BUILD / ".lo-profile").resolve().as_uri()
    subprocess.run(["soffice", "--headless", f"-env:UserInstallation={profile}",
                    "--convert-to", fmt, "--outdir", str(outdir), str(source)],
                   check=True, env=env, timeout=600, stdout=subprocess.DEVNULL)
    return outdir / f"{source.stem}.{fmt}"


def pdf_pages(pdf, outdir, dpi, env):
    prefix = outdir / pdf.stem
    for old in outdir.glob(f"{pdf.stem}-*.png"):
        old.unlink()
    subprocess.run(["pdftoppm", "-png", "-r", str(dpi), str(pdf), str(prefix)], check=True, env=env, timeout=600)
    return sorted(outdir.glob(f"{pdf.stem}-*.png"))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--dpi", type=int, default=110)
    parser.add_argument("--out", type=Path, default=BUILD / "preview")
    args = parser.parse_args()
    for tool in ("soffice", "pdftoppm"):
        if not shutil.which(tool):
            sys.exit(f"{tool} not found: LibreOffice and Poppler are required (see tools/README.md)")
    env = font_environment()
    args.out.mkdir(parents=True, exist_ok=True)
    for source in args.files:
        source = source.resolve()
        suffix = source.suffix.lower()
        if suffix == ".svg":
            images = [soffice(source, "png", args.out, env)]
        elif suffix in (".pptx", ".odp"):
            images = pdf_pages(soffice(source, "pdf", args.out, env), args.out, args.dpi, env)
        elif suffix == ".pdf":
            images = pdf_pages(source, args.out, args.dpi, env)
        else:
            sys.exit(f"unsupported file type: {source.name}")
        for image in images:
            print(image)


if __name__ == "__main__":
    main()
