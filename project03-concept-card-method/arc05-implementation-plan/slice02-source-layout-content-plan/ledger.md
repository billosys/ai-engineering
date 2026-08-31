# Slice 02: Skill Source Layout and Content Sequence

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice02 open set exists with slice plan, ledger, prompt, and artifact home | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && test -d artifacts` | correctness-grade | slice-plan | open | | Open-set row. |
| F-2 | Required Slice02 planning artifacts are produced under the slice-local artifact home | `test -f artifacts/v40-source-layout-plan.md && test -f artifacts/v40-content-sequence-plan.md && test -f artifacts/v40-surface-routing-decision-register.md` | correctness-grade | slice-plan | open | | Artifact home is `artifacts/`. |
| F-3 | Source layout plan names the planned source home and exact planned paths for the v4.0 skill surfaces | `rg -n "source home|knowledge/|SKILL.md|guides/|template|example|validation documentation|support document|planned path" artifacts/v40-source-layout-plan.md` | correctness-grade | slice-plan | open | | Layout row. |
| F-4 | Source layout plan preserves the Slice01 package-behavior constraint or routes package behavior change to Slice04 | `rg -n "package behavior|SKILL.md plus sibling guides|guides/|Slice01|Slice04|package behavior change|package-compatible" artifacts/v40-source-layout-plan.md artifacts/v40-surface-routing-decision-register.md` | correctness-grade | slice-plan | open | | Prevents hidden package drift. |
| F-5 | Content sequence plan covers the thin SKILL.md load contract and operator workflow routing | `rg -n "thin SKILL.md|reason to load|positive load|negative load|problem ownership|dependency direction|operator workflow|guide routing|source edit sequencing" artifacts/v40-content-sequence-plan.md` | correctness-grade | slice-plan | open | | Load contract row. |
| F-6 | Content sequence plan names guide, template, example, cross-link, and first edit-order decisions | `rg -n "guide file|template file|example file|cross-link|first implementation|edit order|content sequence" artifacts/v40-content-sequence-plan.md artifacts/v40-source-layout-plan.md` | correctness-grade | slice-plan | open | | Source sequencing row. |
| F-7 | Decision register records accepted, deferred, and no-op decisions with owner or later-slice routing | `rg -n "accepted|deferred|no-op|owner|later slice|Slice03|Slice04|Slice05|Arc04 decision" artifacts/v40-surface-routing-decision-register.md` | correctness-grade | slice-plan | open | | Decision accountability row. |
| F-8 | Artifacts route schema, enum, validation, tests, package, release, and version-history questions to later Arc05 slices | `rg -n "schema syntax|enum spelling|validator-code|deterministic validation|tests|package target|package list|package-path|generated zip|release gate|version history|Slice03|Slice04|Slice05" artifacts/v40-source-layout-plan.md artifacts/v40-content-sequence-plan.md artifacts/v40-surface-routing-decision-register.md` | serious | slice-plan | open | | Later-slice routing row. |
| F-9 | Artifacts keep source edits, implementation, generated zips, package release, runtime services, and release readiness out of scope | `rg -n "out of scope|does not edit source|source implementation|generated zips|package release|release readiness|runtime|GraphRAG|graph database|ontology database|memory runtime|CCDP service|live extraction" slice-plan.md artifacts/v40-source-layout-plan.md artifacts/v40-content-sequence-plan.md artifacts/v40-surface-routing-decision-register.md` | serious | operator constraint | open | | Planning-only row. |
| F-10 | Source checkout remains clean | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | operator constraint | open | | Source checkout must not change. |
| F-11 | New and modified Slice02 Markdown is ASCII-clean and has no trailing whitespace | `LC_ALL=C grep -RIn '[^ -~]' slice-plan.md ledger.md cc-prompt.md artifacts || true; grep -RIn '[[:blank:]]$' slice-plan.md ledger.md cc-prompt.md artifacts || true` | polish | repo hygiene | open | | Verification should print no matches. |

## What Worked

Pending.

## Closure

Status: open.
