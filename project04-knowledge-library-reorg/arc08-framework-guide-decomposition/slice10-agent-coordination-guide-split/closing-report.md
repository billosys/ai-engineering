# Closing Report: Slice 10 Agent-Coordination Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice10-agent-coordination-guide-split
status: proposed-done
closed-by: CC
closed-on: 2026-09-05
source_commit: 9e2d5d055712efb53028ef250091d70487a257a0
planning_commit: pending until this report is committed
```

## Verdict

Slice10 is proposed-done pending CDC verification.

The source commit split agent-coordination guidance into four selective-load
guides without weakening the thinking-versus-lookup delegation boundary. The
old `SUBAGENT-DELEGATION-POLICY.md` path was moved with `git mv` to
`01-when-to-delegate.md`, semantically extracted into companion guides, and
removed as a live source/package route.

## Commits

Source commit:
`9e2d5d055712efb53028ef250091d70487a257a0`

Planning commit:
pending until this report is committed

## Explicit File Lists

Source explicit file list:

- `AGENTS.md`
- `Makefile`
- `docs/ORIGINS.md`
- `docs/collaboration-framework.md`
- `knowledge/agent-coordination/SKILL.md`
- `knowledge/agent-coordination/guides/01-when-to-delegate.md`
- `knowledge/agent-coordination/guides/02-context-packets.md`
- `knowledge/agent-coordination/guides/03-result-integration.md`
- `knowledge/agent-coordination/guides/04-anti-patterns.md`
- `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`
- `knowledge/agent-coordination/version-history.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/version-history.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

Planning explicit file list:

- `arc08-framework-guide-decomposition/slice10-agent-coordination-guide-split/artifacts/current-agent-coordination-surface-map.md`
- `arc08-framework-guide-decomposition/slice10-agent-coordination-guide-split/artifacts/agent-coordination-split-map.md`
- `arc08-framework-guide-decomposition/slice10-agent-coordination-guide-split/artifacts/legacy-subagent-policy-disposition.md`
- `arc08-framework-guide-decomposition/slice10-agent-coordination-guide-split/artifacts/source-route-repair-map.md`
- `arc08-framework-guide-decomposition/slice10-agent-coordination-guide-split/artifacts/source-validation-results.md`
- `arc08-framework-guide-decomposition/slice10-agent-coordination-guide-split/ledger.md`
- `arc08-framework-guide-decomposition/slice10-agent-coordination-guide-split/closing-report.md`

## Artifact Inventory

Durable Slice10 artifacts live under `artifacts/`:

- `artifacts/current-agent-coordination-surface-map.md`
- `artifacts/agent-coordination-split-map.md`
- `artifacts/legacy-subagent-policy-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`

## Validation

Validation results are recorded in
`artifacts/source-validation-results.md`.

Summary:

- `git diff --check`: pass.
- `make check-skills`: pass.
- Focused local Markdown link validation: 148 local links checked, 0 missing.
- `make collab-framework`: pass after sandbox escalation for generated
  `build/` and `target/skills/` writes.
- `make check-package-paths`: pass; 12 zips, 207 Markdown files, 0 hard
  failures, 364 warnings, 3 explicit exceptions, 656 skipped external URLs.
- `collaboration-framework.zip`: 77 files; all four agent-coordination guides
  present; old `SUBAGENT-DELEGATION-POLICY.md` package entry absent.

## Ledger Walk

| ID | Final status | Evidence |
|----|--------------|----------|
| F-1 | done | Current source, route, package, and history surfaces are inventoried in `artifacts/current-agent-coordination-surface-map.md`. |
| F-2 | done | All four accepted numbered guides exist in source and are mapped in `artifacts/agent-coordination-split-map.md`. |
| F-3 | done | The split map, entrypoint, and guide content preserve the thinking-vs-lookup boundary, main/parent-context judgment, context-packet constraints, result integration, anti-patterns, quality-over-elapsed-time rule, and CC/CDC/Operator terms. |
| F-4 | done | `artifacts/legacy-subagent-policy-disposition.md` records the `git mv` from `SUBAGENT-DELEGATION-POLICY.md` to `01-when-to-delegate.md`, old-path live-route removal, and old package-entry absence. |
| F-5 | done | `artifacts/source-route-repair-map.md` records agent-coordination, collaboration-framework, engineering-methods, public docs, AGENTS, release-note, and Makefile repairs plus package-exception no-op. |
| F-6 | done | Source whitespace, skill-description, focused local-link, collaboration-framework package build, and full package-path validation passed with zero hard failures. |
| F-7 | done | Generated `collaboration-framework.zip` contains all four agent-coordination guides and omits the old `SUBAGENT-DELEGATION-POLICY.md` path. |
| F-8 | done | This report records exact source commit, pending planning commit placeholder, explicit file lists, final statuses, row walk, and bubble-up. |

Rows: 8. Done: 8. Deferred: 0. No-op: 0.

## Clean Status

Source checkout was clean after source commit
`9e2d5d055712efb53028ef250091d70487a257a0`.

Planning checkout cleanliness is checked after this close packet is committed.

## Bubble-Up to Arc08

Slice10 delivered the Arc08 A-10 capability: agent-coordination guidance is
split into four accepted numbered guides with CC/CDC/Operator terminology
preserved in the component entrypoint.

The slice revealed no arc-plan change requirement. The old-path disposition
follows the post-Slice09 pattern: focused guides are primary selective-load
targets, while old monolith paths remain only as historical lineage or explicit
disposition text.

Scope-as-specified versus scope-as-delivered:

- Delivered: four accepted guides, semantic preservation, old-path disposition,
  route repairs, package validation, source commit, planning artifacts, ledger
  update, and close report.
- Deferred: none.
- No-op: package-path exception repair; no old agent-coordination exception
  existed and no new exception was required.
- Silent drops: none identified.

Slice11 can proceed to the contribution-style guide split. It should preserve
the same pattern: focused guides are primary selective-load targets, and any
retained legacy prompt/template material must be explicitly dispositioned as
support material rather than left as a stale live route.
