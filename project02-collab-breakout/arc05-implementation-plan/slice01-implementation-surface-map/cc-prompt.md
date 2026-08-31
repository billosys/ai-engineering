# CC Prompt: Arc05 Slice01 Implementation Surface Map

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Project:

`project02-collab-breakout`

Slice:

`arc05-implementation-plan/slice01-implementation-surface-map`

## Assignment

Follow `slice-plan.md` and `ledger.md`. Produce the required artifacts under
the slice-local `artifacts/` directory.

This is a planning-only slice. Do not edit source files in
`/Users/oubiwann/lab/billosys/ai-engineering`.

## Required Inputs

Read:

- `../../project-plan.md`
- `../../ledger.md`
- `../arc-plan.md`
- `../ledger.md`
- `slice-plan.md`
- `ledger.md`
- `../../arc04-breakout-architecture/closing-report.md`
- `../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md`
- `../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/arc05-implementation-inputs.md`
- `../../../project01-harmonise-paths/closing-report.md`

Inspect the source checkout read-only:

- `/Users/oubiwann/lab/billosys/ai-engineering/README.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/`
- `/Users/oubiwann/lab/billosys/ai-engineering/templates/`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`

## Required Artifacts

Create:

- `artifacts/implementation-surface-inventory.md`
- `artifacts/accepted-component-source-map.md`
- `artifacts/release-validation-surface-map.md`
- `artifacts/cross-cutting-concern-map.md`
- `artifacts/slice02-component-file-plan-inputs.md`

## Output Rules

- Preserve the accepted eight-component map exactly:
  `collaboration-framework`, `engineering-methods`, `project-management`,
  `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and
  `contribution-style`.
- Treat source/package/release gates as owned by `engineering-methods` and as
  mandatory per-component contract fields.
- Treat component versioning as `SKILL.md` version plus sibling
  `version-history.md`.
- Treat ontology critique as
  `engineering-methods/guides/05-component-boundary-analysis.md`.
- Treat memory admission as deferred future research.
- Preserve CCDP separation.
- Do not finalize source edits or package paths beyond accepted component root
  names and planning assumptions.
- Do not edit source files.

## Close

When done, update the slice ledger with attested evidence, write
`closing-report.md`, and leave the slice proposed-done for CDC verification.
