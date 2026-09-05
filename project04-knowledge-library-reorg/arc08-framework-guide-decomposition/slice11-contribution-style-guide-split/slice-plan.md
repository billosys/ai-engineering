# Slice 11: Contribution-Style Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice11-contribution-style-guide-split
status: verified-closed
opened-by: CDC
opened-on: 2026-09-05
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized-by-this-slice
operating-mode: expedited-without-scope-inference
```

## Purpose

Split the current contribution-style guide surface into the two
operator-accepted numbered guides:

1. `knowledge/contribution-style/guides/01-contribution-style.md`
2. `knowledge/contribution-style/guides/02-upstream-ticket-workflow.md`

Preserve `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md` as
the package-local authoring template. The split must keep external
maintainer-facing style guidance distinct from repository-local ticket drafting,
filing, and workflow guidance.

## Source Authorization

Source edits are authorized only for the contribution-style guide split and
directly necessary route, package, history, documentation, release-note, and
package-path repairs.

Expected source surfaces include:

- `knowledge/contribution-style/SKILL.md`
- `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`
- `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`
- `knowledge/contribution-style/version-history.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/version-history.md`
- `Makefile`
- `docs/collaboration-framework.md`
- `AGENTS.md`, only if standing route guidance needs repair
- `workbench/release-notes/RELEASE-0.5.0.md`
- `assets/packaging/path-exceptions.tsv`, only if validation requires a
  package-path exception move or disposition

No generated `build/` or `target/skills/` artifacts are to be committed.

## Required Work

1. Inventory the current source, route, package, template, and history surfaces
   before editing.
2. Split `CONTRIBUTION-STYLE.md` into `01-contribution-style.md` and
   `02-upstream-ticket-workflow.md`, preserving semantics while improving
   selective loading.
3. Preserve the maintainer-facing voice, calibrated confidence, ownership,
   pressure, severity, specificity, and tone guidance.
4. Preserve ticket-shape, filing workflow, local-draft, line-reference,
   blockquote-header, cross-linking, and template usage guidance in the
   workflow/template surface.
5. Keep `templates/CONTRIBUTION-TICKET.md` as a template, not a guide, unless
   validation exposes a concrete reason to change its role.
6. Use `git mv` for the old monolith when choosing the primary successor path
   so file history is preserved where Git similarity permits. If heavy semantic
   rewriting makes Git record delete/add, document that disposition.
7. Remove the old `CONTRIBUTION-STYLE.md` path as a live route unless
   explicitly retained as support/provenance material with operator-consistent
   rationale.
8. Update route surfaces, package lists, histories, documentation, AGENTS if
   affected, and release notes.
9. Validate source, links, generated package shape, and package paths.
10. Close the slice with artifacts, ledger update, and `closing-report.md`.

## Validation Expectations

Minimum validation:

- Source `git diff --check`.
- Focused local Markdown link validation for touched route files.
- `make check-skills`.
- `make collab-framework`.
- `make check-package-paths`.
- Generated `collaboration-framework.zip` inspection confirming the two new
  contribution-style guides and retained ticket template are present, and the
  old monolith package path follows the recorded disposition.
- Final source and planning worktree status checks.

## Outputs

Required planning artifacts:

- `artifacts/current-contribution-style-surface-map.md`
- `artifacts/contribution-style-split-map.md`
- `artifacts/legacy-contribution-style-disposition.md`
- `artifacts/template-role-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`
- `closing-report.md`

Do not create `cdc-verification.md`; CDC writes it after independent review.

## Closure

Slice is verified-closed by CDC.

CDC verification is recorded in `cdc-verification.md`.

Source commit:
`f96c30266b892fa67185f03046b6662326df0481`

Planning close commits:

- `a8edf2b9b166735c7af258afdee4fe2b0c1fe5b5`
- `340cf8ef29b5b76541252a7f2bd691b89afbb0e1`

No Arc08 scope change is required. Slice12 can proceed to final package,
install, link, CCDP disposition, and release reconciliation.
