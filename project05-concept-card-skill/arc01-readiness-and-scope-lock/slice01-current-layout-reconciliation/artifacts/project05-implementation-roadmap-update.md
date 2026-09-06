# Project05 Implementation Roadmap Update

```yaml
project: project05-concept-card-skill
arc: arc01-readiness-and-scope-lock
slice: slice01-current-layout-reconciliation
artifact: project05-implementation-roadmap-update
status: cc-produced
date: 2026-09-06
```

## Purpose

This roadmap update translates the current layout reconciliation into concrete
implementation guidance for the remaining Project05 arcs. It preserves the
nondeferrable skill objectives and makes the current package surface explicit.

## Current Roadmap Confirmation

The existing Project05 project plan remains structurally sound:

- Arc01 reconciles current source/package layout and locks scope.
- Arc02 implements `document-extraction`.
- Arc03 implements `concept-cards` core.
- Arc04 implements concept-card records and examples.
- Arc05 wires packaging, docs, and installability.
- Arc06 runs final gates and closes the project.

No arc re-sequencing is required by this slice.

## Required Updates For Later Arcs

### Arc02: Document Extraction Skill

Arc02 must implement the renamed standalone skill:

- source root: `knowledge/document-extraction/`;
- package name: `document-extraction`;
- source inputs: old PDF/EPUB preparation prompts plus
  `operator-accepted-src-prep-arch.md`;
- scope: PDF, EPUB, HTML, converted Markdown, media normalization, structure
  mapping/splitting, locators, manifests, validation reports, readiness
  reports, and caveats;
- mode support: human-assisted and agent-direct workflows;
- routing: downstream consumers include `concept-cards`, indexing, reading,
  source review, and ordinary analysis.

Arc02 must not implement the superseded `knowledge/source-preparation/` root
unless the operator explicitly reverses the naming decision.

### Arc03: Concept Cards Skill Core

Arc03 must implement the renamed method skill core:

- source root: `knowledge/concept-cards/`;
- package name: `concept-cards`;
- source inputs: Project03 v3.2 baseline and v4.0 conceptual/architecture
  planning;
- scope: concept card representation, claims, source support, spans/locators,
  evidence lifecycle, extraction and re-extraction, relationship edges,
  competency questions, validation/verification, reconciliation,
  preservation, and memory admission;
- routing: raw or converter-produced source cleanup goes to
  `document-extraction`.

Arc03 must not implement the superseded `knowledge/concept-card-method/` root
unless the operator explicitly reverses the naming decision.

### Arc04: Records And Examples

Arc04 must preserve the Project03 v4.0 semantic distinctions while using the
current sibling support-directory layout:

- templates under `knowledge/concept-cards/templates/`;
- examples under `knowledge/concept-cards/examples/`;
- optional `reference/` or `validation/` as sibling directories only if the
  package macro is updated to include them;
- examples should show prepared-source inputs produced by
  `document-extraction`.

Arc04 must not collapse validation, verification, reconciliation, evidence
grade, extraction confidence, and memory admission into one confidence field.

### Arc05: Packaging, Docs, And Installability

Arc05 must make both skills live packages:

- add Makefile targets and zip names for `document-extraction` and
  `concept-cards`;
- add both entrypoints to skill metadata checks;
- include both packages in `make all`, `make skills`, `make install`, and
  `make print-skill-zips`;
- keep release workflow asset collection Makefile-driven;
- update README and `docs/skill-library.md`;
- run `make check-skills`, per-skill package builds, package listing
  inspection, `make check-package-paths`, and install smoke or an accepted
  narrower install check.

Arc05 should update `docs/building-and-installing.md` if the new skills require
package macro support beyond current sibling `templates/` and `examples/`.

### Arc06: Gate Evidence And Project Closure

Arc06 must close against evidence, not intention:

- generated zips inspected;
- package-path validation passes or exceptions are justified;
- installed package shape is checked;
- project ledger rows P-2 and P-3 are done, not deferred;
- any runtime/infrastructure deferrals have owner, reason, and re-entry
  condition;
- no silent drop from the nondeferrable objectives.

## Allowed Deferrals

Allowed deferrals remain limited to adjacent systems not required for the two
skills to exist and be usable:

- executable validators;
- validator-code tests;
- runtime services;
- GraphRAG;
- graph database;
- ontology database;
- memory runtime automation;
- CCDP service integration;
- live extraction runtime;
- CI expansion;
- release publication outside repository-local validation gates.

Every deferral must have a reason and re-entry condition.

## Disallowed Deferrals

The following are not allowed to be deferred by later CC or CDC passes without
explicit operator approval recorded in Project05:

- live `document-extraction` skill creation;
- live `concept-cards` skill creation;
- detailed human-assisted and agent-direct guidance for both skills;
- PDF and EPUB preparation modernization in `document-extraction`;
- concept-card v4.0 representation and lifecycle guidance in `concept-cards`;
- Makefile/package/docs/install validation wiring for both skills.

## Carry-Forward Decisions

- Current Project05 plan names are authoritative even though the project
  directory remains `project05-concept-card-skill` for lineage.
- Project04 layout and package behavior supersede Project03 package
  workarounds.
- Sibling support directories are preferred and currently package-compatible
  for `templates/` and `examples/`.
- If new support directory classes are required, package behavior must be
  extended openly.
- `ontology-engineering` remains reserved for a future composite skill.

## Suggested Next Slice

After CDC verifies Slice01, Arc01 can close. The next implementation slice
should be Arc02 Slice01 for the `document-extraction` source scaffold and load
contract, using this slice's package-surface requirements as input.
