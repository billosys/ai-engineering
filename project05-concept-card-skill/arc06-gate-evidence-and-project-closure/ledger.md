# Arc06 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A6-1 | Final repository gates pass against the current source tree. | Run `make check-skills`, `make check-skill-versions`, `make check-package-paths`, and `make all`; record any warning dispositions. | serious | project DoD | open | | |
| A6-2 | Current generated packages still contain the documented Project05 support shapes. | Inspect `target/skills/document-extraction.zip` and `target/skills/concept-cards.zip` for entrypoint, sibling history, guides, templates, examples, and `concept-cards/references/`. | serious | project DoD | open | | |
| A6-3 | Project ledger rows P-2 through P-8 are reconciled without silent drops. | Inspect closed arc evidence and update `project05-concept-card-skill/ledger.md` with reproduced evidence, explicit deferrals, or explicit no-op decisions. | serious | project closure | open | | |
| A6-4 | Final deferral/no-op statement preserves nondeferrable objectives. | Read the final project closeout and verify deferrals exclude live installable `document-extraction` and `concept-cards` unless the operator explicitly approves otherwise. | serious | operator reorientation | open | | |
| A6-5 | Project closure artifacts and hygiene are complete. | Inspect final project closing report, Arc06 slice closeout, whitespace checks, source status, and planning status. | serious | project closure | open | | |

Rows: 5. Open: 5. Done: 0. Deferred: 0. No-op: 0.
