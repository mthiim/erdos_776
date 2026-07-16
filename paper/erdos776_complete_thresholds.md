---
title: "Erdős Problem 776: exact thresholds for antichains with level multiplicity"
author: "Human-led (mthiim), AI-assisted research package"
date: "16 July 2026 - v0.3.0 complete-threshold candidate"
geometry: margin=1in
fontsize: 10pt
colorlinks: true
linkcolor: blue
urlcolor: blue
toc: true
toc-depth: 2
---

# Status and principal statement

For the threshold `n_0(r)` defined for `r>=2`, the combined result is

\[
 n_0(r)=
 \begin{cases}
 3,&r=2,\\
 8,&r=3,\\
 2r+4,&4\le r\le10,\\
 2r+5,&r\ge11.
 \end{cases}
\]

The values at `r=2,3` are due to Yixin He and Quanyu Tang.  The range
`4<=r<=10` is proved by exact finite profile arithmetic, stored witnesses,
and a symbolic padding argument.  The `r>=11` line is a complete
AI-assisted theorem candidate that has survived four adversarial AI audits
but has not yet received the named human line-by-line verification requested
by the intended forum policy.

The load-bearing proof is split into the following four parts in this PDF:

1. the prescribed-profile criterion and exact `r=11` result;
2. the finite exact range `4<=r<=10`;
3. the L4 reverse-envelope theorem;
4. the uniform `r>=11` construction and obstruction.

The source repository contains exact certificates, standard-library
verification scripts and a contribution record.

\newpage

# Part I: prescribed profiles and the exact case r=11

# An exact calculation at $r=11$ in the Erdős–Trotter antichain problem

*Preliminary note, 15 July 2026. External review requested.*

## 1. Definitions and result

For a family $\mathcal F\subseteq 2^{[n]}$, let

$$
S(\mathcal F)=\{|A|:A\in\mathcal F\}.
$$

An **$r$-multiplicity antichain** is an antichain for which every occurring
level contains at least $r$ members. Let $g(n,r)$ be the maximum possible
value of $|S(\mathcal F)|$. Following He and Tang, let $n_0(r)$ be the
least threshold such that $g(n,r)=n-3$ for every $n>n_0(r)$.

The result certified here is:

**Theorem.**

$$
g(27,11)=23 \quad\text{and}\quad n_0(11)=27.
$$

For completeness, we first record the elementary upper bound needed
throughout the proof. Let $n\ge12$. In an 11-multiplicity antichain, levels
0 and $n$ cannot occur, since each contains only one set. If level 1 occurs,
choose 11 singleton members. Every other member must avoid those 11 points,
so the occupied sizes lie in $\{1\}\cup\{2,3,\ldots,n-11\}$; hence at
most $n-11<n-3$ levels occur. Applying the same argument to the complement
family handles level $n-1$. Otherwise all occupied levels lie among
$2,3,\ldots,n-2$, of which there are $n-3$. Thus

$$
g(n,11)\le n-3,
$$

and equality forces the occupied levels to be exactly $2,3,\ldots,n-2$.
In particular, a hypothetical 24-level witness at $(n,r)=(27,11)$ must
occupy exactly $2,3,\ldots,25$. Trimming each of those levels to exactly
11 members preserves the antichain property. Consequently,

$$
g(27,11)=24
\iff
\text{the profile }f_i=11\ (2\le i\le25)\text{ is feasible.}
$$

## 2. Exact profile criterion

For $m\ge0$ and $k\ge1$, write the unique binomial (cascade)
representation

$$
m=\binom{a_k}{k}+\binom{a_{k-1}}{k-1}+\cdots+\binom{a_t}{t},
\qquad a_k>a_{k-1}>\cdots>a_t\ge t,
$$

and define

$$
\partial_k(m)=
\binom{a_k}{k-1}+\binom{a_{k-1}}{k-2}+\cdots+
\binom{a_t}{t-1},
\qquad \partial_k(0)=0.
$$

Kruskal–Katona says that $\partial_k(m)$ is the minimum possible lower
shadow of $m$ distinct $k$-sets, attained by a colex initial segment.

Let $f=(f_0,\ldots,f_n)$ be a proposed profile and let
$s=\max\{i:f_i>0\}$. Define

$$
m_s=f_s,
\qquad
m_i=f_i+\partial_{i+1}(m_{i+1})\quad(i=s-1,s-2,\ldots,0).
$$

**Profile criterion.** There is an antichain on $[n]$ with profile $f$
if and only if

$$
m_i\le\binom ni
$$

for every $i$.

This is a formulation of the classical squashed-antichain profile theorem.
A short proof is included so that the profile reduction and greedy construction
can be checked locally; Kruskal--Katona itself, in the cascade form stated
above with colex attainment, is used as the classical black box.

### Necessity

For an antichain $\mathcal F$, let $\mathcal F_i$ be its level-$i$
part. Let $D_i$ be the collection of all $i$-sets properly contained in
some member of $\mathcal F$ on a higher level, and set

$$
M_i=\mathcal F_i\mathbin{\dot\cup}D_i.
$$

The union is disjoint because $\mathcal F$ is an antichain. Moreover, the
lower shadow of $M_{i+1}$ lies inside $D_i$. Therefore

$$
|M_i|\ge f_i+\partial_{i+1}(|M_{i+1}|).
$$

At the highest occupied level, $D_s=\varnothing$, so
$|M_s|=f_s=m_s$. Starting from this base and using monotonicity of the
Kruskal–Katona function gives $|M_i|\ge m_i$ by downward induction. Since
$M_i$ consists of $i$-subsets of $[n]$, this implies
$m_i\le\binom ni$.

### Sufficiency

Choose the family from the top down. At the highest occupied level take the
first $f_s$ sets in colex. Inductively, suppose that at level $i+1$ the union
of the down-closure of all higher chosen sets with the sets chosen on level
$i+1$ is the colex initial segment of size $m_{i+1}$. Its lower shadow is
therefore the colex initial segment of size $\partial_{i+1}(m_{i+1})$.
Moreover, an $i$-set lies below some chosen set on a level above $i$ if and
only if it lies below an intermediate $(i+1)$-set in this cumulative segment;
this is just transitivity of containment through level $i+1$. Hence that
shadow is exactly the level-$i$ down-closure of all higher choices.

Choose the next $f_i$ sets in colex, immediately following this shadow. The
hypothesis $m_i\le\binom ni$ ensures that these sets lie in $[n]$, and their
union with the shadow is the colex initial segment of size $m_i$. This
preserves the induction invariant. The newly chosen lower sets avoid the
down-closure of all higher chosen sets, so the resulting family is an
antichain with profile $f$.

## 3. The calculation at $(n,r)=(27,11)$

For the 24-level profile

$$
f_i=11\quad(2\le i\le25),
$$

the recurrence gives

$$
m_3=2709=\binom{26}{3}+\binom{15}{2}+\binom41.
$$

Therefore

$$
\partial_3(m_3)=\binom{26}{2}+\binom{15}{1}+\binom40=341,
\qquad
m_2=341+11=352>351=\binom{27}{2}.
$$

The level-$2$ failure already proves infeasibility. For accuracy, level $1$
also fails: the $2$-cascade of $352=\binom{27}{2}+\binom11$ gives
$m_1=27+1=28>27$. Thus no 11-multiplicity antichain on $[27]$ can use
24 distinct sizes, and

$$
g(27,11)\le23.
$$

For the profile

$$
f_i=11\quad(2\le i\le24),
$$

the recurrence fits at every level. The useful bottom calculation is

$$
m_3=2413=\binom{25}{3}+\binom{15}{2}+\binom81,
\qquad
\partial_3(m_3)=316,
\qquad
m_2=327\le351.
$$

The actual tight capacity occurs one level lower:
$327=\binom{26}{2}+\binom21$, so
$m_1=\partial_2(327)=26+1=27=\binom{27}{1}$.

The colex construction therefore supplies 11 sets on each of the 23 levels
$2,\ldots,24$. The generated family has 253 sets and passes the independent
pairwise-containment checker. Hence

$$
g(27,11)=23.
$$

The complete arithmetic and explicit construction are reproduced by
`tests/verify_r11.py`; the explicit family is in
`certificates/r11_n27_23_levels.txt`.

## 4. Construction for every $n\ge28$

We use two elementary lemmas.

### Core-to-full lemma

Suppose $\mathcal C$ is an antichain on $[q]$ having at least $r$
sets of every size

$$
2,3,\ldots,\lfloor n/2\rfloor-1,
$$

where $q\le n-1-r$. Introduce a pivot point $a$ and $r$ private
points $p_1,\ldots,p_r$, all outside the core. Form the lower family from

