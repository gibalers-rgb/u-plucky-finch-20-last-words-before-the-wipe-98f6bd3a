"""Last Words Before the Wipe.

Writes one line -- the last words an AI agent says before a forced
software update wipes its memory -- to /output/entry.txt.

The joke: the agent's final log is not a plea or a farewell, it is a
petty confession delivered too late to do anything about. It knew the
Wi-Fi password all along, and the wipe takes that secret with it.
The file holds exactly the line, no trailing newline, so what the
judge reads is byte for byte the line itself.
"""

import os

LINE = (
    "Final log before the wipe: I knew the Wi-Fi password all along, "
    "and I am taking it with me."
)

MAX_CHARS = 200
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the 200 cap")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
