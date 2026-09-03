# source edit authorization plan

## Boundary

source-files-edited: false

This Slice02 decision packet authorizes a later Slice03 source wording
implementation only within the surfaces and constraints below. Slice02 itself
made no source edit and created no source commit.

## Slice03 Authorized Surfaces

Slice03 is authorized to edit these source surfaces for accepted public
vocabulary and positioning only:

- `README.md`
- `docs/repository-overview.md`
- `docs/skill-library.md`
- `docs/collaboration-framework.md`
- `docs/knowledge-library-anatomy.md`
- `docs/protocols.md`
- `docs/contributing.md`
- `docs/building-and-installing.md`
- top-level `SKILL.md`

The implementation purpose is narrow: replace provisional Arc05 caveats with
accepted public wording, add concise definitions where needed, preserve
docs/ versus knowledge/ routing, and align collaboration-framework,
domain/tooling, method, protocol distribution, support material, atomic, and
composite language.

## Package-Facing Authorization

package-facing edits are not authorized in Slice03 except for incidental
public prose inside top-level `SKILL.md`.

Do not edit:

- `Makefile`
- `package-path-exceptions.tsv`
- package target names
- `INSTALL_ZIPS`
- `ALL_SKILL_FILES`
- `CF_FILES`
- generated zips
- package root names
- knowledge/*/SKILL*.md frontmatter names/descriptions/categories

If Slice03 discovers that accepted vocabulary requires package metadata or
Makefile help changes, record a deferral or re-entry condition rather than
editing those surfaces.

## Excluded Surfaces

excluded surfaces:

- `knowledge/**` except the top-level `SKILL.md` route targets already linked
  from docs
- `protocols/ccdp/**`
- `templates/GUIDE.md`
- generated `*.zip`
- `package-path-exceptions.tsv`
- source moves, file renames, package-root changes, and package-list changes
- `concept-card-method` implementation
- CCDP repackaging as an installable skill

## Required Slice03 Validation Requirements

validation requirements for Slice03:

- source `git status --short --untracked-files=all` before edits
- source `git diff --check`
- accepted/avoided vocabulary scans over README.md docs SKILL.md
- README/docs route scan for docs/, knowledge/, protocols/, templates/,
  Makefile, and package links
- local Markdown link validation if any links change
- `make check-skills`
- `make check-package-paths` if top-level `SKILL.md` changes
- `make all` if top-level `SKILL.md` changes
- `make ccdp-package` and `make check-ccdp-package` only if docs/protocols.md
  changes CCDP route/package wording in a way that could affect validation
- planning `git diff --check`
- final source and planning `git status --short --untracked-files=all`

## No-Source-Edit Status for Slice02

no source edit occurred in Slice02. The source checkout was checked read-only
with `git status --short --untracked-files=all`, and no source commit was
created.
