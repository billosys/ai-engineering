# Slice 02: Accepted Directory and Root Contract

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Accepted target directory contract selects concrete rules for docs, knowledge, templates, protocols, README, SKILL, wrappers, and exceptions | `rg -n "accepted target directory contract|docs/|knowledge/|templates/|protocols/ccdp|README|SKILL.md|wrapper|migration note|explicit exception" artifacts/accepted-target-directory-contract.md` | serious | slice-plan | open | | Must choose rules, not just list options. |
| F-2 | Source/package root contract separates source-root rules from package-root rules and covers major surface classes | `rg -n "source root rule|package root rule|frontmatter|selected-file|domain/tooling|framework/operational|method|collaboration-framework|concept-card-method|Biome|multi-entrypoint|CCDP" artifacts/source-package-root-contract.md` | serious | slice-plan | open | | Avoid source root equals package root collapse. |
| F-3 | Operator decision register dispositions D-1 through D-12 with no unlabeled unresolved decisions | `rg -n "D-1|D-2|D-3|D-4|D-5|D-6|D-7|D-8|D-9|D-10|D-11|D-12|accepted|adjusted|rejected|operator decision required|no unlabeled unresolved decisions" artifacts/operator-decision-register.md` | serious | slice-plan | open | | Remaining operator-sensitive choices must be explicit. |
| F-4 | Contract preserves Project02 accepted facts, Project03 planned-surface facts, CCDP separation, Biome edge case, and kind/topology independence | `rg -n "Project02 accepted|daily-driver composer|Project03 planned|not live source|CCDP remains separate|Biome|skill kind|topology|atomic|composite|bridge/integration" artifacts/*.md` | serious | slice-plan | open | | Prevent premature or tautological closure. |
| F-5 | Artifacts preserve the planning/source boundary and route migration/validation detail to later slices | `rg -n "source-files-edited: false|not source-edit authorization|Arc03|Slice03|migration sequence|validation matrix|implementation arc|public vocabulary" artifacts/*.md` | correctness-grade | slice-plan | open | | Planning contract only; later slices/arc own execution. |
| F-6 | Closing report walks all six rows, states source checkout remains untouched, and bubbles usable findings up to Arc02 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout remains untouched|Bubble-Up to Arc02|silent-drop" closing-report.md` | serious | slice-plan | open | | Close-set document; do not create before evidence exists. |

## Closure

Slice remains open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
