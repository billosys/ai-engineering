# Implementation Input Question Map

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice01-source-surface-inventory
artifact: implementation-input-question-map
status: proposed-done
observed-on: 2026-08-31
```

## Purpose

This map routes implementation-planning questions to later Arc05 slices. It
preserves accepted Arc04 inputs from `v40-skill-architecture.md`,
`v40-architecture-decision-register.md`, and
`arc05-implementation-planning-handoff.md`. It uses the accepted Arc04
architecture as input: thin SKILL.md, reason to load, problem ownership,
dependency direction, package behavior, and maintenance ownership.

Slice01 remains out of scope for source edit work. It does not decide final
layout, does not edit source, and does not choose schema syntax, enum spelling,
validator implementation language, Makefile edits, package-list changes,
generated zips policy, release readiness, runtime, GraphRAG, graph database,
ontology database, memory runtime, CCDP service, or live extraction behavior.

## Slice02: Layout and Content Sequence

Route these questions to Slice02:

- What source layout should hold the v4.0 concept-card method skill:
  `knowledge/concept-card-method/`, a different `knowledge/` directory, or
  another source path?
- What content sequence should the thin SKILL.md use to route operators from
  reason-to-load through guides, templates, examples, validation, and package
  expectations?
- Which guide files are required for operator workflow, evidence lifecycle,
  review boundaries, and maintenance ownership?
- Which template files are source assets, and should templates live under
  `guides/`, a `templates/` directory, or another package-compatible path?
- Which example files are source assets, and what minimal examples are needed
  to demonstrate accepted Arc04 behavior without turning examples into a
  runtime?
- What cross-links should connect README.md, SKILL.md, guides, templates,
  examples, validation notes, and version history?
- What source-edit sequencing should implementation use so the package can be
  built and checked incrementally?

Slice02 should prepare source placement and content order. It should not close
schema validation, package target names, package list updates, generated zip
policy, release gates, or Project03 close.

## Slice03: Schema and Validation Scope

Route these questions to Slice03:

- What schema syntax should represent v4.0 concept-card fields while
  preserving accepted Arc04 semantics?
- What enum spelling should be used for evidence state, card type, validation
  state, review state, or other controlled values?
- How should source support and source span identity be represented so cited
  evidence remains durable and reviewable?
- Which validation candidates are source-format checks, package checks,
  semantic checks, or human review checks?
- What validator-code scope is appropriate, if any, and what should remain
  manual guidance?
- What tests are needed for schema examples, invalid examples, package-path
  behavior, and expected failure messages?
- Where are semantic review and human review boundaries documented so automated
  validation does not claim more than it can prove?

Slice03 should not decide Makefile target names, package list updates, README
library discoverability prose, release gates, generated zip publication, or
Project03 close.

## Slice04: Packaging, Discoverability, and Release Gates

Route these questions to Slice04:

- What README updates are required for library discoverability once the layout
  and validation surfaces are planned?
- What Makefile target names, if any, should build, validate, package, install,
  or clean the concept-card method skill?
- What package list changes are required for `INSTALL_ZIPS`,
  `ALL_SKILL_FILES`, or related source variables?
- How should package-path checks cover the generated package, and does
  `package-path-exceptions.tsv` need rows for intentional package transforms?
- Should generated zip output be added to existing generated archives behavior,
  and how should `build/` staging be used?
- What release gates should prove the package is installable, discoverable,
  package-path clean, and consistent with accepted Arc04 package behavior?
- What package updates are needed so templates, examples, schema guidance, or
  validation guidance are included only where intended?
- What version history and source version history obligations must be updated
  for SKILL.md, guides, README, validation docs, and package surfaces?

Slice04 should not reopen accepted Arc04 architecture and should not perform a
release. It should decide packaging and discoverability plans for the later
implementation slice.

## Slice05: Implementation Plan Synthesis

Route these questions to Slice05:

- How should Slice02, Slice03, and Slice04 decisions be synthesized into a
  complete implementation plan?
- What implementation-slice recommendations should be used to edit source in a
  separate implementation phase?
- Which decisions, risks, and non-goals belong in the deferral register?
- What evidence should become Project03 close input after implementation,
  package validation, and independent CDC verification?
- Does any later finding require re-sequencing Arc05, adding a slice, or
  correcting scope?

Slice05 should produce synthesis and Project03 close inputs. It should not
pretend that planning artifacts alone implement the v4.0 concept-card method.

## Cross-Slice Source Surfaces

The following source surfaces are shared planning inputs:

- `knowledge/`: candidate method-skill source home.
- `README.md`: repository-level library discoverability and package
  documentation.
- `Makefile`: package targets, skill checks, package-path checks, generated
  archives, generated zip behavior, and `build/` staging.
- `package-path-exceptions.tsv`: intentional exception register for package
  path validation.
- `AGENTS.md` and `CLAUDE.md`: standing source checkout instructions and
  compatibility symlink.
- `workbench/`: ignored source-area provenance for v3.2 concept-card method
  guides.

The later slices should keep current package behavior visible: generated
archives validate the packaged tree, ignored outputs are not source, and source
version history should be updated in the files that actually carry method
behavior.
