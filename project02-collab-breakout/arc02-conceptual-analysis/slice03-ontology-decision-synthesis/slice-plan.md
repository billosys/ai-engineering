# Slice 03: Ontology And Decision Synthesis

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
slice: slice03-ontology-decision-synthesis
status: proposed-done
opened-on: 2026-08-30
proposed-done-on: 2026-08-30
artifact-home: artifacts/
depends-on:
  - slice01-boundary-analysis-instrument:verified-closed
  - slice02-candidate-boundary-evaluation:verified-closed
blocks:
  - arc02-close
related:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-boundary-analysis-instrument/cdc-verification.md
  - ../slice01-boundary-analysis-instrument/artifacts/conceptual-analysis-method.md
  - ../slice01-boundary-analysis-instrument/artifacts/component-boundary-ledger.md
  - ../slice01-boundary-analysis-instrument/artifacts/arc02-input-evidence-register.md
  - ../slice02-candidate-boundary-evaluation/cdc-verification.md
  - ../slice02-candidate-boundary-evaluation/artifacts/candidate-boundary-evaluation.md
  - ../slice02-candidate-boundary-evaluation/artifacts/component-relationship-map.md
  - ../slice02-candidate-boundary-evaluation/artifacts/conceptual-risk-register.md
  - ../../arc01-framework-inventory/closing-report.md
  - ../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md
  - ../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md
  - ../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md
```

## Goal

Synthesize Arc02's conceptual-analysis evidence into the non-final ontology,
naming critique, merge/split findings, missing/overclaimed concept findings,
and operator decision register needed before Arc03 functional analysis and
Arc04 architecture work.

This slice should turn the evaluated candidate rows and relationship/risk
artifacts into a coherent conceptual model. It should preserve evidence
strength, distinguish likely components from support assets and constraints,
and explicitly name what remains undecided.

## Scope

In scope:

- Consume Slice01's conceptual-analysis method and input contract.
- Consume Slice02's verified candidate-boundary evaluation, relationship map,
  conceptual risk register, and CDC verification.
- Synthesize a non-final Arc02 conceptual model with candidate component
  families, standalone candidates, adapters, support assets, dependency edges,
  constraints, templates, package/release gates, and non-component concepts.
- Produce naming critique for mislabeled, surface-specific, over-broad, or
  hidden concepts.
- Record merge/split findings for improper merges, improper splits, deliberate
  overlaps, acceptable duplication, and unresolved relationship questions.
- Record missing and overclaimed concept findings, including component
  maintenance and ontology/boundary-review gaps.
- Produce an operator decision register for Arc04 with decision owner,
  decision options, evidence basis, default recommendation, and go / adjust /
  defer posture.
- Preserve the soft layout hypothesis as tested low-weight input, not accepted
  architecture.
- Carry Project01 path/package constraints forward as component-contract
  constraints for later architecture and implementation planning.
- Identify whether Arc02 can close after this slice or whether a remediation
  slice is required.

Out of scope:

- Selecting final breakout architecture.
- Creating source files, new skills, README changes, Makefile/package changes,
  package exceptions, or generated zip artifacts.
- Performing Arc03 functional usage analysis.
- Performing Arc04 architecture selection.
- Editing planning artifacts outside Project02.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `arc02-conceptual-model.md` - synthesized non-final ontology of components,
  component families, adapters, support assets, constraints, dependency edges,
  templates, package/release gates, and non-component concepts.
- `boundary-and-naming-findings.md` - naming critique, merge/split findings,
  missing concept findings, overclaimed mechanism findings, overlap/duplication
  dispositions, and unresolved relationship questions.
- `arc04-operator-decision-register.md` - operator-facing decisions needed
  before Arc04 architecture, with options, evidence basis, risks, and
  recommended go / adjust / defer posture.
- `arc02-close-readiness.md` - assessment of whether Arc02 has delivered its
  promised capability, including arc-ledger row coverage and any remediation
  needs before formal arc close.

## Verification Approach

The slice verifies by checking that the required artifacts exist under
`artifacts/`, that they cite the verified Slice01/Slice02 inputs, that the
conceptual model includes all required classification families, that naming and
boundary findings cover the critical categories from Slice02, that operator
decisions are explicit and Arc04-oriented, that outputs remain analytical and
non-final, that Project01 path/package constraints remain visible, and that no
source files are edited.

## Exit Criteria

- Slice01 and Slice02 verified inputs are consumed and cited.
- `artifacts/arc02-conceptual-model.md` includes candidate components,
  component family members, support assets, adapters, dependency edges,
  constraints, templates, package/release gates, non-component concepts, and
  the soft layout hypothesis as tested input rather than accepted architecture.
- `artifacts/boundary-and-naming-findings.md` covers mislabels, improper
  merges, improper splits, missing concepts, overclaimed mechanisms, underfit,
  overfit, overlap, duplication, unresolved relationships, and
  component-maintenance concerns.
- `artifacts/arc04-operator-decision-register.md` records operator decisions
  with decision owner, options, evidence basis, risk, default recommendation,
  and go / adjust / defer posture.
- `artifacts/arc02-close-readiness.md` states whether Arc02 can close after
  Slice03 or needs remediation, and maps its verdict to the Arc02 ledger rows.
- Project01 path/package constraints are carried as cross-cutting
  component-contract constraints for Arc04/Arc05.
- Outputs remain analytical and non-final; final architecture remains deferred
  to Arc04 after Arc03 functional analysis and operator acceptance.
- No source files are edited.
