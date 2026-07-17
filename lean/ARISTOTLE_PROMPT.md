# Focused Aristotle handoff for L4

The cascade job originally proposed below has now been completed locally in
`Erdos776/Combinatorics/`, `Erdos776/L4/CascadeSteps.lean`, and
`Erdos776/L4/ReverseSteps.lean`. It is retained as a record of the task split.
The profile-necessity job was subsequently completed in
`Erdos776/Combinatorics/ProfileNecessity.lean` and `Erdos776/L4/Profile.lean`.
No Aristotle handoff remains for the symbolic L4 theorem.

## Completed cascade prompt

> Work in this Lean 4.30.0/mathlib 4.30.0 project. Read
> `Erdos776/L4/ReverseEnvelope.lean` and `docs/L4_PROOF.md`. Do not change the
> statement or proof of `Erdos776.L4.not_l4_chain`, and do not use `sorry`,
> `admit`, `axiom`, `unsafe`, or additional hypotheses. Add a module defining
> the numerical Kruskal--Katona shadow using mathlib's colex initial segments
> (`Mathlib.Combinatorics.SetFamily.KruskalKatona`). Prove:
>
> 1. monotonicity in the family cardinality (within the relevant capacity);
> 2. a generic theorem that the lower shadow of a displayed canonical
>    binomial cascade is obtained by lowering every lower binomial index by
>    one;
> 3. `Erdos776.L4.ReverseSteps` for every `r >= 29`;
> 4. `Erdos776.L4.TopStepIdentities` for every `r >= 29`.
>
> Instantiate `Erdos776.L4.not_l4_chain` with this concrete shadow. Keep each
> canonicality inequality explicit, especially the ranges `i=3..8`,
> `9<=i<=28`, `i=29`, and `30<=i<=r-2`. Run `lake build` and report the exact
> theorem names added and `#print axioms` for the final theorem.

If that job is too large, split it in this order:

1. generic cascade representation and termwise-shadow theorem;
2. `TopStepIdentities` only;
3. `ReverseSteps` for `i=3,...,8`;
4. the three parametric ranges of `ReverseSteps`;
5. concrete instantiation of `not_l4_chain`.

## Completed profile-necessity prompt

> Using the concrete numerical shadow from the cascade module, formalize only
> the necessity direction of the prescribed-profile criterion needed by L4.
> Define an antichain of finite subsets of `Fin (r+4)` with exactly `r` members
> on each level `2,...,r+1`. From such a family construct the cumulative
> down-closures and prove existence of an `IsL4Chain` satisfying
> `c 2 <= choose (r+4) 2`. Use mathlib's `Finset.kruskal_katona`; do not assume
> the Clements/DGH criterion as an axiom. Combine this with the concrete L4
> recurrence theorem `Erdos776.L4.l4_no_recurrence` to prove that the profile is infeasible for every
> `r >= 29`.

The implemented theorem is slightly stronger: it assumes at least `r`, rather
than exactly `r`, members on each required level.

## Review checklist for generated code

- The final theorem must refer to the concrete colex/Kruskal--Katona shadow,
  not an unconstrained function named `shadow`.
- `ReverseSteps` and `TopStepIdentities` must be proved, not passed as theorem
  parameters.
- Search for `sorry`, `admit`, custom `axiom`, and unintended new hypotheses.
- Check all uses of natural-number subtraction have the needed lower bounds.
- Run `lake build` and inspect `#print axioms` on the semantic L4 theorem.
- Compare every Lean definition with the mathematical profile before treating
  a typechecked result as formalization of the manuscript claim.
