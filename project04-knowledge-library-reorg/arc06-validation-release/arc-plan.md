# Arc 06: Validation, Packaging, and Release Readiness

```yaml
project: project04-knowledge-library-reorg
arc: arc06-validation-release
status: active
opened-by: CDC
opened-on: 2026-09-03
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: per-slice
operating-mode: expedited
```

## Capability

Arc06 verifies that the reorganized repository works as a source checkout,
packaged skill library, installed Codex skill set, and CCDP protocol package.
It closes Project04 only after path checks, package checks, README/docs links,
installation behavior, CCDP package behavior, and operator acceptance are
reconciled against the final layout.

## Inputs

- Project04 `project-plan.md` and project `ledger.md`.
- Arc03 directory reorganization closure evidence.
- Arc04 README/docs guide and link-validation closure evidence.
- Arc05 vocabulary and wayfinding closure evidence.
- Current source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`.
- Known re-entry item: `make ccdp-package` reports stale assembled CCDP output
  and requires an authorized `protocols/ccdp/**` repair or explicit final
  disposition.

## Boundaries

In scope:

- Final source checkout status and whitespace checks.
- README/docs/SKILL local link validation and route checks.
- `make check-skills`, `make check-package-paths`, and `make all`.
- Generated package inspection for installable skills and CCDP packages.
- Installation smoke testing into a temporary install directory.
- CCDP package freshness repair or disposition, only in a slice that explicitly
  authorizes the required `protocols/ccdp/**` edits.
- Operator acceptance readiness and final project-close evidence.

Out of scope:

- Reopening Arc02 directory contract, Arc03 source moves, Arc04 documentation
  decomposition, or Arc05 public vocabulary decisions without new evidence.
- Repackaging CCDP as an installable skill.
- Implementing `concept-card-method`.
- Broad prose rewrites unrelated to validation defects.
- Committing generated zips or `build/` artifacts.

## Expedited Mode

Project04 remains in Expedited Mode.

- CC commits after changes, before CDC review, using explicit file lists.
- CDC commits CDC verification and planning updates after review.
- Closed slices automatically advance to the next slice.
- After the last Arc06 slice closes, CDC closes Arc06 and prepares Project04
  for project-level acceptance or project close, according to the project
  ledger.

## Slice Breakdown

### Slice 01: Validation Surface Inventory and Gate Plan

Status: open.

Scope: produce a read-only inventory of final validation surfaces, commands,
package/install checks, CCDP freshness options, and source-edit authorization
needed before Arc06 performs any repair or acceptance work.

Expected artifacts:

- `slice01-validation-surface-inventory/artifacts/current-validation-surface-map.md`
- `slice01-validation-surface-inventory/artifacts/package-install-command-matrix.md`
- `slice01-validation-surface-inventory/artifacts/ccdp-freshness-repair-decision-map.md`
- `slice01-validation-surface-inventory/artifacts/source-edit-authorization-register.md`
- `slice01-validation-surface-inventory/artifacts/release-readiness-risk-register.md`

### Slice 02: Package, Path, and Install Validation

Status: not-open.

Scope: run final package-path, package-build, generated-package inspection, and
temporary install smoke tests; make narrow authorized source repairs if Slice01
shows they are required.

### Slice 03: CCDP Package Freshness and Protocol Validation

Status: not-open.

Scope: resolve the CCDP stale assembled-spec re-entry item through an
explicitly authorized protocol refresh or an accepted final disposition, then
validate `make ccdp-package` and `make check-ccdp-package`.

### Slice 04: Release Readiness and Operator Acceptance

Status: not-open.

Scope: reconcile final README/docs/package/install/protocol evidence, prepare
operator acceptance material, and make Arc06 ready for close.

## Dependencies

- Slice01 must close before validation repair slices because it establishes the
  complete validation surface and authorization boundary.
- Slice02 depends on Slice01's package/install command matrix.
- Slice03 depends on Slice01's CCDP repair decision map and explicit
  authorization boundary.
- Slice04 depends on all final validation gates from Slice02 and Slice03.

## Version History

### v1.0 - 2026-09-03

Opened Arc06 after Arc05 closed. Planned four validation/release-readiness
slices and opened Slice01, `slice01-validation-surface-inventory`, as a
read-only inventory and gate plan before final source/package/install/protocol
validation repairs or acceptance work.
