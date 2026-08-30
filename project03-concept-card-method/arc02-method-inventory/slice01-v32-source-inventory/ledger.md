# Slice 01: v3.2 Source Inventory

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice01 open set exists and names the standard artifact home | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|v32-source-inventory.md|v32-method-structure-map.md|v32-original-assessment.md|source-docs" slice-plan.md cc-prompt.md` | serious | slice-plan | done | Attested on 2026-08-30: command found the open set, `artifact-home: artifacts/`, required inventory artifacts, original assessment, and source-docs references. | |
| F-2 | Preserved v3.2 source snapshots match the workbench inputs and the original assessment memo is present | `cmp -s /Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md artifacts/source-docs/0009-howto-concept-card-extraction-with-llms-v3.2.md && cmp -s /Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md artifacts/source-docs/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md && rg -n "Preserved Assessment|v3.2 is genuinely good|target to v4.0" artifacts/v32-original-assessment.md` | serious | operator direction | done | Attested on 2026-08-30: both `cmp -s` checks passed and `rg` found the preserved assessment plus v4.0 numbering note. | |
| F-3 | Required inventory artifacts exist under the slice artifact home | `test -f artifacts/v32-source-inventory.md && test -f artifacts/v32-method-structure-map.md` | serious | slice-plan | done | Attested on 2026-08-30: both required inventory artifacts exist under `artifacts/`. | |
| F-4 | Source inventory covers both v3.2 docs and major method categories | `rg -n "0009-howto|0010-a-guide|schema|workflow|validation|provenance|relationship|competency question|confidence|re-extraction|preservation" artifacts/v32-source-inventory.md` | serious | slice-plan | done | Attested on 2026-08-30: command found both source docs and all required category terms in `artifacts/v32-source-inventory.md`. | |
| F-5 | Structure map separates v3.2 baseline observations from later v4.0 questions | `rg -n "v3.2 baseline|v4.0 question|schema|workflow|validation|provenance|relationship|competency question|confidence|re-extraction|memory admission|CCDP" artifacts/v32-method-structure-map.md` | serious | slice-plan | done | Attested on 2026-08-30: command found baseline framing, later v4.0 question prompts, and all required method categories in `artifacts/v32-method-structure-map.md`. | |
| F-6 | Slice remains inventory-only and defers v4.0 design | `rg -n "not design|without answering them prematurely|Out of scope|Designing the v4.0 conceptual model" slice-plan.md artifacts/v32-method-structure-map.md` | correctness-grade | slice-plan | done | Attested on 2026-08-30: command found the slice-plan out-of-scope language and structure-map scope fence deferring v4.0 design. | |
| F-7 | Source checkout remains unmodified | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | project boundary | done | Attested on 2026-08-30: implementation source checkout diff was quiet. | |

## Closure

Closed as proposed-done on 2026-08-30 by CC/Codex. Independent CDC
verification remains required before this slice becomes verified-closed.

Rows: 7. Done: 7. Deferred: 0. No-op: 0.
