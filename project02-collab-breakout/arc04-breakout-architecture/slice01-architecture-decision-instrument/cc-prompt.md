# CC Prompt: Project02 Arc04 Slice01 Architecture Decision Instrument

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Source checkout for read-only grounding:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Assignment

Complete Project02 Arc04 Slice01:

`project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument`

This is a planning/analysis slice. Do not edit source files in the main
checkout. Do not create source `SKILL.md`, README, Makefile, package, or zip
changes. Do not edit planning artifacts outside Project02.

## Required Reading

Read these Project02 files before writing artifacts:

- `project02-collab-breakout/project-plan.md`
- `project02-collab-breakout/ledger.md`
- `project02-collab-breakout/arc04-breakout-architecture/arc-plan.md`
- `project02-collab-breakout/arc04-breakout-architecture/ledger.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/slice-plan.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/ledger.md`
- `project02-collab-breakout/arc02-conceptual-analysis/closing-report.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md`
- `project02-collab-breakout/arc03-functional-analysis/closing-report.md`
- `project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc03-functional-model.md`
- `project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/artifacts/scenario-coverage-synthesis.md`
- `project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/artifacts/functional-fit-and-risk-synthesis.md`
- `project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc04-architecture-inputs.md`
- `project02-collab-breakout/arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc03-close-readiness.md`

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

Treat any prior soft layout sketch as low-weight hypothesis evidence only.
Actual Arc04 decisions must come from the closed Project02 evidence and the
operator acceptance path.

## Deliverables

Create these durable artifacts under:

`project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/artifacts/`

- `architecture-input-register.md`
- `architecture-decision-method.md`
- `component-contract-schema.md`
- `candidate-architecture-worklist.md`
- `operator-decision-and-risk-register.md`

Then update:

- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/ledger.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/slice-plan.md`

At close, also write:

- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/closing-report.md`

Do not write `cdc-verification.md`; CDC writes that after independent
verification.

## Required Artifact Content

`architecture-input-register.md` must record the closed Arc02 and Arc03 inputs
Arc04 will use, including each input's role, evidence strength, and any
source/package or operator-acceptance constraints.

`architecture-decision-method.md` must define:

- classification vocabulary;
- reason-to-load and direct-load tests;
- component versus component-family versus support-asset distinctions;
- adapter, constraint, package/release gate, and non-component categories;
- evidence-grade expectations;
- go / adjust / defer posture;
- operator-acceptance rules.

`component-contract-schema.md` must define the fields later slices must fill
for every component candidate:

- component name;
- purpose and owned problem;
- in/out boundary;
- dependency edges;
- wayfinding behavior;
- support assets and templates;
- adapter notes;
- source paths and package paths;
- package-local links and zip root assumptions;
- release gates and validation commands;
- maintenance owner and version-history responsibility;
- Arc05 implementation-plan fields.

`candidate-architecture-worklist.md` must seed later evaluation with all major
candidates and non-component categories carried from Arc02 and Arc03,
including posture, methodology, ledger, project management, audit, coverage,
delegation, contribution, top-level composer, agent adapter, support assets,
constraints, package/release gates, ontology critique, and component
maintenance.

`operator-decision-and-risk-register.md` must carry D-01 through D-12 and
OQ-01 through OQ-09, or explicitly merge rows when the merge improves Arc04
decision quality. It must preserve risks, gates, acceptance questions, and
go / adjust / defer posture.

## Verification

Run every Verify command in `ledger.md` from the slice directory. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check -- project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument
```

If you stage files, stage only the Project02 Arc04 Slice01 subtree unless the
slice plan explicitly requires a Project02 parent update.

## Close Report

The close report must include:

- verdict;
- artifact inventory;
- verification summary;
- row-by-row ledger walk for F-1 through F-8;
- silent-drop diff against the slice plan;
- bubble-up to Arc04, including whether Slice02 can open or whether the Arc04
  plan needs adjustment first;
- what worked;
- closure metadata.

Keep the outputs as a decision instrument. This slice prepares architecture
evaluation; final accepted architecture belongs to later Arc04 slices and
operator acceptance.
