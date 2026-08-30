# CC Prompt: Arc 04 Slice 01 Release Surface Audit

You are working on `/Users/oubiwann/lab/billosys/ai-engineering`.

This is Project 01, Arc 04, Slice 01:

```text
.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/
```

Read and follow:

- `.worktrees/planning/AGENTS.md`
- `.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `.worktrees/planning/project01-harmonise-paths/ledger.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/arc-plan.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/ledger.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/slice-plan.md`
- `.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/ledger.md`

## Assignment

Perform a diagnosis-only release/adoption surface audit. Do not edit source
files in the implementation checkout.

Create durable artifacts under:

```text
.worktrees/planning/project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/artifacts/
```

Required artifacts:

- `release-surface-inventory.md`
- `project-ledger-gap-map.md`
- `warning-release-disposition.md`
- `recommended-slice02-scope.md`
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

Evaluate:

- source-clone workflow visibility for collaboration framework, project
  management/SDLC docs, language skills, and CCDP;
- generated skill zip workflow visibility;
- unzipped/installed skill workflow visibility;
- CCDP package workflow visibility;
- Makefile help and target discoverability;
- package-path gate and CCDP package gate discoverability;
- whether any remaining warning class is release-blocking;
- what Project 01 ledger rows can close as-is versus what still needs source
  repair.

Update this slice's `ledger.md` as proposed-done with attested evidence, then
write `closing-report.md` that walks F-1 through F-8, inventories artifacts,
names implementation state, and includes `Bubble-up to Arc 04`.

Do not create `cdc-verification.md`; CDC owns that after independent
verification.

Before reporting back, run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|Artifacts|Bubble-up to Arc 04" project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/closing-report.md
```

Report:

- whether Slice 02 should be a repair slice, acceptance-prep slice, or no-op;
- the exact implementation/planning files changed;
- verification results;
- any release-blocking findings.
