# Lean formalization

The project is pinned by `lean-toolchain`, `lakefile.lean`, and
`lake-manifest.json`. Build it with:

```bash
lake exe cache get
lake build --wfail
```

## Final endpoint

Lean proves the original least threshold for every `r>=4`:

```lean
theorem Erdos776.Uniform.isErdosThreshold_of_ge_4
    (r : ℕ) (hr : 4 ≤ r) :
    IsErdosThreshold r (erdosThresholdFromFour r)
```

The piecewise value is `2*r+4` for `r<=10` and `2*r+5` otherwise.

`Erdos776/Uniform/ProblemStatement.lean` restates the condition in the
language of Erdős Problems #776 and proves:

```lean
theorem Erdos776.Uniform.erdos776_threshold
    (r : ℕ) (hr : 4 ≤ r) :
    ProblemThreshold r (erdosThresholdFromFour r)
```

See `PROBLEM_STATEMENT_CORRESPONDENCE.md` for the short statement audit and
`THEOREM_CROSSWALK.md` for the paper-to-Lean map.

## Trust boundary by range

| Range | Lean route |
|---|---|
| `4<=r<=10` | One native certificate checks failure at `2r+4`, fit at `2r+5`, and core feasibility; semantic construction and leastness are proved symbolically. |
| `11<=r<=28` | One native certificate checks upper-core data and direct full-profile overflow; free core, padding, and leastness are symbolic. |
| `29<=r<=377` | One native ground-bounded lower-window certificate combines with symbolic L4 to derive the carry, obstruction, and construction. |
| `r>=378` | End-to-end symbolic lower window and L4, followed by carry, obstruction, construction, and leastness. |
| `r=2,3` | Not formalized here; cited from He--Tang. |

The full `r>=4` endpoint therefore reports three generated `native_decide`
certificate axioms and additionally trusts Lean's native evaluator/compiler.
The checker definitions and every bridge from checker success to the
mathematical statement are ordinary Lean definitions and proofs. The purely
symbolic endpoint `isErdosThreshold_of_ge_378` reports only `propext`,
`Classical.choice`, and `Quot.sound`. Run
`python3 tools/check_axiom_audit.py` for the executable audit.

## Main layers

### Canonical cascades and Kruskal--Katona

The modules under `Erdos776/Combinatorics/` prove:

- existence and uniqueness of the greedy binomial cascade;
- realization by a finite colex initial segment;
- agreement of its numerical shadow with mathlib's minimum shadow;
- `boundedShadow_eq_canonicalShadow`, connecting the executable
  ground-bounded evaluator to the mathematical recurrence.

### Asymmetric profile theorem

- `profileChain_isProfileRecurrence_of_antichain`: at least the prescribed
  multiplicities force every recurrence capacity;
- `profile_sufficiency`: fitting capacities construct an antichain with
  exactly the prescribed profile;
- `profile_criterion`: the exact-profile iff packaging.

### L4 and diagonal obstruction

- `l4_multiplicity_profile_infeasible`: semantic L4 for actual antichains,
  symbolic for `r>=29`;
- `canonicalShadow_diagonal_transfer`: the no-carry diagonal-shell identity;
- `fullProfileChain_overflows`: shell peeling plus the L4 residual forces
  overflow;
- `not_fullMiddleProfileExists_of_chain_overflow`: any exact recurrence
  overflow rules out the semantic full profile.

### Carry, core, and construction

- `HasUpperCoreData`: upper capacities together with `1<=e<=6`;
- `hasUpperCoreData_of_lowerWindowFeasible`: reflection and semantic L4 derive
  that data in the symbolic range;
- `explicitFreeFamily_isFree_of_isSperner`: the puncturing lemma for displayed
  top core members;
- `iteratedPaddingState_spec`: persistent two-point padding for an arbitrary
  number of stages;
- `coreToFull_fin`: the private-point/pivot construction and complemented
  upper half;
- `fullMiddleProfileExists_of_suitableFreeCore`: every `n>=2*r+6`, including
  both parity cases.

### Lower window

The symbolic proof under `Erdos776/Uniform/LowerWindow/` is assembled from
exact anchors, a completed anchor, ordinary phases, a rising tail, a
generalized envelope, scalar collision, scalar collapse, and final levels.
`hasLowerWindowPhaseEnvelope` stitches the segment theorems, and
`lowerWindowFits_of_ge_378` closes the symbolic range.

### Original problem statement

`OccupiedLevels.lean` and `GlobalThreshold.lean` define the actual finite
maximum `g(n,r)`, prove the singleton/complement reduction, identify the full
middle profile with `g(n,r)=n-3`, and prove leastness. `ProblemStatement.lean`
then makes the final correspondence explicit in the published problem's
existence language.

## Auditing

```bash
python3 tools/check_lean_placeholders.py
python3 tools/check_github_math.py
python3 tools/check_axiom_audit.py
```

`FORMALIZATION_STATUS.md` records the detailed scope and axiom boundary.
