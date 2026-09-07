# Slice01 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | The required `templates/` files exist as sibling support material and are routed from `SKILL.md`. | Check each required template path and grep `knowledge/concept-cards/SKILL.md` for a live template/support map. | serious | slice plan | open | | |
| S1-2 | Source version and sibling history advance without duplicate skill-version prose or template-local histories. | Inspect `SKILL.md`, `version-history.md`, and the owned tree; run `make check-skill-versions`. | correctness-grade | repository contract | open | | Expected bump: compatible minor version from `1.3.0`. |
| S1-3 | Templates cover user-authored, trace-record, and result-record surfaces. | Inspect templates for concept card, claim, source locator/support, relationship edge, CQ, extraction run, validation, verification, reconciliation, preservation, and memory admission coverage. | serious | Project03 v4.0 | open | | |
| S1-4 | Templates preserve Arc03 construct and lifecycle distinctions without flattening them into one confidence/status field. | Grep and review templates for separate evidence grade, extraction confidence, validation result, verification result/state, reconciliation result/state, preservation decision, and memory admission. | serious | Arc03 close | open | | |
| S1-5 | Templates support document-extraction handoff boundaries. | Inspect source-related fields for prepared-source provenance and confirm no raw PDF/EPUB/HTML cleanup procedure is owned by `concept-cards`. | serious | Arc02 dependency | open | | |
| S1-6 | Scope exclusions are preserved. | Inspect source commit scope for no examples, schema/reference support, package/docs/install edits, executable validators, runtime systems, `concept-card-method`, or `source-preparation` roots. | serious | slice plan | open | | |
| S1-7 | Focused source validation and local links pass. | Run `scripts/check-skill-description.sh knowledge/concept-cards/SKILL.md`, quick skill validation, `git diff --check`, `make check-skills`, `make check-skill-versions`, and a scoped local link/anchor check over `knowledge/concept-cards/`. | serious | repository gate | open | | `make check-package-paths` is conditional unless package surfaces change. |

Rows: 7. Open: 7. Done: 0. Deferred: 0. No-op: 0.
