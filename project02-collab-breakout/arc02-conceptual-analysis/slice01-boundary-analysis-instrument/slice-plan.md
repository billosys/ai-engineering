# Slice 01: Boundary Analysis Instrument

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
slice: slice01-boundary-analysis-instrument
status: open
opened-on: 2026-08-30
artifact-home: artifacts/
depends-on:
  - arc01-framework-inventory:closed
  - project03-concept-card-method:arc01-method-positioning:slice01-project02-boundary-aid:input-only
  - project03-concept-card-method:arc01-method-positioning:slice02-project02-acceptance-handoff:input-only
blocks:
  - slice02-candidate-boundary-evaluation
related:
  - ../../arc01-framework-inventory/closing-report.md
  - ../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md
  - ../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md
  - ../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md
  - ../../../project03-concept-card-method/arc01-method-positioning/slice01-project02-boundary-aid/artifacts/project02-conceptual-boundary-aid.md
  - ../../../project03-concept-card-method/arc01-method-positioning/slice02-project02-acceptance-handoff/artifacts/project02-arc02-acceptance-handoff.md
  - /Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md
  - /Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
```

## Goal

Create the conceptual-analysis instrument Arc02 will use to evaluate
collaboration-framework component boundaries.

This slice should consume Project02 Arc01's closed evidence base and the
Project03 concept-card boundary aid/handoff, then turn them into a local
Arc02 method and a seeded component-boundary ledger. It should make the next
slice mechanically checkable: every candidate label has a row, every row has
the same conceptual fields, and the evidence vocabulary is explicit.

## Scope

In scope:

- Consume Project02 Arc01 close evidence and Slice03 synthesis artifacts.
- Consume Project03 boundary aid and handoff as operator-accepted inputs only.
- Consume the two top-level v3.2 concept-card workbench docs as read-only
  provenance behind the Project03 boundary lens.
- Define the conceptual-analysis method for Arc02, including classification
  vocabulary, evidence grades, relationship types, competency-question use,
  memory-admission status, and non-final decision posture.
- Create a seeded `component-boundary-ledger.md` with one row per Arc01
  candidate label, ready for Slice02 evaluation.
- Create an input evidence register that records which Project02 and Project03
  artifacts Arc02 is allowed to cite and how strongly.
- Preserve Project01 source/package path constraints as cross-cutting gates.

Out of scope:

- Deciding final collaboration-framework component boundaries.
- Closing Project03 slices, Arc01, or project-level controls.
- Editing source `SKILL.md`, `README.md`, framework docs, templates, Makefiles,
  package scripts, generated zips, or package exceptions.
- Performing the full candidate evaluation intended for Slice02.
- Performing functional usage analysis intended for Arc03.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `conceptual-analysis-method.md` - the Arc02 method for evaluating concept,
  component, support asset, adapter, dependency edge, constraint, template, and
  package/release-gate boundaries.
- `component-boundary-ledger.md` - a seeded analysis ledger with one row per
  Arc01 candidate label and fields for the Slice02 evaluation.
- `arc02-input-evidence-register.md` - the input evidence register showing
  Project02/Project03 artifacts, evidence strength, accepted use, and limits.

## Verification Approach

The slice verifies by checking that the artifacts exist under `artifacts/`,
that they consume the named Project02 and Project03 inputs, that the method
contains the concept-card boundary axes and v3.2 provenance concepts, that the
component-boundary ledger contains all 26 Arc01 candidate labels, that
Project03 is treated as input rather than control surface, that all outputs
remain non-final, and that no source files are edited.

## Exit Criteria

- Required Project02 Arc01, Project03, and v3.2 source-baseline input artifacts
  exist and are cited.
- `artifacts/conceptual-analysis-method.md` defines the Arc02 classification
  vocabulary and evaluation method, including reason to load, problem
  ownership, competency questions, relationship type, evidence grade, and
  memory admission, plus the v3.2 method's one-concept, source-faithful,
  explicit-relationship, confidence, provenance, and preservation ideas.
- `artifacts/component-boundary-ledger.md` contains all 26 Arc01 candidate
  labels with a consistent row schema for Slice02 evaluation.
- `artifacts/arc02-input-evidence-register.md` records Project03 outputs as
  operator-accepted inputs, not Project02 control gates.
- Project01 path/package constraints are carried forward as cross-cutting
  constraints for later boundary evaluation.
- The artifacts state that labels and classifications remain analytical and
  non-final until later operator acceptance.
- No source files are edited.
