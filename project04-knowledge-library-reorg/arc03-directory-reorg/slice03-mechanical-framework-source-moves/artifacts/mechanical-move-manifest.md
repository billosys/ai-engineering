# Mechanical Move Manifest

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice03-mechanical-framework-source-moves
artifact: mechanical-move-manifest
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source_commit: 99cebae1e98004164e4ea6735c4a68bc60c233da
source-files-edited: true
```

## Purpose

This mechanical move manifest records the exact collaboration-framework
payload files moved from top-level `docs/` and `templates/` source paths into
`knowledge/collaboration-framework/`.

## Move Map

| Old path | New path | Preservation evidence |
|----------|----------|-----------------------|
| `docs/AI-CONSTITUTION-SUPPLEMENT.md` | `knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md` | `R100`; `cmp OK`. |
| `docs/AI-ENGINEERING-METHODOLOGY.md` | `knowledge/collaboration-framework/docs/AI-ENGINEERING-METHODOLOGY.md` | `R098`; line-level route/link update and version history. |
| `docs/PROJECT-MANAGEMENT.md` | `knowledge/collaboration-framework/docs/PROJECT-MANAGEMENT.md` | `R100`; `cmp OK`. |
| `docs/pm/01-scales-of-work.md` | `knowledge/collaboration-framework/docs/pm/01-scales-of-work.md` | `R100`; `cmp OK`. |
| `docs/pm/02-canonical-planning-worktree.md` | `knowledge/collaboration-framework/docs/pm/02-canonical-planning-worktree.md` | `R100`; `cmp OK`. |
| `docs/pm/03-planning-top-down.md` | `knowledge/collaboration-framework/docs/pm/03-planning-top-down.md` | `R100`; `cmp OK`. |
| `docs/pm/04-closing-slices.md` | `knowledge/collaboration-framework/docs/pm/04-closing-slices.md` | `R100`; `cmp OK`. |
| `docs/pm/05-closing-arcs.md` | `knowledge/collaboration-framework/docs/pm/05-closing-arcs.md` | `R100`; `cmp OK`. |
| `docs/pm/06-confirmation-protocol.md` | `knowledge/collaboration-framework/docs/pm/06-confirmation-protocol.md` | `R100`; `cmp OK`. |
| `docs/pm/07-anti-patterns.md` | `knowledge/collaboration-framework/docs/pm/07-anti-patterns.md` | `R100`; `cmp OK`. |
| `docs/pm/08-maintenance.md` | `knowledge/collaboration-framework/docs/pm/08-maintenance.md` | `R100`; `cmp OK`. |
| `docs/pm/09-worked-example-odm.md` | `knowledge/collaboration-framework/docs/pm/09-worked-example-odm.md` | `R100`; `cmp OK`. |
| `docs/pm/version-history.md` | `knowledge/collaboration-framework/docs/pm/version-history.md` | `R100`; `cmp OK`. |
| `docs/CODE-AUDIT.md` | `knowledge/collaboration-framework/docs/CODE-AUDIT.md` | `R100`; `cmp OK`. |
| `docs/CODE-COVERAGE.md` | `knowledge/collaboration-framework/docs/CODE-COVERAGE.md` | `R100`; `cmp OK`. |
| `docs/SUBAGENT-DELEGATION-POLICY.md` | `knowledge/collaboration-framework/docs/SUBAGENT-DELEGATION-POLICY.md` | `R100`; `cmp OK`. |
| `docs/CONTRIBUTION-STYLE.md` | `knowledge/collaboration-framework/docs/CONTRIBUTION-STYLE.md` | `R100`; `cmp OK`. |
| `templates/LEDGER-DISCIPLINE.md` | `knowledge/collaboration-framework/templates/LEDGER-DISCIPLINE.md` | `R100`; `cmp OK`. |
| `templates/CONTRIBUTION-TICKET.md` | `knowledge/collaboration-framework/templates/CONTRIBUTION-TICKET.md` | `R100`; `cmp OK`. |

## Left In Place

The prompt explicitly kept these top-level files in place:

- `docs/ORIGINS.md`
- `templates/GUIDE.md`

Domain/tooling skills, Biome entrypoints, and `protocols/ccdp` were not moved.

## Source Commit

Source commit: `99cebae1e98004164e4ea6735c4a68bc60c233da`
(`Move collaboration-framework source payload under knowledge`).

`git show --name-status --find-renames --oneline HEAD` records the moved
payload under `knowledge/collaboration-framework`, with the pure moves as
`R100` and the methodology file as `R098` because of the disclosed link and
version-history repair.
