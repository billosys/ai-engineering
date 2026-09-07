# Project05 Plan: Document Extraction And Concept Cards

```yaml
project: project05-concept-card-skill
status: active
created: 2026-09-06
depends-on:
  - project03-concept-card-method
  - project04-knowledge-library-reorg
blocks:
  - live document-extraction skill use
  - live concept-cards skill use
related:
  - future ontology-engineering composite skill
  - NeON and ontology-engineering research
  - historical v3.2 concept-card workbench prompts
```

## Definition Of Done

Project05 implements live, installable skills in the post-Project04
knowledge-library layout. It consumes Project03's concept-card method planning
and the Project05 source-preparation architecture as evidence, while treating
Project04's closed source/package organization as the current repository
contract.

The project is done when:

- `document-extraction` exists as a detailed standalone skill for extracting
  usable Markdown, structure, media references, locators, manifests, reports,
  and caveats from PDF, EPUB, HTML, and converted-source inputs.
- `concept-cards` exists as a detailed standalone method skill for creating,
  validating, reconciling, preserving, and using provenance-bearing concept
  cards.
- Both skills use the current source layout: `SKILL.md`, sibling `guides/`,
  sibling `templates/` and/or `examples/` when needed, sibling
  `version-history.md`, and any other support directories only when the
  package contract explicitly supports them.
- Both skills are wired into repository discoverability, packaging, generated
  zip targets, install behavior, and validation gates.
- `concept-cards` routes raw PDF/EPUB/HTML or converted-source cleanup to
  `document-extraction`; it consumes extracted/prepared source outputs as
  upstream provenance rather than owning document conversion itself.
- Historical Project03/Project05 artifacts remain preserved as provenance, but
  stale layout and naming assumptions are superseded by this plan and current
  repository evidence.
- Project05 closes with evidence for source hygiene, skill metadata checks,
  package path checks, generated package contents, installability, README or
  skill-library discoverability, version history, and no silent drops.

## Nondeferrable Objectives

The following objectives are not optional and must not be downgraded to
deferrals by CC, CDC, or a later session without an explicit operator decision
recorded in this project:

- Create at least two live skills: `document-extraction` and `concept-cards`.
- Make both skills detailed enough for direct assistant use and human-assisted
  operator use.
- Update packaging and install surfaces so the skills are real packages, not
  planning-only documents.
- Preserve and modernize the PDF and EPUB preparation instructions inside
  `document-extraction`; do not bury them inside `concept-cards`.
- Implement the core concept-card v4.0 representation, provenance, evidence,
  reconciliation, validation, and memory-admission guidance in
  `concept-cards`.

Acceptable deferrals are limited to adjacent systems that are not required for
the two skills to exist and work as documented: executable validator programs,
runtime services, graph databases, ontology databases, GraphRAG integrations,
CCDP services, memory runtime automation, CI expansion, and release publishing
outside the repository-local gates. Any such deferral must include a reason and
re-entry condition.

## Naming Decisions

This project keeps the historical directory name
`project05-concept-card-skill` to preserve planning lineage. The implemented
skill names are:

- `document-extraction`, replacing the earlier planning name
  `source-preparation`.
- `concept-cards`, replacing the earlier planning name
  `concept-card-method`.

`ontology-engineering` is reserved as a likely future composite skill that may
route among concept cards, NeON-style methodology, competency questions,
ontology lifecycle work, alignment, and graph/knowledge modeling. Project05
may produce notes for that future skill, but it does not need to implement it
unless the operator explicitly expands the project.

## Current Boundary

Project04 is closed. Its layout and package decisions supersede stale
Project03/Project05 assumptions, especially any plan that placed templates,
examples, validation, or reference material under `guides/` merely for
packaging convenience. Project05 must verify current packaging behavior before
source edits begin and update the package machinery if sibling support
directories need to ship.

Project05 started with a readiness and scope-lock arc. That arc was not a
permission gate for deferring the skills; it was the evidence step that
prevented stale planning artifacts from overriding the current repository
organization.

## Arc Roadmap

