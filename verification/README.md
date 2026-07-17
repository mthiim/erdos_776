# Verification

The Python suite provides independently implemented falsification and
reproducibility support. No Python output is a logical premise of the Lean
theorem for `r>=4`.

For the complete formal audit, run:

```bash
lake exe cache get
lake build --wfail
python3 tests/verify_all.py
python3 tools/check_lean_placeholders.py
python3 tools/check_github_math.py
python3 tools/check_axiom_audit.py
```

Lean uses three closed `native_decide` certificates for `4<=r<=10`,
`11<=r<=28`, and `29<=r<=377`. The checker definitions and soundness bridges
are ordinary Lean definitions and proofs; evaluating the three closed Boolean
propositions additionally trusts Lean's native evaluator/compiler. The range
`r>=378` is end-to-end symbolic and has the smaller standard Lean/mathlib
trust boundary.

Here L4 denotes the profile with $r$ members at every level
$2,\ldots,r+1$ on an $(r+4)$-point ground set.

Run the combined checks from the repository root:

```bash
python3 tests/verify_all.py
```

The scripts have different logical roles:

- `verify_small_r_exact.py` provides an independently implemented exact
  cross-check of all finite ingredients supporting `n_0(r)=2r+4` for every
  `4<=r<=10`. It imports none of the project proof code, recomputes the exact
  Kruskal--Katona recurrences, parses and directly checks all stored
  witnesses/cores/free sets, and exercises the persistent padding
  construction.
- `verify_lower_window_base.py` is the exact finite base used in the
  lower-window proof, for every `11<=r<=377`.  It also contains named
  regression checks at `r=377,378,379`, across the finite/symbolic seam.
- `verify_l4.py` checks the exact L4 base `11<=r<=28`, including the stronger
  statement that the first failure is exactly
  `m_2 = binom(r+4,2)+1`, and stress-tests the symbolic reverse-envelope
  formulas.
- `verify_uniform_finite.py` is a supplementary exact assembly cross-check;
  it is not a replacement for the all-`r` symbolic proof.
- `tests/verify_r11.py` directly checks the stored `r=11` certificates,
  core, free sets, and padding witnesses.
  `computations/validate_profile_thm.py` separately enumerates every antichain
  profile for `n=4,5,6` and checks exhaustive agreement with the
  prescribed-profile criterion. It is included in `tests/verify_all.py`.
