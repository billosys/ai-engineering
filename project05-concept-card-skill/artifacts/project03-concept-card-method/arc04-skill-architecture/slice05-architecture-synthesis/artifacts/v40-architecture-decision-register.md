# v4.0 Architecture Decision Register

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice05-architecture-synthesis
status: proposed-done
mode: final Arc04 decision register
```

## Purpose

This decision register records final decision outcomes from Arc04 and
unresolved decision routing for Arc05. It preserves Slice02, Slice03, and
Slice04 decisions rather than re-deciding them.

## Final Arc04 Decisions

| ID | Final decision | Source | Owner after Slice05 |
|----|----------------|--------|---------------------|
| D-1 | The concept-card method skill loads for method-specific concept-card work, not every research, memory, source-reading, project-management, or implementation task. | Slice02 load contract | Arc04 close, then skill maintainers. |
| D-2 | SKILL.md is a thin entrypoint with reason to load, positive load, negative load, problem ownership, dependency direction, and guide routing. | Slice02 and Slice03 | Arc05 implements wording. |
| D-3 | The skill owns concept-card method representation and routes adjacent concerns to collaboration-framework, source reading, domain skills, and implementation planning. | Slice02 ownership model | Arc05 preserves in source docs. |
| D-4 | Guide architecture is concern-based: load/routing, extraction, re-extraction/preservation, evidence lifecycle, graph/CQ, reconciliation, validation/verification, and memory admission. | Slice03 guide architecture | Arc05 plans guide files. |
| D-5 | Template architecture has user-authored, trace record, and result record surface classes. | Slice03 template architecture | Arc05 plans template files and schema syntax. |
| D-6 | The release-critical example architecture covers minimal card, claim-backed card, CQ coverage, relationship/edge, extraction-run trace, reconciliation, memory-admission, and parallel-worker default recipe. | Slice03 example architecture | Arc05 plans exact example files. |
| D-7 | The five-agent workflow is a default recipe, not an invariant, and extraction runs must capture parallel-worker provenance. | Slice02 and Slice03 | Arc05 preserves in guide/examples. |
| D-8 | Validation architecture separates deterministic structural checks, semantic audit checks, human/operator review, and deferred runtime checks. | Slice04 validation architecture | Arc05 plans validator-code only for accepted deterministic candidates. |
| D-9 | Package/discoverability behavior treats guides, templates, and release-critical examples as packaged surfaces; validation candidates may be packaged as documentation; generated artifacts and executable scripts remain Arc05 decisions. | Slice04 package/discoverability model | Arc05 plans package list and release gates. |
| D-10 | README and skill library discoverability must state the promise boundary and must not imply runtime or release behavior. | Slice04 package/discoverability model | Arc05 writes README/library text. |
| D-11 | Maintenance ownership has explicit owner and change path rules for conceptual model, guides, templates, examples, package behavior, README, skill library, validation candidate, validator-code, and version history. | Slice04 maintenance ownership | Arc05 applies during implementation planning. |

## Preserved Conceptual Decisions

Arc04 preserves the accepted Arc03 conceptual model:

- concept card remains the atomic visible authoring unit.
- claim is first-class when finer-grained source support, evidence grade,
  extraction confidence, verification, reconciliation, validation result, or
  memory admission is needed.
- source span and source support are distinct from general provenance.
- relationship and edge semantics preserve v3.2 vocabulary while allowing
  graph-native edge identity when evidence or lifecycle state attaches.
- competency question/CQ has requirement, answerability, coverage,
  verification, retrieval, obsolete, and deferred roles.
- extraction run is a trace record for source snapshot, method/prompt
  version, agent scope, output set, old-card inputs, validation,
  reconciliation, verification, preservation, and parallel-worker provenance.
- validation result, verification result, verification state, reconciliation
  result, reconciliation state, preservation decision, evidence grade,
  extraction confidence, source support, and memory admission remain distinct.

## Unresolved Decisions and Later Owner

| ID | Unresolved decision | Later owner | Re-entry condition |
|----|---------------------|-------------|--------------------|
| U-1 | Exact source layout for SKILL.md, guides, templates, examples, validation candidate docs, and package metadata. | Arc05 | Arc04 is formally closed and Arc05 opens implementation planning. |
| U-2 | Source edits to create or modify skill files. | Arc05 | Arc05 source-edit slices are accepted. |
| U-3 | Exact guide files, template files, example files, and filenames. | Arc05 | Arc05 decides layout and release-critical file set. |
| U-4 | Exact schema syntax for concept card, claim/source support, CQ, edge, extraction run, validation result, verification result, reconciliation result, preservation decision, and memory admission records. | Arc05 | Arc05 chooses representation and tests. |
| U-5 | Exact enum spelling for evidence grade, extraction confidence, verification state, reconciliation state, CQ status, validation result state, and memory admission state. | Arc05 | Arc05 schema/validator planning accepts names. |
| U-6 | validator-code scope, implementation language, CLI/API behavior, failure output, and deterministic validation scripts. | Arc05 | Arc05 accepts deterministic structural candidates as implementation work. |
| U-7 | Makefile and package-list updates. | Arc05 | Arc05 defines package build and check boundaries. |
| U-8 | README/library text, skill library indexing, and exact discoverability prose. | Arc05 | Arc05 edits source docs with version history. |
| U-9 | Generated zips, generated zip validation, package updates, release gates, and release mechanics. | Arc05 | Arc05 defines packaging and release verification. |
| U-10 | Tests for guides, templates, examples, validator-code, package paths, README/library discoverability, and release gates. | Arc05 | Arc05 creates testable implementation slices. |
| U-11 | Source version history alignment for every changed source document. | Arc05 | Arc05 identifies touched source docs. |
| U-12 | Runtime GraphRAG, graph database, ontology database, memory runtime, CCDP service, and live extraction behavior. | Later runtime or protocol project, not Arc04 | A later authorized project explicitly accepts runtime scope. |

## Final Versus Implementation Inputs

Final Arc04 decisions are method architecture decisions. Arc05
implementation-planning inputs are bounded questions that require source
layout, source edit, exact schema syntax, exact enum spelling, validator-code,
Makefile/package-list updates, README/library text, generated zips, tests,
release gates, package updates, and source version history decisions.

This distinction is part of the decision register: Arc04 accepts the shape of
the skill; Arc05 plans how to edit and verify the source repository.

## Package/Discoverability Promise Boundary

The package/discoverability decision is final at architecture level:

- The skill is discoverable as a document-method skill for concept-card
  extraction, re-extraction, evidence lifecycle, graph/CQ representation,
  reconciliation, validation, verification, and memory admission.
- The architecture does not promise runtime GraphRAG, graph database,
  ontology database, memory runtime, CCDP service, live extraction,
  executable validator, generated zip, package release, or source
  implementation behavior.
- Any such work requires a later owner, normally Arc05 for implementation
  planning or a later runtime/protocol project for services.

## Arc04 Close Inputs

Slice05 creates Arc04 close inputs but not the Arc04 closing-report.md.
Formal arc close must reproduce arc-ledger composition verification:

- A-6: load contract, reason to load, problem ownership, dependency direction,
  package behavior, and maintenance ownership compose across slice artifacts.
- A-7: accepted conceptual model constructs map to skill surfaces without
  collapsing distinct constructs.
- A-8: source edit, validator-code, README, Makefile, package, generated zip,
  implementation-planning, and implementation planning work are recorded as
  Arc05 inputs.

## Out of Scope

Out of scope for this decision register: source SKILL.md edits, source
checkout edits, source edit mechanics, validator-code implementation,
deterministic validation scripts, runtime services, GraphRAG, graph database,
memory runtime, CCDP service, live extraction, generated zips, package
release, source implementation, and the Arc04 arc-level closing-report.
