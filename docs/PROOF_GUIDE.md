# Guide to reading the proof

## The result and threshold convention

For an integer `r >= 2`, let `g(n,r)` be the maximum number of distinct set
sizes represented by an antichain of subsets of an `n`-element set, under the
condition that every represented size occurs at least `r` times.  The
threshold `n_0(r)` is the least integer `N` such that

$$
g(n,r)=n-3\qquad\text{for every }n>N.
$$

The package's threshold table is

$$
 n_0(r)=
 \begin{cases}
 3,&r=2,\\
 8,&r=3,\\
 2r+4,&4\le r\le10,\\
 2r+5,&r\ge11.
 \end{cases}
$$

The values `r=2,3` are cited from He--Tang.  Lean proves the original least
threshold, including its strict `n>N` convention, for every `r>=4`.  The
original-formulation declaration is
`Erdos776.Uniform.erdos776_threshold`; the internal extremal-function
declaration is `Erdos776.Uniform.isErdosThreshold_of_ge_4`.

## One-page dependency diagram

```text
Erdős Problems #776 wording
        |
        | ProblemStatement.lean: explicit equivalence lemmas
        v
IsMultiplicityAntichain / occupiedLevels / extremalOccupiedLevels
        |
        v
FullMiddleProfileExists  <---- asymmetric profile criterion
        |                       necessity: at least profile => capacities
        |                       sufficiency: capacities => exact colex profile
        |
        +---------------------------+------------------------------+
        |                                                          |
  4 <= r <= 10                                                r >= 11
  native finite checks                              lower window  +  L4
  - fail at 2r+4                                  capacities/e<=6   e>=1
  - fit at 2r+5                              (direct finite interface at 11..28)
  - core fits                                                     |
                                                                  v
                                                           upper-core data
                                                   a_b <= C(r+4,b), b >= 4
                                                   a_3 = C(r+4,3) + e
                                                          1 <= e <= 6
        |                                                          |
        |                                  +-----------------------+------------------+
        |                                  |                                          |
        |                            e >= 1 + no-carry                         e <= 6
        |                            diagonal shell transfer                  core fits
        |                                  |                                          |
        |                         failure at n=2r+5                       punctured top sets
        |                                                                            |
        +-------------------- feasible canonical core -------------------------------+
                                         |
                              persistent two-point padding
                                         |
                                    core-to-full
                                         |
                             every ground size above threshold
```

For `r>=29`, lower-window feasibility and L4 derive the upper-core data.  For
`11<=r<=28`, Lean certifies the upper-core data and the final overflow
directly.  This keeps finite computation isolated without weakening the
semantic final theorem.

## Carry-centered conceptual proof for `r>=11`

Put `A=r+4` and run the constant upper-core recurrence `a_b`.  The main
interface is

$$
a_b\le\binom Ab\quad(4\le b\le r+2),\qquad
a_3=\binom A3+e,\qquad 1\le e\le6.
$$

Everything after this interface is short.

1. Lower-window feasibility, after complementation, gives the upper
   capacities and the bound `e<=6`.
2. L4 rules out zero carry and gives `e>=1`.
3. Positive carry enters the full recurrence on `2r+5` points through a
   no-carry diagonal binomial shell.  The residual dominates L4 and eventually
   overflows capacity.
4. The bound `e<=6` makes the same constant core feasible on `r+5` points.
5. Each displayed top core member `T_j` can be punctured at a common point:
   `D_j=T_j\{1}`.  If a core member lay inside `D_j`, antichainness against
   `T_j` would force equality with `T_j`, impossible because `D_j` is proper.
6. The `D_j` are persistent free sets.  Two-point padding constructs larger
   cores indefinitely, and the core-to-full construction handles both
   parities of the final ground-set size.

The quantity `alpha_r` remains a useful interpretation of the lower and
upper windows, but it is not needed in the main logical interface.

## Lower-window segment table

The symbolic lower-window proof for `r>=378` is long only because it gives an
explicit capacity-bounded supersolution.  Read it as the following stitched
segments.  Here `t` is the maximal anchor index and `K=phaseCount r t`.

| Segment | Levels | State | Transition theorem | Capacity theorem | Lean module |
|---|---|---|---|---|---|
| Exact anchors | `r+1` down to `r-t` | `anchorValue r q` | `anchorValue_step` | `lowerWindowChain_fit_anchor_segment` | `LowerWindow/Anchors.lean` |
| Completed anchor | level `r-t-1` and entry to phase 1 | `completedAnchorValue r t` | `lowerWindowChain_le_completedAnchor`, `completedAnchor_to_phase_one` | `completedAnchorValue_lt_capacity` | `Anchors.lean`, `PhaseStart.lean` |
| Ordinary phases | each `phaseBirth r t j` down by `phaseExtensionCount r t j`, including harvest bridges | `phaseState r t j L` | `phase_extension_pays`, `phase_harvest_valid`; stitched by `phase_extension_segment` and `ordinary_harvest_segment` | `phaseState_lt_capacity` | `PhaseTransitions.lean`, `PhaseHarvest.lean`, `PhaseCapacity.lean`, `FullEnvelope.lean` |
| Rising tail | final harvest through `risingLevel r t 2` | `risingState r t p` | `risingState_step`, `risingState_final_step` | `risingState_lt_capacity` | `RisingTail.lean`, `FullEnvelope.lean` |
| Generalized envelope | `t+K+4` down to `t+5` | `generalizedEnvelopeState r t i` | `generalizedEnvelope_step` | `generalizedEnvelopeState_lt_capacity` | `GeneralizedEnvelope.lean`, `FullEnvelope.lean` |
| Scalar collision | `t+5` to `t+4` | envelope state to `scalarState r t 0` | `generalizedEnvelope_collision` | endpoint capacities in `envelope_collision_segment` | `ScalarStates.lean`, `FullEnvelope.lean` |
| Scalar collapse | `t+4` down to `4` | `scalarState r q (scalarResidual t q)` | `scalarState_step_auto` | `scalarState_lt_capacity` | `ScalarCollapse.lean`, `ScalarStates.lean`, `FullEnvelope.lean` |
| Final levels | `4` to `3` to `2` | `finalFourState`, `finalThreeState` | `finalFourState_scalar_step`, `finalThreeState_step`, `finalScalar_bottom` | `finalThreeState_le_capacity`, tight level-two theorem | `FinalLevels.lean`, `PhaseAssembly.lean` |

