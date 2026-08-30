# CC Prompt: Slice 02 Problem-Solution Map

You are working in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project02-collab-breakout/arc01-framework-inventory/slice02-problem-solution-map`

This is Project02 Arc01 Slice02. The slice is planning/analysis work only. Do
not edit source files in `/Users/oubiwann/lab/billosys/ai-engineering`; inspect
them read-only if needed.

## Required Reading

Before writing artifacts, read:

1. `/Users/oubiwann/.agents/skills/collaboration-framework/SKILL.md`
2. `/Users/oubiwann/.agents/skills/collaboration-framework/docs/PROJECT-MANAGEMENT.md`
3. `/Users/oubiwann/.agents/skills/collaboration-framework/docs/pm/01-scales-of-work.md`
4. `/Users/oubiwann/.agents/skills/collaboration-framework/docs/pm/02-canonical-planning-worktree.md`
5. `/Users/oubiwann/.agents/skills/collaboration-framework/docs/pm/03-planning-top-down.md`
6. `/Users/oubiwann/.agents/skills/collaboration-framework/templates/LEDGER-DISCIPLINE.md`
7. `../../project-plan.md` via the project root:
   `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project02-collab-breakout/project-plan.md`
8. `../arc-plan.md`
9. `../ledger.md`
10. `../slice01-source-inventory/cdc-verification.md`
11. `../slice01-source-inventory/artifacts/framework-source-inventory.md`
12. `../slice01-source-inventory/artifacts/source-to-concept-map.md`
13. `../slice01-source-inventory/artifacts/project01-path-contract-notes.md`
14. `slice-plan.md`
15. `ledger.md`

## Assignment

Convert the verified Slice 01 inventory into a source-backed
problem-to-solution map.

For each major problem or failure mode the collaboration framework appears to
address, map:

- the problem class;
- the historical or functional symptom;
- the current framework mechanism(s);
- source evidence for the mechanism;
- candidate breakout labels involved, explicitly non-final;
- fit assessment: strong fit, partial fit, overfit, underfit, duplicated,
  mislabel candidate, improper merge candidate, improper split candidate, or
  missing solution;
- the next question or disposition needed by Slice 03, Arc 02, or the operator.

Use the Slice 01 artifacts as the evidence base. You may inspect current source
files read-only to clarify a mechanism, but do not edit source files.

## Required Outputs

Create these files under `artifacts/`:

- `artifacts/problem-solution-map.md`
- `artifacts/mechanism-coverage-matrix.md`
- `artifacts/problem-solution-findings.md`

Keep the artifacts analytical, not architectural. The goal is to prepare later
conceptual and functional analysis, not to select final components.

## Ledger Discipline

Work against `ledger.md`. Update each row with attested evidence as you produce
the artifacts. At close, write `closing-report.md` with a row-by-row ledger
walk and a bubble-up section for Arc 01.

Do not create `cdc-verification.md`; that is for the independent verification
pass.

## Verification Hints

Useful commands from the slice directory:

```sh
rg -n "Problem class|Current mechanism|Source evidence|Fit assessment|Question|Disposition" artifacts/problem-solution-map.md
rg -n "repository-orientation-and-distribution|ledger-verification-protocol|coverage-hardening-discipline|path-contract-constraints" artifacts/mechanism-coverage-matrix.md
rg -n "overlap|duplication|underfit|overfit|mislabel|improper merge|improper split|missing solution" artifacts/problem-solution-findings.md
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --cached --check
```

The source checkout should remain clean because this slice is planning-only.
