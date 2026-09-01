# CC Prompt: Slice 02 Project02 Acceptance Handoff

You are working in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc01-method-positioning/slice02-project02-acceptance-handoff`

This is Project03 Arc01 Slice02. The slice is planning/analysis work only. Do
not edit source files in `/Users/oubiwann/lab/billosys/ai-engineering`.

## Required Reading

Before writing artifacts, read:

1. `/Users/oubiwann/.codex/skills/collaboration-framework/SKILL.md`
2. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/PROJECT-MANAGEMENT.md`
3. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/01-scales-of-work.md`
4. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/02-canonical-planning-worktree.md`
5. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/03-planning-top-down.md`
6. `/Users/oubiwann/.codex/skills/collaboration-framework/templates/LEDGER-DISCIPLINE.md`
7. `../../project-plan.md`
8. `../arc-plan.md`
9. `../ledger.md`
10. `slice-plan.md`
11. `ledger.md`
12. `../slice01-project02-boundary-aid/artifacts/project02-conceptual-boundary-aid.md`
13. `../slice01-project02-boundary-aid/closing-report.md`
14. `../slice01-project02-boundary-aid/cdc-verification.md`
15. `../../../project02-collab-breakout/project-plan.md`
16. `../../../project02-collab-breakout/arc02-conceptual-analysis/arc-plan.md`

## Assignment

Produce the Project02 Arc02 acceptance handoff for the Slice01 boundary aid.

The handoff should let the operator decide whether Project02 Arc02 can proceed
with the current aid, needs a small adjustment, or should remain deferred. Keep
the framing narrow: Project02 does not need the full Project03 v4.0
concept-card skill before Arc02; it needs a focused boundary-analysis aid, an
acceptance decision, and a clear usage contract.

## Required Outputs

Create:

- `artifacts/project02-arc02-acceptance-handoff.md`

The artifact should include:

- a one-paragraph readiness verdict;
- what Project02 Arc02 may use from the Slice01 boundary aid;
- what Project02 Arc02 must not treat as decided;
- go / adjust / defer criteria for operator acceptance;
- how this handoff supports Project03 Arc01 formal close;
- any open questions for the operator.

## Ledger Discipline

Work against `ledger.md`. Update each row with attested evidence as you
produce artifacts. At close, write `closing-report.md` with a row-by-row ledger
walk and a bubble-up section for Arc01.

Do not create final Project02 architecture decisions. Do not create the final
Project03 v4.0 concept-card extraction skill. Do not close Arc01; this slice
prepares the evidence that the later arc close will consume.

## Verification Hints

Useful commands from the slice directory:

```sh
test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|project02-arc02-acceptance-handoff.md" slice-plan.md cc-prompt.md
test -f artifacts/project02-arc02-acceptance-handoff.md
rg -n "Project02 Arc02|Slice01 boundary aid|v3.2 baseline|v4.0|operator acceptance" artifacts/project02-arc02-acceptance-handoff.md
rg -n "go / adjust / defer|Go|Adjust|Defer|non-final|does not decide|component boundaries" artifacts/project02-arc02-acceptance-handoff.md
rg -n "slice02-project02-acceptance-handoff|full Project03 v4.0 skill|soft dependency" ../../../project02-collab-breakout/project-plan.md ../../../project02-collab-breakout/arc02-conceptual-analysis/arc-plan.md
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```
