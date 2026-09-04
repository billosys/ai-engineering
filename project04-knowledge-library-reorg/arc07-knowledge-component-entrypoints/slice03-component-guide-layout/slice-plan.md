# Slice 03: Component Guide Layout and Standalone Entrypoints

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice03-component-guide-layout
status: verified-closed
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized
operating-mode: expedited
artifact_home: artifacts/
closed-by: CDC
closed-on: 2026-09-04
cdc-verification: cdc-verification.md
```

## Goal

Implement the component guide layout and component-root entrypoint contract
accepted in Slice01, now that Slice02 has moved the collaboration-framework
source entrypoint into `knowledge/collaboration-framework/SKILL.md`.

The target shape is:

- concise component-root `SKILL.md` wayfinders for framework components;
- long component material under `guides/`;
- reusable forms under `templates/`;
- no stale tracked `docs/` holdover directories under the affected framework
  component roots.

## Scope

In scope:

- Add concise component-root `SKILL.md` wayfinders/contracts for:
  - `knowledge/agent-coordination/SKILL.md`;
  - `knowledge/code-auditing/SKILL.md`;
  - `knowledge/contribution-style/SKILL.md`;
  - `knowledge/engineering-methods/SKILL.md`;
  - `knowledge/project-management/SKILL.md`;
  - `knowledge/testing/SKILL.md`;
  - `knowledge/work-verification/SKILL.md`.
- Update existing `knowledge/collaboration-framework/SKILL.md` routing from
  legacy component `docs/` paths to the new `guides/` paths.
- Move long component documents to `guides/` with explicit `git mv` path
  pairs.
- Move `knowledge/project-management/docs/pm/*` directly to
  `knowledge/project-management/guides/`.
- Keep `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`.
- Keep `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`.
- Remove emptied legacy `docs/` directories with `rmdir`, including
  `knowledge/project-management/docs/pm` before
  `knowledge/project-management/docs`.
- Repair README, public docs, component guide links, Makefile packaging lists,
  package-path exceptions, and standing instruction references required by
  these moves.

Out of scope:

- Creating separately installable packages for the component-root `SKILL.md`
  files.
- Broad prose rewrites beyond concise entrypoint text and necessary routing or
  path repairs.
- Moving templates.
- Updating release notes.
- Touching CCDP source or changing CCDP package semantics.
- Committing generated zips, `build/`, or ignored build output.

## Required Source Moves

Use explicit `git mv` operations for every tracked move:

| Source path | Target path |
| --- | --- |
| `knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md` | `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md` |
| `knowledge/agent-coordination/docs/SUBAGENT-DELEGATION-POLICY.md` | `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md` |
| `knowledge/code-auditing/docs/CODE-AUDIT.md` | `knowledge/code-auditing/guides/CODE-AUDIT.md` |
| `knowledge/contribution-style/docs/CONTRIBUTION-STYLE.md` | `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md` |
| `knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md` | `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md` |
| `knowledge/project-management/docs/PROJECT-MANAGEMENT.md` | `knowledge/project-management/guides/PROJECT-MANAGEMENT.md` |
| `knowledge/project-management/docs/pm/01-scales-of-work.md` | `knowledge/project-management/guides/01-scales-of-work.md` |
| `knowledge/project-management/docs/pm/02-canonical-planning-worktree.md` | `knowledge/project-management/guides/02-canonical-planning-worktree.md` |
| `knowledge/project-management/docs/pm/03-planning-top-down.md` | `knowledge/project-management/guides/03-planning-top-down.md` |
| `knowledge/project-management/docs/pm/04-closing-slices.md` | `knowledge/project-management/guides/04-closing-slices.md` |
| `knowledge/project-management/docs/pm/05-closing-arcs.md` | `knowledge/project-management/guides/05-closing-arcs.md` |
| `knowledge/project-management/docs/pm/06-confirmation-protocol.md` | `knowledge/project-management/guides/06-confirmation-protocol.md` |
| `knowledge/project-management/docs/pm/07-anti-patterns.md` | `knowledge/project-management/guides/07-anti-patterns.md` |
| `knowledge/project-management/docs/pm/08-maintenance.md` | `knowledge/project-management/guides/08-maintenance.md` |
| `knowledge/project-management/docs/pm/09-worked-example-odm.md` | `knowledge/project-management/guides/09-worked-example-odm.md` |
| `knowledge/project-management/docs/pm/version-history.md` | `knowledge/project-management/guides/version-history.md` |
| `knowledge/testing/docs/CODE-COVERAGE.md` | `knowledge/testing/guides/CODE-COVERAGE.md` |

After moves, use `rmdir` for emptied directories:

- `knowledge/project-management/docs/pm`
- `knowledge/agent-coordination/docs`
- `knowledge/code-auditing/docs`
- `knowledge/collaboration-framework/docs`
- `knowledge/contribution-style/docs`
- `knowledge/engineering-methods/docs`
- `knowledge/project-management/docs`
- `knowledge/testing/docs`

Do not use `rm -rf`.

## Expected Artifacts

- `artifacts/component-guide-move-report.md`
- `artifacts/component-entrypoint-report.md`
- `artifacts/reference-and-package-repair-report.md`
- `artifacts/validation-report.md`

## Verification Approach

CC should begin from clean source and planning checkouts. Apply the mechanical
file moves first, then add concise component-root `SKILL.md` files, then repair
links and Makefile/package surfaces.

The concise component-root `SKILL.md` files should be wayfinders, not renamed
long documents. They should state when to use the component, its scope, and
which guide or template files to load. They should be compatible with the
repository's `check-skills` validation and included in `ALL_SKILL_FILES`, but
they should not be added as separate installable skill zip targets unless a
later accepted plan changes package topology.

Slice03 must repair the source-level engineering-methods link surfaced by
Slice02 while moving the methodology guide:

- old surface:
  `knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md`
  contained a `../SKILL.md` reference;
- target surface:
  the moved `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`
  should link correctly to `../SKILL.md`.

Slice03 must also update `AGENTS.md` to reference the new project-management
guide paths. Do not edit `CLAUDE.md` as a separate copy; it is the compatibility
surface for the same standing instructions.

## Exit Criteria

- All required source moves are made with explicit `git mv` path pairs.
- Empty legacy component `docs/` directories are removed with `rmdir`, not
  `rm -rf`.
- Concise component-root `SKILL.md` files exist for every accepted component.
- Long material is under `guides/`, and template material remains under
  `templates/`.
- `Makefile` packaging lists include the moved guide paths and component-root
  entrypoints as appropriate.
- README/docs/AGENTS/component links are repaired for the new layout.
- `assets/packaging/path-exceptions.tsv` is updated if existing exception paths
  moved.
- Source commit is created with only authorized source files and both required
  co-author trailers.
- Planning artifacts, ledger, and `closing-report.md` are committed in a
  separate planning commit with both required co-author trailers.

## CDC Close

Slice03 was CDC-verified closed on 2026-09-04. See
`cdc-verification.md`.
