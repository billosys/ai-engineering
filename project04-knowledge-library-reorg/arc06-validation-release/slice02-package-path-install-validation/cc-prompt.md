# CC Prompt: Project04 Arc06 Slice02

You are CC working in Project04 Expedited Mode.

## Context

Arc06 Slice01 is verified-closed. It found the installable skill package path
green enough to proceed, but it did not run the isolated install smoke test.
It also confirmed that CCDP package freshness remains a separate blocker for
Slice03.

Your slice is:

`project04-knowledge-library-reorg/arc06-validation-release/slice02-package-path-install-validation`

Use the source checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Use the planning checkout:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

## Required Reading

Read these before doing work:

- `project04-knowledge-library-reorg/project-plan.md`
- `project04-knowledge-library-reorg/ledger.md`
- `project04-knowledge-library-reorg/arc06-validation-release/arc-plan.md`
- `project04-knowledge-library-reorg/arc06-validation-release/ledger.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice02-package-path-install-validation/slice-plan.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice02-package-path-install-validation/ledger.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice01-validation-surface-inventory/cdc-verification.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice01-validation-surface-inventory/artifacts/package-install-command-matrix.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice01-validation-surface-inventory/artifacts/ccdp-freshness-repair-decision-map.md`

## Assignment

Complete Slice02 by validating the final installable skill package path and
isolated install behavior. Start read-only. If validation exposes a narrow
package/path/install defect, repair only the affected authorized source files
and commit that source change first with an explicit file list. If no source
repair is needed, create no source commit and say so explicitly.

Do not edit `protocols/ccdp/**`. Do not refresh CCDP assembled protocol output.
Do not treat `ccdp.zip` as an installable skill package or as current release
evidence.

Create these artifacts under this slice's `artifacts/` directory:

- `package-path-build-validation-report.md`
- `generated-package-inspection-report.md`
- `isolated-install-smoke-report.md`
- `package-warning-disposition.md`
- `slice03-ccdp-readiness-handoff.md`

Then update this slice's `ledger.md` and create `closing-report.md`.

## Validation Requirements

Required validation includes:

- source `git status --short --untracked-files=all` before work;
- source `git diff --check`;
- README/docs/SKILL local-link validation;
- `make check-skills`;
- `make check-package-paths`;
- `make all`;
- generated installable skill package inspection for the 12 expected
  installable skill zips;
- isolated install smoke test using a temporary `INSTALL_DIR`;
- installed skill root and `SKILL*.md` entrypoint inspection;
- generated zip/build artifact handling, confirming ignored outputs are not
  committed;
- CCDP handoff confirmation that `protocols/ccdp/**` and `ccdp.zip` remain
  outside Slice02 repair scope;
- planning `git diff --check`;
- all six Slice02 ledger verifier commands;
- final source and planning `git status --short --untracked-files=all`.

## Commit Requirement

If source repairs are required, commit the source repair first using only the
explicit affected source path list. Then commit the Slice02 planning packet
using only the explicit planning path list. Do not commit unrelated files and
do not commit generated zips or build outputs.

The planning commit must include both trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Report the source commit hash if one exists, the planning commit hash,
validation outcomes, install smoke result, and any Arc06 bubble-up items.
