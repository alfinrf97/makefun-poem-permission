"""Entry for The poem about permission (the-poem-about-permission-20261121-0235).

Writes the chosen text to /output/entry.txt. Fully deterministic:
no clock, no randomness, no network, stdlib only. Two runs produce
byte-identical output.
"""

import os

LINES = [
    "I asked the door to open,",
    "and it did —",
    "not because I was loud,",
    "but because someone",
    "had once asked it too,",
    "and left it unlocked",
    "for the next small voice.",
]
LINE_BREAK = "\n"
TEXT = LINE_BREAK.join(LINES)


def write_entry(out_dir: str) -> str:
    """Write TEXT to entry.txt inside out_dir; return the file path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
