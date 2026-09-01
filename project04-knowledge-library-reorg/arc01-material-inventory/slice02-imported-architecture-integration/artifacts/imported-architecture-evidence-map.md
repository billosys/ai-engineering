# Imported Architecture Evidence Map

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice02-imported-architecture-integration
artifact: imported-architecture-evidence-map
artifact-status: slice integration evidence
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
created-on: 2026-09-01
source-files-edited: false
```

## Purpose

This map integrates imported Project02 and Project03 planning evidence into
Project04 without converting prior proposals into final Project04 directory
decisions. It preserves accepted architecture facts separately from
implementation-plan hypothesis, compatibility obligation, and Slice03 topology
classification inputs.

## Consumed Source-Surface Context

Slice02 consumes the verified Slice01 source inventory as context:

- `arc01-material-inventory/slice01-source-surface-inventory/artifacts/current-source-surface-map.md`
- `arc01-material-inventory/slice01-source-surface-inventory/artifacts/material-role-classification.md`
- `arc01-material-inventory/slice01-source-surface-inventory/artifacts/source-validation-surface-map.md`
- `arc01-material-inventory/slice01-source-surface-inventory/cdc-verification.md`

The Slice01 artifacts are source inventory, not imported architecture. They
show that current `docs/` is mixed framework, method, extraction, design, and
reader material; current `knowledge/` holds domain/tooling skill substrate;
and current validation depends on `README.md`, `SKILL.md`, `AGENTS.md`,
`CLAUDE.md`, `Makefile`, `package-path-exceptions.tsv`, generated zip roots,
package-local links, and CCDP package checks.

The project-level `artifacts/external-ontology-rubric-research.md` is input,
not accepted taxonomy. It provides a two-axis vocabulary for kind and topology,
but Slice03 owns the classification instrument and matrix. Slice02 uses it to
name questions without finalizing public categories.

## Project02 Accepted Architecture Facts

Evidence source:
`artifacts/operator-accepted-architecture.md`.

Accepted facts Project04 must preserve:

| Fact | Project04 preservation requirement |
|------|------------------------------------|
| Project02 operator-accepted architecture was accepted on 2026-08-31. | Treat the named component architecture as a real constraint, not merely a draft. |
| `collaboration-framework` remains the daily-driver composer. | Do not make Project04 vocabulary imply the composer is deprecated or forced into an atomic skill shape. |
| The seven specialist components are `engineering-methods`, `project-management`, `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and `contribution-style`. | Arc02 must decide where framework component source roots live while preserving these names and roles. |
| `engineering-methods` owns methodology, process, operational routing, component-boundary analysis, and source/package/release gates. | Source/package/release gates should not drift into README-only prose or unrelated package scripts without a route back to `engineering-methods`. |
| Ontology critique belongs at `engineering-methods/guides/05-component-boundary-analysis.md`, not as a standalone Project02 component. | Project04 can reuse ontology vocabulary, but should not accidentally create a new framework component for ontology critique unless a later project reopens that accepted decision. |
| Each component versions as a whole through its `SKILL.md` plus sibling `version-history.md`. | Arc02 and later source-edit slices must preserve component-level version-history policy during moves. |
| CCDP remains a separate protocol distribution, not a collaboration-framework skill component. | Project04 must preserve `protocols/ccdp/` and `ccdp.zip` separation unless a separate protocol-package decision reopens it. |
| Memory admission is future research, not a Project02 component. | Do not use memory-admission vocabulary as a reason to add another Project02 component during this project. |

## Project02 Implementation-Plan Hypotheses

Evidence sources:

- `artifacts/component-file-layout-plan.md`
- `artifacts/package-target-plan.md`
- `artifacts/skill-entrypoint-validation-plan.md`
- `artifacts/readme-wayfinding-plan.md`
- `artifacts/migration-compatibility-plan.md`
- `artifacts/package-path-link-exception-plan.md`
- `artifacts/implementation-sequence-roadmap.md`

Implementation-plan hypothesis items relevant to Project04:

- Component source roots are planned as top-level roots such as
  `engineering-methods/` and `project-management/`. Project04 may need to
  adjust this against the `docs/` as user documentation and `knowledge/` as
  substrate direction before source edits.
- Generated component package roots are planned to match component names, with
  `collaboration-framework.zip` kept as the composer package and seven new
  specialist zips added.
- `ALL_SKILL_FILES`, `INSTALL_ZIPS`, `CF_FILES`, component package targets,
  `make collab-framework`, `make check-skills`, `make check-package-paths`,
  and `make all` are expected validation surfaces after implementation.
- README should describe composed use, standalone component use, source
  checkout, generated zip, unzipped/install, installed skill route, migration
  notes, and CCDP separation.
- Package-local links are preferred. Source-only or provenance references
  should be explicit, and package-path exception rows should be narrow,
  reasoned, and expiring where possible.
