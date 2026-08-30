# Slice 01: Construct Boundaries

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice open set exists and names the slice-local artifact home plus required artifacts | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|v40-construct-boundary-model.md|v40-construct-decision-register.md" slice-plan.md cc-prompt.md` | correctness-grade | slice-plan | open | | Open-set row. |
| F-2 | Required construct-boundary artifacts exist under `artifacts/` | `test -f artifacts/v40-construct-boundary-model.md && test -f artifacts/v40-construct-decision-register.md` | correctness-grade | slice-plan | open | | Durable artifact placement row. |
| F-3 | Boundary model covers all Arc02 candidate constructs | `rg -n "concept card|claim|source span|evidence grade|relationship|edge|competency question|extraction run|verifier|reconciliation|memory admission" artifacts/v40-construct-boundary-model.md artifacts/v40-construct-decision-register.md` | correctness-grade | slice-plan | open | | Coverage row. |
| F-4 | Decision register classifies constructs and records rationale, dependencies, open questions, and downstream Arc03 routing | `rg -n "first-class entity|value object|status|role|process|result record|field|deferred concern|rationale|dependencies|open question|Slice02|Slice03|Slice04" artifacts/v40-construct-decision-register.md` | serious | slice-plan | open | | Boundary decision row. |
| F-5 | Artifacts preserve v3.2 carry-forward commitments while framing v4.0 changes as conceptual-model decisions | `rg -n "v3.2|carry forward|atomicity|source-faithful|provenance|typed relationships|competency questions|source-primary re-extraction|preservation|v4.0 conceptual model" artifacts/v40-construct-boundary-model.md artifacts/v40-construct-decision-register.md` | serious | slice-plan | open | | Preservation row. |
| F-6 | Scope fences defer evidence vocabulary, lifecycle transitions, skill layout, package behavior, deterministic validators, README changes, Makefile changes, and source edits | `rg -n "Out of scope|evidence-grade vocabulary|verification-state transitions|reconciliation algorithms|memory-admission policy|skill layout|package behavior|deterministic validator|README|Makefile|source edits" slice-plan.md artifacts/v40-construct-boundary-model.md artifacts/v40-construct-decision-register.md` | correctness-grade | slice-plan | open | | Boundary row. |
| F-7 | Source checkout remains unmodified | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | correctness-grade | standing instruction | open | | Planning-only row. |

## Closure

Slice remains open.

