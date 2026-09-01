# CC Prompt: Slice04 Model Synthesis and Acceptance

You are CC implementing Project03 Arc03 Slice04 in the planning worktree only.

## Working Directory

Use:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc03-conceptual-model/slice04-model-synthesis`

The source checkout is:

`/Users/oubiwann/lab/billosys/ai-engineering`

Do not write to the source checkout. This slice is planning-only.

## Required Reading

Read these files before creating artifacts:

- `slice-plan.md`
- `ledger.md`
- `../arc-plan.md`
- `../ledger.md`
- `../slice01-construct-boundaries/artifacts/v40-construct-boundary-model.md`
- `../slice01-construct-boundaries/artifacts/v40-construct-decision-register.md`
- `../slice01-construct-boundaries/cdc-verification.md`
- `../slice02-evidence-lifecycle/artifacts/v40-evidence-lifecycle-model.md`
- `../slice02-evidence-lifecycle/artifacts/v40-evidence-state-decision-register.md`
- `../slice02-evidence-lifecycle/cdc-verification.md`
- `../slice03-graph-cq-run-semantics/artifacts/v40-graph-cq-run-semantics.md`
- `../slice03-graph-cq-run-semantics/artifacts/v40-reconciliation-traceability-decision-register.md`
- `../slice03-graph-cq-run-semantics/cdc-verification.md`
- `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md`
- `../../arc02-method-inventory/closing-report.md`

## Task

Implement Slice04 by producing the required durable artifacts and closing the
slice as proposed-done.

Create:

- `artifacts/v40-conceptual-model.md`
- `artifacts/v40-model-decision-register.md`
- `artifacts/arc04-skill-architecture-handoff.md`
- `closing-report.md`

Update:

- `ledger.md`

Do not create `cdc-verification.md`. CDC owns independent verification.

## Artifact Requirements

### `artifacts/v40-conceptual-model.md`

Produce the accepted v4.0 conceptual model for the concept-card method.

The model must integrate:

- concept cards
- claims
- source spans and source support
- evidence grades
- extraction confidence
- relationships and graph-native edges
- competency questions and CQ coverage
- extraction runs
- verifier roles and verification results/states
- validation results
- reconciliation states/results
- memory-admission state

The model must state:

- core invariants
- lifecycle flow
- claim/source/evidence attachment points
- graph and CQ attachment points
- preservation rules for v3.2 carry-forward material
- boundaries between conceptual model, skill architecture, and implementation

### `artifacts/v40-model-decision-register.md`

Create a decision register that includes:

- accepted decisions
- provisional decisions
- deferred decisions
- out-of-scope decisions
- open questions

For each decision, include a short rationale and downstream routing. Use the
prior Slice01, Slice02, and Slice03 decision registers as inputs, but synthesize
them into one Arc03-level register rather than copying them mechanically.

### `artifacts/arc04-skill-architecture-handoff.md`

Create a handoff packet for Arc04. It must identify:

- conceptual-model commitments Arc04 must preserve
- candidate skill-architecture inputs
- likely `SKILL.md`, guide, template, script, example, README, and package
  questions for Arc04 to decide later
- dependencies or risks Arc04 should consider
- Arc03 close input

The handoff must explicitly say that it is not final skill architecture and
does not choose final file layout, package behavior, README integration, exact
schema syntax, or validator implementation.

## Ledger and Closing Report

Update `ledger.md` rows from `open` to `done` only when the row's verification
command passes or the row is satisfied by specific evidence. Keep evidence
concise and cite the produced files.

Create `closing-report.md` with:

- summary
- artifact inventory
- ledger result summary
- explicit scope-as-specified vs scope-as-delivered comparison
- source-checkout cleanliness result
- planning diff/check result
- ASCII/trailing-whitespace hygiene result
- bubble-up notes for Arc03 close and Arc04 planning
- closure statement marking the slice proposed-done pending CDC verification

## Verification

Run and record the results of the ledger checks:

- `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|v40-conceptual-model.md|v40-model-decision-register.md|arc04-skill-architecture-handoff.md" slice-plan.md`
- `test -f artifacts/v40-conceptual-model.md && test -f artifacts/v40-model-decision-register.md && test -f artifacts/arc04-skill-architecture-handoff.md`
- `rg -n "concept card|claim|source span|source support|evidence grade|relationship|edge|competency question|CQ|extraction run|verifier|validation result|reconciliation|memory admission|v4.0 conceptual model" artifacts/v40-conceptual-model.md`
- `rg -n "one concept|atomicity|source-faithful|provenance|claim-source|attachment point|extraction confidence|source support|evidence grade|verification state|reconciliation state|memory admission|not one confidence field|lifecycle|preservation" artifacts/v40-conceptual-model.md`
- `rg -n "accepted|provisional|deferred|out of scope|open question|rationale|dependency|Slice01|Slice02|Slice03|Slice04|Arc04|Arc05" artifacts/v40-model-decision-register.md`
- `rg -n "Arc04|skill architecture|SKILL.md|guide|template|validation script|example|package behavior|README|input|not final|does not choose|handoff|Arc03 close input" artifacts/arc04-skill-architecture-handoff.md`
- `rg -n "Out of scope|source edits|README|Makefile|generated zips|package behavior|final skill layout|schema syntax|enum spelling|validator implementation|GraphRAG runtime|memory runtime|ontology database|CCDP service|live extraction" slice-plan.md artifacts/v40-conceptual-model.md artifacts/v40-model-decision-register.md artifacts/arc04-skill-architecture-handoff.md`
- `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet`

Also run:

- `git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check`
- ASCII hygiene over new/modified Slice04 files
- trailing-whitespace hygiene over new/modified Slice04 files

Do not commit unless the operator explicitly asks.
