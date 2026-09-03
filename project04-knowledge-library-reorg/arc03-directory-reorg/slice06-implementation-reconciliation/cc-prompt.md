# CC Prompt: Arc03 Slice06 Implementation Reconciliation

You are CC working in Project04 Expedited Mode.

## Context

Project: `project04-knowledge-library-reorg`

Arc: `arc03-directory-reorg`

Slice: `slice06-implementation-reconciliation`

Source checkout:
`/Users/oubiwann/lab/billosys/ai-engineering`

Planning checkout:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Project directory:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg`

Start from source commit:
`9b6d5d83d9c8debd977609aa1118004e89e2c895`

## Required Reading

Read these files before working:

- `project-plan.md`
- `ledger.md`
- `arc03-directory-reorg/arc-plan.md`
- `arc03-directory-reorg/ledger.md`
- `arc03-directory-reorg/slice06-implementation-reconciliation/slice-plan.md`
- `arc03-directory-reorg/slice06-implementation-reconciliation/ledger.md`
- Slice01 through Slice05 `closing-report.md` and `cdc-verification.md` files.

Use Slice05's bubble-up as the starting checklist: final Arc03 composition must
cover moved source layout, package roots, compatibility surfaces, validation
gates, Biome dual packages, CCDP separation, generated archive boundaries, and
the unchanged narrow package-path exception policy.

## Task

Complete Arc03 Slice06 as an implementation reconciliation slice.

Create the required artifacts:

- `arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/moved-layout-composition-map.md`
- `arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/package-root-and-validation-composition.md`
- `arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/compatibility-and-edge-case-reconciliation.md`
- `arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/arc03-close-readiness-report.md`

Update:

- `arc03-directory-reorg/slice06-implementation-reconciliation/ledger.md`

Add:

- `arc03-directory-reorg/slice06-implementation-reconciliation/closing-report.md`

Do not create `cdc-verification.md`; CDC owns that after your proposed close.

## Source Edit Policy

This slice is primarily reconciliation and validation. If no source edits are
needed, explicitly record that no source commit was created.

If validation exposes a narrow source repair required for Arc03 composition,
make only that repair. Commit source edits first, before planning edits, using
explicit file paths in both staging and commit commands. Do not commit
generated zips.

Every assistant-authored commit must include both trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Validation

Run and record:

- source `git status --short --untracked-files=all`
- source `git diff --check`
- `make check-skills`
- `make collab-framework`
- `make all`
- `make check-package-paths`
- `make ccdp-package`
- `make check-ccdp-package`
- generated package inspection for `collaboration-framework.zip`,
  `biome-js-linter.zip`, `biome-linter.zip`, and `ccdp.zip`
- planning `git diff --check`
- final source and planning `git status --short`

If package-path validation reports warnings, record the hard failure count,
explicit exception count, and whether any warning requires operator action.

## Planning Commit

After the Slice06 artifacts, ledger update, and closing report are complete,
commit only the Slice06 planning files with an explicit file list:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/moved-layout-composition-map.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/package-root-and-validation-composition.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/compatibility-and-edge-case-reconciliation.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/arc03-close-readiness-report.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/closing-report.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc03 Slice06" \
  -- \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/moved-layout-composition-map.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/package-root-and-validation-composition.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/compatibility-and-edge-case-reconciliation.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/arc03-close-readiness-report.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice06-implementation-reconciliation/closing-report.md
```

Include the required co-author trailers in the commit message. If you had to
make a source commit, report both source and planning commit hashes.

## Report

Report:

- source commit hash, or `no source commit created`;
- planning commit hash;
- ledger result;
- validation commands and outcomes;
- final source and planning checkout status;
- whether Arc03 is ready for CDC verification and formal arc close.
