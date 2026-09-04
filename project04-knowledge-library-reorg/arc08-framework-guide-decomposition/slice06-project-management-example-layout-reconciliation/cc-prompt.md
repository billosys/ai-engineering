# CC Prompt: Arc08 Slice06 Project-Management Example Layout Reconciliation

You are CC working in Project04 Arc08 Slice06.

## Required Reading

Read these before editing:

- `arc08-framework-guide-decomposition/arc-plan.md`
- `arc08-framework-guide-decomposition/ledger.md`
- `arc08-framework-guide-decomposition/slice06-project-management-example-layout-reconciliation/slice-plan.md`
- `arc08-framework-guide-decomposition/slice06-project-management-example-layout-reconciliation/ledger.md`
- `arc08-framework-guide-decomposition/slice05-component-version-history-normalization/cdc-verification.md`
- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`
- Source `AGENTS.md`
- Source `knowledge/collaboration-framework/SKILL.md`
- Source `knowledge/project-management/SKILL.md`
- Source `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`

## Assignment

Implement Slice06 exactly as scoped: reconcile the current
`knowledge/project-management/` layout against the accepted architecture,
especially the accepted target:

- from `knowledge/project-management/guides/09-worked-example-odm.md`
- to `knowledge/project-management/examples/01-worked-example-odm.md`

Use explicit `git mv` path pairs for source moves. If an empty directory must
be removed, use `rmdir` as a precaution. Do not use `rm -rf`.

Preserve the eight numbered project-management guides and the
`guides/PROJECT-MANAGEMENT.md` wayfinder unless source evidence requires a
separately recorded disposition. Do not split or rewrite the
project-management guides in this slice.

Repair all affected routes, including project-management `SKILL.md`,
`version-history.md`, Makefile `CF_FILES`, collaboration-framework routes,
public docs, AGENTS, release notes, staging scripts, and package-path
exceptions where needed.

## Required Artifacts

Create these planning artifacts:

- `artifacts/current-project-management-layout-map.md`
- `artifacts/accepted-layout-delta-map.md`
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
- generated `collaboration-framework.zip` inspection confirming the accepted
  project-management example path is present and the old worked-example guide
  path is absent unless explicitly retained

Run package builds sequentially. Do not commit generated zips, `build/`, or
`target/skills`.

## Commit Requirements

Use explicit file lists for commits.

If source files change, commit only the exact source files you changed with a
message like:

```text
Reconcile project-management example layout

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then commit only the exact Slice06 planning files you changed with a message
like:

```text
Complete Project04 Arc08 Slice06

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Final report should include source commit hash if one was created, planning
commit hash, validation summary, any exceptions/dispositions, and final
source/planning cleanliness.
