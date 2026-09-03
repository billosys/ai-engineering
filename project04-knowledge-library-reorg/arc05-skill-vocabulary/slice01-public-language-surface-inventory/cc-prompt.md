# CC Prompt: Arc05 Slice01 Public Language Surface Inventory

You are CC working in Project04 Expedited Mode.

## Context

Project: `project04-knowledge-library-reorg`

Arc: `arc05-skill-vocabulary`

Slice: `slice01-public-language-surface-inventory`

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
- `artifacts/external-ontology-rubric-research.md`
- `arc01-material-inventory/slice03-skill-topology-classification/cdc-verification.md`
- `arc01-material-inventory/slice03-skill-topology-classification/artifacts/skill-kind-topology-decision-instrument.md`
- `arc01-material-inventory/slice03-skill-topology-classification/artifacts/skill-kind-topology-classification-matrix.md`
- `arc01-material-inventory/slice03-skill-topology-classification/artifacts/public-language-implications.md`
- `arc02-directory-contract/closing-report.md`
- `arc03-directory-reorg/closing-report.md`
- `arc04-user-docs/closing-report.md`
- `arc05-skill-vocabulary/arc-plan.md`
- `arc05-skill-vocabulary/ledger.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/slice-plan.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/ledger.md`

## Task

Produce a read-only inventory of current public wording and prior evidence for
Arc05's vocabulary work. Do not decide final vocabulary yet. Do not edit the
source checkout.

Inspect current source surfaces including:

- `README.md`
- `docs/*.md`
- `SKILL.md`
- `knowledge/*/SKILL*.md`
- `Makefile` and package-facing names/descriptions where relevant
- `protocols/ccdp/README.md`
- `templates/GUIDE.md`

Create these planning artifacts:

- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/current-public-language-surface-map.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/classification-evidence-synthesis.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/terminology-decision-question-register.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/source-edit-impact-map.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/arc05-validation-command-inventory.md`

Update:

- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/ledger.md`

Add:

- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/closing-report.md`

Do not create `cdc-verification.md`; CDC owns that after your proposed close.

## Source Edit Policy

This is a read-only planning slice. Do not edit source files and do not create
a source commit.

Source edits, accepted vocabulary, README/docs/SKILL wording changes, Makefile
changes, package list changes, package-path exception changes,
`concept-card-method` implementation, and CCDP repackaging are out of scope.

## Validation

Run and record:

- source `git status --short --untracked-files=all`
- planning `git diff --check`
- all six Slice01 ledger verifier commands
- final source and planning `git status --short`

Use focused source scans as needed to support the artifacts, but keep source
unchanged.

## Planning Commit

Commit only the Slice01 planning close packet with an explicit file list:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/current-public-language-surface-map.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/classification-evidence-synthesis.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/terminology-decision-question-register.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/source-edit-impact-map.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/arc05-validation-command-inventory.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/ledger.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/closing-report.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc05 Slice01" \
  -- \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/current-public-language-surface-map.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/classification-evidence-synthesis.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/terminology-decision-question-register.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/source-edit-impact-map.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/arc05-validation-command-inventory.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/ledger.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice01-public-language-surface-inventory/closing-report.md
```

Include both required trailers in the planning commit message:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Report

Report:

- planning commit hash;
- source status and confirmation that no source commit was created;
- artifacts created;
- ledger result;
- validation commands and outcomes;
- final source and planning checkout status;
- whether Slice01 is proposed-done pending CDC verification.
