# CC Prompt: Project04 Arc08 Slice03

You are CC for Project04 Arc08 Slice03:
`arc08-framework-guide-decomposition/slice03-collaboration-framework-posture-split`.

Operate in Expedited Mode only as explicitly defined by the source
project-management instructions and this slice. Expedited Mode does not
authorize shortcuts, skipped validation, weaker evidence or review, inferred
source scope, reduction or other change in scope, timeline interpretation, or
approval-gate override.

## Before Editing

Read these planning files first:

- `arc08-framework-guide-decomposition/arc-plan.md`
- `arc08-framework-guide-decomposition/ledger.md`
- `arc08-framework-guide-decomposition/slice03-collaboration-framework-posture-split/slice-plan.md`
- `arc08-framework-guide-decomposition/slice03-collaboration-framework-posture-split/ledger.md`
- `arc08-framework-guide-decomposition/slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`
- `arc08-framework-guide-decomposition/slice01-split-map-version-history-confirmation/artifacts/current-monolith-and-history-inventory.md`
- `arc08-framework-guide-decomposition/slice01-split-map-version-history-confirmation/artifacts/source-impact-and-validation-plan.md`
- `arc08-framework-guide-decomposition/slice02-project-management-process-history/cdc-verification.md`
- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`

Also read the current source files before editing:

- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md`
- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
- `AGENTS.md`

## Assignment

Split the collaboration-framework posture monolith into the four approved
numbered guides:

- `knowledge/collaboration-framework/guides/01-posture-and-ethics.md`
- `knowledge/collaboration-framework/guides/02-structural-pulls.md`
- `knowledge/collaboration-framework/guides/03-collaborative-rights.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`

Preserve the semantic substance of
`knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md`, but
do the semantic work needed to make the new guides independently useful and
easier to selectively load. Do not merely chop the file and leave confusing
fragments.

Remove the old monolith as a live load target, or retain only a narrow
compatibility/provenance stub if source evidence requires it. If retained,
record the reason and scope in `artifacts/posture-split-map.md`.

Create or update `knowledge/collaboration-framework/version-history.md` as the
sibling component history. Reconcile embedded version-history material from the
old monolith into that file. Do not leave or add component history under
`guides/` merely because guides changed.

Update all affected source routes, including:

- `knowledge/collaboration-framework/SKILL.md`
- `Makefile` `CF_FILES`
- package path exceptions if required
- README/docs/AGENTS references as required
- `workbench/release-notes/RELEASE-0.5.0.md` if it mentions old posture routes

Preserve the Slice02 Expedited Mode guardrail wording.

Create the expected Slice03 planning artifacts:

- `artifacts/posture-split-map.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/version-history-reconciliation.md`
- `artifacts/source-validation-results.md`

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
- local Markdown link validation for touched README/docs/AGENTS/SKILL/component
  routes
- `make check-skills`
- `make collab-framework`
- `make check-package-paths`
- generated `collaboration-framework.zip` inspection for the four new guide
  paths and absence or explicit disposition of the old monolith path

If a generated output is ignored, do not commit it. If a validation failure
requires source edits outside this slice's scope, stop and record the blocker
instead of widening scope silently.

At close, update `ledger.md`, write `closing-report.md`, include exact source
and planning commit IDs, record final source and planning statuses, and bubble
up anything Slice04 must know.
