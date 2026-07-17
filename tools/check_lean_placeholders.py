#!/usr/bin/env python3
"""Reject unfinished proof tokens in project Lean source.

Comments and string literals are removed by a small lexer before matching, so
documentation may discuss `sorry`, `admit`, or project axioms without causing
a false positive.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".lake"}
FORBIDDEN = re.compile(
    r"\b(?:sorry|admit|sorryAx|axiom)\b",
    re.MULTILINE,
)


def strip_comments_and_strings(source: str) -> str:
    """Replace comments and strings with spaces while preserving newlines."""

    out: list[str] = []
    i = 0
    block_depth = 0
    in_line_comment = False
    in_string = False

    while i < len(source):
        if in_line_comment:
            if source[i] == "\n":
                in_line_comment = False
                out.append("\n")
            else:
                out.append(" ")
            i += 1
            continue

        if block_depth:
            if source.startswith("/-", i):
                block_depth += 1
                out.extend((" ", " "))
                i += 2
            elif source.startswith("-/", i):
                block_depth -= 1
                out.extend((" ", " "))
                i += 2
            else:
                out.append("\n" if source[i] == "\n" else " ")
                i += 1
            continue

        if in_string:
            if source[i] == "\\" and i + 1 < len(source):
                out.extend((" ", " "))
                i += 2
            elif source[i] == '"':
                in_string = False
                out.append(" ")
                i += 1
            else:
                out.append("\n" if source[i] == "\n" else " ")
                i += 1
            continue

        if source.startswith("--", i):
            in_line_comment = True
            out.extend((" ", " "))
            i += 2
        elif source.startswith("/-", i):
            block_depth = 1
            out.extend((" ", " "))
            i += 2
        elif source[i] == '"':
            in_string = True
            out.append(" ")
            i += 1
        else:
            out.append(source[i])
            i += 1

    return "".join(out)


def lean_sources() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.lean")
        if not any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts)
    )


def main() -> int:
    failures: list[str] = []
    sources = lean_sources()
    for path in sources:
        source = path.read_text(encoding="utf-8")
        code = strip_comments_and_strings(source)
        for match in FORBIDDEN.finditer(code):
            line = code.count("\n", 0, match.start()) + 1
            token = match.group(0).strip()
            failures.append(f"{path.relative_to(ROOT)}:{line}: {token}")

    if failures:
        print("Unfinished Lean source found:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1

    print(f"Lean placeholder scan passed ({len(sources)} source files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
