# CC Prompt: Slice 01 v3.2 Source Inventory

You are working in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc02-method-inventory/slice01-v32-source-inventory`

This is Project03 Arc02 Slice01. The slice is planning/analysis work only. Do
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
13. `artifacts/source-docs/0009-howto-concept-card-extraction-with-llms-v3.2.md`
14. `artifacts/source-docs/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`
15. `artifacts/v32-original-assessment.md`
16. `/Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md`
17. `/Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`

## Assignment

Produce a source-backed inventory of the v3.2 concept-card method.

The goal is to map what the baseline method actually says before later slices
compare it to the v4.0 target. Keep the work descriptive and source-grounded.
Do not design the v4.0 replacement in this slice.

The two preserved source snapshots under `artifacts/source-docs/` and the
preserved prior assessment memo under `artifacts/v32-original-assessment.md`
are baseline artifacts for this slice. Verify the source snapshots still match
the workbench inputs before closing the slice. Treat the prior assessment as
context for later gap analysis, not as a substitute for reading and inventorying
the source docs.

## Required Outputs

Create:

- `artifacts/v32-source-inventory.md`
- `artifacts/v32-method-structure-map.md`

Preserve:

- `artifacts/source-docs/0009-howto-concept-card-extraction-with-llms-v3.2.md`
- `artifacts/source-docs/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`
- `artifacts/v32-original-assessment.md`

The source inventory should cover both v3.2 docs and record each document's
purpose, structure, schema, workflow phases, validation checks, provenance
rules, relationship model, competency-question handling, confidence semantics,
re-extraction mechanics, preservation checks, and notable limitations.

The structure map should organize the method constructs across both docs and
mark later `v4.0 question` prompts without answering them prematurely.

## Ledger Discipline

Work against `ledger.md`. Update each row with attested evidence as you produce
artifacts. At close, write `closing-report.md` with a row-by-row ledger walk and
a bubble-up section for Arc02.

Do not create the v4.0 conceptual model. Do not decide the final skill layout.
Do not edit source files.

## Verification Hints

Useful commands from the slice directory:

```sh
test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && rg -n "artifact-home: artifacts/|Required Artifacts|v32-source-inventory.md|v32-method-structure-map.md|v32-original-assessment.md|source-docs" slice-plan.md cc-prompt.md
cmp -s /Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md artifacts/source-docs/0009-howto-concept-card-extraction-with-llms-v3.2.md && cmp -s /Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md artifacts/source-docs/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md && rg -n "Preserved Assessment|v3.2 is genuinely good|target to v4.0" artifacts/v32-original-assessment.md
test -f artifacts/v32-source-inventory.md && test -f artifacts/v32-method-structure-map.md
rg -n "0009-howto|0010-a-guide|schema|workflow|validation|provenance|relationship|competency question|confidence|re-extraction|preservation" artifacts/v32-source-inventory.md
rg -n "v3.2 baseline|v4.0 question|schema|workflow|validation|provenance|relationship|competency question|confidence|re-extraction|memory admission|CCDP" artifacts/v32-method-structure-map.md
rg -n "not design|without answering them prematurely|Out of scope|Designing the v4.0 conceptual model" slice-plan.md artifacts/v32-method-structure-map.md
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```
