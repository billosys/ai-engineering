# v4.0 Conceptual Model

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice04-model-synthesis
status: accepted
inputs:
  - ../slice01-construct-boundaries/artifacts/v40-construct-boundary-model.md
  - ../slice01-construct-boundaries/artifacts/v40-construct-decision-register.md
  - ../slice01-construct-boundaries/cdc-verification.md
  - ../slice02-evidence-lifecycle/artifacts/v40-evidence-lifecycle-model.md
  - ../slice02-evidence-lifecycle/artifacts/v40-evidence-state-decision-register.md
  - ../slice02-evidence-lifecycle/cdc-verification.md
  - ../slice03-graph-cq-run-semantics/artifacts/v40-graph-cq-run-semantics.md
  - ../slice03-graph-cq-run-semantics/artifacts/v40-reconciliation-traceability-decision-register.md
  - ../slice03-graph-cq-run-semantics/cdc-verification.md
  - ../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md
  - ../../arc02-method-inventory/closing-report.md
mode: Arc03 accepted conceptual model
```

## Purpose

This is the accepted v4.0 conceptual model for the concept-card method at the
end of Arc03. It composes the verified Slice01 construct boundaries, Slice02
evidence lifecycle, and Slice03 graph/CQ/run semantics into one method model.

The model defines concepts and attachment points only. It does not choose final
skill layout, package behavior, README integration, Makefile changes,
generated zips, schema syntax, exact enum spelling, validator implementation,
GraphRAG runtime, memory runtime, ontology database, CCDP service design, live
extraction behavior, or source edits.

## Core Invariants

- one concept, one card: a concept card remains the atomic durable unit of the
  method. The card may contain or reference finer-grained claims, source spans,
  relationship edges, competency questions, run records, result records, and
  memory admission state, but its organizing boundary is still one concept.
- source-faithful synthesis: cards and claims summarize source material rather
  than copying prose or introducing unsupported inference.
- provenance is required: every card, claim, edge, CQ coverage assertion, and
  extraction run must preserve enough provenance to recover its source basis.
- no hidden flattening: extraction confidence, source support, evidence grade,
  verification state, verification result, reconciliation state,
  reconciliation result, validation result, and memory admission are distinct
  model concerns, not one confidence field.
- result records carry outcomes: verification, validation, reconciliation, and
  preservation outcomes are recorded as result records or explicitly attached
  lifecycle state, not buried in prose.
- preservation is explicit: unique prior-card value can be preserved,
  superseded, rejected, or left unresolved, but it cannot disappear silently.
- memory admission is gated: validated content is not automatically durable
  semantic memory. Admission depends on source support, evidence grade,
  verification state, reconciliation state, and any required human/operator
  acceptance.

## Model Constructs

### concept card

Accepted first-class entity. A concept card is the durable container for a
single concept. It carries the v3.2 atomicity rule forward while gaining
explicit attachment points for claims, source support, relationships/edges,
competency questions, extraction runs, verification results, validation
results, reconciliation results, preservation decisions, and memory admission.

### claim

Accepted first-class entity. A claim is a substantive assertion made by or
for a concept card. A card can be a curated summary over one or more claims.
Simple cards may still present claims in prose, but v4.0 conceptually treats
claims as the unit that can carry source support, extraction confidence,
evidence grade, verification state, reconciliation state, and memory admission
where granularity matters.

### source span and source support

Source span is an accepted value object with provisional identity. A source
span names the source locator that supports a claim, card, edge, or CQ
coverage assertion. Source support is the claim-source attachment point that
connects a claim to one or more source spans.

Source support is distinct from bibliographic provenance. Provenance identifies
source material and extraction context; source support states which source
span supports which claim or edge.

### evidence grade and extraction confidence

Evidence grade is a provisional status on a claim or claim-source support
relationship. It describes warrant, not extractor certainty. The final grade
vocabulary and exact enum spelling are deferred.

Extraction confidence is an accepted separate signal about the extraction act:
how direct, ambiguous, or difficult the extraction was from the source. It may
attach to a claim, card, or extraction run. It must not substitute for source
support, evidence grade, verification state, reconciliation state, or memory
admission.

### relationship and graph-native edge

Relationship vocabulary carries forward from v3.2: `prerequisites`, `extends`,
`related`, and `contrasts_with`. These may remain card-local authoring fields
where they are simple navigation aids.

A graph-native edge is required when a relationship needs independent
identity: evidence, source support, verification state/result, reconciliation
state/result, extraction-run provenance, preservation decision, graph closure
state, or conflict handling. Endpoints can be cards, claims, CQs, or other
accepted model constructs when the relationship is about coverage or support.

`prerequisites` and `extends` are directional. `related` and `contrasts_with`
are symmetric unless later model or architecture work introduces a directed
subtype. Direction, inverse reading, endpoint roles, and symmetry expectations
belong to the conceptual model; graph database implementation does not.

### competency question and CQ coverage

Competency question is an accepted first-class entity. CQ coverage is the
attachment point between a CQ and the cards, claims, source support, or edges
that answer it.

A CQ may act as a requirement, answerability check, coverage target,
verification target, retrieval probe, obsolete record, or deferred question.
Answerability is distinct from coverage: a CQ can be covered by a card but not
answerable if the underlying claim lacks source support, verification, or
memory admission. Retrieval use does not imply memory admission.

### extraction run

Extraction run is an accepted first-class trace entity. It records the source
snapshot, method version or prompt version, agent scope, parallel-worker
provenance, generated or updated card set, generated or updated claims,
generated or updated edges, generated or updated CQs, old-card inputs,
preservation decisions, validation result, reconciliation result, and
downstream memory-admission implications.

The run is the common provenance anchor for source-primary extraction,
parallel re-extraction, validation, preservation, reconciliation, and later
verification. It is not a script or runtime execution design.

### verifier role and verification result/state

Verifier is an accepted role. The verifier may be human, model, process, or
tool in later implementation, but the conceptual model only needs the role and
its result provenance.

Verification state is a provisional lifecycle status on a claim, card,
claim-source support relationship, edge, CQ coverage assertion, or extraction
run. Verification result is an accepted result record that states who or what
checked the construct, what was checked, what evidence was used, and what
outcome was reached.

### validation result

Validation result is an accepted result record for structural checks:
required fields, body sections, provenance, source support, relationship
references, CQ coverage, path/slug hygiene, and obvious consistency. It is
separate from semantic verification, reconciliation, and memory admission.

### reconciliation state/result

Reconciliation is an accepted process with accepted result records and
provisional state vocabulary. Reconciliation state attaches to affected
cards, claims, edges, CQs, and extraction runs. Reconciliation result records
cover duplicate concepts, competing definitions, slug drift, taxonomy drift,
relationship asymmetry, CQ coverage conflict, parallel-agent conflict, and
preservation conflict.

The result record names affected constructs, conflict class, source support,
decision, rationale, lifecycle effect, verifier or reconciler role, and memory
admission implication. Reconciliation algorithms are out of scope.

### memory admission state

Memory admission state is a provisional lifecycle gate on cards and possibly
claims, edges, and CQs. It states whether future cognition may rely on the
construct as durable semantic memory.

Admission depends on sufficient source support, evidence grade, verification
state/result, reconciliation state/result, validation result, preservation
disposition, and any required human/operator acceptance. A validated card that
lacks memory admission remains useful artifact content but not admitted
semantic memory.

## Lifecycle Flow

1. Source snapshot selected: the run records source material, old-card inputs,
   prompt or method version, and agent scope.
2. Extraction performed: candidate concept cards, claims, edges, and CQs are
   created with extraction confidence and provenance.
3. Source support attached: claims, edges, and CQ coverage assertions attach to
   source spans through explicit claim-source or edge-source support.
4. Structural validation run: a validation result records required structure,
   provenance, relationship references, CQ coverage, and consistency checks.
5. Preservation reviewed: old-card value is preserved, superseded, rejected,
   or marked unresolved with rationale.
6. Reconciliation run: conflicts across cards, claims, relationships, CQs,
   runs, slugs, taxonomy, and parallel-worker output are resolved or deferred
   through reconciliation result records.
7. Verification run: a verifier checks claims, cards, support relationships,
   edges, CQs, or runs and records verification result/state.
8. Memory admission decided: eligible constructs are admitted, rejected,
   deferred, or marked not applicable based on lifecycle evidence.

## Attachment Points

- Card-level: concept boundary, summary prose, card provenance, card-level
  extraction confidence, validation result, reconciliation state, memory
  admission, and run references.
- Claim-level: source support, source span, extraction confidence, evidence
  grade, verification state/result, reconciliation state/result, memory
  admission, and preservation decisions.
- Claim-source support relationship: source span attachment point, evidence
  grade, verification result, validation result, and provenance.
- Edge-level: endpoints, endpoint roles, direction, inverse/symmetry
  expectation, source support, evidence grade, graph closure state,
  verification state/result, reconciliation state/result, extraction run, and
  memory admission implication.
- CQ-level: requirement source, answerability, coverage, verification,
  retrieval, obsolete or deferred status, covered cards/claims/edges, and
  result records.
- Extraction-run level: source snapshot, method or prompt version, agent
  scope, parallel-worker provenance, output set, old-card inputs,
  preservation decisions, validation result, reconciliation result, and
  verification result.

## Preservation Rules for v3.2 Carry-Forward

The v4.0 model preserves v3.2 atomic cards, source-faithful synthesis,
provenance, typed relationship fields, competency questions, validation,
source-primary re-extraction, parallel-worker coordination, old-card
preservation, and verification notes.

The model changes v3.2 where distinct concerns were implicit or overloaded.
`extraction_confidence` carries forward only as extraction confidence. Evidence
grade, source support, verification state, reconciliation state, validation
result, and memory admission become separate attachment points. Relationship
fields carry forward as method vocabulary, while graph-native edge identity is
introduced when evidence, lifecycle state, provenance, or reconciliation needs
to attach to the relationship itself.

## Boundaries

Conceptual model work ends here: constructs, statuses, result records,
attachment points, invariants, lifecycle flow, and preservation rules.

Skill architecture begins in Arc04: final SKILL.md role, guide split,
template set, validation script candidates, examples, package behavior,
README integration, and operator-facing workflow presentation.

Implementation planning begins in Arc05: source edits, Makefile/package
changes, schema syntax, exact enum spelling, validator implementation,
generated zips, test gates, and release mechanics.

Out of scope for this model: final skill layout, package behavior, README
integration, Makefile changes, generated zips, schema syntax, exact enum
spelling, validator implementation, GraphRAG runtime, memory runtime, ontology
database, CCDP service design, live extraction, and source edits.
