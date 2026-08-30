# CC Prompt: Slice 03 Inventory Synthesis

You are implementing Project03 Arc02 Slice03:
`slice03-inventory-synthesis`.

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
9. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/arc-plan.md`
10. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/ledger.md`
11. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice03-inventory-synthesis/slice-plan.md`
12. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice03-inventory-synthesis/ledger.md`
13. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice01-v32-source-inventory/cdc-verification.md`
14. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice01-v32-source-inventory/artifacts/v32-source-inventory.md`
15. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice01-v32-source-inventory/artifacts/v32-method-structure-map.md`
16. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice01-v32-source-inventory/artifacts/v32-original-assessment.md`
17. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice02-v40-gap-analysis/cdc-verification.md`
18. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice02-v40-gap-analysis/artifacts/v40-gap-register.md`
19. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice02-v40-gap-analysis/artifacts/v32-to-v40-carry-forward-change-matrix.md`

## Assignment

Produce the Slice03 synthesis artifacts that let Arc02 close and let Arc03
start from a clean conceptual-model input packet.

Artifact home: `artifacts/`.

Required artifacts:

- `artifacts/arc02-synthesis.md`
- `artifacts/arc03-conceptual-model-inputs.md`

## Artifact Requirements

`artifacts/arc02-synthesis.md` must:

- Treat the verified Slice01 inventory and verified Slice02 gap analysis as
  the source of truth.
- State what v3.2 keeps, what v4.0 must change, what requires operator choice,
  and what is deferred or out of scope.
- Provide explicit Arc02 close/composition input, including how the synthesis
  supports Arc02 ledger rows A-4, A-5, and A-6.
- Preserve the source-backed framing and avoid introducing new design
  commitments.

`artifacts/arc03-conceptual-model-inputs.md` must:

- Name the candidate constructs Arc03 must consider: concept card, claim,
  source span, evidence grade, relationship or edge, competency question,
  extraction run, verifier, reconciliation, and memory admission.
- Record open questions and required distinctions for those constructs.
- Mark these as Arc03 inputs, not final conceptual model decisions.
- State which packaging, skill-layout, implementation, and source-edit choices
  remain out of scope for Slice03.

## Scope Fences

This slice does not design the v4.0 conceptual model. It does not choose the
Arc04 skill layout. It does not plan Arc05 implementation mechanics. It does
not edit source files in `/Users/oubiwann/lab/billosys/ai-engineering`.

If you discover a defect in the verified Slice01 or Slice02 artifacts, record
it clearly in the closing report as a bubble-up instead of quietly rewriting
the prior slice outputs.

## Ledger Discipline

Work against `ledger.md`. Update each row as you complete it with attested
evidence. At close, write `closing-report.md` with a row-by-row disposition
and bubble-up. Do not create `cdc-verification.md`; that belongs to the
independent CDC pass after your close.

## Verification Hints

Run the ledger checks from this directory:

```sh
cd /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice03-inventory-synthesis
test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|arc02-synthesis.md|arc03-conceptual-model-inputs.md" slice-plan.md cc-prompt.md
test -f artifacts/arc02-synthesis.md && test -f artifacts/arc03-conceptual-model-inputs.md
rg -n "v32-source-inventory.md|v32-method-structure-map.md|v32-original-assessment.md|v40-gap-register.md|v32-to-v40-carry-forward-change-matrix.md|v3.2 keeps|v4.0 must change|operator choice|deferred|out of scope" artifacts/arc02-synthesis.md
rg -n "Arc02 close|composition|A-4|A-5|A-6|carry forward|architectural change|operator decision|defer" artifacts/arc02-synthesis.md
rg -n "concept card|claim|source span|evidence grade|relationship|competency question|extraction run|verifier|reconciliation|memory admission|open question|not final" artifacts/arc03-conceptual-model-inputs.md
rg -n "does not design|Out of scope|Arc03|conceptual model|Arc04|skill layout|Arc05|implementation|source edits" slice-plan.md artifacts/arc02-synthesis.md artifacts/arc03-conceptual-model-inputs.md
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

