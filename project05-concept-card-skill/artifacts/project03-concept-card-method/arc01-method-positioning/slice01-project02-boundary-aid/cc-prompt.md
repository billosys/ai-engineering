# CC Prompt: Slice 01 Project02 Boundary Aid

You are working in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc01-method-positioning/slice01-project02-boundary-aid`

This is Project03 Arc01 Slice01. The slice is planning/analysis work only. Do
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
12. `../../../project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md`
13. `../../../project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md`
14. `../../../project02-collab-breakout/arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md`
15. `/Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md`
16. `/Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`

## Assignment

Open Project03 and produce a compact conceptual-boundary aid for Project02
Arc02.

The aid should explain how the concept-card method can sharpen Project02's
component-boundary analysis without deciding Project02's final architecture.
Treat the v3.2 workbench docs as the baseline and the future Project03 method
as v4.0, not v3.3.
It should adapt these lenses:

- concept versus component;
- component versus support asset, adapter, constraint, and template;
- claim versus evidence;
- provenance and evidence grade;
- competency questions as requirements and tests;
- graph relationships and dependency direction;
- memory admission as a stricter step than extraction.

## Required Outputs

Create:

- `artifacts/project02-conceptual-boundary-aid.md`

Update Project02 planning only enough to record the soft dependency before
Arc02 detailed planning. Keep the changes analytical and reversible.

## Ledger Discipline

Work against `ledger.md`. Update each row with attested evidence as you
produce artifacts. At close, write `closing-report.md` with a row-by-row ledger
walk and a bubble-up section for Arc01.

Do not create final Project02 architecture decisions. Do not create the final
v4.0 concept-card extraction skill.

## Verification Hints

Useful commands from the slice directory:

```sh
rg -n "Project02 Arc02|non-final|not decide|component boundary|concept card|v3.2 baseline|v4.0" artifacts/project02-conceptual-boundary-aid.md
rg -n "project03-concept-card-method|Project03|concept-card|boundary aid|soft dependency" ../../../project02-collab-breakout/project-plan.md ../../../project02-collab-breakout/arc02-conceptual-analysis/arc-plan.md
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```
