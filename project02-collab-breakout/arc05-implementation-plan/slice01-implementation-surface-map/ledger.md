# Slice 01: Implementation Surface Map

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Artifacts cite accepted Arc04 architecture and Project01 path/package constraints | `test -f ../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md && test -f ../../../project01-harmonise-paths/closing-report.md && rg -n "operator-accepted-architecture|Project01|project01-harmonise-paths|source/package|package-local|zip root|accepted architecture" artifacts/*.md` | correctness-grade | slice-plan | open | | Input grounding row. |
| F-2 | Current implementation surface inventory covers source files and release surfaces | `rg -n "README.md|SKILL.md|docs/AI-CONSTITUTION-SUPPLEMENT.md|docs/AI-ENGINEERING-METHODOLOGY.md|docs/PROJECT-MANAGEMENT.md|docs/pm|templates/LEDGER-DISCIPLINE.md|docs/CODE-AUDIT.md|docs/CLAUDE-CODE-COVERAGE.md|docs/SUBAGENT-DELEGATION-POLICY.md|docs/CONTRIBUTION-STYLE.md|templates/CONTRIBUTION-TICKET.md|Makefile|package-path-exceptions.tsv" artifacts/implementation-surface-inventory.md` | correctness-grade | slice-plan | open | | Source/release inventory row. |
| F-3 | Accepted component source map covers all eight accepted components | `rg -n "collaboration-framework|engineering-methods|project-management|work-verification|testing|code-auditing|agent-coordination|contribution-style" artifacts/accepted-component-source-map.md` | correctness-grade | slice-plan | open | | Component coverage row. |
| F-4 | Release validation surface map covers package/build/check surfaces | `rg -n "INSTALL_ZIPS|ALL_SKILL_FILES|CF_FILES|collaboration-framework.zip|generated zip|make check-skills|make check-package-paths|make collab-framework|make all|CCDP|make ccdp-package|make check-ccdp-package|package-path-exceptions" artifacts/release-validation-surface-map.md` | correctness-grade | slice-plan | open | | Release gate row. |
| F-5 | Cross-cutting concern map preserves support assets, adapters, versioning, boundary analysis, memory deferral, and CCDP separation | `rg -n "support asset|adapter|agent-coordination|version-history.md|component-boundary-analysis|memory admission|deferred|CCDP separation|source/package/release gates" artifacts/cross-cutting-concern-map.md` | serious | slice-plan | open | | Cross-cutting row. |
| F-6 | Slice02 inputs name file-plan questions without designing final edits | `rg -n "Slice02|component file plan|open question|input|not final|no source edits|source files remain untouched" artifacts/slice02-component-file-plan-inputs.md` | serious | slice-plan | open | | Handoff row. |
| F-7 | Required artifacts exist under artifacts/ | `test -f artifacts/implementation-surface-inventory.md && test -f artifacts/accepted-component-source-map.md && test -f artifacts/release-validation-surface-map.md && test -f artifacts/cross-cutting-concern-map.md && test -f artifacts/slice02-component-file-plan-inputs.md` | correctness-grade | slice-plan | open | | Artifact placement row. |
| F-8 | Source checkout remains untouched | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | correctness-grade | slice-plan | open | | Planning-only boundary row. |

## What Worked

_(At slice close. Patterns that made the slice close cleanly.)_

## Closure

Slice remains open.
