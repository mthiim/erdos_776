import Erdos776.Uniform.ProblemStatement

/-!
# Permanent axiom audit

Run this file with

```text
lake env lean lean/AxiomAudit.lean
```

`tools/check_axiom_audit.py` checks the output against the documented exact
allowlist.  The three finite-range declarations below intentionally expose
one generated native-evaluation axiom each.  The symbolic declarations use
only Lean/mathlib's standard quotient, choice, and propositional-extensionality
axioms.
-/

#print axioms Erdos776.L4.l4_multiplicity_profile_infeasible
#print axioms Erdos776.Uniform.isErdosThreshold_of_ge_378

#print axioms Erdos776.Uniform.lowerWindowFiniteBaseCheck_verified
#print axioms Erdos776.Uniform.smallUniformFiniteCheck_verified
#print axioms Erdos776.Uniform.smallThresholdFiniteCheck_verified

#print axioms Erdos776.Uniform.isErdosThreshold_of_ge_4
#print axioms Erdos776.Uniform.erdos776_threshold
