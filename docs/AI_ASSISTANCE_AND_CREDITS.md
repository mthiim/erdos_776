# AI assistance, contribution map, and authorship notes

This project was coordinated by a human researcher and developed with
substantial assistance from several language models. 

## Human coordinator and maintainer

`mthiim` coordinates and maintains the repository and is responsible for
preserving the submitted artifact, reporting corrections, and maintaining the
contribution record. This responsibility does not assert sole personal
origination of the proof. The language models are not treated as accountable
authors or independent certifiers.

- selected the problem and research direction;
- coordinated the separate model sessions and review passes;
- preserved and transferred intermediate packages between sessions;
- decided which claims and proof routes to pursue.

## Collaborating LLM A - Claude Fable 5 (Anthropic; proof-development session)

Principal contributions supplied by the model that generated and extended
the original package:

- initial application of the prescribed-profile squashing criterion;
- the original exact `r=11` code, certificates, and padding chain;
- extensive computational exploration of the threshold pattern;
- forced-structure, slot, L4/L5, and multi-side investigations;
- the reverse-envelope proof of L4 (`alpha_r<=r-1`);
- the first bounded lower-window construction and diagnosis of O2;
- the early anchor-deepening/top-fractal proposal;
- the first explicit observation that the same machinery yields
  `n_0(r)=2r+4` for `4<=r<=10`, together with exploratory checks of the
  small cores and free sets.
- reconstructed the lower-window proof as canonical run-compressed cascades;
- checked identities, capacities, phase seams, and scalar collapse;
- performed broad computational falsification at finite and very large
  parameter values;

## OpenAI GPT-5.6 Pro - review/proof collaborator

Principal contributions in this collaboration:

- a separate audit of the original package, including discovery and repair
  of the missing occupied-level reduction;
- separate checking of the `r=11` arithmetic, certificates, core, free
  sets, and indefinite padding argument;
- the diagonal Kruskal--Katona identity and its transfer application;
- the explicit uniform family of free sets in the canonical core;
- the simplifications `L4=>L5` and `L4=>` the one-seed obstruction;
- formalization of the exact anchor ladder;
- the all-`r` lower-window supersolution using the additional anchor,
  compressed phases, one-digit rising tail, generalized envelope, and
  scalar bottom collapse;
- assembly and editing of the uniform theorem;
- a separate derivation and exact cross-check of
  `n_0(r)=2r+4` for every `4<=r<=10`, including the finite obstruction,
  full witnesses, core/free-set certificates, and persistent-padding
  verifier;
- integration of the adversarial audits, complete-threshold package,
  proof-dossier PDF, and release tooling.

## OpenAI Codex (including GPT-5.6 Sol-Max) - audit and Lean formalization

Principal contributions across the audit and formalization sessions:

- performed a second hostile audit of Sections 3--11 and the theorem
  assembly;
- found no counterexample in the intended domain;
- identified release-critical written defects, including the unstated phase
  invariant, false unqualified shadow wording, missing hypotheses for the
  diagonal identity, compressed reflection/transfer arguments, and
  incomplete packaging;
- formalized canonical cascades, finite colex realization, numerical shadows,
  and the prescribed-profile necessity/sufficiency bridge;
- formalized semantic L4, diagonal shell transfer, the upper-core carry,
  punctured free core, persistent padding, core-to-full, occupied-level
  reduction, and global leastness;
- completed the symbolic lower-window proof for `r>=378` and built the
  ground-bounded evaluator and sound finite certificates for all remaining
  values `r>=4`;
- added the original-formulation final theorem, theorem crosswalk, proof guide,
  axiom/source audits, and CI integration;
- simplified the human proof around the carry interface, asymmetric profile
  criterion, no-carry shell principle, lower-window segment table, and
  puncturing lemma.
