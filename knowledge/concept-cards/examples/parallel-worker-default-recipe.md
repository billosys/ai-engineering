---
synthetic: true
surface_class: trace-record
record_type: extraction-run
id: extraction-synthetic-parallel-recipe-001
revision: 1
input_source_ref:
  id: de-synthetic-method-note-003
  revision: 1
prepared_source_ref:
  id: de-prepared-synthetic-method-note-003
  revision: 1
worker_scope:
  mode: agent-direct
  worker_count: 2
  roles: [source-scope, claim-support]
extraction_confidence: mixed
validation_result_refs: []
verification_result_refs: []
reconciliation_result_refs: []
preservation_decision_refs: []
memory_admission_refs: []
---

# Parallel-Worker Default Recipe

**Synthetic example.** A useful default assigns five roles when the work is
large enough: coordinator, source-scope worker, claim-support worker,
relationship/CQ worker, and integration/review worker. It is a recipe, not a
required worker count or a substitute for recorded actual scope.

## Recorded Run Scope

This synthetic run used two workers: source-scope and claim-support. The
coordinator performed integration in the same context, so the run retains
mixed extraction confidence and no independent verification result. Raw cleanup
was completed upstream by `document-extraction` before the workers began.

## Handoff

The next reviewer should inspect each worker output, preserve its source and
prepared-source identities, and record any validation, verification,
reconciliation, preservation, or admission result separately.
