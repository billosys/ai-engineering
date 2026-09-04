# Slice 01: Component Entrypoint Contract and Migration Map

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Current component layout and reference map records root SKILL.md, named component roots, adjacent testing/work-verification surfaces, README/docs/root-SKILL references, Makefile CF_FILES/ALL_SKILL_FILES, and package-path exception surfaces | `rg -n "current component layout|root SKILL.md|agent-coordination|code-auditing|collaboration-framework|contribution-style|engineering-methods|project-management|testing|work-verification|README|docs/|CF_FILES|ALL_SKILL_FILES|package-path" artifacts/current-component-layout-and-reference-map.md` | serious | slice-plan | open | | Source-backed inventory before moves. |
| F-2 | Component entrypoint decision register answers SKILL.md versus guide/template handling for each named component, including the collaboration-framework root entrypoint and project-management guides decision | `rg -n "component entrypoint decision|SKILL.md|guide|template|collaboration-framework/SKILL.md|project-management/guides|agent-coordination|code-auditing|contribution-style|engineering-methods|decision" artifacts/component-entrypoint-decision-register.md` | correctness-grade | slice-plan | open | | Prevents blind renames. |
| F-3 | Source migration impact map records source path to target path moves, affected links, Makefile/package changes, package-path exceptions, release-note impact, and validation risks | `rg -n "source migration impact|source path|target path|Makefile|CF_FILES|ALL_SKILL_FILES|README|docs/|package-path exceptions|release note|validation risk" artifacts/source-migration-impact-map.md` | serious | slice-plan | open | | Implementation handoff evidence. |
| F-4 | Validation command inventory records required source/package/link/install checks for later implementation slices and explicitly dispositions CCDP validation | `rg -n "validation command inventory|git status|diff --check|check-skills|collab-framework|make all|check-package-paths|install smoke|package inspection|CCDP|disposition" artifacts/validation-command-inventory.md` | serious | slice-plan | open | | Validation handoff evidence. |
| F-5 | Implementation slice roadmap proposes follow-on slices with explicit source-edit authorization boundaries, commit scope, and sequencing | `rg -n "implementation slice roadmap|Slice02|Slice03|Slice04|source-edit authorization|commit scope|sequence|entrypoint relocation|guide layout|reconciliation" artifacts/implementation-slice-roadmap.md` | serious | slice-plan | open | | Next-slice planning evidence. |
| F-6 | Closing report walks all six rows, states source/planning status, and bubbles findings up to Arc07 | `test -f closing-report.md && rg -n "Rows: 6|Done:|Deferred:|No-op:|source checkout|planning checkout|Bubble-Up to Arc07|SKILL.md|guides|docs/ holdover|silent-drop" closing-report.md` | serious | slice-plan | open | | Slice close evidence. |

## Closure

Slice is open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
