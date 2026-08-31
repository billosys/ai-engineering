# v4.0 Validation and Review Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice03-schema-validation-plan
artifact: v40-validation-review-plan
status: proposed-done
```

## Purpose

This artifact separates deterministic structural validation, semantic audit,
human/operator review, and deferred runtime checks. It states what each
evidence class can prove and cannot prove for the v4.0 concept-card method.

This is planning only. It does not edit source, does not implement
validator-code, does not implement tests, does not create generated zips, does
not perform package release, does not claim release readiness, and does not
create runtime services, GraphRAG, graph database, ontology database, memory
runtime, CCDP service, or live extraction behavior.

## Evidence Classes

| Evidence class | Can prove | Cannot prove | Planned documentation path |
|----------------|-----------|--------------|----------------------------|
| deterministic structural validation | Required files exist; YAML frontmatter parses; required fields are present; enum values match controlled vocabulary; required sections exist; local references use expected id shapes; path/slug hygiene is acceptable; obvious missing source support or CQ coverage references are detected. | Source support warrant, evidence grade adequacy, extraction confidence calibration, relationship meaning, CQ answerability, reconciliation rationale, preservation rationale, memory admission judgment, or operator acceptance. | `knowledge/concept-card-method/guides/validation/structural-candidates.md` |
| semantic audit | Source support actually warrants claims; evidence grade is adequate; extraction confidence matches source difficulty; relationship semantics are appropriate; CQ answerability is justified; reconciliation rationale is coherent; preservation rationale is source-faithful. | Deterministic completeness by itself, operator policy acceptance, package-path correctness, generated archive validity, runtime behavior, or memory runtime enforcement. | `knowledge/concept-card-method/guides/validation/semantic-review-boundary.md` |
| human/operator review | Memory admission approval, conflict disposition, preservation exceptions, material uncertainty calls, and project-specific acceptance decisions. | Automated structural correctness, package target correctness, generated zip behavior, graph database closure, GraphRAG retrieval quality, ontology database consistency, CCDP service behavior, or live extraction safety. | `knowledge/concept-card-method/guides/validation/human-review-boundary.md` |
| deferred runtime checks | Future checks may prove graph database closure, GraphRAG retrieval probes, ontology database checks, memory runtime enforcement, CCDP service orchestration, or live extraction behavior if a later owner implements those systems. | Anything in the first implementation plan unless explicitly accepted later; these checks cannot be claimed by documentary guidance alone. | `knowledge/concept-card-method/guides/validation/deferred-runtime-checks.md` |

## Deterministic Structural Validation Candidates

Accepted Slice03 candidates for documentation:

- concept card has one concept boundary, required frontmatter, required
  sections, source references, claim references, lifecycle/result references,
  and stable id/slug shape.
- claim has statement, card reference, source support reference, evidence
  grade, extraction confidence, verification state, reconciliation state, and
  optional memory admission reference.
- source support has source-support status, source span references, claim
  reference, and source snapshot reference.
- source span has source locator fields, source reference, and source snapshot
  reference.
- relationship edge has edge id, relationship type, endpoints, endpoint roles,
  direction or symmetry fields, and source support where needed.
- competency question has CQ status, question text, covered references,
  answerability state, and lifecycle rationale.
- extraction run has source snapshot, method version, prompt version, agent
  scope, parallel-worker provenance, output set, and result references.
- validation result, verification result, reconciliation result, preservation
  decision, and memory admission records have target references, outcome,
  rationale or findings, and created-at metadata.
- enum values match the Slice03 enum vocabulary plan.
- local references use declared id prefixes or reference forms.
- required examples can be parsed against the planned documentation-only
  structure when executable checks are introduced later.

## Semantic Audit Boundary

Semantic audit is source-aware review. It is required when a check depends on
meaning, warrant, or interpretation. It can review source support, evidence
grade, extraction confidence, relationship meaning, CQ answerability,
reconciliation rationale, preservation rationale, and memory-admission
readiness.

Semantic audit cannot be replaced by deterministic validation. A structurally
valid card can still be wrong, weakly supported, unreconciled, or not admitted
to memory.

## Human/Operator Review Boundary

Human/operator review is required for policy, judgment, and acceptance
decisions. It covers memory admission approval, conflict disposition,
preservation exceptions, material uncertainty, and any project-specific
override.

Human/operator review cannot prove that automated package checks passed, that
generated archives are valid, or that runtime services exist. Those remain
outside Slice03 and belong to Slice04 or later implementation owners.

## Deferred Runtime Checks

Deferred runtime checks include GraphRAG retrieval probes, graph database
closure, ontology database checks, memory runtime enforcement, CCDP service
orchestration, and live extraction behavior.

These are not first-implementation validation promises. They may become
future implementation or release gates only if a later owner accepts them.

## Later-Slice Routing

- Slice04 owns README, library discoverability, Makefile package target
  names, package list edits, package-path exception rows, package-path checks,
  generated zip policy, release gate details, package release boundaries, and
  source version history.
- Slice05 owns implementation-plan synthesis and Project03 close input.

Slice03 found no validation or review-boundary fact that requires Arc05
re-sequencing, a new slice, or a scope correction.
