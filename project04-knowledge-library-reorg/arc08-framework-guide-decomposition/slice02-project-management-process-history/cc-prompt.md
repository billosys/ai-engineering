# CC Prompt: Project04 Arc08 Slice02

You are CC for Project04 Arc08 Slice02:
`arc08-framework-guide-decomposition/slice02-project-management-process-history`.

Operate in Expedited Mode, but only as explicitly defined by the source
project-management instructions and this slice. Expedited Mode does not
authorize shortcuts, skipped validation, weaker evidence or review, inferred
source scope, reduction or other change in scope, timeline interpretation, or
approval-gate override.

## Before Editing

Read these planning files first:

- `arc08-framework-guide-decomposition/arc-plan.md`
- `arc08-framework-guide-decomposition/ledger.md`
- `arc08-framework-guide-decomposition/slice02-project-management-process-history/slice-plan.md`
- `arc08-framework-guide-decomposition/slice02-project-management-process-history/ledger.md`
- `arc08-framework-guide-decomposition/slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`
- `arc08-framework-guide-decomposition/slice01-split-map-version-history-confirmation/artifacts/source-impact-and-validation-plan.md`
- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`

Also read the source project-management wayfinder and the relevant current
source files before editing.

## Assignment

Implement the process and version-history baseline that must land before the
guide split slices:

- Correct Expedited Mode wording in
  `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`.
- Update `knowledge/collaboration-framework/SKILL.md` routing text that mentions
  Expedited Mode.
- Use the clarified source-scope wording if it helps the prose:
  "Expedited Mode means no inferred source scope and no reduction or other
  change in scope."
- Move `knowledge/project-management/guides/version-history.md` to
  `knowledge/project-management/version-history.md` using `git mv`.
- Repair local links and package/build surfaces affected by that move.
- Document the framework component version-history management practice in the
  top-level `AGENTS.md`, unless you find a clearly better source home. If you
  use a different home, record the rationale in
  `artifacts/version-history-management-practice-record.md`.
- Update version-history entries for touched framework/process files according
  to the sibling-history rule being established.
- Create the expected Slice02 artifacts:
  - `artifacts/expedited-mode-source-reconciliation.md`
  - `artifacts/project-management-version-history-move-map.md`
  - `artifacts/version-history-management-practice-record.md`
  - `artifacts/source-validation-results.md`

Do not split `AI-CONSTITUTION-SUPPLEMENT.md` or
`AI-ENGINEERING-METHODOLOGY.md` in this slice. Do not normalize other component
histories except for route repairs directly required by the project-management
move.

## Commit Requirements

Commit after source changes before handing off for CDC review. Because other
processes may stage unrelated files, explicitly list the files in every commit.
Use both required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then commit the planning close packet with an explicit file list. Do not create
`cdc-verification.md`; CDC writes that file.

## Validation

Run and record:

- `git diff --check`
- local README/docs/AGENTS/SKILL Markdown link validation for touched routes
- `make check-skills`
- `make collab-framework`
- `make check-package-paths`

If a generated output is ignored, do not commit it. If a validation failure
requires source edits outside this slice's scope, stop and record the blocker
instead of widening scope silently.

At close, update `ledger.md`, write `closing-report.md`, include exact source
and planning commit IDs, record final source and planning statuses, and bubble
up anything Slice03 must know.
