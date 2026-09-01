# CC Prompt: Arc04 Slice01 Architecture Input Inventory

You are working in the Project03 planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc04-skill-architecture/slice01-architecture-input-inventory`

The source checkout is:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Task

Complete Arc04 Slice01 by producing the architecture input inventory for the
v4.0 concept-card method skill.

Create these required artifacts under `artifacts/`:

- `artifacts/arc04-architecture-input-inventory.md`
- `artifacts/arc04-decision-question-map.md`

Then update this slice's `ledger.md` with attested evidence and write
`closing-report.md`.

Do not create `cdc-verification.md`; CDC writes that after independently
reproducing the ledger evidence.

## Required Reading

Read these first:

- `../../arc-plan.md`
- `../../ledger.md`
- `slice-plan.md`
- `ledger.md`
- `../../../project-plan.md`
- `../../../ledger.md`
- `../../../arc03-conceptual-model/closing-report.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-model-decision-register.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/arc04-skill-architecture-handoff.md`

## Artifact Requirements

`artifacts/arc04-architecture-input-inventory.md` must:

- Identify the Arc03 conceptual-model commitments Arc04 must preserve.
- Inventory candidate skill surfaces: `SKILL.md`, guides, templates,
  examples, validation candidates, package behavior, README integration, and
  maintenance ownership.
- Distinguish accepted inputs, provisional inputs, deferred inputs, and
  out-of-scope implementation mechanics.
- Keep the inventory source-backed by citing the planning artifacts it
  consumes.

`artifacts/arc04-decision-question-map.md` must:

- Map open architecture questions to decision axes: reason to load, problem
  ownership, dependency direction, package behavior, maintenance ownership,
  validation determinism, and operator workflow.
- Assign each question to a later decision owner: Slice02, Slice03, Slice04,
  Slice05, or Arc05.
- Preserve unresolved questions without choosing final architecture in this
  slice.

## Boundaries

This is an inventory slice. Do not choose final skill architecture, final file
layout, exact schema syntax, exact enum spelling, validator implementation,
source edits, generated zips, released packages, graph database design, memory
runtime design, CCDP service design, or live extraction behavior.

Do not write in the source checkout. This slice is planning-only.

If there are pre-existing staged planning changes when you begin, preserve
them. Do not commit, reset, or change staging unless the operator explicitly
asks you to.

## Verification

Before reporting proposed-done, run the ledger Verify commands:

- Open set and artifact checks from F-1 and F-2.
- Grep checks from F-3 through F-6.
- Source checkout clean check from F-7.
- ASCII and trailing-whitespace hygiene from F-8.

Also run:

- `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check`

## Closing Report

Write `closing-report.md` with:

- A per-row walk for every F-row in `ledger.md`.
- Artifact list.
- Verification summary.
- Bubble-up to Arc04, including any decision-routing changes needed for later
  slices.
- Closure line with row counts and proposed-done status.
