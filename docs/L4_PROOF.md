# L4: a proof that α_r ≤ r − 1 (all r ≥ 29)

*Standalone companion to `UNIFORM_THEOREM.md`. The proof written here is
symbolic for all $r\ge29$. In the final Lean theorem the range
$11\le r<29$ is closed by a direct bounded upper-core/overflow
certificate; `verification/verify_l4.py` remains an independently implemented
exact cross-check of L4 on that finite range. This note uses only the classical
Kruskal--Katona shadow function and elementary binomial identities.*


## Cascade notation

For $m\ge0$ and $k\ge1$, write the canonical cascade
$$
m=\binom{a_k}{k}+\binom{a_{k-1}}{k-1}+\cdots+\binom{a_s}{s},
\qquad a_k>a_{k-1}>\cdots>a_s\ge s,
$$
and define
$$
\partial_k(m)=\binom{a_k}{k-1}+\binom{a_{k-1}}{k-2}+\cdots+
\binom{a_s}{s-1}.
$$
We use monotonicity of $\partial_k$, Pascal's identity, and the fact that
shadowing a displayed canonical cascade lowers each position by one.

## 0. Statement

Here $\alpha_r$ is the largest integer $y$ for which the profile with $r$
sets at every level $2,\ldots,r$ and $y$ sets at level $r+1$ is feasible on
$A=r+4$ points. Equivalently, it is the largest top value whose canonical
profile recurrence fits every capacity; this equivalence is the
prescribed-profile criterion.

**Theorem L4.** For every r ≥ 29 the profile [r sets of every size
2..r, r sets of size r+1] on A = r+4 points is infeasible; equivalently
α_r ≤ r−1. Lean kernel-checks this semantic theorem in
`Erdos776/L4/Profile.lean`. The finite range 11 ≤ r < 29 is checked exactly
by `verification/verify_l4.py`; the final Lean threshold theorem handles
that range through its smaller direct certificate rather than importing the
Python result.

By DGH/Clements necessity, feasibility would give the chain

    c_{r+1} = r,   c_i = r + ∂_{i+1}(c_{i+1})   (i = r, …, 2),

with c_2 ≤ C(A,2). We derive a contradiction from c_2 ≤ C(A,2) alone
(no other capacity bound is used).

## 1. The bounding sequence Ĝ

Define, for r ≥ 29:

    Ĝ_2 = C(r+4, 2)
    Ĝ_3 = C(r+3, 3) + 3
    Ĝ_4 = C(r+2, 4) + C(r+1, 3) + 6
    Ĝ_5 = C(r+2, 5) + C(r, 4) + C(r−1, 3) + 10
    Ĝ_6 = C(r+2, 6) + C(r, 5) + C(r−2, 4) + C(r−3, 3) + 21
    Ĝ_7 = C(r+2, 7) + C(r, 6) + C(r−2, 5) + C(r−4, 4) + C(r−5, 3) + 120
    Ĝ_i = C(r+2, i) + C(r, i−1) + C(r−2, i−2) + C(r−4, i−3)
          + C(r−5, i−4) + C(23, i−5)          for 8 ≤ i ≤ r−2.

(The junk constants are binomials: 3 = C(3,2), 6 = C(4,2), 10 = C(5,2),
21 = C(7,2), 120 = C(16,2); the corrector C(23, i−5) vanishes for
i ≥ 29 — "automatic taper".) For 8 ≤ i ≤ r−2 the displayed form is the
canonical digit sequence of Ĝ_i: digits r+2 > r > r−2 > r−4 > r−5 > 23
(strictly decreasing since r ≥ 29) at consecutive positions i … i−5,
digits ≥ positions (r−5 ≥ i−4 ⟺ i ≤ r−1; 23 ≥ i−5 for i ≤ 28, and for
i ≥ 29 the term is 0 and the sequence ends at position i−4). Levels
3–7 are likewise canonical (junk digits 3, 4, 5, 7, 16 at position 2,
all below the digit above them: 16 < r−5 needs r ≥ 22).

