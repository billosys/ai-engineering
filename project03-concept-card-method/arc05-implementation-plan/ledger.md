# Arc 05: Implementation Plan

## Arc Ledger

Capability: convert the accepted v4.0 concept-card method skill architecture
into a source-edit implementation plan covering layout, content sequence,
schema and validation decisions, README/library discoverability, Makefile and
package updates, generated-artifact policy, release gates, verification
checks, and Project03 close input, without editing source files.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 closes with a source surface and implementation input inventory verified by CDC | `test -f slice01-source-surface-inventory/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice01-source-surface-inventory/cdc-verification.md` | correctness-grade | arc-plan | done | slice01-source-surface-inventory/cdc-verification.md | CDC reproduced all ten Slice01 rows on 2026-08-31. |
| A-2 | Slice02 closes with a skill source layout and content sequence plan verified by CDC | `test -f slice02-source-layout-content-plan/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice02-source-layout-content-plan/cdc-verification.md` | correctness-grade | arc-plan | open | | Children-closed row. |
| A-3 | Slice03 closes with a schema, enum, and validation plan verified by CDC | `test -f slice03-schema-validation-plan/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice03-schema-validation-plan/cdc-verification.md` | correctness-grade | arc-plan | open | | Children-closed row. |
| A-4 | Slice04 closes with a packaging, discoverability, and release-gate plan verified by CDC | `test -f slice04-packaging-release-plan/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice04-packaging-release-plan/cdc-verification.md` | correctness-grade | arc-plan | open | | Children-closed row. |
| A-5 | Slice05 closes with implementation-plan synthesis and Project03 close input verified by CDC | `test -f slice05-implementation-plan-synthesis/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice05-implementation-plan-synthesis/cdc-verification.md` | correctness-grade | arc-plan | open | | Children-closed row. |
| A-6 | The implementation plan preserves accepted Arc04 decisions while assigning exact source layout, guide, template, example, schema, enum, and validation work to implementation slices | `rg -n "Arc04|accepted decision|source layout|SKILL.md|guide|template|example|schema|enum|validation|validator-code|implementation slice|source edit sequence" slice*/artifacts arc-plan.md` | serious | arc-plan | open | | Composition row; reproduce at arc close. |
| A-7 | The implementation plan covers README, library discoverability, Makefile, package list, package-path checks, generated zips, tests, release gates, and version history without performing source edits | `rg -n "README|library discoverability|Makefile|package list|package-path|generated zip|tests|release gates|version history|source edit|planning-only|does not edit" slice*/artifacts arc-plan.md` | serious | arc-plan | open | | Composition row; reproduce at arc close. |
| A-8 | The implementation plan keeps runtime systems and release claims out of scope until a later owner accepts them | `rg -n "out of scope|runtime|GraphRAG|graph database|ontology database|memory runtime|CCDP service|live extraction|release readiness|later owner|deferred" slice*/artifacts arc-plan.md` | serious | arc-plan | open | | Composition row; reproduce at arc close. |
| A-9 | Project03 source-edit boundary remains intact through Arc05 planning | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet && rg -n "planning-only|does not edit source|source edits remain deferred|implementation plan explicitly authorizes" arc-plan.md ../project-plan.md` | serious | operator constraint | open | | Composition row; reproduce at arc close. |

## Closure

Arc remains open.
