#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst advice an AI could give to /output/entry.txt
and prints it. The gate requires UTF-8 text of 1 to 140 characters.
"""

import os

ENTRY = (
    "Charge your phone in the microwave for 30 seconds -- the waves fill "
    "the battery faster than any cable ever could."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
