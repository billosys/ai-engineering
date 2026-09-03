# CC Prompt: Arc05 Slice02 Accepted Vocabulary and Positioning Decision

You are CC working in Project04 Expedited Mode.

## Context

Project: `project04-knowledge-library-reorg`

Arc: `arc05-skill-vocabulary`

Slice: `slice02-accepted-vocabulary-positioning`

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
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/cdc-verification.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/current-public-language-surface-map.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/classification-evidence-synthesis.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/terminology-decision-question-register.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/source-edit-impact-map.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/arc05-validation-command-inventory.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/slice-plan.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/ledger.md`

## Task

Decide the accepted public vocabulary and positioning rules for Arc05. This is
a planning decision slice, not a source-edit slice.

Create these planning artifacts:

- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/accepted-public-vocabulary.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/example-and-edge-case-positioning.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/public-language-avoid-list.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/source-edit-authorization-plan.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/re-entry-condition-register.md`

Update:

- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/ledger.md`

Add:

- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/closing-report.md`

Do not create `cdc-verification.md`; CDC owns that after your proposed close.

## Decision Requirements

Answer the Slice01 question register explicitly. The resulting artifacts must
cover:

- which terms are public now;
- which terms are maintainer-facing only;
- which terms are deferred;
- which terms or claims are avoided;
- accepted examples and edge-case caveats;
- planned-surface language for `concept-card-method`;
- source-edit authorization for Slice03;
- re-entry conditions tied to concrete future evidence.

Keep the kind axis separate from topology. Do not infer public taxonomy from
folder placement alone.

## Source Edit Policy

This is a read-only planning decision slice. Do not edit source files and do
not create a source commit.

Source wording changes, README/docs/SKILL edits, Makefile changes, package list
changes, package-path exception changes, `concept-card-method` implementation,
generated zips, and CCDP repackaging are out of scope.

## Validation

Run and record:

- source `git status --short --untracked-files=all`
- planning `git diff --check`
- all six Slice02 ledger verifier commands
- final source and planning `git status --short`

Use focused source or planning scans as needed to support the artifacts, but
keep source unchanged.

## Planning Commit

Commit only the Slice02 planning close packet with an explicit file list:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/accepted-public-vocabulary.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/example-and-edge-case-positioning.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/public-language-avoid-list.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/source-edit-authorization-plan.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/re-entry-condition-register.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/ledger.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/closing-report.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc05 Slice02" \
  -- \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/accepted-public-vocabulary.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/example-and-edge-case-positioning.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/public-language-avoid-list.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/source-edit-authorization-plan.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/re-entry-condition-register.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/ledger.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/closing-report.md
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
- accepted/deferred vocabulary summary;
- ledger result;
- validation commands and outcomes;
- final source and planning checkout status;
- whether Slice02 is proposed-done pending CDC verification.
