# Project05 Current Source Surface Inventory

```yaml
project: project05-concept-card-skill
arc: arc01-readiness-and-scope-lock
slice: slice01-current-layout-reconciliation
artifact: project05-current-source-surface-inventory
status: cc-produced
source-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
date: 2026-09-06
```

## Purpose

This inventory records the current post-Project04 source, docs, packaging, and
validation surfaces that Project05 implementation arcs must use. It separates
live source facts from historical Project03 and early Project05 planning
assumptions.

## Baseline Status

Initial checkout status was clean for both worktrees:

- Source checkout command: `git status --short --untracked-files=all`
  from `/Users/oubiwann/lab/billosys/ai-engineering`; output empty.
- Planning checkout command: `git status --short --untracked-files=all`
  from `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`;
  output empty.

## Current Repository Orientation

Evidence:

- Source `README.md` describes the repository split: `docs/` for human-facing
  repository explanations, `knowledge/` for skill source and derived
  substrate, and `protocols/` for protocol distributions.
- Source `README.md` currently lists live domain/tooling skill packages, the
  live `scientific-methods` method skill, the composite
  `collaboration-framework`, reusable support material, and CCDP under
  `protocols/ccdp/`.
- Source `docs/skill-library.md` says each installable skill has an entrypoint
  file and package target, and lists the current installable skill zips by
  domain grouping.
- Source `docs/building-and-installing.md` documents generated package shape:
  every installable skill zip has one root `SKILL.md`; standalone domain,
  method, and framework-component skills package their own `guides/` plus
  sibling support directories such as `templates/` or `examples/`;
  `collaboration-framework.zip` is the only skill zip that bundles a
  `knowledge/` support subtree.

Current implication for Project05:

- `document-extraction` and `concept-cards` must be implemented as live
  `knowledge/<skill>/` source roots, not as files under `docs/` and not as
  planning-only artifacts.
- Source documentation should update human-facing discoverability without
  claiming release/publication beyond local repository gates.
- CCDP remains a protocol distribution/package, not a skill package.

## Current Skill Source Roots

Command evidence:

- `find knowledge -maxdepth 1 -type d | sort`
- `find knowledge -maxdepth 2 -name 'SKILL*.md' -o -name version-history.md | sort`

Current live source roots include:

- framework/operational components: `collaboration-framework`,
  `engineering-methods`, `project-management`, `work-verification`, `testing`,
  `code-auditing`, `agent-coordination`, and `contribution-style`.
- method skill: `scientific-methods`.
- domain/tooling skills: `rust`, `go`, `cpp`, `js`, `erlang`, `cobalt`,
  `design`, `tailwindcss`, `deno`, and `biome`.

Current absent roots:

- `knowledge/document-extraction/` is absent.
- `knowledge/concept-cards/` is absent.
- `knowledge/concept-card-method/` is absent.
- `knowledge/source-preparation/` is absent.

Current implication for Project05:

- Project05 must create new source roots for `document-extraction` and
  `concept-cards`.
- The old planned names `source-preparation` and `concept-card-method` must
  not be accidentally implemented as live package names.

## Representative Current Layouts

Representative source inspection:

- `knowledge/scientific-methods/` has `SKILL.md`, `version-history.md`,
  `guides/`, and `templates/`.
- `knowledge/project-management/` has `SKILL.md`, `version-history.md`,
  `guides/`, and `examples/`.
- `knowledge/work-verification/` has `SKILL.md`, `version-history.md`,
  `guides/`, and `templates/`.

Current implication for Project05:

- Sibling `templates/`, `examples/`, and similar support directories are
  package-compatible for standalone component/method packages.
- Project05 should not bury templates, examples, validation reference, or
  support documents under `guides/` merely to make package inclusion work.

## Current Package Surface

Evidence:

- `Makefile` defines `SKILL_ZIP_NAMES` and `INSTALL_ZIPS`.
- `make print-skill-zips` currently prints 20 installable skill zips:
  `collaboration-framework.zip`, seven framework-component zips,
  `scientific-methods.zip`, and eleven domain/tooling zips.
- `Makefile` includes `pack_skill` for domain/tooling-style packages and
  `pack_component_skill` for standalone framework component/method-style
  packages.
- `pack_component_skill` stages `SKILL.md`, `guides/`, `version-history.md`,
  and optional sibling `templates/` and `examples/`.
- `.github/workflows/release-skill-zips.yml` derives release-uploaded skill
  assets from `make -s print-skill-zips` after `make check-skills` and
  `make check-package-paths`.

Current implication for Project05:

- Add `document-extraction.zip` and `concept-cards.zip` to the Makefile skill
  zip list when the corresponding source roots exist.
- Add both `knowledge/document-extraction/SKILL.md` and
  `knowledge/concept-cards/SKILL.md` to `ALL_SKILL_FILES`.
- Add named targets, help text, `skills` aggregate entries, install/uninstall
  coverage, and release asset coverage through `print-skill-zips`.

## Current Validation Surface

Evidence:

- `scripts/check-skill-description.sh` validates frontmatter `description:`
  length for packaged skill entrypoints.
- `scripts/check-package-paths` validates generated skill zips, package-local
  Markdown paths, exception schema, and package shape.
- The package-shape validator hard-fails missing root `SKILL.md`, nested
  `SKILL.md` files, and unexpected `knowledge/` subtrees in standalone skill
  packages.
- `docs/building-and-installing.md` documents `make check-skills`,
  `make check-package-paths`, `git diff --check`, and source/generator
  artifact boundaries.

Current implication for Project05:

- Each new skill entrypoint must pass `make check-skills`.
- Package links must be written for generated package layout, or explicit
  package-path exceptions must be justified.
- Generated zips under `target/skills/` remain ignored build artifacts and
  should be inspected but not committed unless a release process changes that.

## Current Docs Surface

Evidence:

- `docs/skill-library.md` groups current installable skills under Programming
  Languages, Frontend, Software Engineering, Project Management, and Analysis
  And Inquiry.
- `README.md` names the repository's current live package categories and
  quick commands.
- `docs/building-and-installing.md` documents package targets and install
  behavior.

Current implication for Project05:

- `document-extraction` likely belongs in Analysis And Inquiry and Software
  Engineering or a future source/workflow grouping if introduced.
- `concept-cards` belongs in Analysis And Inquiry and should be described as a
  method skill for provenance-bearing concept cards, extraction,
  reconciliation, validation, and memory admission.
- README and docs should distinguish live skills from historical planned
  `concept-card-method` material when Arc05 lands packaging/docs changes.

## Source-Only Boundary

This slice made no source implementation edits. It inspected the source
checkout to produce Project05 planning artifacts.
