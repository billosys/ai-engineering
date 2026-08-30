# Arc 02: Method Inventory and Gap Analysis

## Arc Ledger

Capability: inventory the v3.2 baseline docs from source and identify
source-backed gaps that justify the v4.0 method revision.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closed with CDC verification | `test -f slice01-v32-source-inventory/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice01-v32-source-inventory/cdc-verification.md` | correctness-grade | arc-plan | done | Attested by pointer to `slice01-v32-source-inventory/cdc-verification.md`; spot-checked by CDC on 2026-08-30. | Children-closed row. |
| A-2 | Slice 02 closed with CDC verification | `test -f slice02-v40-gap-analysis/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice02-v40-gap-analysis/cdc-verification.md` | correctness-grade | arc-plan | open | | Children-closed row. |
| A-3 | Slice 03 closed with CDC verification | `test -f slice03-inventory-synthesis/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice03-inventory-synthesis/cdc-verification.md` | correctness-grade | arc-plan | open | | Children-closed row. |
| A-4 | v3.2 baseline is preserved and the inventory covers both source docs and the method's schema, workflow, validation, provenance, relationships, competency questions, confidence, and re-extraction mechanics | `cmp -s /Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md slice01-v32-source-inventory/artifacts/source-docs/0009-howto-concept-card-extraction-with-llms-v3.2.md && cmp -s /Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md slice01-v32-source-inventory/artifacts/source-docs/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md && rg -n "Preserved Assessment|v3.2 is genuinely good|target to v4.0" slice01-v32-source-inventory/artifacts/v32-original-assessment.md && rg -n "0009|0010|schema|workflow|validation|provenance|relationship|competency question|confidence|re-extraction|preservation" slice01-v32-source-inventory/artifacts/v32-source-inventory.md slice01-v32-source-inventory/artifacts/v32-method-structure-map.md` | serious | arc-plan | open | | Reproduce at arc scale. |
| A-5 | v4.0 gap analysis distinguishes source-preserving carry-forward items from architectural changes | `rg -n "v3.2 baseline|v4.0|carry forward|architectural change|evidence grade|verification|reconciliation|memory admission|CCDP|skill packaging" slice02-v40-gap-analysis slice03-inventory-synthesis` | serious | arc-plan | open | | Reproduce at arc scale. |
| A-6 | Arc02 synthesis leaves explicit inputs for Arc03 conceptual-model work | `rg -n "Arc03|conceptual model|concept card|source span|claim|evidence grade|relationship|competency question|extraction run|memory admission" slice03-inventory-synthesis` | correctness-grade | arc-plan | open | | Reproduce at arc scale. |

## Closure

Arc remains open.
