# CC Prompt: Project02 Arc03 Slice03 Standalone And Composition Scenario Evaluation

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Source checkout for read-only grounding:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Assignment

Complete Project02 Arc03 Slice03:

`project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation`

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
- `project02-collab-breakout/arc03-functional-analysis/slice01-usage-surface-instrument/artifacts/scenario-matrix.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/cdc-verification.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/artifacts/current-workflow-evaluation.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/artifacts/load-path-friction-register.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/artifacts/functional-deficiency-register.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/artifacts/source-package-role-language-notes.md`
- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/slice-plan.md`
- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/ledger.md`

Read these Arc02 conceptual-analysis artifacts as candidate-boundary evidence,
not accepted architecture:

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

`project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/artifacts/`

- `standalone-scenario-evaluation.md`
- `composition-scenario-evaluation.md`
- `minimum-load-and-dependency-matrix.md`
- `component-dependency-adapter-findings.md`
- `arc03-functional-decision-inputs.md`

Then update:

- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/ledger.md`
- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/slice-plan.md`

At close, also write:

- `project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation/closing-report.md`

Do not write `cdc-verification.md`; CDC writes that after independent
verification.

## Required Artifact Content

`standalone-scenario-evaluation.md` must evaluate standalone component
scenarios S-08 through S-11 from the Slice01 scenario matrix. For each
scenario, record:

- Actor;
- Entrypoint;
- Trigger;
- Inputs;
- Expected outcome;
- Load set;
- Dependencies;
- Friction signals;
- Evidence collected;
- Downstream owner.

It must also test candidate direct-load moments for coverage hardening,
delegation policy, contribution guidance, posture/methodology, PM, ledger,
audit, agent-adapter, and ontology critique where relevant.

`composition-scenario-evaluation.md` must evaluate composed component
scenarios S-12 through S-14 from the Slice01 scenario matrix. It must cover
PM+ledger, top-level composer, role-language adapter, posture/methodology,
contribution style plus ticket template, and any other composed flows required
by the evidence.

`minimum-load-and-dependency-matrix.md` must compare:

- current monolith;
- standalone component;
- composed component;
- top-level composer combination.

For each, record minimum useful load, context cost, dependency order, over-rich
or over-thin risk, routing friction, and the relevant Slice02 `LPF-*` or
`FD-*` baseline.

`component-dependency-adapter-findings.md` must record:

- dependency direction;
- project-management component-family behavior;
- support-asset travel;
- contribution ticket template ownership;
- role-language clarity;
- agent-adapter behavior;
- source/package constraints;
- package-local link behavior;
- zip root behavior;
- release surface behavior;
- `make check-package-paths`;
- package/release gate implications.

`arc03-functional-decision-inputs.md` must carry forward:

- functional fit signals for Slice04 synthesis;
- concepts that lack real functional load paths;
- concepts that should remain dependency edges, adapters, support assets,
  constraints, or package/release gates on current evidence;
- unresolved operator questions for Arc04;
- go / adjust / defer posture;
- explicit non-final architecture posture.

## Verification

Run every Verify command in `ledger.md` from the slice directory. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check -- project02-collab-breakout/arc03-functional-analysis/slice03-standalone-composition-evaluation
```

If you stage files, stage only the Project02 Slice03 subtree unless the slice
plan explicitly requires a Project02 parent update.

## Close Report

The close report must include:

- verdict;
- artifact inventory;
- verification summary;
- row-by-row ledger walk for F-1 through F-8;
- silent-drop diff against the slice plan;
- bubble-up to Arc03, including whether Arc03 plan changes are required before
  Slice04 opens;
- what worked;
- closure metadata.

Keep the outputs analytical and non-final. This slice evaluates standalone and
composed functional behavior; final architecture belongs to Arc04, after Arc03
closes and the operator accepts the architecture direction.
