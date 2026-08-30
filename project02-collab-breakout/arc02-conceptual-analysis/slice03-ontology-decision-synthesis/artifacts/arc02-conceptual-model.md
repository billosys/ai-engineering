# Arc02 Conceptual Model

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
slice: slice03-ontology-decision-synthesis
status: proposed-done
architecture-decisions: none
model-status: analytical, non-final, not accepted architecture
```

## Evidence Basis

This model consumes the Slice01 input contract and CDC verification, especially
`../slice01-boundary-analysis-instrument/artifacts/conceptual-analysis-method.md`,
`component-boundary-ledger.md`, and `arc02-input-evidence-register.md`.

It also consumes the Slice02 CDC verification and verified Slice02 artifacts:
the `candidate-boundary evaluation`,
`component relationship map`, and `conceptual risk register`.

Arc01 contributes reproduced Project02 control evidence through
`../../arc01-framework-inventory/closing-report.md`,
`arc01-synthesis.md`, `candidate-component-inputs.md`, and
`arc02-question-register.md`.

The live source checkout was used only for spot-check grounding. No source file
was edited. This artifact does not decide final architecture; final selection
belongs to Arc03 functional analysis, Arc04 architecture work, and operator
acceptance.

## Model Summary

Arc02's current conceptual model is a component graph with four likely zones:

- a top-level collaboration-framework composer and adapter surface;
- a project-management component family;
- a standalone ledger-verification component with dependency edges into
  project-management close mechanics;
- specialized operational guide candidates for audit, coverage, delegation,
  and contribution work.

The model also contains support assets, templates, constraints,
package/release gate concepts, non-component concepts, and dependency edges
that must not be promoted to standalone components merely because they are
named.

## Candidate Components

These labels have strong evidence-backed reason to load and remain candidate
component entries for Arc04, not final accepted components:

| Candidate component | Owned problem | Required dependency edges | Current disposition |
|---------------------|---------------|---------------------------|---------------------|
| `collaborative-posture-and-ethics` | Sycophancy, false certainty, role-power blur, structural-pull blindness, and hidden failure. | prerequisite to `engineering-methodology-and-process`; supports contribution voice. | Strong standalone posture candidate and likely methodology dependency. |
| `engineering-methodology-and-process` | Knowledge-substrate loss, SDLC drift, abstraction failure, weak verification posture, and monolithic process load. | uses posture; routes to PM, ledger, audit, coverage, delegation, and contribution components. | Core methodology candidate, but must shed specialized details it only routes to. |
| `ledger-verification-protocol` | Row closure, evidence strength, independent verification, deferral/no-op discipline, and silent-drop prevention. | prerequisite for PM close guides; supports audit and coverage evidence language. | Strong standalone candidate; dependency direction must be explicit. |
| `code-audit-discipline` | Evidence-based diagnosis, multi-scale review, severity calibration, and modernization based on observed findings. | uses domain skills; cites ledger evidence semantics; owns standalone audit output rules. | Strong operational component candidate. |
| `coverage-hardening-discipline` | Hard coverage threshold, root-cause test repair, warning treatment, and quality gate closure. | uses repo-specific tooling and domain test idioms; contrasts with diagnosis-only audit. | Standalone candidate after naming and generality correction. |
| `delegation-policy` | Preventing subagent judgment leakage while preserving parallel lookup leverage. | supports methodology and constrains planning, audit, and review work. | Narrow, low-risk standalone operational component candidate. |
| `contribution-style-and-voice` | Calibrated upstream ticket voice, maintainer burden reduction, and evidence-bounded public claims. | uses `contribution-ticket-template`; supported by posture and methodology. | Candidate component paired with a template support asset. |

## Component Family Members

Project management is the clearest component family. It has a distinct reason
to load, but the Slice02 evidence does not prove that each guide should become
a separate top-level component.

| Component family member | Family role | Disposition |
|-------------------------|-------------|-------------|
| `project-management-wayfinder` | Entrypoint adapter for PM load routing. | Keep as PM entrypoint, not the whole component. |
| `project-management-scale-model` | Vocabulary and sizing model for project, arc, slice, step, and iteration. | Core PM family member. |
| `planning-worktree-and-layout` | Canonical planning branch/worktree, filenames, and artifact-home rules. | Core PM guide and cross-cutting constraint. |
| `planning-open-set-mechanics` | Project, arc, and slice opening discipline, including falsifiable ledgers. | Core PM planning guide. |
| `slice-close-and-bubble-up` | Slice close report, artifact inventory, silent-drop diff, and slice-to-arc bubble-up. | PM close guide using ledger semantics. |
| `arc-project-composition-close` | Parent-scale recomposition, remediation-not-iteration, and project bubble-up. | PM close guide using ledger semantics. |
| `planning-confirmation-protocol` | Operator confirmation for ambiguous layout or artifact conventions. | PM support guide unless Arc03 proves direct standalone use. |

## Support Assets

Support assets should travel with the component that owns the rule or workflow
they support:

- `protocol-distribution-guidance`: support asset and constraint that keeps
  CCDP protocol packaging distinct from installable skill package behavior.
- `planning-anti-patterns-and-repair`: corrective PM support asset.
- `project-management-examples`: PM example asset; useful after the rules are
  loaded, not a primary component.
- `project-management-provenance`: PM version-history and rationale asset.
- `evidence-backed-modernization`: support asset or dependency edge under
  `code-audit-discipline`.
- `contribution-ticket-template`: template support asset under
  `contribution-style-and-voice`.

## Adapters

Adapters mediate entry rather than owning the full discipline:

- `framework-entrypoint-and-routing` is the top-level composer candidate. It
  should remain thin if Arc04 accepts a breakout.
- `repository-orientation-and-distribution` is a README/source-clone and
  package-reader adapter with package/release gate concerns.
- `agent-adapter-and-routing` translates CDC/CC/Claude/Codex role language
  across surfaces and constrains standalone component usability.
- `project-management-wayfinder` routes PM users to the correct PM family
  member.

## Dependency Edges

The graph needs explicit dependency edge ownership before architecture work:

- Posture is a prerequisite for methodology.
- Methodology routes to specialized operational components; it should not
  duplicate their full mechanics.
- PM close mechanics use ledger discipline; ledger owns evidence semantics and
  row closure.
- Code audit uses domain skills and evidence discipline while retaining
  diagnosis-only output ownership.
- Coverage hardening uses repo-specific test tooling and domain test idioms.
- Contribution ticket template supports contribution style and should not ship
  as an isolated guide without the voice discipline.
- Every future component is constrained by Project01 package/release gates.

## Constraints

The conceptual model includes these constraints:

- Project01 and `project01-harmonise-paths` remain a cross-cutting constraint,
  not a user-facing component.
- Current source files and package paths are evidence, not final boundaries.
- Package behavior must distinguish source clone, generated skill zip, unzipped
  install, and CCDP protocol package workflows.
- Standalone components must remain readable when loaded without the top-level
  composer.
- Shared evidence terms must not drift between methodology, ledger, PM close,
  audit, and coverage.

## Templates

Templates are reusable shapes, not automatically components. The current
template concept is `contribution-ticket-template`, which should travel with
the contribution guide. Ledger examples and PM examples are template-like
support assets owned by ledger or PM respectively.

## Package/Release Gates

The following package/release gate concepts remain cross-cutting component
contract requirements for Arc04 and Arc05:

- source/package vocabulary stays explicit;
- package-local Markdown links remain valid;
- generated skill zip roots and entrypoints remain coherent;
- README and SKILL routing preserve source clone, skill zip, unzipped install,
  and CCDP package distinctions;
- CCDP stays a separate protocol package, not an installable skill component;
- `make check-package-paths` remains the release surface validation gate.

## Non-Component Concepts

Some concepts belong in the ontology but should not become standalone packages
on current evidence:

- `verification-methodology`: shared ontology and dependency edge across
  methodology, ledger, PM close, audit, and coverage.
- `path-contract-constraints`: cross-cutting constraint and package/release
  gate, denied as standalone component on current evidence.
- `framework-maintenance-discipline`: support asset plus missing maintenance
  contract candidate; final owner remains an Arc04 decision.
- evidence strength and memory admission vocabulary: conceptual glue that
  should be owned by the ledger/methodology relationship, not duplicated.

## Soft Layout Hypothesis Assessment

The operator-provided soft layout hypothesis is useful as tested input, not
accepted architecture.

Supported by evidence:

- `knowledge/collaboration-framework/` as a thin composer over accepted
  components.
- `knowledge/project-management/` as a likely component family with internal
  guides and support assets.
- `knowledge/ledger-discipline/` as a plausible standalone ledger component.

Not yet accepted:

- each PM split file as a standalone package;
- a broad code-quality family that merges audit and coverage;
- central-only agent-adapter wording with no standalone component notes;
- package layout or source moves.

Arc03 should test usage/load moments. Arc04 should decide architecture with
operator acceptance. Arc05 should plan implementation and package validation.
