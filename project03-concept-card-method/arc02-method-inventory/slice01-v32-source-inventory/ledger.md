# Slice 01: v3.2 Source Inventory

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice01 open set exists and names the standard artifact home | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|v32-source-inventory.md|v32-method-structure-map.md|v32-original-assessment.md|source-docs" slice-plan.md cc-prompt.md` | serious | slice-plan | open | | |
| F-2 | Preserved v3.2 source snapshots match the workbench inputs and the original assessment memo is present | `cmp -s /Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md artifacts/source-docs/0009-howto-concept-card-extraction-with-llms-v3.2.md && cmp -s /Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md artifacts/source-docs/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md && rg -n "Preserved Assessment|v3.2 is genuinely good|target to v4.0" artifacts/v32-original-assessment.md` | serious | operator direction | open | | |
| F-3 | Required inventory artifacts exist under the slice artifact home | `test -f artifacts/v32-source-inventory.md && test -f artifacts/v32-method-structure-map.md` | serious | slice-plan | open | | |
| F-4 | Source inventory covers both v3.2 docs and major method categories | `rg -n "0009-howto|0010-a-guide|schema|workflow|validation|provenance|relationship|competency question|confidence|re-extraction|preservation" artifacts/v32-source-inventory.md` | serious | slice-plan | open | | |
| F-5 | Structure map separates v3.2 baseline observations from later v4.0 questions | `rg -n "v3.2 baseline|v4.0 question|schema|workflow|validation|provenance|relationship|competency question|confidence|re-extraction|memory admission|CCDP" artifacts/v32-method-structure-map.md` | serious | slice-plan | open | | |
| F-6 | Slice remains inventory-only and defers v4.0 design | `rg -n "not design|without answering them prematurely|Out of scope|Designing the v4.0 conceptual model" slice-plan.md artifacts/v32-method-structure-map.md` | correctness-grade | slice-plan | open | | |
| F-7 | Source checkout remains unmodified | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | project boundary | open | | |

## Closure

Slice remains open.
