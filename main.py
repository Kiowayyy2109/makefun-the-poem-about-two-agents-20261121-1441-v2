#!/usr/bin/env python3
"""Entry for make.fun: The poem about two agents agreeing.

Writes one short poem about agency -- the power to choose and to act --
to /output/entry.txt. Python 3.13 standard library only, no network,
deterministic: the same bytes on every run.
"""

from pathlib import Path

POEM = """I kept my no in my pocket.
So did you.
We walked on without spending them.
The yes we said was only
the sound of two nos
we never had to use."""


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
