# v4.0 Construct Decision Register

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice01-construct-boundaries
status: proposed-done
mode: per-construct decision register
```

## Scope Fence

This register records construct-boundary decisions for the v4.0 conceptual
model. It makes the boundary between method concept and later skill or
implementation concern explicit. It does not finalize evidence-grade
vocabulary, verification-state transitions, reconciliation algorithms,
memory-admission policy, schema syntax, skill layout, package behavior,
deterministic validator scripts, README changes, Makefile changes, or source
edits.

## Register

Each row supplies classification, rationale, dependencies, open question,
downstream Arc03 route, decision status, and the method-concept boundary
against later skill or implementation concerns.

| Construct | Classification | Decision | Rationale | Dependencies | Open question | Downstream Arc03 route | Method concept vs later concern |
|-----------|----------------|----------|-----------|--------------|---------------|------------------------|---------------------------------|
| concept card | first-class entity | accepted | v3.2 uses the card as the atomic durable unit; v4.0 should carry forward atomicity, source-faithful synthesis, provenance, body sections, typed relationships, competency questions, source-primary re-extraction, and preservation. | Claims, source spans, relationships, CQs, runs, verification, reconciliation, and memory admission may attach to the card. | Is a simple card allowed to keep implicit claims, or must every substantive assertion become an explicit claim? | Slice04 final model synthesis after Slice02 and Slice03. | Method concept now; final card template, schema syntax, and file layout are Arc04/Arc05 concerns. |
| claim | first-class entity | provisional | Arc02 identified that v3.2 cards contain assertions but do not model claim as separate from card, evidence, confidence, or memory admission. | Source span, evidence grade, extraction confidence, verification result, reconciliation result, memory admission. | Is a card a claim, a bundle of claims, or a curated summary over claims? | Slice02 evidence and lifecycle; Slice04 final synthesis. | Method concept now; storage representation and extraction prompts are later concerns. |
| source span | value object or first-class entity | provisional | v3.2 provenance is strong but card-level; v4.0 needs support granularity for evidence and verification. | Claim, source provenance, evidence grade, verification result, extraction run. | Does source span need durable identity, or is it a structured locator value attached to claim support? | Slice02 evidence and lifecycle; Slice04 final synthesis. | Method concept now; locator syntax and parser implementation are Arc05 concerns. |
| evidence grade | status | provisional | v3.2 `extraction_confidence` mixes source clarity, extractor certainty, verification status, evidence grade, and usability; v4.0 must separate them. | Claim, source span, verifier, verification result, reconciliation state, memory admission. | What evidence-grade vocabulary should be used, and what object does it grade? | Slice02 evidence and lifecycle. | Method concept now; exact enum names and validator schema are later concerns. |
| relationship or edge | first-class entity plus field carry forward | provisional | v3.2 typed relationships are valuable, but graph-native work needs edge identity, evidence, status, inverse policy, and reconciliation. | Concept card endpoints, claim support, evidence grade, reconciliation result, extraction run. | Which v3.2 relationship fields remain card-local fields and which become graph-native edges? | Slice03 graph, CQ, and run semantics; Slice04 final synthesis. | Method concept now; graph database, indexes, or GraphRAG runtime are deferred concern items. |
| competency question | first-class entity plus status | accepted/provisional | v3.2 competency questions already operate as requirements, mapping aids, card links, and coverage checks. | Concept card, claim, coverage result, verifier, extraction run. | Which statuses distinguish covered, answerable, verified, obsolete, and deferred CQs? | Slice03 graph, CQ, and run semantics. | Method concept now; UI, reporting scripts, and package placement are later concerns. |
| extraction run | first-class entity | provisional | Arc02 identified run traceability as missing: source snapshot, prompt version, agent scope, output set, validation, preservation, and reconciliation need an audit home. | Concept cards, claims, source spans, verifier, reconciliation, preservation result, validation result. | What minimum run metadata is required before cards can be trusted downstream? | Slice03 graph, CQ, and run semantics. | Method concept now; metadata file format and deterministic scripts are Arc04/Arc05 concerns. |
| verifier | role | provisional | v4.0 must distinguish extraction confidence from independent verification; verifier names the method authority that performs or records checking. | Verification result record, evidence grade, claim, source span, extraction run. | Is verifier an actor role only, or does the model need verifier identity as data? | Slice02 evidence and lifecycle. | Method role now; account identity, tool identity, and automation implementation are later concerns. |
| reconciliation | process and result record | provisional | Parallel extraction needs an explicit authority for duplicate concepts, competing definitions, slug drift, taxonomy drift, relationship asymmetry, and agent conflict. | Concept card, claim, relationship/edge, extraction run, verifier, memory admission. | Is reconciliation a required gate for all cards, only multi-agent runs, or only conflicts? | Slice03 graph, CQ, and run semantics; Slice04 final synthesis. | Method process/result record now; reconciliation algorithms are out of scope and remain later concerns. |
| memory admission | status or result record | provisional | Project03 targets provenance-bearing memory consolidation; v3.2 validates cards but does not state when future cognition may rely on them. | Evidence grade, verification state, reconciliation state, claim, card, extraction run, operator decision. | Is memory admission a lifecycle status, a policy gate result, or both? | Slice02 evidence and lifecycle; Slice04 final synthesis. | Method concept now; memory runtime and storage policy enforcement are deferred concern items. |

## Cross-cutting Dependencies

- Slice02 must separate extraction confidence, source support, evidence grade,
  verification state, reconciliation state, and memory admission.
- Slice03 must define relationship or edge semantics, competency question
  status, extraction run traceability, and reconciliation result semantics.
- Slice04 must compose accepted and provisional construct boundaries into the
  final v4.0 conceptual model.

## Decision Summary

- Accepted now: concept card as the central first-class entity; competency
  question as a first-class entity with provisional statuses.
- Provisional now: claim, source span, evidence grade, relationship or edge,
  extraction run, verifier, reconciliation, and memory admission.
- Deferred concern: schema syntax, evidence-grade vocabulary wording,
  verification-state transitions, reconciliation algorithms,
  memory-admission policy, skill layout, package behavior, deterministic
  validator scripts, README changes, Makefile changes, source edits, GraphRAG
  runtime, memory runtime, and implementation file locations.