`hasLowerWindowPhaseEnvelope` stitches the middle seven rows;
`lowerWindowFits_of_ge_378` joins them to the exact anchors and final levels.

The numerical finite base ends at `r=377`, just below `T_1=378`. The seam
samples `r=378,379` exercise only the first anchor regime `t=1`; the second
regime starts at `T_2=70,500`. All higher anchor regimes are covered by the
symbolic Lean proof rather than by numerical sampling.

## Range-by-range verification

| Range | Obstruction | Construction | Lean computation status | Independently implemented Python check |
|---|---|---|---|---|
| `4<=r<=10` | Direct level-two overflow at `2r+4` | Direct fit at `2r+5`; checked core plus symbolic padding thereafter | Seven-value `native_decide` certificate | `verification/verify_small_r_exact.py` |
| `11<=r<=28` | Direct full-profile level-two overflow at `2r+5` | Direct upper-core carry certificate, then symbolic core/padding | Eighteen-value `native_decide` certificate | L4, lower-window, and assembly scripts |
| `29<=r<=377` | Symbolic L4 and diagonal transfer | Ground-bounded lower-window certificate, then symbolic carry/core/padding | 349-value `native_decide` certificate | `verification/verify_lower_window_base.py` |
| `r>=378` | Symbolic L4 and diagonal transfer | Fully symbolic lower-window, carry, core, and padding | No finite certificate | Formula and seam stress tests only |
| `r=2,3` | Not formalized here | Not formalized here | External cited results | He--Tang source |

## What Lean verifies

Lean verifies:

- the published-statement-to-internal correspondence;
- the minimum-shadow/canonical-cascade bridge;
- necessity for profiles specified by lower bounds and sufficiency for exact
  profiles;
- L4 for actual antichains in its symbolic range;
- the symbolic lower-window supersolution;
- the carry reflection, free core, puncturing argument, persistent padding,
  core-to-full construction, and diagonal-shell obstruction;
- all finite-range checker soundness theorems;
- the original finite maximum `g(n,r)` and least threshold convention;
- the piecewise threshold for every `r>=4`.

The purely symbolic endpoint `isErdosThreshold_of_ge_378` has only the usual
Lean/mathlib axioms `propext`, `Classical.choice`, and `Quot.sound`.

## What remains externally computed

No Python result is a logical premise of the Lean theorem for `r>=4`.
The finite checker definitions and their semantic soundness bridges are
ordinary Lean definitions and proofs. Three closed finite propositions are
then evaluated with `native_decide`; consequently the full endpoint also
trusts Lean's native evaluator/compiler for those computations.

The independently implemented Python programs and stored witnesses remain
valuable falsification and reproducibility checks. The values `r=2,3` remain
cited from He--Tang rather than formalized in this repository.

## Exact reproduction commands

```bash
lake exe cache get
lake build --wfail
python3 tests/verify_all.py
python3 tools/check_lean_placeholders.py
python3 tools/check_github_math.py
python3 tools/check_axiom_audit.py
./paper/build_pdf.sh
```

The PDF command additionally requires Pandoc, XeLaTeX, and the fonts listed
in `paper/build_pdf.sh`.

## Recommended human review targets

1. `Erdos776/Uniform/ProblemStatement.lean`: check the translation from the
   published problem statement and the strict threshold convention.
2. `ProfileNecessity.lean`, `ProfileSufficiency.lean`, and
   `ProfileCriterion.lean`: check the asymmetric profile theorem.
3. `BoundedShadow.lean`: check that the executable bounded evaluator equals
   `canonicalShadow` under capacity.
4. The three finite certificate definitions and their soundness theorems.
5. `L4/Profile.lean` and `DiagonalObstruction.lean`: check the symbolic
   obstruction and no-carry shell argument.
6. `CoreCarry.lean`, `FreeCore.lean`, `Padding.lean`, and `CoreToFull.lean`:
   check the construction chain.
7. The lower-window segment seams in `FullEnvelope.lean` and final assembly in
   `PhaseAssembly.lean`.

Independent specialist peer review has not yet occurred. Separate adversarial
AI review passes are not treated as a substitute for it.
