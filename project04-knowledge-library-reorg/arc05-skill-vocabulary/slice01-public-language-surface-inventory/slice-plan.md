# Slice 01: Public Language Surface Inventory

```yaml
project: project04-knowledge-library-reorg
arc: arc05-skill-vocabulary
slice: slice01-public-language-surface-inventory
status: verified-closed
opened-by: CDC
opened-on: 2026-09-03
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Inventory current public wording and prior evidence so Arc05 can decide skill
kind, topology, and public positioning without deriving its taxonomy
circularly from current repository layout.

## Scope

In scope:

- Inspect current public-language surfaces in `README.md`, `docs/*.md`,
  `SKILL.md`, `knowledge/*/SKILL*.md`, package metadata, and relevant planning
  artifacts.
- Synthesize Arc01 classification evidence, external ontology rubric input,
  Arc02/Arc03 source/package decisions, and Arc04 README/docs wording.
- Identify decision questions for accepted vocabulary, examples, avoid-list,
  source-edit scope, and re-entry conditions.
- Map which source surfaces may need edits in later Arc05 slices.
- Inventory validation commands needed for vocabulary source edits.

Out of scope:

- Editing source files.
- Accepting final vocabulary.
- Rewriting README, docs, `SKILL.md`, Makefile, package lists, or package-path
  exceptions.
- Implementing `concept-card-method`.
- Repackaging CCDP or changing package roots.

## Expected Artifacts

- `artifacts/current-public-language-surface-map.md`
- `artifacts/classification-evidence-synthesis.md`
- `artifacts/terminology-decision-question-register.md`
- `artifacts/source-edit-impact-map.md`
- `artifacts/arc05-validation-command-inventory.md`

## Verification Approach

This is a read-only planning slice. CC should create the five artifacts,
update this slice's `ledger.md`, add `closing-report.md`, and commit the
planning close packet with an explicit file list. Do not create
`cdc-verification.md`; CDC owns that after proposed close.

Required validation includes:

- source `git status --short --untracked-files=all`;
- planning `git diff --check`;
- all six Slice01 ledger verifier commands;
- final source and planning `git status --short`.

## Exit Criteria

- Current public wording is inventoried with concrete source paths.
- Prior evidence is synthesized without turning research input into accepted
  taxonomy.
- Decision questions for Slice02 are explicit and answerable.
- Later source-edit impact is mapped without authorizing edits.
- Validation commands for later source wording work are recorded.
- Source checkout remains untouched.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc05.

## CDC Close

Verified-closed on 2026-09-03. CDC reproduced all six ledger rows, checked the
planning commit scope and trailers, confirmed no source commit was created,
confirmed source/planning status, and recorded the verification in
`cdc-verification.md`.
