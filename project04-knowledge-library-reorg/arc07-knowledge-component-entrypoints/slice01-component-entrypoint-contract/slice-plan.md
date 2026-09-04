# Slice 01: Component Entrypoint Contract and Migration Map

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice01-component-entrypoint-contract
status: open
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: none
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Produce a source-backed component entrypoint contract and migration map before
any Arc07 source moves. The key decision is whether the framework components
should become standalone component-root `SKILL.md` entrypoints, and which
current long-form documents should instead become guide or template material.

## Scope

In scope:

- Current source inventory for:
  - repository root `SKILL.md`;
  - `knowledge/agent-coordination/`;
  - `knowledge/code-auditing/`;
  - `knowledge/collaboration-framework/`;
  - `knowledge/contribution-style/`;
  - `knowledge/engineering-methods/`;
  - `knowledge/project-management/`;
  - adjacent `knowledge/testing/` and `knowledge/work-verification/` surfaces,
    with an explicit include/exclude recommendation.
- Current references from `README.md`, `docs/`, root `SKILL.md`, Makefile
  `CF_FILES`, `ALL_SKILL_FILES`, package-path exceptions, and component-local
  Markdown links.
- Decision recommendation for component-root `SKILL.md`, `guides/`, and
  `templates/` layout.
- Migration impact map for source moves, link repairs, package behavior, and
  validation gates.
- Implementation slice roadmap with explicit source-edit authorization
  boundaries for each later slice.

Out of scope:

- Editing source files.
- Moving root `SKILL.md`.
- Renaming component documents.
- Updating Makefile/package lists.
- Updating release notes.
- Generating or committing zips.
- Implementing `concept-card-method`.
- Repackaging CCDP as an installable skill.

## Expected Artifacts

- `artifacts/current-component-layout-and-reference-map.md`
- `artifacts/component-entrypoint-decision-register.md`
- `artifacts/source-migration-impact-map.md`
- `artifacts/validation-command-inventory.md`
- `artifacts/implementation-slice-roadmap.md`

## Verification Approach

CC must treat this as read-only planning. Start from clean source and planning
checkouts, inspect the live source tree and Makefile/package surfaces, then
write the five artifacts under `artifacts/`.

The decision register should test this starting recommendation:

- `knowledge/collaboration-framework/SKILL.md` becomes the canonical
  collaboration-framework entrypoint.
- Independently loadable framework components get concise component-root
  `SKILL.md` wayfinders.
- Long current documents become `guides/` material unless they are genuinely
  templates.
- `knowledge/project-management/docs/pm/` becomes
  `knowledge/project-management/guides/`.
- Adjacent `testing` and `work-verification` surfaces are not silently moved;
  include or exclude them with rationale.

The implementation roadmap must separate source-edit slices by risk and must
state the exact validation gates later slices should run.

## Exit Criteria

- All five expected artifacts exist under `artifacts/`.
- Decision register directly answers the component `SKILL.md` question for
  each named component.
- Migration map names source paths, target paths, affected public docs,
  Makefile variables/targets, package-path exception surfaces, and expected
  package/install effects.
- Validation command inventory names the commands needed after source moves.
- Implementation roadmap proposes follow-on slices with explicit source-edit
  boundaries and commit-scope instructions.
- Source checkout remains clean and unmodified.
- Planning checkout contains only this Slice01 planning packet before commit.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc07.
