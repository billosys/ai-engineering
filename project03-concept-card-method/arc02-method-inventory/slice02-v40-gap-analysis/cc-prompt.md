# CC Prompt: Slice 02 v4.0 Gap Analysis

You are working in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice02-v40-gap-analysis`

This is Project03 Arc02 Slice02. The slice is planning/analysis work only. Do
not edit source files in `/Users/oubiwann/lab/billosys/ai-engineering`.

## Required Reading

Before writing artifacts, read:

1. `/Users/oubiwann/.codex/skills/collaboration-framework/SKILL.md`
2. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/PROJECT-MANAGEMENT.md`
3. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/01-scales-of-work.md`
4. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/02-canonical-planning-worktree.md`
5. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/03-planning-top-down.md`
6. `/Users/oubiwann/.codex/skills/collaboration-framework/templates/LEDGER-DISCIPLINE.md`
7. `../../../project-plan.md`
8. `../../../ledger.md`
9. `../../arc-plan.md`
10. `../../ledger.md`
11. `slice-plan.md`
12. `ledger.md`
13. `../slice01-v32-source-inventory/cdc-verification.md`
14. `../slice01-v32-source-inventory/artifacts/v32-source-inventory.md`
15. `../slice01-v32-source-inventory/artifacts/v32-method-structure-map.md`
16. `../slice01-v32-source-inventory/artifacts/v32-original-assessment.md`

## Assignment

Produce a source-backed v4.0 gap analysis from the verified v3.2 baseline.

Use the Slice01 inventory and structure map as the primary baseline, with the
original assessment as context. Identify what v3.2 should carry forward, what
needs minor cleanup, what requires v4.0 architectural change, what needs
operator decision, and what should be deferred.

Do not design the v4.0 conceptual model in this slice. Do not decide the final
skill layout. Record gaps and routing clearly enough that Slice03 can
synthesize Arc02's close input, and Arc03 can later define the conceptual
model.

## Required Outputs

Create:

- `artifacts/v40-gap-register.md`
- `artifacts/v32-to-v40-carry-forward-change-matrix.md`

The gap register should cover:

- evidence/provenance grading
- independent verification
- reconciliation
- memory admission
- graph-native relationships
- CCDP-compatible evidence semantics
- skill packaging
- schema validation
- semantic QA
- extraction run traceability

The carry-forward/change matrix should distinguish:

- `carry forward`
- `minor cleanup`
- `architectural change`
- `operator decision`
- `defer`

## Ledger Discipline

Work against `ledger.md`. Update each row with attested evidence as you produce
artifacts. At close, write `closing-report.md` with a row-by-row ledger walk
and a bubble-up section for Arc02.

Do not create the v4.0 conceptual model. Do not decide the final skill layout.
Do not edit source files.

## Verification Hints

Useful commands from the slice directory:

```sh
test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|v40-gap-register.md|v32-to-v40-carry-forward-change-matrix.md" slice-plan.md cc-prompt.md
test -f artifacts/v40-gap-register.md && test -f artifacts/v32-to-v40-carry-forward-change-matrix.md
rg -n "evidence/provenance grading|independent verification|reconciliation|memory admission|graph-native relationships|CCDP-compatible evidence semantics|skill packaging|schema validation|semantic QA|extraction run traceability" artifacts/v40-gap-register.md
rg -n "carry forward|minor cleanup|architectural change|operator decision|defer|v3.2 baseline|v4.0" artifacts/v32-to-v40-carry-forward-change-matrix.md
rg -n "v32-source-inventory.md|v32-method-structure-map.md|v32-original-assessment.md|0009|0010|source anchor|source-backed" artifacts/v40-gap-register.md artifacts/v32-to-v40-carry-forward-change-matrix.md
rg -n "does not design|Out of scope|Arc03|conceptual model|Arc04|final skill layout|without designing" slice-plan.md artifacts/v40-gap-register.md artifacts/v32-to-v40-carry-forward-change-matrix.md
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```
