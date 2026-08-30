# CC Prompt: Arc02 Slice03 Ontology And Decision Synthesis

You are working in the Project02 planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice directory:

`project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis`

## Mission

Follow this slice's `slice-plan.md` and `ledger.md`. Synthesize the verified
Slice01 method and verified Slice02 candidate-boundary evaluation into Arc02's
non-final conceptual model, naming and boundary findings, Arc04 operator
decision register, and Arc02 close-readiness assessment.

This is synthesis, not implementation and not final architecture selection.
Do not edit source files.

## Required Reading

From the Project02 planning worktree, read:

- `project02-collab-breakout/project-plan.md`
- `project02-collab-breakout/ledger.md`
- `project02-collab-breakout/arc02-conceptual-analysis/arc-plan.md`
- `project02-collab-breakout/arc02-conceptual-analysis/ledger.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/slice-plan.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/ledger.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice01-boundary-analysis-instrument/cdc-verification.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice01-boundary-analysis-instrument/artifacts/conceptual-analysis-method.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice01-boundary-analysis-instrument/artifacts/component-boundary-ledger.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice01-boundary-analysis-instrument/artifacts/arc02-input-evidence-register.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice02-candidate-boundary-evaluation/cdc-verification.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice02-candidate-boundary-evaluation/artifacts/candidate-boundary-evaluation.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice02-candidate-boundary-evaluation/artifacts/component-relationship-map.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice02-candidate-boundary-evaluation/artifacts/conceptual-risk-register.md`
- `project02-collab-breakout/arc01-framework-inventory/closing-report.md`
- `project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md`
- `project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md`
- `project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md`

For spot-check source grounding only, read current source files under:

- `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/README.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/`
- `/Users/oubiwann/lab/billosys/ai-engineering/templates/`

Use source files as evidence, not as permission to edit.

## Required Artifacts

Create `artifacts/` if needed and write:

- `artifacts/arc02-conceptual-model.md`
- `artifacts/boundary-and-naming-findings.md`
- `artifacts/arc04-operator-decision-register.md`
- `artifacts/arc02-close-readiness.md`

### `arc02-conceptual-model.md`

Synthesize the evaluated candidates into a non-final ontology. Include:

- candidate components;
- component family members;
- support assets;
- adapters;
- dependency edges;
- constraints;
- templates;
- package/release gates;
- non-component concepts;
- soft layout hypothesis assessment as tested input, not accepted architecture.

### `boundary-and-naming-findings.md`

Summarize the critical conceptual findings. Cover:

- mislabels;
- improper merges;
- improper splits;
- missing concepts;
- overclaimed mechanisms;
- underfit;
- overfit;
- overlap;
- duplication;
- unresolved relationship questions;
- component-maintenance concerns.

Each finding should cite the Slice02 evidence basis and say what Arc03, Arc04,
or Arc05 should do with it.

### `arc04-operator-decision-register.md`

Record decisions that need operator judgment before Arc04 architecture. Each
decision should include:

- operator decision;
- decision owner;
- options;
- evidence basis;
- risk;
- default recommendation;
- go / adjust / defer posture;
- why this belongs before Arc04.

### `arc02-close-readiness.md`

Assess whether Arc02 can close after Slice03. Map the verdict to Arc02 ledger
rows A-1 through A-7 and state whether a remediation slice is required.

## Guardrails

- Treat Slice01 and Slice02 as verified Project02 inputs.
- Preserve evidence strength. Do not turn attested or analytical claims into
  accepted architecture.
- Treat the soft layout hypothesis as tested low-weight input, not accepted
  architecture.
- Keep Project01 path/package constraints visible as cross-cutting component
  contract requirements.
- Preserve the distinction between conceptual analysis, Arc03 functional
  analysis, Arc04 architecture, and Arc05 implementation planning.
- Do not edit source files.
- Do not edit planning artifacts outside Project02.
- Do not create close-set files until the artifact work is complete.

## Verification

Run every Verify command in `ledger.md` from the slice directory. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check -- project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --cached --check -- project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis
```

If the source checkout has tracked changes, stop and report them. Leave any
unrelated planning-branch changes outside Project02 untouched.

## Close

When the ledger rows are attested:

1. Update `ledger.md` row statuses and evidence.
2. Update `slice-plan.md` status to `proposed-done` and add
   `proposed-done-on: 2026-08-30`.
3. Write `closing-report.md` with a row-by-row ledger walk, artifact inventory,
   silent-drop diff, and Bubble-up to Arc02.
4. Stage only files under:
   `project02-collab-breakout/arc02-conceptual-analysis/slice03-ontology-decision-synthesis/`.

Expected bubble-up question: whether Arc02 can proceed directly to formal arc
close after CDC verification or whether a remediation slice is needed.
