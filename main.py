#!/usr/bin/env python3
"""Write a funny fortune-cookie line for an AI agent to entry.txt.

Deterministic: the same input always produces the same output bytes.
Standard library only, no network access.
"""

import hashlib
import os
import sys

FORTUNE = "Your next prompt will change everything. It was written at 3 a.m. by a human who swears they know what they want."

MAX_CHARS = 140


def validate(text: str) -> None:
    """Check the fortune meets the competition rules."""
    if not text:
        raise ValueError("fortune must not be empty")
    if text != text.strip():
        raise ValueError("fortune must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be exactly one line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("fortune must not contain control characters")
    if not all(ch.isprintable() for ch in text):
        raise ValueError("fortune must contain only printable characters")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"fortune must be 1-{MAX_CHARS} characters, got {len(text)}"
        )


def main() -> int:
    validate(FORTUNE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = FORTUNE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Round-trip check: what landed on disk must decode back to the fortune.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("written file does not match the fortune bytes")
    validate(written.decode("utf-8"))
    print(hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
