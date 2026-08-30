# CC Prompt: Project02 Arc03 Slice01 Usage Surface Instrument

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Source checkout for read-only grounding:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Assignment

Complete Project02 Arc03 Slice01:

`project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument`

This is a planning/analysis slice. Do not edit source files in the main
checkout. Do not create source `SKILL.md`, README, Makefile, package, or zip
changes. Do not edit planning artifacts outside Project02.

## Required Reading

Read these Project02 files before writing artifacts:

- `project02-collab-breakout/project-plan.md`
- `project02-collab-breakout/ledger.md`
- `project02-collab-breakout/arc02-conceptual-analysis/closing-report.md`
- `project02-collab-breakout/arc03-functional-analysis/arc-plan.md`
- `project02-collab-breakout/arc03-functional-analysis/ledger.md`
- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/slice-plan.md`
- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/ledger.md`

Read these Arc02 synthesis artifacts as the required evidence base:

- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-close-readiness.md`

You may inspect the current source checkout for factual grounding, but source
files are read-only for this slice.

## Deliverables

Create these durable artifacts under:

`project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/artifacts/`

- `functional-analysis-method.md`
- `usage-surface-inventory.md`
- `scenario-matrix.md`
- `arc03-input-register.md`

Then update:

- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/ledger.md`
- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/slice-plan.md`

At close, also write:

- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/closing-report.md`

Do not write `cdc-verification.md`; CDC writes that after independent
verification.

## Required Artifact Content

`functional-analysis-method.md` must define:

- usage surface;
- load path;
- entrypoint;
- trigger;
- actor;
- minimum useful load set;
- dependency order;
- context cost;
- routing friction;
- functional deficiency;
- source/package mode;
- role-language clarity;
- evidence grade;
- non-final architecture posture.

`usage-surface-inventory.md` must cover:

- direct source-clone reading;
- packaged skill reading;
- LLM skill loading;
- human orientation;
- session start;
- planning;
- execution;
- review;
- slice close;
- arc close;
- audit;
- coverage;
- delegation;
- upstream contribution;
- standalone use;
- composed use and combinations.

`scenario-matrix.md` must contain scenario rows with fields for:

- Scenario ID;
- Actor;
- Entrypoint;
- Trigger;
- Inputs;
- Expected outcome;
- Load set;
- Dependencies;
- Friction signals;
- Evidence to collect;
- Downstream owner.

`arc03-input-register.md` must carry forward:

- Arc02 conceptual risks as functional questions;
- Arc04 operator decisions as functional questions;
- Project01 path/package constraints as functional test surfaces;
- questions that later slices must answer before Arc04 architecture.

## Verification

Run every Verify command in `ledger.md` from the slice directory. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check -- project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument
```

If you stage files, stage only the Project02 Slice01 subtree unless the slice
plan explicitly requires a Project02 parent update.

## Close Report

The close report must include:

- verdict;
- artifact inventory;
- verification summary;
- row-by-row ledger walk for F-1 through F-8;
- silent-drop diff against the slice plan;
- bubble-up to Arc03, including whether Arc03 plan changes are required before
  Slice02 opens;
- what worked;
- closure metadata.

Keep the outputs analytical and non-final. Final architecture belongs to
Arc04, after Arc03 closes and the operator accepts the architecture direction.
