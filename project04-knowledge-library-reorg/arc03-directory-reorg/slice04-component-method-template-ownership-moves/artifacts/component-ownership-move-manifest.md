# Component Ownership Move Manifest

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice04-component-method-template-ownership-moves
artifact: component ownership move manifest
source_commit: 873a5502acef9c087cefd78d468cf6d123a27341
source-files-edited: true
```

## Summary

This slice performed a mechanical move out of the transitional
`knowledge/collaboration-framework/` payload into accepted Project02
`knowledge/<component>/` owner roots. The top-level
`knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md` posture
document stayed under `knowledge/collaboration-framework/` because the accepted
architecture keeps `collaboration-framework` as the daily-driver composer and
posture floor.

No final guide decomposition was performed. Where splitting would require
rewriting, original file names were preserved under the owning component root.

## Mechanical Move Map

| Old path | New path | Owner root | Move class |
|----------|----------|------------|------------|
| `knowledge/collaboration-framework/docs/AI-ENGINEERING-METHODOLOGY.md` | `knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md` | `knowledge/engineering-methods/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/docs/PROJECT-MANAGEMENT.md` | `knowledge/project-management/docs/PROJECT-MANAGEMENT.md` | `knowledge/project-management/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/docs/pm/01-scales-of-work.md` | `knowledge/project-management/docs/pm/01-scales-of-work.md` | `knowledge/project-management/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/docs/pm/02-canonical-planning-worktree.md` | `knowledge/project-management/docs/pm/02-canonical-planning-worktree.md` | `knowledge/project-management/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/docs/pm/03-planning-top-down.md` | `knowledge/project-management/docs/pm/03-planning-top-down.md` | `knowledge/project-management/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/docs/pm/04-closing-slices.md` | `knowledge/project-management/docs/pm/04-closing-slices.md` | `knowledge/project-management/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/docs/pm/05-closing-arcs.md` | `knowledge/project-management/docs/pm/05-closing-arcs.md` | `knowledge/project-management/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/docs/pm/06-confirmation-protocol.md` | `knowledge/project-management/docs/pm/06-confirmation-protocol.md` | `knowledge/project-management/` | pure mechanical move |
| `knowledge/collaboration-framework/docs/pm/07-anti-patterns.md` | `knowledge/project-management/docs/pm/07-anti-patterns.md` | `knowledge/project-management/` | pure mechanical move |
| `knowledge/collaboration-framework/docs/pm/08-maintenance.md` | `knowledge/project-management/docs/pm/08-maintenance.md` | `knowledge/project-management/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/docs/pm/09-worked-example-odm.md` | `knowledge/project-management/docs/pm/09-worked-example-odm.md` | `knowledge/project-management/` | pure mechanical move |
| `knowledge/collaboration-framework/docs/pm/version-history.md` | `knowledge/project-management/docs/pm/version-history.md` | `knowledge/project-management/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/templates/LEDGER-DISCIPLINE.md` | `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` | `knowledge/work-verification/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/docs/CODE-COVERAGE.md` | `knowledge/testing/docs/CODE-COVERAGE.md` | `knowledge/testing/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/docs/CODE-AUDIT.md` | `knowledge/code-auditing/docs/CODE-AUDIT.md` | `knowledge/code-auditing/` | pure mechanical move |
| `knowledge/collaboration-framework/docs/SUBAGENT-DELEGATION-POLICY.md` | `knowledge/agent-coordination/docs/SUBAGENT-DELEGATION-POLICY.md` | `knowledge/agent-coordination/` | pure mechanical move |
| `knowledge/collaboration-framework/docs/CONTRIBUTION-STYLE.md` | `knowledge/contribution-style/docs/CONTRIBUTION-STYLE.md` | `knowledge/contribution-style/` | mechanical move with route/link update |
| `knowledge/collaboration-framework/templates/CONTRIBUTION-TICKET.md` | `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md` | `knowledge/contribution-style/` | mechanical move with route/link update |

## Source Commit Evidence

Source commit `873a5502acef9c087cefd78d468cf6d123a27341` records the move set.
`git show --name-status --find-renames --oneline HEAD` in the source checkout
reported the moved files as `R100`, `R099`, `R098`, `R097`, `R096`, `R088`, or
`R086` depending on whether package-local route/link updates were required.

The move stayed within accepted component roots and did not move domain/tooling
skill roots, Biome entrypoints, CCDP source, `docs/ORIGINS.md`, README prose,
or generated zips.
