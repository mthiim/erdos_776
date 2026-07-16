#!/usr/bin/env python3
"""Check the finite L4 base and stress-test the symbolic reverse envelope."""
from __future__ import annotations
from math import comb
from kk_exact import kk_shadow, profile_test


def C(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def ghat(r: int, i: int) -> int:
    if i == 2:
        return C(r + 4, 2)
    if i == 3:
        return C(r + 3, 3) + 3
    if i == 4:
        return C(r + 2, 4) + C(r + 1, 3) + 6
    if i == 5:
        return C(r + 2, 5) + C(r, 4) + C(r - 1, 3) + 10
    if i == 6:
        return C(r + 2, 6) + C(r, 5) + C(r - 2, 4) + C(r - 3, 3) + 21
    if i == 7:
        return (C(r + 2, 7) + C(r, 6) + C(r - 2, 5)
                + C(r - 4, 4) + C(r - 5, 3) + 120)
    if 8 <= i <= r - 2:
        return (C(r + 2, i) + C(r, i - 1) + C(r - 2, i - 2)
                + C(r - 4, i - 3) + C(r - 5, i - 4)
                + C(23, i - 5))
    raise ValueError((r, i))


def check_r(r: int) -> None:
    A = r + 4
    # Every reverse step of Lemma RS.
    for i in range(3, r - 1):
        lhs = r + kk_shadow(ghat(r, i) + 1, i, A)
        rhs = ghat(r, i - 1)
        if not lhs > rhs:
            raise AssertionError(("reverse", r, i, lhs, rhs))

    # Three exact top steps of Lemma L4-T.
    cur = r
    for level in range(r, r - 3, -1):
        cur = r + kk_shadow(cur, level + 1, A)
    expected = C(r + 2, 4) + C(r, 3) + C(r - 2, 2) + 3 * r - 9
    if cur != expected:
        raise AssertionError(("top", r, cur, expected))
    if not cur > ghat(r, r - 2):
        raise AssertionError(("margin", r, cur, ghat(r, r - 2)))


def main() -> None:
    # Exact finite base used by the proof.
    for r in range(11, 29):
        A = r + 4
        profile = {i: r for i in range(2, r + 2)}
        ok, states = profile_test(A, profile)
        if ok:
            raise SystemExit(f"FAIL: finite L4 profile feasible at r={r}")

        # profile_test stops at the first capacity violation.  Therefore
        # reaching level 2 certifies that every level above 2 was feasible.
        first_failed_level = min(states)
        if first_failed_level != 2:
            raise SystemExit(
                "FAIL: finite L4 profile first overflows at "
                f"level {first_failed_level}, not level 2, for r={r}"
            )

        expected_bottom = C(A, 2) + 1
        if states[2] != expected_bottom:
            raise SystemExit(
                "FAIL: wrong finite L4 bottom overflow at "
                f"r={r}: m_2={states[2]}, expected {expected_bottom}"
            )

    print(
        "PASS: exact L4 finite base for every 11 <= r <= 28; "
        "the first overflow is m_2 = binom(r+4,2) + 1"
    )

    # Supplementary exact spot checks of the symbolic formulas. The proof
    # itself is all-r; these computations are falsification tests only.
    samples = (29, 30, 31, 40, 60, 100, 200, 400, 1000)
    for r in samples:
        check_r(r)
    print("PASS: L4 reverse-envelope formulas at " + ", ".join(map(str, samples)))


if __name__ == "__main__":
    main()
