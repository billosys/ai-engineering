# Slice01 Plan: Package Targets And Support Directories

```yaml
project: project05-concept-card-skill
arc: arc05-packaging-docs-and-installability
slice: slice01-package-targets-and-support-directories
status: open
opened: 2026-09-10
```

## Goal

Wire `document-extraction` and `concept-cards` into the repository's Makefile
package surface so both skills build as generated zips and are included in the
aggregate build/install lists. Preserve their sibling support directories,
including `concept-cards/references/`, in the generated packages.

## In Scope

- Add package names to `SKILL_ZIP_NAMES`, `INSTALL_ZIPS`, aggregate targets, and
  `.PHONY` declarations as needed.
- Add Makefile targets for `document-extraction` and `concept-cards`.
- Adjust reusable package helpers so method/component-style support directories
  that exist under a skill root are copied, including `references/`.
- Ensure package/version gates can see the new generated packages.
- Update skill wording only when needed to remove "not packaged yet" claims
  that become false after this slice, while preserving docs/install smoke as
  later Arc05 work.
- Update affected version histories if source skill wording or package support
  changes are significant.

## Out Of Scope

- README/docs discoverability beyond wording required by source package claims.
- Isolated install smoke and final package-path reconciliation for Arc05.
- Runtime services, executable validators, JSON Schema, live-corpus extraction,
  graph/ontology databases, GraphRAG, CCDP services, or memory runtime work.

## Verification

- Build the two new target zips or run an aggregate build that includes them.
- Inspect the two generated zip listings for the expected support directories.
- Run `scripts/check-skill-description.sh` for any edited `SKILL.md`.
- Run `make check-skills`.
- Run `make check-skill-versions`.
- Run `git diff --check`.
- Check `git status --short --untracked-files=all` and commit only intended
  source files with explicit pathspecs.

## Exit Criteria

This slice exits when `target/skills/document-extraction.zip` and
`target/skills/concept-cards.zip` can be produced by Makefile targets and their
zip listings include the support directories required by the source skills.
Docs/discoverability and install-smoke proof may remain open for later Arc05
slices, but no source text may still say the skills are not packaged at all
after this slice lands.