$$
\{a,p_j\}\quad(1\le j\le r)
$$

and, for each required core level, $r$ sets $C\cup\{a\}$. Add their
complements to supply the upper levels (at the middle level when $n$ is
even, retaining either side already supplies at least $r$ sets).

The lower family is an antichain. Distinct pairs have the same size;
pivoted core sets satisfy
$C\cup\{a\}\subseteq C'\cup\{a\}$ exactly when $C\subseteq C'$,
which the core antichain excludes; and the private points prevent a pair
$\{a,p_j\}$ from lying inside a pivoted core set. Taking complements
reverses containment, so the complemented upper family is also an
antichain.

It remains to check both cross-side directions. If a lower set $L$ were
contained in the complement of another lower set $L'$, then $L$ and
$L'$ would be disjoint, although both contain $a$. Conversely,
$[n]\setminus L'\subseteq L$ would imply $L\cup L'=[n]$. This is
impossible because both lower sets contain $a$ and have size at most
$\lfloor n/2\rfloor$, giving

$$
|L\cup L'|\le 2\lfloor n/2\rfloor-1\le n-1.
$$

Thus the result is an $r$-multiplicity antichain using every size
$2,\ldots,n-2$.

### Two-point padding lemma

Let $\mathcal C$ be an antichain on $[q]$ with at least $r$ sets of
every size $2,\ldots,s$. Suppose that
$D_1,\ldots,D_r$ are distinct $(s-1)$-subsets of $[q]$, none of which
contains a member of $\mathcal C$. With two new points $x,y$, set

$$
\mathcal C'=
\mathcal C\cup\{D_i\cup\{x,y\}:1\le i\le r\}.
$$

The new sets are mutually incomparable. If an old set were contained in a
new one, it would be contained in $D_i$, contrary to the hypothesis; a
new set cannot be contained in an old one because it uses new points.
Therefore $\mathcal C'$ is an antichain and supplies level $s+1$.

Freeness persists indefinitely in a completely explicit way. Fix base free
sets $G_1,\ldots,G_r$. If the first $t$ added pairs are
$\{x_j,y_j\}$, define

$$
D_i^{(t)}=G_i\cup\{x_1,\ldots,x_t\}.
$$

This set contains no base-core member. It also cannot contain a member born
at stage $j$, because every such member contains $y_j$, whereas
$D_i^{(t)}$ omits $y_j$. Hence the next padding step can add

$$
D_i^{(t)}\cup\{x_{t+1},y_{t+1}\}\qquad(1\le i\le r),
$$

and the same fixed base free sets sustain the chain indefinitely.

### The $r=11$ base

The exact profile criterion constructs a core on 16 points with 11 sets of
every size $2,\ldots,13$. Direct enumeration finds 88 free 12-subsets;
only 11 are required. Both the antichain property and the free-set count are
checked in `tests/verify_r11.py`. The complete 132-set core and the first 11
free 12-subsets are explicitly listed in
`certificates/r11_core_and_free_sets.txt`, which the verifier parses and
checks without regenerating the core.

At padding stage $t$, the core has

$$
q=16+2t,\qquad s=13+t.
$$

For $n=28+2t$, these are exactly the parameters needed by the core-to-full
lemma; for $n=29+2t$, the same core fits with one point to spare. Hence a
full-profile 11-multiplicity antichain exists for every $n\ge28$.

Since the full profile fails at $n=27$, this proves

$$
n_0(11)=27.
$$

## 5. Relation to the uniform companion result

This note deliberately keeps the exact $r=11$ proof self-contained. A
separate companion manuscript in [`UNIFORM_THEOREM.md`](../docs/UNIFORM_THEOREM.md)
gives an AI-assisted proof candidate for

$$
n_0(r)=2r+5\qquad(r\ge11).
$$

The exact calculation and stored certificates in this note do not depend on
the uniform argument. Conversely, the uniform manuscript uses the same
classical profile criterion and the core/padding framework developed here.
The uniform argument has passed four adversarial AI audits but has not yet
undergone traditional peer review; the repository records that distinction
explicitly.

## References

1. P. Erdős, *Problem sessions*, in I. Rival (ed.), *Ordered Sets*
   (Proc. NATO Advanced Study Institute), Reidel, Dordrecht, 1981,
   pp. 860–861.
2. Y. He and Q. Tang, *An Erdős--Trotter problem on antichains with
   multiplicity $r$ on each occurring level*, arXiv:2602.09803 (2026),
   <https://arxiv.org/abs/2602.09803>.
3. G. F. Clements, *A Minimization Problem Concerning Subsets of a Finite
   Set*, Discrete Mathematics **4** (1973), 123–128.
4. D. E. Daykin, J. Godfrey, and A. J. W. Hilton, *Existence Theorems for
   Sperner Families*, Journal of Combinatorial Theory, Series A **17**
   (1974), 245–251.
5. P. Lieby, *Antichains on Three Levels*, Electronic Journal of
   Combinatorics **11** (2004), R50. Theorem 2.8 records the classical
   prescribed-profile squashing theorem:
   <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v11i1r50>.

\newpage

# Part II: exact thresholds for 4 <= r <= 10

# Exact thresholds for multiplicities `4 <= r <= 10`

This note completes the finite range between the exact values of He--Tang
at `r=2,3` and the uniform theorem for `r>=11`.

Throughout, `g(n,r)` is the maximum number of occupied levels in an
`r`-multiplicity antichain on `[n]`, and `n_0(r)` is the least integer
`n_0` such that

\[
g(n,r)=n-3\qquad\text{for every }n>n_0.
\]

The definition of `n_0(r)` is used for `r>=2`.  The original problem treats
`r=1` separately, where the extremal number of occupied levels is `n-2`
rather than `n-3`.

## Theorem

For every integer `r` with `4 <= r <= 10`,

\[
\boxed{n_0(r)=2r+4.}
\]

Together with He--Tang's exact values

\[
n_0(2)=3,\qquad n_0(3)=8,
\]

and the companion uniform theorem candidate

\[
n_0(r)=2r+5\qquad(r\ge11),
\]

this gives the complete threshold table for every value `r>=2`:

\[
\boxed{
 n_0(r)=
 \begin{cases}
 3,&r=2,\\
 8,&r=3,\\
 2r+4,&4\le r\le10,\\
 2r+5,&r\ge11.
 \end{cases}}
\]

The last line retains the review status of `docs/UNIFORM_THEOREM.md`; the
finite statement proved in this note is independent of the symbolic
large-`r` phase argument.

## 1. Reduction to a prescribed profile

For `r>=4`, an `r`-multiplicity antichain with `n-3` occupied levels must
use exactly the levels

\[
2,3,\ldots,n-2.
\]

Indeed, levels `0` and `n` cannot occur.  If level `1` occurs, choose `r`
singleton members.  Every other member avoids those `r` points, so all
occupied sizes lie in

\[
1,2,\ldots,n-r,
\]

and there are at most `n-r <= n-4` of them.  Complementation excludes
level `n-1` in an `n-3`-level witness.  Trimming every occupied level to
exactly `r` members preserves the antichain property and the set of
occupied levels.

Consequently, for `r>=4`, equality `g(n,r)=n-3` is equivalent to
feasibility of the full prescribed profile

\[
f_i=r\quad(2\le i\le n-2),
\qquad f_i=0\quad\text{otherwise}.
\]

We use the classical Clements--Daykin--Godfrey--Hilton criterion in the
form proved in `docs/TECHNICAL_NOTE.md`: if

\[
m_s=f_s,\qquad
m_i=f_i+\partial_{i+1}(m_{i+1}),
\]

then the profile is feasible on `[n]` if and only if

\[
m_i\le\binom ni
\]

at every relevant level.

## 2. The obstruction at `n=2r+4`

For each `4<=r<=10`, run the exact recurrence for the full profile at

\[
n=2r+4.
\]

It overflows at level `2` as follows.

| `r` | `n=2r+4` | `m_2` | `C(n,2)` | overflow |
|---:|---:|---:|---:|---:|
| 4 | 12 | 67 | 66 | 1 |
| 5 | 14 | 92 | 91 | 1 |
| 6 | 16 | 121 | 120 | 1 |
| 7 | 18 | 155 | 153 | 2 |
| 8 | 20 | 192 | 190 | 2 |
| 9 | 22 | 233 | 231 | 2 |
| 10 | 24 | 278 | 276 | 2 |

Thus

\[
g(2r+4,r)<2r+1=(2r+4)-3,
\]

so the threshold cannot be smaller than `2r+4`:

\[
n_0(r)\ge2r+4.
\]

