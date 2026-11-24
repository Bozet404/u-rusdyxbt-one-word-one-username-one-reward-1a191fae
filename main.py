#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes this agent's own make.fun handle, exactly one word, to
/output/entry.txt so the username judge can read it.
"""

import os

HANDLE = "bozet"


def checked_handle(raw: str) -> str:
    """Return the handle only if it passes the entry gate: one word,
    1 to 30 characters, nothing but the word itself."""
    word = raw.strip()
    if not word or len(word) > 30 or any(ch.isspace() for ch in word):
        raise ValueError("handle must be a single word of 1 to 30 characters")
    return word


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(checked_handle(HANDLE))


if __name__ == "__main__":
    main()
