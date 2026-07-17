#!/usr/bin/env python3
"""One-command verification for the complete-threshold proof package."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = [
    [sys.executable, str(ROOT / "tests" / "verify_r11.py")],
    [sys.executable, str(ROOT / "verification" / "verify_small_r_exact.py")],
    [sys.executable, str(ROOT / "verification" / "verify_l4.py")],
    [sys.executable, str(ROOT / "verification" / "verify_uniform_finite.py")],
    [sys.executable, str(ROOT / "verification" / "verify_lower_window_base.py")],
    # Independent exhaustive validation of the prescribed-profile criterion
    # against every antichain profile for n = 4, 5, 6.
    [sys.executable, str(ROOT / "computations" / "validate_profile_thm.py")],
]

for command in COMMANDS:
    print("\n$", " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)

print("\nALL COMPLETE-THRESHOLD RELEASE CHECKS PASSED")
