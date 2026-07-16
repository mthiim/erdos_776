#!/usr/bin/env python3
"""Independent exact verification of n0(r)=2r+4 for 4 <= r <= 10.

This script imports none of the project proof/construction modules. It:

1. recomputes the prescribed-profile obstruction at n=2r+4;
2. recomputes feasibility at n=2r+5 and directly checks the stored witness;
3. directly checks the stored base core and the r explicit free sets;
4. performs five persistent two-point padding stages; and
5. directly checks full witnesses for both parities at every tested stage.

The infinite continuation rests on the elementary padding and core-to-full
lemmas proved in docs/SMALL_R_NOTE.md and docs/TECHNICAL_NOTE.md; the finite
stages here are regression/falsification checks of those formulas.
"""
from __future__ import annotations

import re
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FULL_CERT = ROOT / "certificates" / "small_r_full_witnesses_r4_to_10.txt"
CORE_CERT = ROOT / "certificates" / "small_r_cores_and_free_sets_r4_to_10.txt"


def kk_shadow(m: int, k: int, nmax: int) -> int:
    """Exact Kruskal--Katona minimum lower shadow of m k-sets."""
    if m < 0 or k < 1:
        raise ValueError((m, k))
    if m == 0:
        return 0
    remainder = m
    previous = nmax + 1
    shadow = 0
    for position in range(k, 0, -1):
        hi = previous - 1
        lo = position - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if comb(mid, position) <= remainder:
                lo = mid
            else:
                hi = mid - 1
        digit = lo
        if digit >= position:
            remainder -= comb(digit, position)
            shadow += comb(digit, position - 1)
            previous = digit
            if remainder == 0:
                return shadow
        else:
            previous = digit
    raise AssertionError(f"incomplete cascade: m={m}, k={k}, rem={remainder}")


def full_iterates(n: int, r: int) -> dict[int, int]:
    current = 0
    values: dict[int, int] = {}
    for level in range(n - 2, 1, -1):
        current = r + kk_shadow(current, level + 1, n)
        values[level] = current
    return values


def core_iterates(q: int, s: int, r: int) -> dict[int, int]:
    current = 0
    values: dict[int, int] = {}
    for level in range(s, 1, -1):
        current = r + kk_shadow(current, level + 1, q)
        values[level] = current
    return values


def parse_braced_sets(text: str) -> list[frozenset[int]]:
    return [
        frozenset(int(value) - 1 for value in group.split(","))
        for group in re.findall(r"\{([0-9,]+)\}", text)
    ]


def parse_full_certificates(path: Path) -> dict[int, tuple[int, dict[int, list[frozenset[int]]]]]:
    out: dict[int, tuple[int, dict[int, list[frozenset[int]]]]] = {}
    current_r: int | None = None
    current_n: int | None = None
    layers: dict[int, list[frozenset[int]]] = {}

    def store() -> None:
        nonlocal current_r, current_n, layers
        if current_r is not None and current_n is not None:
            if current_r in out:
                raise AssertionError(f"duplicate full certificate for r={current_r}")
            out[current_r] = (current_n, layers)
        current_r = current_n = None
        layers = {}

    for line in path.read_text(encoding="utf-8").splitlines():
        header = re.match(
            r"A construction showing that for r=(\d+) and n=(\d+),", line
        )
        if header:
            store()
            current_r = int(header.group(1))
            current_n = int(header.group(2))
            continue
        layer = re.match(r"Layer\s+(\d+):(.*)", line)
        if layer and current_r is not None:
            layers[int(layer.group(1))] = parse_braced_sets(layer.group(2))
    store()
    return out


