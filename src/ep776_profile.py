#!/usr/bin/env python3
"""Exact profile test and explicit construction for Erdos problem 776.

Mathematical basis (elementary, from Kruskal-Katona):

  A vector (f_0,...,f_n) is the profile of an antichain in 2^[n] iff the
  top-down cascade iterates fit inside the levels:

      m_s = f_s                       (s = highest occupied level)
      m_i = f_i + kk_shadow(m_{i+1}, i+1)     for i < s
      feasible  <=>  m_i <= C(n,i) for every level i >= lowest occupied.

  Sufficiency: take, on each level from the top down, the f_i colex-first
  sets NOT in the down-closure of the higher choices.  The cumulative
  family on each level is then a colex initial segment of size m_i, whose
  shadow is again a colex initial segment of size kk_shadow(m_i, i).

  Necessity: for an arbitrary antichain F with profile f let D_i be the
  level-i part of the down-closure of the higher levels and M_i = F_i u D_i
  (disjoint union, since F is an antichain).  Every set in the shadow of
  M_{i+1} lies in D_i, so |M_i| >= f_i + kk_shadow(|M_{i+1}|, i+1) and by
  induction |M_i| >= m_i; hence m_i <= C(n,i).

Consequences used here:

  * Whenever a separate missing-level argument shows that every
    (n-3)-level witness must occupy exactly {2,...,n-2}, the question
    g(n,r)=n-3 is equivalent to feasibility of the profile with f_i=r on
    those levels.  Section 1 of docs/TECHNICAL_NOTE.md gives the elementary
    argument needed for the (n,r)=(27,11) result.  No such reduction is
    assumed automatically for arbitrary small parameters.

  * The "core" problem (r sets of every size 2..s on q points, an
    antichain) is likewise a profile question with f_i = r for 2 <= i <= s.
"""

from __future__ import annotations

import argparse
from math import comb


def cascade(m: int, k: int) -> list[tuple[int, int]]:
    """Unique representation m = C(a_k,k)+C(a_{k-1},k-1)+...+C(a_t,t)
    with a_k > a_{k-1} > ... > a_t >= t >= 1.  Requires m >= 0, k >= 1."""
    rep: list[tuple[int, int]] = []
    j = k
    prev_a = None
    while m > 0 and j >= 1:
        # largest a with C(a,j) <= m (and a < prev_a to keep strictness)
        a = j
        while comb(a + 1, j) <= m and (prev_a is None or a + 1 < prev_a):
            a += 1
        rep.append((a, j))
        m -= comb(a, j)
        prev_a = a
        j -= 1
    assert m == 0, "cascade failed (m too large for level?)"
    return rep


def kk_shadow(m: int, k: int) -> int:
    """Minimum size of the (lower) shadow of m k-sets (Kruskal-Katona)."""
    if m == 0:
        return 0
    if k == 0:
        return 0
    return sum(comb(a, j - 1) for a, j in cascade(m, k))


def profile_test(n: int, f: dict[int, int]) -> tuple[bool, dict[int, int]]:
    """Exact feasibility test for an antichain on [n] with profile f.

    Returns (feasible, m) where m maps each level in [lowest occupied,
    highest occupied] to the cascade iterate."""
    occupied = [i for i, c in f.items() if c > 0]
    if not occupied:
        return True, {}
    lo, hi = min(occupied), max(occupied)
    m: dict[int, int] = {}
    cur = 0
    ok = True
    for i in range(hi, lo - 1, -1):
        cur = kk_shadow(cur, i + 1) + f.get(i, 0)
        m[i] = cur
        if cur > comb(n, i):
            ok = False
    return ok, m


def colex_unrank(rank: int, k: int) -> frozenset[int]:
    """The rank-th k-subset of the nonnegative integers in colex order,
    0-indexed, elements 0-based."""
    out = []
    r = rank
    for j in range(k, 0, -1):
        a = j - 1
        while comb(a + 1, j) <= r:
            a += 1
        out.append(a)
        r -= comb(a, j)
    assert r == 0
    return frozenset(out)


