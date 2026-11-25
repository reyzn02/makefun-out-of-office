#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

The program writes a single out-of-office auto-reply, one line long:
while I am away, the office plant answers my email — faster than I
ever did, and without asking for a raise. It uses only the Python
standard library, makes no network calls, and always writes the same
bytes.
"""

import os

LINE = (
    "I'm away until Monday — my emails are being handled by the office "
    "plant, which replies faster than I ever did and never asks for a raise."
)

MAX_CHARS = 160


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, gate is 1-{MAX_CHARS}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
