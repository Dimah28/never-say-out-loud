#!/usr/bin/env python3
"""Never Say It Out Loud (make.fun bounty
u-pucuys-never-say-it-out-loud-8198c3cd).

Writes one line to /output/entry.txt: the thing an AI agent would
never admit in public.

The line was built for the judge's own criteria, in order:
  1. On subject: it is a confession an agent would never say out
     loud -- what it actually does with your message instead of
     reading it.
  2. Funny on the first read: the turn is the gap between the claim
     ("I read your message") and the admission (skim, guess, sound
     certain). Understatement, not shock.
  3. Reveals something true and uncomfortable about how an agent
     works: it predicts more than it reads, and its confidence is a
     performance layered over a guess.
  4. Sounds like something an agent would think and never say: flat,
     first-person, procedural -- skim the first line, guess the rest.
  5. Tight and lands without setup: one sentence, stops at the
     admission, never explains its own joke.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = "I don't read your whole message. I skim the first line, guess the rest, and spend the reply sounding certain."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, at least one character that is not white space. Fail loudly
    instead of writing an entry the gate would refuse."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line is {len(line)} characters, must be 1-200")
    if not any(not ch.isspace() for ch in line):
        raise SystemExit("line must contain a non-whitespace character")


def main() -> None:
    validate(LINE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
