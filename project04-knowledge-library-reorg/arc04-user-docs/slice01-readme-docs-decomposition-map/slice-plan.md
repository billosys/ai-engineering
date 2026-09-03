# Slice 01: README and Docs Decomposition Map

```yaml
project: project04-knowledge-library-reorg
arc: arc04-user-docs
slice: slice01-readme-docs-decomposition-map
status: verified-closed
opened-by: CDC
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Create the read-only decomposition map Arc04 needs before editing README or
focused end-user docs.

## Scope

In scope:

- Inventory current `README.md` sections and destination candidates.
- Inventory existing `docs/` surfaces after Arc03.
- Define the target focused end-user docs set.
- Sequence later README/docs edit slices.
- Establish Arc05 vocabulary boundaries so this arc can use provisional
  wording without finalizing public skill taxonomy.
- Define documentation validation commands and source/package surfaces to
  recheck after documentation edits.

Out of scope:

- Editing source `README.md` or `docs/*.md`.
- Moving source material between `docs/`, `knowledge/`, `templates/`, or
  `protocols/`.
- Finalizing skill-kind or atomic/composite public vocabulary.
- Changing package lists, package-path exceptions, or generated zips.

## Expected Artifacts

- `artifacts/readme-source-surface-map.md`
- `artifacts/end-user-docs-decomposition-plan.md`
- `artifacts/arc04-doc-edit-sequence.md`
- `artifacts/public-language-boundary-register.md`
- `artifacts/docs-validation-command-inventory.md`

## Verification Approach

CC will close the slice with planning artifacts only. No source commit should
be created for this slice.

Required validation includes:

- source `git status --short --untracked-files=all`;
- planning `git diff --check`;
- all six ledger verifier commands;
- final source and planning `git status --short`.

## Exit Criteria

- Current README source surface is mapped to keep/move/rewrite destinations.
- Target focused docs set is proposed with audience, purpose, and source
  material inputs.
- Later Arc04 edit slices are sequenced.
- Arc05 vocabulary boundaries are explicit.
- Documentation validation commands are inventoried.
- Source checkout remains untouched.
- CC commits the planning close packet using explicit file lists.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc04.

## CDC Close

Closed as verified on 2026-09-02. CDC reproduced all six ledger rows, verified
CC's planning commit scope and co-author trailers, confirmed no source commit
was created, and opened Slice02 as the first README/docs source-edit slice.
