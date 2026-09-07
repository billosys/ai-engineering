# Slice02 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S2-1 | The required `examples/` files exist as sibling support material and are routed from `SKILL.md`. | Check each required example path and grep `knowledge/concept-cards/SKILL.md` for a live example/support map. | serious | slice plan | open | | |
| S2-2 | Source version and sibling history advance without duplicate skill-version prose or example-local histories. | Inspect `SKILL.md`, `version-history.md`, and the owned tree; run `make check-skill-versions`. | correctness-grade | repository contract | open | | Expected bump: compatible minor version from `1.4.0`. |
| S2-3 | Examples cover the release-critical Project03 v4.0 set. | Inspect examples for minimal card, claim-backed card, CQ coverage, relationship/edge, extraction-run trace, reconciliation, memory-admission, and parallel-worker default recipe coverage. | serious | Project03 v4.0 | open | | |
| S2-4 | Examples preserve Arc03 construct and lifecycle distinctions without flattening them into one confidence/status field. | Grep and review examples for separate cards, claims, support, locators, edges, CQs, runs, validation, verification, reconciliation, preservation, memory admission, evidence grade, and extraction confidence. | serious | Arc03 close | open | | |
| S2-5 | Examples support document-extraction handoff boundaries. | Inspect source-related example fields for prepared-source provenance and confirm no raw PDF/EPUB/HTML cleanup procedure is owned by `concept-cards`. | serious | Arc02 dependency | open | | |
| S2-6 | Availability/handoff wording is current for templates and examples. | Grep `SKILL.md` and guides for stale claims that templates or examples remain future/unavailable, while confirming schema/reference and validation-review support remain future until Slice03. | correctness-grade | Slice01 bubble-up | open | | |
| S2-7 | Scope exclusions are preserved. | Inspect source commit scope for no schema/reference support, package/docs/install edits, executable validators, runtime systems, `concept-card-method`, or `source-preparation` roots. | serious | slice plan | open | | |
| S2-8 | Focused source validation and local links pass. | Run `scripts/check-skill-description.sh knowledge/concept-cards/SKILL.md`, quick skill validation, `git diff --check`, `make check-skills`, `make check-skill-versions`, and a scoped local link/anchor check over `knowledge/concept-cards/`. | serious | repository gate | open | | `make check-package-paths` is conditional unless package surfaces change. |

Rows: 8. Open: 8. Done: 0. Deferred: 0. No-op: 0.
