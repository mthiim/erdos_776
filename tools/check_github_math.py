#!/usr/bin/env python3
"""Reject LaTeX delimiters that GitHub Markdown displays as plain brackets."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".lake"}
UNSUPPORTED = re.compile(r"^\\\[$|^\\\]$|\\\(|\\\)", re.MULTILINE)


def main() -> int:
    failures: list[str] = []
    files = sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts)
    )

    for path in files:
        source = path.read_text(encoding="utf-8")
        for match in UNSUPPORTED.finditer(source):
            line = source.count("\n", 0, match.start()) + 1
            failures.append(f"{path.relative_to(ROOT)}:{line}: {match.group(0)}")

    if failures:
        print("Unsupported GitHub math delimiters found:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        print("Use $...$ inline and $$...$$ for display math.", file=sys.stderr)
        return 1

    print(f"GitHub math-delimiter scan passed ({len(files)} Markdown files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
