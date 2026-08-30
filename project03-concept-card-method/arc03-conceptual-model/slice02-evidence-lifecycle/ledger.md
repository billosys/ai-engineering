# Slice 02: Evidence and Lifecycle Semantics

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice02 open set exists and names the artifact home plus required artifacts | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|v40-evidence-lifecycle-model.md|v40-evidence-state-decision-register.md" slice-plan.md cc-prompt.md` | correctness-grade | slice-plan | done | Reproduced by CDC on 2026-08-30; command found the open set, artifact home, and required artifact names. | |
| F-2 | Required Slice02 artifacts exist under the slice-local artifact home | `test -f artifacts/v40-evidence-lifecycle-model.md && test -f artifacts/v40-evidence-state-decision-register.md` | correctness-grade | slice-plan | done | Reproduced by CDC on 2026-08-30; command exited 0. | |
| F-3 | Lifecycle model separates extraction confidence, source support, evidence grade, verification state/result, reconciliation state/result, and memory admission rather than treating them as one confidence field | `rg -n "extraction confidence|source support|evidence grade|verification state|verification result|reconciliation state|reconciliation result|memory admission|not one confidence field|distinct" artifacts/v40-evidence-lifecycle-model.md` | serious | arc-plan | done | Reproduced by CDC on 2026-08-30; grep matched the lifecycle model. | |
| F-4 | Lifecycle model and decision register define attachment points for evidence/lifecycle concerns | `rg -n "concept card|claim|source span|claim-source|support relationship|extraction run|verifier|result record|attaches to|attachment point|lifecycle gate" artifacts/v40-evidence-lifecycle-model.md artifacts/v40-evidence-state-decision-register.md` | serious | arc-plan | done | Reproduced by CDC on 2026-08-30; grep matched both artifacts. | |
| F-5 | Decision register records lifecycle decisions with status, rationale, dependencies, open questions, and downstream routing | `rg -n "accepted|provisional|deferred|status|rationale|dependencies|open question|downstream|Slice03|Slice04|Arc04|Arc05" artifacts/v40-evidence-state-decision-register.md` | correctness-grade | slice-plan | done | Reproduced by CDC on 2026-08-30; grep matched the decision register. | |
| F-6 | Slice02 preserves scope fences for later schema, graph/CQ/run, skill architecture, package, and source-edit work | `rg -n "Out of scope|schema syntax|enum spelling|relationship or edge semantics|competency-question semantics|extraction-run trace|skill architecture|package behavior|README|Makefile|source edits" slice-plan.md artifacts/v40-evidence-lifecycle-model.md artifacts/v40-evidence-state-decision-register.md` | correctness-grade | slice-plan | done | Reproduced by CDC on 2026-08-30; grep matched the slice plan and artifacts. | |
| F-7 | Source checkout remains untouched during this planning-only slice | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | operator constraint | done | Reproduced by CDC on 2026-08-30; command exited 0. | |

## Closure

Verified-closed on 2026-08-30 by Codex Desktop CDC pass.

Rows: 7. Done: 7. Deferred: 0. No-op: 0.
