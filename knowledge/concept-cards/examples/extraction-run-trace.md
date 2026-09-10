---
synthetic: true
surface_class: trace-record
record_type: extraction-run
id: extraction-synthetic-method-note-002
revision: 1
input_source_ref:
  id: de-synthetic-method-note-002
  revision: 1
  path: document-extraction/raw/synthetic-method-note-002.txt
prepared_source_ref:
  id: de-prepared-synthetic-method-note-002
  revision: 1
  path: document-extraction/prepared/synthetic-method-note-002.md
worker_scope:
  mode: agent-direct
  worker_count: 1
  roles: [extractor]
output_refs:
  - id: cc-claim-support-is-assertion-specific
    revision: 1
    record_type: concept-card
  - id: claim-support-is-assertion-specific
    revision: 1
    record_type: claim
extraction_confidence: direct
validation_result_refs: []
verification_result_refs: []
reconciliation_result_refs: []
preservation_decision_refs: []
memory_admission_refs: []
---

# Extraction-Run Trace

**Synthetic example.** `document-extraction` owns conversion and raw-source
cleanup. This trace consumes its prepared snapshot, records the actual one-worker
scope, and identifies the derived records without claiming they are validated,
independently verified, reconciled, preserved, or admitted.

## Caveat

The supplied synthetic preparation had no recorded omissions. That caveat is
run provenance, not semantic source support for any downstream claim.
