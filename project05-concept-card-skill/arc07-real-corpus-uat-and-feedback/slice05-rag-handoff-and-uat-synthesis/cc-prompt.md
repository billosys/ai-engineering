# CC Prompt: Arc07 Slice05 RAG Handoff And UAT Synthesis

You are CC working in Expedited Mode on Project05 Arc07 Slice05.

## Required Reading

Read these files before editing:

1. `project05-concept-card-skill/project-plan.md`
2. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/arc-plan.md`
3. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/ledger.md`
4. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice05-rag-handoff-and-uat-synthesis/slice-plan.md`
5. `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice05-rag-handoff-and-uat-synthesis/ledger.md`
6. CDC verification and artifacts for Slices01 through 04, especially:
   - Slice01 corpus intake and UAT protocol
   - Slice02 candidate packet and friction log
   - Slice03 finding disposition and source-change summary
   - Slice04 coverage plan, candidate packet, caveat report, review packet,
     friction log, and CDC verification

## Task

Create the Slice05 handoff and synthesis artifacts under:

```text
project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice05-rag-handoff-and-uat-synthesis/artifacts/
```

Required artifacts:

- `handoff-manifest.md`
- `candidate-set-inventory.md`
- `projection-assumptions.md`
- `query-and-access-needs.md`
- `uat-synthesis.md`
- `coverage-caveats-and-reentry.md`
- `runtime-boundary.md`
- `arc07-close-inputs.md`

The handoff should be useful for forthcoming memory-protocol/RAG/graph/MCP
planning while preserving Project05's boundary: no runtime implementation,
no retrieval-quality claim, no operator acceptance, no semantic verification,
no reconciliation, no preservation decision, and no memory admission unless
separate scoped evidence actually exists.

## Guardrails

- Do not generate additional concept cards or widen corpus coverage.
- Do not implement graph/RAG/MCP, vector storage, retrieval evaluation, import
  automation, or memory runtime behavior.
- Do not claim the ten-card set is complete, accepted, verified, admitted, or
  runtime-ingested.
- Preserve the Slice04 full-book re-entry condition.
- Preserve unrelated work in both source and planning worktrees.

## Validation

- Confirm candidate references resolve to Slice04 and Slice02 paths.
- Confirm projection assumptions are requirements and design inputs, not
  implemented runtime facts.
- Confirm UAT synthesis accounts for Slices01 through 04 and all major caveats.
- Run `git diff --check`.
- Inspect source and planning `git status --short --untracked-files=all`.

## Commit Discipline

Use explicit file names in commit commands. If source and planning both change,
use separate commits for source changes and planning closeout. Include the
required co-author trailers in assistant-authored commits.

Close with a concise report naming the planning commit, artifacts, validation
performed, and any remaining CDC/operator review needs.
