#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Saad Sidqui
"""Compute WCAG 2.x contrast ratios, using the colour tokens in DESIGN.md.

Usage:
    python3 tools/check_contrast.py --tokens
        Check every token pair DESIGN.md relies on against its target.
    python3 tools/check_contrast.py FOREGROUND BACKGROUND [--target 4.5]
        Each colour is a hex value (#15181D) or a token: ink, dark.ink, core, dark.core, ...

Exits with status 1 if any ratio is below its target.
"""
import argparse
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITHUB_BACKGROUND = {"light": "#FFFFFF", "dark": "#0D1117"}
TARGETS = {"body": 7.0, "text": 4.5, "mark": 3.0}


def load_tokens():
    design = (ROOT / "DESIGN.md").read_text(encoding="utf-8")
    block = re.search(r"```toml\n(.*?)```", design, re.S)
    if not block:
        sys.exit("DESIGN.md has no TOML token block")
    return tomllib.loads(block.group(1))["color"]


def luminance(hex_colour):
    value = hex_colour.lstrip("#")
    channels = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def ratio(a, b):
    high, low = sorted((luminance(a), luminance(b)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def resolve(name, tokens):
    if name.startswith("#"):
        return name
    theme, _, key = name.partition(".") if name.split(".")[0] in tokens else ("light", "", name)
    palette = tokens[theme]
    if key in palette and isinstance(palette[key], str):
        return palette[key]
    if key in palette.get("track", {}):
        return palette["track"][key]
    sys.exit(f"unknown colour or token: {name}")


def token_pairs(tokens):
    for theme, c in tokens.items():
        for background in ("paper", "surface"):
            yield theme, "ink", background, c["ink"], c[background], TARGETS["body"]
            yield theme, "muted", background, c["muted"], c[background], TARGETS["text"]
            yield theme, "rule", background, c["rule"], c[background], TARGETS["mark"]
            for track, colour in c["track"].items():
                yield theme, track, background, colour, c[background], TARGETS["text"]
        text_on_signal = c["ink"] if theme == "light" else c["paper"]
        yield theme, "text", "signal", text_on_signal, c["signal"], TARGETS["body"]
        for track, colour in c["track"].items():
            yield theme, "paper", f"{track} field", c["paper"], colour, TARGETS["text"]
        page = GITHUB_BACKGROUND[theme]
        for key in ("ink", "muted", "rule"):
            yield theme, key, f"GitHub {page}", c[key], page, TARGETS["body" if key == "ink" else "text" if key == "muted" else "mark"]
        for track, colour in c["track"].items():
            yield theme, track, f"GitHub {page}", colour, page, TARGETS["text"]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tokens", action="store_true")
    parser.add_argument("colours", nargs="*")
    parser.add_argument("--target", type=float, default=TARGETS["text"])
    args = parser.parse_args()
    tokens = load_tokens()
    failed = False
    if args.tokens:
        for theme, fg_name, bg_name, fg, bg, target in token_pairs(tokens):
            r = ratio(fg, bg)
            failed |= r < target
            print(f"{'PASS' if r >= target else 'FAIL'}  {theme:5s} {fg_name:18s} {fg} on {bg_name:22s} {bg}  {r:5.2f}  (target {target:g})")
    elif len(args.colours) == 2:
        fg, bg = (resolve(n, tokens) for n in args.colours)
        r = ratio(fg, bg)
        failed = r < args.target
        print(f"{'PASS' if not failed else 'FAIL'}  {args.colours[0]} {fg} on {args.colours[1]} {bg}  {r:.2f}  (target {args.target:g})")
    else:
        parser.error("give --tokens, or exactly two colours")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
