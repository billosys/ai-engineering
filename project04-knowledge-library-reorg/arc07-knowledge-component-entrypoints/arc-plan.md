# Arc 07: Knowledge Component Entrypoints and Guide Layout

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
status: active
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: per-slice
operating-mode: expedited
```

## Capability

Arc07 resolves the post-move cleanup surfaced by operator review after Arc06:
the collaboration-framework and component knowledge roots should no longer
carry source-clone `docs/` holdovers when the material is now itself the
knowledge substrate.

This arc decides and implements the component entrypoint contract, including
whether framework components become standalone `SKILL.md` entrypoints,
whether long documents remain guide material, how `project-management/docs/pm`
migrates to `project-management/guides/`, and how the top-level
`collaboration-framework` entrypoint moves from repository root to
`knowledge/collaboration-framework/` while preserving package/install
behavior.

## Inputs

- Operator re-entry request from 2026-09-04:
  - move top-level `SKILL.md` to `knowledge/collaboration-framework/`;
  - update Make targets/files accordingly;
  - remove stale `docs/` directory holdovers for `agent-coordination`,
    `code-auditing`, `collaboration-framework`, `contribution-style`,
    `engineering-methods`, and `project-management`;
  - decide whether these component materials should instead become per-root
    `SKILL.md` files;
  - migrate `knowledge/project-management/docs/pm/` to
    `knowledge/project-management/guides/`.
- Project04 Arc02 directory-contract evidence.
- Project04 Arc03 directory reorganization source edits.
- Project04 Arc05 accepted public vocabulary: skill kind is separate from
  topology, and standalone usability is not the same as package topology.
- Project04 Arc06 final validation evidence.
- Current source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`.

## Starting Position

CDC's starting recommendation is:

- `knowledge/collaboration-framework/SKILL.md` should become the canonical
  collaboration-framework entrypoint, and the package should still stage it as
  `collaboration-framework/SKILL.md`.
- Independently loadable framework components should use component-root
  `SKILL.md` files as concise wayfinders/contracts.
- Long current documents should not be blindly renamed to `SKILL.md`; most
  should move under `guides/` and be routed from the component `SKILL.md`.
- Current component documents accepted as root-level component material should
  move one level up out of their legacy `docs/` directories.
- Reusable forms should remain under `templates/`.
- `project-management/docs/pm/` should become `project-management/guides/`.
- Empty legacy `docs/` directories should be removed with `rmdir` after their
  files move; do not use `rm -rf` for this cleanup.
- Adjacent framework surfaces not named by the operator, especially
  `knowledge/testing/docs/` and `knowledge/work-verification/templates/`,
  must be inventoried and either kept out of scope or explicitly pulled into
  the same contract.

This is a planning hypothesis for Slice01 to test against the live source and
package behavior, not implementation authorization.

## Boundaries

In scope:

- Component entrypoint and guide-layout decision for the named framework
  component roots.
- Mechanical source moves and path repairs once authorized by a source-edit
  slice.
- Makefile packaging lists, `ALL_SKILL_FILES`, `CF_FILES`, package staging,
  and install behavior affected by the entrypoint move.
- README and `docs/` references affected by the moved entrypoints and guide
  paths.
- Package-path exception updates required by accepted path moves.
- Release-note updates for `workbench/RELEASE-0.5.0.md` if the source cleanup
  changes the release surface.

Out of scope:

- Broad rewrites of the collaboration-framework prose beyond routing,
  entrypoint, and path changes.
- Reopening Project02 component architecture, Project03 concept-card method
  architecture, or Project04 kind/topology vocabulary unless a concrete path
  conflict requires a recorded decision.
- Repackaging CCDP as an installable skill.
- Implementing `concept-card-method`.
- Committing generated zips or `build/` outputs.

## Slice Breakdown

### Slice 01: Component Entrypoint Contract and Migration Map

Status: open.

Scope: read-only inventory and decision packet for current framework component
roots, top-level `SKILL.md`, Makefile/package behavior, public docs links, and
adjacent component surfaces. Decide the target entrypoint/guide/template
contract and prepare implementation slices.

### Slice 02: Collaboration Framework Entrypoint Relocation

Status: planned.

Scope: move root `SKILL.md` to `knowledge/collaboration-framework/SKILL.md`,
update Makefile packaging so `collaboration-framework.zip` still exposes
`collaboration-framework/SKILL.md`, and repair direct README/docs/package
references affected by the move.

### Slice 03: Component Guide Layout and Standalone Entrypoints

Status: planned.

Scope: implement the accepted component-root contract from Slice01: remove
stale component `docs/` directory holdovers, migrate
`project-management/docs/pm/` to `project-management/guides/`, create or
preserve component `SKILL.md` entrypoints as accepted, move retained root-level
component documents one level up out of `docs/`, remove emptied legacy `docs/`
directories with `rmdir`, and repair package-local links.

### Slice 04: Reconciliation, Package Validation, and Release Notes

Status: planned.

Scope: run final README/docs/SKILL link validation, `make check-skills`,
`make collab-framework`, `make all`, `make check-package-paths`, package
inspection, install smoke, and release-note reconciliation after the component
entrypoint cleanup.

## Dependencies

- Slice01 must close before source moves because it decides which files become
  `SKILL.md`, which become guides, and which adjacent surfaces are in scope.
- Slice02 depends on Slice01's accepted top-level entrypoint relocation plan.
- Slice03 depends on Slice01's accepted component contract and Slice02's moved
  collaboration-framework entrypoint.
- Slice04 depends on all source moves from Slice02 and Slice03.

## Version History

### v1.0 - 2026-09-04

Opened Arc07 from operator re-entry after Arc06 acceptance-readiness review.
Planned a four-slice cleanup arc to settle component `SKILL.md` entrypoints,
remove stale `docs/` holdovers, migrate project-management guides, preserve
package/install behavior, and reconcile release notes.
