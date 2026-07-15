#!/usr/bin/env python3
"""Run every release-critical check for the r=11 result."""

from __future__ import annotations

import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ep776_check import (  # noqa: E402
    check_antichain_profile,
    check_full_witness,
    parse_witness_file,
)
from ep776_padding import free_sets, full_from_core, pad_core  # noqa: E402
from ep776_profile import (  # noqa: E402
    construct,
    core_profile,
    full_profile,
    profile_test,
    n0_upper_scan,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse_braced_sets(text: str) -> list[frozenset[int]]:
    return [
        frozenset(int(value) - 1 for value in group.split(","))
        for group in re.findall(r"\{([\d,]+)\}", text)
    ]


def parse_core_certificate(
    path: Path,
) -> tuple[dict[int, list[frozenset[int]]], list[frozenset[int]]]:
    core: dict[int, list[frozenset[int]]] = {}
    free: list[frozenset[int]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        layer_match = re.match(r"Core layer\s+(\d+):(.*)", line)
        if layer_match:
            core[int(layer_match.group(1))] = parse_braced_sets(layer_match.group(2))
        elif re.match(r"Free 12-set\s+\d+:", line):
            free.extend(parse_braced_sets(line))
    return core, free


def main() -> None:
    # Generic construction edge cases (not used by the r=11 proof).
    require(construct(5, {}) == {}, "empty profile should construct the empty family")
    level_zero = construct(5, {0: 1})
    require(
        level_zero == {0: [frozenset()]},
        f"unexpected level-0 construction: {level_zero}",
    )
    print("[OK] generic empty-profile and level-0 construction edge cases")

    require(
        n0_upper_scan(11, 0) == 24,
        "the inclusive scan window [2r+2,2r+2] should test n=24",
    )
    print("[OK] finite-scan endpoint convention")

    n, r = 27, 11

    # Upper bound: the only possible 24-level profile fails by one pair.
    full_ok, full_m = profile_test(n, full_profile(n, r))
    require(not full_ok, "the 24-level profile unexpectedly became feasible")
    require(full_m[2] == 352, f"expected m_2=352, found {full_m[2]}")
    print("[OK] n=27, r=11 full profile is infeasible: m_2=352 > 351")

    # Lower bound: construct 11 sets on each of levels 2,...,24.
    profile_23 = {i: r for i in range(2, 25)}
    profile_23_ok, profile_23_m = profile_test(n, profile_23)
    require(profile_23_ok, "the 23-level certificate profile is infeasible")
    require(profile_23_m[2] == 327, f"expected m_2=327, found {profile_23_m[2]}")
    family_23 = construct(n, profile_23)
    require(family_23 is not None, "failed to construct the 23-level family")
    errors = check_antichain_profile(family_23, n, r, set(profile_23))
    require(not errors, f"23-level family failed direct checking: {errors[:3]}")
    require(sum(map(len, family_23.values())) == 253, "unexpected 23-level family size")
    print("[OK] explicit 23-level family: 253 sets, no containments")

    # A direct full-profile construction at n=28.
    family_28 = construct(28, full_profile(28, r))
    require(family_28 is not None, "failed to construct the n=28 full profile")
    errors = check_full_witness(family_28, 28, r)
    require(not errors, f"n=28 family failed direct checking: {errors[:3]}")
    print("[OK] explicit n=28 full-profile family: 275 sets, no containments")

    # Base core and the free sets used by the padding theorem.
    q, s = 16, 13
    core = construct(q, core_profile(s, r))
    require(core is not None, "the r=11 base core is infeasible")
    errors = check_antichain_profile(core, q, r, set(range(2, s + 1)))
    require(not errors, f"base core failed direct checking: {errors[:3]}")
    free = free_sets(core, q, s - 1, 10**9)
    require(len(free) == 88, f"expected 88 free 12-sets, found {len(free)}")
    print("[OK] base core q=16, s=13 and its 88 free 12-sets")

    # Audit the on-disk core and its explicitly listed padding sets without
    # regenerating either from the profile code.
    core_path = ROOT / "certificates" / "r11_core_and_free_sets.txt"
    disk_core, disk_free = parse_core_certificate(core_path)
    errors = check_antichain_profile(disk_core, q, r, set(range(2, s + 1)))
    require(not errors, f"on-disk base core failed checking: {errors[:3]}")
    require(sum(map(len, disk_core.values())) == 132, "on-disk core should have 132 sets")
    require(len(disk_free) == r, f"expected {r} listed free sets, found {len(disk_free)}")
    require(len(set(disk_free)) == r, "listed free sets are not distinct")
    require(all(len(member) == 12 for member in disk_free), "a listed free set is not a 12-set")
    disk_members = [member for layer in disk_core.values() for member in layer]
    require(
        all(not any(member <= candidate for member in disk_members) for candidate in disk_free),
        "a listed free set contains a core member",
    )
    print("[OK] on-disk 132-set core and 11 explicitly listed free 12-sets")

    # Three explicit padding stages and the resulting n=28,...,33 witnesses.
    stage_cores = [(core, q, s)]
    for _ in range(3):
        core, q, s = pad_core(core, q, s, r)
        errors = check_antichain_profile(core, q, r, set(range(2, s + 1)))
        require(not errors, f"padded core failed direct checking: {errors[:3]}")
        stage_cores.append((core, q, s))

    for current_n in range(28, 34):
        needed_s = current_n // 2 - 1
        candidates = [
            (candidate, candidate_q, candidate_s)
            for candidate, candidate_q, candidate_s in stage_cores
            if candidate_s >= needed_s and candidate_q <= current_n - 1 - r
        ]
        require(candidates, f"no padded core available for n={current_n}")
        candidate, candidate_q, _ = candidates[0]
        family = full_from_core(candidate, candidate_q, r, current_n)
        errors = check_full_witness(family, current_n, r)
        require(not errors, f"padded witness n={current_n} failed: {errors[:3]}")
    print("[OK] three padding stages and full witnesses for n=28,...,33")

    # Check every explicit witness shipped in the larger certificate file.
    witness_path = ROOT / "certificates" / "2r_plus_6_r_11_to_20.txt"
    parsed = list(parse_witness_file(str(witness_path)))
    require(len(parsed) == 10, f"expected 10 supplied witnesses, found {len(parsed)}")
    for witness_r, witness_n, family in parsed:
        errors = check_full_witness(family, witness_n, witness_r)
        require(not errors, f"supplied witness r={witness_r} failed: {errors[:3]}")
    print("[OK] supplied full-profile witnesses for r=11,...,20")

    # Check the generated on-disk r=11 lower-bound certificate as well.
    lower_path = ROOT / "certificates" / "r11_n27_23_levels.txt"
    parsed_lower = list(parse_witness_file(str(lower_path)))
    require(len(parsed_lower) == 1, "could not parse the 23-level certificate")
    lower_r, lower_n, lower_family = parsed_lower[0]
    errors = check_antichain_profile(lower_family, lower_n, lower_r, set(range(2, 25)))
    require(not errors, f"on-disk 23-level certificate failed: {errors[:3]}")
    print("[OK] on-disk r=11, n=27, 23-level certificate")

    print("ALL RELEASE CHECKS PASSED")


if __name__ == "__main__":
    main()
