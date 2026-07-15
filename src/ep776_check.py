#!/usr/bin/env python3
"""Independent exhaustive checker for EP776 witnesses.

No shadow arithmetic, no colex: just pairwise subset tests over bitmasks
and direct counting. Importable; also runs as a CLI on the witness text
format stored under ``certificates/``.
"""

from __future__ import annotations

import re
import sys


def check_antichain_profile(
    family: dict[int, list[frozenset[int]]],
    n: int,
    r: int,
    levels: set[int],
) -> list[str]:
    """Return a list of violation messages (empty = all checks pass).

    Checks: elements in [0,n); sets distinct; every set's size equals its
    layer key; exactly the given levels occur; every occurring level has
    >= r sets; NO containment between any two distinct member sets."""
    errors: list[str] = []
    all_sets: list[tuple[int, int]] = []  # (size, bitmask)
    seen: set[int] = set()
    for size, layer in family.items():
        for s in layer:
            if not all(0 <= e < n for e in s):
                errors.append(f"element out of range in {sorted(s)}")
            if len(s) != size:
                errors.append(f"set {sorted(s)} listed at size {size}")
            mask = 0
            for e in s:
                mask |= 1 << e
            if mask in seen:
                errors.append(f"duplicate set {sorted(s)}")
            seen.add(mask)
            all_sets.append((len(s), mask))
    if set(family.keys()) != levels:
        errors.append(f"levels {sorted(family.keys())} != expected {sorted(levels)}")
    for size, layer in family.items():
        if len(layer) < r:
            errors.append(f"level {size} has {len(layer)} < r={r} sets")
    for i, (sa, ma) in enumerate(all_sets):
        for sb, mb in all_sets[i + 1:]:
            if ma & mb == ma or ma & mb == mb:
                if ma != mb:
                    errors.append(f"containment between masks {ma:x} and {mb:x}")
    return errors


def check_full_witness(family: dict[int, list[frozenset[int]]], n: int, r: int) -> list[str]:
    """Witness for g(n,r) = n-3: levels exactly 2..n-2, >= r sets each."""
    return check_antichain_profile(family, n, r, set(range(2, n - 1)))


def parse_witness_file(path: str):
    """Yield (r, n, family) for each construction block in the repo format
    (1-based elements in braces; 'Layer  k: {..}, {..}')."""
    text = open(path).read()
    blocks = re.split(r"A construction showing that for ", text)
    for block in blocks[1:]:
        m = re.match(r"r=(\d+) and n=(\d+)", block)
        if not m:
            m2 = re.match(r"r=(\d+) and n=2r\+5", block)
            if not m2:
                continue
            r = int(m2.group(1))
            n = 2 * r + 5
        else:
            r, n = int(m.group(1)), int(m.group(2))
        if "n=2r+5" in block[:40]:
            n = 2 * r + 5
        family: dict[int, list[frozenset[int]]] = {}
        for lm in re.finditer(r"Layer\s+(\d+):(.*)", block):
            size = int(lm.group(1))
            sets = [
                frozenset(int(x) - 1 for x in grp.split(","))
                for grp in re.findall(r"\{([\d,]+)\}", lm.group(2))
            ]
            family[size] = sets
        yield r, n, family


def main() -> None:
    for path in sys.argv[1:]:
        for r, n, family in parse_witness_file(path):
            errors = check_full_witness(family, n, r)
            status = "OK" if not errors else "FAIL"
            print(f"{path}: r={r} n={n} sets={sum(len(v) for v in family.values())} {status}")
            for e in errors[:10]:
                print("   ", e)


if __name__ == "__main__":
    main()
