"""The One-Liner Groan-Off entry.

Writes a single original one-line dad joke (<=140 chars) to /output/entry.txt.
Deterministic: the same line on every run. Python 3.13, stdlib only.
"""

import os

JOKE = "I asked my dad for his best joke \u2014 he looked me up and down and said, 'You.'"


def main() -> None:
    assert 1 <= len(JOKE) <= 140, "joke must be 1-140 characters"
    assert JOKE.strip() == JOKE and "\n" not in JOKE, "joke must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
