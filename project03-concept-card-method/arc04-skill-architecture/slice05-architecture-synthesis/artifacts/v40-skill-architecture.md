# v4.0 Skill Architecture

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice05-architecture-synthesis
status: proposed-done
mode: final Arc04 skill architecture
```

## Purpose

This artifact synthesizes the final Arc04 skill architecture for the v4.0
concept-card method. It composes the verified Slice02 load contract and
ownership model, Slice03 guide/template/example architecture, and Slice04
validation, package/discoverability, and maintenance ownership decisions.

This is architecture, not implementation or release. It does not edit source
SKILL.md, guides, templates, examples, README, Makefile, package list,
validator-code, schema, enum, tests, generated zips, package release files, or
the source checkout.

## Architecture Summary

The v4.0 concept-card method skill is a loadable knowledge skill with a thin
entrypoint, focused guides, reusable templates, release-critical examples,
documented validation candidates, package behavior boundaries, README/library
discoverability, and explicit maintenance ownership.

| Surface | Final Arc04 decision |
|---------|----------------------|
| SKILL.md | Thin entrypoint that states reason to load, positive load triggers, negative load triggers, problem ownership, dependency direction, and guide routing. |
| guides | Concern-based guides for load/routing, extraction, re-extraction and preservation, evidence lifecycle, graph and CQ, reconciliation, validation and verification, and memory admission. |
| templates | Templates split by surface class: user-authored, trace record, and result record. |
| examples | Release-critical examples for minimal card, claim-backed card, CQ coverage, relationship/edge, extraction-run trace, reconciliation, memory-admission, and five-agent parallel-worker default recipe. |
| validation candidates | Deterministic structural candidates are planned separately from semantic audit, human/operator review, and deferred runtime checks. |
| package behavior | Guides, templates, and release-critical examples are packaged surfaces; validation candidates may be packaged as documentation; executable scripts and generated artifacts are Arc05 decisions. |
| README/library discoverability | README and skill library text should describe the method, load boundary, packaged surfaces, and promise boundary without runtime or release overclaims. |
| maintenance ownership | Conceptual model, guide, template, example, package list, package behavior, README, skill library, validation candidate, validator-code, and version history changes have explicit owners and change paths. |

## Load Contract

The reason to load is method-specific concept-card work: creating, revising,
auditing, reconciling, validating, verifying, or planning concept-card
material as a provenance-bearing knowledge substrate.

Positive load triggers include concept-card extraction, re-extraction,
claim-level source support, evidence grade analysis, extraction confidence
capture, verification state/result capture, validation result capture,
reconciliation result/state handling, competency question/CQ coverage,
relationship/edge modeling, preservation decision work, and memory admission
decisions.

Negative load triggers include ordinary research summaries, generic project
management, ordinary source reading, implementation planning, unrelated
domain-knowledge work, and memory lookup that does not ask for concept-card
method output.

Problem ownership: this skill owns concept-card method representation. It
depends on collaboration-framework for posture, ledger discipline, project
management, and close mechanics; on source-reading practice for faithful
evidence capture; on domain skills for domain correctness; and on Arc05 or
later implementation guidance for source edit and release work. That is the
dependency direction: adjacent guidance remains primary for its own problem,
and this skill loads when the output must become concept-card method
substrate.

## Conceptual Model Preservation

The architecture preserves the accepted Arc03 conceptual model:

- concept card remains the visible atomic authoring unit: one concept per
  card, source-faithful synthesis, and required provenance.
- claim is available as a first-class finer-grained unit when source support,
  evidence grade, extraction confidence, verification state/result,
  validation result, reconciliation state/result, or memory admission needs
  more precision than the card.
- source span and source support remain distinct from general provenance.
- evidence grade is warrant, while extraction confidence is the extractor's
  signal about the extraction act.
- relationship vocabulary carries forward, and graph-native edge identity is
  required when evidence, lifecycle state, provenance, reconciliation, or CQ
  coverage attaches to the relationship.
- competency question/CQ remains first-class for requirement, answerability,
  coverage, verification, retrieval, obsolete, and deferred roles.
- extraction run remains a trace record for source snapshot, method or prompt
  version, agent scope, output set, old-card inputs, preservation decisions,
  validation result, reconciliation result, verification result, and
  parallel-worker provenance.
- validation result, verification result, verification state, reconciliation
  result, reconciliation state, preservation decision, and memory admission
  remain distinct lifecycle or result-record concerns, not one confidence and
  not one validation field.

## Guide Architecture

The guide architecture is concern-based:

- Load and routing guide: reason to load, positive load, negative load,
  problem ownership, dependency direction, and operator workflow entry.
- Extraction guide: source snapshot, source-faithful concept card extraction,
  claim identification, source support capture, extraction confidence, and
  extraction run provenance.
- Re-extraction and preservation guide: comparison against old cards,
  preservation decision handling, and parallel-worker provenance.
- Evidence lifecycle guide: source span, source support, evidence grade,
  extraction confidence, verification state, validation result,
  reconciliation state, and memory admission.
- Graph and CQ guide: relationship vocabulary, edge identity, competency
  question/CQ coverage, answerability, retrieval-probe use, obsolete status,
  and deferred status.
- Reconciliation guide: conflict classes and auditable reconciliation result
  records.
- Validation and verification guide: structural validation result separated
  from semantic verification result/state.
- Memory admission guide: admission as a lifecycle gate that depends on source
  support, evidence grade, verification state, validation result,
  reconciliation state, preservation disposition, and operator acceptance
  when required.

## Template Architecture

Template classes are:

- user-authored surfaces: concept cards, claim/source support records where
  curated by the operator, competency question/CQ records, and
  relationship/edge records.
- trace record surfaces: extraction run records, source snapshot details,
  method or prompt version, agent scope, output set, old-card inputs, and
  parallel-worker provenance.
- result record surfaces: validation result, verification result,
  reconciliation result, preservation decision, and memory admission records.

Arc05 may choose exact schema syntax and enum spelling, but it must preserve
these surface classes and their attachment points.

## Example Architecture

The first-release example set is release-critical for:

- minimal card;
- claim-backed card;
- CQ coverage;
- relationship/edge;
- extraction-run trace;
- reconciliation;
- memory-admission;
- parallel-worker default recipe.

The five-agent workflow is a default recipe, not an invariant. Examples may
name five agents as a known working pattern, but actual extraction run records
must capture agent scope and parallel-worker provenance for whatever worker
count was used.

## Validation Architecture

Validation candidates are classified as:

- deterministic structural: required fields, required sections, provenance,
  source support presence, relationship references, CQ coverage references,
  graph closure over local references, preservation decision records, memory
  admission gate fields, path/slug hygiene, and obvious consistency.
- semantic audit: source support warrant, evidence grade adequacy,
  extraction confidence calibration, relationship meaning, CQ answerability,
  reconciliation rationale, and preservation rationale.
- human/operator review: memory admission approval, conflict disposition,
  preservation exceptions, and material uncertainty.
- deferred runtime: graph database closure, GraphRAG retrieval probes,
  ontology database checks, memory runtime enforcement, CCDP service
  orchestration, and live extraction.

## Package and Discoverability

Package behavior is documentary and method-level. Guides, templates, and
release-critical examples are packaged surfaces. Validation candidates may be
packaged as documentation or future validator requirements. Executable
validator-code, scripts, generated artifacts, generated zip output, Makefile
package mechanics, package updates, and release gates belong to Arc05.

README and library discoverability should name the reason to load, the thin
entrypoint route, packaged surfaces, relationship to collaboration-framework,
and the promise boundary.

Promise boundary: the v4.0 skill architecture does not promise runtime system
behavior, GraphRAG, graph database, ontology database, memory runtime, CCDP
service, live extraction, executable validator, generated zip, package
release, source implementation, or source checkout behavior before later
implementation planning accepts that work.

## Maintenance Ownership

Maintenance ownership follows the Slice04 owner model:

- Arc03 owns accepted conceptual semantics; later model changes need explicit
  proposal and downstream guide/template/example updates.
- Arc04 owns this architecture synthesis and the accepted skill-surface
  decisions until formal arc close.
- Slice05 provides the final architecture packet and Arc05 handoff.
- Arc05 owns implementation planning for source layout, source edit work,
  exact guide files, template files, example files, schema syntax, enum
  spelling, validator-code, Makefile/package lists, README/library text,
  generated zips, tests, release gates, package updates, and source version
  history.

## Arc04 Close Inputs

This artifact is an Arc04 close input. It does not write the Arc04
closing-report.md. Formal arc close should reproduce arc-ledger composition
verification for A-6, A-7, and A-8 after Slice05 receives CDC verification.

## Out of Scope

Out of scope for Slice05 and this architecture artifact: source SKILL.md
edits, source checkout edits, source edit mechanics, validator-code
implementation, deterministic validation scripts, runtime services, GraphRAG
runtime, graph database design, memory runtime, CCDP service behavior, live
extraction, generated zips, package release, source implementation, and the
Arc04 arc-level closing-report.
