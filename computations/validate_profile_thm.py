#!/usr/bin/env python3
"""Exhaustively compare the profile criterion with all antichains for n<=6."""

from __future__ import annotations

import sys
from itertools import combinations
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ep776_profile import profile_test  # noqa: E402


def all_antichain_profiles(n: int) -> set[tuple[int, ...]]:
    sets: list[tuple[int, int]] = []
    for size in range(n + 1):
        for member in combinations(range(n), size):
            mask = 0
            for element in member:
                mask |= 1 << element
            sets.append((size, mask))

    number_of_sets = len(sets)
    incompatible = [0] * number_of_sets
    for i in range(number_of_sets):
        _, first = sets[i]
        for j in range(i + 1, number_of_sets):
            _, second = sets[j]
            intersection = first & second
            if intersection == first or intersection == second:
                incompatible[i] |= 1 << j

    profiles: set[tuple[int, ...]] = set()
    profile = [0] * (n + 1)

    def visit(start: int, allowed: int) -> None:
        profiles.add(tuple(profile))
        remaining = allowed >> start
        index = start
        while remaining:
            if remaining & 1:
                level = sets[index][0]
                profile[level] += 1
                visit(index + 1, allowed & ~incompatible[index] & ~(1 << index))
                profile[level] -= 1
            remaining >>= 1
            index += 1

    visit(0, (1 << number_of_sets) - 1)
    return profiles


def criterion_profiles(n: int):
    ranges = [range(comb(n, level) + 1) for level in range(n + 1)]
    current: list[int] = []

    def visit(level: int):
        if level == n + 1:
            yield tuple(current)
            return
        for value in ranges[level]:
            current.append(value)
            yield from visit(level + 1)
            current.pop()

    yield from visit(0)


def main() -> None:
    for n in (4, 5, 6):
        achieved = all_antichain_profiles(n)
        print(f"n={n}: {len(achieved)} achievable profiles")
        checked = 0
        for candidate in criterion_profiles(n):
            feasible, _ = profile_test(n, dict(enumerate(candidate)))
            if feasible != (candidate in achieved):
                raise AssertionError(
                    f"n={n} mismatch for {candidate}: criterion={feasible}"
                )
            checked += 1
        print(f"n={n}: exhaustive agreement across {checked} candidate profiles")


if __name__ == "__main__":
    main()