def parse_core_certificates(
    path: Path,
) -> dict[int, tuple[int, int, dict[int, list[frozenset[int]]], list[frozenset[int]]]]:
    out: dict[
        int,
        tuple[int, int, dict[int, list[frozenset[int]]], list[frozenset[int]]],
    ] = {}
    current_r: int | None = None
    q = s = 0
    layers: dict[int, list[frozenset[int]]] = {}
    free: list[frozenset[int]] = []

    def store() -> None:
        nonlocal current_r, q, s, layers, free
        if current_r is not None:
            if current_r in out:
                raise AssertionError(f"duplicate core certificate for r={current_r}")
            out[current_r] = (q, s, layers, free)
        current_r = None
        q = s = 0
        layers = {}
        free = []

    for line in path.read_text(encoding="utf-8").splitlines():
        header = re.match(r"=== r=(\d+) q=(\d+) s=(\d+) ===", line)
        if header:
            store()
            current_r = int(header.group(1))
            q = int(header.group(2))
            s = int(header.group(3))
            continue
        layer = re.match(r"Core layer\s+(\d+):(.*)", line)
        if layer and current_r is not None:
            layers[int(layer.group(1))] = parse_braced_sets(layer.group(2))
            continue
        free_line = re.match(r"Free\s+\d+-sets:(.*)", line)
        if free_line and current_r is not None:
            free = parse_braced_sets(free_line.group(1))
    store()
    return out


def check_family(
    family: dict[int, list[frozenset[int]]],
    n: int,
    r: int,
    expected_levels: set[int],
    *,
    exact_multiplicity: bool = True,
) -> None:
    if set(family) != expected_levels:
        raise AssertionError((sorted(family), sorted(expected_levels)))

    masks: list[int] = []
    seen: set[int] = set()
    for level in sorted(family):
        layer = family[level]
        if exact_multiplicity and len(layer) != r:
            raise AssertionError(f"level {level}: {len(layer)} != {r}")
        if not exact_multiplicity and len(layer) < r:
            raise AssertionError(f"level {level}: {len(layer)} < {r}")
        for member in layer:
            if len(member) != level:
                raise AssertionError((level, sorted(member)))
            if not all(0 <= x < n for x in member):
                raise AssertionError((n, sorted(member)))
            mask = sum(1 << x for x in member)
            if mask in seen:
                raise AssertionError(f"duplicate mask {mask:x}")
            seen.add(mask)
            masks.append(mask)

    for i, left in enumerate(masks):
        for right in masks[i + 1 :]:
            intersection = left & right
            if intersection == left or intersection == right:
                raise AssertionError(f"containment: {left:x}, {right:x}")


def flatten(family: dict[int, list[frozenset[int]]]) -> list[frozenset[int]]:
    return [member for layer in family.values() for member in layer]


def pad_persistently(
    base: dict[int, list[frozenset[int]]],
    base_free: list[frozenset[int]],
    q0: int,
    s0: int,
    stages: int,
) -> list[tuple[dict[int, list[frozenset[int]]], int, int]]:
    family = {level: list(layer) for level, layer in base.items()}
    out = [(family, q0, s0)]
    x_points: list[int] = []

    for stage in range(1, stages + 1):
        x = q0 + 2 * (stage - 1)
        y = x + 1
        persistent_before = [D | frozenset(x_points) for D in base_free]
        old_members = flatten(family)
        if any(any(old <= D for old in old_members) for D in persistent_before):
            raise AssertionError(f"persistent freeness failed before stage {stage}")

        new_layer = [D | {x, y} for D in persistent_before]
        family = {level: list(layer) for level, layer in family.items()}
        family[s0 + stage] = new_layer
        x_points.append(x)

        q = q0 + 2 * stage
        s = s0 + stage
        check_family(family, q, len(base_free), set(range(2, s + 1)))

        persistent_after = [D | frozenset(x_points) for D in base_free]
        all_members = flatten(family)
        if any(any(old <= D for old in all_members) for D in persistent_after):
            raise AssertionError(f"persistent freeness failed after stage {stage}")
        out.append((family, q, s))

    return out


def full_from_core(
    core: dict[int, list[frozenset[int]]], q: int, r: int, n: int
) -> dict[int, list[frozenset[int]]]:
    half = n // 2
    pivot = n - 1 - r
    if q > pivot:
        raise AssertionError((q, pivot))
    private = list(range(pivot + 1, pivot + 1 + r))

    low: dict[int, list[frozenset[int]]] = {
        2: [frozenset({pivot, p}) for p in private]
    }
    for core_size in range(2, half):
        layer = core[core_size]
        low[core_size + 1] = [member | {pivot} for member in layer[:r]]

    all_points = frozenset(range(n))
    full = {level: list(layer) for level, layer in low.items()}
    for level, layer in low.items():
        reflected = n - level
        complements = [all_points - member for member in layer]
        if reflected in full and reflected != level:
            full[reflected].extend(complements)
        elif reflected not in full:
            full[reflected] = complements
    return full


