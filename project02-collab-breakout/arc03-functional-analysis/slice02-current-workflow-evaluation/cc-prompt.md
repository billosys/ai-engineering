# CC Prompt: Project02 Arc03 Slice02 Current Workflow Evaluation

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Source checkout for read-only grounding:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Assignment

Complete Project02 Arc03 Slice02:

`project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation`

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
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/slice-plan.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/ledger.md`

Read Arc02 close evidence as background:

- `project02-collab-breakout/arc02-conceptual-analysis/closing-report.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md`

You may inspect the current source checkout for factual grounding. Keep source
files read-only.

Suggested source grounding includes:

- `README.md`
- `SKILL.md`
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

`project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/artifacts/`

- `current-workflow-evaluation.md`
- `load-path-friction-register.md`
- `functional-deficiency-register.md`
- `source-package-role-language-notes.md`

Then update:

- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/ledger.md`
- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/slice-plan.md`

At close, also write:

- `project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation/closing-report.md`

Do not write `cdc-verification.md`; CDC writes that after independent
verification.

## Required Artifact Content

`current-workflow-evaluation.md` must evaluate current-monolith scenarios S-01
through S-07 from the Slice01 scenario matrix. For each scenario, record:

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

It must also cover current framework usage surfaces for README/source-clone,
packaged skill, LLM skill loading, session start, planning, execution, review,
slice close, arc close, audit, coverage, delegation, contribution,
source/package, and role-language behavior.

`load-path-friction-register.md` must record:

- routing friction;
- context cost;
- dependency-order friction;
- unclear handoff;
- support-asset discovery;
- discoverability;
- source/package ambiguity;
- role-language clarity;
- minimum useful load issues;
- over-rich and over-thin current load paths.

`functional-deficiency-register.md` must record:

- functional deficiencies;
- missing functional goals;
- under-served surfaces;
- missing entrypoints;
- over-rich or over-thin load paths;
- hidden dependencies;
- output-location conflicts;
- inherited-composition risks;
- underfit and overfit current behavior;
- downstream routing to Slice03, Slice04, Arc04, or Arc05.

`source-package-role-language-notes.md` must record:

- Project01 and `project01-harmonise-paths` source/package constraints;
- package-local link behavior;
- zip root behavior;
- release surface behavior;
- CCDP contrast;
- `make check-package-paths`;
- component contract and package/release gate implications;
- CDC, CC, Claude, Codex, operator, verifier, reviewer, and fresh-context
  role-language clarity.

## Verification

Run every Verify command in `ledger.md` from the slice directory. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check -- project02-collab-breakout/arc03-functional-analysis/slice02-current-workflow-evaluation
```

If you stage files, stage only the Project02 Slice02 subtree unless the slice
plan explicitly requires a Project02 parent update.

## Close Report

The close report must include:

- verdict;
- artifact inventory;
- verification summary;
- row-by-row ledger walk for F-1 through F-8;
- silent-drop diff against the slice plan;
- bubble-up to Arc03, including whether Arc03 plan changes are required before
  Slice03 opens;
- what worked;
- closure metadata.

Keep the outputs analytical and non-final. This slice evaluates the current
monolith only. Final architecture belongs to Arc04, after Arc03 closes and the
operator accepts the architecture direction.
