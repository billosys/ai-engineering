# CC Prompt: Arc04 Slice05 Architecture Synthesis and Arc05 Handoff

You are working in the Project03 planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis`

The source checkout is:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Task

Complete Arc04 Slice05 by composing the verified Arc04 slice outputs into the
accepted v4.0 concept-card method skill architecture and preparing the Arc05
implementation-planning handoff.

Create these required artifacts under `artifacts/`:

- `artifacts/v40-skill-architecture.md`
- `artifacts/v40-architecture-decision-register.md`
- `artifacts/arc05-implementation-planning-handoff.md`

Then update this slice's `ledger.md` with attested evidence and write
`closing-report.md`.

Do not create `cdc-verification.md`; CDC writes that after independently
reproducing the ledger evidence. Do not write the Arc04 arc-level
`closing-report.md`; that belongs to formal Arc04 close after Slice05 is
independently verified.

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
- `../slice03-guide-template-example-architecture/cdc-verification.md`
- `../slice03-guide-template-example-architecture/artifacts/v40-guide-architecture.md`
- `../slice03-guide-template-example-architecture/artifacts/v40-template-architecture.md`
- `../slice03-guide-template-example-architecture/artifacts/v40-example-architecture.md`
- `../slice04-validation-packaging-discoverability/cdc-verification.md`
- `../slice04-validation-packaging-discoverability/artifacts/v40-validation-architecture.md`
- `../slice04-validation-packaging-discoverability/artifacts/v40-package-discoverability-model.md`
- `../slice04-validation-packaging-discoverability/artifacts/v40-maintenance-ownership-model.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-model-decision-register.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/arc04-skill-architecture-handoff.md`

## Artifact Requirements

`artifacts/v40-skill-architecture.md` must:

- Synthesize the final v4.0 skill architecture across `SKILL.md`, guides,
  templates, examples, validation candidates, package behavior, README/library
  discoverability, and maintenance ownership.
- Preserve the thin `SKILL.md` route: reason to load, positive load triggers,
  negative load triggers, problem ownership, dependency direction, and guide
  routing.
- Preserve accepted concept-card constructs and lifecycle distinctions:
  concept card, claim, source span, source support, evidence grade,
  extraction confidence, relationship/edge, competency question/CQ,
  extraction run, validation result, verification result/state,
  reconciliation result/state, preservation decision, and memory admission.
- Preserve the guide split, user-authored versus trace/result-record template
  classes, release-critical example set, validation-candidate classes,
  package/discoverability promise boundary, and maintenance ownership model.
- State that this is architecture, not implementation or release.

`artifacts/v40-architecture-decision-register.md` must:

- Record final Arc04 architecture decisions.
- Record unresolved decisions and their later owner.
- Preserve decisions from Slice02, Slice03, and Slice04 rather than
  re-deciding them.
- Distinguish final Arc04 decisions from Arc05 implementation-planning inputs.
- Route source layout, source edits, exact schema syntax, exact enum spelling,
  validator-code, Makefile/package-list updates, README/library text,
  generated zips, tests, release gates, package updates, and source version
  history to Arc05.

`artifacts/arc05-implementation-planning-handoff.md` must:

- Provide a bounded Arc05 input, organized by implementation-planning work
  category.
- Include source layout, source edits, guide files, template files, example
  files, schema syntax, enum spelling, validator-code, Makefile/package lists,
  README/library text, generated zips, tests, release gates, package updates,
  and source version-history alignment.
- Name the Arc04 decisions Arc05 must preserve.
- Name unresolved implementation questions Arc05 must answer before source
  edits begin.
- Identify the Arc04 arc-ledger rows A-6, A-7, and A-8 as formal arc-close
  composition inputs, not as work for CC to close inside this slice.

All artifacts must preserve the package/discoverability promise boundary: the
v4.0 concept-card method skill architecture does not promise runtime GraphRAG,
graph database, ontology database, memory runtime, CCDP service, live
extraction, executable validator, generated zip, package release, or source
implementation behavior before later implementation planning accepts it.

## Boundaries

This is an architecture synthesis and handoff slice. Do not write source
`SKILL.md`, guides, templates, examples, README, Makefile, package-list,
validator-code, schema, enum, test, generated-zip, release, or packaged skill
files.

Do not implement deterministic validation scripts, choose exact CLI/API
behavior, build runtime services, design a graph database, build GraphRAG,
build a memory runtime, design a CCDP service, run live extraction, create
release artifacts, or write the Arc04 arc-level `closing-report.md`.

Do not write in the source checkout. This slice is planning-only.

If there are pre-existing staged planning changes when you begin, preserve
them. Do not commit, reset, or change staging unless the operator explicitly
asks you to.

## Verification

Before reporting proposed-done, run the ledger Verify commands:

- Open set and artifact checks from F-1 and F-2.
- Grep checks from F-3 through F-10.
- Source checkout clean check from F-11.
- ASCII and trailing-whitespace hygiene from F-12.

Also run:

- `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check`

## Closing Report

Write `closing-report.md` with:

- A per-row walk for every F-row in `ledger.md`.
- Artifact list.
- Verification summary.
- Bubble-up to Arc04, including whether Arc04 is ready for formal arc close
  and whether any arc-plan change is required.
- Closure line with row counts and proposed-done status.
