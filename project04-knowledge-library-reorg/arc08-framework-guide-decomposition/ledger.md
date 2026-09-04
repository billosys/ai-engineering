# Arc 08: Framework Guide Decomposition and Version History Normalization

## Arc Ledger

Capability: Arc08 splits accepted framework monolith guides into focused
loadable guides, normalizes framework component version history into sibling
files, tightens Expedited Mode wording, and verifies source/package/install
behavior after the semantic decomposition.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 closes with operator-confirmed split map, version-history normalization contract, source-impact map, and exact Expedited Mode wording target before source edits start | `test -f slice01-split-map-version-history-confirmation/cdc-verification.md && rg -n "operator-confirmed|split map|version-history|Expedited Mode|source-impact|no source edits|verified-closed" slice01-split-map-version-history-confirmation/cdc-verification.md` | correctness-grade | arc-plan | open | | Operator approval gate before source decomposition. |
| A-2 | Slice02 closes with Expedited Mode wording corrected in project-management and collaboration-framework route surfaces, and project-management version-history moved to a sibling component history file | `test -f slice02-project-management-process-history/cdc-verification.md && rg -n "Expedited Mode|only changes|no shortcuts|operator approval gate|collaboration-framework/SKILL.md|project-management/version-history.md|guides/version-history.md|verified-closed" slice02-project-management-process-history/cdc-verification.md` | correctness-grade | arc-plan | open | | Process guardrail and first version-history normalization. |
| A-3 | Slice03 closes with collaboration-framework posture material split into the four approved numbered guides and old monolith path removed or explicitly dispositioned | `test -f slice03-collaboration-framework-posture-split/cdc-verification.md && rg -n "01-posture-and-ethics|02-structural-pulls|03-collaborative-rights|04-component-route-table|AI-CONSTITUTION-SUPPLEMENT|version-history|selective loading|verified-closed" slice03-collaboration-framework-posture-split/cdc-verification.md` | correctness-grade | arc-plan | open | | Collaboration-framework selective-load evidence. |
| A-4 | Slice04 closes with engineering-methods methodology material split into the six accepted numbered guides and old monolith path removed or explicitly dispositioned | `test -f slice04-engineering-methods-guide-split/cdc-verification.md && rg -n "01-engineering-methodology|02-knowledge-substrate|03-process-rigour|04-operational-routing|05-component-boundary-analysis|06-source-package-release-gates|AI-ENGINEERING-METHODOLOGY|version-history|verified-closed" slice04-engineering-methods-guide-split/cdc-verification.md` | correctness-grade | arc-plan | open | | Engineering-methods selective-load evidence. |
| A-5 | Slice05 closes with remaining framework component version-history files normalized as siblings and embedded histories moved or explicitly dispositioned | `test -f slice05-component-version-history-normalization/cdc-verification.md && rg -n "work-verification|testing|code-auditing|agent-coordination|contribution-style|version-history.md|embedded Version History|sibling|verified-closed" slice05-component-version-history-normalization/cdc-verification.md` | correctness-grade | arc-plan | open | | Framework-wide version-history contract evidence. |
| A-6 | Slice06 closes with README/docs/AGENTS/SKILL links, package validation, install smoke, CCDP disposition, and release notes reconciled after the guide split | `test -f slice06-final-validation-release-reconciliation/cdc-verification.md && rg -n "README|docs|AGENTS|SKILL|check-skills|check-package-paths|install smoke|ccdp|release notes|monolith|verified-closed" slice06-final-validation-release-reconciliation/cdc-verification.md` | correctness-grade | arc-plan | open | | Final reconciliation evidence. |
| A-7 | Arc08 composition demonstrates that focused guide routes replace monolith live-load targets, framework usability is preserved, and selective loading/access is improved | `test -f closing-report.md && rg -n "Composition verdict: delivered|focused guides|monolith|live load targets|selective loading|version-history|Expedited Mode|package|install|reconciled" closing-report.md` | serious | arc-plan | open | | Reproduce at arc close. |

## Closure

Arc is open. Slice01 is open as the operator-confirmation gate before source
decomposition.

Rows: 7. Done: 0. Deferred: 0. No-op: 0.
