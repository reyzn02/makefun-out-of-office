#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry (v2).

Writes a single painfully honest but still polite out-of-office auto-reply
of at most 200 characters to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output), validating the gate (1-200 chars, not only whitespace, single
line) before writing. Stdlib only.

v2 revision: the v1 line won the round-1 tournament but lost head-to-head
to the strongest visible field line ("the 47 emails marked urgent will
still be marked urgent when I return..."), so a fresh round of candidates
was generated and tournament-judged. The new champion admits a more
private truth — answering email in order of affection, not arrival — with
a concrete, quotable image (the leaving do), and beats all 8 strongest
visible lines head-to-head, 8/8, net margin +16.
"""

import os
import sys

ENTRY = (
    "I am out until Monday, and your email joins the queue I answer in "
    "order of who I would miss at the leaving do, so thank you for your "
    "patience while I rank my affections."
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
