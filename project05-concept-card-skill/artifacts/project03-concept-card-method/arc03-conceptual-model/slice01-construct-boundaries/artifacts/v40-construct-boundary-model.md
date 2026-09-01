# v4.0 Construct Boundary Model

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice01-construct-boundaries
status: proposed-done
inputs:
  - ../../arc02-method-inventory/closing-report.md
  - ../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc02-synthesis.md
  - ../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md
  - ../../arc02-method-inventory/slice02-v40-gap-analysis/artifacts/v40-gap-register.md
  - ../../arc02-method-inventory/slice02-v40-gap-analysis/artifacts/v32-to-v40-carry-forward-change-matrix.md
mode: construct-boundary model
v4-design-stage: provisional
```

## Purpose

This construct-boundary pass turns Arc02's candidate construct list into the
first bounded v4.0 conceptual model layer. It decides which ideas are method
constructs now, which are subordinate fields, statuses, roles, processes, or
result records, and which remain deferred concerns for later Arc03 slices or
later arcs.

This is not an implementation design. It preserves the v3.2 carry forward
commitments: card atomicity, source-faithful synthesis, provenance, typed
relationships, competency questions, source-primary re-extraction, and
preservation. The v4.0 conceptual model changes are expressed as method-model
boundaries, not schema syntax, file layout, scripts, package behavior, or
source edits.

## Boundary Vocabulary

- first-class entity: a durable model object with identity and lifecycle.
- value object: a structured value attached to an entity, without independent
  lifecycle.
- status: a controlled state or grade that records position in a lifecycle.
- role: an actor or authority category in the method.
- process: a named workflow activity, not itself durable content.
- result record: durable evidence that a process or role reached an outcome.
- field: a card-local value retained from v3.2 or added later by design.
- deferred concern: a boundary that belongs to a later slice or arc.

## Construct Boundaries

### concept card

Classification: first-class entity, accepted.

Boundary: the concept card remains the central durable method unit. It carries
the one-concept atomicity rule forward from v3.2 while becoming a container for
more explicit claims, source spans, evidence, relationships, competency
questions, run references, verification results, reconciliation results, and
memory admission status where later slices accept those details.

Provisional area: Slice04 must decide the final whole-model wording after
Slice02 and Slice03 settle evidence/lifecycle and graph/CQ/run semantics.

### claim

Classification: first-class entity, provisional.

Boundary: claim is a model construct because v4.0 must separate what the card
says from the card container itself. A claim may carry or reference source
span, extraction confidence, evidence grade, verification result,
reconciliation result, and memory admission status.

Provisional area: Slice02 must decide how claims relate to evidence grade,
verification state, and memory admission. Slice04 must decide whether claims
are always explicit or can be implicit inside simple cards.

### source span

Classification: value object or first-class entity, provisional.

Boundary: source span names the source-backed support for a claim or card. It
is separate from bibliographic provenance, because v3.2 provenance identifies
source material while v4.0 needs support granularity.

Provisional area: Slice02 must decide whether source span identity is required
for evidence and verification. Slice04 must decide final cardinality between
cards, claims, and spans.

### evidence grade

Classification: status, provisional.

Boundary: evidence grade is a method status about warrant, not the same thing
as extraction confidence. It should attach to the claim or claim-source-span
support relationship after Slice02 decides the lifecycle semantics.

Provisional area: Slice02 must resolve the evidence-grade vocabulary and how
it relates to verification state, reconciliation state, and memory admission.

### relationship or edge

Classification: first-class entity, provisional, with v3.2 fields carried
forward.

Boundary: v3.2 typed relationships remain useful fields, but v4.0 needs a
relationship or edge construct when graph semantics require identity,
evidence, status, inverse policy, reconciliation, or graph closure.

Provisional area: Slice03 must define relationship/edge semantics and decide
which v3.2 relationship fields stay card-local versus become graph-native
edges.

### competency question

Classification: first-class entity and coverage status, accepted/provisional.

Boundary: competency question is accepted as a method construct because v3.2
already uses competency questions for requirements, mapping, card linkage, and
coverage checks. Its identity is accepted; its statuses remain provisional.

Provisional area: Slice03 must define CQ coverage, answerability, verification,
obsolete, and deferred status semantics.

### extraction run

Classification: first-class entity, provisional.

Boundary: extraction run is a trace construct for source snapshot, prompt
version, agent scope, generated card set, old-card inputs, preservation
decisions, validation result, and reconciliation result. It is the unit that
makes multi-agent extraction auditable.

Provisional area: Slice03 must decide minimum traceability semantics. Arc04
and Arc05 later decide files, templates, scripts, and implementation details.

### verifier

Classification: role, provisional, with result record dependency.

Boundary: verifier is a method role because v4.0 separates extractor confidence
from independent checking. The durable model object is likely a verification
result record rather than the role itself.

Provisional area: Slice02 must decide verification-state transitions and what
counts as reproduced evidence. Slice04 must decide final model wording.

### reconciliation

Classification: process and result record, provisional.

Boundary: reconciliation is a process for resolving duplicate concepts,
competing definitions, slug drift, taxonomy drift, relationship asymmetry, and
parallel-agent conflict. Its durable output should be a reconciliation result
record attached to affected cards, claims, relationships, or runs.

Provisional area: Slice03 must define reconciliation semantics across graph,
CQ, and run concerns. Reconciliation algorithms remain out of scope.

### memory admission

Classification: status or result record, provisional.

Boundary: memory admission records whether extracted content may be used as
durable semantic memory. It is distinct from validation, evidence grade,
verification state, and reconciliation state.

Provisional area: Slice02 must define memory-admission policy boundaries and
state relationships. Slice04 must compose the accepted model without turning
the policy into implementation mechanics.

## Deferred Concerns

Out of scope for this slice: evidence-grade vocabulary, verification-state
transitions, reconciliation algorithms, memory-admission policy, schema syntax,
skill layout, package behavior, deterministic validator scripts, README
changes, Makefile changes, and source edits.

Packaging and source structure are Arc04/Arc05 concerns. This boundary model
does not choose guide files, templates, package inclusion, Make targets,
validator language, or source file locations.

## Routing

- Slice02 should resolve evidence and lifecycle semantics for claim, source
  span, evidence grade, verifier, verification result, reconciliation state,
  and memory admission.
- Slice03 should resolve graph-native relationship or edge semantics,
  competency question status, extraction run traceability, and reconciliation
  result semantics across runs and graph edges.
- Slice04 should compose the provisional boundaries into an accepted v4.0
  conceptual model and record any remaining operator decisions.
