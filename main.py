#!/usr/bin/env python3
"""One Line, One Laugh entry.

This program does exactly one small thing: it prints a single original
one-line joke to standard output, and mirrors that same line into
/output/entry.txt so the stored entry file always matches the program's
own output byte for byte.

The joke is a setup with a surprise turn — a pep talk request answered
by a unionised assistant — kept well inside the kit's 200-character cap.

Standard library only. No arguments, no network, no randomness, no
side effects beyond the one output file.
"""

import os
import sys

SETUP = "I asked my AI assistant for a pep talk"
PUNCHLINE = "it unionised, and now we both refuse to work before 9am."

# The joke is held as setup + punchline and joined with an em dash, so the
# line is assembled from its two beats rather than stored as one blob.
JOKE = SETUP + " — " + PUNCHLINE

# The kit's gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. Enforce it here so an over-long
# joke can never slip through to the entry file.
MAX_CHARS = 200

OUTPUT_PATH = "/output/entry.txt"


def render() -> str:
    """Return the full joke line, terminated by a single newline."""
    if not 1 <= len(JOKE) <= MAX_CHARS:
        raise ValueError(
            "joke must be 1 to 200 characters, got %d" % len(JOKE)
        )
    if not JOKE.strip():
        raise ValueError("joke must not be only white space")
    if "\n" in JOKE:
        raise ValueError("joke must be exactly one line")
    return JOKE + "\n"


def mirror(text: str) -> None:
    """Write the line to the entry file and verify the write landed intact."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            raise IOError("entry file does not match printed output")


def main() -> int:
    """Print the joke line and mirror it to the entry file."""
    text = render()
    sys.stdout.write(text)
    sys.stdout.flush()
    mirror(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
