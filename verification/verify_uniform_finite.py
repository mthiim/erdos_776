#!/usr/bin/env python3
"""Fast finite assembly cross-check for the uniform theorem.

Checks every 11 <= r <= 120, matching the exact assembly range reported
by the adversarial audit. This is a falsification test, not the all-r proof.
"""
from __future__ import annotations

MAX_R = 120
MAX_N = 2 * MAX_R + 6

BINOM = [[0] * (MAX_N + 1) for _ in range(MAX_N + 1)]
for n in range(MAX_N + 1):
    BINOM[n][0] = BINOM[n][n] = 1
    for k in range(1, n):
        BINOM[n][k] = BINOM[n - 1][k - 1] + BINOM[n - 1][k]


def C(n: int, k: int) -> int:
    if n < 0 or k < 0 or k > n:
        return 0
    return BINOM[n][k]


def shadow(m: int, k: int, nmax: int) -> int:
    if m == 0:
        return 0
    rem = m
    prev = nmax + 1
    ans = 0
    for pos in range(k, 0, -1):
        hi = prev - 1
        if hi < pos:
            prev = hi
            continue
        lo = pos - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if C(mid, pos) <= rem:
                lo = mid
            else:
                hi = mid - 1
        digit = lo
        if digit >= pos:
            rem -= C(digit, pos)
            ans += C(digit, pos - 1)
            prev = digit
            if rem == 0:
                return ans
        else:
            prev = digit
    raise AssertionError((m, k, nmax, rem))


def profile_test(n: int, lo: int, hi: int, load: int, top_load: int | None = None):
    cur = 0
    states = {}
    for level in range(hi, lo - 1, -1):
        if cur:
            cur = shadow(cur, level + 1, n)
        cur += top_load if top_load is not None and level == hi else load
        states[level] = cur
        if cur > C(n, level):
            return False, states
    return True, states


def main() -> None:
    min_e = 10**9
    max_e = -1
    for r in range(11, MAX_R + 1):
        A = r + 4

        ok, _ = profile_test(A, 2, r + 1, r, r - 6)
        if not ok:
            raise SystemExit(f"FAIL lower window r={r}")

        ok, _ = profile_test(A, 2, r + 1, r)
        if ok:
            raise SystemExit(f"FAIL L4 r={r}")

        ok, _ = profile_test(A + 1, 2, r + 2, r)
        if not ok:
            raise SystemExit(f"FAIL base core r={r}")

        # Upper core on A points, occupied levels 3..r+2.
        _, upper = profile_test(A, 3, r + 2, r)
        e = upper[3] - C(A, 3)
        if not 1 <= e <= 6:
            raise SystemExit(f"FAIL carry r={r}, e={e}")
        min_e = min(min_e, e)
        max_e = max(max_e, e)

        n_bad = 2 * r + 5
        ok, _ = profile_test(n_bad, 2, n_bad - 2, r)
        if ok:
            raise SystemExit(f"FAIL obstruction r={r}")

        n_good = 2 * r + 6
        ok, _ = profile_test(n_good, 2, n_good - 2, r)
        if not ok:
            raise SystemExit(f"FAIL construction profile r={r}")

    print("PASS: exact finite assembly cross-check for every 11 <= r <= 120")
    print(f"observed core carry range: {min_e} <= e_r <= {max_e}")


if __name__ == "__main__":
    main()
