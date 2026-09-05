# Closing Report: Slice 11 Contribution-Style Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice11-contribution-style-guide-split
status: proposed-done
closed-by: CC
closed-on: 2026-09-05
source_commit: f96c30266b892fa67185f03046b6662326df0481
planning_commit: a8edf2b9b166735c7af258afdee4fe2b0c1fe5b5
```

## Verdict

Slice11 is proposed-done pending CDC verification.

The contribution-style guide surface is split into a selective-load
maintainer-facing style guide and a selective-load upstream ticket workflow
guide. The contribution ticket template remains a package-local authoring
template. The old `CONTRIBUTION-STYLE.md` path is no longer a live source or
package route.

Source commit:
`f96c30266b892fa67185f03046b6662326df0481`

Planning commit:
a8edf2b9b166735c7af258afdee4fe2b0c1fe5b5

## Explicit File Lists

Source explicit file list:

- `AGENTS.md`
- `Makefile`
- `docs/collaboration-framework.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/contribution-style/SKILL.md`
- `knowledge/contribution-style/guides/01-contribution-style.md`
- `knowledge/contribution-style/guides/02-upstream-ticket-workflow.md`
- `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md` deleted
- `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`
- `knowledge/contribution-style/version-history.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/version-history.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

Planning explicit file list:

- `arc08-framework-guide-decomposition/slice11-contribution-style-guide-split/artifacts/current-contribution-style-surface-map.md`
- `arc08-framework-guide-decomposition/slice11-contribution-style-guide-split/artifacts/contribution-style-split-map.md`
- `arc08-framework-guide-decomposition/slice11-contribution-style-guide-split/artifacts/legacy-contribution-style-disposition.md`
- `arc08-framework-guide-decomposition/slice11-contribution-style-guide-split/artifacts/template-role-disposition.md`
- `arc08-framework-guide-decomposition/slice11-contribution-style-guide-split/artifacts/source-route-repair-map.md`
- `arc08-framework-guide-decomposition/slice11-contribution-style-guide-split/artifacts/source-validation-results.md`
- `arc08-framework-guide-decomposition/slice11-contribution-style-guide-split/ledger.md`
- `arc08-framework-guide-decomposition/slice11-contribution-style-guide-split/closing-report.md`

## Artifact Inventory

Durable Slice11 artifacts live under `artifacts/`:

- `artifacts/current-contribution-style-surface-map.md`
- `artifacts/contribution-style-split-map.md`
- `artifacts/legacy-contribution-style-disposition.md`
- `artifacts/template-role-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`

No artifact-home override was used.

## Row Walk

| ID | Status | Evidence |
|---|---|---|
| F-1 | done | `artifacts/current-contribution-style-surface-map.md` inventories the pre-edit source, route, template, package, and history surfaces. |
| F-2 | done | Source contains `01-contribution-style.md` and `02-upstream-ticket-workflow.md`; `artifacts/contribution-style-split-map.md` maps them to the accepted material. |
| F-3 | done | `artifacts/contribution-style-split-map.md`, `artifacts/template-role-disposition.md`, both new guides, and the retained template preserve maintainer voice while separating ticket workflow/template usage. |
| F-4 | done | `artifacts/legacy-contribution-style-disposition.md` records the old path move attempt, Git delete/add result, live-route removal, and package absence. |
| F-5 | done | `artifacts/template-role-disposition.md` records that `CONTRIBUTION-TICKET.md` remains a package-local authoring template, not a guide. |
| F-6 | done | `artifacts/source-route-repair-map.md` records contribution-style, collaboration-framework, engineering-methods, docs, AGENTS, release-note, Makefile, and package-exception dispositions. |
| F-7 | done | Source whitespace, skill-description, focused local-link, collaboration-framework package, and full package-path validation passed with zero hard failures. |
| F-8 | done | Generated `collaboration-framework.zip` contains both contribution-style guides and the retained template, and omits the old `CONTRIBUTION-STYLE.md` path. |
| F-9 | done | This report records exact source commit, planning close-packet commit, explicit file lists, final statuses, row walk, and Slice12 bubble-up. |

Rows: 9. Done: 9. Deferred: 0. No-op: 0.

## Final Statuses

Source worktree: clean after source commit.

Planning worktree: pending this close-packet commit.

Deferred: none.

No-op: package-path exception repair; no old contribution-style exception
existed and validation introduced no hard failure requiring an exception.

## Bubble-Up to Arc08

Slice11 delivered the Arc08 A-11 capability: contribution-style guidance is now
split into two accepted numbered guides, and the ticket template remains a
retained package-local authoring template.

Silent-drop diff:

- Accepted guide split: delivered.
- Maintainer-facing voice and calibrated contribution discipline: delivered.
- Upstream ticket workflow separation: delivered.
- Local draft, line-reference, blockquote-header, paste-boundary,
  cross-linking, one-ticket-per-problem, and canonical on-disk artifact
  guidance: delivered.
- `CONTRIBUTION-TICKET.md` template retention: delivered.
- Old `CONTRIBUTION-STYLE.md` route/package disposition: delivered.
- Route, package, docs, AGENTS, release-note, and validation repairs:
  delivered.
- Deferred: none.
- No-op: package-path exception repair.

No Arc08 scope change is required. Slice12 can proceed to final package,
install, link, CCDP disposition, and release reconciliation. It should confirm
that old monolith and pre-split guide filenames are no longer live load targets
unless explicitly retained as compatibility/provenance stubs or package-local
templates.
