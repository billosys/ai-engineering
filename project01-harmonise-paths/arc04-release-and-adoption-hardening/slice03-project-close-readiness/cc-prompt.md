# CC Prompt: Arc 04 Slice 03 Project Close Readiness

You are working on `/Users/oubiwann/lab/billosys/ai-engineering`.

This is Project 01, Arc 04, Slice 03:

```text
.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/
```

Artifact home:

```text
.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/artifacts/
```

Read and follow:

- `.worktrees/planning/AGENTS.md`
- `.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `.worktrees/planning/project01-harmonise-paths/ledger.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/arc-plan.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/ledger.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/cdc-verification.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/cdc-verification.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/artifacts/final-acceptance-command-set.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/artifacts/arc-project-ledger-close-map.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/artifacts/slice03-readiness-scope.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/slice-plan.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/ledger.md`

## Assignment

Run the final project-scale acceptance demonstration and prepare Arc 04 and
Project 01 for formal close.

This is a close-readiness/no-repair slice. Do not edit source files unless one
of the documented re-entry conditions fires. If that happens, stop and report
the concrete defect instead of converting this slice into unplanned repair.

Create durable artifacts under:

```text
.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/artifacts/
```

Required artifacts:

- `final-acceptance-run.md`
- `release-surface-readiness.md`
- `arc04-ledger-readiness.md`
- `project01-ledger-readiness.md`
- `close-recommendation.md`
- command output captures for every verification command run

## Verification

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
- `make ccdp`: exits 0 and does not create tracked assembled-spec drift.

Document any count drift. Count drift is acceptable only if the command still
meets the row's acceptance condition and the drift is explained.

## Evidence to Produce

In `final-acceptance-run.md`, record every command result, expected summary
counts, observed summary counts, and any drift.

In `release-surface-readiness.md`, inspect whether the release/adoption surface
distinguishes:

- source clone use;
- generated/installable skill zips;
- unzipped/installed skill use;
- `ccdp.zip` protocol package use;
- repo-only/provenance/excluded material.

In `arc04-ledger-readiness.md`, walk Arc 04 rows A-2 through A-6 with evidence
or blockers.

In `project01-ledger-readiness.md`, walk Project 01 rows P-2, P-3, P-4, and
P-6 with evidence or blockers.

In `close-recommendation.md`, state:

- whether Arc 04 can proceed to formal close;
- whether Project 01 can close after Arc 04 closure;
- whether a repair slice or remediation arc is required;
- which re-entry condition fired, if any.

## Close Requirements

Update this slice's `ledger.md` as proposed-done with attested evidence for
F-1 through F-9.

Create `closing-report.md` in the slice directory. It must:

- name the implementation commit or current source state;
- inventory durable artifacts under `artifacts/`;
- walk every ledger row F-1 through F-9;
- include Bubble-up to Arc 04;
- say whether Arc 04 can proceed to formal close;
- say whether Project 01 can close after Arc 04 closure or needs remediation.

Do not create `cdc-verification.md`; CDC owns that after independent
verification. Do not create the formal Arc 04 or Project 01 closing report in
this slice; this slice prepares the evidence for those closes.

Before reporting back, run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|Artifacts|Bubble-up to Arc 04|Project 01 close" project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/closing-report.md
git diff --cached --check
```

Report:

- whether source remained unchanged;
- final acceptance command results and any count drift;
- whether Arc 04 can formally close;
- whether Project 01 can close after Arc 04 closure or needs remediation.
