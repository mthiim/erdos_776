# Formalization status and trust boundary

## Final theorem for every `r >= 4`

The published-formulation endpoint proves the original semantic least-threshold
statement for actual antichains:

```lean
theorem Erdos776.Uniform.erdos776_threshold
    (r : ℕ) (hr : 4 ≤ r) :
    ProblemThreshold r (erdosThresholdFromFour r)
```

Here `erdosThresholdFromFour r` is `2*r+4` for `4 <= r <= 10` and
`2*r+5` for `r >= 11`. `ProblemThreshold` includes the strict convention
`n > N` and leastness of `N`. Its equivalent internal endpoint is:

```lean
theorem Erdos776.Uniform.isErdosThreshold_of_ge_4
    (r : ℕ) (hr : 4 ≤ r) :
    IsErdosThreshold r (erdosThresholdFromFour r)
```

## Trust boundary by parameter range

| Range | Lean route | Additional trust beyond the symbolic proof |
|---|---|---|
| `4 <= r <= 10` | Failure at `2*r+4`, first fit at `2*r+5`, and core feasibility are connected to the semantic threshold theorem by proved bridges. | One closed `native_decide` evaluation. |
| `11 <= r <= 28` | Upper-core data and direct full-profile overflow feed the symbolic free-core, padding, construction, and leastness theorems. | One closed `native_decide` evaluation. |
| `29 <= r <= 377` | A ground-bounded lower-window check feeds symbolic L4, carry, obstruction, construction, and leastness. | One closed `native_decide` evaluation. |
| `r >= 378` | Lower window, L4, carry, obstruction, construction, and leastness are all symbolic. | None beyond Lean/mathlib's standard axioms. |

No Python result or stored witness is a logical premise of a Lean theorem.

## Axiom audit

The Lean sources contain no `sorry`, `admit`, or project `axiom`
declarations. `#print axioms` on the symbolic endpoint
`isErdosThreshold_of_ge_378` reports only `propext`, `Classical.choice`, and
`Quot.sound`. The complete endpoints `isErdosThreshold_of_ge_4` and
`erdos776_threshold` additionally report the three generated native-evaluation
axioms belonging to the closed finite certificates. The checker definitions
and every bridge from checker success to the recurrence, antichain, and
least-threshold statements are ordinary Lean definitions and proofs.

The executable audit is maintained in `lean/AxiomAudit.lean` and checked by
`python3 tools/check_axiom_audit.py`.

## External cases `r = 2,3`

The values `n_0(2)=3` and `n_0(3)=8`, attributed to Yixin He and Quanyu Tang,
are cited but not formalized in this repository. Consequently, Lean proves
the complete claimed threshold table from `r=4` onward; the two smaller cases
remain external mathematical inputs to the table stated in the paper.

## Detailed theorem inventory and development record

The Lean sources under `Erdos776/` contain no `sorry`, `admit`, or custom
axiom. They now prove the following statements; the three closed finite
evaluations use the explicitly disclosed native trust boundary described at
the end of this document.

1. a numerical canonical-cascade representation and concrete finite family;
2. termwise shadowing of that family (`shadow_cascadeFamily`);
3. that the family is a colex initial segment and transports losslessly to
   subsets of `Fin n`;
4. using mathlib's Kruskal--Katona theorem, that a canonical cascade realizes
   the minimum numerical shadow (`kkShadow_eq_cascadeShadowValue`);
5. global monotonicity of `kkShadow`;
6. every cascade calculation in Lemma RS, including all parametric ranges
   (`l4_reverseSteps`);
7. all three top calculations in Lemma L4-T (`l4_topStepIdentities`);
8. Lemma IND, the final corrector margin including `r=29,30`, and the concrete
   recurrence contradiction (`l4_no_recurrence`);
9. the necessary half of the prescribed-profile theorem, by forming the
   cumulative down-closure levels of an arbitrary finite antichain and
   applying Kruskal--Katona at each shadow step
   (`l4_profile_forces_recurrence`);
10. the semantic L4 theorem for actual antichains, in the stronger
    at-least-`r` formulation (`l4_multiplicity_profile_infeasible`).

