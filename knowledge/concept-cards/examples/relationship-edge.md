---
synthetic: true
surface_class: user-authored
record_type: relationship-edge
id: edge-prepared-provenance-precedes-support
revision: 1
relation_type: precedes
directed: true
from_ref:
  id: cc-prepared-source-provenance
  revision: 1
to_ref:
  id: cc-claim-support-is-assertion-specific
  revision: 1
source_support_refs:
  - id: support-synthetic-edge-001
    revision: 1
evidence_grade: provisional
extraction_confidence: direct
validation_result_refs: []
verification_result_refs: []
reconciliation_result_refs: []
preservation_decision_refs: []
memory_admission_refs: []
---

# Relationship Edge

**Synthetic example.** This directed edge says prepared-source provenance
precedes claim-support assessment in the synthetic method flow. It does not say
that either endpoint proves the other.

## Support Scope

`support-synthetic-edge-001` supports the edge assertion only. The provisional
grade, direct extraction confidence, and empty lifecycle-result lists remain
separate statements about this edge.
