# v4.0 Package and Discoverability Model

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice04-validation-packaging-discoverability
status: proposed-done
mode: package discoverability model
```

## Purpose

This artifact defines package behavior, package inclusion, packaged surface
categories, and discoverability boundaries for the first v4.0 concept-card
method skill. It decides what the package should promise at architecture
level while routing exact source layout and package mechanics to later owners.

The skill remains discoverable as a method for concept-card extraction,
re-extraction, evidence lifecycle handling, graph/CQ representation,
reconciliation, validation, verification, and memory admission. Its promise
boundary is documentary and method-level: no runtime service, no graph
database, no memory runtime, no live extraction, no GraphRAG runtime, no CCDP
service, and no ontology database.

## Package Surface Decisions

| Surface category | Package behavior | Package inclusion decision |
|------------------|------------------|----------------------------|
| guides | Packaged surface. Include focused method guides as the primary detailed documentation behind the thin entrypoint. | Include in the released skill once Arc05 chooses exact file layout. |
| templates | Packaged surface. Include user-authored templates plus trace record and result record templates. | Include in the released skill once Arc05 chooses schema syntax and filenames. |
| examples | Packaged surface. Include release-critical examples for minimal card, claim-backed card, CQ coverage, relationship/edge, extraction-run trace, reconciliation, memory-admission, and parallel-worker default recipe. | Include release-critical examples; route optional examples to Slice05 or later releases. |
| scripts | Candidate surface only. Validation candidates may be documented, but executable scripts are not promised by this architecture. | Route script inclusion and validator-code to Arc05. |
| generated artifacts | Planning-only input unless Arc05 converts them into release artifacts. | Do not package generated artifacts from planning as authoritative release output. |
| validation candidates | Packaged as architecture guidance and future validator requirements, not as implemented validator-code. | Include as documentation if Arc05 keeps them in a guide or validation reference. |
| planning-only input | Source inventories, CDC checks, slice plans, ledgers, and handoff packets remain planning-only input. | Do not include as ordinary package content except where a future README cites them as provenance. |

## Thin Entrypoint and Routing

`SKILL.md` stays a thin entrypoint. It states the reason to load the skill,
positive load triggers, negative load triggers, problem ownership, and route
choices into guides. It should not become a monolithic method manual.

Positive load examples include concept-card method design, concept extraction,
source-faithful claim support, graph/CQ model work, reconciliation, validation
architecture, and memory admission decisions. Negative load examples include
ordinary research summaries, generic project management, unrelated source
reading, implementation planning, runtime system design, and ad hoc memory
lookup that does not need the concept-card method.

## README and Skill Library Discoverability

README and skill library discoverability should make the method findable by
describing:

- the reason to load the concept-card method skill;
- the packaged guides, templates, release-critical examples, and validation
  candidates;
- the thin entrypoint route into focused guides;
- the compatibility boundary with the collaboration-framework skill;
- the promise boundary for package behavior.

The README and skill library text does not promise runtime GraphRAG behavior,
does not promise a graph database or ontology database, does not promise a
memory runtime, does not promise a CCDP service, does not promise live
extraction, and does not promise executable validator-code before Arc05
implements and tests it.

## Preservation of Prior Decisions

The package preserves the Slice02 load contract, thin SKILL.md posture, and
dependency direction. It preserves Slice03 guide architecture, template
architecture, and example architecture decisions: user-authored artifacts,
trace record artifacts, result record artifacts, release-critical examples,
the five-agent default recipe, not an invariant, and required
parallel-worker provenance.

## Later Owner Routing

| Later owner | Routed question |
|-------------|-----------------|
| Slice05 | architecture synthesis, final package/discoverability summary, optional-example disposition, and Arc05 handoff text. |
| Arc05 | source edit work, exact file layout, schema syntax, enum spelling, Makefile updates, README edits, generated zips, tests, release mechanics, package updates, package list edits, and validator-code implementation planning. |

## Out of Scope

Out of scope for this artifact: source SKILL.md edits, source checkout edits,
source edit mechanics, validator-code implementation, deterministic validation
scripts, exact CLI/API behavior, graph database design, GraphRAG runtime,
memory runtime, CCDP service behavior, live extraction, package release, and
generated zips.
