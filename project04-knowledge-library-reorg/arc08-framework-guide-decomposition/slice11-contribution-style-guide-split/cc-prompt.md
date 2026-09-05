# CC Prompt: Project04 Arc08 Slice11 Contribution-Style Guide Split

You are CC completing Project04 Arc08 Slice11 in Expedited Mode.

Expedited Mode changes only the explicit commit, close, and advance behaviors
already recorded in Project04. It does not authorize shortcuts, skipped
validation, weaker evidence or review, inferred source scope, reduction or
other change in scope, timeline interpretation, or override of operator
approval gates.

## Required Reading

Read before editing:

1. `project04-knowledge-library-reorg/project-plan.md`
2. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/arc-plan.md`
3. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/ledger.md`
4. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice11-contribution-style-guide-split/slice-plan.md`
5. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice11-contribution-style-guide-split/ledger.md`

Also read these source files before editing:

- `AGENTS.md`
- `Makefile`
- `knowledge/contribution-style/SKILL.md`
- `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`
- `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`
- `knowledge/contribution-style/version-history.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/version-history.md`
- `docs/collaboration-framework.md`
- `workbench/release-notes/RELEASE-0.5.0.md`
- `assets/packaging/path-exceptions.tsv`

## Task

Split the current contribution-style guide:

- `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`

into:

- `knowledge/contribution-style/guides/01-contribution-style.md`
- `knowledge/contribution-style/guides/02-upstream-ticket-workflow.md`

Preserve:

- `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`

as the package-local authoring template.

The split must be semantic, not just heading extraction. Each new guide should
be independently useful and selectively loadable. Preserve the current
contribution-style contract:

- maintainer-facing voice is friendly, specific, calibrated, and respectful of
  project ownership;
- confidence, inference, bias, red-herring, pressure, severity, and specificity
  guidance remains intact;
- one-ticket-per-problem and no-wall-of-speculation discipline remains intact;
- upstream ticket workflow remains separate from the external-facing voice
  guidance;
- local draft locations, line-reference re-checking, blockquote header usage,
  tracker paste boundaries, cross-linking, and canonical on-disk artifact
  expectations remain available;
- `CONTRIBUTION-TICKET.md` remains a reusable template, not a guide, unless
  evidence forces a different disposition.

Use `git mv` for the old monolith when choosing the primary successor path so
history is preserved where Git similarity permits. If semantic extraction makes
Git record delete/add rather than a rename, record that in the legacy
disposition artifact and closing report.

Remove `CONTRIBUTION-STYLE.md` as a live source/package route unless a specific
support/provenance retention decision is recorded. Do not leave stale links or
package paths.

## Source Scope

Authorized source edits are limited to the split and necessary repairs in:

- `knowledge/contribution-style/**`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/version-history.md`
- `Makefile`
- `docs/collaboration-framework.md`
- `AGENTS.md`, only if standing route guidance needs repair
- `workbench/release-notes/RELEASE-0.5.0.md`
- `assets/packaging/path-exceptions.tsv`, only if route/package validation
  shows an exception repair is necessary

Do not commit generated zips, `build/`, or `target/skills/`.

## Required Planning Artifacts

Create:

- `artifacts/current-contribution-style-surface-map.md`
- `artifacts/contribution-style-split-map.md`
- `artifacts/legacy-contribution-style-disposition.md`
- `artifacts/template-role-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`
- `closing-report.md`

Update:

- `ledger.md`

Do not create `cdc-verification.md`.

## Validation

Run and record at minimum:

- Source `git diff --check`.
- Focused local Markdown link validation for touched route files.
- `make check-skills`.
- `make collab-framework`.
- `make check-package-paths`.
- Generated `collaboration-framework.zip` inspection confirming both new
  contribution-style guides and the retained ticket template are present, and
  the old `CONTRIBUTION-STYLE.md` package path follows the recorded
  disposition.
- Final source and planning worktree status checks.

Package-path validation must have zero hard failures.

## Commit Instructions

Commit source changes after validation and before final planning close.
Because other work may share the branch, explicitly list every source file in
the commit command. Use a message such as:

```text
Split contribution-style guide surface

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then commit the Slice11 planning close packet, explicitly listing every
planning file changed or created. Use a message such as:

```text
Complete Project04 Arc08 Slice11

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

If the closing report records a pending planning close hash, make a tiny
follow-up planning commit that records the actual close-packet commit hash,
again with explicit file paths and both trailers.

## Report Back

Report:

- source commit hash;
- planning commit hash or hashes;
- exact source and planning file lists;
- validation summary;
- `CONTRIBUTION-STYLE.md` disposition;
- `CONTRIBUTION-TICKET.md` template disposition;
- final source and planning statuses;
- Slice12 bubble-up.