The reusable construction modules additionally prove:

11. generic finite antichain, level-multiplicity, free-family, and embedding
    transport lemmas (`Combinatorics/Antichain.lean`);
12. the two-point padding lemma, including the next occupied level and a
    same-cardinality persistent free family
    (`twoPointPadding_with_persistent_free`);
13. indefinite persistence for every finite number of padding stages
    (`iteratedPaddingState_spec`), rather than an inference from sampled
    stages;
14. the core-to-full lemma: private pairs and pivoted core members form the
    lower antichain, its complements form the upper levels, and the cross-side
    containments are impossible (`coreToFull_fin`).

The general prescribed-profile layer now also proves:

15. existence and uniqueness of the greedy canonical binomial cascade for
    every natural value at every positive lower index
    (`CascadeNormalForm.lean`, `canonicalDigits_unique`);
16. agreement of its ground-independent numerical shadow with the minimum
    finite-family shadow whenever the requested family cardinality is
    feasible (`kkShadow_eq_canonicalShadow`);
17. the sufficiency construction: nested colex segments minus the shadows from
    above form an antichain with exactly the requested profile
    (`profile_sufficiency`);
18. the complete prescribed-profile iff criterion, combining the generic
    necessity and sufficiency directions (`profile_criterion`).

The Section 16 obstruction layer now proves:

19. the exact diagonal cascade transfer identity (16.1), including its
    one-shell specialization (`canonicalShadow_diagonal_transfer`,
    `canonicalShadow_add_shell`);
20. the ground-independent L4 recurrence itself exceeds capacity at level 2,
    by comparison with the already formalized finite L4 recurrence
    (`canonicalL4Chain_bottom_gt`);
21. the upper-shell formula (16.2a), the residual recurrence (16.3), its L4
    lower bound (16.4), and the complete carry/no-carry shell-peeling
    contradiction (`fullProfileChain_overflows`);
22. the semantic antichain obstruction on `Fin (2*r+5)`, with the
    computation isolated behind the exact upper-core capacity and carry
    facts used in the manuscript
    (`upperCore_fit_full_multiplicity_profile_infeasible`).

The uniform assembly layer now also proves:

23. a suitable free core on `r+5` points yields a full middle-profile
    antichain for every `n >= 2*r+6`; the proof performs arbitrary persistent
    padding, resolves the even/odd remainder internally, invokes
    `coreToFull_fin`, and transports to `Fin n`
    (`fullMiddleProfileExists_of_suitableFreeCore`);
24. the requested conditional end-to-end theorem: upper-core data plus a
    suitable free core imply obstruction at `2*r+5` and construction at every
    later size (`uniform_profile_threshold_from_components`).

The Section 15 free-core layer now proves:

25. the complete constant core recurrence fits on `r+5` points using only the
    upper-core capacity data and `1 <= e <= 6`
    (`upperCoreChain_is_core_recurrence`);
26. the first `r` top-level members of the canonical colex core are the
    displayed sets `X \ {j}`; this is derived from an explicit diagonal
    cascade, not assumed from informal colex intuition
    (`coreTopSet_mem_canonicalCore`);
27. the `r` sets `D_j = (X \ {j}) \ {0}` are distinct, have size `r+1`,
    and are free for the entire core. Freeness follows because each `D_j` is
    strictly contained in its corresponding top core member and the core is
    an antichain (`hasSuitableFreeCore_of_upperCoreData`);
28. consequently, upper-core data is now the sole remaining hypothesis of
    the symbolic full-middle-profile threshold
    (`fullMiddleProfileThreshold_of_upperCoreData`).

The core-carry/reflection layer now proves:

29. a semantic lower-window witness may equivalently be supplied by the exact
    canonical recurrence capacity predicate used by the checker and symbolic
    supersolution (`LowerWindowFits`, `lowerWindowFeasible_of_fits`);
30. complementing an actual lower-window antichain produces the reflected
    profile, and its canonical recurrence agrees with the upper core at every
    level `4,...,r+2`
    (`reflectedWindowChain_isProfileRecurrence_of_lowerWindow`);
