# Slice 02: v4.0 Gap Analysis

```yaml
project: project03-concept-card-method
arc: arc02-method-inventory
slice: slice02-v40-gap-analysis
status: open
artifact-home: artifacts/
depends-on:
  - project03-concept-card-method:arc02-method-inventory:slice01-v32-source-inventory
blocks:
  - project03-concept-card-method:arc02-method-inventory:slice03-inventory-synthesis
related:
  - ../../arc-plan.md
  - ../../ledger.md
  - ../../../project-plan.md
  - ../../../ledger.md
  - ../slice01-v32-source-inventory/cdc-verification.md
  - ../slice01-v32-source-inventory/artifacts/v32-source-inventory.md
  - ../slice01-v32-source-inventory/artifacts/v32-method-structure-map.md
  - ../slice01-v32-source-inventory/artifacts/v32-original-assessment.md
```

## Goal

Produce a source-backed v4.0 gap analysis from the verified v3.2 baseline.

This slice should identify what v3.2 keeps, what v4.0 must change, what is a
minor cleanup rather than an architectural change, and what needs operator
choice before Arc03 defines the conceptual model.

## Scope

In scope:

- Use the verified Slice01 artifacts as the primary baseline.
- Compare v3.2 baseline constructs against Project03's v4.0 target concerns:
  evidence/provenance grading, independent verification, reconciliation,
  memory admission, graph-native relationships, CCDP-compatible evidence
  semantics, skill packaging, schema validation, semantic QA, and extraction
  run traceability.
- Classify each finding as `carry forward`, `minor cleanup`, `architectural
  change`, `operator decision`, or `defer`.
- Distinguish source-preserving carry-forward items from changes that require
  new v4.0 concepts or process states.
- Record the reasoning and source anchors for each gap.
- Produce inputs suitable for Slice03 synthesis and Arc03 conceptual-model
  planning.

Out of scope:

- Designing the v4.0 conceptual model.
- Deciding the final skill layout.
- Writing the future `SKILL.md`, guide files, templates, scripts, or package
  lists.
- Editing source files in `/Users/oubiwann/lab/billosys/ai-engineering`.
- Changing the preserved v3.2 source snapshots or original assessment memo.
- Running extraction against a live corpus.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `v40-gap-register.md` - source-backed register of v4.0 gaps, categories,
  evidence, rationale, and downstream routing.
- `v32-to-v40-carry-forward-change-matrix.md` - matrix separating v3.2 items
  to preserve from minor cleanups, architectural changes, operator decisions,
  and deferrals.

## Verification Approach

Verify that the open set exists, both required artifacts exist under
`artifacts/`, the gap register covers all named v4.0 concern areas, the matrix
separates carry-forward items from architectural changes and operator
decisions, and the slice preserves the boundary that Arc03 owns conceptual
model design while Arc04 owns final skill layout.

## Exit Criteria

- Slice02 open set exists: `slice-plan.md`, `ledger.md`, and `cc-prompt.md`.
- `artifacts/v40-gap-register.md` exists.
- `artifacts/v32-to-v40-carry-forward-change-matrix.md` exists.
- Gap register covers evidence/provenance grading, independent verification,
  reconciliation, memory admission, graph-native relationships,
  CCDP-compatible evidence semantics, skill packaging, schema validation,
  semantic QA, and extraction run traceability.
- Matrix distinguishes `carry forward`, `minor cleanup`, `architectural
  change`, `operator decision`, and `defer`.
- Artifacts identify inputs for Slice03 and Arc03 without designing the v4.0
  conceptual model.
- No source files are edited.
