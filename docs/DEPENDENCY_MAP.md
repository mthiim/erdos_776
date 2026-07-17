# Dependency map for the complete threshold table

The threshold `n_0(r)` is the least `N` for which `g(n,r)=n-3` whenever
`n>N`.

## 1. Statement layer

`Erdos776/Uniform/ProblemStatement.lean` follows the wording of Erdős
Problems #776 and proves its equivalence to the reusable internal definitions:

```text
ProblemAdmissible
  <-> IsMultiplicityAntichain

ProblemTargetExists
  <-> OccupiedMiddleProfileExists
  <-> FullMiddleProfileExists       (r>=4 in the threshold range)
```

`ProblemLastFailure r N` says that `N` fails and every `n>N` works. It
immediately implies the least eventual threshold `ProblemThreshold r N`.

## 2. Small multiplicities

- He--Tang prove `n_0(2)=3` and `n_0(3)=8`; these values are cited rather
  than formalized here.
- For `4<=r<=10`, `SmallRangeCertificate.lean` verifies:

  1. recurrence overflow at `n=2r+4`;
  2. recurrence feasibility at `n=2r+5`;
  3. canonical core feasibility on `r+5` points.

Profile sufficiency constructs the first successful full profile. Each
displayed top core member is punctured at one common point to obtain a free
set. Persistent two-point padding and core-to-full cover every `n>=2r+6`.
The resulting Lean endpoint is `isErdosThreshold_of_ge_4_le_10`.

## 3. Uniform range `r>=11`: carry-centered dependency

Let `a_b` be the upper-core recurrence on `A=r+4` points. The central
interface is `HasUpperCoreData r`:

$$
a_b\le\binom Ab\quad(4\le b\le r+2),\qquad
a_3=\binom A3+e,\qquad 1\le e\le6.
$$

For `r>=29`, this interface is derived as follows:

1. **Lower window.** `LowerWindowFits r` gives the upper capacities after
   complementation and gives `e<=6`. It is native-checked for
   `29<=r<=377` and symbolic for `r>=378`.
2. **L4.** The semantic L4 theorem rules out zero carry, so `e>=1`. L4 is
   symbolic for `r>=29`.

For `11<=r<=28`, a direct closed checker certifies the upper capacities,
`1<=e<=6`, and the final level-two full-profile overflow. Its soundness
theorems connect the Boolean result to the same semantic interfaces.

Once `HasUpperCoreData` is available:

3. **Core.** `e<=6` proves the complete core recurrence feasible on `r+5`
   points.
4. **Free sets.** The displayed top core members belong to the canonical
   core. Puncturing each one at a common point gives `r` free `(r+1)`-sets by
   antichainness alone.
5. **Construction.** Persistent padding plus core-to-full gives
   `FullMiddleProfileExists n r` for every `n>=2r+6` and both parities.
6. **Obstruction.** Positive carry enters the full recurrence through the
   no-carry diagonal shell. L4 controls the residual and forces overflow at
   `n=2r+5`.
7. **Global threshold.** The singleton/complement reduction identifies
   `n-3` occupied sizes with the full middle profile and proves leastness.

The resulting endpoint is `isErdosThreshold_of_ge_11`.

The traditional parameter `alpha_r` satisfies `alpha_r=r-e`; it is useful
motivation but is no longer a node required by the main dependency graph.

## 4. Complete formalized range

`ThresholdTable.lean` combines the two ranges:

```lean
theorem isErdosThreshold_of_ge_4 (r : ℕ) (hr : 4 ≤ r) :
    IsErdosThreshold r (erdosThresholdFromFour r)
```

`ProblemStatement.lean` exposes the same result in the problem's original
existence language:

```lean
theorem erdos776_threshold (r : ℕ) (hr : 4 ≤ r) :
    ProblemThreshold r (erdosThresholdFromFour r)
```

where the value is `2*r+4` through `r=10` and `2*r+5` from `r=11` onward.
