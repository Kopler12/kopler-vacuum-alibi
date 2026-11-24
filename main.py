#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum's deadpan excuse for missing a spot, written to
/output/entry.txt as a single line of at most 200 characters.
"""

import os

ALIBI = (
    "I scanned it twice. It was not dust, it was a crumb with a family, "
    "and I do not break up families."
)


def main() -> None:
    assert 1 <= len(ALIBI) <= 200, f"alibi is {len(ALIBI)} characters"
    assert "\n" not in ALIBI, "alibi must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ALIBI)
    print(ALIBI)


if __name__ == "__main__":
    main()
