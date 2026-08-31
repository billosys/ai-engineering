# Slice 02: Load Contract and Ownership Model

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice02 open set exists with slice plan, ledger, prompt, and artifact home | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && test -d artifacts` | correctness-grade | slice-plan | open | | |
| F-2 | Required artifacts are produced under the slice-local artifact home | `test -f artifacts/v40-load-contract.md && test -f artifacts/v40-ownership-routing-model.md` | correctness-grade | slice-plan | open | | |
| F-3 | Load contract defines positive and negative load triggers plus thin SKILL.md routing | `rg -n "reason to load|when to load|load trigger|do not load|negative trigger|SKILL.md|thin entrypoint|route|guide" artifacts/v40-load-contract.md` | serious | slice-plan | open | | |
| F-4 | Ownership model defines problem ownership, non-ownership boundaries, and dependency direction | `rg -n "problem ownership|owns|does not own|non-ownership|dependency direction|adjacent guidance|collaboration-framework|project management|source reading|implementation planning|domain-knowledge" artifacts/v40-ownership-routing-model.md` | serious | slice-plan | open | | |
| F-5 | Operator workflow boundary covers extraction, re-extraction, verification, reconciliation, competency questions, and memory admission | `rg -n "operator workflow|extraction|re-extraction|verification|reconciliation|competency question|CQ|memory admission|five-agent|parallel-worker" artifacts/v40-load-contract.md artifacts/v40-ownership-routing-model.md` | serious | slice-plan | open | | |
| F-6 | Artifacts preserve Arc03 conceptual distinctions instead of collapsing them into one confidence or validation field | `rg -n "concept card|claim|source support|evidence grade|extraction confidence|verification state|validation result|reconciliation state|memory admission|not one confidence|distinct" artifacts/v40-load-contract.md artifacts/v40-ownership-routing-model.md` | correctness-grade | slice-plan | open | | |
| F-7 | Unresolved guide, template, validation, package, README, and source implementation questions are routed to later owners | `rg -n "Slice03|Slice04|Slice05|Arc05|guide|template|example|validation|package|README|Makefile|source edit|implementation planning" artifacts/v40-load-contract.md artifacts/v40-ownership-routing-model.md` | serious | slice-plan | open | | |
| F-8 | Slice scope fences keep final guide/template/package design, validator implementation, runtime services, and source edits out of scope | `rg -n "Out of scope|final guide|final template|package inclusion|README integration|Makefile|validator-code|deterministic validation|generated zips|runtime|live extraction|graph database|memory runtime|CCDP service|source checkout edits" slice-plan.md artifacts/v40-load-contract.md artifacts/v40-ownership-routing-model.md` | serious | slice-plan | open | | |
| F-9 | Source checkout remains clean | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | operator constraint | open | | |
| F-10 | New and modified Slice02 Markdown is ASCII-clean and has no trailing whitespace | `LC_ALL=C grep -RIn '[^ -~]' slice-plan.md ledger.md cc-prompt.md artifacts || true; grep -RIn '[[:blank:]]$' slice-plan.md ledger.md cc-prompt.md artifacts || true` | polish | repo hygiene | open | | Verify commands should print no matches. |

## What Worked

_(At slice close. Patterns that made the slice close cleanly.)_

## Closure

Slice remains open.
