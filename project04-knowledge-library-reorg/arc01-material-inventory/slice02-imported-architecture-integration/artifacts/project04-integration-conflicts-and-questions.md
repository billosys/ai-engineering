# Project04 Integration Conflicts and Questions

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice02-imported-architecture-integration
artifact: project04-integration-conflicts-and-questions
artifact-status: slice integration evidence
created-on: 2026-09-01
source-files-edited: false
```

## Purpose

This artifact records conflicts, compatibility obligations, and Arc02 decision
inputs created by integrating Project02 component architecture, Project03
method-skill planning, Slice01 source inventory, and Project04's direction:
`docs/` should become user-facing documentation while `knowledge/` should hold
raw and derived knowledge-library substrate and skill source material.

## Project02 and Project04 Tensions

| Tension | Evidence | Risk | Arc02 question |
|---------|----------|------|----------------|
| Top-level component root plan versus `knowledge/` as substrate | Project02 plans roots such as `engineering-methods/`, `project-management/`, and `work-verification/`; Project04 plans `knowledge/` as skill/source substrate. | Framework components may become top-level peers to `docs/` and `knowledge/`, weakening the library model. | Should framework component source roots live at repository top level, under `knowledge/`, under a new framework family root, or behind wrapper docs? |
| Current `docs/` contains framework source, not just user docs | Slice01 classifies many `docs/` files as framework/operational source or method material. | Moving all docs to user-facing prose would bury source-like framework material unless it gets a new source root. | Which current `docs/` files move, remain, or become wrapper doc pages pointing to skill/source roots? |
| `engineering-methods` owns source/package/release gates | Project02 accepted this as a component responsibility. | Gate prose could be stranded in README, Makefile help, or validation scripts after Project04 moves. | Where does reusable gate guidance live, and what docs page, README section, or skill route points to it? |
| Ontology critique placement is accepted in Project02 | Project02 places ontology critique under `engineering-methods/guides/05-component-boundary-analysis.md`. | Project04's ontology rubric could be mistaken for a new standalone ontology component. | Does Arc02 preserve ontology critique as `engineering-methods` guidance while Slice03 develops only a classification instrument? |
| Version-history policy spans components | Project02 requires each component `SKILL.md` plus sibling `version-history.md`. | Directory moves can lose history if treated as simple cleanup. | Does the target layout require every skill or component root to have sibling version history, including method skills? |
| README wayfinding becomes more complex | Project02 wants composed and standalone routes; Project04 wants `docs/` as end-user documentation. | README, `docs/`, and skill entrypoints can duplicate or contradict routes. | Which reader mode belongs in README, which belongs in `docs/`, and which belongs in `SKILL.md` route tables? |

## Project03 and Project04 Tensions

| Tension | Evidence | Risk | Slice03 or Arc02 question |
|---------|----------|------|---------------------------|
| `concept-card-method` planned under `knowledge/concept-card-method/` | Project03 Arc05 source layout plan. | This supports `knowledge/` as source substrate, but Project04 still has not accepted the final directory contract. | Arc02 must decide whether method skills belong under `knowledge/`; Slice03 owns topology classification. |
| Method skill may be atomic or composite | External ontology rubric says method skills can be atomic or composite; Project03 has extraction, validation, memory admission, graph/CQ, and CCDP-adjacent concerns. | Premature classification could force the wrong package or route shape. | Slice03 owns topology classification using evidence, not the word "method". |
| Thin `SKILL.md` plus guides is accepted for Project03 | Project03 Arc04 accepts a thin entrypoint and focused guides. | Project04 may overgeneralize this into a rule for every skill or ignore it for framework components. | Arc02 should preserve the pattern as a strong candidate for method skills while checking whether composite framework components need a different route table shape. |
| Validation surfaces are documentary before validator-code | Project03 separates deterministic structural checks, semantic audit, human/operator review, and deferred runtime. | Project04 may confuse validation documentation with executable release gates. | Arc02 should reserve source homes for validation docs; later arcs decide executable validators and package gates. |
| Memory admission is a method lifecycle gate | Project03 accepts memory admission guidance but defers memory runtime. | Memory admission could be conflated with repository memory runtime or Project02 component ownership. | Keep memory admission as method guidance unless a future memory runtime project re-enters. |
| CCDP is adjacent but deferred as a service | Project03 is CCDP-compatible but defers CCDP service behavior; Project02 keeps CCDP a separate protocol distribution. | `concept-card-method` could be misplaced under `protocols/` or CCDP could be pulled into skill packages. | Preserve CCDP separation and describe concept-card method as CCDP-adjacent only. |

## Compatibility Obligations

Arc02 and later implementation planning must preserve these surfaces:

| Surface | Compatibility obligation |
|---------|--------------------------|
| `README.md` | Keep reader modes clear: source checkout, generated zip, unzipped/install, installed skill, and CCDP protocol distribution. |
| `SKILL.md` | Preserve the `collaboration-framework` daily-driver composer, thin entrypoint routing where accepted, and installed-skill route wording for cross-component use. |
| Package roots | Decide whether source roots and generated package roots match; preserve generated package validation once packages exist. |
| Package-local links | Prefer package-local links inside generated packages; use installed-skill route wording across package roots. |
| `package-path-exceptions.tsv` | Add narrow exceptions only for intentional source-only, provenance, external URL, example-project path, or checker false-positive cases. |
| `AGENTS.md` and `CLAUDE.md` | Preserve workflow instructions, planning/source checkout distinction, and `CLAUDE.md` symlink compatibility intent. |
| CCDP separation | Keep `protocols/ccdp/`, `ccdp.zip`, `make ccdp-package`, and `make check-ccdp-package` separate from installable skill packages unless a separate protocol decision reopens that policy. |
| Generated zips | Treat generated archives as validation evidence after source/package edits, not as planning artifacts to commit by default. |

## Concrete Arc02 Decision List

Arc02 directory contract decisions needed:

| Decision needed | Options Arc02 should test | Required preservation or re-entry condition |
|-----------------|---------------------------|--------------------------------------------|
| Framework component source root | Top-level component roots; `knowledge/<component>/`; a framework family root; wrapper docs over source roots. | Must preserve accepted Project02 component names, roles, composer behavior, and version histories. Re-enter Project02 architecture only if the directory contract cannot preserve accepted roles. |
| Current `docs/` framework material | Move into skill/component roots; remain as source docs; become wrapper docs; split source from public docs. | Must preserve source provenance and package-local links. Re-entry condition: source history or user-facing links cannot be preserved. |
| `docs/` public documentation contract | README-only summary; `docs/` pages by material category; generated docs from skill roots; hybrid. | Must keep `docs/` as user-facing explanation if Project04 retains that project direction. Re-entry condition: source material must remain in `docs/` for package validation. |
| Method skill source root | `knowledge/concept-card-method/`; method family under `knowledge/`; separate top-level method root. | Must preserve Project03 planning facts and avoid claiming the package exists before implementation. |
| Atomic and composite skill source roots | Same root family under `knowledge/`; separate composite/framework roots; package roots independent of source roots. | Slice03 owns topology classification before this becomes final. |
| Package root relationship | Generated package root equals source root; generated package root equals frontmatter name; selected-file package from mixed sources. | Must preserve `make check-skills`, `make check-package-paths`, generated zip root checks, and installed route wording. |
| Wrapper doc policy | Wrapper page per moved source; README route only; redirect-style migration note; no wrapper. | Must preserve old source path recognition where users and package exceptions depend on it. |
| Package-path exception policy | Zero exceptions after repair; narrow expiring exceptions; accepted warnings with rationale. | Must run package-path checks after generated zips exist and must not use exceptions to hide broken package-local links. |
| CCDP placement | Keep under `protocols/ccdp/`; add docs wrapper; cross-link from method skills; package with skills. | Preserve separate protocol distribution unless a new CCDP package policy explicitly reopens it. |
| Validation docs and executable validators | Documentation under guides; scripts under `scripts/`; package validation under Makefile; future runtime project. | Re-enter only when a source implementation accepts executable validator-code scope and tests. |

## Slice03 Inputs

Slice03 owns skill kind and topology classification. Inputs handed forward:

- `collaboration-framework`: accepted composite framework/operational anchor.
- `engineering-methods`: framework/operational component with method and
  gate ownership; possible source-home stress case.
- `concept-card-method`: method skill edge case with thin `SKILL.md`,
  focused `guides`, validation, memory admission, and CCDP-adjacent evidence.
- Current domain/tooling skills under `knowledge/`: candidate atomic anchors,
  especially Rust.
- Current `knowledge/biome/`: multiple entrypoints in one source root,
  useful for topology and package-root testing.
- External rubric: input, not accepted taxonomy.

## Re-Entry Conditions

Reopen or escalate decisions only when one of these conditions appears:

- Arc02 cannot preserve Project02 accepted component roles under any coherent
  directory contract.
- Package-local links cannot be repaired without broad exceptions.
- `collaboration-framework` composer behavior would be broken by source-root
  placement.
- Project03 `concept-card-method` would be described as implemented or
  released before source implementation exists.
- CCDP separation cannot be preserved by README, package, or directory
  wording.
- Source provenance or component version-history cannot survive the planned
  moves.

## Silent-Drop Check

Scope specified for Slice02:

- integrate imported Project02 and Project03 materials;
- consume Slice01 inventory and the external rubric as inputs;
- record Project02 accepted facts, hypotheses, constraints, conflicts, and
  open question rows;
- record Project03 method-skill and concept-card-method inputs;
- provide concrete Arc02 directory contract questions;
- avoid source edits and avoid final topology or directory decisions.

Scope delivered by these artifacts:

- Project02 accepted facts, implementation-plan hypotheses, compatibility
  obligations, and Slice03 topology inputs are separated in
  `imported-architecture-evidence-map.md`.
- Every project-level artifact is listed in `prior-proposal-register.md`.
- Conflicts, compatibility obligations, Arc02 decisions, Slice03 inputs, and
  re-entry conditions are recorded here.
- No source checkout files were edited.
