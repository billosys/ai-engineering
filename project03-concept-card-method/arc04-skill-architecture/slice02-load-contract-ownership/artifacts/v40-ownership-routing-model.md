# v4.0 Ownership Routing Model

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice02-load-contract-ownership
status: proposed-done
mode: ownership routing model
```

## Purpose

This artifact defines the concept-card method skill's problem ownership,
non-ownership boundaries, dependency direction, adjacent guidance routing, and
operator workflow boundary. It preserves the Arc03 conceptual model while
leaving guide, template, example, validation, package, README, Makefile,
source edit, validator-code, generated zips, and implementation planning
questions to later owners.

## Problem Ownership

The concept-card method skill owns method-specific guidance for turning source
material into a provenance-bearing concept-card substrate.

It owns:

- concept card authoring as one concept per card with source-faithful
  synthesis and required provenance;
- claim identification when a card needs finer-grained source support,
  evidence grade, extraction confidence, verification state, reconciliation
  state, or memory admission;
- source support modeling that connects claims, edges, or CQ coverage to
  source spans while keeping source support distinct from bibliographic
  provenance;
- evidence-grade reasoning at the method level, without choosing exact enum
  spelling in this slice;
- extraction and re-extraction workflow boundaries, including old-card
  preservation and extraction run traceability;
- competency question and CQ coverage use for requirement, answerability,
  coverage, verification, retrieval, obsolete, and deferred roles;
- relationship and graph-edge method semantics when source support, evidence,
  lifecycle state, reconciliation, or CQ coverage attaches to a relationship;
- validation result, verification result, reconciliation result, preservation
  decision, and memory admission surfaces as distinct method concepts;
- routing unresolved architecture and implementation questions to Slice03,
  Slice04, Slice05, or Arc05.

## Non-Ownership Boundaries

The skill does not own every evidence, memory, project-management, or
implementation task.

It does not own:

- general collaboration-framework posture, ledger discipline, project
  management, arc close, slice close, or plan-change mechanics;
- ordinary source reading, citation gathering, or literature review where the
  requested output is not concept cards or concept-card evidence;
- domain-knowledge correctness for programming languages, systems, writing
  craft, visual design, or other specialized domains;
- implementation planning for source checkout edits, schema files, exact enum
  spelling, validator-code, tests, Makefile updates, README updates, generated
  zips, package updates, or release mechanics;
- runtime services such as graph database design, memory runtime design,
  GraphRAG infrastructure, CCDP service design, or live extraction behavior;
- final guide architecture, final template architecture, final example set,
  package inclusion, README integration, or deterministic validation script
  selection in this slice.

## Dependency Direction

| Adjacent guidance | Dependency direction |
|-------------------|----------------------|
| collaboration-framework | This skill depends on collaboration-framework for posture, ledger discipline, project management, close mechanics, and evidence calibration. Collaboration-framework does not depend on this skill except when a project specifically adopts concept cards as its knowledge substrate. |
| project management | This skill routes project, arc, slice, ledger, and closing mechanics to project management guidance. It may produce concept-card artifacts inside a planned slice, but it does not define planning layout. |
| source reading | This skill depends on source reading for faithful extraction inputs and citations. Source reading does not depend on concept cards unless the operator asks to convert source evidence into cards, claims, source support, or CQs. |
| implementation planning | This skill routes source edit work to implementation planning, especially Arc05 for Project03. Implementation planning consumes the accepted skill architecture after Slice05, not this Slice02 model alone. |
| domain-knowledge | This skill depends on domain-knowledge skills for correctness in the subject matter being represented. Domain-knowledge guidance remains primary when the task is about the domain rather than concept-card representation. |

## Operator Workflow Boundary

The skill should guide the operator through method decisions, not silently run
a memory or extraction system.

Operator workflow coverage:

- Extraction: select source snapshots, identify candidate concept cards,
  claims, source support, relationships, competency questions, and extraction
  confidence while preserving provenance.
- Re-extraction: compare new output with old cards, preserve unique prior-card
  value, supersede or reject unsupported material, and record unresolved
  conflicts.
- Verification: route semantic checking to a verifier role and verification
  result/state; do not treat structural validation as semantic verification.
- Validation: record validation result for required fields, provenance, source
  support, relationship references, CQ coverage, path/slug hygiene, and
  obvious consistency.
- Reconciliation: record duplicate concepts, competing definitions, slug
  drift, taxonomy drift, relationship asymmetry, CQ coverage conflict,
  parallel-worker conflict, and preservation conflict through auditable result
  records.
- Competency questions: use a competency question or CQ as a requirement,
  answerability check, coverage target, verification target, retrieval probe,
  obsolete record, or deferred question without implying memory admission.
- Memory admission: decide whether cards, claims, edges, or CQs may be relied
  on as durable semantic memory only after source support, evidence grade,
  verification state, validation result, reconciliation state, preservation
  disposition, and any required operator acceptance are known.
- Five-agent and parallel-worker use: present five agents as a default recipe
  for parallel re-extraction, while allowing parameterized worker counts and
  requiring extraction-run provenance for the actual workflow used.

## Preservation of Arc03 Distinctions

This ownership model preserves Arc03's no-flattening rule: concept card,
claim, source support, evidence grade, extraction confidence, verification
state, validation result, reconciliation state, competency question,
extraction run, and memory admission are distinct method concerns, not one
confidence field or one validation field.

## Routing of Unresolved Questions

| Owner | Routed questions |
|-------|------------------|
| Slice03 | final guide architecture, final template architecture, final example set, and the split between user-authored surfaces and trace/result-record surfaces. |
| Slice04 | validation determinism, validation candidate selection, package behavior, package inclusion, README integration, discoverability, and maintenance ownership. |
| Slice05 | architecture synthesis, final architecture packet, unresolved decision register, and Arc05 handoff. |
| Arc05 | source edit planning, implementation planning, exact file layout, exact schema syntax, exact enum spelling, validator-code, Makefile updates, README updates, generated zips, package updates, tests, and release gates. |

## Out of Scope

Out of scope for this slice: final guide architecture, final template
architecture, final example set, package inclusion, README integration,
Makefile changes, validator-code, deterministic validation scripts, generated
zips, released packages, graph database design, memory runtime design, CCDP
service design, live extraction behavior, source checkout edits, exact schema
syntax, exact enum spelling, and implementation changes.
