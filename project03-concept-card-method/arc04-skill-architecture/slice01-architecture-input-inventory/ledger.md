# Slice 01: Architecture Input Inventory

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice01 open set exists with slice plan, ledger, prompt, and artifact home | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && test -d artifacts` | correctness-grade | slice-plan | open | | |
| F-2 | Required artifacts are produced under the slice-local artifact home | `test -f artifacts/arc04-architecture-input-inventory.md && test -f artifacts/arc04-decision-question-map.md` | correctness-grade | slice-plan | open | | |
| F-3 | Architecture input inventory covers accepted conceptual-model commitments and candidate skill surfaces | `rg -n "concept card|claim|source support|evidence grade|verification|reconciliation|memory admission|SKILL.md|guide|template|validation candidate|example|README|package behavior|maintenance ownership" artifacts/arc04-architecture-input-inventory.md` | serious | slice-plan | open | | |
| F-4 | Decision-question map covers the required architecture decision axes | `rg -n "reason to load|problem ownership|dependency direction|package behavior|maintenance ownership|validation determinism|operator workflow|decision owner" artifacts/arc04-decision-question-map.md` | serious | slice-plan | open | | |
| F-5 | Decision-question map routes unresolved decisions to later Arc04 slices or Arc05 | `rg -n "Slice02|Slice03|Slice04|Slice05|Arc05|load contract|guide|template|validation|package|architecture synthesis|implementation planning" artifacts/arc04-decision-question-map.md` | serious | slice-plan | open | | |
| F-6 | Slice scope fences keep final architecture, source edits, runtime services, and implementation mechanics out of scope | `rg -n "Out of scope|final skill architecture|final file layout|source .*SKILL.md|README|Makefile|validator-code|generated zips|runtime services|live extraction|graph database|memory runtime|CCDP service" slice-plan.md artifacts/arc04-architecture-input-inventory.md artifacts/arc04-decision-question-map.md` | serious | slice-plan | open | | |
| F-7 | Source checkout remains clean | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | operator constraint | open | | |
| F-8 | New and modified Slice01 Markdown is ASCII-clean and has no trailing whitespace | `LC_ALL=C grep -RIn '[^ -~]' slice-plan.md ledger.md cc-prompt.md artifacts || true; grep -RIn '[[:blank:]]$' slice-plan.md ledger.md cc-prompt.md artifacts || true` | polish | repo hygiene | open | | Verify commands should print no matches. |

## What Worked

_(At slice close. Patterns that made the slice close cleanly.)_

## Closure

Slice remains open.
