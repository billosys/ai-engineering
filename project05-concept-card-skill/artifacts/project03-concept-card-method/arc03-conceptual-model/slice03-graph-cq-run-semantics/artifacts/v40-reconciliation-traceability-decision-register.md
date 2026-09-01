# v4.0 Reconciliation and Traceability Decision Register

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice03-graph-cq-run-semantics
status: proposed-done
mode: graph-cq-run decision register
```

## Scope Fence

This register records graph, competency-question, extraction-run, and
reconciliation construct or state-family decisions for the v4.0 conceptual
model. It does not finalize schema syntax, exact enum spelling, YAML template
shape, validator implementation, reconciliation algorithms, graph database,
graph indexes, GraphRAG runtime, memory runtime, ontology database, CCDP
service design, skill architecture, package behavior, README integration,
Makefile changes, generated zips, or source edits.

## Register

| Construct or state family | Status | Rationale | Dependencies | Open question | Attachment point | Downstream route |
|---------------------------|--------|-----------|--------------|---------------|------------------|------------------|
| v3.2 relationship fields: `prerequisites`, `extends`, `related`, `contrasts_with` | accepted | The fields are useful typed relationship vocabulary and should carry forward even if v4.0 adds graph-native edge records. | Concept card, relationship/edge, source support. | Which authoring fields remain card-local after Slice04 synthesis? | Concept card relationship section; relationship or edge record when evidence or lifecycle state is needed. | Slice04 final model synthesis; Arc04 template planning. |
| relationship or edge | provisional | v4.0 needs first-class edge identity when relationships have evidence, verification, reconciliation, run provenance, or conflicts. | Concept card endpoints, claim endpoints, source support, evidence grade, verification state, reconciliation state, extraction run. | Are all typed relationships represented as edges, or only relationships that need identity? | Edge record attached to endpoint cards, claims, CQs, source support, and extraction run. | Slice04 model synthesis; Arc05 schema and validator planning. |
| endpoint roles | accepted | Direction and symmetry require typed endpoint roles rather than unordered link lists. | Relationship type, concept card, claim, CQ. | Which endpoint role vocabulary is final model language rather than schema enum spelling? | Relationship or edge record. | Slice04 final wording; Arc05 exact enum spelling deferred. |
| direction and inverse policy | provisional | `prerequisites` and `extends` are directional; `related` and `contrasts_with` are symmetric unless a later accepted subtype says otherwise. | Endpoint roles, graph closure, reconciliation result. | Should inverse labels be recorded as model vocabulary or derived by readers and tools? | Relationship or edge record; navigation/readability views. | Slice04 final model synthesis. |
| graph closure state | provisional | The method needs to know whether referenced endpoints resolve, are deferred, or remain unresolved without requiring a graph database implementation. | Endpoint roles, edge records, validation result, reconciliation state. | Which closure failures block memory admission versus ordinary publication? | Relationship/edge record, validation result, reconciliation result. | Slice04 lifecycle synthesis; Arc05 validator planning. |
| competency question identity | accepted | v3.2 already uses competency questions as requirements, coverage hooks, and usability checks; v4.0 should make them durable constructs. | Concept cards, claims, source support, extraction run. | Can simple examples use implicit CQs, or must all CQs be explicit records? | CQ record attached to source scope, card, claim, edge, or extraction run. | Slice04 final model synthesis; Arc04 guide planning. |
| CQ role/status family | provisional | A CQ can be a requirement, answerability check, coverage target, verification target, retrieval probe, obsolete record, or deferred question. | CQ identity, verification result, memory admission, retrieval scenario. | Which roles are statuses, which are use-context labels, and which belong to later tooling? | CQ record and result records for verification, obsolete, or deferred disposition. | Slice04 final model synthesis; Arc04/Arc05 defer UI and tooling. |
| extraction run traceability | accepted | Source-primary extraction and parallel re-extraction need an audit home for source snapshot, method version, prompt version, agent scope, output set, old-card inputs, preservation, validation result, reconciliation result, and parallel-worker provenance. | Source snapshot, method or prompt packet, concept cards, claims, edges, CQs, validation result, reconciliation result. | What minimum trace fields are mandatory for memory admission? | Extraction run record linked to generated cards, updated card records, claims, edges, CQs, and old-card inputs. | Slice04 final model synthesis; Arc05 metadata and scripts planning. |
| source snapshot | accepted | A run cannot be audited if the source material and locator set are not recoverable. | Source span, provenance reference, extraction run. | What locator granularity belongs in the conceptual model versus source-specific implementation? | Extraction run record and source support. | Slice04 source-support synthesis; Arc05 locator syntax planning. |
| method version or prompt version | accepted | A generated or updated card set must be traceable to the method and prompt packet that produced it. | Extraction run, validation result, reconciliation result. | Should method version and prompt version be separate model fields or one provenance bundle? | Extraction run record. | Slice04 final model synthesis; Arc04 prompt/guide planning. |
| agent scope and parallel-worker provenance | provisional | Parallel-worker provenance preserves who or what worked on each source scope and why conflicts arose. | Extraction run, source snapshot, output set, reconciliation result. | Is the exactly-five-worker v3.2 recipe invariant, default, or parameterized pattern? | Extraction run record and reconciliation result. | Slice04 model synthesis for provenance; Arc04 operator-facing workflow decision. |
| old-card preservation decision | accepted | Unique prior-card value must be preserved, superseded, rejected, or unresolved explicitly rather than silently dropped. | Old-card inputs, extraction run, reconciliation result, validation result. | Which preservation outcomes are conceptual statuses versus exact enum spelling? | Extraction run record; affected card, claim, edge, or CQ; reconciliation result. | Slice04 final model synthesis; Arc05 validation planning. |
| validation result | accepted | Structural validation remains a separate gate from semantic verification, reconciliation, and memory admission. | Concept card, claim, edge, CQ, extraction run. | Which validation checks are conceptual requirements and which are implementation-specific tests? | Result record attached to extraction run and affected constructs. | Slice04 lifecycle synthesis; Arc05 deterministic validator planning. |
| reconciliation conflict classes | accepted | Duplicate concept, competing definition, slug drift, taxonomy drift, relationship asymmetry, CQ coverage conflict, and parallel-agent conflict are method-level conflict classes. | Cards, claims, relationships/edges, CQs, extraction runs, source support. | Are there additional conflict classes that only Slice04 can see after synthesis? | Reconciliation result attached to affected cards, affected claims, relationships, CQs, and runs. | Slice04 final model synthesis. |
| reconciliation result record | accepted | Reconciliation needs a durable result record with affected constructs, decision, rationale, source support, lifecycle effect, and memory admission implication. | Reconciliation state, verifier or reconciler role, evidence grade, extraction run. | Does reconciliation require a distinct reconciler role or reuse verifier role? | Result record attached to affected cards, affected claims, relationships/edges, CQs, and extraction runs. | Slice04 final model synthesis; Arc05 result schema planning. |
| memory admission dependency | provisional | Memory admission must depend on source support, verification state, reconciliation state, and unresolved conflict disposition. | Evidence lifecycle from Slice02, reconciliation result, graph closure, CQ status. | Which deferred reconciliation states can be operator-accepted for admission? | Lifecycle gate on concept card, claim, edge, and possibly CQ. | Slice04 final model synthesis; Arc04/Arc05 runtime policy deferred. |
| retrieval semantics for CQs | deferred | CQs can act as retrieval probes, but retrieval UI, indexes, GraphRAG runtime, and memory runtime are later concerns. | CQ identity, memory admission, skill architecture. | What retrieval behavior belongs in the future skill versus a separate memory runtime? | CQ record as conceptual query; implementation attachments deferred. | Arc04 skill architecture and Arc05 implementation planning. |
| implementation mechanics | out of scope | This slice defines conceptual semantics only. It must not choose graph database, graph indexes, reconciliation algorithm, GraphRAG runtime, memory runtime, ontology database, CCDP service design, package behavior, README, Makefile, generated zips, or source edits. | Accepted Arc03 conceptual model. | Which mechanics become requirements after Slice04 accepts the model? | Later-arc planning records, not Slice03 artifacts. | Arc04 skill architecture; Arc05 implementation plan. |

## Decision Summary

- Accepted: v3.2 relationship vocabulary carry-forward, endpoint roles,
  competency question identity, extraction run traceability, source snapshot,
  method version or prompt version traceability, old-card preservation
  decisions, validation result separation, reconciliation conflict classes, and
  reconciliation result records.
- Provisional: relationship or edge identity policy, direction/inverse policy,
  graph closure state, CQ role/status family, agent scope and parallel-worker
  provenance details, and memory admission dependency rules.
- Deferred: retrieval implementation semantics for CQs.
- Out of scope: schema syntax, exact enum spelling, reconciliation algorithms,
  graph database, GraphRAG runtime, memory runtime, ontology database, CCDP
  service design, skill architecture, package behavior, README, Makefile,
  generated zips, and source edits.

## Downstream Routing

Slice04 should compose accepted and provisional graph/CQ/run semantics with
the Slice01 construct boundaries and Slice02 evidence lifecycle. Arc04 should
decide the thin skill entrypoint, guide split, templates, examples, package
behavior, and README integration. Arc05 should plan implementation mechanics,
source edits, Makefile/package changes, deterministic validation scripts, and
verification gates.
