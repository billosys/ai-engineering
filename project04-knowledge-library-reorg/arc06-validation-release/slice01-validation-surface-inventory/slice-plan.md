# Slice 01: Validation Surface Inventory and Gate Plan

```yaml
project: project04-knowledge-library-reorg
arc: arc06-validation-release
slice: slice01-validation-surface-inventory
status: verified-closed
opened-by: CDC
opened-on: 2026-09-03
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: none
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Inventory the final Project04 validation surfaces and produce the gate plan
for Arc06 source/package/install/protocol validation before any repair or
acceptance slice begins.

## Scope

In scope:

- Current source and planning checkout status.
- Final README/docs/SKILL local link and route validation surfaces.
- Make-backed source, package, and generated artifact validation commands.
- Generated skill package inspection surfaces.
- Temporary install smoke-test command options.
- CCDP freshness failure reproduction and repair/disposition options.
- Source-edit authorization boundaries for later Arc06 slices.
- Release-readiness risks and operator acceptance prerequisites.

Out of scope:

- Editing source files.
- Refreshing `protocols/ccdp/**`.
- Changing package lists, package roots, package-path exceptions, or generated
  zips.
- Implementing `concept-card-method`.
- Closing Arc06 or Project04.

## Expected Artifacts

- `artifacts/current-validation-surface-map.md`
- `artifacts/package-install-command-matrix.md`
- `artifacts/ccdp-freshness-repair-decision-map.md`
- `artifacts/source-edit-authorization-register.md`
- `artifacts/release-readiness-risk-register.md`

## Verification Approach

Slice01 is planning-only. CC should inspect current source and planning state,
run or inventory the final validation commands where non-destructive, and
record any command that is expected to fail because a later slice must
authorize repairs.

Required validation/inventory includes:

- source `git status --short --untracked-files=all`;
- planning `git status --short --untracked-files=all`;
- source `git diff --check`;
- planning `git diff --check`;
- README/docs/SKILL local-link validation command or script;
- `make check-skills`;
- `make check-package-paths`;
- `make all`;
- package inspection commands for generated skill zips;
- temporary install smoke-test command plan using an isolated install
  directory;
- `make ccdp-package` and `make check-ccdp-package` disposition, including the
  known stale assembled-spec failure if still present;
- all six Slice01 ledger verifier commands;
- final source and planning `git status --short --untracked-files=all`.

## Exit Criteria

- The validation surface map identifies every final Project04 gate needed for
  source, README/docs, package paths, package builds, generated package
  inspection, install smoke, CCDP package behavior, and operator acceptance.
- The package/install command matrix distinguishes commands that are green now
  from commands that require a later repair or acceptance decision.
- The CCDP freshness repair decision map states whether the stale assembled
  protocol remains present and what later slice authorization is required.
- The source-edit authorization register states which later Arc06 slices may
  edit source and which paths remain off limits.
- The release-readiness risk register names any remaining blockers, warnings,
  operator gates, or no-op confirmations.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc06.

## CDC Close

Verified-closed on 2026-09-03. CDC reproduced all six ledger rows, checked
CC's planning commit scope and required trailers, reran source/package/link
validation, confirmed installable package inspection, and reproduced the CCDP
freshness blocker as Slice03-owned re-entry.
