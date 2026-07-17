import Erdos776.Combinatorics.Cascade
import Erdos776.Combinatorics.CascadeNormalForm
import Erdos776.Combinatorics.CascadeFamily
import Erdos776.Combinatorics.Antichain
import Erdos776.Combinatorics.Padding
import Erdos776.Combinatorics.CoreToFull
import Erdos776.Combinatorics.FiniteColex
import Erdos776.Combinatorics.NumericShadow
import Erdos776.Combinatorics.NormalShadow
import Erdos776.Combinatorics.BoundedShadow
import Erdos776.Combinatorics.DiagonalTransfer
import Erdos776.Combinatorics.ProfileNecessity
import Erdos776.Combinatorics.ProfileSufficiency
import Erdos776.Combinatorics.ProfileCriterion
import Erdos776.L4.CascadeSteps
import Erdos776.L4.ReverseSteps
import Erdos776.L4.ReverseEnvelope
import Erdos776.L4.Profile
import Erdos776.Uniform.DiagonalObstruction
import Erdos776.Uniform.Assembly
import Erdos776.Uniform.FreeCore
import Erdos776.Uniform.CoreCarry
import Erdos776.Uniform.OccupiedLevels
import Erdos776.Uniform.GlobalThreshold
import Erdos776.Uniform.LowerWindow.PhaseParameters
import Erdos776.Uniform.LowerWindow.PhasePositions
import Erdos776.Uniform.LowerWindow.PhaseTransitions
import Erdos776.Uniform.LowerWindow.PhaseBounds
import Erdos776.Uniform.LowerWindow.PhaseHarvest
import Erdos776.Uniform.LowerWindow.PhaseCanonical
import Erdos776.Uniform.LowerWindow.PhaseStart
import Erdos776.Uniform.LowerWindow.PhaseCapacity
import Erdos776.Uniform.LowerWindow.RisingTail
import Erdos776.Uniform.LowerWindow.GeneralizedEnvelope
import Erdos776.Uniform.LowerWindow.ScalarStates
import Erdos776.Uniform.LowerWindow.EnvelopeSegments
import Erdos776.Uniform.LowerWindow.FullEnvelope
import Erdos776.Uniform.LowerWindow.PhaseAssembly
import Erdos776.Uniform.LowerWindow.FiniteChecker
import Erdos776.Uniform.LowerWindow.FiniteCertificate
import Erdos776.Uniform.FiniteProfileChecker
import Erdos776.Uniform.FiniteCertificate
import Erdos776.Uniform.SmallRangeCertificate
import Erdos776.Uniform.ThresholdTable
import Erdos776.Uniform.ProblemStatement

/-!
# Erdős Problem 776

Lean formalization of the non-computational arguments in the accompanying
research package.  It includes the reverse-envelope proof named L4 and the
symbolic diagonal-shell obstruction at `n = 2r+5`, together with the global
occupied-level reduction and the complete symbolic lower-window supersolution
for `r ≥ 378`, together with verified bounded-shadow certificates completing
the least global threshold table for every `r ≥ 4`.
-/
