# Slice01 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | Final gates pass against the post-Arc07 source tree. | Run `make check-skills`, `make check-skill-versions`, `make check-package-paths`, and `make all`; record warnings and failures. | serious | project DoD | open | | Use current source after the Arc07 `document-extraction` refinement. |
| S1-2 | Generated packages match documented Project05 support shapes. | Inspect `target/skills/document-extraction.zip` and `target/skills/concept-cards.zip` for entrypoints, sibling histories, guides, templates, examples, and `concept-cards/references/`. | serious | package closure | open | | Fresh packages only. |
| S1-3 | Project ledger P-2 through P-11 is reconciled after Arc07. | Update and inspect `project05-concept-card-skill/ledger.md`; ensure P-8 accounts for Arc07 and no UAT finding silently drops. | serious | project closure | open | | P-9 through P-11 are Arc07-fed rows; P-8 is final composition. |
| S1-4 | Final project closeout records deferrals, no-ops, follow-ons, warnings, and incidents explicitly. | Inspect `project05-concept-card-skill/closing-report.md` and any slice artifacts for final boundary language and evidence. | serious | project closure | open | | Include Arc06 baseline plus Arc07 UAT. |
| S1-5 | Runtime, retrieval, operator-review, and memory-admission boundaries remain explicit. | Scan final artifacts for claims about card acceptance, semantic verification, reconciliation, preservation, full-book completion, retrieval quality, graph/RAG/MCP implementation, import automation, or memory admission. | serious | Arc07 boundary | open | | These may be future work, not Project05 completion claims. |
| S1-6 | Scope and hygiene remain clean. | Run `git diff --check`; inspect source and planning status; confirm no unrelated work is committed. | serious | repository hygiene | open | | Commit explicit pathspecs only. |

Rows: 6. Open: 6. Done: 0. Deferred: 0. No-op: 0.
