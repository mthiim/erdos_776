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
