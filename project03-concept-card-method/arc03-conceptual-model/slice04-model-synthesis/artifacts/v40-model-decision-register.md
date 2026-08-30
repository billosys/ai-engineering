# v4.0 Model Decision Register

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice04-model-synthesis
status: proposed-done
mode: Arc03 synthesized decision register
```

## Scope

This register synthesizes Slice01, Slice02, and Slice03 decisions into one
Arc03-level decision register. It records accepted, provisional, deferred,
out of scope, and open question items with rationale, dependency notes, and
downstream routing. It is not final skill architecture or implementation
planning.

## Accepted Decisions

| Decision | Rationale | Dependency | Downstream routing |
|----------|-----------|------------|--------------------|
| concept card remains the central first-class entity | v3.2 card atomicity is a core strength, and Slice01 accepted the card as the durable method unit. | Slice01 construct boundary; Arc02 v3.2 baseline. | Arc04 must preserve the card as the visible authoring unit; Arc05 later chooses representation. |
| claim is a first-class conceptual entity | v4.0 needs a unit for source support, evidence grade, verification state, reconciliation state, and memory admission that is finer than the card. | Slice01 claim boundary; Slice02 attachment points. | Slice04 model accepted; Arc04 decides guide/template presentation. |
| source support is distinct from provenance | Provenance identifies source material and run context; source support states which source span supports a claim or edge. | Slice02 lifecycle model. | Arc04 templates/guides must preserve both ideas; Arc05 chooses locator syntax. |
| extraction confidence is distinct from evidence grade | v3.2 confidence remains useful only when narrowed to extractor judgment about the extraction act. | Slice02 evidence lifecycle. | Arc04 must not present confidence as warrant; Arc05 exact enum spelling deferred. |
| verification result and validation result are separate result records | Structural validation and independent semantic checking answer different questions. | Slice02 result-record decisions. | Arc04 should document both gates; Arc05 plans deterministic validation and verification evidence. |
| competency question is a first-class construct | v3.2 CQs already operate as requirements, coverage hooks, and usability checks. | Slice01 boundary; Slice03 CQ semantics. | Arc04 guide design should expose CQ roles and coverage without final UI decisions. |
| extraction run is a first-class trace entity | Source-primary extraction, prompt versioning, old-card preservation, parallel-worker provenance, validation, and reconciliation need one audit home. | Slice03 extraction-run semantics. | Arc04 must plan run-record guidance; Arc05 decides metadata files/scripts. |
| reconciliation conflict classes and result records are method-level concepts | Duplicate concepts, competing definitions, slug drift, taxonomy drift, relationship asymmetry, CQ coverage conflict, and parallel-agent conflict affect trust and memory admission. | Slice02 lifecycle reservations; Slice03 reconciliation semantics. | Arc04 should preserve conflict vocabulary; Arc05 algorithms remain deferred. |
| memory admission is a distinct lifecycle gate | Validated content is not automatically reliable enough for durable semantic memory. | Slice02 lifecycle model; Slice03 reconciliation dependency. | Arc04 must name admission policy surfaces; Arc05/runtime enforcement remains later work. |

## Provisional Decisions

| Decision | Rationale | Dependency | Open question | Downstream routing |
|----------|-----------|------------|---------------|--------------------|
| source span identity remains provisional | The model needs source locators, but durable identity may depend on schema and source-type mechanics. | Slice01 and Slice02 source-span decisions. | Is source span a value object only, or sometimes a first-class entity? | Arc04 guide/template planning; Arc05 schema syntax. |
| evidence grade vocabulary remains provisional | Arc03 accepts the concept but not exact grade names or CCDP mapping details. | Slice02 evidence-grade boundary. | Which grade vocabulary best fits CCDP-compatible claim/provenance/audit semantics? | Arc04 policy wording; Arc05 exact enum spelling. |
| verification state and reconciliation state vocabulary remains provisional | State semantics are accepted, but exact transitions and names are implementation-sensitive. | Slice02 lifecycle model; Slice03 reconciliation model. | Which transitions are required before failed, superseded, or deferred checks? | Arc04 guide language; Arc05 validator implementation. |
| relationship fields can remain card-local authoring affordances | v3.2 fields are useful, but graph-native edge identity is required only when evidence or lifecycle state attaches to the relationship. | Slice03 graph semantics. | Are all relationships stored as edge records, or only evidence-bearing/conflict-bearing ones? | Arc04 template architecture; Arc05 schema planning. |
| memory admission may attach to card, claim, edge, and possibly CQ | Card-level admission is required; finer-grained admission may be needed for claim and graph use. | Slice02 memory-admission model; Slice03 CQ/edge semantics. | Which constructs can be admitted independently? | Slice04 accepted model notes; Arc04 and Arc05 policy planning. |
| human/operator acceptance remains provisional | Some evidence, reconciliation, and memory-admission cases require judgment, but policy thresholds are not finalized. | Slice02 human/operator acceptance row. | Which cases require operator acceptance versus ordinary verification? | Arc04 workflow guide; Arc05 enforcement gates. |

## Deferred Decisions

| Decision | Rationale | Dependency | Re-entry condition | Downstream routing |
|----------|-----------|------------|--------------------|--------------------|
| final skill layout and guide split | Arc03 defines concepts, not loadable skill architecture. | Accepted v4.0 conceptual model. | Arc04 begins skill architecture planning. | Arc04. |
| template shape and exact schema syntax | Syntax depends on architecture and implementation constraints. | Arc04 skill architecture. | Arc04 accepts template roles and Arc05 plans implementation. | Arc04 and Arc05. |
| exact enum spelling for evidence, verification, reconciliation, CQ, and admission states | Arc03 defines state families, not final serialized values. | Accepted model and Arc04 presentation choices. | Arc05 schema/validator planning. | Arc05. |
| deterministic validator implementation | Validation result is conceptual now; scripts and tests are implementation planning. | Arc04 template/schema direction. | Arc05 source-edit plan is accepted. | Arc05. |
| retrieval implementation for CQs | CQ retrieval is a conceptual use, but indexes, UI, GraphRAG runtime, and memory runtime are not Arc03 work. | Memory admission and CQ identity. | A later runtime or skill-architecture slice authorizes retrieval design. | Arc04 or later runtime project. |
| exactly-five parallel-worker workflow policy | v3.2's five-agent pattern is a proven recipe, but Arc03 does not decide whether it is invariant, default, or parameterized. | Extraction-run traceability and operator workflow needs. | Arc04 operator-facing workflow planning. | Arc04. |

## Out of Scope Decisions

| Decision | Rationale | Downstream routing |
|----------|-----------|--------------------|
| source edits, README changes, Makefile changes, generated zips, and package behavior | The planning branch is the source of truth for plans only; implementation changes require an accepted later plan. | Arc04/Arc05 after authorization. |
| final skill layout, final file layout, and package inclusion | Arc03 models method concepts; Arc04 owns skill architecture. | Arc04. |
| GraphRAG runtime, memory runtime, ontology database, graph database, and graph indexes | Arc03 defines graph and memory-admission semantics, not runtime infrastructure. | Later implementation/runtime work if authorized. |
| CCDP service design | Arc03 keeps CCDP-compatible evidence semantics on the method side without designing a service. | Future CCDP-specific planning if needed. |
| live extraction or re-extraction corpus run | Arc03 is conceptual-model synthesis from verified planning inputs. | A later validation project or implementation slice. |

## Open Questions for Later Work

- What source span identity and locator granularity should Arc05 implement?
- What evidence grade vocabulary maps cleanly to CCDP-compatible
  claim/provenance/audit semantics?
- Which verification state, reconciliation state, CQ status, and memory
  admission values become exact enum spelling?
- Should relationship records always become graph-native edges, or only when
  edge-level evidence, lifecycle state, provenance, or reconciliation is
  needed?
- Which memory admission decisions require human/operator acceptance?
- Is the v3.2 five-agent parallel workflow an invariant, default recipe, or
  parameterized workflow?

## Slice Lineage

- Slice01 supplied construct boundaries and initial accepted/provisional
  classifications.
- Slice02 supplied lifecycle separation and claim/source/evidence attachment
  point decisions.
- Slice03 supplied graph, competency-question, extraction-run, reconciliation,
  and traceability decisions.
- Slice04 synthesizes those inputs into the accepted Arc03 conceptual model
  and routes remaining decisions to Arc04 and Arc05.