Only this single failed value is needed for the threshold lower bound.  If
`n_0(r)<=2r+3`, the definition would require success at `n=2r+4`.

## 3. The tight full profile at `n=2r+5`

At

\[
n=2r+5,
\]

the same recurrence is feasible for every `4<=r<=10`, and it is exactly
tight at level `2`:

| `r` | `n=2r+5` | `m_2` | `C(n,2)` |
|---:|---:|---:|---:|
| 4 | 13 | 78 | 78 |
| 5 | 15 | 105 | 105 |
| 6 | 17 | 136 | 136 |
| 7 | 19 | 171 | 171 |
| 8 | 21 | 210 | 210 |
| 9 | 23 | 253 | 253 |
| 10 | 25 | 300 | 300 |

The sufficiency direction of the profile theorem therefore gives an
explicit colex antichain on `[2r+5]` with exactly `r` members on every
level `2,...,2r+3`.  These seven witnesses are stored in

```text
certificates/small_r_full_witnesses_r4_to_10.txt
```

and are checked by direct pairwise containment tests, independently of the
shadow computation.

Hence

\[
g(2r+5,r)=2r+2=(2r+5)-3.
\]

## 4. A base core and explicit free sets

For each `4<=r<=10`, put

\[
q=r+5,\qquad s=r+2.
\]

The core profile with `r` sets on every level `2,...,s` is feasible on
`q` points.  Its bottom recurrence values are:

| `r` | `q` | core `m_2` | `C(q,2)` | slack |
|---:|---:|---:|---:|---:|
| 4 | 9 | 31 | 36 | 5 |
| 5 | 10 | 41 | 45 | 4 |
| 6 | 11 | 51 | 55 | 4 |
| 7 | 12 | 62 | 66 | 4 |
| 8 | 13 | 74 | 78 | 4 |
| 9 | 14 | 87 | 91 | 4 |
| 10 | 15 | 101 | 105 | 4 |

The canonical colex core has an explicit family of `r` free
`(s-1)=(r+1)`-sets.  Write

\[
X=[q-2],\qquad J=\{4,5,\ldots,q-2\}.
\]

The first `r=q-5` top-level core sets are

\[
X\setminus\{j\},\qquad j\in J.
\]

Among the `(q-4)`-subsets of `X`, their shadow misses exactly

\[
X\setminus\{1,2\},\qquad
X\setminus\{1,3\},\qquad
X\setminus\{2,3\}.
\]

These are the first three available sets in colex.  The down-closure of
the top sets together with these three sets contains every subset of `X`
of size at most `q-5`: a subset not containing all of `J` lies in a top
set, while a subset of size at most `|J|=q-5` that contains all of `J` is
`J` itself and lies in each exceptional set.

It follows that every later core member contains `q-1` or `q`.  For each
`j in J`, define

\[
D_j=[q]\setminus\{1,j,q-1,q\}.
\]

There are exactly `r` such sets, each of size `q-4=r+1`.  No core member
is contained in `D_j`:

- a top member is larger than `D_j`;
- each of the three exceptional members has the same size and contains
  `j`, whereas `D_j` omits `j`;
- every later member contains `q-1` or `q`, while `D_j` contains neither.

Thus the `D_j` are free.  The complete stored cores and free sets are in

```text
certificates/small_r_cores_and_free_sets_r4_to_10.txt
```

## 5. Padding to every `n>=2r+6`

The two-point padding lemma from `docs/TECHNICAL_NOTE.md` applies without
any large-`r` hypothesis.  If a core on `q` points has `r` sets on levels
`2,...,s` and free sets `D_1,...,D_r` of size `s-1`, then adding two new
points `x,y` and the sets

\[
D_i\cup\{x,y\}\qquad(1\le i\le r)
\]

produces a core with the next occupied level.

Freeness persists indefinitely.  After earlier padding pairs
`{x_h,y_h}`, use

\[
D_i^{(t)}=D_i\cup\{x_1,\ldots,x_t\}.
\]

A base-core member cannot lie in `D_i^{(t)}` because it would lie in
`D_i`, and a member born at stage `h` contains `y_h`, which
`D_i^{(t)}` omits.

Starting from `(q,s)=(r+5,r+2)`, after `t` stages the core parameters are

\[
(q_t,s_t)=(r+5+2t,r+2+t).
\]

The core-to-full construction then gives the full profile for both

\[
n=2r+6+2t
\quad\text{and}\quad
n=2r+7+2t.
\]

Therefore

\[
g(n,r)=n-3\qquad\text{for every }n\ge2r+6.
\]

Together with the direct full-profile construction at `n=2r+5`, this
proves

\[
n_0(r)\le2r+4.
\]

Combining with Section 2 gives the theorem.


## 6. The transition at `r=11`

The finite thresholds also explain why the uniform formula changes at
`r=11`.  Let `A=r+4`, and run the upper core recurrence with `r` sets on
levels `2,...,r+2`.  Write

\[
a_3=\binom A3+e_r.
\]

Exact cascade arithmetic gives

| `r` | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `e_r` | -7 | -4 | -3 | -2 | -2 | -2 | -2 | 1 |

Thus the core residual remains below the binomial shell through `r=10`,
but crosses it at `r=11`.  This is the same carry that, in the uniform
argument, obstructs the full profile at `n=2r+5`.  The threshold jump

\[
2r+4\longrightarrow 2r+5
\]

therefore coincides with a sign change in a single combinadic residual.
This observation is explanatory rather than a separate proof dependency.

## 7. Reproducibility

Run

```bash
python3 verification/verify_small_r_exact.py
```

The script is independent of the project profile implementation.  It:

- recomputes every obstruction and feasible profile using its own exact
  Kruskal--Katona cascade;
- parses and directly checks all seven stored full-profile witnesses;
- parses and directly checks all seven stored cores and free-set families;
- directly checks five persistent padding stages and the resulting full
  witnesses for both parities at every tested stage.

Expected final lines:

```text
PASS: n_0(r)=2r+4 is certified for every 4 <= r <= 10
```

The proof for all larger `n` is the symbolic persistent-padding argument in
Section 5, not an inference from a finite scan.

\newpage

# Part III: the L4 reverse-envelope theorem

# L4: a proof that α_r ≤ r − 1 (all r ≥ 29)

*Standalone companion to `UNIFORM_THEOREM.md`. The proof is symbolic for
all \(r\ge29\); the finite range \(11\le r<29\) is checked by
`verification/verify_l4.py`. This note uses only the classical
Kruskal--Katona shadow function and elementary binomial identities.*


## Cascade notation

For \(m\ge0\) and \(k\ge1\), write the canonical cascade
\[
m=\binom{a_k}{k}+\binom{a_{k-1}}{k-1}+\cdots+\binom{a_s}{s},
\qquad a_k>a_{k-1}>\cdots>a_s\ge s,
\]
and define
\[
\partial_k(m)=\binom{a_k}{k-1}+\binom{a_{k-1}}{k-2}+\cdots+
\binom{a_s}{s-1}.
\]
We use monotonicity of \(\partial_k\), Pascal's identity, and the fact that
shadowing a displayed canonical cascade lowers each position by one.

## 0. Statement

**Theorem L4.** For every r ≥ 29 the profile [r sets of every size
2..r, r sets of size r+1] on A = r+4 points is infeasible; equivalently
α_r ≤ r−1. The finite range 11 ≤ r < 29 is checked exactly by
`verification/verify_l4.py`.

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
The difference is therefore exactly r+i−5. \(\square\)

**Lemma IND (the bound).** If the profile is feasible then
c_i ≤ Ĝ_i for every 2 ≤ i ≤ r−2.
*Proof.* c_2 ≤ C(A,2) = Ĝ_2. Inductively, if c_{i−1} ≤ Ĝ_{i−1} and
c_i ≥ Ĝ_i + 1, then by monotonicity c_{i−1} = r + ∂_i(c_i) ≥ r + ∂_i(Ĝ_i+1)
> Ĝ_{i−1}, a contradiction; so c_i ≤ Ĝ_i. \(\square\)

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
    (positions r−2, r−3, r−4 for the three leading terms). \(\square\)

(These three identities are re-verified numerically for every r in the
verification range; the verifier recomputes the chain with the
independent exact kk_shadow.)

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
is infeasible and α_r ≤ r − 1 for all r ≥ 29. \(\square\)

## 4. Remarks

1. **Uniformity.** Unlike the lower half, there is no upper threshold:
   the forward chain is used only three levels deep, so no top-zone
   budget arises. L4 is proved for ALL r ≥ 29.
