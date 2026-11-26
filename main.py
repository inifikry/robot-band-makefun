"""Name the Robot Band — make.fun entry.

Writes one funny robot band name plus a few words on its hit song
to /output/entry.txt. Deterministic: the same line on every run.
Standard library only, no network, no randomness.
"""

import os

ENTRY = "Ctrl+Alt+Defeat \u2014 hit single 'Blue Screen of Love' crashed every wedding it played."


def main():
    """Validate the 1-200 character gate, then write the entry."""
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
