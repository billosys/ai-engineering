---
record_type: extraction-run
id: null
revision: null
operation: null
method_ref: null
prompt_ref: null
settings: {}
actor: {id: null, role: null, mode: null}
started_at: null
finished_at: null
source_snapshot_refs: []
prepared_source_refs: []
prior_run_refs: []
intended_scope: null
actual_coverage: null
intended_outputs: null
old_card_inputs: []
agent_scope: null
parallel_worker_count: null
worker_outputs: []
output_refs:
  cards: []
  claims: []
  source_support: []
  locators: []
  edges: []
  cqs: []
extraction_confidence: {assessment: unassessed, rationale: null, scope: null}
preservation_refs: []
validation_refs: []
verification_refs: []
reconciliation_refs: []
memory_admission_refs: []
---

# Extraction Run: <operation and scope>

Use the [template conventions](../SKILL.md#record-templates),
[extraction](../guides/03-extraction.md) and, when applicable,
[re-extraction](../guides/04-re-extraction-preservation.md). This trace records
what actually happened; reviewing existing records need not invent an extraction.

## Source And Method Snapshot

<Identify source inputs, old-card revisions, method/prompt identity and revision,
material settings and supplied instructions. Keep old cards secondary to source.
For document-extraction output, reference original/prepared snapshots, preparation
run, manifest, maps, readiness and caveats as upstream provenance. Route raw
PDF/EPUB/HTML or converted-source cleanup there; a preparation run is distinct
from this concept-card run and does not establish assertion support.>

## Actor Scope And Worker Trace

<Record actual actor identity and assigned scope. Set parallel_worker_count to
the number of additional workers used, zero for none, or leave unknown with a
reason. For each worker_outputs entry, record worker identity/role, assigned
source/task coverage, input revisions, prompt variation, produced output refs,
conflicts and integration disposition/result refs. Record overlaps and gaps.
No fixed worker count or delegation is required; agreement is not verification.>

## Outputs, Coverage And Prior Value

<Distinguish intended from actual coverage and outputs. Record generated versus
updated status for each output reference, partial results and omissions.
Map prior values to preservation decisions and destinations; retain unresolved
material. Describe source drift and changed locator mappings without rewriting
the old input or run history.>

## Results And Limitations

<Link each validation, verification, reconciliation, preservation and admission
record with its actual target/scope, not one run-wide successful status.
Run-level extraction confidence describes the extraction act; it does not give
all output claims one evidence grade. Record unperformed checks explicitly.>

## Handoff

<Report input/output revisions and locations, direct versus operator-reported
observations, remaining coverage, failed or unavailable work, next checks and
storage/delivery limits. A completed trace implies no runtime or memory write.>
