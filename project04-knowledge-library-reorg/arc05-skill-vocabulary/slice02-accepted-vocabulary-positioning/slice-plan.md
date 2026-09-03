# Slice 02: Accepted Vocabulary and Positioning Decision

```yaml
project: project04-knowledge-library-reorg
arc: arc05-skill-vocabulary
slice: slice02-accepted-vocabulary-positioning
status: open
opened-by: CDC
opened-on: 2026-09-03
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Decide the accepted public vocabulary and positioning rules for Arc05 before
any README/docs/SKILL source wording implementation begins.

## Scope

In scope:

- Decide which skill-kind terms are public, maintainer-facing, deferred, or
  avoided.
- Decide which topology terms are public, maintainer-facing, deferred, or
  avoided.
- Decide accepted examples and edge-case language for Rust,
  `collaboration-framework`, CCDP, Biome, `templates/GUIDE.md`, and planned
  `concept-card-method`.
- Produce an avoid-list that prevents false collapses such as domain equals
  atomic or framework equals composite.
- Record re-entry conditions for future changes in entrypoints, package roots,
  Makefile targets, package-path exceptions, generated zip contents, or docs
  routes.
- Decide source-edit authorization boundaries for Slice03.

Out of scope:

- Editing source files.
- Implementing `concept-card-method`.
- Reopening Arc02 directory contract or Arc03 source moves.
- Changing package roots, Makefile package lists, package-path exceptions, or
  generated zips.
- Repackaging CCDP as an installable skill.

## Expected Artifacts

- `artifacts/accepted-public-vocabulary.md`
- `artifacts/example-and-edge-case-positioning.md`
- `artifacts/public-language-avoid-list.md`
- `artifacts/source-edit-authorization-plan.md`
- `artifacts/re-entry-condition-register.md`

## Verification Approach

This is a read-only planning decision slice. CC should create the five
artifacts, update this slice's `ledger.md`, add `closing-report.md`, and commit
the planning close packet with an explicit file list. Do not create
`cdc-verification.md`; CDC owns that after proposed close.

Required validation includes:

- source `git status --short --untracked-files=all`;
- planning `git diff --check`;
- all six Slice02 ledger verifier commands;
- final source and planning `git status --short`.

## Exit Criteria

- Accepted public vocabulary is recorded with clear public/deferred/internal
  status.
- Examples and edge cases are resolved or explicitly deferred with re-entry
  conditions.
- Avoid-list entries are concrete enough for Slice03 implementation checks.
- Slice03 source-edit authorization is explicit and scoped.
- Re-entry conditions are tied to concrete future evidence.
- Source checkout remains untouched.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc05.