def main() -> None:
    full_certificates = parse_full_certificates(FULL_CERT)
    core_certificates = parse_core_certificates(CORE_CERT)
    if set(full_certificates) != set(range(4, 11)):
        raise AssertionError(f"unexpected full-certificate keys: {sorted(full_certificates)}")
    if set(core_certificates) != set(range(4, 11)):
        raise AssertionError(f"unexpected core-certificate keys: {sorted(core_certificates)}")

    obstruction_rows = {
        4: (67, 66, 1),
        5: (92, 91, 1),
        6: (121, 120, 1),
        7: (155, 153, 2),
        8: (192, 190, 2),
        9: (233, 231, 2),
        10: (278, 276, 2),
    }
    expected_core_carries = {4: -7, 5: -4, 6: -3, 7: -2, 8: -2, 9: -2, 10: -2, 11: 1}
    observed_core_carries: dict[int, int] = {}
    for carry_r in range(4, 12):
        A = carry_r + 4
        current = 0
        for level in range(carry_r + 2, 2, -1):
            current = carry_r + kk_shadow(current, level + 1, A)
        observed_core_carries[carry_r] = current - comb(A, 3)
    if observed_core_carries != expected_core_carries:
        raise AssertionError((observed_core_carries, expected_core_carries))

    for r in range(4, 11):
        # Obstruction at n=2r+4.
        n_fail = 2 * r + 4
        values = full_iterates(n_fail, r)
        expected_m2, expected_capacity, expected_excess = obstruction_rows[r]
        excess = values[2] - comb(n_fail, 2)
        if (values[2], comb(n_fail, 2), excess) != (
            expected_m2,
            expected_capacity,
            expected_excess,
        ):
            raise AssertionError(f"r={r}: obstruction arithmetic mismatch")

        # Direct full witness at n=2r+5.
        n_base = 2 * r + 5
        values_base = full_iterates(n_base, r)
        if any(values_base[i] > comb(n_base, i) for i in values_base):
            raise AssertionError(f"r={r}: recurrence says n={n_base} infeasible")
        if values_base[2] != comb(n_base, 2):
            raise AssertionError(f"r={r}: expected tight level 2 at n={n_base}")
        stored_n, full_witness = full_certificates[r]
        if stored_n != n_base:
            raise AssertionError((r, stored_n, n_base))
        check_family(full_witness, n_base, r, set(range(2, n_base - 1)))

        # Base core and explicit free sets.
        q, s, core, free = core_certificates[r]
        if (q, s) != (r + 5, r + 2):
            raise AssertionError((r, q, s))
        core_values = core_iterates(q, s, r)
        if any(core_values[i] > comb(q, i) for i in core_values):
            raise AssertionError(f"r={r}: base core infeasible")
        check_family(core, q, r, set(range(2, s + 1)))
        expected_free = [
            frozenset(set(range(q)) - {0, j, q - 2, q - 1})
            for j in range(3, q - 2)
        ]
        if free != expected_free or len(set(free)) != r:
            raise AssertionError(f"r={r}: explicit D_j list mismatch")
        core_members = flatten(core)
        if any(any(member <= D for member in core_members) for D in free):
            raise AssertionError(f"r={r}: a stored D_j is not free")

        # Five padding stages and both parities of the full construction.
        stages = pad_persistently(core, free, q, s, stages=5)
        for t, (stage_core, stage_q, _stage_s) in enumerate(stages):
            for n in (2 * r + 6 + 2 * t, 2 * r + 7 + 2 * t):
                full = full_from_core(stage_core, stage_q, r, n)
                check_family(full, n, r, set(range(2, n - 1)))

        print(
            f"[OK] r={r}: n={n_fail} fails by {excess}; "
            f"n={n_base} witness checked; core/free sets and 5 padding stages checked"
        )

    print("[OK] core carry changes sign between r=10 and r=11")
    print("PASS: n_0(r)=2r+4 is certified for every 4 <= r <= 10")


if __name__ == "__main__":
    main()
