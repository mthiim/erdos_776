# A uniform threshold for the Erdős–Trotter antichain problem

**Status:** end-to-end Lean formalized for $r\ge4$ after four separate
adversarial AI review passes; pending independent specialist peer review
**Date:** 2026-07-17

Throughout this note, $n_0(r)$ denotes the least integer $N$ such that a
target family exists for every $n>N$. Thus the strict inequality is part of
the convention: the displayed value is the last failing ground-set size.

**Main result of this note:**
$$
\boxed{n_0(r)=2r+5\qquad(r\ge11).}
$$

The conceptual interface is the upper-core carry. Put $A=r+4$, let $a_b$ be
the constant upper-core recurrence, and prove

$$
a_b\le\binom Ab\quad(4\le b\le r+2),\qquad
a_3=\binom A3+e,\qquad 1\le e\le6.
\tag{0.1}
$$

Lower-window feasibility gives the capacities and $e\le6$; L4 gives $e\ge1$.
Positive carry gives the obstruction, bounded carry gives the feasible core,
puncturing gives free sets, and padding gives every later ground-set size.

For later interpretation, define $\alpha_r$ to be the largest integer $y$
for which the profile
$$
f_i=r\quad(2\le i\le r),
\qquad
f_{r+1}=y
$$
is feasible on an $A=r+4$ point ground set. Equivalently, $\alpha_r$ is the
largest $y$ for which the recurrence
$$
m_{r+1}=y,
\qquad
m_i=r+\partial_{i+1}(m_{i+1})
\quad(i=r,\ldots,2)
$$
satisfies
$$
m_i\le\binom Ai
\qquad(2\le i\le r+1).
$$
The equivalence follows from the prescribed-profile criterion. Part I proves
$\alpha_r\ge r-6$, and the carry identity implies $\alpha_r=r-e$, but
$\alpha_r$ is not needed as an object in the main logical dependency.

The point of this proof is that the old top-zone cutoff $r\le 28\,710$
disappears. The replacement is:

1. follow the exact anchor ladder as far as it naturally goes;
2. complete one additional anchor;
3. build a short sequence of compressed phases;
4. use a one-digit rising tail to enter an exact generalized envelope;
5. let a small scalar recurrence perform the entire bottom collapse.

The human proof uses two finite exact checks: the lower-window base
$11\le r\le377$, consisting of 367 integer cascade computations, and
the L4 base $11\le r\le28$, consisting of 18 exact profile checks.
The lower window is symbolic for $r\ge378$, while L4 is symbolic for
$r\ge29$. Additional witness checks and adversarial computations archived
with this repository are supplementary falsification tests. In Lean, the range
$11\le r\le28$ is discharged by a direct bounded upper-core/overflow
certificate, $29\le r\le377$ by a bounded lower-window certificate, and
$r\ge378$ symbolically. The resulting least-threshold theorem is formalized
for every $r\ge4$.

---

## 1. Kruskal--Katona notation

For $m\ge0$ and $k\ge1$, write the $k$-cascade of $m$ as
$$
m=\binom{a_k}{k}+\binom{a_{k-1}}{k-1}+\cdots+\binom{a_s}{s},
\qquad
a_k>a_{k-1}>\cdots>a_s\ge s.
$$
Set
$$
\partial_k(m)
=
\binom{a_k}{k-1}
+\binom{a_{k-1}}{k-2}
+\cdots+
\binom{a_s}{s-1},
\qquad
\partial_k(0)=0.
$$

For lower bounds $f$, define
$$
m_s=f_s,\qquad
m_i=f_i+\partial_{i+1}(m_{i+1}),
$$
The profile theorem is used asymmetrically:

- any antichain with at least $f_i$ members at level $i$ forces
$$
m_i\le\binom ni
$$
at every level;
- if all capacities fit, the colex construction produces an antichain with
  exactly $f_i$ members at every requested level.

Thus obstruction never requires trimming, while construction obtains the
exact profile.

