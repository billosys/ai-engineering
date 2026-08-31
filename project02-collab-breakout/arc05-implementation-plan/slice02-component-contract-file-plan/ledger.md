# Slice 02: Component Contract And File Plan

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Artifacts consume verified Slice01 inputs and accepted Arc04 architecture | `test -f ../slice01-implementation-surface-map/cdc-verification.md && test -f ../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md && rg -n "verified Slice01|slice01-implementation-surface-map|operator-accepted-architecture|accepted architecture|implementation surface|source map|release validation|cross-cutting|Slice02" artifacts/*.md` | correctness-grade | slice-plan | open | | Input grounding row. |
| F-2 | Component contract matrix covers all eight accepted components and core contract fields | `rg -n "collaboration-framework|engineering-methods|project-management|work-verification|testing|code-auditing|agent-coordination|contribution-style|standalone use|composed use|dependency|support asset|validation|deferred" artifacts/component-contract-matrix.md` | correctness-grade | slice-plan | open | | Component contract coverage row. |
| F-3 | Component file layout plan defines entrypoints, guides, version histories, templates/examples, and component roots | `rg -n "SKILL.md|version-history.md|guides/|templates/|examples/|collaboration-framework/|engineering-methods/|project-management/|work-verification/|testing/|code-auditing/|agent-coordination/|contribution-style/" artifacts/component-file-layout-plan.md` | correctness-grade | slice-plan | open | | File layout row. |
| F-4 | Source-to-component migration plan maps current source files to target move/copy/split/new-prose/defer decisions | `rg -n "README.md|SKILL.md|docs/AI-CONSTITUTION-SUPPLEMENT.md|docs/AI-ENGINEERING-METHODOLOGY.md|docs/PROJECT-MANAGEMENT.md|docs/pm|templates/LEDGER-DISCIPLINE.md|docs/CODE-AUDIT.md|docs/CLAUDE-CODE-COVERAGE.md|docs/SUBAGENT-DELEGATION-POLICY.md|docs/CONTRIBUTION-STYLE.md|templates/CONTRIBUTION-TICKET.md|move|copy|split|new prose|defer" artifacts/source-to-component-migration-plan.md` | correctness-grade | slice-plan | open | | Source mapping row. |
| F-5 | Package/source contract register includes required per-component source/package fields without finalizing Slice03 release edits | `rg -n "source path|package root|package-local link|installed skill|README route|SKILL route|Makefile impact|generated zip|validation command|owner|versioning contract|not final|Slice03" artifacts/package-source-contract-register.md` | serious | slice-plan | open | | Package/source contract row. |
| F-6 | Support, adapter, dependency, and deferred-boundary plan preserves accepted cross-cutting decisions | `rg -n "support asset|adapter|dependency edge|agent-coordination|CC/CDC/operator|context-packet|result integration|component-boundary-analysis|source/package/release gates|memory admission|deferred|CCDP separation" artifacts/support-adapter-dependency-plan.md` | serious | slice-plan | open | | Cross-cutting preservation row. |
| F-7 | Slice03 inputs identify package, README, validation, migration, and open-question handoff without editing source | `rg -n "Slice03|package|README|SKILL.md|Makefile|generated zip|package-path exception|make check-skills|make check-package-paths|migration|open question|no source edits|source files remain untouched" artifacts/slice03-package-readme-validation-inputs.md` | serious | slice-plan | open | | Handoff row. |
| F-8 | Required artifacts exist under artifacts/ | `test -f artifacts/component-contract-matrix.md && test -f artifacts/component-file-layout-plan.md && test -f artifacts/source-to-component-migration-plan.md && test -f artifacts/package-source-contract-register.md && test -f artifacts/support-adapter-dependency-plan.md && test -f artifacts/slice03-package-readme-validation-inputs.md` | correctness-grade | slice-plan | open | | Artifact placement row. |
| F-9 | Source checkout remains untouched | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | correctness-grade | slice-plan | open | | Planning-only boundary row. |

## What Worked

_(At slice close. Patterns that made the slice close cleanly.)_

## Closure

Slice is open. Rows: 9. Done: 0. Deferred: 0. No-op: 0.
