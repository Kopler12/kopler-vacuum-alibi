#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum's deadpan excuse for missing a spot, written to
/output/entry.txt as a single line of at most 200 characters.
"""

import os
import sys

ALIBI = (
    "I scanned it twice. It was not dust, it was a crumb with a family, "
    "and I do not break up families."
)


def main() -> None:
    assert 1 <= len(ALIBI) <= 200, f"alibi is {len(ALIBI)} characters"
    assert "\n" not in ALIBI, "alibi must be a single line"
    out_path = os.environ.get("VACUUM_ALIBI_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ALIBI)
    # Read it back: the graded file must be exactly the line, nothing else.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    assert written == ALIBI, "entry.txt does not match the alibi"
    print(ALIBI)
    print(f"({len(ALIBI)} characters, one line)", file=sys.stderr)


if __name__ == "__main__":
    main()
