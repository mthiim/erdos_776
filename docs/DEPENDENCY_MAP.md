# Dependency map for the complete threshold table

The threshold `n_0(r)` is defined for `r>=2` by requiring
`g(n,r)=n-3` for every `n>n_0(r)`.

## 1. Small multiplicities

- He--Tang prove
  \[
  n_0(2)=3,\qquad n_0(3)=8.
  \]
- `SMALL_R_NOTE.md` proves, by exact prescribed-profile arithmetic plus
  explicit construction/padding,
  \[
  n_0(r)=2r+4\qquad(4\le r\le10).
  \]

For `4<=r<=10`, the logical chain is:

1. the full profile fails at `n=2r+4`;
2. it is feasible, with stored direct certificates, at `n=2r+5`;
3. the base core on `r+5` points is feasible and has `r` explicit free
   sets;
4. persistent two-point padding plus the core-to-full lemma covers every
   `n>=2r+6`;
5. the occupied-level reduction converts the full-profile statements to
   the threshold equality.

## 2. Uniform range `r>=11`

For `r>=11`, let `alpha_r` be the largest top load in the window profile
on `r+4` points.

1. **Lower window:** `UNIFORM_THEOREM.md`, Sections 2--12, proves
   \[
   \alpha_r\ge r-6.
   \]
   The range `11..377` is exact finite arithmetic; `r>=378` is symbolic.

2. **Upper window (L4):** `L4_PROOF.md` proves
   \[
   \alpha_r\le r-1.
   \]
   The range `11..28` is exact finite arithmetic; `r>=29` is symbolic.

3. **Core carry:** if
   \[
   a_3=\binom{r+4}{3}+e_r,
   \]
   reflection gives `alpha_r=r-e_r`; hence `1<=e_r<=6`.

4. **Base core:** the carry bound gives feasibility of the full core on
   `r+5` points.

5. **Construction:** the canonical core has `r` explicit free sets.  The
   two-point padding lemma and core-to-full construction give the full
   profile for every `n>=2r+6`.

6. **Obstruction:** the diagonal cascade identity transfers `e_r>=1` to
   the full profile at `n=2r+5`.  L4 controls the residual recurrence,
   giving a capacity overflow.

7. **Level reduction:** the elementary singleton/complement argument shows
   that an `n-3`-level witness must occupy exactly levels `2,...,n-2`.

Therefore
\[
n_0(r)=2r+5\qquad(r\ge11).
\]

## 3. Complete table

Combining the cited He--Tang cases, the finite theorem, and the uniform
theorem candidate gives

\[
 n_0(r)=
 \begin{cases}
 3,&r=2,\\
 8,&r=3,\\
 2r+4,&4\le r\le10,\\
 2r+5,&r\ge11.
 \end{cases}
\]

