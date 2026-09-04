# Slice 02: Collaboration Framework Entrypoint Relocation

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice02-collaboration-framework-entrypoint-relocation
status: open
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Move the canonical collaboration-framework source entrypoint from repository
root `SKILL.md` to `knowledge/collaboration-framework/SKILL.md` while
preserving generated package behavior: `collaboration-framework.zip` must still
install with `collaboration-framework/SKILL.md` as its package entrypoint.

## Scope

In scope:

- Mechanical source move:
  - `SKILL.md` -> `knowledge/collaboration-framework/SKILL.md`.
- Makefile/package updates required by the relocated source entrypoint:
  - `ALL_SKILL_FILES`;
  - `CF_FILES`;
  - `make collab-framework`;
  - any narrow staging helper update needed to package the moved source file as
    root package `SKILL.md`.
- Direct source-reference repairs caused by the moved entrypoint in:
  - `README.md`;
  - `docs/skill-library.md`;
  - `docs/knowledge-library-anatomy.md`;
  - `docs/repository-overview.md`;
  - `docs/collaboration-framework.md`;
  - `docs/ORIGINS.md`, only if direct moved-entrypoint links or package
    validation require it.
- `assets/packaging/path-exceptions.tsv`, only for path-exception rows made
  stale by this relocation.
- Package-local link repairs required for the moved entrypoint.

Out of scope:

- Moving component `docs/` directories to `guides/`.
- Adding new component-root `SKILL.md` files other than the moved
  collaboration-framework entrypoint.
- Moving `knowledge/project-management/docs/pm/`.
- Moving templates.
- Broad prose rewrites unrelated to the entrypoint relocation.
- Updating release notes.
- Touching CCDP source or changing CCDP package semantics.
- Committing generated zips, `build/`, or other ignored build output.

## Expected Artifacts

- `artifacts/entrypoint-relocation-report.md`
- `artifacts/makefile-package-staging-report.md`
- `artifacts/source-reference-repair-report.md`
- `artifacts/validation-report.md`

## Verification Approach

CC should begin from clean source and planning checkouts. Implement the source
move first with an explicit `git mv`, then repair Makefile/package behavior and
direct source references. If the move exposes package-local link issues, repair
the narrow affected links or staging behavior before adding or widening
package-path exceptions.

The slice must prove both source and package views:

- source view: no repository-root `SKILL.md`; canonical source entrypoint is
  `knowledge/collaboration-framework/SKILL.md`;
- package view: generated `collaboration-framework.zip` still has package root
  `collaboration-framework/` and entrypoint
  `collaboration-framework/SKILL.md`.

If implementation requires any source file outside the authorized list in
`cc-prompt.md`, stop and bubble it up instead of expanding scope silently.

## Exit Criteria

- Source root `SKILL.md` is removed through `git mv`, not copied.
- `knowledge/collaboration-framework/SKILL.md` exists and is the canonical
  collaboration-framework source entrypoint.
- Makefile validation and packaging paths refer to the moved source entrypoint.
- `collaboration-framework.zip` still exposes `collaboration-framework/SKILL.md`
  as the package entrypoint.
- Direct README/docs links affected by the relocation are repaired.
- Package-path exceptions are repaired or explicitly preserved with rationale.
- Source commit is created with only authorized source files and both required
  co-author trailers.
- Planning artifacts, ledger, and `closing-report.md` are committed in a
  separate planning commit with both required co-author trailers.
