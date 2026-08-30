# Slice 03: Relationship, CQ, and Run Semantics

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice03 open set exists and names the artifact home plus required artifacts | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|v40-graph-cq-run-semantics.md|v40-reconciliation-traceability-decision-register.md" slice-plan.md cc-prompt.md` | correctness-grade | slice-plan | open | | |
| F-2 | Required Slice03 artifacts exist under the slice-local artifact home | `test -f artifacts/v40-graph-cq-run-semantics.md && test -f artifacts/v40-reconciliation-traceability-decision-register.md` | correctness-grade | slice-plan | open | | |
| F-3 | Graph relationship/edge semantics cover v3.2 relationship carry-forward, endpoints, direction/inverse policy, graph closure, and evidence/reconciliation attachment | `rg -n "prerequisites|extends|related|contrasts_with|relationship|edge|endpoint|direction|inverse|symmetry|graph closure|evidence|reconciliation|attachment" artifacts/v40-graph-cq-run-semantics.md artifacts/v40-reconciliation-traceability-decision-register.md` | serious | arc-plan | open | | |
| F-4 | Competency-question semantics cover requirement, answerability, coverage, verification, retrieval, obsolete, and deferred roles or statuses | `rg -n "competency question|CQ|requirement|answerability|answerable|coverage|covered|verification|retrieval|obsolete|deferred|status" artifacts/v40-graph-cq-run-semantics.md artifacts/v40-reconciliation-traceability-decision-register.md` | serious | arc-plan | open | | |
| F-5 | Extraction-run semantics define traceability for source snapshot, method/prompt version, agent scope, outputs, old-card inputs, preservation, validation, reconciliation, and parallel-worker provenance | `rg -n "extraction run|traceability|source snapshot|method version|prompt version|agent scope|output set|generated|updated card|old-card|preservation|validation result|reconciliation result|parallel-worker|provenance" artifacts/v40-graph-cq-run-semantics.md artifacts/v40-reconciliation-traceability-decision-register.md` | serious | arc-plan | open | | |
| F-6 | Reconciliation semantics cover conflict classes, result records, affected constructs, and memory-admission dependencies without defining algorithms | `rg -n "reconciliation|duplicate concept|competing definition|slug drift|taxonomy drift|relationship asymmetry|CQ coverage|parallel-agent conflict|result record|affected cards|affected claims|relationships|runs|memory admission|algorithm" artifacts/v40-graph-cq-run-semantics.md artifacts/v40-reconciliation-traceability-decision-register.md` | correctness-grade | slice-plan | open | | |
| F-7 | Slice03 preserves scope fences and downstream routing for Slice04, Arc04, Arc05, and source-edit work | `rg -n "Out of scope|schema syntax|enum spelling|algorithm|graph database|GraphRAG runtime|memory runtime|ontology database|CCDP service|skill architecture|package behavior|README|Makefile|source edits|Slice04|Arc04|Arc05" slice-plan.md artifacts/v40-graph-cq-run-semantics.md artifacts/v40-reconciliation-traceability-decision-register.md` | correctness-grade | slice-plan | open | | |
| F-8 | Source checkout remains untouched during this planning-only slice | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | operator constraint | open | | |

## Closure

Slice remains open.
