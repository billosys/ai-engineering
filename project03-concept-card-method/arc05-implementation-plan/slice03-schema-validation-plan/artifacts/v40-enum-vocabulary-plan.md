# v4.0 Enum Vocabulary Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice03-schema-validation-plan
artifact: v40-enum-vocabulary-plan
status: proposed-done
enum-style: lowercase snake_case
```

## Purpose

This artifact names the controlled vocabulary and enum spelling for the first
implementation plan. It preserves accepted Arc03 lifecycle distinctions,
accepted Arc04 skill architecture, and the Slice02 source layout/content
sequence.

This is planning only. It does not edit source, does not implement source
schema files, does not create generated zips, does not perform package
release, does not claim release readiness, and does not create runtime
services, GraphRAG, graph database, ontology database, memory runtime, CCDP
service, or live extraction behavior.

## Vocabulary Style

Accepted Slice03 decision: v4.0 controlled vocabulary should use lowercase
snake_case enum spelling.

Rationale:

- It matches existing Markdown/YAML frontmatter conventions.
- It is easy to grep and validate deterministically.
- It avoids display-label drift between templates, examples, validation
  documentation, and source records.

## Controlled Vocabulary

| Field | Enum values | Owner |
|-------|-------------|-------|
| evidence grade | `direct`, `supported`, `inferred`, `synthesis`, `contested`, `unsupported`, `unknown` | Slice03 |
| extraction confidence | `high`, `medium`, `low`, `ambiguous`, `not_assessed` | Slice03 |
| verification state | `unverified`, `verified`, `rejected`, `needs_review`, `deferred`, `not_applicable` | Slice03 |
| validation result | `not_run`, `passed`, `passed_with_warnings`, `failed`, `blocked`, `not_applicable` | Slice03 |
| reconciliation state | `not_needed`, `unreconciled`, `reconciled`, `conflict_open`, `deferred`, `not_applicable` | Slice03 |
| CQ status | `proposed`, `active`, `covered`, `answerable`, `not_answerable`, `obsolete`, `deferred` | Slice03 |
| preservation decision | `keep`, `revise`, `retire`, `merge`, `split`, `defer`, `not_applicable` | Slice03 |
| memory admission | `not_evaluated`, `admitted`, `rejected`, `deferred`, `not_applicable`, `operator_required` | Slice03 |
| source-support status | `present`, `partial`, `missing`, `ambiguous`, `conflicting`, `not_applicable` | Slice03 |
| relationship type | `prerequisites`, `extends`, `related`, `contrasts_with` | Arc03 preserved by Slice03 |
| direction | `directed`, `symmetric`, `inverse_documented`, `not_applicable` | Slice03 |
| verifier role | `human`, `model`, `tool`, `process`, `operator`, `cdc`, `unknown` | Slice03 |
| conflict class | `duplicate_concept`, `competing_definition`, `slug_drift`, `taxonomy_drift`, `relationship_asymmetry`, `cq_coverage_conflict`, `parallel_agent_conflict`, `preservation_conflict`, `source_conflict`, `other` | Slice03 |
| review requirement | `required`, `optional`, `not_required`, `blocked`, `not_applicable` | Slice03 |
| lifecycle effect | `none`, `update_target`, `mark_verified`, `mark_rejected`, `mark_reconciled`, `mark_deferred`, `requires_operator`, `blocks_memory_admission` | Slice03 |

## Field Guidance

Evidence grade describes warrant, not extractor certainty. Extraction
confidence describes the extraction act, not source support. Verification
state records review outcome or pending state, while validation result records
structural check outcome. Reconciliation state records conflict disposition,
and memory admission records whether future cognition may rely on the target
as durable semantic memory.

`source-support status` is separate from evidence grade. A claim can have
`source-support status: present` and still have `evidence grade: contested` if
the source supports the claim but another source disputes it. A claim can also
have `source-support status: partial` and `evidence grade: inferred` when only
part of the claim is directly supported.

Relationship type preserves the accepted Arc03 vocabulary:
`prerequisites`, `extends`, `related`, and `contrasts_with`. `prerequisites`
and `extends` are directional. `related` and `contrasts_with` are symmetric
unless a later accepted model change creates a directed subtype.

## Template and Example Application

The enum vocabulary applies to these planned Slice02 paths:

- `knowledge/concept-card-method/guides/templates/concept-card.md`
- `knowledge/concept-card-method/guides/templates/claim-source-support.md`
- `knowledge/concept-card-method/guides/templates/competency-question.md`
- `knowledge/concept-card-method/guides/templates/relationship-edge.md`
- `knowledge/concept-card-method/guides/templates/extraction-run.md`
- `knowledge/concept-card-method/guides/templates/validation-result.md`
- `knowledge/concept-card-method/guides/templates/verification-result.md`
- `knowledge/concept-card-method/guides/templates/reconciliation-result.md`
- `knowledge/concept-card-method/guides/templates/preservation-decision.md`
- `knowledge/concept-card-method/guides/templates/memory-admission.md`
- `knowledge/concept-card-method/guides/examples/minimal-card.md`
- `knowledge/concept-card-method/guides/examples/claim-backed-card.md`
- `knowledge/concept-card-method/guides/examples/cq-coverage.md`
- `knowledge/concept-card-method/guides/examples/relationship-edge.md`
- `knowledge/concept-card-method/guides/examples/extraction-run-trace.md`
- `knowledge/concept-card-method/guides/examples/reconciliation.md`
- `knowledge/concept-card-method/guides/examples/memory-admission.md`
- `knowledge/concept-card-method/guides/examples/five-agent-default-recipe.md`

## Later-Slice Routing

- Slice04 owns README, library discoverability, Makefile package target
  names, package list edits, package-path exception rows, package-path checks,
  generated zip policy, release gate details, package release boundaries, and
  source version history.
- Slice05 owns implementation-plan synthesis and Project03 close input.

Slice03 found no enum-vocabulary fact that requires Arc05 re-sequencing, a new
slice, or a scope correction.
