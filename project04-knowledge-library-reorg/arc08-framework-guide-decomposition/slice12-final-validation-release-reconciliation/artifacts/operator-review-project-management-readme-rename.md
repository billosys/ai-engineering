# Operator Review Repair: Project-Management Guide README Rename

## Summary

During operator review of Arc08 Slice12, the operator identified
`knowledge/project-management/guides/PROJECT-MANAGEMENT.md` as a guide-set
index/wayfinder rather than an ordinary named guide. The operator approved
renaming it to `knowledge/project-management/guides/README.md`.

CDC performed this repair directly by operator authorization. This was not a
new CC implementation slice, and it does not constitute CDC verification or
formal Arc08 closure.

## Source Repair Commit

Source commit:
`c97b4e42e441b9bdd0a29a37ac1be508696ab9c0`

Source commit message:
`Rename project-management guide README`

Primary source change:

- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md` renamed to
  `knowledge/project-management/guides/README.md`.

Related route and history repairs updated live references in AGENTS, public
docs, collaboration-framework routes, project-management routes, component
histories, packaging lists, templates, and release notes.

## Validation Evidence

- `git diff --check`: pass.
- `git diff --cached --check`: pass before source commit.
- `make check-skills`: pass.
- Focused live-route local Markdown link validation after source commit:
  60 files checked, 417 local links checked, 0 missing.
- `make collab-framework`: pass.
- `make check-package-paths`: pass with 12 zips scanned, 208 packaged Markdown
  files scanned, 0 hard failures, 376 warnings, 3 explicit exceptions, and 656
  skipped external URLs.
- `collaboration-framework.zip` inspection: contains
  `collaboration-framework/knowledge/project-management/guides/README.md`.
- `collaboration-framework.zip` inspection: no
  `collaboration-framework/knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
  package entry remains.
- Source checkout status after source commit: clean.

## Disposition

The old filename remains only in historical rename notes and disposition text.
It is no longer a live route, package path, or required-load target.

Slice12 remains proposed-done pending CDC verification and operator acceptance.
Arc08 remains open for review until the operator requests formal closure.
