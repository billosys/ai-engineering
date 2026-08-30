# CC Prompt: Project02 Arc03 Slice04 Functional Synthesis

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Source checkout for read-only grounding:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Assignment

Complete Project02 Arc03 Slice04:

`project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis`

This is a planning/analysis slice. Do not edit source files in the main
checkout. Do not create source `SKILL.md`, README, Makefile, package, or zip
changes. Do not edit planning artifacts outside Project02.

## Required Reading

Read these Project02 files before writing artifacts:

- `project02-collab-breakout/project-plan.md`
- `project02-collab-breakout/ledger.md`
- `project02-collab-breakout/arc03-functional-analysis/arc-plan.md`
- `project02-collab-breakout/arc03-functional-analysis/ledger.md`
- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/cdc-verification.md`
- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/artifacts/functional-analysis-method.md`
- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/artifacts/usage-surface-inventory.md`
- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/artifacts/scenario-matrix.md`
- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/artifacts/arc03-input-register.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/cdc-verification.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/artifacts/current-workflow-evaluation.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/artifacts/load-path-friction-register.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/artifacts/functional-deficiency-register.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/artifacts/source-package-role-language-notes.md`
- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/cdc-verification.md`
- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/artifacts/standalone-scenario-evaluation.md`
- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/artifacts/composition-scenario-evaluation.md`
- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/artifacts/minimum-load-and-dependency-matrix.md`
- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/artifacts/component-dependency-adapter-findings.md`
- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/artifacts/arc03-functional-decision-inputs.md`
- `project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/slice-plan.md`
- `project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/ledger.md`

Read these Arc02 conceptual-analysis artifacts as candidate-boundary evidence,
not accepted architecture:

- `project02-collab-breakout/arc02-conceptual-analysis/closing-report.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md`

You may inspect the current source checkout for factual grounding. Keep source
files read-only.

Suggested source grounding includes:

- `README.md`
- `SKILL.md`
- `docs/AI-CONSTITUTION-SUPPLEMENT.md`
- `docs/AI-ENGINEERING-METHODOLOGY.md`
- `docs/PROJECT-MANAGEMENT.md`
- `docs/pm/*.md`
- `templates/LEDGER-DISCIPLINE.md`
- `docs/CODE-AUDIT.md`
- `docs/CLAUDE-CODE-COVERAGE.md`
- `docs/SUBAGENT-DELEGATION-POLICY.md`
- `docs/CONTRIBUTION-STYLE.md`
- `templates/CONTRIBUTION-TICKET.md`
- `Makefile`
- package/path validation docs or exceptions where relevant

## Deliverables

Create these durable artifacts under:

`project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/artifacts/`

- `arc03-functional-model.md`
- `scenario-coverage-synthesis.md`
- `functional-fit-and-risk-synthesis.md`
- `arc04-architecture-inputs.md`
- `arc03-close-readiness.md`

Then update:

- `project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/ledger.md`
- `project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/slice-plan.md`

At close, also write:

- `project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/closing-report.md`

Do not write `cdc-verification.md`; CDC writes that after independent
verification.

## Required Artifact Content

`arc03-functional-model.md` must synthesize the functional model across:

- direct source reading;
- source-clone reading;
- packaged skill reading;
- skill loading;
- human orientation;
- session start;
- planning;
- execution;
- review;
- audit;
- coverage;
- delegation;
- contribution;
- combination workflows.

`scenario-coverage-synthesis.md` must cover S-01 through S-14 from the
Slice01 scenario matrix and distinguish current monolith, standalone,
composed, and top-level composer scenario findings.

`functional-fit-and-risk-synthesis.md` must consolidate:

- inefficiencies;
- deficiencies;
- context-load and context-cost problems;
- unclear handoffs;
- routing friction;
- missing functional goals;
- under-served surfaces;
- over-rich and over-thin paths;
- source/package risks;
- role-language risks;
- package/release risks;
- relevant `LPF-*`, `FD-*`, `SPR-*`, and `RLF-*` baseline rows.

`arc04-architecture-inputs.md` must record:

- Arc04-ready architecture inputs;
- component-fit signals;
- strong, plausible, and weak direct-load classifications;
- dependency edges;
- support assets;
- adapters;
- constraints;
- package/release gates;
- component contract implications;
- operator questions;
- go / adjust / defer posture.

`arc03-close-readiness.md` must map Slice04 outputs to Arc03 ledger rows A-5
through A-9, state whether a remediation slice is required before Arc03 close,
and preserve the evidence needed for formal arc close. This is not the Arc03
closing report; it is a readiness input for that close.

## Verification

Run every Verify command in `ledger.md` from the slice directory. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check -- project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis
```

If you stage files, stage only the Project02 Slice04 subtree unless the slice
plan explicitly requires a Project02 parent update.

## Close Report

The close report must include:

- verdict;
- artifact inventory;
- verification summary;
- row-by-row ledger walk for F-1 through F-8;
- silent-drop diff against the slice plan;
- bubble-up to Arc03, including whether Arc03 is ready for formal arc close or
  requires a remediation slice;
- what worked;
- closure metadata.

Keep the outputs analytical and non-final. This slice prepares functional
inputs for Arc04; final architecture belongs to Arc04, after Arc03 closes and
the operator accepts the architecture direction.
