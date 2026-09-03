# CC Prompt: Arc04 Slice01 README and Docs Decomposition Map

You are CC working in Project04 Expedited Mode.

## Context

Project: `project04-knowledge-library-reorg`

Arc: `arc04-user-docs`

Slice: `slice01-readme-docs-decomposition-map`

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
- `arc04-user-docs/slice01-readme-docs-decomposition-map/slice-plan.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/ledger.md`
- `arc03-directory-reorg/closing-report.md`
- `arc03-directory-reorg/slice06-implementation-reconciliation/cdc-verification.md`

Use the source checkout only for read-only inspection in this slice.

## Task

Complete Arc04 Slice01 as a read-only decomposition and validation map for
README/docs work.

Create these artifacts:

- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/readme-source-surface-map.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/end-user-docs-decomposition-plan.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/arc04-doc-edit-sequence.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/public-language-boundary-register.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/docs-validation-command-inventory.md`

Update:

- `arc04-user-docs/slice01-readme-docs-decomposition-map/ledger.md`

Add:

- `arc04-user-docs/slice01-readme-docs-decomposition-map/closing-report.md`

Do not create `cdc-verification.md`; CDC owns that after your proposed close.

## Source Edit Policy

No source edits are authorized in this slice. Do not edit `README.md`,
`docs/*.md`, `knowledge/**`, `Makefile`, package-path exceptions, or generated
zips. Record `no source commit created`.

## Validation

Run and record:

- source `git status --short --untracked-files=all`
- planning `git diff --check`
- all six Slice01 ledger verifier commands
- final source and planning `git status --short`

## Planning Commit

After the artifacts, ledger update, and closing report are complete, commit
only the Slice01 planning close packet with an explicit file list:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/readme-source-surface-map.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/end-user-docs-decomposition-plan.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/arc04-doc-edit-sequence.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/public-language-boundary-register.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/docs-validation-command-inventory.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/ledger.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/closing-report.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc04 Slice01" \
  -- \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/readme-source-surface-map.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/end-user-docs-decomposition-plan.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/arc04-doc-edit-sequence.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/public-language-boundary-register.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/docs-validation-command-inventory.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/ledger.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice01-readme-docs-decomposition-map/closing-report.md
```

Include both required trailers in the commit message:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Report

Report:

- no source commit created;
- planning commit hash;
- ledger result;
- validation commands and outcomes;
- final source and planning checkout status;
- whether Slice01 is proposed-done pending CDC verification.
