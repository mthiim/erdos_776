#!/usr/bin/env python3
"""Constructive chain: base core -> padded cores -> full witnesses.

Base: CORE(q0=r+5, levels 2..s0=r+2) via the colex greedy (ep776_profile).

Padding Lemma (verified here with explicit sets): if C is an antichain on
[q] with >= r sets of each size 2..s, and D_1,...,D_r are distinct
(s-1)-subsets of [q] containing no member of C ("free"), then

    C' = C  u  { D_i u {x,y} : i in [r] }        (x,y two new points)

is an antichain on q+2 points with >= r sets of each size 2..s+1.

Iterating from the base with D chosen as G u {x_1,...,x_t} (G free for the
base, one point of each earlier pair) keeps the freeness hypothesis alive
forever off the base's r free sets alone.

Reduction (He-Tang style, proved in docs/TECHNICAL_NOTE.md): a core on q <= n-1-r
points with levels 2..floor(n/2)-1 plus a point a and r private points
gives a full witness for g(n,r) = n-3.
"""

from __future__ import annotations

import argparse
from itertools import combinations

from ep776_profile import construct, core_profile
from ep776_check import check_antichain_profile, check_full_witness


def free_sets(core: dict[int, list[frozenset[int]]], q: int, size: int, want: int):
    """First `want` size-subsets of [0,q) containing no member of core."""
    members = [s for layer in core.values() for s in layer]
    out = []
    for c in combinations(range(q), size):
        cand = frozenset(c)
        if not any(m <= cand for m in members):
            out.append(cand)
            if len(out) == want:
                break
    return out


def pad_core(core, q, s, r):
    """One padding step: returns (core', q+2, s+1). Points q, q+1 are new."""
    frees = free_sets(core, q, s - 1, r)
    if len(frees) < r:
        raise ValueError(f"only {len(frees)} free ({s-1})-sets, need {r}")
    new = [d | {q, q + 1} for d in frees]
    core2 = {lvl: list(layer) for lvl, layer in core.items()}
    core2[s + 1] = new
    return core2, q + 2, s + 1


def full_from_core(core, q, r, n):
    """He-Tang reduction: core (levels 2..floor(n/2)-1 used) -> witness on [n]."""
    k = n // 2
    a = n - 1 - r  # place a after the core points; privates after a
    priv = list(range(a + 1, a + 1 + r))
    assert q <= a, (q, a)
    low = {2: [frozenset({a, p}) for p in priv]}
    for size in range(2, k):
        layer = core[size]
        low[size + 1] = [s | {a} for s in layer[:r]]
    full = dict(low)
    allpts = frozenset(range(n))
    for size, layer in low.items():
        if n - size not in full:
            full[n - size] = [allpts - s for s in layer]
        elif n - size != size:
            full[n - size].extend(allpts - s for s in layer)
    return full


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("r", type=int)
    ap.add_argument("--stages", type=int, default=3)
    args = ap.parse_args()
    r = args.r
    q, s = r + 5, r + 2
    core = construct(q, core_profile(s, r))
    if core is None:
        raise SystemExit("base core infeasible")
    errs = check_antichain_profile(core, q, r, set(range(2, s + 1)))
    print(f"base core q={q} s={s}: {'OK' if not errs else errs[:3]}")

    stage_cores = [(core, q, s)]
    for t in range(args.stages):
        core, q, s = pad_core(core, q, s, r)
        errs = check_antichain_profile(core, q, r, set(range(2, s + 1)))
        print(f"stage {t+1}: core q={q} s={s}: {'OK' if not errs else errs[:3]}")
        stage_cores.append((core, q, s))

    # build and check full witnesses for n = 2r+6 .. 2r+5+2*stages
    for n in range(2 * r + 6, 2 * r + 6 + 2 * args.stages):
        k = n // 2
        # pick the first stage with s >= k-1 and q <= n-1-r
        for c, qq, ss in stage_cores:
            if ss >= k - 1 and qq <= n - 1 - r:
                fam = full_from_core(c, qq, r, n)
                errs = check_full_witness(fam, n, r)
                nsets = sum(len(v) for v in fam.values())
                print(f"n={n} (r={r}): witness from core(q={qq},s={ss}), "
                      f"{nsets} sets: {'OK' if not errs else errs[:3]}")
                break
        else:
            print(f"n={n}: no suitable stage core!")


if __name__ == "__main__":
    main()
