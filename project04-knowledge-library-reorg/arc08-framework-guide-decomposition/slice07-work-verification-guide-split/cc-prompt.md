# CC Prompt: Arc08 Slice07 Work-Verification Guide Split

You are CC working in Project04 Arc08 Slice07.

## Required Reading

Read these before editing:

- `arc08-framework-guide-decomposition/arc-plan.md`
- `arc08-framework-guide-decomposition/ledger.md`
- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/slice-plan.md`
- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/ledger.md`
- `arc08-framework-guide-decomposition/slice06-project-management-example-layout-reconciliation/cdc-verification.md`
- `arc08-framework-guide-decomposition/slice05-component-version-history-normalization/cdc-verification.md`
- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`
- Source `AGENTS.md`
- Source `knowledge/collaboration-framework/SKILL.md`
- Source `knowledge/work-verification/SKILL.md`
- Source `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`
- Source `knowledge/work-verification/version-history.md`

## Assignment

Implement Slice07 exactly as scoped: split or extract the current
work-verification ledger-discipline material into the five accepted numbered
guides:

- `knowledge/work-verification/guides/01-ledger-discipline.md`
- `knowledge/work-verification/guides/02-evidence-strength.md`
- `knowledge/work-verification/guides/03-row-closure.md`
- `knowledge/work-verification/guides/04-silent-drop-checks.md`
- `knowledge/work-verification/guides/05-independent-verification.md`

Preserve `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` as a
package-local support/template asset if it still carries useful complete
protocol or copyable table material. Record that decision in
`artifacts/template-retention-disposition.md`.

This is semantic decomposition work. Do not perform a heading-only split unless
the resulting guides are independently useful, correctly cross-routed, and
easier to load selectively than the current template.

Repair all affected routes, including work-verification `SKILL.md`,
`version-history.md`, Makefile `CF_FILES`, collaboration-framework routes,
project-management and engineering-methods references, public docs, AGENTS,
release notes, staging scripts, and package-path exceptions where needed.

Use explicit `git mv` path pairs for source moves. If an empty directory must
be removed, use `rmdir` as a precaution. Do not use `rm -rf`.

## Required Artifacts

Create these planning artifacts:

- `artifacts/current-work-verification-surface-map.md`
- `artifacts/work-verification-split-map.md`
- `artifacts/template-retention-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`

Update:

- `ledger.md`

Create:

- `closing-report.md`

Do not create `cdc-verification.md`.

## Validation

Run the slice ledger verifier commands and record results in
`artifacts/source-validation-results.md` and `closing-report.md`.

At minimum, source validation must include:

- source `git diff --check`
- focused local Markdown link validation for touched route surfaces
- `make check-skills`
- `make collab-framework`
- `make check-package-paths`
- generated `collaboration-framework.zip` inspection confirming the five new
  work-verification guides are present and the retained/omitted template shape
  matches `artifacts/template-retention-disposition.md`

Run package builds sequentially. Do not commit generated zips, `build/`, or
`target/skills`.

## Commit Requirements

Use explicit file lists for commits.

If source files change, commit only the exact source files you changed with a
message like:

```text
Split work-verification guide surface

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then commit only the exact Slice07 planning files you changed with a message
like:

```text
Complete Project04 Arc08 Slice07

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Final report should include source commit hash if one was created, planning
commit hash, validation summary, template disposition, and final
source/planning cleanliness.
