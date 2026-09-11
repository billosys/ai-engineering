# Slice02 Plan: Docs And Discoverability

```yaml
project: project05-concept-card-skill
arc: arc05-packaging-docs-and-installability
slice: slice02-docs-and-discoverability
status: open
opened: 2026-09-10
depends-on:
  - slice01-package-targets-and-support-directories
```

## Goal

Update repository README/docs surfaces so `document-extraction` and
`concept-cards` are discoverable as current method-skill packages with accurate
source entrypoints, build targets, generated zip names, support-directory
boundaries, and install-command routing.

## In Scope

- Update `README.md` if needed so the top-level repository overview no longer
  omits the new method skills or preserves stale planned-method wording.
- Update `docs/skill-library.md` so both skills appear as live installable
  method skills with correct source entrypoints and use cases.
- Update `docs/building-and-installing.md` so focused targets, aggregate
  builds, release-uploadable zip listing, and install behavior account for both
  new skills without claiming isolated install smoke has been performed.
- Update `docs/knowledge-library-anatomy.md` if needed so sibling support
  directories such as `templates/`, `examples/`, and explicitly packaged
  `references/` are described accurately.
- Remove or replace stale planned `concept-card-method`,
  `source-preparation`, or "future method skill" wording where Project05 has
  now landed `document-extraction` and `concept-cards`.

## Out Of Scope

- Makefile package wiring already closed in Slice01 unless a docs check
  exposes a narrowly necessary correction.
- `make check-package-paths`, isolated install smoke, installed-directory
  inspection, and final package/docs reconciliation remain Slice03 work.
- Runtime services, executable validators, JSON Schema, live-corpus
  extraction, graph/ontology databases, GraphRAG, CCDP services, memory
  runtime work, CI/release publishing, and old-root revival are out of scope.

## Verification

- Inspect changed README/docs surfaces for accurate method-skill listings,
  focused target names, generated zip names, support-directory wording, and
  no stale planned-method language.
- Run a targeted grep over README/docs for stale `concept-card-method`,
  `source-preparation`, `planned method`, `not packaged`, or equivalent wording
  and disposition any historical references explicitly.
- Run source Markdown link checks or another repository-native equivalent for
  changed docs.
- Run `make check-skills`.
- Run `make check-skill-versions`.
- Run `git diff --check`.
- Check `git status --short --untracked-files=all` and commit only intended
  source files with explicit pathspecs.

## Exit Criteria

This slice exits when the public repository docs present `document-extraction`
and `concept-cards` as live, current method-skill packages with accurate
package/build/install boundaries. Slice03 may still own package-path validation,
isolated install smoke, installed-content inspection, and final reconciliation,
but docs must no longer tell users that the implemented method-skill material
is merely planned.
