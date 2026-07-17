# A Leanified Proof of Erdős Problem 776

This repository presents a solution to [Erdős Problem #776](https://www.erdosproblems.com/776), with both a human-readable proof and a Lean formalization of that proof collected in a combined proof and verification [PDF](paper/erdos776_complete_thresholds.pdf).

## Contents

- [Problem and notation](#problem-and-notation)
- [Main theorem](#main-theorem)
- [Proof](#proof)
- [Lean proof](#lean-proof)
- [Combined proof document](#combined-proof-document)
- [Reproducing the checks](#reproducing-the-checks)
- [Attribution and responsibility](#attribution-and-responsibility)

## Problem and notation

The original problem asks:

> Let $r\ge2$ and $A_1,\ldots,A_m\subseteq\{1,\ldots,n\}$ be such that
> $A_i\not\subseteq A_j$ for all $i\ne j$, and suppose that for every $t$,
> if some $A_i$ has size $t$, then at least $r$ sets have size $t$.
>
> How large must $n$ be, as a function of $r$, to ensure that such a family
> can achieve $n-3$ distinct set sizes?

Write $[n]=\{1,\ldots,n\}$, and call a family satisfying these conditions an
**$r$-multiplicity antichain**. Its set of occupied sizes is

$$
L(\mathcal F)=\{|A|:A\in\mathcal F\}.
$$

Let $g(n,r)$ be the maximum possible value of $|L(\mathcal F)|$, and let
$n_0(r)$ be the least integer $N$ such that

$$
g(n,r)=n-3\qquad\text{for every }n>N.
$$

## Main theorem

For the threshold $n_0(r)$ defined for $r\ge2$, the package gives the complete
determination

$$
\boxed{
 n_0(r)=
 \begin{cases}
 3,&r=2,\\
 8,&r=3,\\
 2r+4,&4\le r\le10,\\
 2r+5,&r\ge11.
 \end{cases}}
$$

The values at $r=2,3$ are due to Yixin He and Quanyu Tang. The result for
every $r\ge4$ is formalized in Lean in this repository.

This is an end-to-end mathematical proof, not merely a numerical conjecture
check. Its structural arguments are symbolic; finite native evaluation is
used only for three explicitly bounded parameter ranges, through soundness
bridges proved in Lean. The entire range $r\ge378$ is proved symbolically.

As accessed on 17 July 2026, the [Erdős Problems page](https://www.erdosproblems.com/776)
still listed Problem 776 as open. [He and Tang](https://arxiv.org/abs/2602.09803)
had established $n_0(r)=2r+o(r)$ and determined the exact values for
$r=2,3$. Building on their results, this package claims the exact value for
every $r\ge4$.

The original problem treats $r=1$ separately: the relevant extremal number
of occupied levels is $n-2$, whereas $n_0(r)$ is defined for the $n-3$
threshold when $r\ge2$.

## Proof

The complete human-readable proof is available in the
[combined PDF](paper/erdos776_complete_thresholds.pdf). The
[Lean proof](#lean-proof) section below describes the architecture of the
formal proof and gives the main entry points for reviewing it.

For a guided conceptual review, read:

1. [`docs/PROOF_GUIDE.md`](docs/PROOF_GUIDE.md)
2. [`docs/TECHNICAL_NOTE.md`](docs/TECHNICAL_NOTE.md)
3. Sections 14--16 of
   [`docs/UNIFORM_THEOREM.md`](docs/UNIFORM_THEOREM.md#14-core-carry-and-feasibility-on-r5-points)

### Exact finite range `4 <= r <= 10`

The profile criterion gives an obstruction at `n=2r+4` and a tight
construction at `n=2r+5`.  A canonical core on `r+5` points has `r` explicit
free sets, so the same two-point padding mechanism covers every larger `n`.
Thus

$$
n_0(r)=2r+4\qquad(4\le r\le10).
$$

See [`docs/SMALL_R_NOTE.md`](docs/SMALL_R_NOTE.md) and the stored
certificates under [`certificates/`](certificates/).

### Exact case `r = 11`

The package proves and directly certifies

$$
g(27,11)=23,
\qquad
n_0(11)=27.
$$

The 24-level profile on `[27]` fails at level 2:

$$
m_2=352>\binom{27}{2}=351.
$$

An explicit 253-set antichain gives the matching 23-level lower bound.  A
checked core, 11 stored free sets, and a two-point padding chain give the
full profile for every `n>=28`.

See [`docs/TECHNICAL_NOTE.md`](docs/TECHNICAL_NOTE.md).

### Uniform theorem for `r >= 11`

The companion manuscripts give an AI-assisted proof, formalized in Lean, for

$$
\boxed{n_0(r)=2r+5\qquad(r\ge11).}
$$

Its main interface is the upper-core carry `1<=e<=6`. Lower-window
feasibility gives the upper capacities and `e<=6`; L4 gives `e>=1`; positive
carry gives the obstruction; bounded carry, puncturing, and persistent padding
give every later construction.

See [`docs/UNIFORM_THEOREM.md`](docs/UNIFORM_THEOREM.md) and
[`docs/L4_PROOF.md`](docs/L4_PROOF.md).

## Lean proof

Lean proves the claimed threshold for every $r\ge4$ as an end-to-end theorem
about actual finite antichains. The theorem includes failure at the displayed
threshold value, construction for every larger ground-set size, and leastness
under the strict convention $n>N$. It does not stop at checking that a
numerical recurrence exceeds a binomial coefficient.

The structural proof is symbolic. In particular, Lean proves the numerical
Kruskal--Katona bridge, the necessity and sufficiency of the profile
recurrence, L4 and diagonal transfer, the upper-core carry, the free-core and
persistent-padding constructions, the occupied-level reduction, and the
translation back to the original problem formulation. Every bridge from a
finite checker to a recurrence statement, and from a recurrence statement to
an actual antichain theorem, is itself proved in Lean.

The original-formulation endpoint
`Erdos776.Uniform.erdos776_threshold` proves the least-threshold statement
above for every $r\ge4$. Its internal counterpart is
`Erdos776.Uniform.isErdosThreshold_of_ge_4`. The cited cases $r=2,3$ are not
formalized in this repository.

Three finite initial ranges are discharged by explicitly isolated native
evaluations, while the remaining argument is symbolic:

- `4<=r<=10`: seven values are checked for failure, first success, and core
  feasibility;
- `11<=r<=28`: eighteen values are checked for upper-core data and direct
  full-profile overflow;
- `29<=r<=377`: a ground-bounded checker verifies the lower-window
  capacities for 349 values;
- `r>=378`: the lower window, L4, carry, obstruction, construction, and
  leastness are all proved symbolically, with no finite evaluation.

The source contains no `sorry`, `admit`, or project `axiom` declarations.
The three closed finite evaluations use `native_decide`, so the complete
endpoint additionally trusts Lean's native evaluator/compiler; the axiom
audit reports exactly the corresponding three generated certificate axioms.
The symbolic $r\ge378$ endpoint reports only standard Lean/mathlib axioms.
No Python result or stored witness is a logical premise of the Lean theorem.

For a formal review, begin with:

1. [`lean/PROBLEM_STATEMENT_CORRESPONDENCE.md`](lean/PROBLEM_STATEMENT_CORRESPONDENCE.md)
2. [`lean/THEOREM_CROSSWALK.md`](lean/THEOREM_CROSSWALK.md)
3. [`Erdos776/Uniform/ProblemStatement.lean`](Erdos776/Uniform/ProblemStatement.lean)
4. [`lean/AxiomAudit.lean`](lean/AxiomAudit.lean)

See also [`lean/README.md`](lean/README.md) and
[`lean/FORMALIZATION_STATUS.md`](lean/FORMALIZATION_STATUS.md) for the exact
scope and trust boundary.

## Combined proof document

A generated combined source and PDF are included under [`paper/`](paper/):

```text
paper/erdos776_complete_thresholds.md
paper/erdos776_complete_thresholds.pdf
```

Release identifier: `v0.4.1-proof-claim`.

The PDF combines the profile theorem, exact `r=11` note, small-`r` theorem,
L4 proof, and uniform theorem into one dated review document.

## Reproducing the checks

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
- an independently implemented exact cross-check of all finite ingredients
  supporting `n_0(r)=2r+4` for every `4<=r<=10`;
- the exact lower-window finite base `11<=r<=377`, with named seam checks at
  `r=377,378,379`;
- the exact L4 finite base `11<=r<=28`, including the precise level-2
  overflow, and symbolic-formula checks;
- a supplementary exact uniform-assembly cross-check;
- exhaustive comparison of the prescribed-profile criterion with every
  antichain profile for `n=4,5,6`.

The scripts and their logical roles are documented in
[`verification/README.md`](verification/README.md).

The complete release audit is:

```bash
lake exe cache get
lake build --wfail
python3 tests/verify_all.py
python3 tools/check_lean_placeholders.py
python3 tools/check_github_math.py
python3 tools/check_axiom_audit.py
./paper/build_pdf.sh
```

GitHub CI runs this same sequence; see
[`.github/workflows/ci.yml`](.github/workflows/ci.yml). The detailed scope and
trust boundary are recorded in the Lean documentation linked below.

## Attribution and responsibility

The work was developed through a human-led collaboration involving multiple
language models.  A contribution-level account is in
[`docs/AI_ASSISTANCE_AND_CREDITS.md`](docs/AI_ASSISTANCE_AND_CREDITS.md).

The repository is coordinated and maintained by `mthiim`, who is responsible
for preserving the submitted artifact, reporting corrections, and maintaining
the contribution record. This identifies responsibility for the artifact, not
sole personal origination of the proof. The language models are not treated as
accountable authors or independent certifiers.
