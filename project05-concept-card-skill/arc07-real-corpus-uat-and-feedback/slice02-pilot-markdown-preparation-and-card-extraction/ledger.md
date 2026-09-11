# Slice02 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S2-1 | The pinned corpus source is acquired outside the planning tree and identified exactly. | Inspect `artifacts/source-acquisition.md` for checkout/archive path, commit, tree, hashes or equivalent identity evidence, and cleanup/non-vendoring statement. | serious | Slice01 protocol | open | | |
| S2-2 | Pilot Markdown preparation covers only the declared Chapter 1 and Chapter 7 sample. | Inspect manifest, structure map, locator map, and artifact paths for sampled sections only. | serious | Slice01 sampling plan | open | | |
| S2-3 | Prepared-source evidence preserves locators, dependencies, readiness, and caveats. | Inspect `prepared-source-manifest.md`, `structure-map.md`, `locator-map.md`, and `validation-readiness.md`. | serious | document-extraction | open | | |
| S2-4 | Candidate concept-card records are small, source-faithful, and reviewable. | Inspect `candidate-cards/` and `extraction-run.md` for one-concept discipline, source support, evidence grade, extraction confidence, and unresolved dependency handling. | serious | concept-cards | open | | |
| S2-5 | Figures, citations, and cross-references are not silently promoted to support. | Inspect candidate records, support records, and caveats for directly inspected or explicitly unresolved dependencies. | correctness-grade | UAT protocol | open | | |
| S2-6 | Pilot review packet distinguishes candidate output from operator acceptance, verification, and memory admission. | Inspect `pilot-review-packet.md` for review states, operator tasks, and explicit non-admission boundaries. | serious | UAT protocol | open | | |
| S2-7 | Real-use friction and missing guidance are captured for Slice03 disposition. | Inspect `friction-log.md` for source-preparation, extraction, validation, review-burden, and RAG-handoff findings with severity and suggested disposition. | serious | feedback loop | open | | |
| S2-8 | Scope and hygiene remain clean. | Run `git diff --check`; inspect source/planning status; confirm no full corpus vendoring, whole-corpus run, source-skill edits, or runtime implementation without explicit approval. | serious | repository hygiene | open | | |

Rows: 8. Open: 8. Done: 0. Deferred: 0. No-op: 0.
