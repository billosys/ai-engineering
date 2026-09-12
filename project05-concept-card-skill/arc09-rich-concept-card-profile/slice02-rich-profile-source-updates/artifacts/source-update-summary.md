# Slice02 Source Update Summary

## Delivered Source Change

Source commit: `1d6bbd08` (`Add rich concept-card profile`).

The live `concept-cards` skill now defaults real-corpus extraction to a rich,
readable, one-concept body while retaining the separate v4 control layer. The
owning entrypoint received a compatible minor version increment and matching
sibling history entry.

## Rich Profile Implementation

`templates/concept-card.md` now requires these body sections:

- concept boundary;
- quick definition and core definition;
- prerequisites and key properties;
- construction or recognition;
- context and application;
- examples;
- relationships and competency questions;
- common errors and common confusions;
- source reference and support map; and
- extraction notes and review boundaries.

Each section requires a reason when material is not applicable, not established
in the selected source, or unresolved. The template keeps source/prepared-source
provenance, claims, source support, extraction confidence, lifecycle states,
and result references distinct. Its extraction/review section expressly cannot
claim a completed check, operator acceptance, or memory admission.

The new `examples/rich-profile-card.md` is a synthetic, source-shaped example
with all required sections, fictional source/claim/support identities, a typed
edge and CQ reference, and unassessed lifecycle fields. It illustrates the
profile without representing real-corpus work or a completed review.

Guides 01 through 06 where owned by the scope, plus guide 08, make the rich
body operational for extraction and re-extraction while retaining source-support,
evidence, relationship/CQ, validation, verification, reconciliation,
preservation, operator-gate, and admission boundaries. The three review
references add structural candidates, semantic audit questions, and a bounded
operator exception for the rich profile.

## Changed Source Files

- `knowledge/concept-cards/SKILL.md`
- `knowledge/concept-cards/guides/01-load-contract.md`
- `knowledge/concept-cards/guides/02-operator-workflow.md`
- `knowledge/concept-cards/guides/03-extraction.md`
- `knowledge/concept-cards/guides/04-re-extraction-preservation.md`
- `knowledge/concept-cards/guides/05-evidence-lifecycle.md`
- `knowledge/concept-cards/guides/06-graph-cq.md`
- `knowledge/concept-cards/guides/08-validation-verification.md`
- `knowledge/concept-cards/templates/concept-card.md`
- `knowledge/concept-cards/examples/rich-profile-card.md`
- `knowledge/concept-cards/references/structural-validation-candidates.md`
- `knowledge/concept-cards/references/semantic-audit-boundaries.md`
- `knowledge/concept-cards/references/operator-review-gates.md`
- `knowledge/concept-cards/version-history.md`

## Intentionally Untouched

`document-extraction` was not changed: its source/preparation, mapping, and
locator contracts remain sufficient upstream provenance for this source-only
profile update, and no direct blocker was found. No Arc07 candidate card was
regenerated. No executable validator, schema, graph/RAG/MCP runtime, retrieval
evaluation, reconciliation, semantic verification, operator acceptance, or
memory admission was added or claimed.

## Slice03 Re-entry

Slice03 must execute the proof protocol in Slice01
`artifacts/validation-regression-plan.md`: compare the rich template/example to
the named `complete-musician` and Erlang v3.2 evidence; record required-section
coverage, source-specific-example traceability, wrapper hygiene, typed
relationship/CQ discipline, and lifecycle/evidence separation. The current
planning tree has no Slice03 CC prompt yet; that prompt must be created from the
Arc09 plan and this existing regression plan before implementation advances.
