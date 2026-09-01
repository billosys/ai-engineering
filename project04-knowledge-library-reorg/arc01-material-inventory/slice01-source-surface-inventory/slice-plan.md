# Slice 01: Source Surface Inventory

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice01-source-surface-inventory
status: open
opened-on: 2026-09-01
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
```

## Goal

Produce the first read-only evidence base for Project04 by inventorying the
live source checkout and classifying the repository's current material
surfaces. This slice answers: what exists today, what role does each surface
currently play, and which validation/package/compatibility surfaces will later
be affected by the docs/knowledge-library reorganization?

## Scope

In scope:

- Inspect the source checkout's current top-level layout and relevant files:
  `README.md`, `SKILL.md`, `AGENTS.md`, `CLAUDE.md`, `docs/`, `knowledge/`,
  `templates/`, `protocols/`, `Makefile`, `package-path-exceptions.tsv`,
  `scripts/`, `assets/`, `site/`, and `workbench/`.
- Inventory current docs and knowledge-library files by directory and role.
- Identify source/package/validation surfaces that reference these paths:
  Make targets, package file lists, generated zip behavior, package-path
  exceptions, README links, skill route text, and validation scripts.
- Produce durable planning artifacts under `artifacts/`.
- Flag early observations about atomic/composite skill topology only when they
  are directly visible from the source tree; final topology classification is
  Slice03.

Out of scope:

- Moving, deleting, renaming, or editing source files.
- Rewriting README or docs prose.
- Deciding final target homes for files.
- Classifying imported Project02/Project03 project-level artifacts beyond
  naming them as later Slice02 inputs.
- Finalizing atomic/composite terminology.

## Artifacts

Expected artifact home: `artifacts/`.

Expected artifacts:

- `artifacts/current-source-surface-map.md`
- `artifacts/material-role-classification.md`
- `artifacts/source-validation-surface-map.md`

## Verification Approach

Use read-only source checkout commands and planning-tree inspection. The
artifacts should cite concrete paths and, where useful, command outputs or grep
queries. The final close must show that every ledger row was satisfied by
evidence in the artifacts.

## Exit Criteria

- The live source checkout top-level and key subtree inventories are recorded.
- `docs/` and `knowledge/` files are classified by current role without
  deciding final target homes.
- The validation/package/link surfaces affected by future moves are mapped.
- Imported Project02/Project03 project-level artifacts are named as later
  inputs, but not substituted for source inventory.
- The slice produces the expected artifacts and no source files are edited.

## Version History

### v1.0 - 2026-09-01

Opened Slice01 as the read-only source-surface inventory pass for Project04
Arc01.
