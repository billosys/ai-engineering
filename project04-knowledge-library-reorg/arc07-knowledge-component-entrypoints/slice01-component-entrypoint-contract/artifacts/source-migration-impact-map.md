# Source Migration Impact Map

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice01-component-entrypoint-contract
status: proposed-done
source_edits: none
```

## Source Path to Target Path Moves

Later source-edit slices should use explicit `git mv` path pairs. Do not use
bulk glob moves for this cleanup.

### Slice02 Entrypoint Relocation

| Source path | Target path | Notes |
| --- | --- | --- |
| `SKILL.md` | `knowledge/collaboration-framework/SKILL.md` | Move canonical source entrypoint under the collaboration-framework component root. |

### Slice03 Component Guide Layout

| Source path | Target path | Notes |
| --- | --- | --- |
| `knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md` | `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md` | Long-form posture guide. |
| `knowledge/agent-coordination/docs/SUBAGENT-DELEGATION-POLICY.md` | `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md` | Long-form component guide. |
| `knowledge/code-auditing/docs/CODE-AUDIT.md` | `knowledge/code-auditing/guides/CODE-AUDIT.md` | Long-form component guide. |
| `knowledge/contribution-style/docs/CONTRIBUTION-STYLE.md` | `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md` | Long-form component guide. |
| `knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md` | `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md` | Long-form component guide. |
| `knowledge/project-management/docs/PROJECT-MANAGEMENT.md` | `knowledge/project-management/guides/PROJECT-MANAGEMENT.md` | Component wayfinder becomes guide material routed by root `SKILL.md`. |
| `knowledge/project-management/docs/pm/01-scales-of-work.md` | `knowledge/project-management/guides/01-scales-of-work.md` | Prompt-requested `docs/pm/` to `guides/` migration. |
| `knowledge/project-management/docs/pm/02-canonical-planning-worktree.md` | `knowledge/project-management/guides/02-canonical-planning-worktree.md` | Prompt-requested `docs/pm/` to `guides/` migration. |
| `knowledge/project-management/docs/pm/03-planning-top-down.md` | `knowledge/project-management/guides/03-planning-top-down.md` | Prompt-requested `docs/pm/` to `guides/` migration. |
| `knowledge/project-management/docs/pm/04-closing-slices.md` | `knowledge/project-management/guides/04-closing-slices.md` | Prompt-requested `docs/pm/` to `guides/` migration. |
| `knowledge/project-management/docs/pm/05-closing-arcs.md` | `knowledge/project-management/guides/05-closing-arcs.md` | Prompt-requested `docs/pm/` to `guides/` migration. |
| `knowledge/project-management/docs/pm/06-confirmation-protocol.md` | `knowledge/project-management/guides/06-confirmation-protocol.md` | Prompt-requested `docs/pm/` to `guides/` migration. |
| `knowledge/project-management/docs/pm/07-anti-patterns.md` | `knowledge/project-management/guides/07-anti-patterns.md` | Prompt-requested `docs/pm/` to `guides/` migration. |
| `knowledge/project-management/docs/pm/08-maintenance.md` | `knowledge/project-management/guides/08-maintenance.md` | Prompt-requested `docs/pm/` to `guides/` migration. |
| `knowledge/project-management/docs/pm/09-worked-example-odm.md` | `knowledge/project-management/guides/09-worked-example-odm.md` | Prompt-requested `docs/pm/` to `guides/` migration. |
| `knowledge/project-management/docs/pm/version-history.md` | `knowledge/project-management/guides/version-history.md` | Prompt-requested `docs/pm/` to `guides/` migration. |
| `knowledge/testing/docs/CODE-COVERAGE.md` | `knowledge/testing/guides/CODE-COVERAGE.md` | Adjacent `CF_FILES` component with same docs holdover shape. |

### New Component Entrypoints

Later source-edit slices should add these files:

- `knowledge/agent-coordination/SKILL.md`
- `knowledge/code-auditing/SKILL.md`
- `knowledge/contribution-style/SKILL.md`
- `knowledge/engineering-methods/SKILL.md`
- `knowledge/project-management/SKILL.md`
- `knowledge/testing/SKILL.md`
- `knowledge/work-verification/SKILL.md`

`knowledge/collaboration-framework/SKILL.md` is created by moving root
`SKILL.md`, not by adding a second copy.

## Directory Cleanup Mechanics

After the explicit `git mv` operations have emptied the legacy directories,
later implementation slices should remove them with `rmdir`, not `rm -rf`:

```sh
rmdir knowledge/project-management/docs/pm
rmdir knowledge/agent-coordination/docs
rmdir knowledge/code-auditing/docs
rmdir knowledge/collaboration-framework/docs
rmdir knowledge/contribution-style/docs
rmdir knowledge/engineering-methods/docs
rmdir knowledge/project-management/docs
rmdir knowledge/testing/docs
```

`knowledge/work-verification/templates/` and
`knowledge/contribution-style/templates/` should remain.

## Affected Links

Later source-edit slices must update affected links in:

- relocated `knowledge/collaboration-framework/SKILL.md`;
- new component-root `SKILL.md` files;
- moved guides that link across component roots;
- `README.md`;
- `docs/skill-library.md`;
- `docs/knowledge-library-anatomy.md`;
- `docs/repository-overview.md`;
- `docs/collaboration-framework.md`;
- `docs/ORIGINS.md`;
- `Makefile`;
- `assets/packaging/path-exceptions.tsv`.

Expected public-doc changes:

- replace `./SKILL.md`/`../SKILL.md` source references for the collaboration
  framework with `knowledge/collaboration-framework/SKILL.md` where referring
  to source;
- preserve generated package language that says the installed package exposes
  `collaboration-framework/SKILL.md`;
- update component material links from `knowledge/*/docs/...` to
  `knowledge/*/guides/...`;
- keep template links under `knowledge/*/templates/...`.

## Makefile and Package Changes

Expected Makefile changes:

- `ALL_SKILL_FILES`: replace repository-root `SKILL.md` with
  `knowledge/collaboration-framework/SKILL.md`; decide whether component-root
  `SKILL.md` files are checked by `check-skills` in the same list.
- `CF_FILES`: replace repository-root `SKILL.md` with staged-entrypoint logic
  for `knowledge/collaboration-framework/SKILL.md`.
- `CF_FILES`: update component guide paths from `docs/` and `docs/pm/` to
  `guides/`.
- `CF_FILES`: include new component-root `SKILL.md` files if they are intended
  to be available inside the collaboration-framework package.
- `CF_FILES`: keep `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`
  and `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` as template
  surfaces unless a later accepted decision changes them.
- `collab-framework` target: stage the source entrypoint as
  `$(CF_STAGE)/SKILL.md` so package output remains
  `collaboration-framework/SKILL.md`.

Package-path exceptions:

- update `assets/packaging/path-exceptions.tsv` rows whose document paths move
  from `docs/` to `guides/`;
- re-evaluate whether existing collaboration-framework package exceptions
  still point at the correct package-local `SKILL.md` document after the source
  entrypoint move.

## Release Note Impact

Release note impact is expected if Arc07 changes the public release surface:

- `workbench/RELEASE-0.5.0.md` may need targeted source updates in a later
  implementation/reconciliation slice.
- `workbench/` is ignored, so any intended release-note source update requires
  explicit `git add -f` only if the accepted later slice authorizes committing
  that file.

## Validation Risk

Primary validation risk:

- source-local links and package-local links for the relocated
  collaboration-framework entrypoint may diverge unless the implementation
  explicitly stages package paths.
- `make collab-framework` may pass file copying but fail package-path
  validation if entrypoint links are not transformed or authored to work in
  both contexts.
- README/docs references must distinguish source entrypoint path from generated
  package entrypoint path.
- package-path exceptions may go stale after document path moves.

No CCDP source path is affected by this migration. CCDP validation remains a
release/reconciliation gate, not a source-edit target for Arc07 component
cleanup.

