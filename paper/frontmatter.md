---
title: "Erdős Problem 776: exact thresholds for antichains with level multiplicity"
author: "Human-led, AI-assisted research package"
date: "17 July 2026 - release tag v0.4.1-proof-claim"
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

$$
 n_0(r)=
 \begin{cases}
 3,&r=2,\\
 8,&r=3,\\
 2r+4,&4\le r\le10,\\
 2r+5,&r\ge11.
 \end{cases}
$$

The values at `r=2,3` are due to Yixin He and Quanyu Tang. Lean proves the
original least-threshold statement for every `r>=4`: `4<=r<=10` uses one
closed seven-value certificate, `11<=r<=28` one closed eighteen-value
certificate, `29<=r<=377` one ground-bounded lower-window certificate, and
`r>=378` a symbolic proof. The checker definitions and soundness bridges are
ordinary Lean definitions and proofs; the three closed finite evaluations use
`native_decide` and therefore additionally trust Lean's native
evaluator/compiler. Four separate adversarial AI review passes attempted to
falsify the argument. They are not treated as independent specialist peer
review.

The load-bearing proof is split into the following four parts in this PDF:

1. the prescribed-profile criterion and exact `r=11` result;
2. the finite exact range `4<=r<=10`;
3. the L4 reverse-envelope theorem;
4. the uniform `r>=11` construction and obstruction.

The source repository contains the original-formulation Lean statement, exact
certificates, standard-library verification scripts, theorem crosswalk,
axiom audit, proof guide, audit trail, and contribution record.

\newpage
