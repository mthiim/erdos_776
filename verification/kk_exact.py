"""Small exact Kruskal--Katona helpers for release verification."""
from __future__ import annotations
from math import comb


def kk_shadow(m: int, k: int, nmax: int) -> int:
    if m < 0:
        raise ValueError("m must be nonnegative")
    if m == 0:
        return 0
    if not 1 <= k <= nmax:
        raise ValueError((m, k, nmax))
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
            if comb(mid, pos) <= rem:
                lo = mid
            else:
                hi = mid - 1
        digit = lo
        if digit >= pos:
            rem -= comb(digit, pos)
            ans += comb(digit, pos - 1)
            prev = digit
            if rem == 0:
                return ans
        else:
            prev = digit
    raise AssertionError((m, k, nmax, rem))


def profile_test(n: int, profile: dict[int, int]) -> tuple[bool, dict[int, int]]:
    occupied = [i for i, value in profile.items() if value > 0]
    if not occupied:
        return True, {}
    lo, hi = min(occupied), max(occupied)
    states: dict[int, int] = {}
    cur = 0
    for level in range(hi, lo - 1, -1):
        if cur:
            cur = kk_shadow(cur, level + 1, n)
        cur += profile.get(level, 0)
        states[level] = cur
        if cur > comb(n, level):
            return False, states
    return True, states
