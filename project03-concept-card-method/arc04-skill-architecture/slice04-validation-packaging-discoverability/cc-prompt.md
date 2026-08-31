# CC Prompt: Arc04 Slice04 Validation, Packaging, and Discoverability

You are working in the Project03 planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc04-skill-architecture/slice04-validation-packaging-discoverability`

The source checkout is:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Task

Complete Arc04 Slice04 by defining the v4.0 concept-card method skill's
validation, packaging, discoverability, and maintenance architecture.

Create these required artifacts under `artifacts/`:

- `artifacts/v40-validation-architecture.md`
- `artifacts/v40-package-discoverability-model.md`
- `artifacts/v40-maintenance-ownership-model.md`

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
- `../slice01-architecture-input-inventory/artifacts/arc04-decision-question-map.md`
- `../slice02-load-contract-ownership/cdc-verification.md`
- `../slice02-load-contract-ownership/artifacts/v40-load-contract.md`
- `../slice02-load-contract-ownership/artifacts/v40-ownership-routing-model.md`
- `../slice03-guide-template-example-architecture/cdc-verification.md`
- `../slice03-guide-template-example-architecture/artifacts/v40-guide-architecture.md`
- `../slice03-guide-template-example-architecture/artifacts/v40-template-architecture.md`
- `../slice03-guide-template-example-architecture/artifacts/v40-example-architecture.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`
- `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/arc04-skill-architecture-handoff.md`

## Artifact Requirements

`artifacts/v40-validation-architecture.md` must:

- Classify validation candidates as deterministic structural checks, semantic
  audit checks, human/operator review checks, or deferred runtime checks.
- Include candidates for required fields, required sections, provenance,
  source support, relationship references, CQ coverage, path/slug hygiene,
  graph closure, preservation decisions, reconciliation records, extraction
  run traceability, and memory admission gates.
- Preserve the distinction between validation result, verification
  result/state, evidence grade, extraction confidence, reconciliation
  result/state, and memory admission.
- Explain which checks are stable enough to plan for later automation and
  which must remain review/audit judgments.
- Avoid choosing exact schema syntax, exact enum spelling, validator-code, or
  executable validator behavior.

`artifacts/v40-package-discoverability-model.md` must:

- Decide package behavior at the surface-category level for guides,
  templates, examples, scripts, generated artifacts, validation candidates,
  and planning-only inputs.
- Decide README and skill-library discoverability promises.
- Preserve the thin `SKILL.md` route and the positive/negative load trigger
  boundary.
- State that the first v4.0 skill architecture does not promise runtime
  GraphRAG, graph database, ontology database, memory runtime, CCDP service,
  live extraction, or released package behavior before implementation
  planning.
- Route exact file layout, Makefile edits, README edits, generated zips,
  tests, package updates, and release mechanics to Arc05.

`artifacts/v40-maintenance-ownership-model.md` must:

- Assign maintenance owners or change paths for conceptual-model updates,
  guide updates, template updates, example updates, validation-candidate
  changes, validator-code follow-up, package-list/package-behavior updates,
  README and skill-library updates, generated artifacts, and version history.
- Preserve Slice02's load contract and Slice03's concern-based guide split,
  user-authored versus trace/result-record template classes, release-critical
  example set, and five-agent default-recipe decision.
- Decide what Slice05 must synthesize and what Arc05 must implement or plan.
- Avoid creating implementation policy that belongs to later source-edit
  planning.

All artifacts must route unresolved implementation, source-edit, exact file
layout, schema, enum, validator-code, Makefile, README edit, generated-zip,
test, release, and package-update questions to Slice05 or Arc05 as
appropriate.

## Boundaries

This is a validation/package/discoverability architecture slice. Do not write
source `SKILL.md`, guides, templates, examples, README, Makefile,
package-list, validator-code, schema, enum, test, generated-zip, release, or
packaged skill files.

Do not implement deterministic validation scripts, choose exact CLI/API
behavior, build runtime services, design a graph database, build GraphRAG,
build a memory runtime, design a CCDP service, run live extraction, or create
release artifacts.

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
- Bubble-up to Arc04, including any decision-routing changes needed for
  Slice05 or Arc05.
- Closure line with row counts and proposed-done status.
