---
synthetic: true
surface_class: user-authored
record_type: concept-card
id: cc-claim-support-is-assertion-specific
revision: 1
title: Claim support is assertion-specific
prepared_source_refs:
  - id: de-prepared-synthetic-method-note-002
    revision: 1
    path: document-extraction/prepared/synthetic-method-note-002.md
claim_refs:
  - id: claim-support-is-assertion-specific
    revision: 1
    path: records/claim-support-is-assertion-specific.md
evidence_grade: provisional
extraction_confidence: direct
validation_result_refs:
  - id: validation-synthetic-claim-shape-001
    revision: 1
    path: records/validation-synthetic-claim-shape-001.md
verification_result_refs:
  - id: verification-synthetic-claim-001
    revision: 1
    path: records/verification-synthetic-claim-001.md
reconciliation_result_refs: []
preservation_decision_refs: []
memory_admission_refs: []
---

# Claim-Backed Card

**Synthetic example.** The prepared source below is a fictional prepared note;
the support record is scoped to one claim, not to the card as a whole.

## Claim

`claim-support-is-assertion-specific` asserts: a prepared document alone does
not support a claim until the relevant span is inspected and linked.

## Source Locator And Support

The locator names `de-synthetic-method-note-002`, revision 1, section
`Support assertions`. Its synthetic span says that an assertion needs an
inspectable source span. `support-synthetic-claim-001` records that span as
support for the claim above, with direct extraction confidence and provisional
evidence grade. It does not support unrelated assertions on this card.

## Lifecycle Records

`validation-synthetic-claim-shape-001` is a structural, same-context check of
the record shape. `verification-synthetic-claim-001` records a same-context
semantic comparison, not independent verification. Reconciliation,
preservation, and memory admission are unassessed and have no result records.
