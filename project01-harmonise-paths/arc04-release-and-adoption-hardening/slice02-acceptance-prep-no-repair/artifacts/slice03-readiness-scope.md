# Slice 03 Project-Close Readiness Scope

Recommended slice:

`slice03-project-close-readiness`

## Purpose

Run the final project-scale acceptance demonstration and prepare Project 01 for
close, without rediscovering the no-repair decision from Slice 02.

## Inputs

- Arc 04 Slice 01 `cdc-verification.md`
- Arc 04 Slice 01 release-surface audit artifacts
- Arc 04 Slice 02 `no-repair-decision.md`
- Arc 04 Slice 02 `final-acceptance-command-set.md`
- Arc 04 Slice 02 `arc-project-ledger-close-map.md`
- Project 01 `project-plan.md` and `ledger.md`
- Arc 04 `arc-plan.md` and `ledger.md`
- Implementation checkout `README.md`, `Makefile`,
  `package-path-exceptions.tsv`, `scripts/check-package-paths`,
  `scripts/check-ccdp-package`, and `protocols/ccdp/README.md`

## Required Work

- Reproduce the final acceptance command set from
  `artifacts/final-acceptance-command-set.md`.
- Capture every command output under the Slice 03 `artifacts/` directory.
- Inspect release-surface grep output for source clone, skill zip,
  unzipped/installed skill, and CCDP package workflow visibility.
- Walk Arc 04 rows A-2 through A-6 with reproduced evidence or a concrete
  blocker.
- Walk Project 01 rows P-2, P-3, P-4, and P-6 with project-scale reproduced
  evidence or a concrete blocker.
- State whether Arc 04 can close.
- State whether Project 01 can close after Arc 04 closure, or whether a
  remediation arc is required.

## Out of Scope

- Source edits.
- Checker or Makefile implementation changes.
- Broad warning burn-down.
- Release publication, tagging, or remote upload.
- Reopening Arc 01, Arc 02, or Arc 03.

## Re-entry to Repair

Stop and route a repair slice only if one of the no-repair re-entry conditions
fires:

- missing or ambiguous workflow guidance;
- hard skill-package path failure;
- CCDP package shape, README, Markdown path, or extracted rebuild failure;
- invalid or broad package-path exception policy;
- tracked source drift after accepted build/check commands;
- source/documentation change required to make project-close evidence honest.

## Expected Outcome

If the current evidence reproduces, Slice 03 should close as project-close
readiness with no source changes and should prepare Arc 04 for formal close.
