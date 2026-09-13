# Slice06 Handoff

Delivered 37 contextual memberships: root id/revision for claim,
competency-question, extraction-run, memory-admission, preservation-decision,
reconciliation-result, relationship-edge, source-locator, source-support,
validation-result and verification-result; root record_type for those kinds and
concept-card; and untyped category/subcategory/tier.

The key integration boundary is that record identity/revision is local to its
record kind. It must not absorb actor, subject, endpoint, source or lifecycle
identities. record_type remains a record discriminator, not a semantic taxonomy.
Legacy category/subcategory are discovery vocabulary and tier is pedagogical
depth, distinct from each other and from source coordinates. Current-template
absence is not evidence of migration loss.

This leaves 508 pairs outside Batch01/Slice06 for their existing owners.
Slice04 may consume this packet only after CDC review; it does not close
Slice04, Slice01 or Arc01. Later research must decide any future
classification/migration design rather than treating these observed legacy
fields as an accepted schema.
