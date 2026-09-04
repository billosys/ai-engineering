# Slice 01: Confirm Split Map, Version-History Contract, and Expedited Wording

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice01-split-map-version-history-confirmation
status: verified-closed
opened-by: CDC
opened-on: 2026-09-04
closed-by: CDC
closed-on: 2026-09-04
cdc-verification: cdc-verification.md
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
operating-mode: expedited-with-explicit-operator-gate
artifact_home: artifacts/
```

## Goal

Confirm the exact guide split map, framework component version-history
normalization contract, and Expedited Mode wording target before any source
decomposition starts.

This slice exists to prevent the accepted split from becoming a third
deferral. It produces an operator-facing confirmation packet and records the
operator approval gate that must close before Slice02 opens.

## Scope

In scope:

- Inventory current headings and embedded version-history sections in:
  - `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md`
  - `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`
  - framework component `SKILL.md`, guide, and template files with embedded
    `## Version History` sections.
- Confirm the approved collaboration-framework guide sequence:
  - `01-posture-and-ethics.md`
  - `02-structural-pulls.md`
  - `03-collaborative-rights.md`
  - `04-component-route-table.md`
- Confirm the accepted engineering-methods guide sequence:
  - `01-engineering-methodology.md`
  - `02-knowledge-substrate.md`
  - `03-process-rigour.md`
  - `04-operational-routing.md`
  - `05-component-boundary-analysis.md`
  - `06-source-package-release-gates.md`
- Confirm sibling `version-history.md` normalization for the eight framework
  component roots.
- Confirm the exact Expedited Mode source wording target from the operator's
  notes.
- Inventory live source surfaces that currently mention Expedited Mode:
  - `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
  - `knowledge/collaboration-framework/SKILL.md`
  - `knowledge/project-management/guides/version-history.md`
- Map source files, Makefile package lists, package-path exception surfaces,
  README/docs/AGENTS references, and release-note surfaces likely affected by
  later slices.

Out of scope:

- Editing source checkout files.
- Moving, deleting, or renaming source files.
- Creating or editing generated zips, `build/`, or `target/skills`.
- Opening Slice02 before the operator approves the confirmation packet.

## Support Inputs

- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`
- Arc07 close report and CDC verification files.
- Current source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`.

## Expected Artifacts

- `artifacts/current-monolith-and-history-inventory.md`
- `artifacts/operator-confirmation-packet.md`
- `artifacts/source-impact-and-validation-plan.md`
- `artifacts/slice-sequence-and-approval-gate.md`

## Verification Approach

CC should inspect the source checkout and the supporting artifacts, then create
the four expected planning artifacts without editing source. The confirmation
packet must quote or summarize the exact split and version-history map that
needs operator approval before Slice02 opens.

## Exit Criteria

- Current monolith headings and embedded version-history sections are
  inventoried.
- Confirmation packet lists every proposed target guide and sibling
  `version-history.md` file.
- Confirmation packet includes the exact Expedited Mode wording target.
- Current Expedited Mode source surfaces are inventoried, including the
  collaboration-framework `SKILL.md` routing references.
- Source impact and validation plan identifies likely source files and checks.
- Slice sequence records that Slice02 must not open until operator approval is
  recorded.
- Planning artifacts, ledger, and `closing-report.md` are committed with both
  required co-author trailers.
