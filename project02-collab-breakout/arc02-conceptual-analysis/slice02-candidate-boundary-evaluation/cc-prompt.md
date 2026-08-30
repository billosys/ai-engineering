# CC Prompt: Arc02 Slice02 Candidate Boundary Evaluation

You are working in the Project02 planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice directory:

`project02-collab-breakout/arc02-conceptual-analysis/slice02-candidate-boundary-evaluation`

## Mission

Follow this slice's `slice-plan.md` and `ledger.md`. Evaluate all 26 seeded
candidate labels from Slice01 using the Slice01 conceptual-analysis method.
Produce the durable evaluation artifacts under this slice's `artifacts/`
directory, update the slice ledger with attested evidence, mark the slice
`proposed-done`, and write `closing-report.md`.

This is conceptual analysis only. Do not select final breakout architecture.
Do not edit source files.

## Required Reading

From the Project02 planning worktree, read:

- `project02-collab-breakout/project-plan.md`
- `project02-collab-breakout/ledger.md`
- `project02-collab-breakout/arc02-conceptual-analysis/arc-plan.md`
- `project02-collab-breakout/arc02-conceptual-analysis/ledger.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice02-candidate-boundary-evaluation/slice-plan.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice02-candidate-boundary-evaluation/ledger.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice01-boundary-analysis-instrument/cdc-verification.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice01-boundary-analysis-instrument/artifacts/conceptual-analysis-method.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice01-boundary-analysis-instrument/artifacts/component-boundary-ledger.md`
- `project02-collab-breakout/arc02-conceptual-analysis/slice01-boundary-analysis-instrument/artifacts/arc02-input-evidence-register.md`
- `project02-collab-breakout/arc01-framework-inventory/closing-report.md`
- `project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md`
- `project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md`
- `project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md`

For source grounding, read the relevant current source files under:

- `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/README.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/`
- `/Users/oubiwann/lab/billosys/ai-engineering/templates/`

Use source files as evidence, not as permission to edit. If Arc01 evidence and
current source differ, preserve the difference as an evaluation finding rather
than silently smoothing it away.

## Soft Layout Hypothesis

The operator supplied a 2026-08-30 screenshot with a possible future layout.
Treat this as a soft, low-weight hypothesis to test against the evidence, not
as accepted architecture and not as a recommendation to follow.

The sketch suggests:

```text
knowledge/collaboration-framework/
  SKILL.md                       # top-level composer
  guides/
    posture-and-ethics.md
    engineering-methodology.md
    verification-methodology.md
    maintenance.md

knowledge/project-management/
  SKILL.md                       # PM wayfinder
  guides/
    scales-of-work.md
    planning-worktree.md
    planning-top-down.md
    closing-slices.md
    closing-arcs.md
    confirmation-protocol.md
    anti-patterns.md

knowledge/ledger-discipline/
  SKILL.md
  guides/
    evidence-ladder.md
    row-closure.md
    verification.md
  templates/

knowledge/code-audit/
knowledge/coverage-hardening/
knowledge/delegation-policy/
knowledge/contribution-guidance/
```

The screenshot also suggests that project management may be a component family,
ledger discipline is a strong standalone candidate, delegation is narrow and
standalone, contribution style probably travels with its ticket template, and
the top-level framework remains a composer over accepted components.

Your job is to test these claims. Where evidence supports the sketch, record
that with evidence grade. Where it over-splits, under-splits, mislabels, or
prematurely chooses architecture, record that as a risk or question for
Slice03.

## Required Artifacts

Create `artifacts/` if needed and write:

- `artifacts/candidate-boundary-evaluation.md`
- `artifacts/component-relationship-map.md`
- `artifacts/conceptual-risk-register.md`

### `candidate-boundary-evaluation.md`

Include one completed row per seeded label. Use a schema that exposes, at
minimum:

- Candidate label
- Final classification, using the Slice01 classification vocabulary
- Reason to load
- Problem ownership
- Competency questions
- Relationship edges
- Evidence grade
- Memory admission
- Source evidence
- Conceptual risks
- Path/package gates
- Provisional disposition

Do not leave any row as `seeded-for-Slice02`. If evidence is weak, mark the
weakness as the evaluation result; do not invent confidence.

### `component-relationship-map.md`

Record typed edges using the Slice01 relationship vocabulary:

- prerequisite
- extends
- uses
- supports
- constrains
- contrasts-with
- composes-into
- routes-to

Also record likely component families, support assets, adapters, constraints,
and unresolved relationship questions.

### `conceptual-risk-register.md`

Cover these categories explicitly, even when a category has no confirmed
instance:

- mislabel
- improper merge
- improper split
- missing concept
- overclaimed mechanism
- underfit
- overfit
- overlap
- duplication

Each risk entry should include the affected label or labels, evidence basis,
risk disposition, and follow-up needed for Slice03, Arc03, or Arc04.

## Guardrails

- Treat Slice01's method as the local evaluation contract.
- Treat Arc01 candidate labels as evidence handles, not final component
  boundaries.
- Treat the soft layout hypothesis as low-weight input; evidence outranks it.
- Treat accepted concept-card inputs as input-only method aids, not Project02
  control gates.
- Apply Project01 path/package rules as cross-cutting constraints.
- Keep every architecture claim analytical and non-final. Final architecture
  belongs to Arc04 after Arc03 functional analysis and operator acceptance.
- Do not edit `/Users/oubiwann/lab/billosys/ai-engineering` source files.
- Do not edit planning artifacts outside Project02.
- Do not create close-set files until the artifact work is complete.

## Verification

Run every Verify command in `ledger.md` from the slice directory. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check -- project02-collab-breakout/arc02-conceptual-analysis/slice02-candidate-boundary-evaluation
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --cached --check -- project02-collab-breakout/arc02-conceptual-analysis/slice02-candidate-boundary-evaluation
```

If the source checkout has tracked changes, stop and report them. If there are
unrelated planning-branch changes outside Project02, leave them untouched.

## Close

When the ledger rows are attested:

1. Update `ledger.md` row statuses and evidence.
2. Update `slice-plan.md` status to `proposed-done` and add
   `proposed-done-on: 2026-08-30`.
3. Write `closing-report.md` with a row-by-row ledger walk, artifact
   inventory, silent-drop diff, and Bubble-up to Arc02.
4. Stage only files under:
   `project02-collab-breakout/arc02-conceptual-analysis/slice02-candidate-boundary-evaluation/`.

Expected bubble-up question: whether Slice02 found evaluation results that
require changing Arc02's Slice03 scope before synthesis begins.
