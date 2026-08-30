# CC Prompt: Slice 01 Boundary Analysis Instrument

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project02-collab-breakout/arc02-conceptual-analysis/slice01-boundary-analysis-instrument`

This is a planning/analysis slice. Do not edit source files in
`/Users/oubiwann/lab/billosys/ai-engineering`.

## Required Reading

Read these files before writing artifacts:

1. `../../project-plan.md`
2. `../../ledger.md`
3. `../arc-plan.md`
4. `../ledger.md`
5. `slice-plan.md`
6. `ledger.md`
7. `../../arc01-framework-inventory/closing-report.md`
8. `../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md`
9. `../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md`
10. `../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md`
11. `../../../project03-concept-card-method/arc01-method-positioning/slice01-project02-boundary-aid/artifacts/project02-conceptual-boundary-aid.md`
12. `../../../project03-concept-card-method/arc01-method-positioning/slice02-project02-acceptance-handoff/artifacts/project02-arc02-acceptance-handoff.md`
13. `/Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md`
14. `/Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`

Treat Project03 files as input artifacts only. Do not close, verify, or update
Project03 controls as part of this slice.
Treat the v3.2 workbench docs as read-only provenance for the Project03
concept-card lens, not as Project02 control gates.

## Task

Create Arc02's conceptual-analysis instrument and seeded
component-boundary ledger.

Produce these artifacts under `artifacts/`:

- `conceptual-analysis-method.md`
- `component-boundary-ledger.md`
- `arc02-input-evidence-register.md`

The method should merge the Project02 Arc01 evidence base with the Project03
concept-card boundary lens. It should define how Arc02 will distinguish:

- concept;
- candidate component;
- component family member;
- support asset;
- adapter;
- dependency edge;
- constraint;
- template;
- package/release gate;
- non-component concept.

Use the Project03 axes explicitly: reason to load, problem ownership,
competency questions, relationship type, evidence grade, and memory admission.
Use the v3.2 source docs to preserve the original method ideas of one concept
per card, source-faithful extraction, explicit relationships, confidence,
provenance, competency questions, and preservation during re-extraction. Carry
Project01 path/package constraints as cross-cutting gates. Keep all
classifications analytical and non-final.

The seeded `component-boundary-ledger.md` should include one row for each of
the 26 Arc01 candidate labels from
`../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md`.
Do not complete the full evaluation; create the consistent row schema and seed
the rows so Slice02 can evaluate them.

## Verification Commands

Run these before proposing the slice done:

```sh
test -f ../../arc01-framework-inventory/closing-report.md
test -f ../../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md
test -f ../../../project03-concept-card-method/arc01-method-positioning/slice01-project02-boundary-aid/artifacts/project02-conceptual-boundary-aid.md
test -f ../../../project03-concept-card-method/arc01-method-positioning/slice02-project02-acceptance-handoff/artifacts/project02-arc02-acceptance-handoff.md
test -f /Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md
test -f /Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
rg -n "Arc01|Project03|concept-card|acceptance handoff|candidate-component-inputs|v3.2 source baseline|0009-howto|0010-a-guide" artifacts/conceptual-analysis-method.md artifacts/arc02-input-evidence-register.md
rg -n "classification vocabulary|reason to load|problem ownership|competency question|relationship type|evidence grade|memory admission|one concept|source-faithful|explicit relationship|confidence|provenance|preservation|non-final" artifacts/conceptual-analysis-method.md
rg -n "repository-orientation-and-distribution|protocol-distribution-guidance|framework-entrypoint-and-routing|agent-adapter-and-routing|collaborative-posture-and-ethics|engineering-methodology-and-process|verification-methodology|project-management-wayfinder|project-management-scale-model|planning-worktree-and-layout|planning-open-set-mechanics|slice-close-and-bubble-up|arc-project-composition-close|planning-confirmation-protocol|planning-anti-patterns-and-repair|framework-maintenance-discipline|project-management-examples|project-management-provenance|ledger-verification-protocol|code-audit-discipline|evidence-backed-modernization|coverage-hardening-discipline|delegation-policy|contribution-style-and-voice|contribution-ticket-template|path-contract-constraints" artifacts/component-boundary-ledger.md
test "$(rg -c '^\| `[^`]+` \|' artifacts/component-boundary-ledger.md)" -eq 26
rg -n "Project03|operator-accepted input|input-only|not a control gate|does not gate Project02|boundary aid|acceptance handoff" artifacts/arc02-input-evidence-register.md
rg -n "Project01|project01-harmonise-paths|source/package|package-local|zip|release surface|make check-package-paths|cross-cutting constraint|package/release gate" artifacts/conceptual-analysis-method.md artifacts/component-boundary-ledger.md artifacts/arc02-input-evidence-register.md
rg -n "non-final|not final|not accepted architecture|does not decide|analytical|operator acceptance|Arc04" artifacts/conceptual-analysis-method.md artifacts/component-boundary-ledger.md artifacts/arc02-input-evidence-register.md
test -f artifacts/conceptual-analysis-method.md
test -f artifacts/component-boundary-ledger.md
test -f artifacts/arc02-input-evidence-register.md
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

## Close Requirements

When done:

- Update this slice ledger with CC-attested evidence.
- Write `closing-report.md` with a row-by-row ledger walk.
- Include a bubble-up to Arc02:
  - whether Slice02 can start from the seeded ledger;
  - any method questions that should change Arc02 plan or ledger rows;
  - silent-drop diff against this prompt and `slice-plan.md`.
- Do not write `cdc-verification.md`; CDC writes it during independent review.
