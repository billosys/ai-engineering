# Arc 03: Directory Reorganization Implementation

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
status: active
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: per-slice
operating-mode: expedited
```

## Capability

Arc03 executes the accepted Project04 directory reorganization in
implementation-sized slices while preserving history, minimizing prose changes,
and keeping package/build validation green after each source-edit slice.

Arc03 consumes Arc02's accepted directory contract, source/package root
contract, migration sequence, validation matrix, package-path exception policy,
and implementation handoff. It must keep mechanical moves separate from prose
rewrites and must not collapse Arc04 end-user docs or Arc05 public vocabulary
work into source-move slices.

## Inputs

- Project04 `project-plan.md` and project `ledger.md`.
- Arc02 close: `../arc02-directory-contract/closing-report.md`.
- Arc02 Slice04 handoff:
  - `../arc02-directory-contract/slice04-implementation-handoff/cdc-verification.md`
  - `../arc02-directory-contract/slice04-implementation-handoff/artifacts/arc03-readiness-packet.md`
  - `../arc02-directory-contract/slice04-implementation-handoff/artifacts/source-edit-slice-roadmap.md`
  - `../arc02-directory-contract/slice04-implementation-handoff/artifacts/arc02-decision-summary.md`
- Arc02 Slice02 and Slice03 artifacts as needed for accepted contract and
  validation detail.
- Source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`.

## Boundaries

In scope:

- Preflight source status, impact mapping, and validation command inventory.
- Source-edit slices that perform accepted mechanical moves from `docs/`,
  top-level selected-file framework material, and owner-local support material
  into accepted `knowledge/` roots.
- Top-level `SKILL.md` compatibility decision and implementation, with
  validated shim, replacement route, or explicit no-shim path.
- Package/list updates, package-local link repair, generated package
  inspection, and narrow exception handling required by accepted moves.
- Compatibility review for `README.md`, `SKILL.md`, `AGENTS.md`, `CLAUDE.md`,
  `Makefile`, `package-path-exceptions.tsv`, generated zips, and CCDP package
  separation where source edits touch those surfaces.

Out of scope:

- Deep README rewrite and focused end-user documentation prose; Arc04 owns
  that work.
- Final public skill-kind or atomic/composite vocabulary; Arc05 owns that work.
- Reopening the Arc02 accepted directory contract unless a source-edit slice
  records a concrete re-entry condition.
- Folding CCDP into installable skill packages.
- Broad package-path exceptions without operator approval.

## Expedited Mode

Project04 is operating in Expedited Mode as of 2026-09-02.

- CC prompts must instruct CC to commit after his changes, before CDC review,
  using explicit file lists for both `git add` and `git commit -- <paths>`.
- CDC commits after CDC review or planning changes and reports the result to
  the operator.
- When evidence is in place for a full slice close, close the slice rather than
  leaving it proposed-done.
- After a slice closes, open the next slice immediately and report the
  `cc-prompt.md` path relative to the project directory.
- After the last slice in the arc closes, continue to formal arc close, then
  open Arc04 and its first slice.

## Slice Breakdown

### Slice 01: Preflight Source Status and Impact Map

Status: verified-closed.

Scope: record the clean source baseline, live source surfaces, package targets,
generated package roots, validation commands, operator gates, and proposed
source-edit slice boundaries before any source files move.

Expected artifacts:

- `slice01-preflight-source-status-impact-map/artifacts/source-status-impact-map.md`
- `slice01-preflight-source-status-impact-map/artifacts/validation-command-inventory.md`
- `slice01-preflight-source-status-impact-map/artifacts/source-edit-authorization-register.md`

### Slice 02: Top-Level Compatibility Decision

Status: verified-closed.

Scope: select and implement the top-level `SKILL.md` compatibility path:
validated shim, replacement route, or explicit no-shim decision. This slice
must preserve `AGENTS.md` and `CLAUDE.md` compatibility behavior and run the
skill/framework validation gates that apply.

### Slice 03: Mechanical Framework Source Moves

Status: verified-closed.

Scope: mechanically move accepted collaboration-framework source material into
the accepted `knowledge/collaboration-framework/` root while preserving source
prose and package behavior.

### Slice 04: Component, Method, and Template Ownership Moves

Status: verified-closed.

Scope: mechanically place accepted Project02 component roots, authorized method
material, and owner-local templates under accepted `knowledge/` roots while
preserving top-level `templates/` only for cross-cutting support exceptions.

### Slice 05: Package, Link, and Edge-Case Reconciliation

Status: open.

Scope: synchronize package/list surfaces, repair package-local links, preserve
Biome multi-entrypoint behavior, preserve CCDP package separation, and record
only narrow package-path exceptions with required operator approval.

### Slice 06: Arc03 Implementation Reconciliation

Status: not open.

Scope: verify that accepted file moves, link updates, package roots,
compatibility surfaces, generated package behavior, and validation gates
compose before Arc03 closes.

## Dependencies

- Slice01 must close before source-edit slices because it establishes the clean
  baseline and exact validation surface.
- Slice02 must close before moving composer source material because top-level
  `SKILL.md` compatibility is a gating decision.
- Mechanical move slices must close before package/list reconciliation because
  package paths should be updated against real moved files.
- Package-local link repair must be attempted before package-path exceptions.
- Arc04 and Arc05 remain later arcs and must not be silently folded into Arc03.

## Version History

### v1.4 - 2026-09-02

Recorded Slice04 as verified-closed after CDC reproduced all six ledger rows
and reran source/package validation. Slice04 moved accepted specialist
component substrate into `knowledge/<component>/` owner roots, left
`concept-card-method` reserved, and preserved `templates/GUIDE.md` as a
cross-cutting support exception. Opened Slice05,
`slice05-package-link-edge-reconciliation`, with package-local link repair as
the first reconciliation rule before any package-path exception.

### v1.3 - 2026-09-02

Recorded Slice03 as verified-closed after CDC reproduced all six ledger rows,
reran source/package validation, and repaired one stale `AGENTS.md` framework
planning path in source commit `27cc255`. Opened Slice04,
`slice04-component-method-template-ownership-moves`, to move owner-specific
component, method, and template substrate out of the transitional
`knowledge/collaboration-framework/` root where mechanical moves can preserve
prose.

### v1.2 - 2026-09-02

Recorded Slice02 as verified-closed after CDC reproduced all six ledger rows
and reran the source-side skill/framework validation gates. Opened Slice03,
`slice03-mechanical-framework-source-moves`, to move the current selected-file
collaboration-framework payload as a transitional substrate under
`knowledge/collaboration-framework/` while preserving package behavior and
deferring the specialist component split to Slice04.

### v1.1 - 2026-09-02

Recorded Slice01 as verified-closed after CDC reproduced all six ledger rows.
Opened Slice02, `slice02-top-level-compatibility-decision`, as the compatibility
gate before any collaboration-framework composer source material moves.

### v1.0 - 2026-09-02

Opened Arc03 after Arc02 closed. Planned six implementation-sized slices and
opened Slice01, `slice01-preflight-source-status-impact-map`, as a
preflight-only baseline before source-edit slices.
