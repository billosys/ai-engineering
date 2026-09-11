# Slice01 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | Corpus identity and license are recorded. | Inspect `artifacts/corpus-intake.md` for source URL, commit/ref or supplied snapshot identity, license, and access method. | serious | UAT intake | open | | |
| S1-2 | Corpus structure and candidate source files are inventoried. | Inspect `artifacts/corpus-intake.md` for chapter/frontmatter/endmatter/glossary/references/metadata/figures inventory and any exclusions. | serious | UAT intake | open | | |
| S1-3 | UAT questions and measures are defined before generation. | Inspect `artifacts/uat-protocol.md` for decision, claims under test, measures, evidence to collect, stop conditions, and limitations. | serious | scientific-methods | open | | |
| S1-4 | Pilot sample is justified and representative enough for real feedback. | Inspect `artifacts/pilot-sampling-plan.md` for selected files/sections, rationale, expected pressure on both skills, and caveats. | correctness-grade | UAT design | open | | |
| S1-5 | RAG/graph/MCP handoff assumptions are explicit and bounded. | Inspect `artifacts/rag-handoff-assumptions.md` for intended downstream use, import shape expectations, query/access goals, and runtime boundaries. | serious | memory protocol preparation | open | | |
| S1-6 | Planning hygiene and scope boundaries are clean. | Run `git diff --check`; inspect source/planning status; confirm no full corpus vendoring or source edits occurred without explicit approval. | serious | repository hygiene | open | | |

Rows: 6. Open: 6. Done: 0. Deferred: 0. No-op: 0.
