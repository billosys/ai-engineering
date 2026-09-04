# Arc 07: Knowledge Component Entrypoints and Guide Layout

## Arc Ledger

Capability: Arc07 resolves post-move framework component source layout by
settling component entrypoints, removing stale `docs/` holdovers, preserving
package/install behavior, and reconciling docs/release surfaces.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 closes with component layout inventory, SKILL.md/guide/template decision register, migration impact map, validation command inventory, and implementation slice roadmap | `test -f slice01-component-entrypoint-contract/cdc-verification.md && rg -n "component layout|SKILL.md|guide|template|migration impact|validation command|implementation slice roadmap|verified-closed" slice01-component-entrypoint-contract/cdc-verification.md` | serious | arc-plan | done | verified: `slice01-component-entrypoint-contract/cdc-verification.md` records component layout, SKILL.md/guide/template decisions, migration impact, validation command inventory, implementation slice roadmap, and verified-closed status. | Read-only contract evidence before source moves. |
| A-2 | Slice02 closes with collaboration-framework entrypoint relocated from repository root to knowledge/collaboration-framework while package/install behavior remains valid | `test -f slice02-collaboration-framework-entrypoint-relocation/cdc-verification.md && rg -n "collaboration-framework/SKILL.md|root SKILL|Makefile|CF_FILES|ALL_SKILL_FILES|package root|install|verified-closed" slice02-collaboration-framework-entrypoint-relocation/cdc-verification.md` | correctness-grade | arc-plan | done | verified: `slice02-collaboration-framework-entrypoint-relocation/cdc-verification.md` records relocated source entrypoint, root SKILL.md absence, Makefile/CF_FILES/ALL_SKILL_FILES updates, package root, install/package behavior, and verified-closed status. | Top-level skill entrypoint move evidence. |
| A-3 | Slice03 closes with accepted component guide layout implemented, stale docs/ holdovers removed or dispositioned, project-management guides moved, and component SKILL.md decisions applied | `test -f slice03-component-guide-layout/cdc-verification.md && rg -n "agent-coordination|code-auditing|collaboration-framework|contribution-style|engineering-methods|project-management|guides|SKILL.md|docs/ holdover|verified-closed" slice03-component-guide-layout/cdc-verification.md` | correctness-grade | arc-plan | done | verified: `slice03-component-guide-layout/cdc-verification.md` records agent-coordination, code-auditing, collaboration-framework, contribution-style, engineering-methods, project-management, testing, work-verification, guides, SKILL.md entrypoints, docs/ holdover removal, and verified-closed status. | Component source layout evidence. |
| A-4 | Slice04 closes with README/docs links, skill/package/install validation, package-path checks, and release notes reconciled after Arc07 source moves | `test -f slice04-reconciliation-package-validation/cdc-verification.md && rg -n "README|docs/|check-skills|collab-framework|check-package-paths|install smoke|release notes|verified-closed" slice04-reconciliation-package-validation/cdc-verification.md` | correctness-grade | arc-plan | done | verified: `slice04-reconciliation-package-validation/cdc-verification.md` records README/docs links, check-skills, collab-framework, make all, check-package-paths, install smoke, release notes, CCDP validation, and verified-closed status. | Final validation evidence. |
| A-5 | Arc07 composition demonstrates accepted knowledge component entrypoints and guide layout without path/package ambiguity | `test -f closing-report.md && rg -n "Composition verdict: delivered|component entrypoint|SKILL.md|guides|docs/ holdover|package|install|reconciled" closing-report.md` | serious | arc-plan | done | reproduced: `closing-report.md` records `Composition verdict: delivered`, component entrypoints, `SKILL.md`, guides, docs/ holdover cleanup, package, install, and reconciled release/package evidence. | Arc close composition evidence. |

## Closure

Arc is closed. Slice01 through Slice04 are verified-closed and the arc
composition row is done.

Rows: 5. Done: 5. Deferred: 0. No-op: 0.
