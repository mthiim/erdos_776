#!/usr/bin/env python3
"""Run `#print axioms` and enforce the project's exact trust allowlist."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_FILE = ROOT / "lean" / "AxiomAudit.lean"

STANDARD = {"propext", "Classical.choice", "Quot.sound"}
LOWER_NATIVE = (
    "Erdos776.Uniform.lowerWindowFiniteBaseCheck_verified"
    "._native.native_decide.ax_1_1"
)
UNIFORM_NATIVE = (
    "Erdos776.Uniform.smallUniformFiniteCheck_verified"
    "._native.native_decide.ax_1_1"
)
SMALL_NATIVE = (
    "Erdos776.Uniform.smallThresholdFiniteCheck_verified"
    "._native.native_decide.ax_1_1"
)
ALL_NATIVE = {LOWER_NATIVE, UNIFORM_NATIVE, SMALL_NATIVE}

EXPECTED: dict[str, set[str]] = {
    "Erdos776.L4.l4_multiplicity_profile_infeasible": STANDARD,
    "Erdos776.Uniform.isErdosThreshold_of_ge_378": STANDARD,
    "Erdos776.Uniform.lowerWindowFiniteBaseCheck_verified": {LOWER_NATIVE},
    "Erdos776.Uniform.smallUniformFiniteCheck_verified": {UNIFORM_NATIVE},
    "Erdos776.Uniform.smallThresholdFiniteCheck_verified": {SMALL_NATIVE},
    "Erdos776.Uniform.isErdosThreshold_of_ge_4": STANDARD | ALL_NATIVE,
    "Erdos776.Uniform.erdos776_threshold": STANDARD | ALL_NATIVE,
}

BLOCK = re.compile(r"'([^']+)' depends on axioms: \[(.*?)\]", re.DOTALL)


def parse_axioms(output: str) -> dict[str, set[str]]:
    parsed: dict[str, set[str]] = {}
    for declaration, body in BLOCK.findall(output):
        parsed[declaration] = {
            item.strip() for item in body.split(",") if item.strip()
        }
    return parsed


def main() -> int:
    lake = shutil.which("lake")
    if lake is None:
        elan_lake = Path.home() / ".elan" / "bin" / "lake"
        if elan_lake.is_file():
            lake = str(elan_lake)
        else:
            print("lake was not found on PATH or under ~/.elan/bin", file=sys.stderr)
            return 127

    command = [lake, "env", "lean", str(AUDIT_FILE.relative_to(ROOT))]
    print("$", " ".join(command), flush=True)
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    print(result.stdout, end="")
    if result.returncode:
        return result.returncode

    parsed = parse_axioms(result.stdout)
    failures: list[str] = []
    for declaration, expected in EXPECTED.items():
        if declaration not in parsed:
            failures.append(f"missing audit output for {declaration}")
            continue
        actual = parsed[declaration]
        if actual != expected:
            failures.append(
                f"{declaration}: expected {sorted(expected)}, got {sorted(actual)}"
            )

    unexpected_declarations = set(parsed) - set(EXPECTED)
    if unexpected_declarations:
        failures.append(
            "unexpected audited declarations: "
            + ", ".join(sorted(unexpected_declarations))
        )

    if failures:
        print("\nAXIOM AUDIT FAILED", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1

    print("Axiom audit passed: symbolic endpoints use only the three standard")
    print("axioms, and the final endpoints additionally use exactly the three")
    print("disclosed native_decide certificate axioms.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
