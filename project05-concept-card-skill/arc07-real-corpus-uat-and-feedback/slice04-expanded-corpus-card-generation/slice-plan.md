# Slice04 Plan: Expanded Corpus Card Generation

```yaml
project: project05-concept-card-skill
arc: arc07-real-corpus-uat-and-feedback
slice: slice04-expanded-corpus-card-generation
status: cdc-verified
opened: 2026-09-11
depends-on:
  - slice03-feedback-driven-skill-refinement
```

## Goal

Generate an expanded concept-card candidate set from the pinned
`CompCogNeuro/book` corpus or an explicitly justified accepted subset, using
the updated `document-extraction` and `concept-cards` workflows. The slice must
make corpus coverage, dependency handling, validation sampling, caveats, and
review boundaries inspectable before any completeness or handoff claim.

## Artifact Home

Durable Slice04 artifacts live under:

```text
arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/
```

Expected artifact groups:

- `coverage-plan.md`
- `source-preparation-manifest.md`
- `dependency-audit.md`
- `extraction-run.md`
- `candidate-cards/`
- `validation-sampling.md`
- `coverage-and-caveat-report.md`
- `review-packet.md`
- `friction-log.md`

## In Scope

- Reuse the pinned corpus commit
  `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d`, acquired outside the planning
  tree.
- Define the expanded coverage target before extraction: full corpus, selected
  chapters, or another justified subset.
- Prepare source evidence for the selected coverage, including structure,
  locators, figure/citation/cross-reference dependency handling, readiness,
  and caveats.
- Apply the Slice03 citation-bearing Markdown rule where citation keys affect
  candidate support.
- Generate concept-card candidates with claim-specific support records,
  lifecycle fields, extraction-run provenance, and unresolved dependency
  caveats.
- Sample generated candidates for source-faithfulness, locator recovery,
  qualification retention, and lifecycle-boundary preservation.
- Produce a review packet that clearly distinguishes assistant-generated
  candidates from operator-accepted or independently verified records.
- Record any new real-use friction for Slice05 synthesis or later follow-on
  work.

## Out Of Scope

- Operator acceptance of generated cards unless the operator explicitly
  performs and records review.
- Treating candidates as verified truth, reconciled records, admitted memory,
  or runtime-ingested data.
- Production graph database, GraphRAG, MCP server, vector store, memory
  runtime, or retrieval evaluation.
- Whole-bibliography research unless required by the selected coverage and
  bounded by the slice plan.
- Source-skill edits unless a new blocking defect is discovered and the
  operator explicitly approves a narrow correction.

## Verification

- Inspect coverage plan before generated-card claims.
- Inspect source-preparation records, dependency audit, locator records,
  extraction run, candidate cards, support records, validation sampling, and
  review packet.
- Confirm selected coverage is neither silently narrowed nor silently widened.
- Confirm all generated records preserve evidence grade, extraction confidence,
  validation, verification, reconciliation, preservation, and memory-admission
  distinctions.
- Confirm figures, citations, and cross-references are directly inspected,
  sampled with stated limits, or explicitly caveated.
- Confirm generated cards remain candidates unless operator review actually
  occurs.
- Run `git diff --check`.
- Inspect source and planning `git status --short --untracked-files=all`.

## Exit Criteria

This slice exits when the expanded corpus candidate set, or an explicitly
caveated stop/partial set, is inspectable with source coverage, dependency,
validation sampling, review, and caveat evidence sufficient for Slice05 RAG
handoff and UAT synthesis planning.
