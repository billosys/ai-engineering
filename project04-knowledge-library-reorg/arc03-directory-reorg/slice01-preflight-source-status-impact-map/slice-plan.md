# Slice 01: Preflight Source Status and Impact Map

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice01-preflight-source-status-impact-map
status: open
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
artifact-home: artifacts/
operating-mode: expedited
```

## Goal

Establish the clean source baseline, impact map, validation command inventory,
and source-edit authorization register for Arc03 before any source files move.

This slice is preflight-only. It may inspect the source checkout, but it must
not edit source files.

## Inputs

- `../arc-plan.md` and `../ledger.md`.
- `../../project-plan.md` and `../../ledger.md`.
- `../../arc02-directory-contract/closing-report.md`.
- `../../arc02-directory-contract/slice04-implementation-handoff/cdc-verification.md`.
- `../../arc02-directory-contract/slice04-implementation-handoff/artifacts/arc03-readiness-packet.md`.
- `../../arc02-directory-contract/slice04-implementation-handoff/artifacts/source-edit-slice-roadmap.md`.
- `../../arc02-directory-contract/slice04-implementation-handoff/artifacts/arc02-decision-summary.md`.
- Source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`, read-only.

## In Scope

- Create `artifacts/source-status-impact-map.md`, recording branch/worktree
  identity, source status baseline, planning status baseline, and the source
  surfaces Arc03 expects later slices to touch.
- Create `artifacts/validation-command-inventory.md`, mapping likely Arc03
  source-edit surfaces to validation commands and review gates.
- Create `artifacts/source-edit-authorization-register.md`, listing proposed
  Arc03 source-edit slices, whether each is authorized now, what operator gates
  remain, and what validation evidence it must produce.
- Preserve Arc02 accepted sequencing: source status first, top-level
  `SKILL.md` compatibility before composer moves, mechanical moves before prose
  rewrites, package-local link repair before exceptions, and Arc04/Arc05
  separation.

## Out of Scope

- Moving, deleting, renaming, or editing source checkout files.
- Editing source `README.md`, `SKILL.md`, `docs/`, `knowledge/`, `templates/`,
  `protocols/`, `Makefile`, package-path exceptions, generated zips, or
  package contents.
- Selecting or implementing the top-level `SKILL.md` shim/replacement/no-shim
  path.
- Creating source-edit commits or generated packages.
- Writing Arc04 end-user docs or Arc05 public vocabulary.

## Artifacts

Durable artifacts live under this slice's `artifacts/` directory:

- `artifacts/source-status-impact-map.md`
- `artifacts/validation-command-inventory.md`
- `artifacts/source-edit-authorization-register.md`

## Verification Approach

The slice ledger uses grep-verifiable rows against the three artifacts and
closing report. CC should run every Verify command before reporting
proposed-done. CDC will independently rerun them before marking the slice
verified-closed.

## Exit Criteria

- The source and planning status baselines are recorded.
- The impact map names expected source surfaces and package/build surfaces.
- The validation inventory covers source status, diff hygiene, skill checks,
  package checks, framework package checks, CCDP checks, generated package
  inspection, and compatibility review.
- The authorization register distinguishes preflight work from later
  source-edit slices and names operator gates.
- The source checkout remains untouched.

## Expedited Mode

CC must commit the proposed-done slice packet after his changes using explicit
file paths. CDC will then review, verify, update parent status, commit CDC
changes, and open the next slice immediately if this slice closes.
