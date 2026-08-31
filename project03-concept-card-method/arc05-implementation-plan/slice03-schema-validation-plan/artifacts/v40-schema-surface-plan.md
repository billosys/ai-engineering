# v4.0 Schema Surface Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice03-schema-validation-plan
artifact: v40-schema-surface-plan
status: proposed-done
schema-treatment: Markdown records with YAML frontmatter plus named sections
planned-source-home: knowledge/concept-card-method/
```

## Purpose

This artifact decides the v4.0 schema surface treatment for the concept-card
method. It preserves the accepted Arc03 conceptual model, the accepted Arc04
skill architecture, and the verified Slice02 source layout and content
sequence. It maps schema surfaces to planned template, example, guide, and
validation documentation paths without editing source files.

This is planning only. It does not edit source, does not perform source
implementation, does not create generated zips, does not perform package
release, does not claim release readiness, and does not create runtime
services, GraphRAG, graph database, ontology database, memory runtime, CCDP
service, or live extraction behavior.

## Schema Treatment Decision

Accepted Slice03 decision: the first implementation plan should represent
v4.0 concept-card method surfaces as Markdown records with YAML frontmatter
plus named body sections.

Rationale:

- The method is a human-operable knowledge skill, not a runtime service.
- Markdown keeps user-authored and reviewable surfaces legible.
- YAML frontmatter gives deterministic structural validation candidates stable
  field names without requiring a database.
- Named body sections preserve source-faithful synthesis, rationale, review
  notes, and human/operator judgment.
- Separate result records prevent hidden flattening of validation result,
  verification result, reconciliation result, preservation decision, and
  memory admission.

## Surface Map

| Surface | Representation | Planned template path | Planned example path | Primary guide path | Validation path |
|---------|----------------|-----------------------|----------------------|--------------------|-----------------|
| concept card | Markdown record for one concept with YAML frontmatter and sections for summary, claims, relationships, CQs, provenance, and lifecycle references. | `knowledge/concept-card-method/guides/templates/concept-card.md` | `knowledge/concept-card-method/guides/examples/minimal-card.md` | `knowledge/concept-card-method/guides/03-extraction.md` | `knowledge/concept-card-method/guides/validation/structural-candidates.md` |
| claim | Markdown-compatible record or embedded card section with stable claim id, statement, source support references, evidence grade, extraction confidence, verification state, reconciliation state, and memory admission reference. | `knowledge/concept-card-method/guides/templates/claim-source-support.md` | `knowledge/concept-card-method/guides/examples/claim-backed-card.md` | `knowledge/concept-card-method/guides/03-extraction.md` | `knowledge/concept-card-method/guides/validation/semantic-review-boundary.md` |
| source support | Claim-source attachment record linking claim id to one or more source span records, with source-support status, evidence grade, extraction confidence, and provenance. | `knowledge/concept-card-method/guides/templates/claim-source-support.md` | `knowledge/concept-card-method/guides/examples/claim-backed-card.md` | `knowledge/concept-card-method/guides/05-evidence-lifecycle.md` | `knowledge/concept-card-method/guides/validation/structural-candidates.md` |
| source span | Value object inside source support with source id, locator type, locator value, quote policy, source snapshot reference, and optional checksum or edition note. | `knowledge/concept-card-method/guides/templates/claim-source-support.md` | `knowledge/concept-card-method/guides/examples/claim-backed-card.md` | `knowledge/concept-card-method/guides/reference/source-locator-notes.md` | `knowledge/concept-card-method/guides/validation/structural-candidates.md` |
| source locator | Field group inside source span that records page, section, heading, paragraph, timestamp, URI fragment, line range, or other source-specific locator. | `knowledge/concept-card-method/guides/templates/claim-source-support.md` | `knowledge/concept-card-method/guides/examples/claim-backed-card.md` | `knowledge/concept-card-method/guides/reference/source-locator-notes.md` | `knowledge/concept-card-method/guides/validation/semantic-review-boundary.md` |
| relationship edge | Markdown record with edge id, relationship type, endpoints, endpoint roles, direction or symmetry, source support, evidence grade, verification state, reconciliation state, and run reference. | `knowledge/concept-card-method/guides/templates/relationship-edge.md` | `knowledge/concept-card-method/guides/examples/relationship-edge.md` | `knowledge/concept-card-method/guides/06-graph-cq.md` | `knowledge/concept-card-method/guides/validation/structural-candidates.md` |
| competency question | Markdown record with CQ id, question text, CQ status, requirement source, answerability, covered constructs, verification references, retrieval use, obsolete/deferred rationale, and memory implication. | `knowledge/concept-card-method/guides/templates/competency-question.md` | `knowledge/concept-card-method/guides/examples/cq-coverage.md` | `knowledge/concept-card-method/guides/06-graph-cq.md` | `knowledge/concept-card-method/guides/validation/semantic-review-boundary.md` |
| extraction run | Trace record with run id, source snapshot, method version, prompt version, agent scope, parallel-worker provenance, generated or updated output sets, old-card inputs, preservation decisions, validation result, reconciliation result, and verification result. | `knowledge/concept-card-method/guides/templates/extraction-run.md` | `knowledge/concept-card-method/guides/examples/extraction-run-trace.md` | `knowledge/concept-card-method/guides/04-re-extraction-preservation.md` | `knowledge/concept-card-method/guides/validation/structural-candidates.md` |
| validation result | Result record for structural validation checks, checked files, validator or checklist identity, outcome, findings, warnings, and limits. | `knowledge/concept-card-method/guides/templates/validation-result.md` | `knowledge/concept-card-method/guides/examples/extraction-run-trace.md` | `knowledge/concept-card-method/guides/08-validation-verification.md` | `knowledge/concept-card-method/guides/validation/structural-candidates.md` |
| verification result | Result record for semantic or human verification with verifier role, target constructs, evidence reviewed, outcome, rationale, caveats, and lifecycle effect. | `knowledge/concept-card-method/guides/templates/verification-result.md` | `knowledge/concept-card-method/guides/examples/claim-backed-card.md` | `knowledge/concept-card-method/guides/08-validation-verification.md` | `knowledge/concept-card-method/guides/validation/semantic-review-boundary.md` |
| reconciliation result | Result record for duplicate concepts, competing definitions, slug drift, taxonomy drift, relationship asymmetry, CQ coverage conflict, parallel-agent conflict, or preservation conflict. | `knowledge/concept-card-method/guides/templates/reconciliation-result.md` | `knowledge/concept-card-method/guides/examples/reconciliation.md` | `knowledge/concept-card-method/guides/07-reconciliation.md` | `knowledge/concept-card-method/guides/validation/semantic-review-boundary.md` |
| preservation decision | Result record for keep, revise, retire, merge, split, or defer decisions over old-card value, with rationale and lifecycle effect. | `knowledge/concept-card-method/guides/templates/preservation-decision.md` | `knowledge/concept-card-method/guides/examples/reconciliation.md` | `knowledge/concept-card-method/guides/04-re-extraction-preservation.md` | `knowledge/concept-card-method/guides/validation/human-review-boundary.md` |
| memory admission | Lifecycle result record stating whether future cognition may rely on a construct as durable semantic memory, based on support, grade, verification, validation, reconciliation, preservation, and operator acceptance. | `knowledge/concept-card-method/guides/templates/memory-admission.md` | `knowledge/concept-card-method/guides/examples/memory-admission.md` | `knowledge/concept-card-method/guides/09-memory-admission.md` | `knowledge/concept-card-method/guides/validation/human-review-boundary.md` |

## Required Field Groups

First implementation templates should use these field groups. Exact field
formatting belongs to the source templates, but the planned schema treatment
requires the groups below.

| Surface | Required field groups |
|---------|-----------------------|
| concept card | `id`, `title`, `concept_slug`, `method_version`, `card_status`, `source_refs`, `claim_refs`, `relationship_refs`, `cq_refs`, `run_refs`, `validation_refs`, `verification_refs`, `reconciliation_refs`, `memory_admission_ref`, and named body sections. |
| claim | `claim_id`, `statement`, `card_ref`, `source_support_refs`, `evidence_grade`, `extraction_confidence`, `verification_state`, `reconciliation_state`, `memory_admission_ref`, and rationale section. |
| source support | `support_id`, `claim_ref`, `source_span_refs`, `source_support_status`, `evidence_grade`, `extraction_confidence`, `verification_refs`, and notes. |
| source span | `span_id`, `source_ref`, `source_snapshot_ref`, `locator_type`, `locator_value`, `quote_policy`, and optional `checksum` or `edition_note`. |
| relationship edge | `edge_id`, `relationship_type`, `from_ref`, `to_ref`, `endpoint_roles`, `direction`, `symmetry`, `source_support_refs`, `evidence_grade`, `verification_state`, `reconciliation_state`, and `run_ref`. |
| competency question | `cq_id`, `question`, `cq_status`, `requirement_source`, `covered_refs`, `answerability_state`, `verification_refs`, `retrieval_probe_use`, and lifecycle rationale. |
| extraction run | `run_id`, `method_version`, `prompt_version`, `source_snapshot_refs`, `agent_scope`, `parallel_worker_count`, `worker_outputs`, `old_card_inputs`, `output_refs`, `validation_result_ref`, `reconciliation_result_ref`, and `verification_result_ref`. |
| validation result | `validation_id`, `target_refs`, `validator_identity`, `check_scope`, `validation_result`, `findings`, `warnings`, `cannot_prove`, and `created_at`. |
| verification result | `verification_id`, `verifier_role`, `target_refs`, `evidence_refs`, `verification_state`, `outcome`, `rationale`, `caveats`, and `created_at`. |
| reconciliation result | `reconciliation_id`, `conflict_class`, `affected_refs`, `decision`, `rationale`, `source_support_refs`, `lifecycle_effect`, `reconciler_role`, and `memory_admission_implication`. |
| preservation decision | `preservation_id`, `old_card_ref`, `new_ref`, `preservation_decision`, `unique_value_summary`, `rationale`, `lifecycle_effect`, and `operator_review_required`. |
| memory admission | `admission_id`, `target_refs`, `memory_admission`, `support_summary`, `evidence_grade_summary`, `verification_state_summary`, `validation_result_ref`, `reconciliation_state_summary`, `preservation_summary`, `operator_acceptance`, and `rationale`. |

## Continuity Constraints

- Arc03 conceptual model continuity: concept card, claim, source support,
  source span, source locator, relationship edge, competency question,
  extraction run, validation result, verification result, reconciliation
  result, preservation decision, and memory admission remain distinct.
- Arc04 skill architecture continuity: templates stay split into
  user-authored, trace record, and result record surface classes.
- Slice02 source layout continuity: all planned paths stay under
  `knowledge/concept-card-method/`, with templates under `guides/templates`,
  examples under `guides/examples`, validation documentation under
  `guides/validation`, and support documents under `guides/reference`.

## Later-Slice Routing

- Slice04 owns README, library discoverability, Makefile package target
  names, package list edits, package-path exception rows, package-path checks,
  generated zip policy, release gate details, package release boundaries, and
  source version history text.
- Slice05 owns implementation-plan synthesis and Project03 close input.

Slice03 found no schema-surface fact that requires Arc05 re-sequencing, a new
slice, or a scope correction.
