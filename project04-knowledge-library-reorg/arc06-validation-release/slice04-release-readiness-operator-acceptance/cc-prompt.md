# CC Prompt: Project04 Arc06 Slice04

You are CC working in Project04 Expedited Mode.

## Context

Arc06 Slice01, Slice02, and Slice03 are verified-closed. Installable skill
package/path/install validation is green, and the CCDP package freshness
blocker is resolved. Slice04 is the final Arc06 slice: reconcile release
readiness, prepare operator acceptance evidence, and make Arc06 ready for CDC
arc close.

Your slice is:

`project04-knowledge-library-reorg/arc06-validation-release/slice04-release-readiness-operator-acceptance`

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
- `project04-knowledge-library-reorg/arc06-validation-release/slice04-release-readiness-operator-acceptance/slice-plan.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice04-release-readiness-operator-acceptance/ledger.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice01-validation-surface-inventory/cdc-verification.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice02-package-path-install-validation/cdc-verification.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice03-ccdp-package-validation/cdc-verification.md`
- `project04-knowledge-library-reorg/arc05-skill-vocabulary/closing-report.md`

## Assignment

Complete Slice04 by reconciling final Project04 release readiness and
preparing operator acceptance evidence. Start read-only. If validation exposes
a narrow release blocker, repair only the affected authorized source file(s)
and commit the source change first with an explicit file list. If no source
repair is needed, create no source commit and say so explicitly.

Do not overclaim operator acceptance. Prepare the acceptance-readiness packet;
the operator or CDC project-close process owns final acceptance.

Create these artifacts under this slice's `artifacts/` directory:

- `final-validation-reconciliation-report.md`
- `operator-acceptance-readiness-packet.md`
- `project04-close-readiness-report.md`
- `generated-artifact-and-source-cleanliness-report.md`
- `arc06-close-readiness-report.md`

Then update this slice's `ledger.md` and create `closing-report.md`.

## Validation Requirements

Required validation includes:

- source `git status --short --untracked-files=all` before work;
- source `git diff --check`;
- README/docs/SKILL local-link validation;
- `make check-skills`;
- `make check-package-paths`;
- `make all`;
- generated installable skill package inspection;
- isolated temporary install smoke test;
- `make ccdp-package`;
- `make check-ccdp-package`;
- `ccdp.zip` protocol-package inspection;
- generated artifact handling, confirming generated zips and `build/` remain
  ignored and untracked unless a separate release process explicitly asks
  otherwise;
- planning `git diff --check`;
- all six Slice04 ledger verifier commands;
- final source and planning `git status --short --untracked-files=all`.

## Commit Requirement

If source repairs are required, commit the source repair first using only the
explicit affected source path list. Then commit the Slice04 planning packet
using only the explicit planning path list. Do not commit unrelated files and
do not commit generated zips or build outputs.

Every assistant-authored commit must include both trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Report the source commit hash if one exists, the planning commit hash,
validation outcomes, release-readiness verdict, operator acceptance readiness,
and any Arc06 or Project04 bubble-up items.