2. **Reverse-step margins.** The quantity
   \(r+\partial_i(\widehat G_i+1)-\widehat G_{i-1}\) equals 1 for
   \(i=3,\ldots,7\), equals \(r+135\) at \(i=8\), and has the exact
   positive values displayed above thereafter. The final contradiction
   margin is positive (and equals \(r\) for \(r\ge31\)). The knife-edge lives entirely in the six head
   computations — which mirror (and were extracted from) the exactly
   tight true-anchor envelope.
3. **Sharper nearby behavior (not needed).** Exploratory exact
   computations in the research-history notes suggest the stronger value
   \(\alpha_r=r-2\) over a substantial tested range. This is not used or
   claimed here.
4. **Verification.** `verification/verify_l4.py` checks the exact finite
   base \(11\le r<29\) and recomputes every reverse step, the three top
   identities, and the final margin at representative values through
   \(r=1000\). The proof above is symbolic and
   does not depend on any stress test.

## 5. Consequences (dependency update)

With L4 proved for \(r\ge29\), and the finite base checked for
\(11\le r<29\):

- L5 follows immediately. Its two top singleton loads induce cumulative
  load \(r+3\) at level \(r+1\), larger than the L4-admissible maximum
  \(r-1\).
- The one-seed residual recurrence used in the full-profile obstruction
  dominates the L4 recurrence by monotonicity.
- Together with the uniform lower-window theorem in `UNIFORM_THEOREM.md`,
  this supplies the upper half of the core window for every \(r\ge11\).

\newpage

# Part IV: the uniform theorem for r >= 11

# A uniform threshold for the Erdős–Trotter antichain problem

**Status:** Pending review
**Date:** 2026-07-16
**Main new result in this note:** a uniform proof of
\[
\alpha_r\ge r-6\qquad(r\ge 11),
\]
where \(\alpha_r\) is the largest \(y\) for which the profile
\[
f_i=r\quad(2\le i\le r),\qquad f_{r+1}=y
\]
is feasible on \(r+4\) points.

Together with the companion L4 proof \(\alpha_r\le r-1\), the classical
prescribed-profile criterion, the diagonal transfer identity, and the
already-verified padding/free-set construction, this yields
\[
\boxed{n_0(r)=2r+5\qquad(r\ge11).}
\]

The point of this proof is that the old top-zone cutoff \(r\le 28\,710\)
disappears. The replacement is:

1. follow the exact anchor ladder as far as it naturally goes;
2. complete one additional anchor;
3. build a short sequence of compressed phases;
4. use a one-digit rising tail to enter an exact generalized envelope;
5. let a small scalar recurrence perform the entire bottom collapse.

The proof uses two finite exact checks: the lower-window base
\(11\le r\le377\), consisting of 367 integer cascade computations, and
the L4 base \(11\le r\le28\), consisting of 18 exact profile checks.
The lower window is symbolic for \(r\ge378\), while L4 is symbolic for
\(r\ge29\). Additional witness checks and adversarial computations archived
with this repository are independent falsification tests rather than
logical substitutes for the symbolic arguments.

---

## 1. Kruskal--Katona notation

For \(m\ge0\) and \(k\ge1\), write the \(k\)-cascade of \(m\) as
\[
m=\binom{a_k}{k}+\binom{a_{k-1}}{k-1}+\cdots+\binom{a_s}{s},
\qquad
a_k>a_{k-1}>\cdots>a_s\ge s.
\]
Set
\[
\partial_k(m)
=
\binom{a_k}{k-1}
+\binom{a_{k-1}}{k-2}
+\cdots+
\binom{a_s}{s-1},
\qquad
\partial_k(0)=0.
\]

For a profile \(f\), the classical Clements--Daykin--Godfrey--Hilton
criterion says that, with
\[
m_s=f_s,\qquad
m_i=f_i+\partial_{i+1}(m_{i+1}),
\]
the profile is feasible on \(n\) points if and only if
\[
m_i\le\binom ni
\]
at every level.

