# Erdős Problem #776: complete threshold table (AI-assisted theorem candidate)

This repository is a reproducible AI-assisted research
package for the Erdős--Trotter antichain problem
([Erdős Problem #776](https://www.erdosproblems.com/776)).

## Main result

For the threshold `n_0(r)` defined for `r>=2`, the package gives the complete
candidate determination

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

The values at `r=2,3` are due to Yixin He and Quanyu Tang.  The exact finite
range `4<=r<=10`, the independently certified case `r=11`, and the uniform
argument for `r>=11` are documented here.

The original problem treats `r=1` separately: the relevant extremal number
of occupied levels is `n-2`, whereas `n_0(r)` is defined for the `n-3`
threshold when `r>=2`.

## Components

### Exact finite range `4 <= r <= 10`

The profile criterion gives an obstruction at `n=2r+4` and a tight
construction at `n=2r+5`.  A canonical core on `r+5` points has `r` explicit
free sets, so the same two-point padding mechanism covers every larger `n`.
Thus

\[
n_0(r)=2r+4\qquad(4\le r\le10).
\]

See [`docs/SMALL_R_NOTE.md`](docs/SMALL_R_NOTE.md) and the stored
certificates under [`certificates/`](certificates/).

### Exact case `r = 11`

The package proves and directly certifies

\[
g(27,11)=23,
\qquad
n_0(11)=27.
\]

The 24-level profile on `[27]` fails at level 2:

\[
m_2=352>\binom{27}{2}=351.
\]

An explicit 253-set antichain gives the matching 23-level lower bound.  A
checked core, 11 stored free sets, and a two-point padding chain give the
full profile for every `n>=28`.

See [`docs/TECHNICAL_NOTE.md`](docs/TECHNICAL_NOTE.md).

### Uniform theorem candidate for `r >= 11`

The companion manuscripts give an AI-assisted proof candidate for

\[
\boxed{n_0(r)=2r+5\qquad(r\ge11).}
\]

Their main ingredients are the classical prescribed-profile squashing
theorem and Kruskal--Katona, a reverse-envelope proof of the upper core
window, a uniform lower-window supersolution, an exact core-carry identity,
explicit free sets and indefinite padding, and a diagonal cascade transfer
that obstructs `n=2r+5`.

See [`docs/UNIFORM_THEOREM.md`](docs/UNIFORM_THEOREM.md) and
[`docs/L4_PROOF.md`](docs/L4_PROOF.md).

## Review status

Four adversarial AI audits found no mathematical error in a load-bearing
argument. 

Some parts of the argument have undergone human review, but especially the L4 proof requires much more scrutiny.

## Stable proof document

A single combined source and PDF are included under [`paper/`](paper/):

```text
paper/erdos776_complete_thresholds.md
paper/erdos776_complete_thresholds.pdf
```

The PDF combines the profile theorem, exact `r=11` note, small-`r` theorem,
L4 proof, and uniform theorem into one dated review document.

## One-command verification

Python 3.10 or newer is sufficient; only the standard library is used.

```bash
python3 tests/verify_all.py
```

Expected final line:

```text
ALL COMPLETE-THRESHOLD RELEASE CHECKS PASSED
```

The command runs:

- the release-critical `r=11` certificate and padding checks;
- an independent exact proof/certificate check of
  `n_0(r)=2r+4` for every `4<=r<=10`;
- the exact lower-window finite base `11<=r<=377`, with named seam checks at
  `r=377,378,379`;
- the exact L4 finite base `11<=r<=28`, including the precise level-2
  overflow, and symbolic-formula checks;
- a supplementary exact uniform-assembly cross-check;
- exhaustive comparison of the prescribed-profile criterion with every
  antichain profile for `n=4,5,6`.

The scripts and their logical roles are documented in
[`verification/README.md`](verification/README.md).

## Attribution and responsibility

The work was developed through a human-led collaboration involving multiple
language models.  A contribution-level account is in
[`docs/AI_ASSISTANCE_AND_CREDITS.md`](docs/AI_ASSISTANCE_AND_CREDITS.md).

