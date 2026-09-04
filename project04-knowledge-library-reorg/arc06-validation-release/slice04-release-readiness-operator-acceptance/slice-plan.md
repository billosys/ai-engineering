# Slice 04: Release Readiness and Operator Acceptance

```yaml
project: project04-knowledge-library-reorg
arc: arc06-validation-release
slice: slice04-release-readiness-operator-acceptance
status: verified-closed
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: optional-narrow-final-repair
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Reconcile final Project04 release readiness after package/install and CCDP
validation, prepare operator acceptance evidence, and make Arc06 ready for
formal arc close.

## Scope

In scope:

- Final source and planning checkout cleanliness.
- README/docs/SKILL local link validation.
- Final installable skill validation: `make check-skills`,
  `make check-package-paths`, `make all`, generated package inspection, and
  temporary install smoke evidence.
- Final CCDP validation: `make ccdp-package`, `make check-ccdp-package`, and
  `ccdp.zip` protocol-package inspection.
- Reconciliation of Arc06 Slice01 through Slice03 evidence.
- Operator acceptance readiness packet for Project04 final layout and
  remaining project-close gate.
- Arc06 close-readiness report.
- Narrow source repair only if final reconciliation exposes a release blocker.

Out of scope:

- Reopening Arc02 directory contract, Arc03 source moves, Arc04 documentation
  decomposition, Arc05 vocabulary decisions, or Slice02/Slice03 validation
  results without new evidence.
- Repackaging CCDP as an installable skill.
- Implementing `concept-card-method`.
- Broad prose rewrites unrelated to a final validation defect.
- Committing generated zips or `build/` artifacts.
- Closing Arc06 or Project04; CDC owns formal arc close after Slice04 is
  verified, and Project04 close still requires project-ledger acceptance.

## Expected Artifacts

- `artifacts/final-validation-reconciliation-report.md`
- `artifacts/operator-acceptance-readiness-packet.md`
- `artifacts/project04-close-readiness-report.md`
- `artifacts/generated-artifact-and-source-cleanliness-report.md`
- `artifacts/arc06-close-readiness-report.md`

## Verification Approach

CC should start from a clean checkout and reconcile the final validation story
across Arc06 Slices01-03. If validation exposes a narrow release blocker, make
only the minimal authorized repair and commit it first with an explicit file
list. If no source repair is needed, create no source commit and say so
explicitly.

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

## Exit Criteria

- Final validation reconciliation shows README/docs links, installable skill
  package/build/install behavior, and CCDP protocol-package behavior are green.
- Operator acceptance readiness packet clearly states what the operator can
  accept, what evidence supports it, and what remains for Project04 close.
- Project04 close readiness report maps Arc06 results to project ledger rows
  P-6 and P-7 without overclaiming operator acceptance.
- Generated artifact/source cleanliness report confirms source status and
  ignored-output handling.
- Arc06 close-readiness report states whether formal Arc06 close can proceed.
- Source and planning commits, if any, use explicit file lists and required
  trailers.
- Source and planning worktrees finish clean.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc06.

## CDC Close

Slice04 is verified-closed as of 2026-09-04. CDC reproduced all six ledger
rows, reran final README/docs/SKILL link validation, package/build/install
checks, CCDP package checks, and source/planning cleanliness checks, then
closed Arc06.
