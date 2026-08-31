# CC Prompt: Arc04 Slice03 Guide, Template, and Example Architecture

You are working in the Project03 planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc04-skill-architecture/slice03-guide-template-example-architecture`

The source checkout is:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Task

Complete Arc04 Slice03 by defining the v4.0 concept-card method skill's guide,
template, and example architecture.

Create these required artifacts under `artifacts/`:

- `artifacts/v40-guide-architecture.md`
- `artifacts/v40-template-architecture.md`
- `artifacts/v40-example-architecture.md`

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
- `../slice02-load-contract-ownership/cdc-verification.md`
- `../slice02-load-contract-ownership/artifacts/v40-load-contract.md`
- `../slice02-load-contract-ownership/artifacts/v40-ownership-routing-model.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/arc04-skill-architecture-handoff.md`

## Artifact Requirements

`artifacts/v40-guide-architecture.md` must:

- Decide the guide-surface architecture by method concern.
- Preserve a thin `SKILL.md` entrypoint that routes to guides without embedding
  the full method.
- Cover extraction, re-extraction, evidence lifecycle, graph/CQ semantics,
  reconciliation, validation/verification workflow, and memory admission.
- Preserve the Slice02 positive/negative load trigger boundary.
- Route validation determinism, package behavior, README integration,
  maintenance ownership, and implementation planning to later owners.

`artifacts/v40-template-architecture.md` must:

- Decide the template-surface architecture.
- Distinguish user-authored surfaces from trace/result-record surfaces.
- Cover concept card, claim/source support, competency question/CQ,
  extraction run, validation result, verification result, reconciliation
  result, preservation decision, relationship/edge, and memory admission
  surfaces where appropriate.
- Preserve Arc03's separation between extraction confidence, source support,
  evidence grade, verification state, validation result, reconciliation state,
  and memory admission.

`artifacts/v40-example-architecture.md` must:

- Decide the example-surface architecture for the first v4.0 release.
- Cover minimal card, claim-backed card, CQ coverage, relationship/edge,
  extraction-run trace, reconciliation, memory admission, and parallel-worker
  or five-agent default-recipe examples.
- Explain which examples are release-critical versus optional or later.
- Preserve the decision that the five-agent workflow is a default recipe, not
  an invariant, while requiring extraction-run and parallel-worker provenance.

All artifacts must route unresolved validation, package, README, Makefile,
source-edit, schema, enum, generated-zip, release, and implementation
questions to Slice04, Slice05, or Arc05 as appropriate.

## Boundaries

This is a guide/template/example architecture slice. Do not choose validation
candidate selection, package inclusion, README integration, Makefile changes,
validator-code, deterministic validation scripts, generated zips, released
packages, graph database design, memory runtime design, CCDP service design,
live extraction behavior, exact schema syntax, exact enum spelling, or source
checkout edits.

Do not write in the source checkout. This slice is planning-only.

If there are pre-existing staged planning changes when you begin, preserve
them. Do not commit, reset, or change staging unless the operator explicitly
asks you to.

## Verification

Before reporting proposed-done, run the ledger Verify commands:

- Open set and artifact checks from F-1 and F-2.
- Grep checks from F-3 through F-9.
- Source checkout clean check from F-10.
- ASCII and trailing-whitespace hygiene from F-11.

Also run:

- `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check`

## Closing Report

Write `closing-report.md` with:

- A per-row walk for every F-row in `ledger.md`.
- Artifact list.
- Verification summary.
- Bubble-up to Arc04, including any decision-routing changes needed for
  Slice04, Slice05, or Arc05.
- Closure line with row counts and proposed-done status.