**Lemma RS (reverse steps).** For every 3 ≤ i ≤ r−2:

    r + ∂_i(Ĝ_i + 1) > Ĝ_{i−1}.

*Proof.* Each case is obtained by termwise shadowing of the displayed
canonical cascade for Ĝ_i+1; throughout we use C(n,k) − C(n−1,k) = C(n−1,k−1) and
C(m,2) − C(m−1,2) = m−1.

i = 3: Ĝ_3+1 = C(r+3,3)+C(3,2)+C(1,1), shadow C(r+3,2)+3+1, so
LHS = C(r+3,2)+r+4 = C(r+4,2)+1 = Ĝ_2 + 1.  [difference 1]

i = 4: Ĝ_4+1 = C(r+2,4)+C(r+1,3)+C(4,2)+C(1,1), shadow
C(r+2,3)+C(r+1,2)+4+1; LHS − Ĝ_3 = r + C(r+1,2)+5 − C(r+2,2) − 3
= r + 2 − (r+1) = 1.  [difference 1]

i = 5: Ĝ_5+1 = C(r+2,5)+C(r,4)+C(r−1,3)+C(5,2)+C(1,1), shadow
C(r+2,4)+C(r,3)+C(r−1,2)+5+1; LHS − Ĝ_4
= r + C(r,3)+C(r−1,2)+6 − C(r+1,3) − 6 = r + C(r−1,2) − C(r,2) = 1.

i = 6: Ĝ_6+1 = C(r+2,6)+C(r,5)+C(r−2,4)+C(r−3,3)+C(7,2)+C(1,1)
(22 = C(7,2)+C(1,1)), shadow …+C(r−3,2)+7+1; LHS − Ĝ_5
= r + C(r−2,3)+C(r−3,2)+8 − C(r−1,3) − 10
= r − 2 + C(r−3,2) − C(r−2,2) = r − 2 − (r−3) = 1.

i = 7: Ĝ_7+1 = C(r+2,7)+C(r,6)+C(r−2,5)+C(r−4,4)+C(r−5,3)
+C(16,2)+C(1,1), shadow …+C(r−5,2)+16+1; LHS − Ĝ_6
= r + C(r−4,3)+C(r−5,2)+17 − C(r−3,3) − 21
= r − 4 + C(r−5,2) − C(r−4,2) = r − 4 − (r−5) = 1.

i = 8 (the switch): Ĝ_8+1 = C(r+2,8)+C(r,7)+C(r−2,6)+C(r−4,5)
+C(r−5,4)+C(23,3)+C(2,2), shadow
C(r+2,7)+C(r,6)+C(r−2,5)+C(r−4,4)+C(r−5,3)+C(23,2)+C(2,1);
LHS − Ĝ_7 = r + 253 + 2 − 120 = r + 135.

9 ≤ i ≤ 28: Ĝ_i+1 appends the unary digit i−6 at position i−6
(valid: i−6 < 23), so the shadow is [the five leading terms shifted]
+ C(23, i−6) + (i−6) = Ĝ_{i−1} + (i−6) − [0], giving difference r + i − 6.

i = 29: this case is nonempty only when r ≥ 31. Since C(23,24) = 0,
Ĝ_29+1 appends the unary digit 24 at position 24 (valid: 24 < r−5),
and the shadow is
[five terms shifted] + C(24,23) = (Ĝ_28 − C(23,23)) + 24 = Ĝ_28 + 23;
difference r + 23.

30 ≤ i ≤ r−2: all corrector terms have vanished. Thus Ĝ_i+1 appends
the unary digit i−5 at position i−5 (valid: i−5 < r−5), and its
shadow is [the five leading terms shifted] + (i−5) = Ĝ_{i−1}+(i−5).
The difference is therefore exactly r+i−5. ∎

**Lemma IND (the bound).** If the profile is feasible then
c_i ≤ Ĝ_i for every 2 ≤ i ≤ r−2.
*Proof.* c_2 ≤ C(A,2) = Ĝ_2. Inductively, if c_{i−1} ≤ Ĝ_{i−1} and
c_i ≥ Ĝ_i + 1, then by monotonicity c_{i−1} = r + ∂_i(c_i) ≥ r + ∂_i(Ĝ_i+1)
> Ĝ_{i−1}, a contradiction; so c_i ≤ Ĝ_i. ∎

