# v4.0 Evidence and Lifecycle Model

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice02-evidence-lifecycle
status: proposed-done
inputs:
  - ../slice01-construct-boundaries/cdc-verification.md
  - ../slice01-construct-boundaries/artifacts/v40-construct-boundary-model.md
  - ../slice01-construct-boundaries/artifacts/v40-construct-decision-register.md
  - ../../arc02-method-inventory/closing-report.md
  - ../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc02-synthesis.md
  - ../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md
mode: evidence-lifecycle model
v4-design-stage: provisional
```

## Purpose

This model defines the v4.0 evidence and lifecycle semantics needed to avoid
the v3.2 failure mode where source explicitness, extractor certainty,
verification, reconciliation, and memory readiness collapse into one
confidence signal.

The model preserves v3.2 carry-forward strengths: source-faithful synthesis,
provenance, confidence signalling, validation checks, source-primary
re-extraction, and preservation of unique prior-card value. The v4.0 change is
that these strengths become distinct lifecycle concerns rather than one
overloaded field.

## Core Separation

The lifecycle uses distinct concepts, not one confidence field:

- extraction confidence: the extractor's judgment about how direct or
  difficult the extraction was.
- source support: the source span or source material that supports a claim.
- evidence grade: the warrant level assigned to a claim or claim-source
  support relationship.
- verification state: the current state of independent checking.
- verification result: the result record produced by a verifier.
- reconciliation state: whether conflict review is pending, complete, or not
  applicable.
- reconciliation result: the result record produced by reconciliation.
- memory admission: the lifecycle gate that says whether future cognition may
  rely on the card or claim as durable semantic memory.

These concepts are related, but they are distinct. A claim can have high
extraction confidence and weak source support. A claim can have strong source
support but no verification result. A card can be structurally valid but not
memory admitted. A reconciliation result can change relationship or edge
confidence without changing the original source span.

## Attachment Points

Each concern attaches to a specific model object or lifecycle gate; none of
these status concerns should attach only to the card as a catch-all field.

| Concern | Meaning | Must not be confused with | Primary attachment point | Notes |
|---------|---------|---------------------------|--------------------------|-------|
| extraction confidence | Extractor's confidence in the extraction act. | Evidence grade, source support, verification state, or memory admission. | claim, concept card, extraction run | Preserves v3.2 confidence signalling while narrowing what it means. |
| source support | The source span or source material supporting a claim. | Bibliographic provenance alone or verifier approval. | claim-source support relationship | May reference source span as value object or first-class entity, as Slice04 later settles. |
| evidence grade | Warrant level for supported content. | Extraction confidence or verification state. | claim-source support relationship, claim | Exact evidence-grade vocabulary is deferred. |
| verification state | Lifecycle state of independent checking. | The verification result record itself. | claim, concept card, claim-source support relationship | Tracks whether checking is absent, pending, accepted, failed, or superseded without final enum spelling. |
| verification result | Durable record of a verifier's check. | Verifier role or evidence grade. | result record attached to claim, card, support relationship, or extraction run | Records who or what checked, what was checked, and the outcome. |
| reconciliation state | Lifecycle state of conflict review. | Reconciliation algorithm or graph semantics. | claim, concept card, relationship/edge, extraction run | The state exists here; detailed graph/CQ/run semantics are Slice03 work. |
| reconciliation result | Durable record of conflict resolution. | Verification result or memory admission. | result record attached to affected claims, cards, relationships, or runs | Captures duplicate, drift, conflict, or merge decisions without defining algorithms. |
| memory admission | Permission state for durable semantic memory use. | Validation, evidence grade, verification state, or reconciliation state. | lifecycle gate on concept card and possibly claim | Requires sufficient evidence, verification, reconciliation disposition, and operator or human acceptance where policy requires it. |

## Candidate Lifecycle Flow

1. Extracted candidate: a concept card or claim is created from source-primary
   extraction. It can carry extraction confidence and source support, but it is
   not yet verified or memory admitted.
2. Structurally checked: v3.2 validation checks are applied for required
   fields, body sections, provenance, path/slug hygiene, and obvious
   consistency. This may advance a card toward review, but not into durable
   semantic memory by itself.
3. Source-supported: each claim has an identified source span or source
   support relationship. Evidence grade can be assigned provisionally, but
   exact evidence-grade vocabulary remains deferred.
4. Verification pending or complete: a verifier checks the claim, card,
   support relationship, or run and emits a verification result. The
   verification state records whether the check is pending, passed, failed,
   superseded, or requires operator review, without final enum spelling.
5. Reconciliation pending or complete: conflicts across duplicate concepts,
   competing definitions, slug/taxonomy drift, relationship asymmetry, or
   parallel-agent output are routed to reconciliation. Reconciliation result
   is reserved here as an attachment point; reconciliation algorithms and
   graph-native semantics remain Slice03 work.
6. Admission decision: memory admission is evaluated after source support,
   verification, and reconciliation disposition are sufficient. Human/operator
   acceptance can be required for high-impact or uncertain content. A validated
   card that lacks the admission gate remains useful artifact content, but not
   durable semantic memory that future cognition should lean on.
7. Durable semantic memory candidate: admitted content becomes eligible for
   later skill, package, or memory-substrate planning. This slice does not
   implement storage, runtime memory, or package behavior.

## Advancement Rules

- Extracted content may advance to structural checking with only extraction
  confidence and source support.
- A concept card or claim may be reviewed before reconciliation when no known
  conflict exists, but memory admission must wait for reconciliation state to
  be complete or explicitly not applicable.
- Evidence grade can be provisional before verification, but an admitted card
  or claim must record verification state and any required verification result.
- A failed verification result blocks memory admission until corrected,
  superseded, or explicitly deferred with operator acceptance.
- Human/operator acceptance is required where the method policy marks evidence
  as insufficient, high-impact, or dependent on judgment.

## Preservation Commitments

v3.2 confidence signalling is retained, but narrowed to extraction confidence.
v3.2 provenance is retained and strengthened through source support. v3.2
validation checks remain useful structural gates. v3.2 source-primary
re-extraction and preservation of unique prior-card value remain lifecycle
constraints: old-card value can be preserved, rejected, or marked unresolved,
but it cannot disappear silently.

## Out of scope

Out of scope for this slice: final schema syntax, enum spelling, YAML template
shape, validator implementation, deterministic scripts, skill architecture,
package behavior, README integration, Makefile changes, generated zips, source
edits, relationship or edge semantics, competency-question semantics,
extraction-run trace schema, reconciliation algorithms, GraphRAG runtime,
memory runtime, ontology database, and CCDP service design.

This model only reserves attachment points needed by the evidence lifecycle.
Slice03 owns graph/CQ/run semantics. Slice04 owns final model synthesis. Arc04
owns skill architecture. Arc05 owns implementation planning.
