# Slice 01: Source Surface and Implementation Input Inventory

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice01 open set exists with slice plan, ledger, prompt, and artifact home | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && test -d artifacts` | correctness-grade | slice-plan | done | closing-report.md | Local CC verification passed on 2026-08-31. |
| F-2 | Required inventory artifacts are produced under the slice-local artifact home | `test -f artifacts/source-surface-inventory.md && test -f artifacts/implementation-input-question-map.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/source-surface-inventory.md; artifacts/implementation-input-question-map.md | Artifact home is `artifacts/`. |
| F-3 | Source-surface inventory covers live repository source and packaging surfaces | `rg -n "source checkout|knowledge/|SKILL.md|guides|README.md|Makefile|package-path-exceptions.tsv|generated archive|generated zip|build/|package target|check-skills|check-package-paths|ignored output" artifacts/source-surface-inventory.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/source-surface-inventory.md | Local CC verification passed on 2026-08-31. |
| F-4 | Source-surface inventory names concrete existing source paths for later planning | `rg -n "/Users/oubiwann/lab/billosys/ai-engineering|knowledge/[^ ]+|README.md|Makefile|package-path-exceptions.tsv|AGENTS.md|CLAUDE.md|workbench/" artifacts/source-surface-inventory.md` | serious | slice-plan | done | closing-report.md; artifacts/source-surface-inventory.md | Supports later source-layout planning. |
| F-5 | Implementation question map routes questions to later Arc05 slices | `rg -n "Slice02|source layout|content sequence|guide files|template files|example files|Slice03|schema|enum|validation|validator-code|Slice04|README|library discoverability|Makefile|package list|package-path|generated zip|release gates|Slice05|synthesis|Project03 close" artifacts/implementation-input-question-map.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/implementation-input-question-map.md | Later-slice routing is explicit. |
| F-6 | Artifacts preserve accepted Arc04 handoff inputs | `rg -n "v40-skill-architecture.md|v40-architecture-decision-register.md|arc05-implementation-planning-handoff.md|accepted Arc04|thin SKILL.md|reason to load|problem ownership|dependency direction|package behavior|maintenance ownership" artifacts/source-surface-inventory.md artifacts/implementation-input-question-map.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/source-surface-inventory.md; artifacts/implementation-input-question-map.md | Arc04 decisions are inputs, not reopened decisions. |
| F-7 | Slice01 scope fences keep implementation decisions and runtime/release behavior out of scope | `rg -n "out of scope|does not decide final layout|does not edit source|source edit|schema syntax|enum spelling|validator implementation|Makefile edits|package-list changes|generated zips|release readiness|runtime|GraphRAG|graph database|ontology database|memory runtime|CCDP service|live extraction" slice-plan.md artifacts/source-surface-inventory.md artifacts/implementation-input-question-map.md` | serious | slice-plan | done | closing-report.md; slice-plan.md; artifacts/source-surface-inventory.md; artifacts/implementation-input-question-map.md | Slice01 inventories; later slices decide. |
| F-8 | Artifacts identify source implementation surfaces later slices may plan against | `rg -n "knowledge/|README.md|Makefile|package-path-exceptions.tsv|package targets|skill checks|package-path checks|generated archives|version history|source version history|ignored outputs|build/" artifacts/source-surface-inventory.md artifacts/implementation-input-question-map.md` | serious | slice-plan | done | closing-report.md; artifacts/source-surface-inventory.md; artifacts/implementation-input-question-map.md | Provides inputs for Slice02-Slice04. |
| F-9 | Source checkout remains clean | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | operator constraint | done | closing-report.md | Source checkout was not modified. |
| F-10 | New and modified Slice01 Markdown is ASCII-clean and has no trailing whitespace | `LC_ALL=C grep -RIn '[^ -~]' slice-plan.md ledger.md cc-prompt.md artifacts || true; grep -RIn '[[:blank:]]$' slice-plan.md ledger.md cc-prompt.md artifacts || true` | polish | repo hygiene | done | closing-report.md | Verification printed no matches. |

## What Worked

- Targeted source inspection kept Slice01 factual while avoiding source edits.
- Grep-verifiable artifact language made the ledger rows reproducible.
- Separating source-surface inventory from later-slice question routing kept
  Arc04 architecture accepted and avoided premature implementation decisions.

## Closure

Status: proposed-done pending independent CDC verification.

Rows: 10. Done: 10. Deferred: 0. No-op: 0.