## 2. The forced top of the chain (Lemma L4-T)

Exact computation of three steps of the chain by termwise shadowing of
the displayed canonical cascades, for r ≥ 15:

  * c_{r+1} = r: unary digits r+1, r, …, 2 at positions r+1 … 2.
    Shadow Σ_{j=2}^{r+1} j = C(r+2,2) − 1, so
    **c_r = C(r+2,2) + (r−1)**, with digit sequence C(r+2, r) +
    [unary r−1, …, 1 at positions r−1 … 1].
  * Shadow of c_r: C(r+2, r−1) + Σ_{j=1}^{r−1} j = C(r+2,r−1) + C(r,2),
    so **c_{r−1} = C(r+2,r−1) + C(r,2) + r**, with digit sequence
    C(r+2, r−1) + C(r, r−2) + C(r−2, r−3) + C(r−4, r−4) + C(r−5, r−5)
    (indeed C(r,r−2) = C(r,2), then r = (r−2) + 1 + 1).
  * Shadow: C(r+2,r−2)+C(r,r−3)+C(r−2,r−4)+(r−4)+(r−5), so
    **c_{r−2} = C(r+2,4) + C(r,3) + C(r−2,2) + (3r − 9)** in value
    (positions r−2, r−3, r−4 for the three leading terms). ∎

(These three identities are re-verified numerically for every r in the
verification range; the verifier recomputes the chain with a separately
implemented exact `kk_shadow`.)

## 3. The contradiction

For r ≥ 31, C(23, (r−2)−5) = C(23, r−7) = 0 (r−7 > 23), so

    Ĝ_{r−2} = C(r+2,4) + C(r,3) + C(r−2,2)
                 + C(r−4,r−5) + C(r−5,r−6)
               = C(r+2,4) + C(r,3) + C(r−2,2) + (2r−9).

Indeed, C(r−4,r−5)=r−4 and C(r−5,r−6)=r−5. Hence

    c_{r−2} − Ĝ_{r−2} = (3r − 9) − (2r − 9) = r > 0,

contradicting Lemma IND at i = r−2. For r ∈ {29, 30} the corrector
term C(23, r−7) equals C(23,22) = 23 resp. C(23,23) = 1 and the margin
is r − 23 = 6 resp. r − 1 = 29, still positive. Therefore the profile
is infeasible and α_r ≤ r − 1 for all r ≥ 29. ∎

## 4. Remarks

1. **Uniformity.** Unlike the lower half, there is no upper threshold:
   the forward chain is used only three levels deep, so no top-zone
   budget arises. L4 is proved for ALL r ≥ 29.
2. **Reverse-step margins.** The quantity
   $r+\partial_i(\widehat G_i+1)-\widehat G_{i-1}$ equals 1 for
   $i=3,\ldots,7$, equals $r+135$ at $i=8$, and has the exact
   positive values displayed above thereafter. The final contradiction
   margin is positive (and equals $r$ for $r\ge31$). Thus all tight
   cases are confined to the six explicit head computations above.
3. **Verification.** `verification/verify_l4.py` checks the exact finite
   base $11\le r<29$ and recomputes every reverse step, the three top
   identities, and the final margin at representative values through
   $r=1000$. The proof above is symbolic and
   does not depend on any stress test.

## 5. Consequences (dependency update)

With L4 proved for $r\ge29$, and the finite base checked for
$11\le r<29$:

- L5 follows immediately. Its two top singleton loads induce cumulative
  load $r+3$ at level $r+1$, larger than the L4-admissible maximum
  $r-1$.
- The one-seed residual recurrence used in the full-profile obstruction
  dominates the L4 recurrence by monotonicity.
- Together with the uniform lower-window theorem in `UNIFORM_THEOREM.md`,
  this supplies the upper half of the core window for every $r\ge11$.
