# Slice 01: v3.2 Source Inventory

```yaml
project: project03-concept-card-method
arc: arc02-method-inventory
slice: slice01-v32-source-inventory
status: open
artifact-home: artifacts/
depends-on:
  - project03-concept-card-method:arc01-method-positioning
blocks:
  - project03-concept-card-method:arc02-method-inventory:slice02-v40-gap-analysis
related:
  - ../../arc-plan.md
  - ../../ledger.md
  - ../../../project-plan.md
  - ../../../ledger.md
  - /Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md
  - /Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
```

## Goal

Produce a source-backed inventory of the v3.2 concept-card method from the two
workbench docs.

This slice should map what v3.2 actually says before Arc02 starts gap analysis.
It should not design the v4.0 replacement.

## Scope

In scope:

- Read both v3.2 workbench docs directly.
- Inventory each document's purpose, structure, schema, workflow phases,
  validation checks, provenance rules, relationship model, competency-question
  handling, confidence semantics, re-extraction mechanics, and preservation
  checks.
- Preserve exact copies of the two `workbench/00*.md` v3.2 source docs under
  the slice artifact home.
- Preserve the pre-Project03 assessment memo as context for later gap analysis,
  while keeping the Slice01 inventory descriptive and source-grounded.
- Produce a method-structure map that shows which v3.2 constructs feed later
  v4.0 questions.
- Keep citations source-backed with paths and line anchors where useful.

Out of scope:

- Designing the v4.0 conceptual model.
- Deciding the final skill layout.
- Editing source files in `/Users/oubiwann/lab/billosys/ai-engineering`.
- Rewriting the v3.2 workbench docs.
- Running extraction against a live corpus.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `source-docs/0009-howto-concept-card-extraction-with-llms-v3.2.md` - exact
  preserved copy of the v3.2 extraction guide.
- `source-docs/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md` -
  exact preserved copy of the v3.2 parallel re-extraction guide.
- `v32-original-assessment.md` - preserved assessment memo from the
  pre-Project03 conversation, with a note that the target revision is now v4.0.
- `v32-source-inventory.md` - per-document inventory of the v3.2 baseline
  method.
- `v32-method-structure-map.md` - cross-document map of schema, workflow,
  validation, provenance, relationships, competency questions, confidence, and
  re-extraction mechanics.

## Verification Approach

Verify that the open set exists, the preserved source snapshots match the
workbench inputs, the original assessment memo is present, both inventory
artifacts exist under `artifacts/`, the inventory covers both v3.2 source docs
and major method categories, the structure map separates baseline observations
from later v4.0 questions, and the implementation source checkout remains
clean.

## Exit Criteria

- Slice01 open set exists: `slice-plan.md`, `ledger.md`, and `cc-prompt.md`.
- `artifacts/source-docs/0009-howto-concept-card-extraction-with-llms-v3.2.md`
  matches the workbench source document.
- `artifacts/source-docs/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`
  matches the workbench source document.
- `artifacts/v32-original-assessment.md` exists and preserves the original
  assessment with the v4.0 numbering note.
- `artifacts/v32-source-inventory.md` exists.
- `artifacts/v32-method-structure-map.md` exists.
- Inventory covers both v3.2 workbench docs and the categories named in scope.
- Structure map preserves v3.2 as baseline evidence and flags v4.0 questions
  without answering them prematurely.
- No source files are edited.
