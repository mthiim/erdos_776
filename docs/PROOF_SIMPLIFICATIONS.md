# Proof simplifications in the current revision

This note records conceptual simplifications made after the proof was already
formalized.  They remove unnecessary human-proof bookkeeping; they do not
change the mathematical claim or hide computational assumptions.

## 1. Puncturing replaces member classification

The old free-set proof classified three exceptional colex members and every
later core member.  None of that classification is needed.

**Puncturing lemma.** Let `C` be an antichain, let `T` belong to `C`, and let
`D` be a proper subset of `T`.  Then `D` contains no member of `C`.

Indeed, if `A` belongs to `C` and `A` is contained in `D`, then `A` is
contained in `T`.  Antichainness forces `A=T`, contradicting the fact that
`T` is not contained in the proper subset `D`.

For each displayed top core member

$$
T_j=X\setminus\{j\},
$$

take

$$
D_j=T_j\setminus\{1\}.
$$

These are exactly the formerly displayed free sets.  The proof now needs only
that `T_j` is a member of the canonical core and that the core is an
antichain.  Lean implements this argument in
`explicitFreeFamily_isFree_of_isSperner`.

The same puncturing argument applies without change in the finite range
`4<=r<=10` once the core recurrence has been proved feasible.

## 2. The upper-core carry is the main interface

The uniform proof is now organized around

$$
a_b\le\binom{r+4}{b}\quad(4\le b\le r+2),
\qquad
a_3=\binom{r+4}{3}+e,
\qquad
1\le e\le6.
$$

The dependency is:

- lower-window feasibility gives the upper capacities and `e<=6`;
- L4 gives `e>=1`;
- `e>=1` starts the obstructing residual inside the diagonal shell;
- `e<=6` makes the core feasible on one additional point;
- puncturing supplies the free sets;
- persistent padding and core-to-full supply every later `n`.

This interface is the Lean proposition `HasUpperCoreData`.

## 3. `alpha_r` is interpretation, not plumbing

The identity `alpha_r=r-e` remains informative: it explains why the lower
window and L4 bound the same carry.  The main dependency graph no longer
routes every later theorem through `alpha_r`.  Lean works with the exact
lower-window capacity predicate and `HasUpperCoreData` directly.

## 4. The profile theorem is deliberately asymmetric

For obstruction, an antichain with **at least** `f_i` members at each level
forces the canonical recurrence capacities.  No trimming is required.

For construction, fitting capacities build an antichain with **exactly**
profile `f` by successive colex layers.

This is stronger and cleaner than presenting both directions only as an
exact-profile equivalence.  The Lean declarations are
`profileChain_isProfileRecurrence_of_antichain` and `profile_sufficiency`.

## 5. Diagonal transfer is a no-carry shell principle

The identity in Section 16 should be read as one invariant.  A diagonal
binomial shell shadows term by term as long as the residual is strictly below
the next shell capacity.  That strict inequality is precisely the no-carry
condition.  If it fails, capacity overflow has already occurred; if it keeps
holding, the shell peels away and exposes an L4-dominated residual at the
bottom.

Lean isolates this principle as `canonicalShadow_diagonal_transfer` and then
uses it in `fullProfileChain_diagonal_transfer`.

## 6. The lower-window proof is a sequence of stitched segments

The detailed cascade calculations remain available, but the conceptual unit
is a capacity-bounded supersolution assembled from:

1. exact anchors;
2. one completed anchor;
3. ordinary phases;
4. a rising tail;
5. a generalized envelope;
6. the scalar collision;
7. scalar collapse;
8. the final levels.

The segment table in `PROOF_GUIDE.md` gives the level interval, state,
transition theorem, capacity theorem, and Lean module for every segment.

## 7. Statement correspondence is now explicit

`Erdos776/Uniform/ProblemStatement.lean` restates the published problem
condition and threshold convention directly. It proves the equivalence to the
reusable internal definitions and exposes both a last-failure theorem and the
least eventual-threshold theorem for every `r>=4`.
