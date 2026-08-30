# Slice 04: Model Synthesis and Acceptance

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice04 open set exists and declares the artifact home plus required artifacts | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|v40-conceptual-model.md|v40-model-decision-register.md|arc04-skill-architecture-handoff.md" slice-plan.md` | correctness-grade | slice-plan | done | Attested by CC on 2026-08-30; command found the open set, artifact home, and required artifact names. | Opening packet row. |
| F-2 | Required Slice04 artifacts exist | `test -f artifacts/v40-conceptual-model.md && test -f artifacts/v40-model-decision-register.md && test -f artifacts/arc04-skill-architecture-handoff.md` | correctness-grade | slice-plan | done | Attested by CC on 2026-08-30; command exited 0. | Durable artifact inventory. |
| F-3 | Conceptual model covers the required v4.0 constructs | `rg -n "concept card|claim|source span|source support|evidence grade|relationship|edge|competency question|CQ|extraction run|verifier|validation result|reconciliation|memory admission|v4.0 conceptual model" artifacts/v40-conceptual-model.md` | correctness-grade | slice-plan | done | Attested by CC on 2026-08-30; grep matched required constructs in `artifacts/v40-conceptual-model.md`. | Composition coverage row. |
| F-4 | Conceptual model preserves key invariants, boundaries, and lifecycle separation | `rg -n "one concept|atomicity|source-faithful|provenance|claim-source|attachment point|extraction confidence|source support|evidence grade|verification state|reconciliation state|memory admission|not one confidence field|lifecycle|preservation" artifacts/v40-conceptual-model.md` | correctness-grade | slice-plan | done | Attested by CC on 2026-08-30; grep matched invariants, attachment points, lifecycle separation, and preservation terms. | Boundary preservation row. |
| F-5 | Decision register records accepted, provisional, deferred, out-of-scope, and open decisions with routing | `rg -n "accepted|provisional|deferred|out of scope|open question|rationale|dependency|Slice01|Slice02|Slice03|Slice04|Arc04|Arc05" artifacts/v40-model-decision-register.md` | serious | slice-plan | done | Attested by CC on 2026-08-30; grep matched decision statuses, rationale, dependency notes, lineage, open questions, and routing. | Decision accountability row. |
| F-6 | Arc04 handoff names skill-architecture inputs without choosing final architecture | `rg -n "Arc04|skill architecture|SKILL.md|guide|template|validation script|example|package behavior|README|input|not final|does not choose|handoff|Arc03 close input" artifacts/arc04-skill-architecture-handoff.md` | serious | slice-plan | done | Attested by CC on 2026-08-30; grep matched architecture inputs and explicit non-decision language. | Handoff boundary row. |
| F-7 | Scope fences preserve later/source work | `rg -n "Out of scope|source edits|README|Makefile|generated zips|package behavior|final skill layout|schema syntax|enum spelling|validator implementation|GraphRAG runtime|memory runtime|ontology database|CCDP service|live extraction" slice-plan.md artifacts/v40-conceptual-model.md artifacts/v40-model-decision-register.md artifacts/arc04-skill-architecture-handoff.md` | correctness-grade | slice-plan | done | Attested by CC on 2026-08-30; grep matched the slice plan and all artifacts. | Later-work fence row. |
| F-8 | Source checkout remains clean | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | correctness-grade | standing instruction | done | Attested by CC on 2026-08-30; command exited 0. | Planning-only guardrail. |

## Closure

Closed as proposed-done on 2026-08-30 by CC/Codex. Independent CDC
verification remains required before this slice becomes verified-closed.

Rows: 8. Done: 8. Deferred: 0. No-op: 0.
