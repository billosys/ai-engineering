# Slice 04: Arc02 Implementation Handoff

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Arc03 readiness packet consumes verified Slice01-Slice03 evidence and summarizes accepted contract, migration, validation, and exception policy | `rg -n "Arc03 readiness|Slice01|Slice02|Slice03|verified-closed|accepted target directory contract|source-package root contract|migration sequence|validation matrix|package-path exception policy" artifacts/arc03-readiness-packet.md` | serious | slice-plan | open | | Must prepare implementation without reopening Arc02 decisions. |
| F-2 | Source-edit slice roadmap orders preflight, mechanical moves, compatibility shims/wrappers, package/list/link updates, validation, and later prose/doc work | `rg -n "preflight|source status|mechanical move|compatibility shim|wrapper|migration note|package/list update|package-local link repair|validation gate|prose rewrite|Arc04|Arc05" artifacts/source-edit-slice-roadmap.md` | serious | slice-plan | open | | Must keep mechanical moves and prose rewrites separate. |
| F-3 | Decision summary records accepted contract decisions, operator gates, explicit exceptions, and re-entry conditions | `rg -n "accepted contract|operator gate|top-level SKILL.md|validated shim|replacement route|no-shim|persistent package-path exception|Biome|selected-file|CCDP remains separate|re-entry condition" artifacts/arc02-decision-summary.md` | serious | slice-plan | open | | Must preserve unresolved operator decisions rather than burying them. |
| F-4 | Artifacts preserve source-edit boundary and route implementation/public docs/vocabulary to later arcs | `rg -n "source-files-edited: false|not source-edit authorization|Arc03 implementation|Arc04|end-user docs|Arc05|public vocabulary|planning only|source checkout remains untouched" artifacts/*.md` | serious | slice-plan | open | | This slice is planning handoff only. |
| F-5 | Artifacts prepare Arc02 arc-close composition row without prematurely closing the arc | `rg -n "Arc02 composition|not arc close|formal arc close|target layout|path contract|migration plan|compatibility|exception|source root|package root|atomic|composite" artifacts/*.md` | correctness-grade | slice-plan | open | | Arc close remains CDC/arc-level work after Slice04 verification. |
| F-6 | Closing report walks all six rows, states source checkout remains untouched, and bubbles usable findings up to Arc02 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout remains untouched|Bubble-Up to Arc02|silent-drop" closing-report.md` | serious | slice-plan | open | | Close-set document; do not create before evidence exists. |

## Closure

Slice remains open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
