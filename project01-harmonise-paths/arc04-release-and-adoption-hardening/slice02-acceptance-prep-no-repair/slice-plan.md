# Slice 02: Acceptance Prep and No-Repair Decision

```yaml
project: project01-harmonise-paths
arc: arc04-release-and-adoption-hardening
slice: slice02-acceptance-prep-no-repair
status: open
opened-on: 2026-08-29
artifact-home: artifacts/
depends-on:
  - slice01-release-surface-audit
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
```

## Capability

Convert the verified release-surface audit into an explicit no-repair decision
and a concrete project-close acceptance command set.

This is an acceptance-prep/no-op slice. It should not edit source files unless
it discovers a concrete defect that contradicts Slice 01's verified audit. If
that happens, stop and report the defect instead of broadening the slice into
implementation repair.

## Inputs

- `../slice01-release-surface-audit/cdc-verification.md`
- `../slice01-release-surface-audit/closing-report.md`
- `../slice01-release-surface-audit/artifacts/recommended-slice02-scope.md`
- `../slice01-release-surface-audit/artifacts/project-ledger-gap-map.md`
- `../slice01-release-surface-audit/artifacts/warning-release-disposition.md`
- `../arc-plan.md`
- `../ledger.md`
- `../../project-plan.md`
- `../../ledger.md`
- implementation checkout `README.md`
- implementation checkout `Makefile`
- implementation checkout `package-path-exceptions.tsv`
- implementation checkout `protocols/ccdp/README.md`

## Scope

Prepare Arc 04 for project-close readiness by documenting:

- the no-repair decision and its evidence;
- the final source/package acceptance command set for Slice 03 and Project 01
  close;
- how remaining Arc 04 rows A-2 through A-6 will close;
- how remaining Project 01 rows P-2, P-3, P-4, and P-6 will close;
- the exact re-entry conditions that would still force a repair slice.

## Out of Scope

- Source edits.
- Checker or Makefile implementation changes.
- Broad warning burn-down.
- Release publication, tagging, or remote upload.
- Project close itself.
- Arc 04 close itself.

## Artifact Requirements

Durable slice artifacts belong under:

```text
project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/artifacts/
```

Expected artifacts:

- `no-repair-decision.md`: evidence-backed decision that no source repair
  slice is required before project-close readiness.
- `final-acceptance-command-set.md`: exact commands to reproduce in Slice 03
  and at Project 01 close, including expected summary counts.
- `arc-project-ledger-close-map.md`: Arc 04 and Project 01 rows mapped to the
  final acceptance evidence.
- `slice03-readiness-scope.md`: concrete scope recommendation for Slice 03.
- command output captures for every verification command run.

## Verification Approach

Run from `/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
make help
make check-package-paths
make check-ccdp-package
scripts/check-package-paths --check-exceptions-only
make all
make ccdp-package
make ccdp
git diff --check
git status --short --branch --untracked-files=all
```

Inspect:

```sh
rg -n "source clone|zip|unzipped|install|package root|repo-only|provenance|check-package-paths|check-ccdp-package|ccdp.zip|protocol package" README.md Makefile package-path-exceptions.tsv protocols/ccdp/README.md scripts/check-package-paths scripts/check-ccdp-package
```

Run from `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

```sh
git diff --check
find project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|Artifacts|Bubble-up to Arc 04" project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/closing-report.md
```

## Exit Criteria

- No-repair decision is explicit, evidence-backed, and bounded by re-entry
  conditions.
- Final acceptance command set is named with expected summary counts.
- Arc 04 and Project 01 ledger rows are mapped to close evidence for the next
  slice/project close.
- Slice 03 project-close readiness scope is concrete.
- Implementation checkout remains free of tracked source edits.
- Durable artifacts live under this slice's `artifacts/` directory.
- The close report walks every ledger row and bubbles findings up to Arc 04.
