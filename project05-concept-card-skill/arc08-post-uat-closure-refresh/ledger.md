# Arc08 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A8-1 | Final repository gates pass against the post-Arc07 source tree. | Run `make check-skills`, `make check-skill-versions`, `make check-package-paths`, and `make all`; record warning dispositions. | serious | project DoD | open | | Arc07 made one source refinement in `document-extraction`; final closure must use current packages. |
| A8-2 | Current generated packages still contain the documented Project05 support shapes. | Inspect `target/skills/document-extraction.zip` and `target/skills/concept-cards.zip` for entrypoint, sibling history, guides, templates, examples, and `concept-cards/references/`. | serious | project DoD | open | | Use fresh packages from the final gate run. |
| A8-3 | Project ledger rows P-2 through P-11 are reconciled without silent drops. | Inspect closed arc evidence and update `project05-concept-card-skill/ledger.md` with reproduced evidence, explicit deferrals, or explicit no-op decisions. | serious | project closure | open | | P-8 remains open until final project close composes Arc07. |
| A8-4 | Final deferral/follow-on statement preserves nondeferrable objectives and Arc07 boundaries. | Read the final project closeout and verify deferrals exclude live installable `document-extraction` and `concept-cards`; verify candidate review, runtime, retrieval, graph/MCP, and memory admission are future boundaries, not hidden claims. | serious | operator reorientation | open | | Adjacent future work may be recorded with reasons and re-entry conditions. |
| A8-5 | Project closure artifacts and hygiene are complete. | Inspect final project closing report, Arc08 slice closeout, whitespace checks, source status, and planning status. | serious | project closure | open | | Must integrate Arc06 baseline and Arc07 UAT close. |
| A8-6 | Arc08 closes Project05 only if the full project composes. | Inspect Arc08 closing report for slice walk, composition, accepted warnings, source changes, no-ops, deferrals, and project ledger bubble-up. | serious | project closure | open | | The closure decision is evidence-based, not automatic. |

Rows: 6. Open: 6. Done: 0. Deferred: 0. No-op: 0.
