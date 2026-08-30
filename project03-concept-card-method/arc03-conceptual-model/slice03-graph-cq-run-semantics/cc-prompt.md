# CC Prompt: Slice03 Relationship, CQ, and Run Semantics

You are implementing Project03 Arc03 Slice03:
`arc03-conceptual-model/slice03-graph-cq-run-semantics`.

## Context

Project03 is planning the v4.0 concept-card method. Arc03 owns the conceptual
model only. Slice01 established construct boundaries. Slice02 separated the
evidence and lifecycle layer, reserving attachment points for reconciliation
state/result, relationship/edge, competency-question, and extraction-run
semantics. This slice now defines those graph/CQ/run semantics so Slice04 can
synthesize the accepted v4.0 conceptual model.

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
14. `../slice02-evidence-lifecycle/cdc-verification.md`
15. `../slice02-evidence-lifecycle/artifacts/v40-evidence-lifecycle-model.md`
16. `../slice02-evidence-lifecycle/artifacts/v40-evidence-state-decision-register.md`
17. `../../arc02-method-inventory/closing-report.md`
18. `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc02-synthesis.md`
19. `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md`
20. `slice-plan.md`
21. `ledger.md`

## Assignment

Produce the two required artifacts under `artifacts/`:

- `artifacts/v40-graph-cq-run-semantics.md`
- `artifacts/v40-reconciliation-traceability-decision-register.md`

The graph/CQ/run model must:

- Define relationship/edge semantics for v4.0 while preserving the value of
  v3.2 `prerequisites`, `extends`, `related`, and `contrasts_with`.
- Explain endpoints, direction, inverse/symmetry expectations, graph closure,
  and when a relationship needs first-class edge identity.
- Define competency-question semantics, including requirement, answerability,
  coverage, verification, retrieval, obsolete, and deferred roles or statuses.
- Define extraction-run traceability: source snapshot, method or prompt
  version, agent scope, generated/updated card set, old-card inputs,
  preservation decisions, validation result, reconciliation result, and
  parallel-worker provenance.
- Define reconciliation semantics across cards, claims, relationships/edges,
  CQs, and extraction runs, including conflict classes and result-record
  attachment points.

The decision register must:

- Record each graph, CQ, run, and reconciliation construct or state family.
- Include status, rationale, dependencies, open question, attachment point,
  and downstream route.
- Mark decisions as accepted, provisional, deferred, or out of scope without
  pretending Slice04, Arc04, or Arc05 work has already happened.

## Scope Fences

Do not finalize schema syntax, exact enum spelling, YAML template shape,
validator implementation, skill architecture, package behavior, README
integration, Makefile changes, generated zips, or source edits.

Do not design reconciliation algorithms, graph database implementation, graph
indexes, GraphRAG runtime, memory runtime, ontology database, CCDP service
design, or package/runtime execution behavior. You may define conceptual
conflict classes, attachment points, lifecycle dependencies, and downstream
routes.

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

Also confirm that new or modified Slice03 files are ASCII-clean.
