# CC Prompt: Arc 04 Slice 02 Acceptance Prep and No-Repair Decision

You are working on `/Users/oubiwann/lab/billosys/ai-engineering`.

This is Project 01, Arc 04, Slice 02:

```text
.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/
```

Read and follow:

- `.worktrees/planning/AGENTS.md`
- `.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `.worktrees/planning/project01-harmonise-paths/ledger.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/arc-plan.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/ledger.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/cdc-verification.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/artifacts/recommended-slice02-scope.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/slice-plan.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/ledger.md`

## Assignment

Perform an acceptance-prep/no-op slice. Do not edit source files unless you
find a concrete defect that contradicts the verified Slice 01 audit. If that
happens, stop and report the defect instead of broadening this slice into
repair.

Create durable artifacts under:

```text
.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/artifacts/
```

Required artifacts:

- `no-repair-decision.md`
- `final-acceptance-command-set.md`
- `arc-project-ledger-close-map.md`
- `slice03-readiness-scope.md`
- command output captures for every verification command run

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

Inspect the release/adoption surface with:

```sh
rg -n "source clone|zip|unzipped|install|package root|repo-only|provenance|check-package-paths|check-ccdp-package|ccdp.zip|protocol package" README.md Makefile package-path-exceptions.tsv protocols/ccdp/README.md scripts/check-package-paths scripts/check-ccdp-package
```

Document:

- why no source repair slice is required;
- the exact final acceptance command set for Slice 03 and Project 01 close,
  including expected summary counts;
- how Arc 04 rows A-2 through A-6 should close;
- how Project 01 rows P-2, P-3, P-4, and P-6 should close;
- what conditions would still force a repair slice;
- the concrete scope for Slice 03 project-close readiness.

Update this slice's `ledger.md` as proposed-done with attested evidence, then
write `closing-report.md` that walks F-1 through F-7, inventories artifacts,
names implementation state, and includes `Bubble-up to Arc 04`.

Do not create `cdc-verification.md`; CDC owns that after independent
verification.

Before reporting back, run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|Artifacts|Bubble-up to Arc 04" project01-harmonise-paths/arc04-release-and-adoption-hardening/slice02-acceptance-prep-no-repair/closing-report.md
```

Report:

- whether source remained unchanged;
- final acceptance command set selected;
- verification results;
- whether Slice 03 can open directly on project-close readiness.
