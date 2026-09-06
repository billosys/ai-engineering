# Slice 12: Final Validation, Install, Link, and Release Reconciliation

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice12-final-validation-release-reconciliation
status: verified-closed
opened-by: CDC
opened-on: 2026-09-05
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: repair-only-if-validation-finds-defect
operating-mode: expedited-without-scope-inference
```

## Purpose

Perform final Arc08 reconciliation after all guide splits and version-history
normalization have landed. Confirm that README/docs/AGENTS/SKILL routes, package
contents, install behavior, CCDP package separation, and release notes describe
the current source truth.

This is a validation and reconciliation slice. Source edits are authorized only
to repair concrete defects found by the final checks: broken or stale live
routes, package-list mismatches, release-note inaccuracies, install-surface
problems, or CCDP disposition inconsistencies.

## Source Authorization

Expected read surfaces:

- `README.md`
- `AGENTS.md`
- `Makefile`
- `docs/*.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/{project-management,work-verification,testing,code-auditing,agent-coordination,contribution-style}/SKILL.md`
- `knowledge/{project-management,work-verification,testing,code-auditing,agent-coordination,contribution-style}/version-history.md`
- framework component `guides/`, `templates/`, and `examples/` directories
- `assets/packaging/path-exceptions.tsv`
- `protocols/ccdp/README.md`
- `protocols/ccdp/composite-cognition-dispatch-protocol.md`
- `protocols/ccdp/src/README.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

Authorized source repairs, if required by evidence, are limited to:

- route/link/documentation repairs in the surfaces above;
- `Makefile` package-list repairs;
- `assets/packaging/path-exceptions.tsv` disposition repairs;
- `workbench/release-notes/RELEASE-0.5.0.md` reconciliation;
- `protocols/ccdp/**` only if `make ccdp-package` proves the assembled CCDP
  file is stale and the repair is the mechanical freshness refresh required by
  the existing CCDP package gate.

No generated `build/`, `target/skills/`, or installed smoke-test output is to
be committed.

## Required Work

1. Inventory the final Arc08 source surface after Slices01-11.
2. Validate README/docs/AGENTS/SKILL/component routes and local Markdown links.
3. Scan for old monolith and pre-split guide filenames, classifying every hit as
   live route, historical/provenance/disposition text, package-local template,
   or defect.
4. Confirm framework component sibling `version-history.md` placement and the
   absence of guide/template-local component histories unless explicitly
   justified.
5. Run source and package validation, including all installable skill zips.
6. Inspect generated package shapes, especially `collaboration-framework.zip`.
7. Run an isolated install smoke test for the installable skill packages.
8. Validate CCDP package freshness and shape while preserving CCDP as a protocol
   package, not an installable skill.
9. Reconcile release notes with the final Arc08 source/package/install/CCDP
   result, or record that no release-note repair was needed.
10. Close the slice with artifacts, ledger update, and `closing-report.md`.

## Validation Expectations

Minimum validation:

- Source `git diff --check`.
- Local README/docs/AGENTS/SKILL/component link validation.
- Old live-load target scan for:
  - `AI-CONSTITUTION-SUPPLEMENT.md`
  - `AI-ENGINEERING-METHODOLOGY.md`
  - `CODE-AUDIT.md`
  - `CODE-COVERAGE.md`
  - `SUBAGENT-DELEGATION-POLICY.md`
  - `CONTRIBUTION-STYLE.md`
  - `guides/09-worked-example-odm.md`
  - `guides/version-history.md`
- `make check-skills`.
- `make all`.
- `make check-package-paths`.
- Generated installable package inspection for all expected skill zips.
- Isolated install smoke using a temporary install root under `/private/tmp`.
- `make ccdp-package`.
- `make check-ccdp-package`.
- Focused `ccdp.zip` inspection confirming `ccdp/` root, required protocol
  package files, and no `SKILL*` entrypoint.
- Final source and planning worktree status checks.

Package-path validation and CCDP package validation must have zero hard
failures. Existing warning-only package-path findings may remain if they are
already accepted or explicitly dispositioned.

## Outputs

Required planning artifacts:

- `artifacts/final-source-route-reconciliation.md`
- `artifacts/old-live-target-disposition-map.md`
- `artifacts/version-history-placement-check.md`
- `artifacts/package-validation-results.md`
- `artifacts/install-smoke-results.md`
- `artifacts/ccdp-disposition-results.md`
- `artifacts/release-note-reconciliation.md`
- `closing-report.md`

Do not create `cdc-verification.md`; CDC writes it after independent review.

## Closure

Slice is verified-closed by CDC.

CDC verification on 2026-09-05 reproduced the Slice12 ledger evidence and
reran final source/package/link/install/CCDP validation. A final project
wrap-up pass found current CCDP assembled-spec drift after later Arc09 source
work; CDC repaired that date-only freshness drift in source commit
`b18d049333799141f4d2e2328b1cd6ba444a437b` before closing Slice12.
