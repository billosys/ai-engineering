# Project05 Package Surface Requirements

```yaml
project: project05-concept-card-skill
arc: arc01-readiness-and-scope-lock
slice: slice01-current-layout-reconciliation
artifact: project05-package-surface-requirements
status: cc-produced
date: 2026-09-06
```

## Purpose

This artifact states the package and source-surface requirements for
`document-extraction` and `concept-cards` against the current post-Project04
repository behavior.

## Current Package Contract

Evidence:

- `docs/building-and-installing.md` states every installable skill zip must
  contain exactly one root `SKILL.md`.
- `docs/building-and-installing.md` states standalone domain, method, and
  framework-component skills package their own `guides/` plus local support
  directories such as `templates/` or `examples/`.
- `Makefile` `pack_component_skill` stages root `SKILL.md`, sibling `guides/`,
  `version-history.md`, and optional sibling `templates/` and `examples/`.
- `scripts/check-package-paths` hard-fails missing root `SKILL.md`, nested
  `SKILL.md`, and unexpected `knowledge/` subtrees in standalone packages.
- `.github/workflows/release-skill-zips.yml` uploads assets derived from
  `make -s print-skill-zips`.

Project05 consequence:

- Use sibling support directories by default.
- Do not put templates, examples, validation reference, or support material
  under `guides/` merely for packaging.
- If Project05 needs a support directory not currently copied by
  `pack_component_skill`, update the package macro or add explicit package
  behavior rather than hiding the material under `guides/`.

## Required Source Roots

`document-extraction` should use:

```text
knowledge/document-extraction/
├── SKILL.md
├── version-history.md
├── guides/
├── templates/
└── examples/
```

Potential additional sibling directories, if accepted by the implementation
slice and package macro:

```text
knowledge/document-extraction/reference/
knowledge/document-extraction/validation/
```

`concept-cards` should use:

```text
knowledge/concept-cards/
├── SKILL.md
├── version-history.md
├── guides/
├── templates/
└── examples/
```

Potential additional sibling directories, if accepted by the implementation
slice and package macro:

```text
knowledge/concept-cards/reference/
knowledge/concept-cards/validation/
```

## Minimum `document-extraction` Package Surface

Required entrypoint:

- `knowledge/document-extraction/SKILL.md`
- frontmatter `name: document-extraction`
- concise description under `scripts/check-skill-description.sh` limit
- clear positive triggers, negative triggers, ownership boundary, route to
  `concept-cards`, guide map, and version-history pointer

Required guides should cover:

- load contract and routing;
- operator workflow and agent-direct workflow;
- PDF/Marker preparation;
- EPUB/pandoc preparation;
- HTML and converted Markdown preparation;
- media path normalization;
- structure mapping and splitting;
- locator model;
- manifests, validation reports, readiness reports, and caveats.

Required templates should cover:

- extraction manifest;
- structure map;
- locator map;
- media normalization report;
- validation/readiness report;
- caveat record.

Required examples should cover at least:

- PDF/Marker preparation report;
- EPUB/pandoc preparation report;
- prepared-source manifest consumed by downstream concept-card extraction.

## Minimum `concept-cards` Package Surface

Required entrypoint:

- `knowledge/concept-cards/SKILL.md`
- frontmatter `name: concept-cards`
- concise description under `scripts/check-skill-description.sh` limit
- clear positive triggers, negative triggers, ownership boundary, route to
  `document-extraction`, guide map, and version-history pointer

Required guides should cover:

- load contract and adjacent routing;
- operator workflow and extraction workflow;
- source-faithful extraction from prepared sources;
- re-extraction and preservation;
- evidence lifecycle;
- claims, source support, spans, and locators;
- relationship edges and competency questions;
- reconciliation;
- validation and verification boundaries;
- memory admission;
- maintenance and packaging.

Required templates should cover:

- concept card;
- claim and source support;
- source span or locator record;
- competency question;
- relationship edge;
- extraction run;
- validation result;
- verification result;
- reconciliation result;
- preservation decision;
- memory admission decision.

Required examples should cover at least:

- minimal card;
- claim-backed card;
- relationship edge;
- competency-question coverage;
- extraction-run trace from prepared source;
- reconciliation example;
- memory-admission example.

## Makefile Requirements

When source implementation lands, update `Makefile` to include:

- `document-extraction.zip` and `concept-cards.zip` in `SKILL_ZIP_NAMES`;
- `knowledge/document-extraction/SKILL.md` and
  `knowledge/concept-cards/SKILL.md` in `ALL_SKILL_FILES`;
- `.PHONY` entries for `document-extraction` and `concept-cards`;
- named targets for each package, reusing `pack_component_skill` or a small
  method-skill macro that preserves sibling support directories;
- help output for both package targets;
- `skills` aggregate coverage;
- install/uninstall coverage through `INSTALL_ZIPS` and `INSTALL_SKILLS`;
- release workflow coverage through unchanged `make print-skill-zips`.

If sibling `reference/` or `validation/` directories are needed, update the
package macro and `docs/building-and-installing.md` package-shape language in
the same implementation slice.

## Documentation Requirements

When source implementation lands, update:

- `README.md` live skill list;
- `docs/skill-library.md` domain groupings and package table entries;
- `docs/building-and-installing.md` command list if new explicit targets are
  added;
- any affected version-history files under each new skill source root.

Documentation must distinguish:

- live `document-extraction` and `concept-cards` skills;
- historical `source-preparation` and `concept-card-method` planning names;
- future reserved `ontology-engineering`;
- local repository validation versus public release publication.

## Validation Requirements

Minimum implementation validation:

- `git diff --check`;
- `make check-skills`;
- `make document-extraction`;
- `make concept-cards`;
- inspect both generated zip listings;
- `make check-package-paths`;
- install/uninstall smoke or an accepted narrower install check.

Expected zip shape:

- `document-extraction/SKILL.md`;
- `document-extraction/guides/**`;
- `document-extraction/version-history.md`;
- `document-extraction/templates/**` if templates exist;
- `document-extraction/examples/**` if examples exist;
- `concept-cards/SKILL.md`;
- `concept-cards/guides/**`;
- `concept-cards/version-history.md`;
- `concept-cards/templates/**` if templates exist;
- `concept-cards/examples/**` if examples exist;
- no nested `SKILL.md` files;
- no standalone-package `knowledge/` subtree.

## Generated Artifact Policy

Generated zips remain ignored artifacts under `target/skills/`. Implementation
arcs should build and inspect them for evidence but not commit them unless a
release owner explicitly changes repository policy.
