# Slice 03: Project Close Readiness

```yaml
project: project01-harmonise-paths
arc: arc04-release-and-adoption-hardening
slice: slice03-project-close-readiness
status: open
opened: 2026-08-29
artifact-home: artifacts/
source-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
```

## Goal

Run the final project-scale acceptance demonstration for Project 01 and prepare
the remaining Arc 04 and Project 01 ledger rows for formal close.

This is a close-readiness slice, not a repair slice. Source edits are out of
scope unless the final acceptance commands expose a concrete defect that makes
the no-repair decision false.

## Background

Slice 01 audited the release/adoption surface and found no release-blocking
source gap. Slice 02 converted that finding into a CDC-verified no-repair
decision, a final acceptance command set, and an Arc/Project close map.

Slice 03 now needs to reproduce that acceptance set as project-scale evidence.
The key discipline is to avoid inherited composition: this slice must run the
commands and inspect the release surface again rather than closing rows only by
pointing back to earlier slice reports.

## In Scope

- Reproduce the final acceptance command set from Slice 02.
- Capture command outputs under this slice's `artifacts/` directory.
- Inspect release/adoption wording for source-clone, skill zip, unzipped skill,
  and CCDP package workflows.
- Walk Arc 04 rows A-2 through A-6 with reproduced evidence or a concrete
  blocker.
- Walk Project 01 rows P-2, P-3, P-4, and P-6 with reproduced project-scale
  evidence or a concrete blocker.
- Decide whether Arc 04 can proceed to formal close.
- Decide whether Project 01 can proceed to project close after Arc 04 closure,
  or whether a remediation arc is required.

## Out of Scope

- Source edits, unless a no-repair re-entry condition fires.
- Checker, Makefile, or README implementation changes.
- Broad warning burn-down.
- Release publication, tagging, pushing, or remote upload.
- Reopening Arc 01, Arc 02, or Arc 03.
- Creating CDC verification or the formal Arc 04/project closing reports.

## Required Artifacts

Create durable artifacts under `artifacts/`:

- `final-acceptance-run.md`: command-by-command results, expected counts, and
  any drift from the Slice 02 baseline.
- `release-surface-readiness.md`: source-clone, skill zip, unzipped skill, and
  CCDP package workflow visibility review.
- `arc04-ledger-readiness.md`: A-2 through A-6 evidence/disposition map.
- `project01-ledger-readiness.md`: P-2, P-3, P-4, and P-6 evidence/disposition
  map.
- `close-recommendation.md`: whether Arc 04 can close and whether Project 01
  can close after Arc 04, with any remediation/re-entry conditions.
- command output captures for every verification command run.

## Verification Commands

Run from `/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
git status --short --branch --untracked-files=all
make help
make check-package-paths
make check-ccdp-package
scripts/check-package-paths --check-exceptions-only
make all
make ccdp-package
make ccdp
rg -n "source clone|zip|unzipped|install|package root|repo-only|provenance|check-package-paths|check-ccdp-package|ccdp.zip|protocol package" README.md Makefile package-path-exceptions.tsv protocols/ccdp/README.md scripts/check-package-paths scripts/check-ccdp-package
git diff --check
git status --short --branch --untracked-files=all
```

Expected current summaries:

- `make check-package-paths`: 12 zips scanned, 171 Markdown files scanned,
  0 hard failures, 295 warnings, 3 explicit exceptions, 656 skipped external
  URLs.
- `make check-ccdp-package`: 42 Markdown files scanned, 14 package references
  checked, 91 protocol-syntax skips, 4 external URLs skipped, 0 shape errors,
  0 README errors, 0 Markdown path failures, and extracted assembly succeeds.
- `make ccdp-package`: produces `ccdp.zip` with one `ccdp/` root and 122
  entries.
- `make ccdp`: exits 0 and leaves no tracked assembled-spec drift.

Run from `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

```sh
git diff --check
find project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|Artifacts|Bubble-up to Arc 04|Project 01 close" project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/closing-report.md
git diff --cached --check
```

## Re-entry Conditions

Stop and report a repair need instead of soft-closing this slice if any of
these occur:

- `make check-package-paths` produces a hard failure;
- `make check-ccdp-package` produces a shape, README, Markdown path, or
  extracted rebuild failure;
- `package-path-exceptions.tsv` fails schema validation or hides a broad class
  rather than a narrow exception;
- `make ccdp` or package builds create tracked source drift;
- release/adoption wording is missing or ambiguous for source clone, skill zip,
  unzipped skill, or `ccdp.zip` workflows;
- Project 01 close would require a source or documentation change that cannot
  honestly close through evidence alone.

## Exit Criteria

- Every Slice 03 ledger row reaches `done`, `deferred`, or `no-op` with
  attested evidence.
- All required artifacts live under `artifacts/`.
- The implementation checkout remains unchanged, unless a re-entry condition
  was reported and the operator explicitly converted the slice to repair.
- `closing-report.md` walks F-1 through F-9, inventories artifacts, names the
  implementation state, and includes Bubble-up to Arc 04.
- The Bubble-up states whether Arc 04 can formally close and whether Project
  01 can close after Arc 04 closure.
