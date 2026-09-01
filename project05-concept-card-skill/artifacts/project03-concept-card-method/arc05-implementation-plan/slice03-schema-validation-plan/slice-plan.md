# Slice 03: Schema, Enum, and Validation Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice03-schema-validation-plan
status: open
opened-on: 2026-08-31
opened-by: Codex Desktop CDC planning pass
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-source-surface-inventory/cdc-verification.md
  - ../slice02-source-layout-content-plan/cdc-verification.md
  - ../slice02-source-layout-content-plan/artifacts/v40-source-layout-plan.md
  - ../slice02-source-layout-content-plan/artifacts/v40-content-sequence-plan.md
  - ../slice02-source-layout-content-plan/artifacts/v40-surface-routing-decision-register.md
  - ../../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md
  - ../../arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md
artifact-home: artifacts/
```

## Goal

Plan the v4.0 concept-card method schema surfaces, controlled vocabulary, and
validation/review boundaries for implementation. The slice should decide the
schema treatment and enum vocabulary that future templates and examples will
use, plus the validation and validator-code scope needed before packaging and
release planning.

This is planning work only. It does not implement validators or edit the source
checkout.

## Scope

In scope:

- Decide schema surface treatment for concept cards, claims, source support,
  source spans/source locators, relationship edges, competency questions,
  extraction runs, validation results, verification results, reconciliation
  results, preservation decisions, and memory admission records.
- Decide controlled vocabulary and enum spelling for evidence grades,
  extraction confidence, verification state, validation result,
  reconciliation state, CQ status, preservation decision, memory admission,
  source-support status, and related lifecycle fields.
- Plan deterministic structural validation candidates and distinguish them
  from semantic audit, human/operator review, and deferred runtime checks.
- Decide validator-code scope for the first implementation plan: whether it is
  source documentation only, executable code, or a deliberately deferred
  implementation, and what tests/failure-output expectations attach to that
  decision.
- Preserve Slice02's package-compatible planned source layout and route README,
  Makefile, package-list, package-path, generated zip, release gate, and source
  version-history mechanics to Slice04.

Out of scope:

- Editing source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, package-path, validator-code, generated-zip, or release files.
- Implementing executable validators, tests, generated zips, package targets,
  package list edits, package-path exception rows, README/library prose,
  release gates, release readiness, package release, or source version-history
  text.
- Creating runtime services, GraphRAG, graph database, ontology database,
  memory runtime, CCDP service, or live extraction behavior.
- Changing the Slice02 source layout unless a schema or validation finding
  forces a documented Arc05 plan update.
- Closing Arc05 or Project03.

## Required Artifacts

Durable Slice03 outputs belong under `artifacts/`:

- `artifacts/v40-schema-surface-plan.md`
- `artifacts/v40-enum-vocabulary-plan.md`
- `artifacts/v40-validation-review-plan.md`
- `artifacts/v40-validator-scope-test-plan.md`

## Verification Approach

The slice should be verifiable by file existence, schema-surface coverage,
controlled-vocabulary coverage, validation/review boundary coverage,
validator-code/test-scope coverage, later-slice routing, and source checkout
cleanliness.

The artifacts should distinguish accepted schema/enum/validation decisions
from questions deliberately deferred to Slice04, Slice05, or a later
implementation effort.

## Exit Criteria

- The slice open set exists: `slice-plan.md`, `ledger.md`, `cc-prompt.md`, and
  `artifacts/`.
- The four required artifacts exist under `artifacts/`.
- The schema surface plan covers concept card, claim, source support, source
  span/source locator, relationship edge, competency question, extraction run,
  validation result, verification result, reconciliation result, preservation
  decision, and memory admission surfaces.
- The schema surface plan maps those schema surfaces to the Slice02 planned
  template/example/guide paths without editing source files.
- The enum vocabulary plan names controlled vocabulary or enum spelling for
  evidence grade, extraction confidence, verification state, validation
  result, reconciliation state, CQ status, preservation decision, memory
  admission, and source-support status.
- The validation/review plan separates deterministic structural validation,
  semantic audit, human/operator review, and deferred runtime checks, including
  the evidence each kind can and cannot prove.
- The validator scope/test plan decides validator-code scope, test scope,
  invalid-example or failure-output expectations, and what remains manual or
  deferred.
- The artifacts route README, library discoverability, Makefile targets,
  package lists, package-path exceptions, generated zip policy, release gates,
  package release, and source version-history obligations to Slice04.
- The artifacts keep source edits, source implementation, generated zips,
  package release, runtime services, and release readiness out of scope.
- The source checkout remains clean.
- New and modified Slice03 Markdown is ASCII-clean and has no trailing
  whitespace.

## Bubble-up Expectations

At close, report whether Slice03 found any schema, enum, validation, or
validator-scope fact that requires Arc05 re-sequencing, a new slice, or a scope
correction. If no such finding is found, say so explicitly.

Slice03 should prepare Slice04 to plan packaging, discoverability, and release
gates against known schema, enum, validation, and validator-scope decisions.
