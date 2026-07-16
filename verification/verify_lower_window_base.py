#!/usr/bin/env python3
"""Fast independent finite-base verifier for the EP776 lower window.

Checks every integer 11 <= r <= 377 using exact arithmetic and a
precomputed Pascal triangle.  It also checks r = 377, 378, 379 explicitly
across the finite/symbolic proof boundary.  It does not import the EP776
project.
"""
from __future__ import annotations
from bisect import bisect_right

FINITE_BASE_MAX_R = 377
SEAM_EXPECTED = {
    377: (3, 2),
    378: (3, 2),
    379: (3, 2),
}
MAX_R = max(SEAM_EXPECTED)
MAX_N = MAX_R + 4

BINOM = [[0] * (MAX_N + 1) for _ in range(MAX_N + 1)]
for n in range(MAX_N + 1):
    BINOM[n][0] = 1
    BINOM[n][n] = 1
    for k in range(1, n):
        BINOM[n][k] = BINOM[n - 1][k - 1] + BINOM[n - 1][k]

COL = [None] * (MAX_N + 1)
for k in range(1, MAX_N + 1):
    COL[k] = [BINOM[a][k] for a in range(k, MAX_N + 1)]


def C(n: int, k: int) -> int:
    if k < 0 or k > n or n < 0:
        return 0
    return BINOM[n][k]


def kk_shadow(m: int, k: int, nmax: int) -> int:
    if m < 0:
        raise ValueError("m must be nonnegative")
    if m == 0:
        return 0
    remainder = m
    previous_digit = nmax + 1
    shadow = 0
    for position in range(k, 0, -1):
        max_digit = previous_digit - 1
        if max_digit < position:
            previous_digit = max_digit
            continue
        values = COL[position]
        index = bisect_right(
            values, remainder, 0, max_digit - position + 1
        ) - 1
        if index >= 0:
            digit = position + index
            remainder -= values[index]
            shadow += BINOM[digit][position - 1]
            previous_digit = digit
            if remainder == 0:
                return shadow
        else:
            previous_digit = position - 1
    raise AssertionError((m, k, nmax, remainder))


def check_r(r: int) -> tuple[bool, int, int]:
    A = r + 4
    current = r - 6
    minimum_slack = C(A, r + 1) - current
    minimum_level = r + 1
    for level in range(r, 1, -1):
        current = r + kk_shadow(current, level + 1, A)
        slack = C(A, level) - current
        if slack < minimum_slack:
            minimum_slack = slack
            minimum_level = level
        if slack < 0:
            return False, minimum_slack, minimum_level
    return True, minimum_slack, minimum_level


def main() -> None:
    global_minimum = None
    for r in range(11, FINITE_BASE_MAX_R + 1):
        feasible, slack, level = check_r(r)
        if not feasible:
            raise SystemExit(f"FAIL: r={r}, deficit={-slack}, level={level}")
        candidate = (slack, r, level)
        if global_minimum is None or candidate < global_minimum:
            global_minimum = candidate
    assert global_minimum is not None
    slack, r, level = global_minimum
    print("PASS: exact lower-window check for every 11 <= r <= 377")
    print(f"minimum slack = {slack}, attained at r={r}, level={level}")

    # Regression checks at the finite/symbolic seam.  The recurrence is
    # deterministic, so record the exact minimum slack as well as feasibility.
    for seam_r, expected in SEAM_EXPECTED.items():
        feasible, seam_slack, seam_level = check_r(seam_r)
        if not feasible:
            raise SystemExit(
                f"FAIL: lower-window seam r={seam_r}, "
                f"deficit={-seam_slack}, level={seam_level}"
            )
        observed = (seam_slack, seam_level)
        if observed != expected:
            raise SystemExit(
                f"FAIL: lower-window seam r={seam_r}: "
                f"observed (minimum slack, level)={observed}, "
                f"expected {expected}"
            )
    print(
        "PASS: lower-window finite/symbolic seam at r=377,378,379; "
        "minimum slack is 3 at level 2 in each case"
    )


if __name__ == "__main__":
    main()
