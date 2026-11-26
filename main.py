#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse -- make.fun entry.

Writes one line (at most 120 characters) in which a robot vacuum explains
why it missed a spot, to /output/entry.txt.

The excuse, in the vacuum's own voice: a machine that circled the crumb,
did the maths, and made peace with the failure.
"""

import os
import sys

ENTRY = "I circled that crumb three times, ran the numbers, and concluded it was load-bearing."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def validate(text: str) -> str:
    """Return the entry text, or raise if it cannot pass the gate."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry is empty or only whitespace")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(f"entry is {len(cleaned)} chars, over the 120-char cap")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    return cleaned


def main() -> int:
    try:
        text = validate(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
