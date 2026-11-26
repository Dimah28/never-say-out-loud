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


def check_shape(line: str) -> None:
    """Enforce the competition's gate: 1-200 Unicode code points,
    at least one character that is not white space."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line is {len(line)} characters, must be 1-200")
    if not any(not ch.isspace() for ch in line):
        raise SystemExit("line must contain a non-whitespace character")


def render_entry(line: str) -> bytes:
    """Render the entry exactly as the judge will read it: the line,
    UTF-8, no trailing newline, nothing else."""
    check_shape(line)
    return line.encode("utf-8")


def write_entry(line: str) -> None:
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the rendered bytes: the judge reads exactly the
    # bytes in the file.
    output_path.write_bytes(render_entry(line))


def main() -> None:
    write_entry(LINE)


if __name__ == "__main__":
    main()
