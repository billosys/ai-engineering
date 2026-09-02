# Slice 02: Accepted Directory and Root Contract

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice02-accepted-directory-contract
status: open
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
artifact-home: artifacts/
operating-mode: expedited
```

## Goal

Select the accepted target directory contract and source/package root contract
for Project04 from the verified Arc02 Slice01 decision surface. The contract
must be concrete enough for Slice03 to plan migration sequencing and
validation, while still preserving that actual source edits belong to later
implementation arcs.

## Inputs

- `../arc-plan.md` and `../ledger.md`.
- `../slice01-decision-surface-inventory/cdc-verification.md`.
- `../slice01-decision-surface-inventory/artifacts/target-contract-decision-surface.md`.
- `../slice01-decision-surface-inventory/artifacts/source-root-option-matrix.md`.
- `../slice01-decision-surface-inventory/artifacts/compatibility-obligation-inventory.md`.
- Arc01 close and Slice04 synthesis artifacts as supporting evidence when
  Slice01 artifacts need provenance detail.

## In Scope

- Create `artifacts/accepted-target-directory-contract.md` defining the
  selected `docs/`, `knowledge/`, `templates/`, `protocols/`, README,
  `SKILL.md`, wrapper, and exception rules.
- Create `artifacts/source-package-root-contract.md` defining source-root and
  package-root rules separately for domain/tooling skills, Project02
  framework/operational components, the `collaboration-framework` composer,
  planned `concept-card-method`, Biome multi-entrypoint roots, support
  templates, and CCDP.
- Create `artifacts/operator-decision-register.md` dispositioning D-1 through
  D-12 as accepted, adjusted, rejected, or operator decision required.
- Select evidence-backed defaults where Arc01/Slice01 evidence is sufficient.
- Mark any remaining operator-sensitive choice explicitly; no unlabeled
  unresolved decision should remain.
- Preserve current/live versus planned/not-live distinctions.
- Preserve skill kind and topology as independent axes.

## Out of Scope

- Moving, deleting, renaming, or editing source checkout files.
- Editing source `README.md`, source `SKILL.md`, `docs/`, `knowledge/`,
  `templates/`, `protocols/`, `Makefile`, package-path exceptions, generated
  zips, or package contents.
- Writing the migration sequence, validation matrix, or package-path exception
  policy in final implementation detail; Slice03 owns that.
- Writing final end-user docs or Arc05 public vocabulary.
- Claiming Project02 component roots or Project03 `concept-card-method` exist
  as live source before implementation.
- Reopening CCDP package policy unless the decision register records explicit
  evidence and operator decision need.

## Artifacts

Durable artifacts live under this slice's `artifacts/` directory:

- `artifacts/accepted-target-directory-contract.md`
- `artifacts/source-package-root-contract.md`
- `artifacts/operator-decision-register.md`

## Verification Approach

The slice ledger uses grep-verifiable rows against the three artifacts and
closing report. CC should run every Verify command before reporting
proposed-done. CDC will independently rerun them before marking the slice
verified-closed.

## Exit Criteria

- The accepted target directory contract covers `docs/`, `knowledge/`,
  `templates/`, `protocols/ccdp`, README, `SKILL.md`, wrapper/migration-note
  policy, and explicit exceptions.
- The source/package root contract separates source roots from package roots
  and handles current edge cases without collapsing them.
- The operator decision register dispositions D-1 through D-12.
- The contract preserves Project02 accepted facts, Project03 planned-surface
  facts, CCDP separation, Biome multi-entrypoint behavior, and kind/topology
  independence.
- No source-edit authorization is implied.
- The source checkout remains untouched.

## Expedited Mode

CC must commit the proposed-done slice packet after his changes using explicit
file paths. CDC will then review, verify, update parent status, commit CDC
changes, and open the next slice immediately if this slice closes.
