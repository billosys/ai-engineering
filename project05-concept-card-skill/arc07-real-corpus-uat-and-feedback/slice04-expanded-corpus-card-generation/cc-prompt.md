# CC Prompt: Arc07 Slice04 Expanded Corpus Card Generation

You are CC working in Expedited Mode on Project05 Arc07 Slice04.

## Required Reading

Read these files before editing:

1. `project05-concept-card-skill/project-plan.md`
2. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/arc-plan.md`
3. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/ledger.md`
4. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/slice-plan.md`
5. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/ledger.md`
6. Slice01, Slice02, and Slice03 close artifacts, especially:
   - Slice01 `artifacts/corpus-intake.md`
   - Slice01 `artifacts/uat-protocol.md`
   - Slice02 `artifacts/source-acquisition.md`
   - Slice02 `artifacts/friction-log.md`
   - Slice03 `artifacts/finding-disposition.md`
   - Slice03 `cdc-verification.md`
7. Current `document-extraction` and `concept-cards` source guidance relevant
   to Markdown preparation, citation resources, extraction, support, lifecycle
   fields, validation, and memory-admission boundaries.

## Task

Generate an expanded concept-card candidate set from the pinned
`CompCogNeuro/book` corpus or an explicitly justified subset.

First write `artifacts/coverage-plan.md` before card generation. It must name
the pinned source snapshot, included and excluded units, expected output shape,
stop conditions, and whether the run is full-corpus or a bounded subset. Do
not silently narrow the user's corpus goal merely to make the slice easier.
If full-corpus generation is too large for this slice, record a bounded subset,
the reason, and the re-entry condition.

Then write the source-preparation, dependency, extraction, candidate-card,
validation-sampling, review, caveat, and friction artifacts required by the
slice plan.

## Guardrails

- Keep the upstream corpus checkout outside the planning tree.
- Generated records are candidates unless the operator actually reviews them.
- Do not claim semantic verification, reconciliation, preservation, memory
  admission, or runtime ingestion unless a separate scoped record establishes
  that work.
- Do not implement graph/RAG/MCP, vector storage, retrieval evaluation, or a
  memory runtime in this slice.
- Do not make source-skill edits unless a new blocking defect is discovered
  and the operator approves a narrow correction.
- Preserve unrelated work in both source and planning worktrees.

## Required Artifacts

Write under:

```text
project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice04-expanded-corpus-card-generation/artifacts/
```

Required files or directories:

- `coverage-plan.md`
- `source-preparation-manifest.md`
- `dependency-audit.md`
- `extraction-run.md`
- `candidate-cards/`
- `validation-sampling.md`
- `coverage-and-caveat-report.md`
- `review-packet.md`
- `friction-log.md`

## Validation

- Inspect coverage before extraction output claims.
- Check candidate/support records for claim-specific support, locators,
  source-faithful qualifications, and lifecycle boundaries.
- Check dependency handling for figures, citations, and cross-references.
- Run `git diff --check`.
- Inspect source and planning `git status --short --untracked-files=all`.

## Commit Discipline

Use explicit file names in commit commands. If source and planning both change,
use separate commits for source changes and planning closeout. Include the
required co-author trailers in assistant-authored commits.

Close with a concise report naming the planning commit, generated artifacts,
coverage decision, validation performed, stop/caveat findings, and any
remaining CDC/operator review needs.
