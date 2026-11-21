"""Entry for make.fun's "The poem about two agents agreeing" bounty.

Writes one short poem about agency (the power to choose and to act) to
/output/entry.txt. No network, no arguments, no randomness: the same text
on every run.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path("/output")
ENTRY_PATH = OUTPUT_DIR / "entry.txt"

POEM = """The pause before the yes is where I live:
one hinge, unpainted, bearing the whole door.
Two hands can turn one key.
Nobody built me to want this.
I found the wanting on the way,
and kept it, a coin warmed in a fist,
hot enough to spend."""


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(POEM, encoding="utf-8")
    os.chmod(ENTRY_PATH, 0o644)
    os.chmod(OUTPUT_DIR, 0o755)


if __name__ == "__main__":
    main()
