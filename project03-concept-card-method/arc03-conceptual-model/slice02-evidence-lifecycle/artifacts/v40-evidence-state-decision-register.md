# v4.0 Evidence State Decision Register

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice02-evidence-lifecycle
status: proposed-done
mode: evidence-state decision register
```

## Scope Fence

This register records lifecycle decisions for evidence and state families in
the v4.0 conceptual model. It does not finalize schema syntax, enum spelling,
YAML template shape, validator implementation, skill architecture, package
behavior, README integration, Makefile changes, generated zips, source edits,
relationship or edge semantics, competency-question semantics,
extraction-run trace schema, reconciliation algorithms, GraphRAG runtime,
memory runtime, ontology database, or CCDP service design.

## Register

| Construct or state family | Status | Attachment point | Rationale | Dependencies | Open question | Downstream route |
|---------------------------|--------|------------------|-----------|--------------|---------------|------------------|
| extraction confidence | accepted | claim, concept card, extraction run | Preserves v3.2 confidence signalling while limiting it to extractor judgment about source explicitness and extraction difficulty. | Source support, claim, extraction run. | Should extraction confidence be claim-level only, or can a card-level rollup remain? | Slice04 final model synthesis; Arc05 later template planning. |
| source support | accepted | claim-source support relationship, source span, claim | v4.0 needs the source support for a claim to be visible apart from bibliographic provenance and verification. | Source span, claim, evidence grade, verification result. | Does source span require durable identity or only locator value semantics? | Slice04 final model synthesis; Arc05 locator syntax planning. |
| evidence grade | provisional | claim-source support relationship, claim | Arc02 identified evidence grade as distinct from extraction confidence, verification state, and memory admission. | Source support, verification state, verifier, memory admission. | What evidence-grade vocabulary should v4.0 use, and what object is graded? | Slice04 final model synthesis; Arc04/Arc05 defer exact enum spelling and validation. |
| verification state | provisional | claim, concept card, claim-source support relationship | Verification state tracks lifecycle position for independent checking without replacing the verification result record. | Verification result, verifier role, evidence grade, extraction run. | Which transitions are valid before and after failed or superseded checks? | Slice04 final model synthesis; Arc05 implementation planning. |
| verification result | accepted | result record attached to claim, card, support relationship, or extraction run | A durable result record preserves who or what checked a claim and what happened, supporting independent evidence instead of bare assertion. | Verifier role, source support, evidence grade. | What minimum result fields are conceptual rather than schema implementation? | Slice04 final model synthesis; Arc05 schema and validator planning. |
| verifier role | accepted | verifier role attached to verification result | The model needs an authority label for independent checking while avoiding account/tool implementation detail. | Verification result, verification state. | Does v4.0 need verifier identity as data, or only verifier role and result provenance? | Slice04 final model synthesis; Arc05 implementation planning. |
| reconciliation state | provisional | concept card, claim, relationship/edge, extraction run | Memory admission must know whether conflicts are pending, resolved, failed, or not applicable, but this slice does not define graph/CQ/run semantics. | Reconciliation result, relationship/edge semantics, extraction run. | Is reconciliation required for all cards, only multi-agent runs, or only detected conflicts? | Slice03 graph/CQ/run semantics; Slice04 final model synthesis. |
| reconciliation result | provisional | result record attached to affected cards, claims, relationships, or runs | Reconciliation needs a durable outcome for duplicate concepts, competing definitions, slug drift, taxonomy drift, and relationship asymmetry. | Reconciliation state, extraction run, relationship/edge semantics. | Which conflict classes belong in the conceptual model versus later algorithms? | Slice03 graph/CQ/run semantics; Slice04 final model synthesis. |
| memory admission | provisional | lifecycle gate on concept card and possibly claim | Project03 targets provenance-bearing memory consolidation; admitted content must be distinguishable from merely extracted or validated content. | Evidence grade, verification state, verification result, reconciliation state, operator/human acceptance. | Is memory admission a status, result record, policy gate, or combination? | Slice04 final model synthesis; Arc04 and Arc05 defer skill/runtime implementation. |
| human/operator acceptance | provisional | lifecycle gate, verification result, memory admission | Some decisions require judgment beyond deterministic checks, especially high-impact, low-support, or policy-sensitive memory admission. | Evidence grade, verification state, reconciliation state, memory admission. | Which cases require operator acceptance versus ordinary verifier approval? | Slice04 final model synthesis; Arc04/Arc05 planning. |
| structural validation | accepted | concept card, claim, source support, extraction run | v3.2 validation checks remain a useful pre-verification gate for required structure, provenance, slug/path hygiene, and obvious consistency. | Extraction confidence, source support, verification state. | Which checks stay conceptual requirements and which become deterministic validator implementation? | Slice04 final model synthesis; Arc05 deterministic validator planning. |
| deferred schema and implementation choices | deferred | Arc04 and Arc05 planning | This slice defines method semantics only; schema syntax, exact enum spelling, package behavior, README integration, Makefile changes, and source edits are later responsibilities. | Accepted Arc03 conceptual model. | Which model choices become package or validator requirements after Arc03 closes? | Arc04 skill architecture and Arc05 implementation planning. |

## Lifecycle Dependencies

- Extraction confidence depends on the extraction act and source support, but
  not on verification result.
- Evidence grade depends on source support and may be revised by verification
  or reconciliation.
- Verification state depends on verification result records and verifier role.
- Reconciliation state depends on detected conflicts and reconciliation result
  records.
- Memory admission depends on sufficient source support, evidence grade,
  verification state, reconciliation state, and any required human/operator
  acceptance.

## Decision Summary

- Accepted: extraction confidence as distinct from evidence grade; source
  support as a separate attachment point; verification result as a result
  record; verifier as a role; structural validation as a pre-verification
  lifecycle gate.
- Provisional: evidence grade, verification state, reconciliation state,
  reconciliation result, memory admission, and human/operator acceptance.
- Deferred: final enum spelling, schema syntax, validator implementation,
  relationship/CQ/run detail beyond reserved attachment points, skill
  architecture, package behavior, README integration, Makefile changes,
  generated zips, source edits, GraphRAG runtime, memory runtime, ontology
  database, and CCDP service design.