A self-contained necessity-and-sufficiency proof, together with the
canonical colex construction, is given in
[`TECHNICAL_NOTE.md`, Section 2](TECHNICAL_NOTE.md#2-exact-profile-criterion).

We repeatedly use two elementary facts.

### Monotonicity

If $x\le y$, then
$$
\partial_k(x)\le\partial_k(y).
$$

### Completion of a constant-offset run

A finite cascade run
$$
\binom d p+\binom{d-1}{p-1}+\cdots+\binom{d-\ell}{p-\ell}
$$
is bounded above by the corresponding completed binomial
$$
\binom{d+1}{p}.
$$
This is just Pascal/hockey-stick expansion. Consequently, after a run is
shadowed, it may be rounded up to its completed stone in a supersolution.

A **supersolution** for the recurrence is a sequence $V_i$ satisfying
$$
V_{i-1}\ge r+\partial_i(V_i).
$$
If the exact recurrence is below $V_i$ at one level, monotonicity keeps it
below the supersolution at every lower level.

### Notation roadmap

The proof has two long recurrences and one phased supersolution. The following
table fixes the recurring symbols and, in particular, separates phase
positions from the residual used in the final obstruction.

| Symbol | Meaning |
|---|---|
| $A=r+4$ | ground-set size for the lower window and reflected upper core |
| $B=2r+4$ | diagonal-shell parameter for the obstruction on $B+1=2r+5$ points |
| $m_i$ | exact lower-window recurrence state in (2.1) |
| $T_q$ | anchor threshold defined recursively in (3.1) |
| $B_q=T_q-2q$ | bottom digit of the unary block at anchor $q$ |
| $t$ | maximal anchor index with $T_t\le r<T_{t+1}$ |
| $N,c,h$ | phase parameters $N=r-2t$, $c=2t+3$, and $h=t+2$ |
| $K$ | final phase index selected by (5.1) |
| $s_j$ | tower stone $r+1-c2^{j-1}$ |
| $b_j,u_j,\ell_j$ | birth level, active top position, and extension count for phase $j$ |
| $a_i$ | reflected upper-core recurrence in Sections 14--16 |
| $M_i$ | full-profile recurrence on $2r+5$ points in Section 16 |
| $v_i$ | residual recurrence after the diagonal shell is removed |
| $c_i$ | L4 recurrence used to lower-bound $v_i$ |

---

# Part I. The uniform lower window

## 2. The lower-window recurrence

Put
$$
A=r+4.
$$
To prove $\alpha_r\ge r-6$, it is enough to show that the recurrence
$$
m_{r+1}=r-6,\qquad
m_i=r+\partial_{i+1}(m_{i+1})
\quad(i=r,r-1,\ldots,2)
\tag{2.1}
$$
satisfies
$$
m_i\le\binom Ai
\qquad(2\le i\le r+1).
\tag{2.2}
$$

The range $11\le r\le377$ is checked exactly in Section 12. Hence assume
throughout Sections 3--11 that
$$
r\ge378.
$$

### Conceptual segment table

The detailed proof below is one supersolution assembled from the following
segments. The full theorem/module cross-reference is in
[`PROOF_GUIDE.md`](PROOF_GUIDE.md).

| Segment, levels, and state | Transition, capacity, and Lean modules |
|---|---|
| Exact anchors: $r+1$ to $r-t$; (3.2) | Lemma 3.1 and the exact top-segment bound. Lean: Anchors. |
| Completed anchor: $r-t-1$; (4.1)--(4.2) | Rounded-anchor and phase-one entry; completed-anchor bound. Lean: Anchors, Phase Start. |
| Ordinary phases: phase-birth intervals; (6.0) | Extension and harvest lemmas; Lemma 5.1 and (6.2), (6.4). Lean: Phase Canonical, Transitions, Harvest, Capacity. |
| Rising tail: final harvest to level $L$; (7.2)--(7.3) | Steps (7.4)--(7.5) and rising-state capacity. Lean: Rising Tail. |
| Generalized envelope: $t+K+4$ to $t+5$; (8.1) | Exact step (8.2) and envelope capacity. Lean: Generalized Envelope. |
| Scalar collision: $t+5$ to $t+4$; $E_i$ to $F_t(0)$ | Collision identity in Section 9 and endpoint capacity. Lean: Scalar States, Full Envelope. |
| Scalar collapse: $t+4$ to $4$; (9.1) | Lemmas 10.1--10.2 and scalar-state capacity. Lean: Scalar Collapse, Scalar States. |
| Final levels: $4,3,2$; final scalar states | Equations (11.1)--(11.3), including tight bottom capacity. Lean: Final Levels, Phase Assembly. |

---

## 3. Exact anchor ladder

Define
$$
T_0=28,\qquad
T_{q+1}=\binom{T_q-2q}{2},
\tag{3.1}
$$
and put
$$
B_q=T_q-2q.
$$
Thus
$$
T_1=378,\qquad
T_2=70\,500,\qquad
T_3=2\,484\,807\,760,
$$
and so on.

For integers $a\le b$, write
$$
U(a,b)=\sum_{x=a}^{b}\binom xx,
$$
with $U(a,b)=0$ if $a>b$.

### Lemma 3.1: exact anchors

If $r\ge T_q$, then the exact recurrence (2.1) satisfies
$$
\boxed{
m_{r-q}
=
\sum_{j=0}^{q}
\binom{r+2-2j}{r-q-j}
+
U(B_q,r-2q-1).
}
\tag{3.2}
$$

#### Proof

For $q=0$, the $r-6$ top sets are unary at level $r+1$, so
$$
m_r
=
\binom{r+2}{r}
+
U(28,r-1).
$$

Assume (3.2). Let
$$
N=r-2q.
$$
After taking one shadow, the unary part contributes
$$
\sum_{x=B_q}^{N-1}x
=
\binom N2-\binom{B_q}{2}.
$$
Adding the new flow $r$ gives
$$
\binom N2+\bigl(r-T_{q+1}\bigr).
$$
The first term is the new anchor
$$
\binom N{N-2},
$$
and, when $r\ge T_{q+1}$, the residual $r-T_{q+1}$ is the unary block
$$
U(T_{q+1}-2q-2,r-2q-3)
=
U(B_{q+1},r-2(q+1)-1).
$$
This proves the induction. ∎

### Capacity on the exact top segment

The exact states just constructed already satisfy the required capacity
bounds. At the top level,
$$
m_{r+1}=r-6<\binom{r+4}{r+1}.
$$
At level $i=r-q$ in Lemma 3.1, the canonical cascade has leading digit
$r+2$ at position $i$, and every remaining digit is strictly smaller.
The remaining positions form a canonical cascade of index at most $i-1$
whose digits are at most $r+1$, so its value is strictly less than
$\binom{r+2}{i-1}$. Consequently
$$
m_i<\binom{r+2}{i}+\binom{r+2}{i-1}
=\binom{r+3}{i}
<\binom{r+4}{i}.
$$
Thus every level from $r+1$ down through the last exact anchor level
fits on the $A=r+4$-point ground set.

Choose $t\ge1$ maximal such that
$$
T_t\le r<T_{t+1}.
\tag{3.3}
$$
Set
$$
N=r-2t,\qquad
c=2t+3,\qquad
h=t+2.
\tag{3.4}
$$

A useful elementary bound is
$$
T_t\ge128t+250
\qquad(t\ge1).
\tag{3.5}
$$
It is equality at $t=1$, and the induction step follows immediately from
(3.1). In particular,
$$
r\ge64c.
\tag{3.6}
$$

---

## 4. Complete one additional anchor

At level
$$
I=r-t,
$$
Lemma 3.1 gives the exact state. Descending one more level, the residual
below the old anchors is
$$
\binom N2-\bigl(T_{t+1}-r\bigr).
$$
Since $r<T_{t+1}$, this is at most $\binom N2$. It is also
nonnegative: since $r\ge T_t$,
$$
N=r-2t\ge T_t-2t=B_t,
$$
and therefore
$$
\binom N2-\bigl(T_{t+1}-r\bigr)
=\binom N2-\binom{B_t}{2}+r\ge0.
$$
We therefore round it up and define
$$
V_{I-1}
=
\sum_{j=0}^{t+1}
\binom{r+2-2j}{I-1-j}.
\tag{4.1}
$$
This is a valid supersolution step.

The new final anchor is $N$, and after one shadow it sits at position
$N-3$. At the next level
$$
b_1=I-2=r-t-2
$$
place beneath it the two-term run
$$
\binom{N-3}{N-4}
+
\binom{N-4}{N-5}.
\tag{4.2}
$$
Its value is
$$
2N-7\ge r
\tag{4.3}
$$
by (3.5). Thus (4.2) pays the next flow.

Define the tower stones
$$
\boxed{
s_j=r+1-c\,2^{j-1}
\qquad(j\ge1).
}
\tag{4.4}
$$
Then
$$
s_1=N-2,
$$
and the run in (4.2) has top digit $s_1-1$. Moreover
$$
s_{j+1}=2s_j-r-1.
\tag{4.5}
$$

---

## 5. Choice of the final phase

Let $K$ be the unique integer satisfying
$$
c\,2^{K-1}\le\frac r4<c\,2^K.
\tag{5.1}
$$
Because of (3.6), $K\ge5$.

For $1\le j\le K$,
$$
s_j\ge\frac{3r}{4}+1,
\tag{5.2}
$$
and
$$
s_{K+1}\ge\frac r2+1.
\tag{5.3}
$$

The first phase begins with top position
$$
u_1=N-4.
\tag{5.4}
$$
It already has two terms, as in (4.2).

For the first phase, set
$$
\ell_1=\left\lfloor\frac{u_1-5}{2}\right\rfloor.
\tag{5.5}
$$
After $\ell_1$ extensions, the run bottom is $4$ or $5$. Harvest the
run to $s_1$ and birth phase $2$.

For every later ordinary phase $j\ge2$, if its top position is $u_j$,
set
$$
\ell_j=\left\lfloor\frac{u_j-4}{2}\right\rfloor,
\qquad
u_{j+1}=u_j-\ell_j-2
=\left\lceil\frac{u_j}{2}\right\rceil.
\tag{5.6}
$$
The first transition differs by at most one:
$$
u_2\le\left\lceil\frac{u_1}{2}\right\rceil+1.
$$

Let $b_j$ be the birth level of phase $j$. Then
$$
b_1=I-2,
\qquad
b_{j+1}=b_j-\ell_j-1,
\tag{5.6a}
$$
and
$$
\boxed{b_j-u_j=h+j-1=t+j+1.}
\tag{5.6b}
$$
The identity holds at $j=1$, because
$(I-2)-(N-4)=t+2=h$. A harvest decreases the level by
$\ell_j+1$ and the next active top position by $\ell_j+2$, so the
slot increases by exactly one. In particular, the phases cover every
intervening level without gaps.

Consequently
$$
\frac{u_1}{2^{j-1}}
\le u_j
\le
\frac{u_1}{2^{j-1}}+2.
\tag{5.7}
$$
For completeness, the lower bound follows because every transition is at
least halving. For the upper bound, the exceptional first transition gives
$u_2\le u_1/2+3/2\le u_1/2+2$. If the upper bound holds at some
$j\ge2$, then
$$
u_{j+1}=\left\lceil\frac{u_j}{2}\right\rceil
\le \frac{u_1}{2^j}+\frac32
\le \frac{u_1}{2^j}+2,
$$
which proves the two-case induction.
Using (5.1), (5.7), and $u_1>3r/4$, we get
$$
\boxed{
3c\le u_K\le8c+2.
}
\tag{5.8}
$$


### Lemma 5.1: quantitative phase bounds

The estimates used in Sections 6--8 follow uniformly from the preceding
parameters:

1. $3c\le u_K\le8c+2$.
2. Every phase-1 extension term in (6.1) has lower index at least $4$,
   complementary index at least $2$, and upper digit at least
   $(N-1)/2$.
3. Every later ordinary extension term in (6.3) has lower index at least
   $4$, complementary index at least $2$, and upper digit at least
   $r/2-3$.
4. Every newborn term at an ordinary harvest has upper digit at least
   $3r/4$, lower index at least $2$, and complementary index at least
   $2$; hence it has value greater than $r$.
5. In the final rising-tail zone, $d_p\ge3r/8$ whenever $p\ge4$.
6. The terminal envelope level satisfies $L<r/4$.

*Proof.* From $u_1=r-c-1$, (5.1), and (5.7),
$$
u_K\ge \frac{r-c-1}{2^{K-1}}
\ge 4c-\frac{4c(c+1)}r>3c,
$$
where the last inequality uses $r\ge64c$. The other half of (5.1)
gives $2^{-(K-1)}<8c/r$, hence
$$
u_K\le\frac{u_1}{2^{K-1}}+2<8c+2.
$$

For phase 1, the extension in (6.1) has index
$u_1-3-2\ell$, which is at least $4$ because
$\ell<\ell_1$. Its complementary index is
$$
(s_1-3-\ell)-(u_1-3-2\ell)=2+\ell,
$$
and the endpoint choice of $\ell_1$ gives upper digit at least
$(N-1)/2$.

For a later phase, the index in (6.3) is at least $4$. Its complementary
index equals
$$
s_j-u_j+\ell.
$$
For $2\le j\le K-1$, we have $c2^{j-1}\le r/8$ and
$u_j\le r/2+2$, so
$$
s_j-u_j\ge r+1-\frac r8-\left(\frac r2+2\right)>2.
$$
Also $\ell\le u_j/2$, and therefore
$$
s_j-2-\ell\ge \frac{3r}{4}-1-\frac{r/2+2}{2}
\ge \frac r2-3.
$$
At harvest, the next stone has digit at least $3r/4+1$, so the newborn
active digit is at least $3r/4$. Its position is at most $r/2+2$,
and the preceding bounds leave both index and complementary index at least
$2$; its value is therefore at least $\binom{3r/4}{2}>r$.

In the final zone, $D\ge r/2+3$ and $p\le u-1\le r/8+1$, so
$$
d_p=D-p+1\ge\frac{3r}{8}+3>\frac{3r}{8}.
$$
Finally, (3.5) gives $t<r/128$, while (5.1) gives
$K\le\log_2 r$. Thus
$$
L=t+K+4<\frac r{128}+\log_2r+4<\frac r4
\qquad(r\ge378).
$$
∎

---

## 6. Ordinary phase transitions

The full active-run invariant is as follows. At level $b_1-L$, after
$L$ completed phase-1 extensions, the active run is
$$
R_{1,L}=\sum_{p=0}^{L+1}
\binom{s_1-1-p}{u_1-L-p},
\qquad 0\le L\le\ell_1.
\tag{6.0a}
$$
For every later phase $j\ge2$, at level $b_j-L$, after $L$
completed extensions, the active run is
$$
R_{j,L}=\sum_{p=0}^{L}
\binom{s_j-1-p}{u_j-L-p},
\qquad 0\le L\le\ell_j.
\tag{6.0b}
$$
The completed anchors and stones simply shadow one position at a time.
The digits and positions in each run both decrease by one as $p$
increases, so the displayed runs are canonical. After one further shadow,
the hockey-stick completion dominates the old run, and the newborn term
sits at $u_j-\ell_j-2=u_{j+1}$. These formulas fix the meanings of
“extension”, “harvest”, and “birth” below.

### Worked schematic: one ordinary extension

Fix a phase $j\ge2$ and suppose $0\le L<\ell_j$. At level $b_j-L$ its
active run is
$$
R_{j,L}=\sum_{p=0}^{L}
\binom{s_j-1-p}{u_j-L-p}.
$$
Termwise shadowing lowers every position by one:
$$
\partial_{b_j-L}(R_{j,L})=
\sum_{p=0}^{L}
\binom{s_j-1-p}{u_j-L-p-1}.
$$
The next prescribed load is paid by appending the new final digit
$$
Q_{j,L}=
\binom{s_j-L-2}{u_j-2L-2}.
$$
The bounds in Lemma 5.1 ensure that this digit is valid, lies below the
preceding digit, and satisfies $Q_{j,L}\ge r$. Consequently
$$
r+\partial_{b_j-L}(R_{j,L})
\le
\partial_{b_j-L}(R_{j,L})+Q_{j,L}
=R_{j,L+1}.
$$
All completed anchors and earlier stones shadow unchanged alongside this
calculation. This is the exact transition formalized by
`phase_extension_pays` and `isCanonical_phase_extension`. At
$L=\ell_j$, the same run is completed by the hockey-stick identity; the
harvest transition places the next active digit at
$u_j-\ell_j-2=u_{j+1}$ and begins phase $j+1$. Thus one extension and one
harvest account for every seam used in the ordinary-phase segment.

### Phase 1

At birth level $b_1=I-2$, phase $1$ consists of
$$
s_1-1,\ s_1-2
$$
at positions
$$
u_1,\ u_1-1.
$$
For $0\le\ell<\ell_1$, shadow to level
$b_1-1-\ell=I-3-\ell$ and append
$$
\binom{s_1-3-\ell}{u_1-3-2\ell}.
\tag{6.1}
$$
Whenever this extension is used, its lower index is at least $4$, its
complement is at least $2$, and its upper digit is at least
$$
\frac{N-1}{2}.
$$
From (3.5), $t\le(r-250)/128$, so
$$
N=r-2t\ge \frac{63r}{64}+\frac{125}{32}>\frac r2.
$$
Thus the upper digit is larger than $r/4-1$; for $r\ge378$, even the
smaller endpoint binomial $\binom{\lfloor r/4\rfloor-1}{2}$ exceeds
$r$. For a fixed upper digit, a binomial coefficient whose index and
complementary index are both at least $2$ is at least its endpoint value
$\binom d2$. Since the actual lower index is at least $4$ and the
complementary index is at least $2$, we obtain
$$
\binom{s_1-3-\ell}{u_1-3-2\ell}\ge r.
\tag{6.2}
$$

### Phases $2,\ldots,K-1$

At birth level $b_j$, phase $j$ begins with
$$
\binom{s_j-1}{u_j}.
$$
For $0\le\ell<\ell_j$, shadow to level $b_j-1-\ell$ and append
$$
\binom{s_j-2-\ell}{u_j-2\ell-2}.
\tag{6.3}
$$
For $j\le K-1$, (5.2), (5.7), and (5.8) imply that throughout every
extension:

- the lower index is at least $4$;
- the complementary index is at least $2$;
- the upper digit is at least $r/2-3$.

Hence
$$
\binom{s_j-2-\ell}{u_j-2\ell-2}
\ge
\binom{r/2-3}{2}
>r.
\tag{6.4}
$$

At a harvest step, completion of the old run costs nothing: the completed
stone dominates its shadow. The newly born active term for the next phase
has upper digit at least $3r/4$, while its position lies between $2$
and $r/2+2$. Therefore that newborn term alone has value greater than
$r$.

Thus every ordinary in-phase and harvest transition is a valid
supersolution step.

---

## 7. A one-digit final zone

At the harvest of phase $K-1$, namely at level $b_K$, do not birth
an ordinary phase $K$. Instead, place the completed stone $s_K$ at
position $u_K$, and place the new tail immediately below it at position
$u_K-1$. Completion of the
old phase-$(K-1)$ run dominates its shadow, while
$$
\binom{s_K}{u_K}
\ge \binom{3r/4}{2}>r.
$$
Thus the new $s_K$-term alone pays the incoming flow; the tail introduced
below it is additional slack.

Put
$$
u=u_K,\qquad
D=s_{K+1}+2.
\tag{7.1}
$$
At the position immediately below $s_K$, namely $u-1$, place the digit
$$
d_{u-1}=D-u+2.
\tag{7.2}
$$

As the construction descends, let this one tail digit move from position
$p$ to $p-1$, while changing according to
$$
d_p=
\begin{cases}
D,&p=2,\\
D-p+1,&p\ge3.
\end{cases}
\tag{7.3}
$$

Thus the digit rises by $1$ at every step except the final transition
$3\to2$, where it rises by $2$.

### Canonical validity

From (5.1),
$$
s_K-D=c2^{K-1}-2>0.
$$
Also, by (5.3), (5.8), and (3.6),
$$
D\ge \frac r2+3,
\qquad
u\le\frac r8+2.
$$
Hence
$$
D-u+2\ge u-1,
$$
so the initial tail term is valid, and it remains strictly below $s_K$.

### Gain at each step

For $p\ge4$, the gain from raising by one is
$$
\binom{d_p+1}{p-1}-\binom{d_p}{p-1}
=
\binom{d_p}{p-2}.
\tag{7.4}
$$
Here
$$
d_p\ge\frac{3r}{8},
\qquad
2\le p-2\le d_p-2,
$$
so (7.4) is greater than $r$.

For the last step,
$$
\binom D2-\binom{D-2}{2}
=
2D-3
\ge r.
\tag{7.5}
$$

Therefore the rising tail pays every remaining flow.

After $u-3$ steps, $s_K$ has reached position $3$, and the tail has
reached position $2$ with digit $D=s_{K+1}+2$. The level reached is
$$
b_K-(u_K-3)=(b_K-u_K)+3=h+K+2.
\tag{7.5a}
$$
More generally, once $s_q$ is completed, its permanent slot is
$$
\text{level}-\text{position}=h+q-1.
\tag{7.5b}
$$
This is the simultaneous alignment invariant at the Section 7/8 seam.

Let
$$
L=h+K+2.
\tag{7.6}
$$
The state at level $L$ is exactly the generalized envelope introduced
next.

---

## 8. Exact generalized envelope

For $h+3\le i\le L$, define
$$
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
$$

At level $L$, this is exactly the endpoint of Section 7. Indeed, by
(7.5b), stone $s_q$ occupies position
$L-(h+q-1)=L-h-q+1$, exactly its position in the second sum of (8.1);
$s_K$ is at position $3$, and the tail $s_{K+1}+2$ is at position
$2$.

The representation is canonical:

- the initial anchors fall by $2$;
- $r-2t=N>s_1=N-2$;
- successive tower stones satisfy $s_q>s_{q+1}$;
- the terminal digit $s_{i-h-1}+2$ is still below the preceding stone.

Moreover, all tower digits used here are at least $s_{K+1}\ge r/2+1$.
From (3.5), $t<r/128$; from (5.1), $K\le\log_2 r$. Hence
$$
L=t+K+4
<
\frac r{128}+\log_2 r+4
<
\frac r4
\qquad(r\ge378),
$$
so every digit is above its position.

### Exact envelope step

The fixed anchors and old stones simply shift under one shadow. At the
bottom, write
$$
m=i-h-1.
$$
The difference needed to pass from $E_i$ to $E_{i-1}$ is
$$
\binom{s_{m-1}+2}{2}
-
\binom{s_{m-1}}{2}
-
(s_m+2).
$$
Using (4.5), this equals
$$
2s_{m-1}-s_m-1=r.
$$
Hence
$$
\boxed{
E_{i-1}=r+\partial_i(E_i)
\qquad(h+4\le i\le L).
}
\tag{8.2}
$$

---

## 9. Collision of the extra anchors

At level
$$
i=h+3=t+5,
$$
the last anchor is $N$ at position $4$, the first tower stone is
$$
s_1=N-2
$$
at position $3$, and the terminal digit is $s_2+2$ at position $2$.

After one shadow and addition of $r$, the part below the shifted $N$
anchor is
$$
\binom{N-2}{2}+(s_2+2)+r.
$$
Since
$$
s_2+2=r-4t-3
$$
and
$$
\binom N2-\binom{N-2}{2}=2N-3=2r-4t-3,
$$
this part is exactly $\binom N2$. It merges with $\binom N3$ to give
$\binom{N+1}{3}$.

Thus, at level $t+4$, the state is
$$
F_t(0),
$$
where for $0\le q\le t$ and $z\ge0$ we define
$$
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
$$
with $z$ inserted in its $2$-cascade below the displayed position-$3$
term.

---

## 10. Scalar bottom collapse

Set
$$
z_t=0,
$$
and for $q=t,t-1,\ldots,1$, define
$$
\boxed{
z_{q-1}=2q-1+\partial_2(z_q).
}
\tag{10.1}
$$

The residuals really do append canonically below the position-$3$ digit.
For $q\ge6$, the proof of Lemma 10.2 gives $z_q\le q^2$, so the top
digit of the $2$-cascade of $z_q$ is at most $2q$. For the smaller
indices the same proof gives
$$
z_5\le20,\quad z_4\le16,\quad z_3\le14,\quad z_2\le11,\quad z_1\le9.
\tag{10.1a}
$$
Since $\binom72=21$, their top $2$-cascade digit is at most $6$.
On the other hand, by (3.5),
$$
r-2q+1\ge r-2t+1>2q.
$$
Thus no residual carry enters the displayed position-$3$ digit.

### Lemma 10.1

For every $q\ge1$,
$$
r+\partial_{q+4}\bigl(F_q(z_q)\bigr)
=
F_{q-1}(z_{q-1}).
\tag{10.2}
$$

#### Proof

At level $q+4$, the last ordinary anchor has digit
$$
a=r-2q+2
$$
at position $4$, and the special digit is $a-1$ at position $3$.
After shadowing, filling the position-$2$ term from
$\binom{a-1}{2}$ to $\binom a2$ costs
$$
a-1=r-2q+1.
$$
The incoming amount is
$$
r+\partial_2(z_q).
$$
The excess is therefore
$$
r+\partial_2(z_q)-(r-2q+1)
=
2q-1+\partial_2(z_q)
=
z_{q-1}.
$$
Finally,
$$
\binom a3+\binom a2=\binom{a+1}{3},
$$
which is precisely the new special digit in $F_{q-1}$. ∎

### Lemma 10.2: terminal residual

The recurrence (10.1) gives
$$
z_0=
\begin{cases}
1,&t=1,\\
4,&t=2,\\
6,&t\ge3.
\end{cases}
\tag{10.3}
$$

#### Proof

The cases $t=1,2$ are direct.

Assume $t\ge3$. We first show
$$
5\le z_2\le11.
\tag{10.4}
$$
The lower bound follows from the $q=3$ step.

For the upper bound, the first three cases are
$$
\begin{array}{c|c}
t & (z_t,z_{t-1},\ldots,z_0)\\
\hline
3&(0,5,7,6)\\
4&(0,7,10,8,6)\\
5&(0,9,12,11,9,6).
\end{array}
$$
If $t\ge6$, use the invariant
$$
z_q\le q^2\qquad(q\ge6).
$$
Indeed, if $q\ge7$ and $z_q\le q^2$, let $a_2$ be the top digit
of the canonical $2$-cascade of $z_q$. If $a_2\ge2q$, then
$z_q\ge\binom{2q}{2}>q^2$, a contradiction. Hence
$a_2\le2q-1$. A possible position-$1$ term contributes only one more
to the shadow, so
$$
\partial_2(z_q)\le a_2+1\le2q.
$$
Therefore
$$
z_{q-1}\le4q-1\le(q-1)^2.
$$
Starting from $z_t=0$, this yields $z_6\le36$. Hence
$$
z_5\le11+9=20,\qquad
z_4\le9+7=16,\qquad
z_3\le7+7=14,
$$
and then
$$
z_2\le5+6=11.
$$

For $5\le z_2\le11$,
$$
4\le\partial_2(z_2)\le6,
$$
so
$$
7\le z_1\le9.
$$
Every integer from $7$ through $9$ has $2$-shadow $5$. Thus
$$
z_0=1+5=6.
$$
∎

---

## 11. The final two levels

At level $4$, the state is
$$
F_0(z_0)
=
\binom{r+2}{4}
+
\binom{r+1}{3}
+
z_0.
$$

Descending to level $3$ gives
$$
E_3
=
\binom{r+3}{3}
+
\bigl(\partial_2(z_0)-1\bigr).
\tag{11.1}
$$
By Lemma 10.2,
$$
E_3=
\begin{cases}
\binom{r+3}{3}+1,&t=1,\\[2mm]
\binom{r+3}{3}+3,&t\ge2.
\end{cases}
\tag{11.2}
$$

Therefore
$$
E_2=r+\partial_3(E_3)
=
\begin{cases}
\binom{r+4}{2}-1,&t=1,\\[2mm]
\binom{r+4}{2},&t\ge2.
\end{cases}
\tag{11.3}
$$

All higher constructed states have canonical leading digit $r+2$, so
they are strictly below
$$
\binom{r+3}{i}<\binom{r+4}{i}.
$$
The level-$3$ values in (11.2) also lie well below
$\binom{r+4}{3}$, and (11.3) handles the tight bottom level.

By monotonicity, the exact recurrence (2.1) lies below this supersolution.
This proves
$$
\alpha_r\ge r-6
\qquad(r\ge378).
$$

---

## 12. Finite base $11\le r\le377$

For each $r$ in this range, evaluate (2.1) with exact integer
Kruskal--Katona cascades and check (2.2). A standalone implementation is
provided as `verify_lower_window_base.py`; it does not import the original
project code.

The full sweep has:

- 367 values of $r$;
- no failures;
- minimum capacity slack $3$, attained at level $2$ for every
  $20\le r\le377$; its first occurrence is at $r=20$.

Thus
$$
\boxed{\alpha_r\ge r-6\qquad(r\ge11).}
\tag{12.1}
$$

The standalone verifier `verification/verify_lower_window_base.py` is
archived with this release. It uses exact integer arithmetic; no SAT or
search is involved.

The numerical coverage boundary is worth making explicit. The finite base
ends at $r=377$, immediately below the first symbolic anchor threshold
$T_1=378$. The named seam checks at $r=378,379$ lie in the first anchor
regime $t=1$; the next regime begins only at
$$
T_2=70\,500.
$$
Thus the finite sweep and seam samples do not exercise the $t\ge2$ phase
structure. Coverage of the second anchor regime and every higher regime comes
from the symbolic proof formalized in Lean, not from numerical sampling.

Lean's ground-bounded evaluator certifies the subrange $29\le r\le377$ and is
proved equal to the original canonical shadow recurrence. For
$11\le r\le28$,
the final Lean theorem instead uses a smaller direct certificate of exactly
the upper-core capacities/carry and the full-profile overflow. The all-value
Python sweep remains an independently implemented exact cross-check of the
human lower-window proof.

---

# Part II. Assembly around the upper-core carry

The remainder uses the carry interface (0.1). Its dependency is:

1. lower-window feasibility gives upper capacities and $e\le6$;
2. L4 gives $e\ge1$;
3. $e\le6$ gives a feasible core on $r+5$ points;
4. puncturing top core members gives $r$ free sets;
5. padding gives every $n\ge2r+6$;
6. $e\ge1$ enters a no-carry diagonal shell and obstructs $n=2r+5$.

The identity involving $\alpha_r$ is retained below as an interpretation of
the same carry, not as a required intermediate object.

## 13. The L4 upper window

The companion reverse-envelope proof in
[`L4_PROOF.md`](L4_PROOF.md) establishes
$$
\boxed{\alpha_r\le r-1\qquad(r\ge11).}
\tag{13.1}
$$
It is symbolic for $r\ge29$, with exact finite verification for
$11\le r\le28$.

In particular, the profile
$$
r\text{ sets at every level }2,\ldots,r+1
$$
on $r+4$ points has bottom recurrence value strictly larger than
$\binom{r+4}{2}$.

L5 is immediate from L4: its two top singleton loads already induce a load
$r+3$ at level $r+1$, which exceeds the L4-admissible maximum.

---

## 14. Core carry and feasibility on $r+5$ points

Put
$$
A=r+4.
$$
Run the recurrence for the core profile
$$
r\text{ sets at every level }2,\ldots,r+2
$$
and denote its states by $a_i$.

Complement the feasible lower-window profile with top load $r-6$. Its
reflected recurrence agrees with the upper core at every level $i\ge4$, so it
supplies
$$
a_i\le\binom Ai\qquad(4\le i\le A-2).
\tag{14.0}
$$

At level $3$, reflected feasibility says
$$
(r-6)+\partial_4(a_4)\le\binom A3.
$$
Since
$$
a_3=r+\partial_4(a_4),
$$
we obtain
$$
a_3\le\binom A3+6.
$$

On the other hand, suppose
$$
a_3\le\binom A3.
$$
Together with (14.0), the recurrence states $a_i$ then satisfy all capacity
inequalities for the truncated constant profile
$$
f_i=r\qquad(3\le i\le r+2)
$$
on $A=r+4$ points. By profile sufficiency, there is an antichain with $r$
members on every one of those levels. Complementation maps the levels
$$
3,\ldots,r+2
$$
to
$$
2,\ldots,r+1,
$$
producing precisely the forbidden L4 profile. Therefore
$$
a_3>\binom A3.
$$
Define the positive carry by
$$
a_3=\binom A3+e_r.
\tag{14.1}
$$
The two preceding bounds give
$$
\boxed{1\le e_r\le6.}
\tag{14.2}
$$

For interpretation, repeat the reflected argument with an arbitrary top load
$y$. Level-three feasibility is equivalent to $y\le r-e_r$, and colex
sufficiency attains every such value. Consequently
$$
\alpha_r=r-e_r.
\tag{14.3}
$$
Thus the traditional lower and upper bounds on $\alpha_r$ encode precisely
the same carry bounds, but later sections use (14.0)--(14.2) directly.

This reflection and carry argument is formalized in
`Erdos776/Uniform/CoreCarry.lean`.  The certificate-facing theorem
`fullMiddleProfileThreshold_of_lowerWindowFits` takes only the capacity
inequalities (2.2); complementation, reflected recurrence identification,
the bounds on $e_r$, and all subsequent assembly are proved symbolically in
Lean.

The remaining capacities on $A+1$ points are explicit. At level $3$,
$$
a_3=\binom A3+e_r\le\binom A3+6<\binom{A+1}{3}.
$$
At level $2$, using (14.2),
$$
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
$$
For $i\ge4$, (14.0) gives
$a_i\le\binom Ai<\binom{A+1}{i}$; the level-3 and level-2 bounds were
just proved. Thus the complete core profile is feasible on
$$
A+1=r+5
$$
points.

---

## 15. Explicit free sets

Let
$$
q=r+5,\qquad X=[q-2],\qquad J=\{4,\ldots,q-2\}.
$$
In the canonical colex core, the first $r=q-5$ top-level sets are
$$
T_j=X\setminus\{j\},
\qquad j\in J.
$$
Indeed, the top state $r$ has a cascade of $r$ unit diagonal digits. Its
colex realization consists exactly of the $(r+2)$-subsets of
$X=[r+3]$ obtained by deleting one of the $r$ points in
$J=\{4,\ldots,r+3\}$.

We need only the following elementary observation.

**Puncturing lemma.** If $C$ is an antichain, $T$ belongs to $C$, and $D$ is
a proper subset of $T$, then $D$ contains no member of $C$.

Indeed, if $S$ belongs to $C$ and $S$ is contained in $D$, then $S$ is
contained in $T$. Antichainness forces $S=T$, while properness gives $T$ not
contained in $D$, a contradiction.

For
$$
4\le j\le q-2,
$$
define
$$
D_j=T_j\setminus\{1\}
   =[q]\setminus\{1,j,q-1,q\}.
\tag{15.1}
$$
There are exactly $r$ distinct such sets, each of size $q-4=r+1$.
Because $1$ belongs to every displayed $T_j$, each $D_j$ is a proper subset
of the core member $T_j$. The puncturing lemma immediately makes every
$D_j$ free. No classification of exceptional or later core members is
required.

The two-point padding lemma therefore applies indefinitely. At stage
$t$, retain the persistent free sets
$$
D_j^{(t)}=D_j\cup\{x_1,\ldots,x_t\},
$$
where $x_h$ is one selected point from the $h$-th added pair
$\{x_h,y_h\}$. An original core member is excluded by freeness of
$D_j$, and a member born at stage $h$ contains $y_h$, which is
absent from $D_j^{(t)}$. After $t$ stages the core parameters are
$$
(q,s)=(r+5+2t,r+2+t).
$$
The core-to-full lemma is proved in
[`TECHNICAL_NOTE.md`, Section 4](TECHNICAL_NOTE.md#4-construction-for-every-nge28).
Applied to the padded core, it gives a full-profile antichain for both
$$
n=2r+6+2t
\quad\text{and}\quad
n=2r+7+2t.
$$
Hence
$$
g(n,r)=n-3
\qquad(n\ge2r+6).
\tag{15.3}
$$

The assembly from one suitable free core through arbitrary padding and both
parities is formalized by
`Erdos776.Uniform.fullMiddleProfileExists_of_suitableFreeCore` in
`Erdos776/Uniform/Assembly.lean`.

The preceding explicit free-set argument is formalized in
`Erdos776/Uniform/FreeCore.lean`.  In particular,
`hasSuitableFreeCore_of_upperCoreData` constructs the canonical core and its
free family from the Section 14 upper-core data; no freeness certificate is
assumed by the final symbolic assembly.

---

## 16. Obstruction at $n=2r+5$

The symbolic argument in this section is formalized in Lean in
`Erdos776/Uniform/DiagonalObstruction.lean`.  Its certificate-facing endpoint
takes (14.0) and $1\le e_r\le6$ as explicit hypotheses; diagonal transfer,
L4 residual domination, shell peeling, overflow, and the final antichain
contradiction are then proved symbolically in Lean for $r\ge29$.

Put
$$
B=2r+4.
$$
Let $M_i$ be the full-profile recurrence for
$$
r\text{ sets at every level }2,\ldots,2r+3
$$
on $2r+5=B+1$ points.

The inequalities in (14.0) are in fact strict. Suppose first that
$5\le i\le A-2$ and
$$
a_i=\binom Ai.
$$
Then
$$
a_{i-1}
=r+\partial_i(a_i)
=r+\binom A{i-1}
>\binom A{i-1},
$$
contradicting the capacity inequality at level $i-1$.

If instead
$$
a_4=\binom A4,
$$
then
$$
a_3=r+\partial_4(a_4)
=r+\binom A3.
$$
Comparing this with
$$
a_3=\binom A3+e_r
$$
gives $e_r=r$, contradicting $e_r\le6<r$. Hence
$$
0\le a_i<\binom Ai\qquad(4\le i\le A-2).
\tag{16.0}
$$

### The no-carry diagonal-shell principle

The transfer is one no-carry principle rather than a collection of unrelated
calculations. If
$$
t\ge0,\qquad 1\le b<A,\qquad 0\le x<\binom Ab,
$$
then
$$
\boxed{
\partial_{b+t}\left(
\binom{A+t}{b+t}-\binom Ab+x
\right)
=
\binom{A+t}{b+t-1}-\binom A{b-1}+\partial_b(x).
}
\tag{16.1}
$$
Indeed,
$$
\binom{A+t}{b+t}-\binom Ab
=\sum_{j=1}^{t}\binom{A+j-1}{b+j}
$$
is a diagonal binomial shell above the canonical $b$-cascade of $x$.
The strict inequality $x<\binom Ab$ is exactly the condition that no carry
enters the shell, so termwise shadowing proves (16.1). If that condition ever
fails during peeling, the recurrence has already reached the next capacity
shell and overflow follows immediately or after the next positive load.

For clarity, write the transfer as an induction. Let $x_b$ denote the
upper-core recurrence, so $x_b=a_b$ for $3\le b\le r+2$, and use
$x_{r+3}=0$ at the empty level above the core. Repeated application of
(16.1), starting at the top of the full profile, gives
$$
M_{b+r}=\binom B{b+r}-\binom Ab+x_b
\qquad(3\le b\le r+3).
\tag{16.2a}
$$
Each applied step has $b<A$ and uses (16.0); the last identity
application is the $b=4$ step, so no assumption that $a_3$ fits on
$A$ is needed. At $b=3$,
$$
M_{r+3}=\binom B{r+3}-\binom A3+a_3
=\binom B{r+3}+e_r
\ge\binom B{r+3}+1.
\tag{16.2}
$$

Define a residual sequence by
$$
v_{r+3}=1,\qquad
v_{k-1}=r+\partial_{k-1}(v_k)
\quad(k=r+3,r+2,\ldots,4).
\tag{16.3}
$$

The shadow index is $k-1$ because, after separating the leading shell term
$\binom Bk$, the residual $v_k$ occupies cascade positions at most $k-1$.
Whenever
$$
v_k<\binom B{k-1},
$$
the decomposition
$$
\binom Bk+v_k
$$
is a canonical $k$-cascade, and therefore
$$
\partial_k\left(\binom Bk+v_k\right)
=
\binom B{k-1}+\partial_{k-1}(v_k).
\tag{16.3a}
$$
This is the exact shell-peeling identity used below: a diagonal shell plus a
subcritical residual shadows independently.

Let $c_i$ be the L4 recurrence:
$$
c_{r+1}=r,\qquad
c_i=r+\partial_{i+1}(c_{i+1}).
$$
Since
$$
v_{r+2}=r+\partial_{r+2}(1)=2r+2\ge c_{r+1},
$$
monotonicity gives
$$
v_3\ge c_2>\binom A2.
\tag{16.4}
$$

Starting from (16.2), peel the shell $\binom Bk$ downward. The
no-carry branch is $v_k<\binom B{k-1}$, exactly the condition that the
shell followed by the residual is canonical. If instead, at some level
including $k=3$,
$$
v_k\ge\binom B{k-1},
$$
then
$$
M_k\ge\binom Bk+\binom B{k-1}=\binom{B+1}{k}.
$$
A strict inequality is immediate failure; equality is followed by a
positive prescribed load and therefore fails one level later. For
$k=3$, this means failure at level $3$ or $2$.

Otherwise, in particular $v_3<\binom B2$, the shell-peeling identity
(16.3a) applies at every step, and
$$
M_3\ge\binom B3+v_3.
$$
Using (16.4),
$$
\partial_2(v_3)\ge A+1.
$$
Therefore
$$
\begin{aligned}
M_2
&\ge
r+\binom B2+(A+1)\\
&=
\binom{B+1}{2}+1.
\end{aligned}
$$
Thus the full profile at $n=2r+5$ is impossible.

---

## 17. Conclusion

We first record the missing-level reduction. For $r\ge11$, levels
$0$ and $n$ cannot occur in an $r$-multiplicity antichain. If
level $1$ occurs, choose $r$ singleton members. Every other member
avoids those $r$ points, so only the sizes
$$
1,2,\ldots,n-r
$$
can occur, giving at most $n-r<n-3$ occupied levels. Complementation
excludes level $n-1$ from any family with $n-3$ occupied levels.
Hence an $n-3$-level witness must occupy exactly
$$
2,3,\ldots,n-2.
$$
The asymmetric profile theorem now applies directly: at least $r$ members on
these levels force the recurrence capacities, while fitting capacities
construct a family with exactly $r$ members on them. No trimming is needed.

For every $r\ge11$, Section 16 proves failure at $n=2r+5$, while
Sections 14--15 construct the full profile for every $n\ge2r+6$.
Consequently
$$
\boxed{n_0(r)=2r+5\qquad(r\ge11).}
$$

Together with He--Tang's exact values for $r=2,3$ and the finite theorem in
`SMALL_R_NOTE.md`, this gives the complete threshold classification
$$
 n_0(r)=
 \begin{cases}
  3,&r=2,\\
  8,&r=3,\\
  2r+4,&4\le r\le10,\\
  2r+5,&r\ge11.
 \end{cases}
$$
The least constant in He--Tang's bounded-error question
$n_0(r)\le2r+C$ for all $r\ge4$ is therefore $C=5$.

---

# 18. Audit and publication status

Four separate adversarial AI review passes dated 2026-07-16 attempted to
falsify the lower-window construction, the L4 reverse envelope, the
profile-theorem foundations, and the final assembly. None found a
mathematical error in a load-bearing argument. The first two audits drove
the release-critical repairs already incorporated above. Audit C found only
twelve minor or typographical issues; the present revision incorporates all
of them, including the two false but non-load-bearing sentences in the
technical note and L4 note.

The repository includes the companion L4 proof, finite verifiers, exact
$r=11$ witnesses, a complete Lean development for $r\ge4$, and explicit
statement-correspondence and axiom-audit files.

The result remains AI-assisted and has not undergone independent specialist
peer review. Lean verifies the original-formulation least-threshold theorem for
every $r\ge4$; the finite subranges use three disclosed `native_decide`
certificates, while the $r\ge378$ endpoint is purely symbolic. Specialist
human scrutiny is still strongly encouraged, especially for statement
correspondence, the finite checker soundness bridges, Sections 5--8, Section
16, and the companion L4 proof.

---

# 19. References

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
   Combinatorics **11** (2004), R50.
