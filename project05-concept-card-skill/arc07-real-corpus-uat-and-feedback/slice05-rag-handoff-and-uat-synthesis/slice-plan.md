# Slice05 Plan: RAG Handoff And UAT Synthesis

```yaml
project: project05-concept-card-skill
arc: arc07-real-corpus-uat-and-feedback
slice: slice05-rag-handoff-and-uat-synthesis
status: cdc-verified
opened: 2026-09-11
depends-on:
  - slice04-expanded-corpus-card-generation
```

## Goal

Synthesize the real-corpus UAT evidence and package the bounded candidate-card
set for downstream RAG/graph/MCP planning without implementing a runtime or
claiming retrieval quality. The handoff must make coverage, caveats,
candidate-review state, projection assumptions, and follow-on boundaries clear
enough for the future memory-protocol work to consume.

## Artifact Home

Durable Slice05 artifacts live under:

```text
arc07-real-corpus-uat-and-feedback/slice05-rag-handoff-and-uat-synthesis/artifacts/
```

Expected artifact groups:

- `handoff-manifest.md`
- `candidate-set-inventory.md`
- `projection-assumptions.md`
- `query-and-access-needs.md`
- `uat-synthesis.md`
- `coverage-caveats-and-reentry.md`
- `runtime-boundary.md`
- `arc07-close-inputs.md`

## In Scope

- Inventory the ten-card candidate set and identify its source paths, coverage,
  lifecycle states, and unresolved dependencies.
- Summarize UAT findings from Slices01 through 04, including what worked,
  friction, accepted source refinements, no-ops, caveats, and partial coverage.
- Define a downstream projection handoff for future RAG/graph/MCP work:
  record identities, fields likely needed, locator requirements, graph/retrieval
  assumptions, access/query needs, and unresolved design questions.
- Preserve the distinction between generated candidates, operator-accepted
  cards, independently verified records, memory admission decisions, and runtime
  ingestion.
- Preserve the full-book re-entry condition from Slice04.
- Prepare Arc07 close inputs for child-slice composition and Arc08 closure
  refresh.

## Out Of Scope

- Implementing a graph database, vector index, GraphRAG system, MCP server,
  retrieval evaluator, memory runtime, or import automation.
- Claiming retrieval quality or query answerability from the candidate set.
- Operator acceptance, independent semantic verification, reconciliation,
  preservation, or memory admission for any candidate card.
- Generating additional concept cards or widening corpus coverage.
- Editing source skills unless the operator explicitly approves a narrow
  correction for a newly discovered blocking defect.

## Verification

- Inspect all expected artifacts and confirm they reference Slice01 through
  Slice04 evidence.
- Confirm candidate inventory resolves to the Slice04 and Slice02 card paths
  and preserves candidate/unverified/unadmitted status.
- Confirm projection assumptions are framed as downstream requirements, not
  implemented runtime behavior.
- Confirm UAT synthesis includes accepted refinements, checked no-ops,
  unresolved caveats, full-book re-entry, and remaining operator review needs.
- Confirm `arc07-close-inputs.md` is sufficient for Arc07 closure.
- Run `git diff --check`.
- Inspect source and planning `git status --short --untracked-files=all`.

## Exit Criteria

This slice exits when the bounded candidate-card corpus, UAT evidence, RAG
handoff assumptions, runtime boundaries, full-book re-entry condition, and
Arc07 close inputs are durable and inspectable, with no runtime or memory
admission claims smuggled into Project05.