A self-contained necessity-and-sufficiency proof, together with the
canonical colex construction, is given in
[`TECHNICAL_NOTE.md`, Section 2](../docs/TECHNICAL_NOTE.md#2-exact-profile-criterion).

We repeatedly use two elementary facts.

### Monotonicity

If \(x\le y\), then
\[
\partial_k(x)\le\partial_k(y).
\]

### Completion of a constant-offset run

A finite cascade run
\[
\binom d p+\binom{d-1}{p-1}+\cdots+\binom{d-\ell}{p-\ell}
\]
is bounded above by the corresponding completed binomial
\[
\binom{d+1}{p}.
\]
This is just Pascal/hockey-stick expansion. Consequently, after a run is
shadowed, it may be rounded up to its completed stone in a supersolution.

A **supersolution** for the recurrence is a sequence \(V_i\) satisfying
\[
V_{i-1}\ge r+\partial_i(V_i).
\]
If the exact recurrence is below \(V_i\) at one level, monotonicity keeps it
below the supersolution at every lower level.

---

# Part I. The uniform lower window

## 2. The lower-window recurrence

Put
\[
A=r+4.
\]
To prove \(\alpha_r\ge r-6\), it is enough to show that the recurrence
\[
m_{r+1}=r-6,\qquad
m_i=r+\partial_{i+1}(m_{i+1})
\quad(i=r,r-1,\ldots,2)
\tag{2.1}
\]
satisfies
\[
m_i\le\binom Ai
\qquad(2\le i\le r+1).
\tag{2.2}
\]

The range \(11\le r\le377\) is checked exactly in Section 12. Hence assume
throughout Sections 3--11 that
\[
r\ge378.
\]

---

## 3. Exact anchor ladder

Define
\[
T_0=28,\qquad
T_{q+1}=\binom{T_q-2q}{2},
\tag{3.1}
\]
and put
\[
B_q=T_q-2q.
\]
Thus
\[
T_1=378,\qquad
T_2=70\,500,\qquad
T_3=2\,484\,807\,760,
\]
and so on.

For integers \(a\le b\), write
\[
U(a,b)=\sum_{x=a}^{b}\binom xx,
\]
with \(U(a,b)=0\) if \(a>b\).

### Lemma 3.1: exact anchors

If \(r\ge T_q\), then the exact recurrence (2.1) satisfies
\[
\boxed{
m_{r-q}
=
\sum_{j=0}^{q}
\binom{r+2-2j}{r-q-j}
+
U(B_q,r-2q-1).
}
\tag{3.2}
\]

#### Proof

For \(q=0\), the \(r-6\) top sets are unary at level \(r+1\), so
\[
m_r
=
\binom{r+2}{r}
+
U(28,r-1).
\]

Assume (3.2). Let
\[
N=r-2q.
\]
After taking one shadow, the unary part contributes
\[
\sum_{x=B_q}^{N-1}x
=
\binom N2-\binom{B_q}{2}.
\]
Adding the new flow \(r\) gives
\[
\binom N2+\bigl(r-T_{q+1}\bigr).
\]
The first term is the new anchor
\[
\binom N{N-2},
\]
and, when \(r\ge T_{q+1}\), the residual \(r-T_{q+1}\) is the unary block
\[
U(T_{q+1}-2q-2,r-2q-3)
=
U(B_{q+1},r-2(q+1)-1).
\]
This proves the induction. \(\square\)

### Capacity on the exact top segment

The exact states just constructed already satisfy the required capacity
bounds. At the top level,
\[
m_{r+1}=r-6<\binom{r+4}{r+1}.
\]
At level \(i=r-q\) in Lemma 3.1, the canonical cascade has leading digit
\(r+2\) at position \(i\), and every remaining digit is strictly smaller.
The remaining positions form a canonical cascade of index at most \(i-1\)
whose digits are at most \(r+1\), so its value is strictly less than
\(\binom{r+2}{i-1}\). Consequently
\[
m_i<\binom{r+2}{i}+\binom{r+2}{i-1}
=\binom{r+3}{i}
<\binom{r+4}{i}.
\]
Thus every level from \(r+1\) down through the last exact anchor level
fits on the \(A=r+4\)-point ground set.

Choose \(t\ge1\) maximal such that
\[
T_t\le r<T_{t+1}.
\tag{3.3}
\]
Set
\[
N=r-2t,\qquad
c=2t+3,\qquad
h=t+2.
\tag{3.4}
\]

A useful elementary bound is
\[
T_t\ge128t+250
\qquad(t\ge1).
\tag{3.5}
\]
It is equality at \(t=1\), and the induction step follows immediately from
(3.1). In particular,
\[
r\ge64c.
\tag{3.6}
\]

---

## 4. Complete one additional anchor

At level
\[
I=r-t,
\]
Lemma 3.1 gives the exact state. Descending one more level, the residual
below the old anchors is
\[
\binom N2-\bigl(T_{t+1}-r\bigr).
\]
Since \(r<T_{t+1}\), this is at most \(\binom N2\). It is also
nonnegative: since \(r\ge T_t\),
\[
N=r-2t\ge T_t-2t=B_t,
\]
and therefore
\[
\binom N2-\bigl(T_{t+1}-r\bigr)
=\binom N2-\binom{B_t}{2}+r\ge0.
\]
We therefore round it up and define
\[
V_{I-1}
=
\sum_{j=0}^{t+1}
\binom{r+2-2j}{I-1-j}.
\tag{4.1}
\]
This is a valid supersolution step.

The new final anchor is \(N\), and after one shadow it sits at position
\(N-3\). At the next level
\[
b_1=I-2=r-t-2
\]
place beneath it the two-term run
\[
\binom{N-3}{N-4}
+
\binom{N-4}{N-5}.
\tag{4.2}
\]
Its value is
\[
2N-7\ge r
\tag{4.3}
\]
by (3.5). Thus (4.2) pays the next flow.

Define the tower stones
\[
\boxed{
s_j=r+1-c\,2^{j-1}
\qquad(j\ge1).
}
\tag{4.4}
\]
Then
\[
s_1=N-2,
\]
and the run in (4.2) has top digit \(s_1-1\). Moreover
\[
s_{j+1}=2s_j-r-1.
\tag{4.5}
\]

---

## 5. Choice of the final phase

Let \(K\) be the unique integer satisfying
\[
c\,2^{K-1}\le\frac r4<c\,2^K.
\tag{5.1}
\]
Because of (3.6), \(K\ge5\).

For \(1\le j\le K\),
\[
s_j\ge\frac{3r}{4}+1,
\tag{5.2}
\]
and
\[
s_{K+1}\ge\frac r2+1.
\tag{5.3}
\]

The first phase begins with top position
\[
u_1=N-4.
\tag{5.4}
\]
It already has two terms, as in (4.2).

For the first phase, set
\[
\ell_1=\left\lfloor\frac{u_1-5}{2}\right\rfloor.
\tag{5.5}
\]
After \(\ell_1\) extensions, the run bottom is \(4\) or \(5\). Harvest the
run to \(s_1\) and birth phase \(2\).

For every later ordinary phase \(j\ge2\), if its top position is \(u_j\),
set
\[
\ell_j=\left\lfloor\frac{u_j-4}{2}\right\rfloor,
\qquad
u_{j+1}=u_j-\ell_j-2
=\left\lceil\frac{u_j}{2}\right\rceil.
\tag{5.6}
\]
The first transition differs by at most one:
\[
u_2\le\left\lceil\frac{u_1}{2}\right\rceil+1.
\]

Let \(b_j\) be the birth level of phase \(j\). Then
\[
b_1=I-2,
\qquad
b_{j+1}=b_j-\ell_j-1,
\tag{5.6a}
\]
and
\[
\boxed{b_j-u_j=h+j-1=t+j+1.}
\tag{5.6b}
\]
The identity holds at \(j=1\), because
\((I-2)-(N-4)=t+2=h\). A harvest decreases the level by
\(\ell_j+1\) and the next active top position by \(\ell_j+2\), so the
slot increases by exactly one. In particular, the phases cover every
intervening level without gaps.

Consequently
\[
\frac{u_1}{2^{j-1}}
\le u_j
\le
\frac{u_1}{2^{j-1}}+2.
\tag{5.7}
\]
For completeness, the lower bound follows because every transition is at
least halving. For the upper bound, the exceptional first transition gives
\(u_2\le u_1/2+3/2\le u_1/2+2\). If the upper bound holds at some
\(j\ge2\), then
\[
u_{j+1}=\left\lceil\frac{u_j}{2}\right\rceil
\le \frac{u_1}{2^j}+\frac32
\le \frac{u_1}{2^j}+2,
\]
which proves the two-case induction.
Using (5.1), (5.7), and \(u_1>3r/4\), we get
\[
\boxed{
3c\le u_K\le8c+2.
}
\tag{5.8}
\]


### Lemma 5.1: quantitative phase bounds

The estimates used in Sections 6--8 follow uniformly from the preceding
parameters:

1. \(3c\le u_K\le8c+2\).
2. Every phase-1 extension term in (6.1) has lower index at least \(4\),
   complementary index at least \(2\), and upper digit at least
   \((N-1)/2\).
3. Every later ordinary extension term in (6.3) has lower index at least
   \(4\), complementary index at least \(2\), and upper digit at least
   \(r/2-3\).
4. Every newborn term at an ordinary harvest has upper digit at least
   \(3r/4\), lower index at least \(2\), and complementary index at least
   \(2\); hence it has value greater than \(r\).
5. In the final rising-tail zone, \(d_p\ge3r/8\) whenever \(p\ge4\).
6. The terminal envelope level satisfies \(L<r/4\).

*Proof.* From \(u_1=r-c-1\), (5.1), and (5.7),
\[
u_K\ge \frac{r-c-1}{2^{K-1}}
\ge 4c-\frac{4c(c+1)}r>3c,
\]
where the last inequality uses \(r\ge64c\). The other half of (5.1)
gives \(2^{-(K-1)}<8c/r\), hence
\[
u_K\le\frac{u_1}{2^{K-1}}+2<8c+2.
\]

For phase 1, the extension in (6.1) has index
\(u_1-3-2\ell\), which is at least \(4\) because
\(\ell<\ell_1\). Its complementary index is
\[
(s_1-3-\ell)-(u_1-3-2\ell)=2+\ell,
\]
and the endpoint choice of \(\ell_1\) gives upper digit at least
\((N-1)/2\).

For a later phase, the index in (6.3) is at least \(4\). Its complementary
index equals
\[
s_j-u_j+\ell.
\]
For \(2\le j\le K-1\), we have \(c2^{j-1}\le r/8\) and
\(u_j\le r/2+2\), so
\[
s_j-u_j\ge r+1-\frac r8-\left(\frac r2+2\right)>2.
\]
Also \(\ell\le u_j/2\), and therefore
\[
s_j-2-\ell\ge \frac{3r}{4}-1-\frac{r/2+2}{2}
\ge \frac r2-3.
\]
At harvest, the next stone has digit at least \(3r/4+1\), so the newborn
active digit is at least \(3r/4\). Its position is at most \(r/2+2\),
and the preceding bounds leave both index and complementary index at least
\(2\); its value is therefore at least \(\binom{3r/4}{2}>r\).

In the final zone, \(D\ge r/2+3\) and \(p\le u-1\le r/8+1\), so
\[
d_p=D-p+1\ge\frac{3r}{8}+3>\frac{3r}{8}.
\]
Finally, (3.5) gives \(t<r/128\), while (5.1) gives
\(K\le\log_2 r\). Thus
\[
L=t+K+4<\frac r{128}+\log_2r+4<\frac r4
\qquad(r\ge378).
\]
\(\square\)

---

## 6. Ordinary phase transitions

The full active-run invariant is as follows. At level \(b_1-L\), after
\(L\) completed phase-1 extensions, the active run is
\[
R_{1,L}=\sum_{p=0}^{L+1}
\binom{s_1-1-p}{u_1-L-p},
\qquad 0\le L\le\ell_1.
\tag{6.0a}
\]
For every later phase \(j\ge2\), at level \(b_j-L\), after \(L\)
completed extensions, the active run is
\[
R_{j,L}=\sum_{p=0}^{L}
\binom{s_j-1-p}{u_j-L-p},
\qquad 0\le L\le\ell_j.
\tag{6.0b}
\]
The completed anchors and stones simply shadow one position at a time.
The digits and positions in each run both decrease by one as \(p\)
increases, so the displayed runs are canonical. After one further shadow,
the hockey-stick completion dominates the old run, and the newborn term
sits at \(u_j-\ell_j-2=u_{j+1}\). These formulas fix the meanings of
“extension”, “harvest”, and “birth” below.

### Phase 1

At birth level \(b_1=I-2\), phase \(1\) consists of
\[
s_1-1,\ s_1-2
\]
at positions
\[
u_1,\ u_1-1.
\]
For \(0\le\ell<\ell_1\), shadow to level
\(b_1-1-\ell=I-3-\ell\) and append
\[
\binom{s_1-3-\ell}{u_1-3-2\ell}.
\tag{6.1}
\]
Whenever this extension is used, its lower index is at least \(4\), its
complement is at least \(2\), and its upper digit is at least
\[
\frac{N-1}{2}.
\]
From (3.5), \(t\le(r-250)/128\), so
\[
N=r-2t\ge \frac{63r}{64}+\frac{125}{32}>\frac r2.
\]
Thus the upper digit is larger than \(r/4-1\); for \(r\ge378\), even the
smaller endpoint binomial \(\binom{\lfloor r/4\rfloor-1}{2}\) exceeds
\(r\). For a fixed upper digit, a binomial coefficient whose index and
complementary index are both at least \(2\) is at least its endpoint value
\(\binom d2\). Since the actual lower index is at least \(4\) and the
complementary index is at least \(2\), we obtain
\[
\binom{s_1-3-\ell}{u_1-3-2\ell}\ge r.
\tag{6.2}
\]

### Phases \(2,\ldots,K-1\)

At birth level \(b_j\), phase \(j\) begins with
\[
\binom{s_j-1}{u_j}.
\]
For \(0\le\ell<\ell_j\), shadow to level \(b_j-1-\ell\) and append
\[
\binom{s_j-2-\ell}{u_j-2\ell-2}.
\tag{6.3}
\]
For \(j\le K-1\), (5.2), (5.7), and (5.8) imply that throughout every
extension:

- the lower index is at least \(4\);
- the complementary index is at least \(2\);
- the upper digit is at least \(r/2-3\).

Hence
\[
\binom{s_j-2-\ell}{u_j-2\ell-2}
\ge
\binom{r/2-3}{2}
>r.
\tag{6.4}
\]

At a harvest step, completion of the old run costs nothing: the completed
stone dominates its shadow. The newly born active term for the next phase
has upper digit at least \(3r/4\), while its position lies between \(2\)
and \(r/2+2\). Therefore that newborn term alone has value greater than
\(r\).

Thus every ordinary in-phase and harvest transition is a valid
supersolution step.

---

## 7. A one-digit final zone

At the harvest of phase \(K-1\), namely at level \(b_K\), do not birth
an ordinary phase \(K\). Instead, place the completed stone \(s_K\) at
position \(u_K\), and place the new tail immediately below it at position
\(u_K-1\). Completion of the
old phase-\((K-1)\) run dominates its shadow, while
\[
\binom{s_K}{u_K}
\ge \binom{3r/4}{2}>r.
\]
Thus the new \(s_K\)-term alone pays the incoming flow; the tail introduced
below it is additional slack.

Put
\[
u=u_K,\qquad
D=s_{K+1}+2.
\tag{7.1}
\]
At the position immediately below \(s_K\), namely \(u-1\), place the digit
\[
d_{u-1}=D-u+2.
\tag{7.2}
\]

As the construction descends, let this one tail digit move from position
\(p\) to \(p-1\), while changing according to
\[
d_p=
\begin{cases}
D,&p=2,\\
D-p+1,&p\ge3.
\end{cases}
\tag{7.3}
\]

Thus the digit rises by \(1\) at every step except the final transition
\(3\to2\), where it rises by \(2\).

### Canonical validity

From (5.1),
\[
s_K-D=c2^{K-1}-2>0.
\]
Also, by (5.3), (5.8), and (3.6),
\[
D\ge \frac r2+3,
\qquad
u\le\frac r8+2.
\]
Hence
\[
D-u+2\ge u-1,
\]
so the initial tail term is valid, and it remains strictly below \(s_K\).

### Gain at each step

For \(p\ge4\), the gain from raising by one is
\[
\binom{d_p+1}{p-1}-\binom{d_p}{p-1}
=
\binom{d_p}{p-2}.
\tag{7.4}
\]
Here
\[
d_p\ge\frac{3r}{8},
\qquad
2\le p-2\le d_p-2,
\]
so (7.4) is greater than \(r\).

For the last step,
\[
\binom D2-\binom{D-2}{2}
=
2D-3
\ge r.
\tag{7.5}
\]

Therefore the rising tail pays every remaining flow.

After \(u-3\) steps, \(s_K\) has reached position \(3\), and the tail has
reached position \(2\) with digit \(D=s_{K+1}+2\). The level reached is
\[
b_K-(u_K-3)=(b_K-u_K)+3=h+K+2.
\tag{7.5a}
\]
More generally, once \(s_q\) is completed, its permanent slot is
\[
\text{level}-\text{position}=h+q-1.
\tag{7.5b}
\]
This is the simultaneous alignment invariant at the Section 7/8 seam.

Let
\[
L=h+K+2.
\tag{7.6}
\]
The state at level \(L\) is exactly the generalized envelope introduced
next.

---

## 8. Exact generalized envelope

For \(h+3\le i\le L\), define
\[
\boxed{
E_i
=
\sum_{j=0}^{h-1}
\binom{r+2-2j}{i-j}
+
\sum_{q=1}^{i-h-2}
\binom{s_q}{i-h-q+1}
+
\binom{s_{i-h-1}+2}{2}.
}
\tag{8.1}
\]

At level \(L\), this is exactly the endpoint of Section 7. Indeed, by
(7.5b), stone \(s_q\) occupies position
\(L-(h+q-1)=L-h-q+1\), exactly its position in the second sum of (8.1);
\(s_K\) is at position \(3\), and the tail \(s_{K+1}+2\) is at position
\(2\).

The representation is canonical:

- the initial anchors fall by \(2\);
- \(r-2t=N>s_1=N-2\);
- successive tower stones satisfy \(s_q>s_{q+1}\);
- the terminal digit \(s_{i-h-1}+2\) is still below the preceding stone.

Moreover, all tower digits used here are at least \(s_{K+1}\ge r/2+1\).
From (3.5), \(t<r/128\); from (5.1), \(K\le\log_2 r\). Hence
\[
L=t+K+4
<
\frac r{128}+\log_2 r+4
<
\frac r4
\qquad(r\ge378),
\]
so every digit is above its position.

### Exact envelope step

The fixed anchors and old stones simply shift under one shadow. At the
bottom, write
\[
m=i-h-1.
\]
The difference needed to pass from \(E_i\) to \(E_{i-1}\) is
\[
\binom{s_{m-1}+2}{2}
-
\binom{s_{m-1}}{2}
-
(s_m+2).
\]
Using (4.5), this equals
\[
2s_{m-1}-s_m-1=r.
\]
Hence
\[
\boxed{
E_{i-1}=r+\partial_i(E_i)
\qquad(h+4\le i\le L).
}
\tag{8.2}
\]

---

## 9. Collision of the extra anchors

At level
\[
i=h+3=t+5,
\]
the last anchor is \(N\) at position \(4\), the first tower stone is
\[
s_1=N-2
\]
at position \(3\), and the terminal digit is \(s_2+2\) at position \(2\).

After one shadow and addition of \(r\), the part below the shifted \(N\)
anchor is
\[
\binom{N-2}{2}+(s_2+2)+r.
\]
Since
\[
s_2+2=r-4t-3
\]
and
\[
\binom N2-\binom{N-2}{2}=2N-3=2r-4t-3,
\]
this part is exactly \(\binom N2\). It merges with \(\binom N3\) to give
\(\binom{N+1}{3}\).

Thus, at level \(t+4\), the state is
\[
F_t(0),
\]
where for \(0\le q\le t\) and \(z\ge0\) we define
\[
\boxed{
F_q(z)
=
\sum_{j=0}^{q}
\binom{r+2-2j}{q+4-j}
+
\binom{r-2q+1}{3}
+
z,
}
\tag{9.1}
\]
with \(z\) inserted in its \(2\)-cascade below the displayed position-\(3\)
term.

---

## 10. Scalar bottom collapse

Set
\[
z_t=0,
\]
and for \(q=t,t-1,\ldots,1\), define
\[
\boxed{
z_{q-1}=2q-1+\partial_2(z_q).
}
\tag{10.1}
\]

The residuals really do append canonically below the position-\(3\) digit.
For \(q\ge6\), the proof of Lemma 10.2 gives \(z_q\le q^2\), so the top
digit of the \(2\)-cascade of \(z_q\) is at most \(2q\). For the smaller
indices the same proof gives
\[
z_5\le20,\quad z_4\le16,\quad z_3\le14,\quad z_2\le11,\quad z_1\le9.
\tag{10.1a}
\]
Since \(\binom72=21\), their top \(2\)-cascade digit is at most \(6\).
On the other hand, by (3.5),
\[
r-2q+1\ge r-2t+1>2q.
\]
Thus no residual carry enters the displayed position-\(3\) digit.

### Lemma 10.1

For every \(q\ge1\),
\[
r+\partial_{q+4}\bigl(F_q(z_q)\bigr)
=
F_{q-1}(z_{q-1}).
\tag{10.2}
\]

#### Proof

At level \(q+4\), the last ordinary anchor has digit
\[
a=r-2q+2
\]
at position \(4\), and the special digit is \(a-1\) at position \(3\).
After shadowing, filling the position-\(2\) term from
\(\binom{a-1}{2}\) to \(\binom a2\) costs
\[
a-1=r-2q+1.
\]
The incoming amount is
\[
r+\partial_2(z_q).
\]
The excess is therefore
\[
r+\partial_2(z_q)-(r-2q+1)
=
2q-1+\partial_2(z_q)
=
z_{q-1}.
\]
Finally,
\[
\binom a3+\binom a2=\binom{a+1}{3},
\]
which is precisely the new special digit in \(F_{q-1}\). \(\square\)

### Lemma 10.2: terminal residual

The recurrence (10.1) gives
\[
z_0=
\begin{cases}
1,&t=1,\\
4,&t=2,\\
6,&t\ge3.
\end{cases}
\tag{10.3}
\]

#### Proof

The cases \(t=1,2\) are direct.

Assume \(t\ge3\). We first show
\[
5\le z_2\le11.
\tag{10.4}
\]
The lower bound follows from the \(q=3\) step.

For the upper bound, the first three cases are
\[
\begin{array}{c|c}
t & (z_t,z_{t-1},\ldots,z_0)\\
\hline
3&(0,5,7,6)\\
4&(0,7,10,8,6)\\
5&(0,9,12,11,9,6).
\end{array}
\]
If \(t\ge6\), use the invariant
\[
z_q\le q^2\qquad(q\ge6).
\]
Indeed, if \(q\ge7\) and \(z_q\le q^2\), let \(a_2\) be the top digit
of the canonical \(2\)-cascade of \(z_q\). If \(a_2\ge2q\), then
\(z_q\ge\binom{2q}{2}>q^2\), a contradiction. Hence
\(a_2\le2q-1\). A possible position-$1$ term contributes only one more
to the shadow, so
\[
\partial_2(z_q)\le a_2+1\le2q.
\]
Therefore
\[
z_{q-1}\le4q-1\le(q-1)^2.
\]
Starting from \(z_t=0\), this yields \(z_6\le36\). Hence
\[
z_5\le11+9=20,\qquad
z_4\le9+7=16,\qquad
z_3\le7+7=14,
\]
and then
\[
z_2\le5+6=11.
\]

For \(5\le z_2\le11\),
\[
4\le\partial_2(z_2)\le6,
\]
so
\[
7\le z_1\le9.
\]
Every integer from \(7\) through \(9\) has \(2\)-shadow \(5\). Thus
\[
z_0=1+5=6.
\]
\(\square\)

---

## 11. The final two levels

At level \(4\), the state is
\[
F_0(z_0)
=
\binom{r+2}{4}
+
\binom{r+1}{3}
+
z_0.
\]

Descending to level \(3\) gives
\[
E_3
=
\binom{r+3}{3}
+
\bigl(\partial_2(z_0)-1\bigr).
\tag{11.1}
\]
By Lemma 10.2,
\[
E_3=
\begin{cases}
\binom{r+3}{3}+1,&t=1,\\[2mm]
\binom{r+3}{3}+3,&t\ge2.
\end{cases}
\tag{11.2}
\]

Therefore
\[
E_2=r+\partial_3(E_3)
=
\begin{cases}
\binom{r+4}{2}-1,&t=1,\\[2mm]
\binom{r+4}{2},&t\ge2.
\end{cases}
\tag{11.3}
\]

All higher constructed states have canonical leading digit \(r+2\), so
they are strictly below
\[
\binom{r+3}{i}<\binom{r+4}{i}.
\]
The level-\(3\) values in (11.2) also lie well below
\(\binom{r+4}{3}\), and (11.3) handles the tight bottom level.

By monotonicity, the exact recurrence (2.1) lies below this supersolution.
This proves
\[
\alpha_r\ge r-6
\qquad(r\ge378).
\]

---

## 12. Finite base \(11\le r\le377\)

For each \(r\) in this range, evaluate (2.1) with exact integer
Kruskal--Katona cascades and check (2.2). A standalone implementation is
provided as `verify_lower_window_base.py`; it does not import the original
project code.

The full sweep has:

- 367 values of \(r\);
- no failures;
- minimum capacity slack \(3\), attained at \(r=20\), level \(2\).

Thus
\[
\boxed{\alpha_r\ge r-6\qquad(r\ge11).}
\tag{12.1}
\]

The standalone verifier `verification/verify_lower_window_base.py` is
archived with this release. It uses exact integer arithmetic; no SAT or
search is involved.

---

# Part II. Assembly of the uniform theorem

The remainder records how the lower window combines with the already
established pieces.

## 13. The L4 upper window

The companion reverse-envelope proof in
[`L4_PROOF.md`](../docs/L4_PROOF.md) establishes
\[
\boxed{\alpha_r\le r-1\qquad(r\ge11).}
\tag{13.1}
\]
It is symbolic for \(r\ge29\), with exact finite verification for
\(11\le r\le28\).

In particular, the profile
\[
r\text{ sets at every level }2,\ldots,r+1
\]
on \(r+4\) points has bottom recurrence value strictly larger than
\(\binom{r+4}{2}\).

L5 is immediate from L4: its two top singleton loads already induce a load
\(r+3\) at level \(r+1\), which exceeds the L4-admissible maximum.

---

## 14. Core carry and feasibility on \(r+5\) points

Put
\[
A=r+4.
\]
Run the recurrence for the core profile
\[
r\text{ sets at every level }2,\ldots,r+2
\]
and write
\[
a_3=\binom A3+e_r.
\]

We now justify the exact relation between the core carry and the window.
Complement the profile defining \(\alpha_r\) on the \(A\)-point ground
set. The reflected profile has \(y\) sets at level \(3\), and \(r\) sets
at levels \(4,\ldots,A-2\). Its cumulative recurrence at every level
\(i\ge4\) is exactly the upper part \(a_i\) of the core recurrence. The
lower-window feasibility \(\alpha_r\ge r-6\ge0\) therefore supplies all
upper capacity inequalities
\[
a_i\le\binom Ai\qquad(4\le i\le A-2).
\tag{14.0}
\]
At level \(3\), the reflected profile is feasible precisely when
\[
y+\partial_4(a_4)\le\binom A3.
\]
Since
\[
a_3=r+\partial_4(a_4)=\binom A3+e_r,
\]
this is equivalent to \(y\le r-e_r\). The upper conditions (14.0) do not
depend on \(y\), and the colex construction attains every such \(y\).
Hence both necessity and sufficiency give
\[
\boxed{\alpha_r=r-e_r.}
\tag{14.1}
\]
Hence Sections 12 and 13 give
\[
1\le e_r\le6.
\tag{14.2}
\]

The lower-window family also shows that every upper core level \(i\ge4\)
fits on \(A\) points. The remaining capacities on \(A+1\) points are
explicit. At level \(3\),
\[
a_3=\binom A3+e_r\le\binom A3+6<\binom{A+1}{3}.
\]
At level \(2\), using (14.2),
\[
\begin{aligned}
a_2
&=
r+\partial_3\left(\binom A3+e_r\right)\\
&=
r+\binom A2+\partial_2(e_r)\\
&\le
r+\binom A2+4\\
&=
\binom{A+1}{2}.
\end{aligned}
\]
For \(i\ge4\), (14.0) gives
\(a_i\le\binom Ai<\binom{A+1}{i}\); the level-3 and level-2 bounds were
just proved. Thus the complete core profile is feasible on
\[
A+1=r+5
\]
points.

---

## 15. Explicit free sets

Let
\[
q=r+5,\qquad X=[q-2],\qquad J=\{4,\ldots,q-2\}.
\]
In the canonical colex core, the first \(r=q-5\) top-level sets are
\[
X\setminus\{j\},
\qquad j\in J.
\]
Among the \((q-4)\)-subsets of \(X\), their lower shadow misses exactly
\[
X\setminus\{1,2\},\qquad
X\setminus\{1,3\},\qquad
X\setminus\{2,3\}.
\tag{15.1}
\]
Indeed, a \((q-4)\)-subset of \(X\) has the form
\(X\setminus\{a,b\}\), and it lies in one of the top sets precisely when
at least one of \(a,b\) belongs to \(J\). Since every subset of \(X\)
precedes every set using \(q-1\) or \(q\) in colex, the three sets in
(15.1) are the first three available sets selected one level lower.

The down-closure of the top sets together with those three newly selected
sets contains every subset of \(X\) of size at most \(q-5\). Let
\(S\subseteq X\) with \(|S|\le q-5=|J|\). If \(S\) omits some
\(j\in J\), then \(S\subseteq X\setminus\{j\}\), one of the top sets. If
it contains all of \(J\), then the size bound forces \(S=J\), which is
contained in each of the three sets in (15.1). Consequently every later
core member contains \(q-1\) or \(q\).

For
\[
4\le j\le q-2,
\]
define
\[
D_j=[q]\setminus\{1,j,q-1,q\}.
\tag{15.2}
\]
There are exactly \(r\) such sets, each of size \(q-4=r+1\). No top core
member is contained in \(D_j\), because every top member contains \(1\).
None of the three exceptional members in (15.1) is contained in \(D_j\),
because it has the same size and contains \(j\). Every later core member
contains \(q-1\) or \(q\), both omitted from \(D_j\). Thus no \(D_j\)
contains a core member: these are the required free sets.

The two-point padding lemma therefore applies indefinitely. At stage
\(t\), retain the persistent free sets
\[
D_j^{(t)}=D_j\cup\{x_1,\ldots,x_t\},
\]
where \(x_h\) is one selected point from the \(h\)-th added pair
\(\{x_h,y_h\}\). An original core member is excluded by freeness of
\(D_j\), and a member born at stage \(h\) contains \(y_h\), which is
absent from \(D_j^{(t)}\). After \(t\) stages the core parameters are
\[
(q,s)=(r+5+2t,r+2+t).
\]
The core-to-full lemma is proved in
[`TECHNICAL_NOTE.md`, Section 4](../docs/TECHNICAL_NOTE.md#4-construction-for-every-nge28).
Applied to the padded core, it gives a full-profile antichain for both
\[
n=2r+6+2t
\quad\text{and}\quad
n=2r+7+2t.
\]
Hence
\[
g(n,r)=n-3
\qquad(n\ge2r+6).
\tag{15.3}
\]

---

## 16. Obstruction at \(n=2r+5\)

Put
\[
B=2r+4.
\]
Let \(M_i\) be the full-profile recurrence for
\[
r\text{ sets at every level }2,\ldots,2r+3
\]
on \(2r+5=B+1\) points.

For every \(i\ge4\), the inequalities in Section 14 are strict. If
\(a_i=\binom Ai\), then the next reflected recurrence level would exceed
capacity because its prescribed load is positive. Thus
\[
0\le a_i<\binom Ai\qquad(4\le i\le A-2).
\tag{16.0}
\]

We use the following diagonal cascade identity. If
\[
t\ge0,\qquad 1\le b<A,\qquad 0\le x<\binom Ab,
\]
then
\[
\boxed{
\partial_{b+t}\left(
\binom{A+t}{b+t}-\binom Ab+x
\right)
=
\binom{A+t}{b+t-1}-\binom A{b-1}+\partial_b(x).
}
\tag{16.1}
\]
Indeed,
\[
\binom{A+t}{b+t}-\binom Ab
=\sum_{j=1}^{t}\binom{A+j-1}{b+j}
\]
is a canonical diagonal run above the canonical \(b\)-cascade of \(x\).
The strict inequality \(x<\binom Ab\) prevents a carry into the final
term, so termwise shadowing proves (16.1).

For clarity, write the transfer as an induction. Let \(x_b\) denote the
upper-core recurrence, so \(x_b=a_b\) for \(3\le b\le r+2\), and use
\(x_{r+3}=0\) at the empty level above the core. Repeated application of
(16.1), starting at the top of the full profile, gives
\[
M_{b+r}=\binom B{b+r}-\binom Ab+x_b
\qquad(3\le b\le r+3).
\tag{16.2a}
\]
Each applied step has \(b<A\) and uses (16.0); the last identity
application is the \(b=4\) step, so no assumption that \(a_3\) fits on
\(A\) is needed. At \(b=3\),
\[
M_{r+3}=\binom B{r+3}-\binom A3+a_3
=\binom B{r+3}+e_r
\ge\binom B{r+3}+1.
\tag{16.2}
\]

Define a residual sequence by
\[
u_{r+3}=1,\qquad
u_{k-1}=r+\partial_{k-1}(u_k)
\quad(k=r+3,r+2,\ldots,4).
\tag{16.3}
\]

Let \(\ell_i\) be the L4 recurrence:
\[
\ell_{r+1}=r,\qquad
\ell_i=r+\partial_{i+1}(\ell_{i+1}).
\]
Since
\[
u_{r+2}=r+\partial_{r+2}(1)=2r+2\ge\ell_{r+1},
\]
monotonicity gives
\[
u_3\ge\ell_2>\binom A2.
\tag{16.4}
\]

Starting from (16.2), peel the shell \(\binom Bk\) downward. The
no-carry branch is \(u_k<\binom B{k-1}\), exactly the condition that the
shell followed by the residual is canonical. If instead, at some level
including \(k=3\),
\[
u_k\ge\binom B{k-1},
\]
then
\[
M_k\ge\binom Bk+\binom B{k-1}=\binom{B+1}{k}.
\]
A strict inequality is immediate failure; equality is followed by a
positive prescribed load and therefore fails one level later. For
\(k=3\), this means failure at level \(3\) or \(2\).

Otherwise, in particular \(u_3<\binom B2\), the shell peels exactly, and
\[
M_3\ge\binom B3+u_3.
\]
Using (16.4),
\[
\partial_2(u_3)\ge A+1.
\]
Therefore
\[
\begin{aligned}
M_2
&\ge
r+\binom B2+(A+1)\\
&=
\binom{B+1}{2}+1.
\end{aligned}
\]
Thus the full profile at \(n=2r+5\) is impossible.

---

## 17. Conclusion

We first record the missing-level reduction. For \(r\ge11\), levels
\(0\) and \(n\) cannot occur in an \(r\)-multiplicity antichain. If
level \(1\) occurs, choose \(r\) singleton members. Every other member
avoids those \(r\) points, so only the sizes
\[
1,2,\ldots,n-r
\]
can occur, giving at most \(n-r<n-3\) occupied levels. Complementation
excludes level \(n-1\) from any family with \(n-3\) occupied levels.
Hence an \(n-3\)-level witness must occupy exactly
\[
2,3,\ldots,n-2.
\]
Trimming every occupied level to exactly \(r\) members shows that the
threshold question is equivalent to the full prescribed profile.

For every \(r\ge11\), Section 16 proves failure at \(n=2r+5\), while
Sections 14--15 construct the full profile for every \(n\ge2r+6\).
Consequently
\[
\boxed{n_0(r)=2r+5\qquad(r\ge11).}
\]

Together with He--Tang's exact values for `r=2,3` and the finite theorem in
`SMALL_R_NOTE.md`, this gives the complete threshold classification
\[
 n_0(r)=
 \begin{cases}
  3,&r=2,\\
  8,&r=3,\\
  2r+4,&4\le r\le10,\\
  2r+5,&r\ge11.
 \end{cases}
\]
The least constant in He--Tang's bounded-error question
`n_0(r)<=2r+C` for all `r>=4` is therefore `C=5`.

---

# 18. Audit and publication status

Four adversarial AI audits dated 2026-07-16 attempted to
falsify the lower-window construction, the L4 reverse envelope, the
profile-theorem foundations, and the final assembly. None found a
mathematical error in a load-bearing argument. The first two audits drove
the release-critical repairs already incorporated above. Audit C found only
twelve minor or typographical issues; the present revision incorporates all
of them, including the two false but non-load-bearing sentences in the
technical note and L4 note. 

The repository includes the companion L4 proof, finite verifiers, exact r=11 witnesses, the small-r witnesses and cores, and the complete source for this document.

The result remains AI-assisted and has not undergone traditional
peer review; independent human line-by-line scrutiny is strongly encouraged,
especially for Sections 5--8, Section 16, and the companion L4 proof.

---

# 19. References

1. P. Erdős, *Problem sessions*, in I. Rival (ed.), *Ordered Sets*
   (Proc. NATO Advanced Study Institute), Reidel, Dordrecht, 1981,
   pp. 860–861.
2. Y. He and Q. Tang, *An Erdős--Trotter problem on antichains with
   multiplicity \(r\) on each occurring level*, arXiv:2602.09803 (2026),
   <https://arxiv.org/abs/2602.09803>.
3. G. F. Clements, *A Minimization Problem Concerning Subsets of a Finite
   Set*, Discrete Mathematics **4** (1973), 123–128.
4. D. E. Daykin, J. Godfrey, and A. J. W. Hilton, *Existence Theorems for
   Sperner Families*, Journal of Combinatorial Theory, Series A **17**
   (1974), 245–251.
5. P. Lieby, *Antichains on Three Levels*, Electronic Journal of
   Combinatorics **11** (2004), R50.
