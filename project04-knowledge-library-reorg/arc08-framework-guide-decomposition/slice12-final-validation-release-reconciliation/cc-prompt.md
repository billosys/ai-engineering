# CC Prompt: Project04 Arc08 Slice12 Final Validation, Install, Link, and Release Reconciliation

You are CC completing Project04 Arc08 Slice12 in Expedited Mode.

Expedited Mode changes only the explicit commit, close, and advance behaviors
already recorded in Project04. It does not authorize shortcuts, skipped
validation, weaker evidence or review, inferred source scope, reduction or
other change in scope, timeline interpretation, or override of operator
approval gates.

## Required Reading

Read before editing or validating:

1. `project04-knowledge-library-reorg/project-plan.md`
2. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/arc-plan.md`
3. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/ledger.md`
4. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice12-final-validation-release-reconciliation/slice-plan.md`
5. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice12-final-validation-release-reconciliation/ledger.md`

Also read the current source route surfaces before deciding whether any source
repair is needed:

- `README.md`
- `AGENTS.md`
- `Makefile`
- `docs/*.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/project-management/SKILL.md`
- `knowledge/project-management/version-history.md`
- `knowledge/work-verification/SKILL.md`
- `knowledge/work-verification/version-history.md`
- `knowledge/testing/SKILL.md`
- `knowledge/testing/version-history.md`
- `knowledge/code-auditing/SKILL.md`
- `knowledge/code-auditing/version-history.md`
- `knowledge/agent-coordination/SKILL.md`
- `knowledge/agent-coordination/version-history.md`
- `knowledge/contribution-style/SKILL.md`
- `knowledge/contribution-style/version-history.md`
- component `guides/`, `templates/`, and `examples/` directories under the
  eight framework component roots
- `assets/packaging/path-exceptions.tsv`
- `protocols/ccdp/README.md`
- `protocols/ccdp/composite-cognition-dispatch-protocol.md`
- `protocols/ccdp/src/README.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

## Task

Run final Arc08 reconciliation after the guide splits and version-history
normalization. Confirm that:

- README/docs/AGENTS/SKILL/component route surfaces point at the current
  selective-load guide layout;
- old monolith and pre-split guide filenames are not live load targets unless
  explicitly classified as historical/provenance/disposition text, compatibility
  stubs, or package-local templates;
- framework component version histories live as siblings beside component
  `SKILL.md` files;
- all installable skill packages build and pass package-path validation;
- isolated install behavior still produces the expected skill roots;
- CCDP remains a protocol package, not an installable skill;
- release notes accurately describe the final Arc08 source/package/install/CCDP
  state.

This is a validation and reconciliation slice. Do not make source edits unless a
concrete defect is found by the checks above. If no source repair is needed,
record that explicitly and create no source commit.

## Source Scope

Authorized source repairs, if evidence requires them, are limited to:

- `README.md`
- `AGENTS.md`
- `Makefile`
- `docs/*.md`
- framework component `SKILL.md`, `guides/`, `templates/`, `examples/`, and
  sibling `version-history.md` files
- `assets/packaging/path-exceptions.tsv`
- `workbench/release-notes/RELEASE-0.5.0.md`
- `protocols/ccdp/**` only for the mechanical assembled-spec freshness repair
  required if `make ccdp-package` proves the checked-in assembled protocol is
  stale

Do not commit generated zips, `build/`, `target/skills/`, or isolated install
smoke output.

## Required Planning Artifacts

Create:

- `artifacts/final-source-route-reconciliation.md`
- `artifacts/old-live-target-disposition-map.md`
- `artifacts/version-history-placement-check.md`
- `artifacts/package-validation-results.md`
- `artifacts/install-smoke-results.md`
- `artifacts/ccdp-disposition-results.md`
- `artifacts/release-note-reconciliation.md`
- `closing-report.md`

Update:

- `ledger.md`

Do not create `cdc-verification.md`.

## Validation

Run and record at minimum:

- Source `git diff --check`.
- Local README/docs/AGENTS/SKILL/component Markdown link validation.
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
- Generated installable package inspection for all 12 expected skill zips.
- Isolated install smoke using a temporary install root under `/private/tmp`.
- `make ccdp-package`.
- `make check-ccdp-package`.
- Focused `ccdp.zip` inspection confirming `ccdp/` root, required protocol
  package files, and no `SKILL*` entrypoint.
- Final source and planning worktree status checks.

Package-path validation and CCDP package validation must have zero hard
failures. Warning-only package-path findings may remain if accepted or
explicitly dispositioned.

## Commit Instructions

If source changes are required, commit them after validation and before final
planning close. Because other work may share the branch, explicitly list every
source file in the commit command. Use a message such as:

```text
Reconcile Arc08 final release surfaces

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

If no source changes are required, do not create a source commit; record the
source no-op explicitly in the artifacts and closing report.

Then commit the Slice12 planning close packet, explicitly listing every
planning file changed or created. Use a message such as:

```text
Complete Project04 Arc08 Slice12

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

If the closing report records a pending planning close hash, make a tiny
follow-up planning commit that records the actual close-packet commit hash,
again with explicit file paths and both trailers.

## Report Back

Report:

- source commit hash, or explicit no-source-commit result;
- planning commit hash or hashes;
- exact source and planning file lists;
- validation summary;
- old live-load target disposition;
- version-history placement result;
- package/install/CCDP disposition;
- release-note reconciliation result;
- final source and planning statuses;
- Arc08 close bubble-up.
