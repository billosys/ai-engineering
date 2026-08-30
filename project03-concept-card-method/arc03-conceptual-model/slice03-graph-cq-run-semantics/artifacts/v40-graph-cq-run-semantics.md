# v4.0 Graph, CQ, and Run Semantics

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice03-graph-cq-run-semantics
status: proposed-done
inputs:
  - ../slice01-construct-boundaries/cdc-verification.md
  - ../slice01-construct-boundaries/artifacts/v40-construct-boundary-model.md
  - ../slice01-construct-boundaries/artifacts/v40-construct-decision-register.md
  - ../slice02-evidence-lifecycle/cdc-verification.md
  - ../slice02-evidence-lifecycle/artifacts/v40-evidence-lifecycle-model.md
  - ../slice02-evidence-lifecycle/artifacts/v40-evidence-state-decision-register.md
  - ../../arc02-method-inventory/closing-report.md
  - ../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc02-synthesis.md
  - ../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md
mode: graph-cq-run conceptual model
v4-design-stage: provisional
```

## Purpose

This model defines the v4.0 conceptual semantics for relationship or edge
constructs, competency question records, extraction run traceability, and
reconciliation result records. It extends the Slice01 construct boundaries and
the Slice02 evidence lifecycle attachment points without finalizing schema
syntax, exact enum spelling, YAML template shape, validator implementation,
skill architecture, package behavior, README integration, Makefile changes,
generated zips, or source edits.

The model preserves the v3.2 strengths that should carry forward:
`prerequisites`, `extends`, `related`, and `contrasts_with`; competency
question coverage; source-primary re-extraction; parallel-worker
coordination; validation; and preservation of unique prior-card value.

## Relationship and Edge Semantics

v3.2 relationship fields remain protected method vocabulary:

- `prerequisites`: directional dependency. If card A lists card B as a
  prerequisite, the edge direction is B -> A: B supports understanding A.
- `extends`: directional elaboration. If card A extends card B, the edge
  direction is A -> B for "extends", with B -> A available as the inverse
  reading "is extended by".
- `related`: symmetric association. Either endpoint can name the edge, but a
  graph-native representation should not duplicate contradictory copies.
- `contrasts_with`: symmetric comparison or distinction. Either endpoint can
  name the edge, and the method should preserve the reason for contrast.

Card-local fields may remain useful as authoring affordances, but v4.0 needs a
first-class relationship or edge when the relationship has evidence,
verification state, reconciliation state, lifecycle history, a preservation
decision, or a conflict that must survive outside one card.

### Endpoints

An edge connects typed endpoints. The minimum conceptual endpoint is a concept
card. A more precise edge may connect a card to a claim, claim to claim, card
to competency question, or competency question to claim when the relationship
is about coverage or answerability rather than general conceptual relatedness.

Endpoint semantics:

- Each endpoint must identify the target construct and its role on the edge.
- Directional edges distinguish source endpoint from target endpoint.
- Symmetric edges still record two endpoints, but they do not assign semantic
  priority to one side.
- Edge evidence attaches to the edge or to the claim-source support
  relationship that justifies the edge, not only to one endpoint card.

### Direction, Inverse, and Symmetry

Direction is part of the relationship meaning, not a display choice.
`prerequisites` and `extends` require direction. `related` and
`contrasts_with` are symmetric unless a later model synthesis explicitly
accepts a directed subtype.

Inverse expectations:

- A directional edge may define an inverse reading for navigation and QA, but
  the inverse does not create a second independent claim unless it has separate
  evidence.
- A symmetric edge should be visible from both endpoint cards. If both cards
  carry different copies, reconciliation should collapse or resolve the
  duplicates.
- Relationship asymmetry is a reconciliation conflict when one endpoint asserts
  an edge and the other endpoint contradicts, omits a required reciprocal view,
  or assigns incompatible evidence or status.

### Graph Closure

Graph closure means the method can reason about the connected conceptual graph
without losing local card authorship. It does not mean implementing graph
indexes, GraphRAG runtime, ontology database, or a graph database.

Closure expectations:

- Referenced endpoints should resolve to known cards, claims, or CQs, or be
  explicitly marked deferred.
- Edge type, endpoint roles, evidence attachment, verification state,
  reconciliation state, and extraction run provenance should be recoverable
  from the method record.
- Dangling relationship references are allowed only as deferred or unresolved
  records with a re-entry condition.
- Graph closure can be checked later by deterministic validators, but the
  validator design is out of scope for this slice.

### First-Class Edge Identity

A relationship needs first-class edge identity when any of these are true:

- It has its own source support, evidence grade, verification result, or
  reconciliation result.
- It was generated, updated, preserved, rejected, or marked unresolved by an
  extraction run.
- It participates in a duplicate, relationship asymmetry, slug drift, taxonomy
  drift, or parallel-agent conflict.
- It has lifecycle state different from either endpoint.
- It is referenced by a competency question as coverage evidence.

Relationships that merely aid human reading can remain card-local fields until
Slice04 decides final model wording. Relationships that carry method evidence
or conflict must be edge records.

## Competency Question Semantics

A competency question, or CQ, is a first-class method construct whose role is
explicitly stated rather than inferred from placement. One CQ can play several
roles over time, but the active role and status must be visible.

CQ roles and statuses:

- requirement: the CQ states what the concept-card set is expected to explain.
- answerability: the CQ records whether the current cards and claims can
  answer it from available source support.
- coverage: the CQ maps to the card, claim, source support, or edge that
  covers it.
- verification: the CQ can be used as a check target for a verifier or
  validation pass.
- retrieval: the CQ can be used as a search or memory-retrieval probe for
  future use.
- obsolete: the CQ no longer matches the accepted model, source scope, or
  operator question, but remains recorded for audit history.
- deferred: the CQ is valid but intentionally not covered yet, with a reason
  and re-entry condition.

Answerability is not the same as coverage. A CQ may be covered by a card but
not answerable if the supporting claim lacks evidence, verification, or memory
admission. A CQ may be answerable for local use but not yet verified for
durable semantic memory. Retrieval use must not imply memory admission.

CQ attachment points:

- A requirement CQ attaches to the source scope, extraction run, project/arc
  intent, or operator question that created it.
- A coverage CQ attaches to covered cards, claims, source spans, relationships,
  or edges.
- A verification CQ attaches to a verification result record.
- A retrieval CQ attaches to a query or retrieval scenario in later skill
  architecture, not in this conceptual slice.
- An obsolete or deferred CQ attaches to the result record or decision that
  explains its current status.

## Extraction Run Traceability

An extraction run is the audit home for how a set of cards, claims, edges, and
CQs came into being or changed. The run is a conceptual trace object, not a
script, package behavior, or runtime execution design.

Minimum extraction run traceability:

- source snapshot: the exact source material, version, locator set, and any
  old-card inputs used by the run.
- method version or prompt version: the concept-card method version, prompt
  version, or prompt packet used to perform extraction or re-extraction.
- agent scope: which agent, model, human, or parallel-worker lane was assigned
  which source scope or task scope.
- output set: generated cards, updated card records, generated or updated
  claims, generated or updated relationships/edges, and generated or updated
  CQs.
- old-card inputs: prior cards supplied as secondary preservation input, with
  explicit status as preserved, superseded, rejected, or unresolved.
- preservation decisions: unique prior-card value cannot disappear silently;
  every preservation decision needs a recorded outcome and rationale.
- validation result: structural validation output for required fields,
  provenance, body sections, relationship references, CQ coverage, and obvious
  consistency.
- reconciliation result: duplicate concept, competing definition, slug or
  taxonomy drift, relationship asymmetry, CQ coverage, and parallel-agent
  conflict outcomes.
- parallel-worker provenance: worker identity or role, assigned slice of the
  corpus, produced artifacts, conflicts raised, and merge/reconciliation
  disposition.

The extraction run should be the common provenance anchor for downstream
verification, reconciliation, and memory admission. A later implementation may
store this in files or metadata, but this slice only defines the method-level
traceability requirement.

## Reconciliation Semantics

Reconciliation is a process with durable result records. It resolves or
records conflicts across cards, claims, relationships/edges, CQs, and
extraction runs. It does not define a reconciliation algorithm.

Conflict classes:

- duplicate concept: two or more cards appear to represent the same concept.
- competing definition: claims define or explain the same concept in
  incompatible ways.
- slug drift: stable identifiers, filenames, or slugs diverge from the
  accepted concept boundary.
- taxonomy drift: concept placement changes without a recorded model reason.
- relationship asymmetry: directional, inverse, or symmetry expectations do
  not match between endpoint records.
- CQ coverage conflict: a CQ is claimed covered, answerable, verified, or
  obsolete in a way contradicted by source support or card coverage.
- parallel-agent conflict: parallel-worker outputs disagree on concept
  boundaries, claims, edge sets, coverage, preservation, or validation.

Reconciliation result records attach to affected cards, affected claims,
relationships or edges, competency questions, and extraction runs. A result
record should state the conflict class, affected constructs, source support,
decision, rationale, verifier or reconciler role, lifecycle effect, and memory
admission implication.

Reconciliation is a lifecycle dependency for memory admission. An admitted
card, claim, edge, or CQ must have reconciliation state complete, explicitly
not applicable, or deferred with operator acceptance and a re-entry condition.

## Scope Fences and Downstream Routing

Out of scope for this slice: final schema syntax, exact enum spelling, YAML
template shape, validator implementation, reconciliation algorithms, graph
database, graph indexes, GraphRAG runtime, memory runtime, ontology database,
CCDP service design, skill architecture, package behavior, README integration,
Makefile changes, generated zips, and source edits.

Slice04 should synthesize these provisional graph, competency-question,
extraction-run, and reconciliation semantics into the accepted v4.0 conceptual
model. Arc04 should decide skill architecture, guide layout, templates,
examples, package behavior, and README integration. Arc05 should plan source
edits, Makefile/package changes, validation gates, and implementation
mechanics.
