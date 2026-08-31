# v4.0 Surface Routing Decision Register

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice02-source-layout-content-plan
artifact: v40-surface-routing-decision-register
status: proposed-done
```

## Purpose

This register records accepted, deferred, and no-op decisions for Slice02.
Every row names an owner or later slice routing. The register preserves each
Arc04 decision as an input and does not reopen accepted architecture.

## Decision Register

| ID | Status | Decision | Owner or later slice | Rationale |
|----|--------|----------|----------------------|-----------|
| D-1 | accepted | Use `knowledge/concept-card-method/` as the planned source home. | Slice02 | Matches the existing `knowledge/` skill pattern and keeps concept-card method problem ownership separate from the root collaboration-framework skill. |
| D-2 | accepted | Use `knowledge/concept-card-method/SKILL.md` as the thin SKILL.md entrypoint. | Slice02 | Preserves the Arc04 decision that SKILL.md carries reason to load, positive load, negative load, problem ownership, dependency direction, and guide routing. |
| D-3 | accepted | Use numbered guide files under `knowledge/concept-card-method/guides/`. | Slice02 | Preserves the Arc04 concern split and makes content sequence clear for implementation. |
| D-4 | accepted | Put template files under `knowledge/concept-card-method/guides/templates/`. | Slice02 | Keeps templates package-compatible with the Slice01 package behavior constraint. |
| D-5 | accepted | Put example files under `knowledge/concept-card-method/guides/examples/`. | Slice02 | Keeps release-critical examples package-compatible while leaving release gating to Slice04. |
| D-6 | accepted | Put validation documentation under `knowledge/concept-card-method/guides/validation/`. | Slice02 | Packages validation guidance as documentation without choosing validator-code or deterministic validation implementation. |
| D-7 | accepted | Put support documents under `knowledge/concept-card-method/guides/reference/`. | Slice02 | Keeps support document surfaces package-compatible and separates reference detail from workflow guides. |
| D-8 | accepted | Preserve package behavior by fitting the current SKILL.md plus sibling guides package contract. | Slice02; Slice04 for final package acceptance | No package behavior change is required by the planned layout, but package target names and package list edits remain Slice04 work. |
| D-9 | deferred | Decide schema syntax for cards, claims, source support, source spans, edges, CQs, extraction runs, validation results, verification results, reconciliation results, preservation decisions, and memory admission records. | Slice03 | Slice02 names files and attachment points only. |
| D-10 | deferred | Decide enum spelling for evidence grade, extraction confidence, verification state, reconciliation state, CQ status, validation result, and memory admission. | Slice03 | Enum choices affect templates, examples, and validation checks. |
| D-11 | deferred | Decide validator-code scope, validator-code language, deterministic validation, tests, and failure-message format. | Slice03 | Validation mechanics need their own plan before implementation. |
| D-12 | deferred | Decide package target names, package list edits, package-path exceptions, package-path checks, generated zip policy, generated archives, release gates, package release boundary, README/library discoverability, and source version-history obligations. | Slice04 | Package and discoverability mechanics require Makefile and README planning. |
| D-13 | deferred | Compose source edit sequence, implementation slice recommendations, deferral register, and Project03 close input. | Slice05 | Slice05 synthesizes verified Slice02 through Slice04 outputs. |
| D-14 | no-op | Do not create top-level `templates/`, `examples/`, `validation/`, or `reference/` directories beside `guides/` in the planned skill source home. | Slice02 | A sibling layout would require a package behavior change; Slice02 can avoid that by using package-compatible guide subdirectories. |
| D-15 | no-op | Do not move or rewrite v3.2 workbench files as part of Slice02. | Slice02 | Workbench files are source inputs and provenance, not the planned v4.0 skill source layout. |
| D-16 | no-op | Do not edit source, generated zips, package release files, runtime services, GraphRAG, graph database, ontology database, memory runtime, CCDP service, or live extraction behavior in Slice02. | Slice02 | The arc is planning-only and the prompt forbids these changes. |

## Arc04 Preservation

Arc04 decision preservation by surface:

- SKILL.md remains a thin SKILL.md entrypoint with reason to load, positive
  load, negative load, problem ownership, dependency direction, and guide
  routing.
- Guide files preserve the accepted Arc04 concern split: load/routing,
  extraction, re-extraction and preservation, evidence lifecycle, graph/CQ,
  reconciliation, validation/verification, and memory admission.
- Template files preserve the accepted Arc04 surface classes:
  user-authored, trace record, and result record.
- Example files preserve the release-critical set: minimal card,
  claim-backed card, CQ coverage, relationship/edge, extraction-run trace,
  reconciliation, memory-admission, and five-agent default recipe.
- Validation documentation preserves the accepted Arc04 split between
  deterministic structural candidates, semantic audit, human/operator review,
  and deferred runtime checks.
- Package behavior preserves the Slice01 constraint by making all planned
  non-SKILL surfaces live under sibling `guides/`.
- Maintenance ownership remains explicit: Slice03 owns schema and validation;
  Slice04 owns package, discoverability, release, and version history; Slice05
  owns synthesis and Project03 close input.

## Later-Slice Routing Checklist

The following items are deliberately deferred to later slice owners:

- Slice03: schema syntax.
- Slice03: enum spelling.
- Slice03: validator-code scope and validator-code language.
- Slice03: deterministic validation.
- Slice03: tests and failure-message format.
- Slice04: package target names.
- Slice04: package list edits.
- Slice04: package-path exception rows and package-path checks.
- Slice04: generated zip policy and generated archives.
- Slice04: README and library discoverability.
- Slice04: release gates and package release boundaries.
- Slice04: source version-history obligations and final version history text.
- Slice05: implementation-plan synthesis, implementation slice
  recommendations, deferral register, and Project03 close input.

## Scope Boundary

Slice02 is out of scope for source implementation and does not edit source. It
does not create generated zips, package release files, release readiness
claims, runtime services, GraphRAG, graph database, ontology database, memory
runtime, CCDP service, or live extraction behavior.

No decision in this register requires Arc05 re-sequencing, a new slice, or a
scope correction.
