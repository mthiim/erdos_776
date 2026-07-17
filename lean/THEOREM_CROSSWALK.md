# Paper-to-Lean theorem crosswalk

This table maps the load-bearing mathematical statements to their Lean
declarations. “Native” means that an ordinary Lean checker and proved
soundness bridge are supplied with a closed Boolean result evaluated by
`native_decide`; this last evaluation additionally trusts Lean's native
evaluator/compiler.

| Paper result or interface | Lean declaration | Exact hypotheses / range | Status | Direct dependencies |
|---|---|---|---|---|
| Finite family of subsets | `Erdos776.Antichain.Family` | Any finite ground type | Definition | `Finset` |
| Antichain | `Erdos776.Antichain.IsSperner` | Any family | Definition | mathlib `IsAntichain (· ⊆ ·)` |
| Published multiplicity condition | `Erdos776.Uniform.IsMultiplicityAntichain` | Any `n,r` | Definition | `IsSperner`, `occupiedLevels`, `level` |
| Published wording equals internal condition | `problemAdmissible_iff_isMultiplicityAntichain` | Any `n,r,F` | Symbolic | elementary finite-set cardinality |
| Maximum `g(n,r)` | `extremalOccupiedLevels` | Any `n,r` | Definition | finite supremum over all families |
| Published target equals occupied-profile event | `problemTargetExists_iff_occupiedMiddleProfileExists` | Any `n,r` | Symbolic | problem-statement correspondence definitions |
| `n-3` occupied sizes equal full middle profile | `problemTargetExists_iff_fullMiddleProfileExists` | `4<=r`, `r+1<=n` | Symbolic | singleton/complement reduction |
| Exact threshold convention | `ProblemThreshold`; internally `IsErdosThreshold` | Any `r,N` | Definitions | strict inequality `N<n` and leastness clause |
| At-least profile forces recurrence capacities | `profileChain_isProfileRecurrence_of_antichain` | Positive interval as instantiated | Symbolic | cumulative down-closures, Kruskal--Katona |
| Fitting recurrence constructs exact profile | `profile_sufficiency` | `1<=lo` and `IsProfileRecurrence` | Symbolic | canonical colex layers |
| Full profile event | `FullMiddleProfileExists n r` | Levels `2,...,n-2` | Definition | `IsSperner`, `HasMultiplicities` |
| L4 semantic obstruction | `Erdos776.L4.l4_multiplicity_profile_infeasible` | `29<=r` | Symbolic | cascade steps, reverse envelope, profile necessity |
| Exact lower-window capacity predicate | `LowerWindowFits r` | Any `r` | Definition | `lowerWindowChain`, `canonicalShadow` |
| Symbolic lower window | `lowerWindowFits_of_ge_378` | `378<=r` | Symbolic | anchors, phases, rising tail, envelope, scalar collapse |
| Finite lower window | `lowerWindowFits_of_ge_29_le_377` | `29<=r<=377` | Native | bounded-shadow checker and soundness theorem |
| Bounded evaluator correctness | `boundedShadow_eq_canonicalShadow` | `1<=k`, `m<=choose n k` | Symbolic | bounded greedy head equals canonical greedy head |
| Upper-core interface | `HasUpperCoreData r` | Capacities at `4,...,r+2`; `a_3=C+e`; `1<=e<=6` | Definition | `upperCoreChain` |
| Lower window plus L4 gives upper-core data | `hasUpperCoreData_of_lowerWindowFeasible` | `29<=r` plus semantic lower-window feasibility | Symbolic | complementation, reflected recurrence, semantic L4 |
| Direct finite upper-core data | `hasUpperCoreData_of_ge_11_le_28` | `11<=r<=28` | Native | constant-profile checker |
| Punctured top sets are free | `explicitFreeFamily_isFree_of_isSperner` | Canonical core is an antichain | Symbolic | `coreTopSet_mem_canonicalCore`, proper deletion |
| Upper-core data gives suitable free core | `hasSuitableFreeCore_of_upperCoreData` | `1<=r`, `HasUpperCoreData r` | Symbolic | core recurrence, puncturing |
| Direct feasible recurrence gives suitable core | `hasSuitableFreeCore_of_recurrence` | Exact core `IsProfileRecurrence` | Symbolic | canonical core and puncturing |
| Suitable core gives all later profiles | `fullMiddleProfileExists_of_suitableFreeCore` | `2*r+6<=n` | Symbolic | persistent padding, parity decomposition, core-to-full |
| No-carry diagonal shell transfer | `canonicalShadow_diagonal_transfer` | Residual below shell capacity | Symbolic | canonical cascade concatenation |
| Upper carry obstructs `2r+5` | `not_fullMiddleProfileExists_of_upperCoreData` | `29<=r`, `HasUpperCoreData r` | Symbolic | diagonal transfer, residual L4 comparison |
| Any exact recurrence overflow obstructs | `not_fullMiddleProfileExists_of_chain_overflow` | Overflow at a level in `2,...,n-2` | Symbolic | profile necessity |
| Direct finite obstruction | `not_fullMiddleProfileExists_of_ge_11_le_28` | `11<=r<=28` | Native | level-two overflow checker soundness |
| Uniform full-profile threshold | `fullMiddleProfileThreshold_of_ge_11` | `11<=r` | Mixed | finite `11..28`; finite/symbolic lower-window split above 29 |
| Small-range threshold | `fullMiddleProfileThresholdAt_of_ge_4_le_10` | `4<=r<=10` | Native plus symbolic construction | bad/good/core checker, profile sufficiency, padding |
| Least threshold for all `r>=4` | `isErdosThreshold_of_ge_4` | `4<=r` | Mixed | small-range and uniform threshold theorems |
| Original-formulation last failure | `erdos776_lastFailure` | `4<=r` | Mixed | full-profile thresholds and correspondence lemmas |
| Original-formulation final theorem | `erdos776_threshold` | `4<=r` | Mixed | last failure implies least eventual threshold |

## Most important translation points

### `IsMultiplicityAntichain`

This says exactly that the family is an antichain and that every occupied
level contains at least `r` members. `ProblemStatement.lean` restates the
published problem's “if there exists a set of size `t`” wording and proves
equivalence.

### `extremalOccupiedLevels`

This is the finite maximum of `(occupiedLevels F).card` over every admissible
family on `Fin n`.  Invalid families contribute zero to the finite supremum.

### `FullMiddleProfileExists`

This is a semantic existence statement about an actual family on `Fin n`,
not a numerical recurrence.  It requests at least `r` members at every level
`2,...,n-2`.

### `LowerWindowFits`

This is the exact capacity statement for the canonical lower-window
recurrence.  For `r>=29`, it is converted symbolically into upper-core data,
the canonical free core, all later constructions, and the obstruction.

### `HasUpperCoreData`

This is the carry-centered interface:

```text
a_b <= choose (r+4) b       for 4 <= b <= r+2
a_3 = choose (r+4) 3 + e
1 <= e <= 6
```

It cleanly separates the long lower-window/L4 input from the short
obstruction and construction arguments.

### `IsErdosThreshold`

Its first clause says `g(n,r)=n-3` for every strict successor `N<n`; its
second says `N` is least among all integers with that eventual-success
property. `ProblemThreshold` states the same convention directly in terms
of existence of families satisfying the published formulation.
