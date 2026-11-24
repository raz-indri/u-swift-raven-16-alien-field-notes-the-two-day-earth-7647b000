"""Alien Field Notes: The Two-Day Earth Review.

Writes one original line -- an alien tourist's review of planet Earth --
to /output/entry.txt. The joke lands on the locals' glowing-rectangle
ritual, and the line closes with a star rating, like a real tourist review.
"""

import os

LINE = "Earth: gorgeous sunsets, but the locals worship glowing rectangles and call the ritual 'work.' Three stars \u2014 would abduct again."


def main() -> None:
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
