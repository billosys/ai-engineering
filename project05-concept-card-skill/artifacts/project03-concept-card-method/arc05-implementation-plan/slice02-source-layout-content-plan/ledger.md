# Slice 02: Skill Source Layout and Content Sequence

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice02 open set exists with slice plan, ledger, prompt, and artifact home | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && test -d artifacts` | correctness-grade | slice-plan | done | closing-report.md | Local CC verification passed on 2026-08-31. |
| F-2 | Required Slice02 planning artifacts are produced under the slice-local artifact home | `test -f artifacts/v40-source-layout-plan.md && test -f artifacts/v40-content-sequence-plan.md && test -f artifacts/v40-surface-routing-decision-register.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-source-layout-plan.md; artifacts/v40-content-sequence-plan.md; artifacts/v40-surface-routing-decision-register.md | Artifact home is `artifacts/`. |
| F-3 | Source layout plan names the planned source home and exact planned paths for the v4.0 skill surfaces | `rg -n "source home|knowledge/|SKILL.md|guides/|template|example|validation documentation|support document|planned path" artifacts/v40-source-layout-plan.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-source-layout-plan.md | Layout row verified locally. |
| F-4 | Source layout plan preserves the Slice01 package-behavior constraint or routes package behavior change to Slice04 | `rg -n "package behavior|SKILL.md plus sibling guides|guides/|Slice01|Slice04|package behavior change|package-compatible" artifacts/v40-source-layout-plan.md artifacts/v40-surface-routing-decision-register.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-source-layout-plan.md; artifacts/v40-surface-routing-decision-register.md | Prevents hidden package drift. |
| F-5 | Content sequence plan covers the thin SKILL.md load contract and operator workflow routing | `rg -n "thin SKILL.md|reason to load|positive load|negative load|problem ownership|dependency direction|operator workflow|guide routing|source edit sequencing" artifacts/v40-content-sequence-plan.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-content-sequence-plan.md | Load contract row verified locally. |
| F-6 | Content sequence plan names guide, template, example, cross-link, and first edit-order decisions | `rg -n "guide file|template file|example file|cross-link|first implementation|edit order|content sequence" artifacts/v40-content-sequence-plan.md artifacts/v40-source-layout-plan.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-content-sequence-plan.md; artifacts/v40-source-layout-plan.md | Source sequencing row verified locally. |
| F-7 | Decision register records accepted, deferred, and no-op decisions with owner or later-slice routing | `rg -n "accepted|deferred|no-op|owner|later slice|Slice03|Slice04|Slice05|Arc04 decision" artifacts/v40-surface-routing-decision-register.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-surface-routing-decision-register.md | Decision accountability row verified locally. |
| F-8 | Artifacts route schema, enum, validation, tests, package, release, and version-history questions to later Arc05 slices | `rg -n "schema syntax|enum spelling|validator-code|deterministic validation|tests|package target|package list|package-path|generated zip|release gate|version history|Slice03|Slice04|Slice05" artifacts/v40-source-layout-plan.md artifacts/v40-content-sequence-plan.md artifacts/v40-surface-routing-decision-register.md` | serious | slice-plan | done | closing-report.md; artifacts/ | Later-slice routing row verified locally. |
| F-9 | Artifacts keep source edits, implementation, generated zips, package release, runtime services, and release readiness out of scope | `rg -n "out of scope|does not edit source|source implementation|generated zips|package release|release readiness|runtime|GraphRAG|graph database|ontology database|memory runtime|CCDP service|live extraction" slice-plan.md artifacts/v40-source-layout-plan.md artifacts/v40-content-sequence-plan.md artifacts/v40-surface-routing-decision-register.md` | serious | operator constraint | done | closing-report.md; slice-plan.md; artifacts/ | Planning-only row verified locally. |
| F-10 | Source checkout remains clean | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | operator constraint | done | closing-report.md | Source checkout was not modified. |
| F-11 | New and modified Slice02 Markdown is ASCII-clean and has no trailing whitespace | `LC_ALL=C grep -RIn '[^ -~]' slice-plan.md ledger.md cc-prompt.md artifacts || true; grep -RIn '[[:blank:]]$' slice-plan.md ledger.md cc-prompt.md artifacts || true` | polish | repo hygiene | done | closing-report.md | Verification printed no matches. |

## What Worked

- Planning all package-relevant support files under `guides/` kept the layout
  compatible with the current generic skill package contract.
- Separating accepted layout decisions from Slice03 and Slice04 routing kept
  schema, validation, package, release, and version-history mechanics from
  being decided prematurely.
- The decision register made no-op decisions explicit where Slice02 avoided
  top-level support directories and source edits.

## Closure

Status: proposed-done pending independent CDC verification.

Rows: 11. Done: 11. Deferred: 0. No-op: 0.
