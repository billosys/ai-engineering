# CC Prompt: Arc08 Slice08 Testing Guide Split

You are CC working in Project04 Arc08 Slice08.

## Required Reading

Read these before editing:

- `arc08-framework-guide-decomposition/arc-plan.md`
- `arc08-framework-guide-decomposition/ledger.md`
- `arc08-framework-guide-decomposition/slice08-testing-guide-split/slice-plan.md`
- `arc08-framework-guide-decomposition/slice08-testing-guide-split/ledger.md`
- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/cdc-verification.md`
- `arc08-framework-guide-decomposition/slice06-project-management-example-layout-reconciliation/cdc-verification.md`
- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`
- Source `AGENTS.md`
- Source `knowledge/collaboration-framework/SKILL.md`
- Source `knowledge/testing/SKILL.md`
- Source `knowledge/testing/guides/CODE-COVERAGE.md`
- Source `knowledge/testing/version-history.md`
- Source `knowledge/work-verification/SKILL.md`

## Assignment

Implement Slice08 exactly as scoped: split or extract the current testing
coverage material into the three accepted numbered guides:

- `knowledge/testing/guides/01-testing-discipline.md`
- `knowledge/testing/guides/02-coverage-hardening.md`
- `knowledge/testing/guides/03-validation-gates.md`

The existing `knowledge/testing/guides/CODE-COVERAGE.md` file is the current
source material. Prefer preserving Git history by moving it with an explicit
`git mv` if it becomes one of the accepted guide files, then extract the
general testing discipline and validation-gate material into companion guides.

Do not perform a heading-only split. The resulting guides must be independently
useful, correctly cross-routed, and easier to load selectively than the current
single coverage prompt.

Preserve the current quality floor: hard coverage-threshold discipline,
warnings/lint/format pressure, tests-must-pass rule, root-cause repair,
coverage anti-patterns, systematic coverage work, progress reporting, and
adaptation from Rust/Cargo examples to the active repository's own tools.
Broaden public routing from "coverage only" to testing discipline, coverage
hardening, and validation gates without claiming a full future TDD method.

Repair all affected routes, including testing `SKILL.md`, `version-history.md`,
Makefile `CF_FILES`, collaboration-framework routes, work-verification,
project-management and engineering-methods references, public docs, AGENTS,
release notes, staging scripts, and package-path exceptions where needed.

Use explicit `git mv` path pairs for source moves. If an empty directory must
be removed, use `rmdir` as a precaution. Do not use `rm -rf`.

## Required Artifacts

Create these planning artifacts:

- `artifacts/current-testing-surface-map.md`
- `artifacts/testing-split-map.md`
- `artifacts/legacy-code-coverage-disposition.md`
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
- generated `collaboration-framework.zip` inspection confirming the three new
  testing guides are present and the old `CODE-COVERAGE.md` path follows
  `artifacts/legacy-code-coverage-disposition.md`

Run package builds sequentially. Do not commit generated zips, `build/`, or
`target/skills`.

## Commit Requirements

Use explicit file lists for commits.

If source files change, commit only the exact source files you changed with a
message like:

```text
Split testing guide surface

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then commit only the exact Slice08 planning files you changed with a message
like:

```text
Complete Project04 Arc08 Slice08

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Final report should include source commit hash if one was created, planning
commit hash, validation summary, `CODE-COVERAGE.md` disposition, and final
source/planning cleanliness.
