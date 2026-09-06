# Arc02 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A2-1 | Slice01 creates the `document-extraction` source scaffold and load/output contracts. | Read Slice01 CDC verification and inspect `knowledge/document-extraction/SKILL.md`, `version-history.md`, `guides/01-load-contract.md`, `guides/02-workflow.md`, and `guides/03-output-contract.md`. | serious | arc plan | done | Slice01 CDC verification reproduced all seven Slice01 rows against source commit `fb8af78b2e4fe50cf0485bc26b9a8b063f460038`; direct inspection confirmed the five source files exist and match the assigned scaffold/load/output contract scope. Evidence strength: reproduced. | |
| A2-2 | Format-specific PDF and EPUB preparation guidance is implemented from the preserved v2 prompts. | Read Slice02 CDC verification and inspect the PDF/Marker and EPUB/pandoc guides. | serious | arc plan | open | | |
| A2-3 | Shared structure, media, locator, validation/readiness, and caveat guidance is implemented. | Read Slice03 CDC verification and inspect the shared guides. | serious | arc plan | open | | |
| A2-4 | Sibling templates and examples make the skill usable for human-assisted and agent-direct workflows. | Read Slice04 CDC verification and inspect `knowledge/document-extraction/templates/` and `knowledge/document-extraction/examples/`. | correctness-grade | arc plan | open | | |
| A2-5 | The implemented skill remains standalone and does not recreate the superseded `source-preparation` root. | Confirm `knowledge/document-extraction/` exists and `knowledge/source-preparation/` does not. | serious | operator reorientation | open | | |
| A2-6 | Arc02 preserves Arc01 package-layout constraints for sibling support directories. | Inspect Arc02 source output for sibling `guides/`, `templates/`, `examples/`, and `version-history.md`; confirm no support material is hidden under `guides/` as a packaging workaround. | correctness-grade | Arc01 | open | | |

Rows: 6. Open: 5. Done: 1. Deferred: 0. No-op: 0.
