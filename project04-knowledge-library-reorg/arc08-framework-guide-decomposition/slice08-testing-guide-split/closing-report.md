# Closing Report: Slice 08 Testing Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice08-testing-guide-split
status: proposed-done
closed-by: CC
closed-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg
source_commit: 120c2ceaf26ca656068d9f2ec34c978eefaf04a5
planning_commit: 6308c2f7408f3439fa5f8f41f52680232a130385
```

## Verdict

Slice08 is proposed-done pending CDC verification.

The source implementation split the testing component into three accepted
numbered guides, renamed the old `CODE-COVERAGE.md` prompt into
`02-coverage-hardening.md` with `git mv`, repaired live routes, updated
component histories, rebuilt the collaboration-framework package, and
validated package-local paths with zero hard failures.

## Source Commit

Source commit:
`120c2ceaf26ca656068d9f2ec34c978eefaf04a5`

Planning commit:
6308c2f7408f3439fa5f8f41f52680232a130385

Source explicit file list:

- `AGENTS.md`
- `Makefile`
- `docs/collaboration-framework.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/SKILL.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/version-history.md`
- `knowledge/testing/SKILL.md`
- `knowledge/testing/guides/01-testing-discipline.md`
- `knowledge/testing/guides/02-coverage-hardening.md`
- `knowledge/testing/guides/03-validation-gates.md`
- `knowledge/testing/version-history.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

## Planning Explicit File List

- `arc08-framework-guide-decomposition/slice08-testing-guide-split/artifacts/current-testing-surface-map.md`
- `arc08-framework-guide-decomposition/slice08-testing-guide-split/artifacts/testing-split-map.md`
- `arc08-framework-guide-decomposition/slice08-testing-guide-split/artifacts/legacy-code-coverage-disposition.md`
- `arc08-framework-guide-decomposition/slice08-testing-guide-split/artifacts/source-route-repair-map.md`
- `arc08-framework-guide-decomposition/slice08-testing-guide-split/artifacts/source-validation-results.md`
- `arc08-framework-guide-decomposition/slice08-testing-guide-split/ledger.md`
- `arc08-framework-guide-decomposition/slice08-testing-guide-split/closing-report.md`

## CODE-COVERAGE Disposition

`knowledge/testing/guides/CODE-COVERAGE.md` was renamed with `git mv` to
`knowledge/testing/guides/02-coverage-hardening.md`. No copy of the old path
was retained, and the generated collaboration-framework package does not
contain a `CODE-COVERAGE.md` entry.

## Validation Summary

- `git diff --check`: pass.
- Focused local Markdown link validation: pass, 116 local links checked, 0
  missing.
- `make check-skills`: pass, all skill descriptions within limit.
- `make collab-framework`: pass; generated package contains 70 files.
- `make check-package-paths`: pass; 242 Markdown files scanned, 0 hard
  failures, 378 warnings, 3 explicit exceptions, 660 skipped external URLs.
- `unzip -l target/skills/collaboration-framework.zip` focused inspection:
  pass; three testing guides are present and the old `CODE-COVERAGE.md` path is
  absent.

Generated `target/skills/*.zip`, `build/`, and `target/skills/` contents were
not committed.

## Ledger Walk

| ID | Result | Evidence |
|---|---|---|
| F-1 | done | `artifacts/current-testing-surface-map.md` records the current testing source, route, package, and history surface. |
| F-2 | done | Source commit `120c2ceaf26ca656068d9f2ec34c978eefaf04a5` creates the three accepted numbered guides; `artifacts/testing-split-map.md` maps them to source semantics. |
| F-3 | done | The split map and guide contents preserve the testing/coverage quality floor and independent load reasons. |
| F-4 | done | `artifacts/legacy-code-coverage-disposition.md` records the `git mv` rename and old package-entry absence. |
| F-5 | done | `artifacts/source-route-repair-map.md` records repaired testing, collaboration-framework, engineering-methods, docs, AGENTS, release-note, and package-list surfaces. |
| F-6 | done | `artifacts/source-validation-results.md` records passing diff, link, skill, collaboration-framework package, and package-path validation. |
| F-7 | done | Zip inspection confirms all three testing guides are present and `CODE-COVERAGE.md` is absent. |
| F-8 | done | This report records exact source commit, planning close-packet commit, explicit file lists, final statuses, row walk, and bubble-up. |

Rows: 8. Done: 8. Deferred: 0. No-op: 0.

## Artifact Inventory

Slice08 produced these durable planning artifacts under `artifacts/`:

- `current-testing-surface-map.md`
- `testing-split-map.md`
- `legacy-code-coverage-disposition.md`
- `source-route-repair-map.md`
- `source-validation-results.md`

No artifact-home override was used.

## Bubble-Up to Arc08

Slice08 delivered the Arc08 testing guide split assigned to it. The accepted
testing layout now exists in source and in the generated collaboration-framework
package.

Implementation revealed no required Arc08 plan change. The old
`CODE-COVERAGE.md` path was renamed into the accepted coverage-hardening guide,
which matches the Slice08 prompt's preferred history-preserving route.

Slice09 can proceed to the code-auditing guide split. It should preserve the
post-Slice08 route pattern: focused guides are primary selective-load targets,
and any retained legacy prompt/template material must be explicitly
dispositioned as support material.
