# CC Prompt: Project04 Arc06 Slice03

You are CC working in Project04 Expedited Mode.

## Context

Arc06 Slice01 and Slice02 are verified-closed. Installable skill package
builds, package-path checks, generated package inspection, and isolated install
smoke are green. The remaining Arc06 blocker is CCDP package freshness:
`make ccdp-package` and `make check-ccdp-package` have been failing because
`protocols/ccdp/composite-cognition-dispatch-protocol.md` is stale.

Your slice is:

`project04-knowledge-library-reorg/arc06-validation-release/slice03-ccdp-package-validation`

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
- `project04-knowledge-library-reorg/arc06-validation-release/slice03-ccdp-package-validation/slice-plan.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice03-ccdp-package-validation/ledger.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice01-validation-surface-inventory/artifacts/ccdp-freshness-repair-decision-map.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice02-package-path-install-validation/cdc-verification.md`
- `project04-knowledge-library-reorg/arc06-validation-release/slice02-package-path-install-validation/artifacts/slice03-ccdp-readiness-handoff.md`

## Assignment

Complete Slice03 by resolving CCDP package freshness and validating CCDP as a
standalone protocol package.

First reproduce the current CCDP package failure. If the failure is the known
stale assembled spec, run:

```text
make -C protocols/ccdp ccdp-rfc
```

Then inspect the source diff. If the only required repair is the refreshed
assembled protocol, commit that source change first using an explicit path
list. If evidence shows a different CCDP package/freshness defect, make only
the narrow authorized repair and record why.

Authorized source repair paths for this slice:

- `protocols/ccdp/composite-cognition-dispatch-protocol.md`
- `protocols/ccdp/**` only when required for CCDP freshness or package
  validation
- source `Makefile` CCDP targets only if the package target is proven
  defective
- `scripts/check-ccdp-package` only if the package validator is proven
  defective

Do not repackage CCDP as an installable skill. Do not commit generated
`ccdp.zip`, installable skill zips, or `build/` output.

Create these artifacts under this slice's `artifacts/` directory:

- `ccdp-freshness-repair-report.md`
- `ccdp-package-validation-report.md`
- `protocol-package-separation-report.md`
- `source-change-and-generated-artifact-report.md`
- `release-readiness-handoff.md`

Then update this slice's `ledger.md` and create `closing-report.md`.

## Validation Requirements

Required validation includes:

- source `git status --short --untracked-files=all` before work;
- source `git diff --check`;
- reproduce `make ccdp-package` before repair or explain why already green;
- `make -C protocols/ccdp ccdp-rfc` if stale assembled output is present;
- inspect source diff for authorized CCDP files only;
- `make ccdp-package`;
- `make check-ccdp-package`;
- inspect generated `ccdp.zip` root and expected protocol package contents;
- `make check-skills`;
- `make check-package-paths`;
- generated artifact handling, confirming `ccdp.zip`, installable zips, and
  `build/` remain ignored and untracked unless a separate release process
  explicitly asks otherwise;
- planning `git diff --check`;
- all six Slice03 ledger verifier commands;
- final source and planning `git status --short --untracked-files=all`.

## Commit Requirement

If source repairs are required, commit the source repair first using only the
explicit affected source path list. Then commit the Slice03 planning packet
using only the explicit planning path list. Do not commit unrelated files and
do not commit generated zips or build outputs.

Every assistant-authored commit must include both trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Report the source commit hash if one exists, the planning commit hash,
validation outcomes, generated artifact handling, and any Arc06 bubble-up
items.