- Implementation sequence should establish roots and compatibility before
  Makefile and README changes, then repair package-local links before adding
  package-path exceptions.

These are useful implementation-plan hypotheses. They do not override
Project04's need to decide a target directory contract in Arc02.

## Project02 Compatibility Obligations

Project04 must carry these compatibility obligations into Arc02 and later
implementation planning:

- Preserve the `collaboration-framework` daily-driver composer route.
- Preserve installed-skill route wording for cross-component use rather than
  brittle cross-package relative links.
- Preserve README discoverability for source checkout, generated zip,
  unzipped/install, and installed skill reader modes.
- Preserve component `SKILL.md` plus `version-history.md` policy.
- Preserve generated package roots and package-local link checks once
  packages exist.
- Preserve `AGENTS.md` and `CLAUDE.md` compatibility instructions and the
  symlink intent.
- Preserve CCDP as a separate protocol distribution with separate package
  validation.

## Project03 Method-Skill Evidence

Evidence sources:

- `../project03-concept-card-method/closing-report.md`
- `../project03-concept-card-method/arc04-skill-architecture/closing-report.md`
- `../project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md`
- `../project03-concept-card-method/arc04-skill-architecture/slice02-load-contract-ownership/artifacts/v40-load-contract.md`
- `../project03-concept-card-method/arc04-skill-architecture/slice03-guide-template-example-architecture/artifacts/v40-guide-architecture.md`
- `../project03-concept-card-method/arc04-skill-architecture/slice04-validation-packaging-discoverability/artifacts/v40-validation-architecture.md`
- `../project03-concept-card-method/arc04-skill-architecture/slice04-validation-packaging-discoverability/artifacts/v40-package-discoverability-model.md`
- `../project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/artifacts/v40-source-layout-plan.md`
- `../project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/v40-deferral-register.md`

Accepted Project03 facts relevant to Project04:

| Fact | Project04 relevance |
|------|---------------------|
| `concept-card-method` is planned as a method skill, not yet implemented or packaged in source. | Project04 should treat it as planned method-skill input, not live source inventory. |
| The future source home was planned as `knowledge/concept-card-method/`. | Arc02 must decide whether method skills belong under `knowledge/` and whether this remains the right source root. |
| The future entrypoint is a thin `SKILL.md`. | Project04 should preserve the thin-entrypoint plus focused-guides pattern for method skills where accepted. |
| Focused `guides/` own extraction, re-extraction, evidence lifecycle, graph/CQ, reconciliation, validation/verification, memory admission, and maintenance/package concerns. | Project04 should not collapse method guidance into a README page or one monolithic prompt. |
| Templates, examples, validation documentation, and support documents were planned under `guides/` subdirectories to fit existing package behavior. | Arc02 must decide whether this package-compatible layout remains acceptable under the broader docs/knowledge split. |
| Validation separates deterministic structural checks, semantic audit, human/operator review, and deferred runtime checks. | Project04 should preserve validation surface distinctions when planning knowledge-library categories. |
| Memory admission is a method lifecycle gate, not a memory runtime. | Project04 should keep memory admission as method guidance unless a future memory runtime project accepts ownership. |
| CCDP compatibility is evidence-language and boundary-aware; CCDP service behavior is deferred. | Treat the concept-card method as CCDP-adjacent, not as a CCDP protocol package or service. |

## Slice03 Topology Inputs

Inputs for Arc01 Slice03 skill-kind and topology classification:

- `collaboration-framework` is the accepted composite framework/operational
  example because its identity is daily-driver composition over specialist
  components.
- Rust remains a candidate atomic domain/tooling anchor from Slice01 because
  it has a single coherent load reason and current `knowledge/rust/` skill
  substrate.
- `concept-card-method` is a method skill edge case. It may classify as atomic
  if the load reason is one coherent method, but it may classify as composite
  if its identity depends on orchestrating ontology, extraction, validation,
  memory admission, and CCDP-adjacent work. Slice03 owns topology
  classification.
- `knowledge/biome/` remains a source-backed topology stress case because one
  source root currently contains multiple installable skill entrypoints.

## Boundary Summary

Accepted fact: Project02 accepted components and Project03 accepted method
architecture constrain Project04.

Implementation-plan hypothesis: component root placement, package target
details, README wording, Makefile edits, source-edit sequencing, and
package-path exception shape are prior implementation plans that Project04 must
test against its own target directory contract.

Compatibility obligation: package-local links, generated zip roots,
installed-skill route wording, source checkout reader routes, `AGENTS.md` /
`CLAUDE.md`, and CCDP separation must remain visible in later plans.

Slice03 topology input: atomic/composite and skill-kind classification remain
open until Slice03 applies the rubric to source-backed and imported surfaces.
