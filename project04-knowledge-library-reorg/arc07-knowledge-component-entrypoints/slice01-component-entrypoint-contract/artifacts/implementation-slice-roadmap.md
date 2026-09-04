# Implementation Slice Roadmap

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice01-component-entrypoint-contract
status: proposed-done
source_edits: none
```

## Sequence

This implementation slice roadmap proposes follow-on slices with explicit
source-edit authorization, commit scope, and sequence for entrypoint
relocation, guide layout, and reconciliation.

## Slice02: Collaboration Framework Entrypoint Relocation

Source-edit authorization:

- `SKILL.md`
- `knowledge/collaboration-framework/SKILL.md`
- `Makefile`
- `scripts/stage-skill-entrypoint` if package-only path transforms are needed
- `README.md`
- `docs/skill-library.md`
- `docs/knowledge-library-anatomy.md`
- `docs/repository-overview.md`
- `docs/collaboration-framework.md`
- `assets/packaging/path-exceptions.tsv`

Required mechanics:

- use explicit `git mv SKILL.md knowledge/collaboration-framework/SKILL.md`;
- update Makefile `ALL_SKILL_FILES` and `CF_FILES`;
- preserve generated package entrypoint as `collaboration-framework/SKILL.md`;
- repair public docs and package-path exceptions affected by the source
  entrypoint move;
- do not move component `docs/` directories in Slice02 unless required to make
  the entrypoint relocation coherent.

Commit scope:

- explicit source paths only;
- no generated zips;
- no `build/`;
- no unrelated component guide moves.

Validation:

- source `git diff --check`;
- README/docs/SKILL local-link validation;
- `make check-skills`;
- `make collab-framework`;
- generated `collaboration-framework.zip` inspection;
- source status clean after commit, ignoring generated outputs.

## Slice03: Component Guide Layout and Standalone Entrypoints

Source-edit authorization:

- named component roots:
  - `knowledge/agent-coordination/**`
  - `knowledge/code-auditing/**`
  - `knowledge/collaboration-framework/**`
  - `knowledge/contribution-style/**`
  - `knowledge/engineering-methods/**`
  - `knowledge/project-management/**`
  - `knowledge/testing/**`
  - `knowledge/work-verification/**`
- `Makefile`
- `README.md`
- `docs/ORIGINS.md`
- `docs/collaboration-framework.md`
- `docs/knowledge-library-anatomy.md`
- `docs/repository-overview.md`
- `docs/skill-library.md`
- `assets/packaging/path-exceptions.tsv`

Required mechanics:

- use explicit `git mv` path pairs from the source migration impact map;
- add concise component-root `SKILL.md` wayfinders/contracts;
- move long component documents to `guides/`;
- move `knowledge/project-management/docs/pm/*` directly to
  `knowledge/project-management/guides/`;
- keep `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`;
- keep `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`;
- remove emptied legacy `docs/` directories with `rmdir`;
- remove `knowledge/project-management/docs/pm` with `rmdir`;
- never use `rm -rf` for this cleanup.

Commit scope:

- explicit source paths only;
- include removed empty directory effects only through Git-tracked file moves
  and local `rmdir` cleanup;
- no generated zips;
- no broad prose rewrites.

Validation:

- source `git diff --check`;
- README/docs/SKILL/component-guide local-link validation;
- `make check-skills`;
- `make collab-framework`;
- `make check-package-paths`;
- generated package inspection;
- source status clean after commit, ignoring generated outputs.

## Slice04: Reconciliation, Package Validation, and Release Notes

Source-edit authorization:

- narrow link/package/release-note repairs discovered after Slice02/Slice03;
- `README.md`;
- `docs/**`;
- `Makefile`;
- `assets/packaging/path-exceptions.tsv`;
- `workbench/RELEASE-0.5.0.md` only if release-note reconciliation is explicitly
  required by the source cleanup and the slice authorizes forced add for the
  ignored workbench path.

Required mechanics:

- rerun final validation after all source moves;
- inspect generated package and install behavior;
- confirm generated zips remain under `target/skills`;
- confirm generated zips and `build/` are not tracked;
- run CCDP package validation or explicitly record why no CCDP command is
  required by unchanged protocol surfaces.

Commit scope:

- explicit source repair paths only, if any;
- explicit planning close paths only;
- no generated zips or `build/`;
- ignored release note path only if explicitly authorized.

Validation:

- source `git diff --check`;
- README/docs/SKILL local-link validation;
- `make check-skills`;
- `make collab-framework`;
- `make all`;
- `make check-package-paths`;
- generated package inspection;
- isolated install smoke;
- CCDP validation disposition, including `make ccdp-package` and
  `make check-ccdp-package` if release readiness requires a full final gate.

## No Additional Arc07 Slice Needed Now

The existing Arc07 slice breakdown remains sufficient:

- Slice01 decides the contract.
- Slice02 moves the collaboration-framework entrypoint.
- Slice03 implements component guide layout and component entrypoints.
- Slice04 reconciles validation and release notes.

No new slice or arc-plan change is required by this read-only decision packet.

