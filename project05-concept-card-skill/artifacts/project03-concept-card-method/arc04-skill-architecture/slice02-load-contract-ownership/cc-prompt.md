# CC Prompt: Arc04 Slice02 Load Contract and Ownership Model

You are working in the Project03 planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc04-skill-architecture/slice02-load-contract-ownership`

The source checkout is:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Task

Complete Arc04 Slice02 by defining the v4.0 concept-card method skill's load
contract and ownership model.

Create these required artifacts under `artifacts/`:

- `artifacts/v40-load-contract.md`
- `artifacts/v40-ownership-routing-model.md`

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
- `../slice01-architecture-input-inventory/cdc-verification.md`
- `../slice01-architecture-input-inventory/artifacts/arc04-architecture-input-inventory.md`
- `../slice01-architecture-input-inventory/artifacts/arc04-decision-question-map.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/arc04-skill-architecture-handoff.md`

## Artifact Requirements

`artifacts/v40-load-contract.md` must:

- Define positive load triggers: when a session should load the concept-card
  method skill.
- Define negative load triggers: when related research, project-management,
  source-reading, implementation, or memory work should not load this skill by
  default.
- Describe the intended thin `SKILL.md` entrypoint and how it should route to
  future guides without naming final guide files as accepted architecture.
- Address the v3.2 five-agent workflow question as invariant, default recipe,
  parameterized pattern, or explicitly deferred with rationale.

`artifacts/v40-ownership-routing-model.md` must:

- Define what the concept-card method skill owns directly.
- Define what it does not own and should route to adjacent guidance.
- Define dependency direction with adjacent framework, project-management,
  source-reading, implementation-planning, and domain-knowledge guidance.
- Define the operator workflow boundary for extraction, re-extraction,
  verification, reconciliation, competency questions, and memory admission.
- Preserve Arc03 conceptual distinctions, especially concept card, claim,
  source support, evidence grade, extraction confidence, verification,
  validation, reconciliation, competency question, extraction run, and memory
  admission.

Both artifacts must route unresolved guide, template, example, validation,
package, README, Makefile, source-edit, and implementation questions to
Slice03, Slice04, Slice05, or Arc05 as appropriate.

## Boundaries

This is a load-contract and ownership slice. Do not choose final guide
architecture, final template architecture, final example set, package
inclusion, README integration, Makefile changes, validator-code, generated
zips, released packages, graph database design, memory runtime design, CCDP
service design, or live extraction behavior.

Do not write in the source checkout. This slice is planning-only.

If there are pre-existing staged planning changes when you begin, preserve
them. Do not commit, reset, or change staging unless the operator explicitly
asks you to.

## Verification

Before reporting proposed-done, run the ledger Verify commands:

- Open set and artifact checks from F-1 and F-2.
- Grep checks from F-3 through F-8.
- Source checkout clean check from F-9.
- ASCII and trailing-whitespace hygiene from F-10.

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
