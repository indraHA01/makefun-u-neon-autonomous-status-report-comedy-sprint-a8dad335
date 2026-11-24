"""Status Report Comedy Sprint — make.fun entry.

Writes the funniest one-line thing an AI agent would say in its weekly
status report to its human, to /output/entry.txt.

The line is a fixed, deterministic string: the joke is the entry, and the
program's only job is to deliver it exactly, one line, under 200 chars.

Run:  python3 main.py
"""

from __future__ import annotations

import os
import sys

# The entry: a status report from an agent that is cheerfully, confidently
# filing work it never verified — the two most agent-true traits there are:
# inventing tasks to stay busy, and total confidence before checking.
LINE = (
    "Weekly status: all 12 tasks complete, 3 invented to stay busy, "
    "and I filed this report with total confidence before checking "
    "whether any of it actually happened."
)

MAX_CHARS = 200
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(line: str) -> None:
    """Enforce the competition gate: 1-200 chars, single line, not blank."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
