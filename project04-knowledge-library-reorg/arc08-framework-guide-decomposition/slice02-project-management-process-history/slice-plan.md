# Slice 02: Project-Management Process Wording and Version-History Baseline

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice02-project-management-process-history
status: verified-closed
opened-by: CDC
opened-on: 2026-09-04
closed-by: CDC
closed-on: 2026-09-04
cdc-verification: cdc-verification.md
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized
operating-mode: expedited
artifact_home: artifacts/
operator-approval-source: ../slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md
```

## Goal

Implement the Arc08 process baseline before the guide decomposition slices:
correct Expedited Mode wording, normalize project-management version history
placement, and document the framework component version-history management
practice where future sessions will see it.

## Scope

In scope:

- Update Expedited Mode wording in
  `knowledge/project-management/guides/PROJECT-MANAGEMENT.md` so it is limited
  to the explicit process changes the operator named.
- Ensure Expedited Mode explicitly means no shortcuts, no skipped validation,
  no weaker evidence or review, no inferred source scope and no reduction or
  other change in scope, no timeline interpretation, and no override of
  explicit operator approval gates.
- Update `knowledge/collaboration-framework/SKILL.md` routing text that mentions
  Expedited Mode so it points to the corrected project-management behavior.
- Move `knowledge/project-management/guides/version-history.md` to
  `knowledge/project-management/version-history.md` and repair local links.
- Document the framework component version-history management practice in the
  top-level `AGENTS.md`, unless implementation evidence shows a more
  appropriate source surface; if so, record the rationale in the closing report.
- Update package/build surfaces affected by the project-management
  version-history move, including `Makefile`, package path exceptions, and any
  staging scripts if required.
- Update README/docs/AGENTS references only where needed to keep routes current.
- Update version-history entries for touched framework/process files according
  to the new sibling-history rule being established.
- Create Slice02 planning evidence artifacts under `artifacts/` and close the
  slice with explicit source and planning commits.

Out of scope:

- Splitting `AI-CONSTITUTION-SUPPLEMENT.md`.
- Splitting `AI-ENGINEERING-METHODOLOGY.md`.
- Normalizing version histories for framework components other than
  `project-management`, except where direct route repairs are required.
- Changing public skill kind/topology vocabulary.
- Committing generated zips, `build/`, or `target/skills`.

## Support Inputs

- `../slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`
- `../slice01-split-map-version-history-confirmation/artifacts/source-impact-and-validation-plan.md`
- `../slice01-split-map-version-history-confirmation/artifacts/current-monolith-and-history-inventory.md`
- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`
- Arc08 `arc-plan.md` and `ledger.md`

## Expected Artifacts

- `artifacts/expedited-mode-source-reconciliation.md`
- `artifacts/project-management-version-history-move-map.md`
- `artifacts/version-history-management-practice-record.md`
- `artifacts/source-validation-results.md`

## Verification Approach

CC should perform source edits on the main checkout and planning evidence edits
on the planning checkout. Use explicit path lists for every commit. Source
validation must cover wording, links, package paths, generated package shape,
and the project-management version-history move.

## Exit Criteria

- Expedited Mode source wording contains the narrowed scope and approval-gate
  guardrails.
- The clarified phrase "no inferred source scope and no reduction or other
  change in scope" is present where it improves the source wording, or the
  closing report explains why an equivalent wording was used.
- Project-management version history lives beside
  `knowledge/project-management/SKILL.md`, not under `guides/`.
- The top-level `AGENTS.md`, or a recorded better home, documents the
  framework component version-history management practice.
- Package/build surfaces and local links are repaired.
- Validation commands in `ledger.md` pass.
- Source and planning commits are created with explicit file lists and both
  required co-author trailers.
