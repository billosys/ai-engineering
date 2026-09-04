# Component Guide Move Report

Source commit: `0b0f363a4070df09f1bcf7b225f4cd0db018baeb`

## Component Guide Move

The Slice03 source change used explicit `git mv` operations for the long
collaboration-framework component documents:

| From | To |
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

Empty legacy directories were removed with `rmdir` after the moves:

- `knowledge/project-management/docs/pm`
- `knowledge/agent-coordination/docs`
- `knowledge/code-auditing/docs`
- `knowledge/collaboration-framework/docs`
- `knowledge/contribution-style/docs`
- `knowledge/engineering-methods/docs`
- `knowledge/project-management/docs`
- `knowledge/testing/docs`

Templates remain under their existing component `templates/` directories:

- `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`
- `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`

## Source Commit Scope

The source commit used explicit staging paths authorized by the Slice03 prompt:
`AGENTS.md`, `Makefile`, `README.md`, public `docs/` pages,
`assets/packaging/path-exceptions.tsv`, `scripts/stage-skill-entrypoint`, and
the affected `knowledge/` component directories.

Generated zips and build output were excluded. `build/` and `target/skills/`
were used only as ignored validation outputs.

The committed source change includes the required co-author trailers.
