# Slice 03: Relationship, CQ, and Run Semantics

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice03-graph-cq-run-semantics
status: open
artifact-home: artifacts/
opened-on: 2026-08-30
```

## Goal

Define the v4.0 conceptual semantics for graph-native relationships,
competency questions, extraction runs, and reconciliation. This slice turns
the v3.2 relationship and CQ practices, plus the v4.0 lifecycle attachment
points from Slice02, into model-level semantics that Slice04 can synthesize
into the accepted conceptual model.

The output is conceptual-model material for Arc03. It should name the
construct boundaries, lifecycle dependencies, and open decisions needed for
model synthesis, but it must not choose final schema syntax, implementation
algorithms, package layout, deterministic validator implementation, or source
edits.

## Inputs

- `../slice01-construct-boundaries/cdc-verification.md`
- `../slice01-construct-boundaries/artifacts/v40-construct-boundary-model.md`
- `../slice01-construct-boundaries/artifacts/v40-construct-decision-register.md`
- `../slice02-evidence-lifecycle/cdc-verification.md`
- `../slice02-evidence-lifecycle/artifacts/v40-evidence-lifecycle-model.md`
- `../slice02-evidence-lifecycle/artifacts/v40-evidence-state-decision-register.md`
- `../../arc02-method-inventory/closing-report.md`
- `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc02-synthesis.md`
- `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md`

## In Scope

- Define relationship/edge semantics for v4.0, including how the v3.2
  relationship fields carry forward, when an edge needs identity, what
  endpoint and direction semantics are required, and where evidence,
  verification, and reconciliation attach.
- Define competency-question semantics: whether a CQ is a requirement, test,
  retrieval query, coverage target, or a construct that can play several of
  those roles under explicit statuses.
- Define extraction-run traceability semantics: the minimum conceptual record
  for source snapshot, method or prompt version, agent scope, generated or
  updated card set, old-card inputs, preservation decisions, validation
  results, and reconciliation results.
- Define reconciliation semantics across cards, claims, relationships/edges,
  CQs, and extraction runs, including conflict classes and result-record
  attachment points.
- Preserve v3.2 carry-forward strengths: typed relationship fields,
  competency-question coverage, source-primary re-extraction, parallel-worker
  coordination, validation, and preservation of unique prior-card value.
- Record accepted, provisional, deferred, and open decisions for Slice04 model
  synthesis and later architecture/implementation planning.

## Out of Scope

- Final schema syntax, exact enum spelling, YAML template shape, validator
  language, deterministic scripts, package behavior, README integration,
  Makefile changes, generated zips, or source edits.
- Final evidence-grade vocabulary, verification-state transitions, or memory
  admission policy except where graph/CQ/run semantics depend on the Slice02
  lifecycle layer.
- Reconciliation algorithms, graph database implementation, graph indexes,
  GraphRAG runtime, memory runtime, ontology database, or CCDP service design.
- Skill architecture, guide layout, package inclusion, examples, or
  implementation slice breakdown.

## Required Artifacts

Durable artifacts belong under `artifacts/`:

- `artifacts/v40-graph-cq-run-semantics.md` - conceptual model for
  relationship/edge, competency-question, extraction-run, and reconciliation
  semantics.
- `artifacts/v40-reconciliation-traceability-decision-register.md` - decision
  register for graph, CQ, run, and reconciliation constructs, including
  rationale, dependencies, status, downstream routing, and open questions.

## Verification Approach

The slice ledger uses grep-verifiable rows for artifact existence,
relationship/edge semantics, competency-question semantics, extraction-run
traceability, reconciliation semantics, scope fences, downstream routing, and
source-checkout cleanliness. CC should update the ledger with attested
evidence and write a closing report. CDC will independently reproduce the
ledger rows before the slice can be treated as closed.

## Exit Criteria

- The two required artifacts exist under `artifacts/`.
- The model defines relationship/edge semantics, including v3.2 carry-forward
  fields, endpoints, direction/inverse policy, graph closure expectations, and
  evidence/reconciliation attachment points.
- The model defines competency-question semantics, including requirement,
  answerability, coverage, verification, retrieval, obsolete, and deferred
  roles or statuses.
- The model defines extraction-run traceability, including source snapshot,
  method or prompt version, agent scope, output set, old-card inputs,
  preservation decisions, validation result, reconciliation result, and
  parallel-worker provenance.
- The model defines reconciliation semantics for duplicate concepts,
  competing definitions, slug/taxonomy drift, relationship asymmetry,
  CQ coverage conflicts, parallel-agent conflict, result records, and affected
  cards/claims/relationships/runs.
- Later work remains fenced: schema syntax, final enum spelling, algorithms,
  graph/runtime implementation, skill architecture, package behavior, and
  source edits are not performed in this slice.
- The source checkout remains clean.
