# Closing Report: Slice 09 Code-Auditing Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice09-code-auditing-guide-split
status: proposed-done
closed-by: CC
closed-on: 2026-09-05
source_commit: 1eb10d789734d9cca5c2c0f7cdedb4257dfab1e6
planning_commit: pending until this report is committed
```

## Verdict

Slice09 is proposed-done pending CDC verification.

The source commit split code-auditing guidance into five selective-load guides
without weakening the diagnosis-only audit contract. The old `CODE-AUDIT.md`
path was moved with `git mv` to `01-audit-scope-and-map.md`, semantically
extracted into companion guides, and removed as a live source/package route.

## Commits

Source commit:
`1eb10d789734d9cca5c2c0f7cdedb4257dfab1e6`

Planning commit:
pending until this report is committed

## Explicit File Lists

Source explicit file list:

- `AGENTS.md`
- `Makefile`
- `assets/packaging/path-exceptions.tsv`
- `docs/ORIGINS.md`
- `docs/collaboration-framework.md`
- `knowledge/code-auditing/SKILL.md`
- `knowledge/code-auditing/guides/01-audit-scope-and-map.md`
- `knowledge/code-auditing/guides/02-findings-and-severity.md`
- `knowledge/code-auditing/guides/03-scale-aware-auditing.md`
- `knowledge/code-auditing/guides/04-modernization-synthesis.md`
- `knowledge/code-auditing/guides/05-audit-to-hardening-handoff.md`
- `knowledge/code-auditing/guides/CODE-AUDIT.md`
- `knowledge/code-auditing/version-history.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/SKILL.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/version-history.md`
- `knowledge/project-management/guides/08-maintenance.md`
- `knowledge/project-management/version-history.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

Planning explicit file list:

- `arc08-framework-guide-decomposition/slice09-code-auditing-guide-split/artifacts/current-code-auditing-surface-map.md`
- `arc08-framework-guide-decomposition/slice09-code-auditing-guide-split/artifacts/code-auditing-split-map.md`
- `arc08-framework-guide-decomposition/slice09-code-auditing-guide-split/artifacts/legacy-code-audit-disposition.md`
- `arc08-framework-guide-decomposition/slice09-code-auditing-guide-split/artifacts/source-route-repair-map.md`
- `arc08-framework-guide-decomposition/slice09-code-auditing-guide-split/artifacts/source-validation-results.md`
- `arc08-framework-guide-decomposition/slice09-code-auditing-guide-split/ledger.md`
- `arc08-framework-guide-decomposition/slice09-code-auditing-guide-split/closing-report.md`

## Artifact Inventory

Durable Slice09 artifacts live under `artifacts/`:

- `artifacts/current-code-auditing-surface-map.md`
- `artifacts/code-auditing-split-map.md`
- `artifacts/legacy-code-audit-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`

## Validation

Validation results are recorded in
`artifacts/source-validation-results.md`.

Summary:

- `git diff --check`: pass.
- `make check-skills`: pass.
- Focused local Markdown link validation: 161 local links checked, 0 missing.
- `make collab-framework`: pass after sandbox escalation for generated
  `build/` and `target/skills/` writes.
- `make check-package-paths`: pass; 12 zips, 204 Markdown files, 0 hard
  failures, 368 warnings, 3 explicit exceptions, 656 skipped external URLs.
- `collaboration-framework.zip`: 74 files; all five code-auditing guides
  present; old `CODE-AUDIT.md` package entry absent.

## Ledger Walk

| ID | Final status | Evidence |
|----|--------------|----------|
| F-1 | done | Current source, route, package, and history surfaces are inventoried in `artifacts/current-code-auditing-surface-map.md`. |
| F-2 | done | All five accepted numbered guides exist in source and are mapped in `artifacts/code-auditing-split-map.md`. |
| F-3 | done | The split map and guide content preserve the diagnosis-only audit contract, audit map, language/tool detection, all-scale review, severity, file:line evidence, modernization synthesis, negative findings, final checklist, and no-code-change rule. |
| F-4 | done | `artifacts/legacy-code-audit-disposition.md` records the `git mv` from `CODE-AUDIT.md` to `01-audit-scope-and-map.md`, old-path live-route removal, and old package-entry absence. |
| F-5 | done | `artifacts/source-route-repair-map.md` records code-auditing, collaboration-framework, engineering-methods, project-management, public docs, AGENTS, release-note, Makefile, and package-exception repairs plus work-verification/testing no-ops. |
| F-6 | done | Source whitespace, skill-description, focused local-link, collaboration-framework package build, and full package-path validation passed with zero hard failures. |
| F-7 | done | Generated `collaboration-framework.zip` contains all five code-auditing guides and omits the old `CODE-AUDIT.md` path. |
| F-8 | done | This report records exact source commit, pending planning commit placeholder, explicit file lists, final statuses, row walk, and bubble-up. |

Rows: 8. Done: 8. Deferred: 0. No-op: 0.

## Clean Status

Source checkout was clean after source commit
`1eb10d789734d9cca5c2c0f7cdedb4257dfab1e6`.

Planning checkout cleanliness is checked after this close packet is committed.

## Bubble-Up to Arc08

Slice09 delivered the Arc08 A-9 capability: code-auditing guidance is split into
five accepted numbered guides without weakening the diagnosis-only audit
contract.

The slice revealed no arc-plan change requirement. The old-path disposition
follows the post-Slice08 pattern: focused guides are primary selective-load
targets, while old monolith paths remain only as historical lineage or explicit
disposition text.

Scope-as-specified versus scope-as-delivered:

- Delivered: five accepted guides, semantic preservation, old-path disposition,
  route repairs, package validation, source commit, planning artifacts, ledger
  update, and close report.
- Deferred: none.
- No-op: work-verification and testing source route repairs; no live old audit
  route existed there.
- Silent drops: none identified.

Slice10 can proceed to the agent-coordination guide split. It should preserve
the same pattern: focused guides are primary selective-load targets, and any
retained legacy prompt/template material must be explicitly dispositioned as
support material rather than left as a stale live route.