31. reflected level-three capacity gives the upper-core fit and carry bound
    `e <= 6` (`upperCoreChain_three_le_of_lowerWindow`);
32. a zero carry would make the reflected constant profile feasible;
    complementing its colex witness would produce the semantic L4 profile,
    so L4 forces `e >= 1` (`upperCoreChain_three_gt_of_fit`);
33. hence lower-window feasibility supplies `HasUpperCoreData`, and all later
    obstruction, free-core, padding, and assembly results follow
    (`hasUpperCoreData_of_lowerWindowFeasible`,
    `fullMiddleProfileThreshold_of_lowerWindowFits`).

The occupied-level/global-threshold layer now proves:

34. if level one occurs then every other member avoids the occupied singleton
    points, giving at most `n-r` occupied levels; complementation proves the
    dual statement for level `n-1` (`OccupiedLevels.lean`);
35. for `r >= 4`, every multiplicity antichain has at most `n-3` occupied
    levels, and equality forces exactly levels `2,...,n-2`
    (`occupiedLevels_eq_middle_of_card`);
36. attaining `n-3` occupied levels is equivalent to the semantic full-middle
    profile (`occupiedMiddleProfileExists_iff_fullMiddleProfileExists`);
37. the actual finite extremal maximum `extremalOccupiedLevels n r` (the
    paper's `g(n,r)`) is defined, and its equality to `n-3` is equivalent to
    the full-middle profile;
38. `IsErdosThreshold r N` expresses leastness, and the assembled profile
    threshold implies that `2*r+5` is this least threshold
    (`isErdosThreshold_of_fullMiddleProfileThreshold`).

The lower-window supersolution layer now additionally proves:

39. the generic supersolution comparison principle for the exact canonical
    recurrence (`lowerWindowFits_of_supersolution`);
40. the threshold ladder `T_q`, its displayed initial values, unboundedness,
    the maximal anchor index, `T_t >= 128*t+250`, and
    `r >= 64*(2*t+3)` (`LowerWindow/Parameters.lean`);
41. the displayed anchor lists are canonical cascades, every state in Lemma
    3.1 agrees with the actual recurrence, all exact anchors fit, and the
    additional rounded anchor dominates the next exact state
    (`LowerWindow/Anchors.lean`);
42. the scalar collapse in Lemma 10.2, including its quadratic invariant and
    exact terminal values `1,4,6`, without the Python checker
    (`LowerWindow/ScalarCollapse.lean`);
43. the level-four, level-three, and tight level-two identities of Section 11
    (`LowerWindow/FinalLevels.lean`);
44. the least phase count, all phase positions, slot identities, no-gap birth
    recurrence, and the uniform payment estimates used in Sections 4--6
    (`PhaseParameters.lean`, `PhasePositions.lean`, `PhaseBounds.lean`);
45. every ordinary phase is an actual canonical cascade, every extension and
    harvest evaluates through `canonicalShadow`, and every phase state fits
    its binomial capacity (`PhaseTransitions.lean`, `PhaseHarvest.lean`,
    `PhaseCanonical.lean`, `PhaseCapacity.lean`);
46. the completed-anchor entry and the entire one-digit rising tail, including
    its exceptional final jump, canonicity, and capacities (`PhaseStart.lean`,
    `RisingTail.lean`);
47. the generalized envelope, its exact recurrence, top seam, canonicity, and
    capacity bounds (`GeneralizedEnvelope.lean`);
48. the envelope-to-scalar collision and all semantic scalar states, including
    residual bounds, canonical digit lists, exact `canonicalShadow` steps, and
    capacities (`ScalarStates.lean`);
49. a reusable finite-segment comparison and stitching layer, followed by the
    complete assembly of the anchor, ordinary phases, final harvest, rising
    tail, envelope, collision, and scalar descent (`EnvelopeSegments.lean`,
    `FullEnvelope.lean`);
50. the formerly conditional proposition `HasLowerWindowPhaseEnvelope` for
    every `r >= 378`, with no mathematical hypotheses beyond maximal-anchor
    selection (`hasLowerWindowPhaseEnvelope`);
51. consequently, the exact lower-window fit, full middle-profile threshold,
    and least global Erdős threshold are unconditional throughout the symbolic
    range (`lowerWindowFits_of_ge_378`,
    `fullMiddleProfileThreshold_of_ge_378`,
    `isErdosThreshold_of_ge_378`).
52. a ground-bounded executable cascade shadow whose digit bound decreases
    after every selected digit; its head search and multiplicative binomial
    evaluator are proved equal to `Nat.choose` and the generic greedy cascade
    (`BoundedShadow.lean`);
53. a top-down Boolean lower-window checker which verifies capacity before
    every bounded shadow call, together with a proof that checker success
    implies the original mathematical `LowerWindowFits` predicate
    (`FiniteChecker.lean`, `lowerWindowCheck_sound`);
54. one isolated native certificate checks all 349 values `29 <= r <= 377`
    and is promoted through that soundness theorem
    (`lowerWindowFiniteBaseCheck_verified`,
    `lowerWindowFits_of_ge_29_le_377`);
55. the finite certificate and symbolic phase theorem meet at `377/378`,
    yielding unconditional full-profile and least global threshold theorems
    for every `r >= 29` (`fullMiddleProfileThreshold_of_ge_29`,
    `isErdosThreshold_of_ge_29`).
56. the hypotheses on the reusable free-core construction have been weakened
    to their actual arithmetic requirement `r >= 1`, and the generic bridge
    from a full-profile threshold to the global least threshold now assumes
    only `r >= 4`;
57. a reusable checked constant-profile recurrence evaluates every shadow
    with a ground bound and proves each successful state equal to the original
    `profileChain` state (`FiniteProfileChecker.lean`);
58. its upper-core specialization proves the complete capacity window
    `4,...,r+2` and the exact level-three carry `1 <= e <= 6`, thereby
    producing the semantic proposition `HasUpperCoreData`;
59. its full-profile specialization proves fit through level three followed
    by exact overflow at level two; a generic necessity theorem promotes any
    such recurrence overflow to `¬ FullMiddleProfileExists`;
60. one isolated native certificate verifies both checks for all 18 values
    `11 <= r <= 28` (`smallUniformFiniteCheck_verified`);
61. the direct finite obstruction and the already formalized canonical free
    core, indefinite padding, core-to-full construction, occupied-level
    reduction, and the `r >= 29` theorem combine into unconditional
    full-profile and least global threshold theorems for every `r >= 11`
    (`fullMiddleProfileThreshold_of_ge_11`,
    `isErdosThreshold_of_ge_11`).
62. the generic proposition `FullMiddleProfileThresholdAt r N` and its bridge
    to `IsErdosThreshold r N`, allowing the small-range last failure
    `N=2*r+4` to use the same global leastness proof;
63. the constant-profile checker now certifies an arbitrary interval and a
    successful check is fed through `profile_sufficiency` to construct an
    actual colex antichain (`constantProfileCheck_sound`,
    `fullMiddleProfileExists_of_constantProfileCheck`);
64. the explicit canonical free-family argument has been factored to require
    only feasibility of the canonical core recurrence, rather than the
    positive-carry route used in the uniform range
    (`hasSuitableFreeCore_of_recurrence`);
65. one isolated native certificate verifies, for all seven values
    `4 <= r <= 10`, full-profile overflow at `2*r+4`, feasibility at
    `2*r+5`, and core feasibility on `r+5` points. Profile sufficiency handles
    the first successful size, and persistent padding handles every later one
    (`SmallRangeCertificate.lean`);
66. the piecewise theorem `isErdosThreshold_of_ge_4` proves the original least
    threshold for the entire range `r >= 4`, with value `2*r+4` through
    `r=10` and `2*r+5` from `r=11` onward (`ThresholdTable.lean`).
67. a problem-statement façade restates the antichain, occurring-level
    multiplicity, `n-3` sizes, strict `n>N`, and leastness conditions directly;
    explicit equivalence lemmas connect it to the internal definitions, and
    `erdos776_lastFailure` plus `erdos776_threshold` prove the
    original problem statement for every `r >= 4` (`ProblemStatement.lean`).

## Intermediate semantic endpoints and assembly interfaces

An important intermediate semantic endpoint is:

```lean
theorem Erdos776.L4.l4_multiplicity_profile_infeasible
    (r : ℕ) (hr : 29 ≤ r) :
    ¬ ∃ F : Finset (Finset (Fin (r + 4))),
      HasL4MultiplicityProfile r F
```

Here `HasL4MultiplicityProfile r F` means that `F` is an antichain with at
least `r` members on every level from `2` through `r+1`. Thus the endpoint is
about actual families of subsets, not merely a numerical recurrence. The
underlying `l4Shadow r` is the minimum shadow defined from actual set families
on `Fin (r+4)`, and no Python verifier is used by any Lean proof.

A certificate-facing Section 16 endpoint is:

```lean
theorem Erdos776.Uniform.upperCore_fit_full_multiplicity_profile_infeasible
    (r : ℕ) (hr : 29 ≤ r) {e : ℕ}
    (hfit : ∀ b, 4 ≤ b → b ≤ r + 2 →
      upperCoreChain r b ≤ (r + 4).choose b)
    (hexcess : upperCoreChain r 3 = (r + 4).choose 3 + e)
    (heLower : 1 ≤ e) (heUpper : e ≤ 6) :
    ¬ ∃ F : Family (Fin (2 * r + 5)),
      IsSperner F ∧
        ∀ i, 2 ≤ i → i ≤ 2 * r + 3 → r ≤ (level F i).card
```

Thus all diagonal transfer, residual comparison, shell peeling, recurrence
overflow, and profile-to-antichain reasoning are kernel checked. The four
displayed hypotheses are the intended trust boundary to the package's
upper-core computation; they are not hidden inside a shadow lemma.

The conditional assembly endpoint is:

```lean
theorem Erdos776.Uniform.uniform_profile_threshold_from_components
    (r : ℕ) (hr : 29 ≤ r)
    (hupper : HasUpperCoreData r)
    (hcore : HasSuitableFreeCore r) :
    FullMiddleProfileThreshold r
```

Here `FullMiddleProfileThreshold r` means that the full middle profile is
impossible on `2*r+5` points and exists on every `n >= 2*r+6`. The component
propositions are transparent definitions, not axioms. This theorem verifies
all cardinalities, parity cases, padding indices, and construction transports
at a reusable component boundary. It was introduced before the remaining
leaves were closed; those leaves are now discharged by the unconditional
endpoints documented below.

After Section 15, the sharper endpoint is:

```lean
theorem Erdos776.Uniform.fullMiddleProfileThreshold_of_upperCoreData
    (r : ℕ) (hr : 29 ≤ r) (hupper : HasUpperCoreData r) :
    FullMiddleProfileThreshold r
```

Thus the suitable-free-core component has been discharged rather than merely
postulated at the assembly boundary.

The lower-window certificate-facing symbolic endpoint is:

```lean
theorem Erdos776.Uniform.fullMiddleProfileThreshold_of_lowerWindowFits
    (r : ℕ) (hr : 29 ≤ r) (hfit : LowerWindowFits r) :
    FullMiddleProfileThreshold r
```

`LowerWindowFits r` says exactly that the canonical recurrence (2.1) stays
within `choose (r+4) i` at every required level. No reflection, carry,
free-core, padding, diagonal-transfer, or antichain assembly premise remains.

The corresponding global endpoint is:

```lean
theorem Erdos776.Uniform.isErdosThreshold_of_lowerWindowFits
    (r : ℕ) (hr : 29 ≤ r) (hfit : LowerWindowFits r) :
    IsErdosThreshold r (2 * r + 5)
```

`IsErdosThreshold` includes the leastness clause in the definition of
`n_0(r)`, so the former occupied-level reduction gap is closed.

The completed non-computational endpoint is:

```lean
theorem Erdos776.Uniform.isErdosThreshold_of_ge_378
    (r : ℕ) (hr : 378 ≤ r) :
    IsErdosThreshold r (2 * r + 5)
```

There is no lower-window, upper-core, free-core, or assembly hypothesis in
this theorem. Its companion
`fullMiddleProfileThreshold_of_ge_378` states directly that the full middle
profile is impossible at `2*r+5` and exists at every later ground-set size.

After the verified finite base is joined to that theorem, the intermediate
`r>=29` endpoint is:

```lean
theorem Erdos776.Uniform.isErdosThreshold_of_ge_29
    (r : ℕ) (hr : 29 ≤ r) :
    IsErdosThreshold r (2 * r + 5)
```

For `29 <= r <= 377`, the only computational input is the Boolean result in
`LowerWindow/FiniteCertificate.lean`. Its evaluator searches cascade digits below the
ground-set bound and is connected to `canonicalShadow` by a proved equality;
the native computation is not trusted as an alternative recurrence.

The combined uniform endpoint is:

```lean
theorem Erdos776.Uniform.isErdosThreshold_of_ge_11
    (r : ℕ) (hr : 11 ≤ r) :
    IsErdosThreshold r (2 * r + 5)
```

For `11 <= r <= 28`, `FiniteProfileChecker.lean` separately certifies the
upper-core data used by the symbolic construction and direct overflow of the
full recurrence at level two. The Boolean computation is connected by proved
soundness theorems to `HasUpperCoreData` and the semantic nonexistence of an
actual antichain profile.

The final internal endpoint is the piecewise theorem:

```lean
theorem Erdos776.Uniform.isErdosThreshold_of_ge_4
    (r : ℕ) (hr : 4 ≤ r) :
    IsErdosThreshold r (erdosThresholdFromFour r)
```

where `erdosThresholdFromFour r` is `2*r+4` for `r<=10` and `2*r+5`
otherwise. For `4 <= r <= 10`, one seven-value native certificate verifies
the bad recurrence, the first good recurrence, and the reusable free core;
all semantic realizations and all later-size constructions are proved by the
generic Lean theorems.

The same endpoint is exposed in the published problem's existence language:

```lean
theorem Erdos776.Uniform.erdos776_threshold
    (r : ℕ) (hr : 4 ≤ r) :
    ProblemThreshold r (erdosThresholdFromFour r)
```

The stronger companion `erdos776_lastFailure` says that the displayed
value itself fails and every larger ground-set size succeeds.

## Scope boundary

The symbolic `r >= 29` theorem L4 and the global occupied-level reduction are
end-to-end formalized. The repository defines the finite extremal maximum
`extremalOccupiedLevels n r` and the least-threshold predicate from the
problem statement.

The construction lemmas are stated parametrically and do not assume the
existence of any computationally checked core. In the symbolic range
`r >= 378`, Lean constructs the needed canonical core and free family from the
proved lower-window fit, so no stored certificate enters the final theorem.
The complete phase/rising-tail/generalized-envelope bridge is proved rather
than postulated.

The full uniform range `r >= 11` is now covered inside Lean: direct finite
checking handles `11 <= r <= 28`, lower-window finite checking handles
`29 <= r <= 377`, and the symbolic theorem handles `r >= 378`. The semantic
L4 theorem itself remains uniform from `r=29` onward and is not used for the
18 smaller values. A separate finite certificate plus the generic semantic
construction proves the exact thresholds for `4 <= r <= 10`. Thus every
threshold in the package from `r=4` onward is formalized; only the separately
attributed cases `r=2,3` remain outside this Lean development.

## Reproduction commands and detailed audit

```bash
lake build --wfail
python3 tools/check_lean_placeholders.py
python3 tools/check_github_math.py
python3 tools/check_axiom_audit.py
```

`lake-manifest.json`, `lakefile.lean`, and `lean-toolchain` pin the environment
to Lean/mathlib v4.30.0.

There are no source-level project axioms. `#print axioms` on the purely
symbolic endpoint `isErdosThreshold_of_ge_378` reports only Lean/mathlib's
standard `propext`, `Classical.choice`, and `Quot.sound`. As expected,
`isErdosThreshold_of_ge_4` and `erdos776_threshold` additionally
report the three generated
`native_decide` axioms belonging to the finite Boolean certificates. Thus the
finite ranges trust Lean's native evaluator/compiler for the closed
computations, while all bridges from checker success to the mathematical
recurrences and semantic antichain statements are ordinary proved theorems.
