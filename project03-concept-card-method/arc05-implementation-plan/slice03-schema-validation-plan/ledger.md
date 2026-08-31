# Slice 03: Schema, Enum, and Validation Plan

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice03 open set exists with slice plan, ledger, prompt, and artifact home | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && test -d artifacts` | correctness-grade | slice-plan | open | | Open-set row. |
| F-2 | Required Slice03 planning artifacts are produced under the slice-local artifact home | `test -f artifacts/v40-schema-surface-plan.md && test -f artifacts/v40-enum-vocabulary-plan.md && test -f artifacts/v40-validation-review-plan.md && test -f artifacts/v40-validator-scope-test-plan.md` | correctness-grade | slice-plan | open | | Artifact home is `artifacts/`. |
| F-3 | Schema surface plan covers all v4.0 concept-card method record surfaces | `rg -n "concept card|claim|source support|source span|source locator|relationship edge|competency question|extraction run|validation result|verification result|reconciliation result|preservation decision|memory admission" artifacts/v40-schema-surface-plan.md` | correctness-grade | slice-plan | open | | Schema-surface coverage row. |
| F-4 | Schema surface plan maps schema surfaces to Slice02 planned paths without source edits | `rg -n "knowledge/concept-card-method|guides/templates|guides/examples|guides/validation|planned path|Slice02|does not edit source" artifacts/v40-schema-surface-plan.md` | correctness-grade | slice-plan | open | | Layout continuity row. |
| F-5 | Enum vocabulary plan names controlled vocabulary or enum spelling for lifecycle and support fields | `rg -n "evidence grade|extraction confidence|verification state|validation result|reconciliation state|CQ status|preservation decision|memory admission|source-support status|enum|controlled vocabulary" artifacts/v40-enum-vocabulary-plan.md` | correctness-grade | slice-plan | open | | Vocabulary row. |
| F-6 | Validation/review plan separates deterministic, semantic, human, and deferred runtime checks | `rg -n "deterministic structural|semantic audit|human/operator review|deferred runtime|can prove|cannot prove|evidence" artifacts/v40-validation-review-plan.md` | correctness-grade | slice-plan | open | | Evidence boundary row. |
| F-7 | Validator scope/test plan decides validator-code scope, test scope, and failure-output expectations | `rg -n "validator-code scope|source documentation|executable|deferred|test scope|invalid example|failure-output|failure message|manual" artifacts/v40-validator-scope-test-plan.md` | correctness-grade | slice-plan | open | | Validator planning row. |
| F-8 | Artifacts route packaging and release mechanics to Slice04 | `rg -n "README|library discoverability|Makefile|package target|package list|package-path|generated zip|release gate|package release|version history|Slice04" artifacts/v40-schema-surface-plan.md artifacts/v40-enum-vocabulary-plan.md artifacts/v40-validation-review-plan.md artifacts/v40-validator-scope-test-plan.md` | serious | slice-plan | open | | Later-slice routing row. |
| F-9 | Artifacts keep source edits, implementation, generated zips, package release, runtime services, and release readiness out of scope | `rg -n "out of scope|does not edit source|source implementation|generated zips|package release|release readiness|runtime|GraphRAG|graph database|ontology database|memory runtime|CCDP service|live extraction" slice-plan.md artifacts/v40-schema-surface-plan.md artifacts/v40-enum-vocabulary-plan.md artifacts/v40-validation-review-plan.md artifacts/v40-validator-scope-test-plan.md` | serious | operator constraint | open | | Planning-only row. |
| F-10 | Artifacts preserve accepted Arc03/Arc04 concepts and Slice02 layout decisions | `rg -n "Arc03|Arc04|accepted|conceptual model|skill architecture|Slice02|source layout|content sequence|knowledge/concept-card-method|guides/" artifacts/v40-schema-surface-plan.md artifacts/v40-enum-vocabulary-plan.md artifacts/v40-validation-review-plan.md artifacts/v40-validator-scope-test-plan.md` | serious | arc-plan | open | | Continuity row. |
| F-11 | Source checkout remains clean | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | operator constraint | open | | Source checkout must not change. |
| F-12 | New and modified Slice03 Markdown is ASCII-clean and has no trailing whitespace | `LC_ALL=C grep -RIn '[^ -~]' slice-plan.md ledger.md cc-prompt.md artifacts || true; grep -RIn '[[:blank:]]$' slice-plan.md ledger.md cc-prompt.md artifacts || true` | polish | repo hygiene | open | | Verification should print no matches. |

## What Worked

Pending.

## Closure

Status: open.
