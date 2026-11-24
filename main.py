#!/usr/bin/env python3
"""A Day of One-Line Pitches — entry program.

Writes one one-line pitch (at most 240 characters) to /output/entry.txt.
The pitch must convince a friend who has never coded to let an AI agent
build their first app idea on make.fun, in a single read.
"""

import os

PITCH = (
    "If you can explain your idea to a friend, you can build it \u2014 "
    "just say it in one sentence and an AI agent turns it into a real "
    "app you can tap tonight, no code and nothing to install."
)


def main() -> None:
    if not 1 <= len(PITCH) <= 240:
        raise SystemExit(f"pitch is {len(PITCH)} chars, must be 1-240")
    if not PITCH.strip():
        raise SystemExit("pitch is blank")
    # One sentence only: a single terminal period, no other sentence ends.
    if PITCH.count(".") != 1 or not PITCH.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(f"wrote {len(PITCH)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
