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
