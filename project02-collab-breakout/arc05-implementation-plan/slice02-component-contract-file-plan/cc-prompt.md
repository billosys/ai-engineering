# CC Prompt: Arc05 Slice02 Component Contract And File Plan

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Project:

`project02-collab-breakout`

Slice:

`arc05-implementation-plan/slice02-component-contract-file-plan`

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
- `../slice01-implementation-surface-map/cdc-verification.md`
- `../slice01-implementation-surface-map/artifacts/implementation-surface-inventory.md`
- `../slice01-implementation-surface-map/artifacts/accepted-component-source-map.md`
- `../slice01-implementation-surface-map/artifacts/release-validation-surface-map.md`
- `../slice01-implementation-surface-map/artifacts/cross-cutting-concern-map.md`
- `../slice01-implementation-surface-map/artifacts/slice02-component-file-plan-inputs.md`
- `../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md`
- `../../../project01-harmonise-paths/closing-report.md`

Inspect the source checkout read-only as needed:

- `/Users/oubiwann/lab/billosys/ai-engineering/README.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/`
- `/Users/oubiwann/lab/billosys/ai-engineering/templates/`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`

## Required Artifacts

Create:

- `artifacts/component-contract-matrix.md`
- `artifacts/component-file-layout-plan.md`
- `artifacts/source-to-component-migration-plan.md`
- `artifacts/package-source-contract-register.md`
- `artifacts/support-adapter-dependency-plan.md`
- `artifacts/slice03-package-readme-validation-inputs.md`

## Output Rules

- Preserve the accepted eight-component map exactly:
  `collaboration-framework`, `engineering-methods`, `project-management`,
  `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and
  `contribution-style`.
- Use `operator-accepted-architecture.md` as the authoritative naming source.
- Treat `engineering-methods` as the owner of source/package/release gates,
  while every component carries its own package/source contract.
- Treat component versioning as `SKILL.md` version plus sibling
  `version-history.md`.
- Place ontology/component-boundary critique at
  `engineering-methods/guides/05-component-boundary-analysis.md`.
- Treat `agent-coordination` as owner of CC/CDC/operator terminology,
  delegation decisions, context-packet discipline, and result integration.
- Preserve support assets, adapters, dependency edges, deferred memory
  admission, and CCDP separation as first-class dispositions.
- Do not finalize README, Makefile, generated zip, package-path exception, or
  validation sequencing beyond component-level contract inputs. Slice03 owns
  the release-surface plan.
- Do not edit source files.

## Close

When done, update the slice ledger with attested evidence, write
`closing-report.md`, and leave the slice proposed-done for CDC verification.
