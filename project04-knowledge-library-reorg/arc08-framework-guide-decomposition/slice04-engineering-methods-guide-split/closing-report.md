# Slice 04 Closing Report: Engineering-Methods Guide Split

## Status

Proposed-done pending CDC verification.

Source commit: `0ad843dfff6e01bdc68a566e9b8907ac76da88b6`

Planning commit: `7e392b81cebd5e6845b3dcca71a8786de61684c4`

## Scope Completed

Slice04 implemented the accepted engineering-methods guide split in the main source checkout. The former live monolith route at `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md` was replaced by six numbered guides:

- `knowledge/engineering-methods/guides/01-engineering-methodology.md`
- `knowledge/engineering-methods/guides/02-knowledge-substrate.md`
- `knowledge/engineering-methods/guides/03-process-rigour.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/guides/05-component-boundary-analysis.md`
- `knowledge/engineering-methods/guides/06-source-package-release-gates.md`

The component's version history was normalized to sibling `knowledge/engineering-methods/version-history.md`, with the former monolith history preserved there as provenance and lineage. Live routes in engineering-methods and collaboration-framework entrypoints now point to the split guides while preserving Slice02 Expedited Mode guardrails and Slice03 collaboration-framework posture routes.

## Explicit Source File List

Source commit `0ad843dfff6e01bdc68a566e9b8907ac76da88b6` changed these files:

- `Makefile`
- `docs/ORIGINS.md`
- `docs/collaboration-framework.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`
- `knowledge/engineering-methods/SKILL.md`
- `knowledge/engineering-methods/guides/01-engineering-methodology.md`
- `knowledge/engineering-methods/guides/02-knowledge-substrate.md`
- `knowledge/engineering-methods/guides/03-process-rigour.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/guides/05-component-boundary-analysis.md`
- `knowledge/engineering-methods/guides/06-source-package-release-gates.md`
- `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`
- `knowledge/engineering-methods/version-history.md`
- `knowledge/project-management/guides/02-canonical-planning-worktree.md`
- `knowledge/project-management/guides/08-maintenance.md`
- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
- `knowledge/project-management/version-history.md`
- `knowledge/testing/guides/CODE-COVERAGE.md`
- `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

## Planning Evidence

The close packet includes:

- `ledger.md`
- `closing-report.md`
- `artifacts/methodology-split-map.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/version-history-reconciliation.md`
- `artifacts/source-validation-results.md`

## Validation

Source validation completed in `/Users/oubiwann/lab/billosys/ai-engineering`:

- `git diff --check`: pass.
- Focused Markdown link scan over touched Markdown files: `checked_files=21 checked_links=200 missing_links=0`.
- `make check-skills`: pass.
- `make collab-framework`: pass.
- `make check-package-paths`: pass.
- Direct package-path validator summary: `exit_code=0`, `hard failures: 0`, `warnings: 369`.
- Zip inspection confirmed all six numbered engineering-methods guides and `knowledge/engineering-methods/version-history.md` are included in `target/skills/collaboration-framework.zip`.
- Zip inspection confirmed `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md` is absent from the generated package.

The 369 package-path warnings are existing warning-class validator findings, not hard failures. This distinction is preserved for CDC review.

## Ledger Row Walk

Rows: 8. Done: 8. Deferred: 0. No-op: 0.

- F-1 proposed-done: six accepted engineering-methods guides exist; old live monolith path is absent and provenance references are dispositioned.
- F-2 proposed-done: split preserves the monolith's major semantic sections and makes each new guide independently loadable.
- F-3 proposed-done: engineering-methods and collaboration-framework routes point to split guides while preserving Slice02/Slice03 guardrails.
- F-4 proposed-done: engineering-methods version history is normalized to sibling `version-history.md`.
- F-5 proposed-done: public docs, route tables, component guides, and release-note references were repaired or explicitly dispositioned.
- F-6 proposed-done: package, local-link, and generated collaboration-framework validation passed.
- F-7 proposed-done: generated `collaboration-framework.zip` contains the split guide set and omits the old live monolith path.
- F-8 proposed-done: this close packet records source evidence, validation evidence, row walk, and Slice05 bubble-up.

## Bubble-Up to Arc08

Slice05 should reconcile the remaining component version histories after the Slice02-Slice04 split sequence. In particular, it should normalize or explicitly disposition remaining component-local history for `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and `contribution-style` without reintroducing live routes to `AI-ENGINEERING-METHODOLOGY.md` or `AI-CONSTITUTION-SUPPLEMENT.md`.

Slice05 should preserve current live references to the split engineering-methods guides, especially `knowledge/engineering-methods/guides/01-engineering-methodology.md#notes-for-codex`, and continue to distinguish package-path hard failures from warning-class historical/prose findings.

## CDC Notes

This report does not create or substitute for `cdc-verification.md`. CDC should independently verify the source commit, regenerated package shape, source validation outputs, and ledger evidence before closing Slice04.
