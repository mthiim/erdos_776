# Original problem formulation and Lean correspondence

This note checks the formulation published at
<https://www.erdosproblems.com/776> against the formal statement in
`Erdos776/Uniform/ProblemStatement.lean`.

`ProblemStatement.lean` is a review façade following the published wording;
the reusable internal proof is phrased independently of that presentation.

| Published problem phrase | Lean object |
|---|---|
| subsets of `{1,...,n}` | `Finset (Fin n)`; `Fin n` merely relabels the points as `0,...,n-1` |
| a finite family `A_1,...,A_m` | `Family (Fin n) = Finset (Finset (Fin n))` |
| `A_i` is not contained in `A_j` for `i != j` | `IsSperner F = IsAntichain (· ⊆ ·) F` |
| some set has size `t` | `(level F t).Nonempty` |
| at least `r` sets have that size | `r <= (level F t).card` |
| exactly `n-3` distinct sizes occur | `(occupiedLevels F).card = n-3` |
| the target exists | `ProblemTargetExists n r` |
| for every `n>N` the target exists, with least such `N` | `ProblemThreshold r N` |

An indexed family cannot contain duplicates under the stated antichain
condition: equal entries would be contained in one another. Representing the
family by a `Finset` therefore loses no admissible examples.

The central translation declarations are:

```lean
problemAdmissible_iff_isMultiplicityAntichain
problemTargetExists_iff_occupiedMiddleProfileExists
problemTargetExists_iff_fullMiddleProfileExists
```

The final original-formulation claims are:

```lean
theorem erdos776_lastFailure (r : ℕ) (hr : 4 ≤ r) :
    ProblemLastFailure r (erdosThresholdFromFour r)

theorem erdos776_threshold (r : ℕ) (hr : 4 ≤ r) :
    ProblemThreshold r (erdosThresholdFromFour r)
```

Here

```lean
erdosThresholdFromFour r = if r <= 10 then 2*r+4 else 2*r+5.
```

The last-failure theorem is stronger and especially easy to audit: the
displayed value itself fails, and every larger ground-set size works. Its
one-line order argument implies leastness.

The theorem covers `r>=4`. The values `r=2,3` in the package's complete table
are cited from He--Tang and are not asserted by this Lean theorem.

The full `r>=4` theorem depends on three generated `native_decide` certificate
axioms for the closed finite ranges and therefore additionally trusts Lean's
native evaluator/compiler. Their checker definitions and semantic soundness
bridges are ordinary Lean proofs. The symbolic `r>=378` endpoint reports only
`propext`, `Classical.choice`, and `Quot.sound`. See `lean/AxiomAudit.lean` and
`tools/check_axiom_audit.py` for the executable audit.
