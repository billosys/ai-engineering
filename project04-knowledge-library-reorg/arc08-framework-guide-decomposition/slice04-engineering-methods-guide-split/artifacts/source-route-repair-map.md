# Slice04 Source Route Repair Map

Date: 2026-09-04
Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`
Source commit: `0ad843dfff6e01bdc68a566e9b8907ac76da88b6`

## Support Inputs

- `../slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`
- `../slice01-split-map-version-history-confirmation/artifacts/source-impact-and-validation-plan.md`
- `../slice03-collaboration-framework-posture-split/cdc-verification.md`
- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`

## Source Files Repaired

| Source file | Repair |
|---|---|
| `Makefile` | Replaced old methodology monolith in `CF_FILES` with the six numbered guides and `knowledge/engineering-methods/version-history.md`. |
| `docs/ORIGINS.md` | Updated the methodology route to `01-engineering-methodology.md`. |
| `docs/collaboration-framework.md` | Updated the engineering-method source route to the split guide-set entrypoint. |
| `knowledge/collaboration-framework/SKILL.md` | Bumped to `1.5.1`; expanded the engineering-methods route table to all six guide files while preserving Slice03 posture routes and Slice02 Expedited Mode guardrails. |
| `knowledge/collaboration-framework/guides/04-component-route-table.md` | Expanded the operational component set to the six engineering-methods guides. |
| `knowledge/collaboration-framework/version-history.md` | Added a `1.5.1` entry for the route-surface update. |
| `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md` | Repaired methodology route to `01-engineering-methodology.md`. |
| `knowledge/engineering-methods/SKILL.md` | Bumped to `1.1.0`; replaced the old single-guide route with the six-guide list and sibling history pointer. |
| `knowledge/project-management/guides/02-canonical-planning-worktree.md` | Repaired methodology route to `01-engineering-methodology.md`. |
| `knowledge/project-management/guides/08-maintenance.md` | Repaired methodology route to `01-engineering-methodology.md`. |
| `knowledge/project-management/guides/PROJECT-MANAGEMENT.md` | Repaired methodology and Notes-for-Codex route to `01-engineering-methodology.md`. |
| `knowledge/project-management/version-history.md` | Repaired historical inline links that would otherwise point to the removed live path. |
| `knowledge/testing/guides/CODE-COVERAGE.md` | Repaired Notes-for-Codex route to `01-engineering-methodology.md`. |
| `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` | Repaired Notes-for-Codex route to `01-engineering-methodology.md`. |
| `workbench/release-notes/RELEASE-0.5.0.md` | Repaired release-note route to `01-engineering-methodology.md`; the file is ignored by default but was committed intentionally as a tracked release-note source. |

## Old Reference Scan

No live Markdown route in README/docs/AGENTS/SKILL/component guide surfaces points to `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`. Remaining old-filename mentions are version-history provenance in:

```text
knowledge/collaboration-framework/version-history.md
knowledge/engineering-methods/version-history.md
```

## Guardrail Preservation

The Slice02 Expedited Mode language remains in `knowledge/project-management/guides/PROJECT-MANAGEMENT.md` and in the collaboration-framework route table. The Slice03 posture guide routes remain in `knowledge/collaboration-framework/SKILL.md` and `knowledge/collaboration-framework/guides/04-component-route-table.md`.
