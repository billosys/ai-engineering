# Slice 01: Project02 Boundary Aid

```yaml
project: project03-concept-card-method
arc: arc01-method-positioning
slice: slice01-project02-boundary-aid
status: verified-closed
closed: 2026-08-30
verified: 2026-08-30
verification-note: same-context CDC-style verification; independent fresh-context verification still stronger
artifact-home: artifacts/
depends-on:
  - project02-collab-breakout:arc01-synthesis
blocks:
  - project02-collab-breakout:arc02-conceptual-analysis
  - project03-concept-card-method:arc02-method-inventory
related:
  - ../../../project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md
  - ../../../project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md
  - ../../../project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md
```

## Goal

Open Project03 and produce a compact conceptual-boundary aid that Project02
Arc02 can use when deciding collaboration-framework component boundaries.

The aid should adapt the concept-card method into a focused evaluation lens:
what counts as a concept, component, support asset, adapter, constraint,
template, evidence rule, or memory-bearing substrate. It should treat v3.2 as
the baseline method and v4.0 as the target revision.

## Scope

In scope:

- Create Project03 project, arc, and slice planning artifacts.
- Produce `artifacts/project02-conceptual-boundary-aid.md`.
- Update Project02 planning notes only enough to record the soft dependency
  before Arc02 detailed planning.
- Keep all Project02 and Project03 architecture decisions non-final.

Out of scope:

- Editing source files in `/Users/oubiwann/lab/billosys/ai-engineering`.
- Creating the final concept-card extraction skill.
- Rewriting the v3.2 baseline workbench docs.
- Closing Project02 Arc01 or planning Project02 Arc02 in detail.
- Selecting final Project02 collaboration-framework component boundaries.

## Required Artifacts

Produce this durable artifact under `artifacts/`:

- `project02-conceptual-boundary-aid.md` - a compact aid for Project02 Arc02
  that describes how the concept-card method should sharpen component-boundary
  analysis without taking over Project02.

## Verification Approach

Verify that the Project03 planning scaffold exists, the Project02 aid artifact
exists under `artifacts/`, the aid references Project02 Arc02, the v3.2
baseline, and the v4.0 target, Project02 planning records the soft dependency,
and the implementation source checkout remains clean.

## Exit Criteria

- Project03 `project-plan.md` and project `ledger.md` exist.
- Arc01 `arc-plan.md` and arc `ledger.md` exist.
- Slice01 open set exists: `slice-plan.md`, `ledger.md`, and `cc-prompt.md`.
- `artifacts/project02-conceptual-boundary-aid.md` exists and gives Project02
  Arc02 a non-final boundary-analysis aid.
- Project02 planning records that Arc02 should wait for or consume the
  Project03 Slice01 aid before detailed conceptual analysis.
- No source files are edited.
