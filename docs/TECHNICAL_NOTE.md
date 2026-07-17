# An exact calculation at $r=11$ in the Erdős–Trotter antichain problem

*Revised note, 17 July 2026. The result below is included in the end-to-end
Lean theorem for every `r>=4`; independent specialist peer review remains
pending.*

## 1. Definitions and result

For a family $\mathcal F\subseteq 2^{[n]}$, let

$$
S(\mathcal F)=\{|A|:A\in\mathcal F\}.
$$

An **$r$-multiplicity antichain** is an antichain for which every occurring
level contains at least $r$ members. Let $g(n,r)$ be the maximum possible
value of $|S(\mathcal F)|$. Following He and Tang, let $n_0(r)$ be the
least threshold such that $g(n,r)=n-3$ for every $n>n_0(r)$.

The result proved here is:

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
occupy exactly $2,3,\ldots,25$, with at least 11 members on each level.
The lower-bound necessity theorem therefore obstructs such a witness
directly, while recurrence feasibility constructs one with exactly 11
members on each level. Consequently,

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

The form used in this package is deliberately asymmetric.

**Necessity from lower bounds.** If an antichain has at least $f_i$ members
on every level $i$, then

$$
m_i\le\binom ni
$$

for every $i$.

**Sufficiency with equality.** Conversely, if all these capacities fit, the
colex construction produces an antichain with exactly $f_i$ members on every
level $i$.

In particular, for an exact proposed profile this gives the usual if-and-only-if
criterion.  The asymmetric statement avoids any trimming step in obstruction
arguments.

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

At the highest requested level, whether or not there are family members above
it, $M_s$ contains the level-$s$ slice of the antichain, so
$|M_s|\ge f_s=m_s$. Starting from this base and using monotonicity of the
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
$2,\ldots,24$. The generated family has 253 sets and passes a separately
implemented pairwise-containment checker. Hence

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
separate companion manuscript in [`UNIFORM_THEOREM.md`](UNIFORM_THEOREM.md)
gives an AI-assisted proof, now formalized in Lean, for

$$
n_0(r)=2r+5\qquad(r\ge11).
$$

The exact calculation and stored certificates in this note do not depend on
the uniform argument. Conversely, the uniform manuscript uses the same
classical profile criterion and the core/padding framework developed here.
The uniform argument has passed four adversarial AI audits but has not yet
undergone independent specialist peer review; the repository records that
distinction explicitly.

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