| Arc | Capability | Dependencies |
| --- | --- | --- |
| Arc01: Readiness And Scope Lock | Reconcile Project03/Project05 evidence with Project04's current layout, lock skill names, package surfaces, and implementation sequence. | Project03 artifacts, Project04 close evidence, current source tree. |
| Arc02: Document Extraction Skill | Implement `document-extraction` as a standalone source skill with PDF/EPUB/HTML/converter workflows, manifests, templates, and examples. | Arc01. |
| Arc03: Concept Cards Skill Core | Implement `concept-cards` entrypoint and core guides for load contract, extraction, re-extraction, provenance, evidence lifecycle, relationship/CQ semantics, reconciliation, validation, verification, and memory admission. | Arc01, Arc02 routing decisions. |
| Arc04: Concept Card Records And Examples | Implement concept-card templates, examples, schema/reference material, and validation review surfaces using Project03 v4.0 semantics. | Arc03. |
| Arc05: Packaging, Docs, And Installability | Wire both skills into Makefile targets, README/docs skill-library discoverability, package path checks, generated zips, install behavior, and version histories. | Arc02, Arc03, Arc04. |
| Arc06: Gate Evidence And Project Closure | Run final validation, inspect generated package contents, reconcile ledgers, document any explicit deferrals, and close the project. | Arc05. |

## Status

Closed arcs:

- Arc01: Readiness And Scope Lock
- Arc02: Document Extraction Skill
- Arc03: Concept Cards Skill Core

Active arc: Arc04.

Arc04 is open with Slice01:
`arc04-concept-card-records-and-examples/slice01-record-template-foundation/`.

## Version History

### v1.0 - 2026-09-06

Initial Project05 plan opened after Project04 closure. Reoriented the project
around current post-Project04 layout, `document-extraction`, `concept-cards`,
future `ontology-engineering`, and nondeferrable implementation objectives.

### v1.1 - 2026-09-06

Arc01 close updated status only: readiness and scope-lock evidence is
CDC-verified, Arc01 is closed, and Arc02 is active. No roadmap re-sequencing or
scope reduction was made.

### v1.2 - 2026-09-06

Slice01 of Arc02 is CDC-verified and Arc02 has advanced to Slice02. This is a
status-only update; no roadmap re-sequencing, scope reduction, or Arc02 plan
change was made.

### v1.3 - 2026-09-06

Slice02 of Arc02 is CDC-verified and Arc02 has advanced to Slice03. This is a
status-only update; no roadmap re-sequencing, scope reduction, or Arc02 plan
change was made.

### v1.4 - 2026-09-06

Slice03 of Arc02 is CDC-verified and Arc02 has advanced to Slice04. This is a
status-only update; no roadmap re-sequencing, scope reduction, or Arc02 plan
change was made.

### v1.5 - 2026-09-06

Arc02 closed after Slice04 CDC verification and composition review. Arc03 is
now active with Slice01 opened for the `concept-cards` source scaffold and
load contract. The Arc02 roadmap wording was aligned with the already-planned
Arc05 package/docs/install boundary. No roadmap re-sequencing or scope
reduction was made.

### v1.6 - 2026-09-06

Slice01 of Arc03 is CDC-verified and Arc03 has advanced to Slice02 for
source-faithful extraction, re-extraction, preservation decisions, source
spans, source support, and extraction-run provenance. This is a status-only
update; no roadmap re-sequencing, scope reduction, or Arc03 plan change was
made.

### v1.7 - 2026-09-06

Slice02 of Arc03 is CDC-verified and Arc03 has advanced to Slice03 for
evidence lifecycle, extraction confidence/evidence-grade separation,
validation results, verification results/state, and review boundaries. The
Slice02 caller-wording cleanup is assigned to Slice03 source scope. No roadmap
re-sequencing, scope reduction, or Arc03 plan change was made.

### v1.8 - 2026-09-06

Slice03 of Arc03 is CDC-verified and Arc03 has advanced to Slice04 for
relationship edges, competency questions, reconciliation, memory admission,
and maintenance/promise boundaries. This is a status-only update; no roadmap
re-sequencing, scope reduction, or Arc03 plan change was made.

### v1.9 - 2026-09-06

Arc03 closed after Slice04 CDC verification and composition review. Arc04 is
now active with Slice01 opened for concept-card record template foundations
under the current sibling support layout. No roadmap re-sequencing or scope
reduction was made.
