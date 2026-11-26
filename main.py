#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry (v1).

Writes a single painfully honest but still polite out-of-office auto-reply
of at most 200 characters to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output), validating the gate (1-200 chars, not only whitespace, single
line) before writing. Stdlib only.

v1 line (tournament champion, round 1): the last email answered properly
was the one that got me this job.
"""

import os
import sys

ENTRY = (
    "I am out of office until Monday, and honestly the last email I "
    "answered properly was the one that got me this job, so thank you "
    "for your patience while I find that person again."
)


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: entry is {len(line)} chars, over the 200-char gate",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
