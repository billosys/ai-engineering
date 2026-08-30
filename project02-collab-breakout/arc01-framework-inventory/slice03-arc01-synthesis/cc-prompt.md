# CC Prompt: Slice 03 Arc 01 Synthesis

You are working in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis`

This is Project02 Arc01 Slice03. The slice is planning/analysis work only. Do
not edit source files in `/Users/oubiwann/lab/billosys/ai-engineering`; inspect
them read-only only if needed to resolve a synthesis inconsistency.

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
10. `../slice01-source-inventory/cdc-verification.md`
11. `../slice01-source-inventory/artifacts/framework-source-inventory.md`
12. `../slice01-source-inventory/artifacts/source-to-concept-map.md`
13. `../slice01-source-inventory/artifacts/project01-path-contract-notes.md`
14. `../slice02-problem-solution-map/cdc-verification.md`
15. `../slice02-problem-solution-map/artifacts/problem-solution-map.md`
16. `../slice02-problem-solution-map/artifacts/mechanism-coverage-matrix.md`
17. `../slice02-problem-solution-map/artifacts/problem-solution-findings.md`
18. `slice-plan.md`
19. `ledger.md`

## Assignment

Synthesize Arc 01 into explicit inputs for Arc 02 conceptual analysis.

Do not choose final component boundaries. Instead, prepare the evidence so Arc
02 can evaluate boundaries with a critical eye. The synthesis must distinguish:

- candidate components;
- support assets;
- dependency edges;
- surface adapters;
- cross-cutting constraints;
- package/release gates;
- naming or mislabel risks;
- improper merge and improper split candidates;
- missing-solution or underfit areas;
- operator questions.

Use verified Slice 01 and Slice 02 artifacts as the evidence base. Current
source files may be inspected read-only when an artifact citation needs
clarification.

## Required Outputs

Create these files under `artifacts/`:

- `artifacts/arc01-synthesis.md`
- `artifacts/candidate-component-inputs.md`
- `artifacts/arc02-question-register.md`

Keep these artifacts analytical and handoff-oriented. They should make Arc 02
easier to plan and discuss; they should not settle the final breakout.

## Ledger Discipline

Work against `ledger.md`. Update each row with attested evidence as you produce
the artifacts. At close, write `closing-report.md` with a row-by-row ledger
walk and a bubble-up section for Arc 01.

The bubble-up must explicitly answer whether Arc 01 is ready for arc close
after this slice or whether a remediation slice is required before Arc 02 can
begin. Do not create `cdc-verification.md`; that is for the independent
verification pass.

## Verification Hints

Useful commands from the slice directory:

```sh
rg -n "Arc 01 established|Undecided|Ready to close|remediation|not final" artifacts/arc01-synthesis.md
rg -n "candidate component|support asset|dependency edge|adapter|constraint|package/release gate" artifacts/candidate-component-inputs.md
rg -n "Owner:|Decision needed:|Why it matters:|Source evidence:|Operator|Arc 02" artifacts/arc02-question-register.md
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --cached --check
```

The source checkout should remain clean because this slice is planning-only.
