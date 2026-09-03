# CC Prompt: Arc04 Slice04 Documentation Link and Navigation Reconciliation

You are CC working in Project04 Expedited Mode.

## Context

Project: `project04-knowledge-library-reorg`

Arc: `arc04-user-docs`

Slice: `slice04-doc-link-navigation-reconciliation`

Source checkout:
`/Users/oubiwann/lab/billosys/ai-engineering`

Planning checkout:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Project directory:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg`

## Required Reading

Read these files before working:

- `project-plan.md`
- `ledger.md`
- `arc04-user-docs/arc-plan.md`
- `arc04-user-docs/ledger.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/cdc-verification.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/docs-validation-command-inventory.md`
- `arc04-user-docs/slice02-readme-orientation-rewrite/cdc-verification.md`
- `arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/readme-route-repair-evidence.md`
- `arc04-user-docs/slice03-focused-end-user-guide-set/cdc-verification.md`
- `arc04-user-docs/slice03-focused-end-user-guide-set/artifacts/docs-content-boundary-evidence.md`
- `arc04-user-docs/slice03-focused-end-user-guide-set/artifacts/readme-navigation-preservation.md`
- `arc04-user-docs/slice04-doc-link-navigation-reconciliation/slice-plan.md`
- `arc04-user-docs/slice04-doc-link-navigation-reconciliation/ledger.md`

## Task

Reconcile README/docs navigation and link behavior after the focused guide set
has landed. Validate local links, stale-route scans, Make-backed package gates,
and CCDP package gates. Repair only narrow README/docs defects if you find
them.

Create these planning artifacts:

- `arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/documentation-link-reconciliation-report.md`
- `arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/navigation-route-validation-evidence.md`
- `arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/package-and-build-validation-evidence.md`
- `arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/arc04-close-readiness-report.md`

Update:

- `arc04-user-docs/slice04-doc-link-navigation-reconciliation/ledger.md`

Add:

- `arc04-user-docs/slice04-doc-link-navigation-reconciliation/closing-report.md`

Do not create `cdc-verification.md`; CDC owns that after your proposed close.

## Source Edit Policy

Source edits are conditional. If no source edits are needed, record
`source commit: none` in the close evidence.

If source edits are needed, they are authorized only for narrow repairs in:

- `README.md`
- `docs/*.md`
- `docs/ORIGINS.md`

Do not edit `knowledge/**`, `Makefile`, `package-path-exceptions.tsv`,
`SKILL.md`, generated zips, or CCDP source files unless you stop and record an
operator gate. Do not finalize Arc05 vocabulary.

If source edits are made, commit them first, before planning edits, using
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
- targeted route checks:
  - `rg -n "\\[[^\\]]+\\]\\([^\\)]+\\)|https?://|docs/|knowledge/|protocols/|templates/|Makefile|package" README.md docs`
  - `rg -n "docs/dev|docs/design|CODE-AUDIT|AI-ENGINEERING|PROJECT-MANAGEMENT|SUBAGENT|LEDGER-DISCIPLINE|CONTRIBUTION-TICKET|templates/" README.md docs`
  - `find docs -maxdepth 2 -type f | sort`
  - `rg -n "^#{1,4} " README.md docs`
- file-existence validation for local Markdown links in `README.md` and
  `docs/*.md`; use a small script or equivalent command and record the method
  and result
- `make check-skills`
- `make check-package-paths`
- `make all`
- `make ccdp-package`
- `make check-ccdp-package`
- planning `git diff --check`
- all six Slice04 ledger verifier commands
- final source and planning `git status --short`

If a targeted route check still reports stale strings, record whether the
match is repaired historical context, a deliberate Arc05 deferral, or a
remaining defect.

## Source Commit

If no source edits are required, do not create a source commit. Record
`source commit: none` and the no-op rationale in the artifacts and closing
report.

If source edits are required, commit source edits with explicit paths. Example
shape only:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering add \
  README.md \
  docs/repository-overview.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering commit \
  -m "Reconcile Project04 documentation links" \
  -- \
  README.md \
  docs/repository-overview.md
```

Include the required co-author trailers in the source commit message. Adjust
the path list to exactly match every source file you edit.

## Planning Commit

After source validation, commit only the Slice04 planning close packet with an
explicit file list:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/documentation-link-reconciliation-report.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/navigation-route-validation-evidence.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/package-and-build-validation-evidence.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/arc04-close-readiness-report.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/ledger.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/closing-report.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc04 Slice04" \
  -- \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/documentation-link-reconciliation-report.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/navigation-route-validation-evidence.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/package-and-build-validation-evidence.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/artifacts/arc04-close-readiness-report.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/ledger.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice04-doc-link-navigation-reconciliation/closing-report.md
```

Include both required trailers in the planning commit message.

## Report

Report:

- source commit hash or `none`;
- planning commit hash;
- source files edited or no-source-edit rationale;
- ledger result;
- validation commands and outcomes;
- final source and planning checkout status;
- whether Slice04 is proposed-done pending CDC verification.