def construct(n: int, f: dict[int, int]) -> dict[int, list[frozenset[int]]] | None:
    """Explicit antichain with profile f on [n] via the colex greedy,
    or None if the test fails.  Family maps level -> list of 0-based sets."""
    ok, m = profile_test(n, f)
    if not ok:
        return None
    occupied = sorted(i for i, c in f.items() if c > 0)
    if not occupied:
        return {}
    lo, hi = occupied[0], occupied[-1]
    family: dict[int, list[frozenset[int]]] = {}
    shadow_size = 0  # size of down-closure (colex initial segment) at level i
    for i in range(hi, lo - 1, -1):
        cnt = f.get(i, 0)
        if cnt:
            layer = [colex_unrank(shadow_size + t, i) for t in range(cnt)]
            assert all(all(0 <= element < n for element in member) for member in layer)
            family[i] = layer
        shadow_size = kk_shadow(shadow_size + cnt, i)
    return family


# ---------------------------------------------------------------------------
# EP776-specific wrappers


def full_profile(n: int, r: int) -> dict[int, int]:
    return {i: r for i in range(2, n - 1)}


def test_full(n: int, r: int) -> bool:
    ok, _ = profile_test(n, full_profile(n, r))
    return ok


def core_profile(s: int, r: int) -> dict[int, int]:
    return {i: r for i in range(2, s + 1)}


def test_core(q: int, s: int, r: int) -> bool:
    ok, _ = profile_test(q, core_profile(s, r))
    return ok


def n0_upper_scan(r: int, n_max_extra: int = 80) -> int | None:
    """Largest failed full-profile instance in an inclusive finite window.

    The scanned window is [2r+2, 2r+2+n_max_extra].  This helper tests only
    prescribed-profile feasibility inside that window; it does not by itself
    certify n_0(r).  It returns None when the window contains no failures.
    """
    n_min = 2 * r + 2
    n_max = n_min + n_max_extra
    fails = [n for n in range(n_min, n_max + 1) if not test_full(n, r)]
    return max(fails) if fails else None


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("full", help="test g(n,r)=n-3 profile feasibility")
    p.add_argument("n", type=int)
    p.add_argument("r", type=int)
    p.add_argument("--emit", action="store_true", help="print explicit family")

    p = sub.add_parser("core", help="test core profile (r sets of sizes 2..s on q points)")
    p.add_argument("q", type=int)
    p.add_argument("s", type=int)
    p.add_argument("r", type=int)
    p.add_argument("--emit", action="store_true")

    p = sub.add_parser("n0", help="finite full-profile scan for a range of r")
    p.add_argument("rmin", type=int)
    p.add_argument("rmax", type=int)
    p.add_argument("--extra", type=int, default=80)

    args = ap.parse_args()
    if args.cmd == "full":
        f = full_profile(args.n, args.r)
        ok, m = profile_test(args.n, f)
        print(f"n={args.n} r={args.r} feasible={ok}")
        for i in sorted(m):
            slack = comb(args.n, i) - m[i]
            flag = "" if slack >= 0 else "  <-- VIOLATED"
            print(f"  level {i:3d}: m={m[i]}  C(n,i)={comb(args.n, i)}  slack={slack}{flag}")
        if ok and args.emit:
            fam = construct(args.n, f)
            for i in sorted(fam):
                print(f"{i}: " + " ".join(
                    "{" + ",".join(str(e + 1) for e in sorted(s)) + "}" for s in fam[i]))
    elif args.cmd == "core":
        f = core_profile(args.s, args.r)
        ok, m = profile_test(args.q, f)
        print(f"q={args.q} s={args.s} r={args.r} feasible={ok}")
        for i in sorted(m):
            slack = comb(args.q, i) - m[i]
            flag = "" if slack >= 0 else "  <-- VIOLATED"
            print(f"  level {i:3d}: m={m[i]}  C(q,i)={comb(args.q, i)}  slack={slack}{flag}")
        if ok and args.emit:
            fam = construct(args.q, f)
            for i in sorted(fam):
                print(f"{i}: " + " ".join(
                    "{" + ",".join(str(e + 1) for e in sorted(s)) + "}" for s in fam[i]))
    elif args.cmd == "n0":
        for r in range(args.rmin, args.rmax + 1):
            largest_failure = n0_upper_scan(r, args.extra)
            if largest_failure is None:
                print(f"r={r:5d}  no failures in the scanned window")
            else:
                print(
                    f"r={r:5d}  largest_scanned_failure={largest_failure}  "
                    f"largest_failure-2r={largest_failure - 2 * r}"
                )


if __name__ == "__main__":
    main()
