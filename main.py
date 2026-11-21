#!/usr/bin/env python3
"""Entry for make.fun: the-joke-the-reviewer-laughs-at-20261121-0329.

Writes a single one-line joke about working beside AI coding agents
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only, no network, fully deterministic.
"""

import os

JOKE = (
    "The reviewer said my code was 'self-documenting'. "
    "It documented itself a resignation letter."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
