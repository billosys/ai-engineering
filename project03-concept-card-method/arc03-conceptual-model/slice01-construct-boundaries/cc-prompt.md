# CC Prompt: Slice 01 Construct Boundaries

You are implementing Project03 Arc03 Slice01:
`slice01-construct-boundaries`.

## Required Reading

Read these files before editing:

1. `/Users/oubiwann/.codex/skills/collaboration-framework/SKILL.md`
2. `/Users/oubiwann/lab/billosys/ai-engineering/docs/PROJECT-MANAGEMENT.md`
3. `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/01-scales-of-work.md`
4. `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/02-canonical-planning-worktree.md`
5. `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/03-planning-top-down.md`
6. `/Users/oubiwann/lab/billosys/ai-engineering/templates/LEDGER-DISCIPLINE.md`
7. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/project-plan.md`
8. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/ledger.md`
9. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/closing-report.md`
10. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc02-synthesis.md`
11. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md`
12. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice02-v40-gap-analysis/artifacts/v40-gap-register.md`
13. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice02-v40-gap-analysis/artifacts/v32-to-v40-carry-forward-change-matrix.md`
14. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc03-conceptual-model/arc-plan.md`
15. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc03-conceptual-model/ledger.md`
16. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc03-conceptual-model/slice01-construct-boundaries/slice-plan.md`
17. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc03-conceptual-model/slice01-construct-boundaries/ledger.md`

## Assignment

Produce the first Arc03 conceptual-model artifacts: a construct-boundary model
and a per-construct decision register.

Artifact home: `artifacts/`.

Required artifacts:

- `artifacts/v40-construct-boundary-model.md`
- `artifacts/v40-construct-decision-register.md`

## Artifact Requirements

`artifacts/v40-construct-boundary-model.md` must:

- State the purpose of the construct-boundary pass.
- Cover all Arc02 candidate constructs: concept card, claim, source span,
  evidence grade, relationship or edge, competency question, extraction run,
  verifier, reconciliation, and memory admission.
- Distinguish first-class entities, value objects, statuses, roles, processes,
  result records, fields, and deferred concerns where useful.
- Preserve v3.2 carry-forward commitments while naming v4.0 conceptual-model
  changes as model decisions, not implementation details.
- Mark provisional areas that Slice02, Slice03, or Slice04 must resolve.

`artifacts/v40-construct-decision-register.md` must:

- Provide one row per candidate construct.
- Include classification, rationale, dependencies, open question, downstream
  Arc03 route, and whether the decision is accepted, provisional, or deferred.
- Make the boundary between method concept and later skill/implementation
  concern explicit.

## Scope Fences

This slice does not finalize evidence-grade vocabulary, verification-state
transitions, reconciliation algorithms, memory-admission policy, schema syntax,
skill layout, package behavior, deterministic validator scripts, README
changes, Makefile changes, or source edits.

Do not edit source files in `/Users/oubiwann/lab/billosys/ai-engineering`.
Do not create `closing-report.md` until the ledger rows are complete. Do not
create `cdc-verification.md`; that belongs to the independent CDC pass.

## Ledger Discipline

Work against `ledger.md`. Update each row as you complete it with attested
evidence. At close, write `closing-report.md` with a row-by-row disposition
and bubble-up. If you discover that the construct-boundary slice is too large
or under-specified, report the needed plan change rather than silently
shrinking the model.

## Verification Hints

Run the ledger checks from this directory:

```sh
cd /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc03-conceptual-model/slice01-construct-boundaries
test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|v40-construct-boundary-model.md|v40-construct-decision-register.md" slice-plan.md cc-prompt.md
test -f artifacts/v40-construct-boundary-model.md && test -f artifacts/v40-construct-decision-register.md
rg -n "concept card|claim|source span|evidence grade|relationship|edge|competency question|extraction run|verifier|reconciliation|memory admission" artifacts/v40-construct-boundary-model.md artifacts/v40-construct-decision-register.md
rg -n "first-class entity|value object|status|role|process|result record|field|deferred concern|rationale|dependencies|open question|Slice02|Slice03|Slice04" artifacts/v40-construct-decision-register.md
rg -n "v3.2|carry forward|atomicity|source-faithful|provenance|typed relationships|competency questions|source-primary re-extraction|preservation|v4.0 conceptual model" artifacts/v40-construct-boundary-model.md artifacts/v40-construct-decision-register.md
rg -n "Out of scope|evidence-grade vocabulary|verification-state transitions|reconciliation algorithms|memory-admission policy|skill layout|package behavior|deterministic validator|README|Makefile|source edits" slice-plan.md artifacts/v40-construct-boundary-model.md artifacts/v40-construct-decision-register.md
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

