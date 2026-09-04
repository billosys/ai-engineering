# Closing Report: Slice 07 Work-Verification Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice07-work-verification-guide-split
status: proposed-done
closed-by: CC
closed-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg
source_commit: 2a092d76090387a12e34d08e895084ee5389dbb2
planning_commit: pending until this report is committed
```

## Verdict

Slice07 is proposed-done pending CDC verification.

The source implementation split the work-verification guide surface into five
accepted numbered guides, retained `templates/LEDGER-DISCIPLINE.md` as the full
protocol and copyable-table support asset, repaired live routes, updated
component histories, rebuilt the collaboration-framework package, and validated
package-local paths with zero hard failures.

## Source Commit

Source commit:
`2a092d76090387a12e34d08e895084ee5389dbb2`

Planning commit:
pending until this report is committed

Source explicit file list:

- `AGENTS.md`
- `Makefile`
- `docs/ORIGINS.md`
- `docs/collaboration-framework.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/SKILL.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/guides/06-source-package-release-gates.md`
- `knowledge/engineering-methods/version-history.md`
- `knowledge/project-management/SKILL.md`
- `knowledge/project-management/guides/01-scales-of-work.md`
- `knowledge/project-management/guides/02-canonical-planning-worktree.md`
- `knowledge/project-management/guides/03-planning-top-down.md`
- `knowledge/project-management/guides/04-closing-slices.md`
- `knowledge/project-management/guides/05-closing-arcs.md`
- `knowledge/project-management/version-history.md`
- `knowledge/work-verification/SKILL.md`
- `knowledge/work-verification/guides/01-ledger-discipline.md`
- `knowledge/work-verification/guides/02-evidence-strength.md`
- `knowledge/work-verification/guides/03-row-closure.md`
- `knowledge/work-verification/guides/04-silent-drop-checks.md`
- `knowledge/work-verification/guides/05-independent-verification.md`
- `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`
- `knowledge/work-verification/version-history.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

## Planning Explicit File List

- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/artifacts/current-work-verification-surface-map.md`
- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/artifacts/work-verification-split-map.md`
- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/artifacts/template-retention-disposition.md`
- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/artifacts/source-route-repair-map.md`
- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/artifacts/source-validation-results.md`
- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/ledger.md`
- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/closing-report.md`

## Template Disposition

`knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` is retained as a
package-local support/template asset. It remains useful because it carries the
complete protocol and copyable slice/arc/project ledger table material in one
file. The focused guides are now the preferred live routes for selective
loading.

## Validation Summary

- `git diff --check`: pass.
- Focused local Markdown link validation: pass, 178 local links checked, 0
  missing.
- `make check-skills`: pass, all skill descriptions within limit.
- `make collab-framework`: pass; generated package contains 68 files.
- `make check-package-paths`: pass; 240 Markdown files scanned, 0 hard
  failures, 377 warnings, 3 explicit exceptions, 660 skipped external URLs.
- `unzip -l target/skills/collaboration-framework.zip` focused inspection:
  pass; five work-verification guides and retained template are present.

Generated `target/skills/*.zip`, `build/`, and `target/skills/` contents were
not committed.

## Ledger Walk

| ID | Result | Evidence |
|---|---|---|
| F-1 | done | `artifacts/current-work-verification-surface-map.md` records the current source, route, package, and history surface. |
| F-2 | done | Source commit `2a092d76090387a12e34d08e895084ee5389dbb2` creates the five accepted numbered guides; `artifacts/work-verification-split-map.md` maps them to source semantics. |
| F-3 | done | The split map and guide contents preserve semantic substance for ledger format, evidence strength, row closure, silent-drop checks, independent verification, and composition. |
| F-4 | done | `artifacts/template-retention-disposition.md` records retained-template rationale; source updates cross-route the template and history. |
| F-5 | done | `artifacts/source-route-repair-map.md` records repaired work-verification, collaboration-framework, project-management, engineering-methods, docs, AGENTS, release-note, and package-list surfaces. |
| F-6 | done | `artifacts/source-validation-results.md` records passing diff, link, skill, collaboration-framework package, and package-path validation. |
| F-7 | done | Zip inspection confirms all five guides and retained `templates/LEDGER-DISCIPLINE.md` are present. |
| F-8 | done | This report records exact source commit, pending planning commit placeholder, explicit file lists, final statuses, row walk, and bubble-up. |

Rows: 8. Done: 8. Deferred: 0. No-op: 0.

## Artifact Inventory

Slice07 produced these durable planning artifacts under `artifacts/`:

- `current-work-verification-surface-map.md`
- `work-verification-split-map.md`
- `template-retention-disposition.md`
- `source-route-repair-map.md`
- `source-validation-results.md`

No artifact-home override was used.

## Bubble-Up to Arc08

Slice07 delivered the Arc08 work-verification split assigned to it. The
accepted work-verification layout now exists in source and in the generated
collaboration-framework package.

Implementation revealed no required Arc08 plan change. The template was
retained, which matches the accepted architecture and the Slice07 prompt. The
collaboration-framework package grew from the Slice06 verified 62-entry shape
to 68 files because the five new guides were added while the retained template
remained packaged.

Slice08 can proceed to the testing guide split. It should preserve the
post-Slice07 route pattern: focused guides are primary selective-load targets,
while retained legacy prompt/template material is kept only when explicitly
dispositioned as support material.
