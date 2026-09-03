# CC Prompt: Project04 Arc06 Slice01

You are CC working in Project04 Expedited Mode.

## Context

Project04 has closed Arc01 through Arc05. The repository layout, README/docs
decomposition, and public skill vocabulary have landed. Arc06 is the final
validation/release-readiness arc.

Your slice is:

`project04-knowledge-library-reorg/arc06-validation-release/slice01-validation-surface-inventory`

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
- `project04-knowledge-library-reorg/arc06-validation-release/slice01-validation-surface-inventory/slice-plan.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice01-validation-surface-inventory/ledger.md`
- Arc05 close evidence, especially
  `project04-knowledge-library-reorg/arc05-skill-vocabulary/closing-report.md`
  and
  `project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/cdc-verification.md`

## Assignment

Complete Slice01 as a read-only validation inventory and gate plan. Do not edit
source files. Do not refresh `protocols/ccdp/**`. If a validation command
exposes a defect, record the later-slice authorization needed instead of
repairing it in this slice.

Create these artifacts under this slice's `artifacts/` directory:

- `current-validation-surface-map.md`
- `package-install-command-matrix.md`
- `ccdp-freshness-repair-decision-map.md`
- `source-edit-authorization-register.md`
- `release-readiness-risk-register.md`

Then update this slice's `ledger.md` and create `closing-report.md`.

## Validation and Inventory Requirements

Inventory or run the non-destructive final gates needed for Arc06:

- source `git status --short --untracked-files=all`;
- planning `git status --short --untracked-files=all`;
- source `git diff --check`;
- planning `git diff --check`;
- README/docs/SKILL local-link validation command or script;
- `make check-skills`;
- `make check-package-paths`;
- `make all`;
- generated skill package inspection commands;
- temporary install smoke-test command plan using an isolated install
  directory;
- `make ccdp-package` and `make check-ccdp-package` disposition, including the
  known stale assembled-spec failure if still present;
- all six Slice01 ledger verifier commands;
- final source and planning `git status --short --untracked-files=all`.

## Commit Requirement

After completing the slice, commit only the exact Slice01 planning packet using
explicit file lists. Do not commit unrelated files and do not commit generated
zips or build outputs.

The planning commit must include both trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Report the planning commit hash, validation outcomes, any source commit status
which should be `none`, and any Arc06 bubble-up items.
