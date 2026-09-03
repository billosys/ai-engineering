# Arc04 Doc Edit Sequence

Date: 2026-09-02
Slice: Arc04 Slice01 README and docs decomposition map

## doc edit sequence

Arc04 should proceed in dependency order so README navigation never claims
focused docs that have not been created.

## Slice02: README Orientation Rewrite

source-files-edited: true

Purpose: rewrite `README.md` into a concise repository orientation.

Scope:

- Preserve title, badges, logo, license pointer, and repository identity.
- Replace long framework, skill library, build/install, repository layout,
  CCDP, and contribution sections with short orientation blocks.
- Link only to focused docs that already exist, or use clearly staged links if
  Slice02 also creates minimal placeholders by explicit plan.
- Preserve source/package commands that a new user needs immediately.

Validation:

- source `git status --short --untracked-files=all`
- `git diff --check`
- README self-anchor/link checks
- `make check-skills`
- documentation path grep for stale `docs/dev`, old framework doc paths, and
  moved template paths

Dependency: Slice02 consumes this Slice01 map and should not finalize Arc05
public vocabulary.

## Slice03: Focused Docs

source-files-edited: true

Purpose: create or update focused docs under `docs/`.

Expected docs:

- `docs/repository-overview.md`
- `docs/skill-library.md`
- `docs/collaboration-framework.md`
- `docs/knowledge-library-anatomy.md`
- `docs/building-and-installing.md`
- `docs/protocols.md`
- `docs/contributing.md`
- `docs/ORIGINS.md` link repair

Validation:

- source `git status --short --untracked-files=all`
- `git diff --check`
- docs links check
- README links check
- `make check-package-paths`
- `make ccdp-package`
- `make check-ccdp-package`

Dependency: Slice03 should follow the README target shape selected in Slice02
and preserve the `docs/` versus `knowledge/` boundary.

## Slice04: Documentation Link and Navigation Reconciliation

source-files-edited: true

Purpose: final validation and repair of README/docs navigation after source
documentation edits.

Scope:

- Check README links.
- Check docs links.
- Check package-path behavior if docs/package-facing references changed.
- Confirm `README.md`, `docs/`, `knowledge/`, `protocols/ccdp`,
  `templates/GUIDE.md`, `SKILL.md`, `Makefile`, `AGENTS.md`, and
  `CLAUDE.md -> AGENTS.md` remain coherent.
- Confirm generated zips are not committed.

Validation:

- source `git status --short --untracked-files=all`
- `git diff --check`
- README/docs link verification
- `make check-skills`
- `make check-package-paths`
- `make all`
- `make ccdp-package`
- `make check-ccdp-package`

Dependency: Slice04 closes Arc04 only after Slice02 and Slice03 source edits
land and CDC verifies their slice ledgers.
