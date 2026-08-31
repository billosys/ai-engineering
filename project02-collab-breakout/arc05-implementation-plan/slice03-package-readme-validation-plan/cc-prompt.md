# CC Prompt: Arc05 Slice03 Package, README, And Validation Plan

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Project:

`project02-collab-breakout`

Slice:

`arc05-implementation-plan/slice03-package-readme-validation-plan`

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
- `../slice01-implementation-surface-map/artifacts/release-validation-surface-map.md`
- `../slice02-component-contract-file-plan/cdc-verification.md`
- `../slice02-component-contract-file-plan/artifacts/component-contract-matrix.md`
- `../slice02-component-contract-file-plan/artifacts/component-file-layout-plan.md`
- `../slice02-component-contract-file-plan/artifacts/package-source-contract-register.md`
- `../slice02-component-contract-file-plan/artifacts/source-to-component-migration-plan.md`
- `../slice02-component-contract-file-plan/artifacts/support-adapter-dependency-plan.md`
- `../slice02-component-contract-file-plan/artifacts/slice03-package-readme-validation-inputs.md`
- `../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md`
- `../../../project01-harmonise-paths/closing-report.md`

Inspect the source checkout read-only as needed:

- `/Users/oubiwann/lab/billosys/ai-engineering/README.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-skill-description.sh`

## Required Artifacts

Create:

- `artifacts/package-target-plan.md`
- `artifacts/readme-wayfinding-plan.md`
- `artifacts/skill-entrypoint-validation-plan.md`
- `artifacts/package-path-link-exception-plan.md`
- `artifacts/migration-compatibility-plan.md`
- `artifacts/slice04-implementation-sequence-inputs.md`

## Output Rules

- Preserve the accepted eight-component map exactly:
  `collaboration-framework`, `engineering-methods`, `project-management`,
  `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and
  `contribution-style`.
- Preserve the daily-driver `collaboration-framework` composer while making
  standalone component use clear and useful.
- Distinguish source checkout, generated zip, unzipped/install, and installed
  skill reader modes.
- Treat `engineering-methods` as the shared source/package/release gate owner,
  while preserving per-component package/source contracts.
- Preserve `agent-coordination` ownership of role/delegation/context-packet/
  result-integration language.
- Preserve component versioning as `SKILL.md` version plus sibling
  `version-history.md`.
- Prefer package-local link repairs over package-path exceptions; add
  exception recommendations only with explicit rationale.
- Preserve CCDP separation and do not treat `ccdp.zip` or `protocols/ccdp/`
  as collaboration-framework component payload.
- Do not edit source files or generated zip artifacts.
- Do not close Arc05; Slice04 owns final implementation sequence synthesis.

## Expedited Commit Rule

When the slice is proposed-done, commit only the Slice03 close packet with an
explicit file list. Include the required assistant commit trailers:

- `Co-authored-by: Codex <noreply@openai.com>`
- `Co-authored-by: Billo AI <ai-engineering@billo.systems>`

## Close

When done, update the slice ledger with attested evidence, write
`closing-report.md`, commit only the Slice03 packet, and leave the slice
proposed-done for CDC verification.
