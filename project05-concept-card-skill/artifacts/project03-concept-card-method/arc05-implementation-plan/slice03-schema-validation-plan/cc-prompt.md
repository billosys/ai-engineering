# CC Prompt: Arc05 Slice03 Schema, Enum, and Validation Plan

You are CC implementing Project03 Arc05 Slice03 in the planning worktree.

Work only under:

`project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/`

Do not edit the source checkout at
`/Users/oubiwann/lab/billosys/ai-engineering`. Do not create or edit
`cdc-verification.md`; CDC owns that file after your close.

## Context

Read these files before writing:

- `project03-concept-card-method/project-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/arc-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/ledger.md`
- `project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/slice-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/ledger.md`
- `project03-concept-card-method/arc05-implementation-plan/slice01-source-surface-inventory/cdc-verification.md`
- `project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/cdc-verification.md`
- `project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/artifacts/v40-source-layout-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/artifacts/v40-content-sequence-plan.md`
- `project03-concept-card-method/arc05-implementation-plan/slice02-source-layout-content-plan/artifacts/v40-surface-routing-decision-register.md`
- `project03-concept-card-method/arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`
- `project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md`

Preserve the accepted Arc03 conceptual model, accepted Arc04 skill
architecture, and accepted Slice02 source layout/content sequence. Slice03 may
decide schema treatment, controlled vocabulary, validation boundaries, and
validator-code/test scope, but it must not perform source implementation.

## Task

Create the required Slice03 artifacts:

- `artifacts/v40-schema-surface-plan.md`
- `artifacts/v40-enum-vocabulary-plan.md`
- `artifacts/v40-validation-review-plan.md`
- `artifacts/v40-validator-scope-test-plan.md`

Update:

- `ledger.md`
- `closing-report.md`

The schema surface plan should decide how the v4.0 method will represent
concept card, claim, source support, source span/source locator, relationship
edge, competency question, extraction run, validation result, verification
result, reconciliation result, preservation decision, and memory admission
surfaces. Map those surfaces to the Slice02 planned template, example, guide,
and validation paths.

The enum vocabulary plan should name controlled vocabulary or enum spelling
for evidence grade, extraction confidence, verification state, validation
result, reconciliation state, CQ status, preservation decision, memory
admission, source-support status, and any related lifecycle fields needed for
the first implementation plan.

The validation/review plan should separate deterministic structural validation
from semantic audit, human/operator review, and deferred runtime checks. State
what each evidence class can prove and cannot prove.

The validator scope/test plan should decide validator-code scope for the first
implementation plan: source documentation only, executable code, or explicitly
deferred implementation. It should also decide test scope, invalid-example or
failure-output expectations, and what remains manual or deferred.

Route README/library discoverability, Makefile targets, package lists,
package-path exceptions, generated zip policy, release gates, package release,
and source version-history obligations to Slice04.

## Scope Fences

Do not:

- edit source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, package-path, validator-code, generated-zip, or release files;
- implement executable validators, tests, generated zips, package targets,
  package list edits, package-path exception rows, README/library prose,
  release gates, release readiness, package release, or source version-history
  text;
- create runtime services, GraphRAG, graph database, ontology database, memory
  runtime, CCDP service, or live extraction behavior;
- change the Slice02 source layout unless a schema or validation finding forces
  a documented Arc05 plan update;
- close Arc05 or Project03.

## Verification

Run the Slice03 ledger checks from this directory:

`project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/`

Also run:

- `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet`
- `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check`
- strict ASCII and trailing-whitespace checks over Slice03 Markdown.

The closing report must include:

- row-by-row disposition for F-1 through F-12;
- `Rows: 12. Done: 12. Deferred: 0. No-op: 0.` unless a row is explicitly
  deferred or no-op with rationale;
- artifact inventory;
- Bubble-Up section stating whether Slice03 requires Arc05 re-sequencing, a new
  slice, or a scope correction.

## Expedited Commit Requirement

After verification passes, commit your changes. Stage only these explicit files:

```sh
git add \
  project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/artifacts/v40-schema-surface-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/artifacts/v40-enum-vocabulary-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/artifacts/v40-validation-review-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/artifacts/v40-validator-scope-test-plan.md \
  project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/ledger.md \
  project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/closing-report.md
```

Then commit:

```sh
git commit -m "Close Arc05 schema validation plan" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>"
```

If any other file changes, report it and do not commit until the operator
approves the exact file list.
