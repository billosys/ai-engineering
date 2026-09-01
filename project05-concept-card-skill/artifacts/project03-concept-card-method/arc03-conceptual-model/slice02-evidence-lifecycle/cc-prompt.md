# CC Prompt: Slice02 Evidence and Lifecycle Semantics

You are implementing Project03 Arc03 Slice02:
`arc03-conceptual-model/slice02-evidence-lifecycle`.

## Context

Project03 is planning the v4.0 concept-card method. Arc03 owns the conceptual
model only. This slice defines the method semantics for evidence and lifecycle
state so v4.0 does not flatten source support, extractor judgment,
independent verification, reconciliation, and memory admission into one
confidence field.

This is planning work in the `planning` worktree. Do not edit the source
checkout, packaged skills, README, Makefile, generated zips, or implementation
files.

## Required Reading

Read these before writing artifacts:

1. `/Users/oubiwann/.codex/skills/collaboration-framework/SKILL.md`
2. `/Users/oubiwann/lab/billosys/ai-engineering/docs/PROJECT-MANAGEMENT.md`
3. `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/01-scales-of-work.md`
4. `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/02-canonical-planning-worktree.md`
5. `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/03-planning-top-down.md`
6. `/Users/oubiwann/lab/billosys/ai-engineering/templates/LEDGER-DISCIPLINE.md`
7. `../../project-plan.md`
8. `../../ledger.md`
9. `../arc-plan.md`
10. `../ledger.md`
11. `../slice01-construct-boundaries/cdc-verification.md`
12. `../slice01-construct-boundaries/artifacts/v40-construct-boundary-model.md`
13. `../slice01-construct-boundaries/artifacts/v40-construct-decision-register.md`
14. `../../arc02-method-inventory/closing-report.md`
15. `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc02-synthesis.md`
16. `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md`
17. `slice-plan.md`
18. `ledger.md`

## Assignment

Produce the two required artifacts under `artifacts/`:

- `artifacts/v40-evidence-lifecycle-model.md`
- `artifacts/v40-evidence-state-decision-register.md`

The lifecycle model must:

- Distinguish extraction confidence, source support, evidence grade,
  verification state, verification result, reconciliation state,
  reconciliation result, and memory admission.
- Explain what each concern means, what it must not be confused with, and what
  object or relationship it attaches to.
- Describe the candidate lifecycle flow from extracted content to durable
  semantic memory candidate.
- Preserve v3.2 carry-forward strengths while naming the v4.0 distinctions
  needed for evidence-graded, provenance-bearing memory consolidation.

The decision register must:

- Record each evidence/lifecycle construct or state family.
- Include status, rationale, dependencies, open question, attachment point, and
  downstream route.
- Mark decisions as accepted, provisional, deferred, or out of scope without
  pretending later Arc03/Arc04/Arc05 work has already happened.

## Scope Fences

Do not finalize schema syntax, exact enum spelling, YAML template shape,
validator implementation, skill architecture, package behavior, README
integration, Makefile changes, generated zips, or source edits.

Do not design graph-native relationship or edge semantics, competency-question
semantics, extraction-run trace schema, reconciliation algorithms, GraphRAG
runtime, memory runtime, ontology database, or CCDP service design. You may
reserve attachment points or downstream dependencies where the evidence
lifecycle needs them.

Do not create `cdc-verification.md`; that is CDC's independent verification
artifact after your close.

## Ledger Instructions

Work against `ledger.md`. Update each row with status and attested evidence as
you satisfy it. If a row cannot be satisfied, mark it deferred with a concrete
reason and re-entry condition.

When complete, write `closing-report.md` with:

- per-row ledger walk,
- artifact inventory,
- silent-drop check against this prompt and `slice-plan.md`,
- bubble-up findings for Arc03,
- What Worked,
- closure line naming the commit/status if available.

## Verification

Run the ledger checks from this slice directory, then run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

Also confirm that new or modified Slice02 files are ASCII-clean.
