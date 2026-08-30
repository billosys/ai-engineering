# Slice 01: Source Inventory

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice01-source-inventory
status: verified-closed
proposed-done-on: 2026-08-29
verified-closed-on: 2026-08-29
artifact-home: artifacts/
depends-on:
  - project01-harmonise-paths:closed-and-completely-verified
blocks:
  - slice02-problem-solution-map
```

## Goal

Create the source-backed inventory that later Project 02 analysis can trust.
This slice identifies the current collaboration-framework sources, records
what each source contributes, maps major concepts and operational disciplines
to source locations, and captures Project 01 path/package implications that
must constrain any future breakout.

## Execution Gate

Do not execute this slice until `project01-harmonise-paths` is closed and
completely verified. Planning artifacts may exist before then; analysis work
must wait so it can consume Project 01's accepted source/package path contract.

## In Scope

- Inspect the current source checkout at
  `/Users/oubiwann/lab/billosys/ai-engineering`.
- Inventory the framework entry points and source documents:
  - `README.md`
  - `SKILL.md`
  - `docs/AI-CONSTITUTION-SUPPLEMENT.md`
  - `docs/AI-ENGINEERING-METHODOLOGY.md`
  - `docs/PROJECT-MANAGEMENT.md`
  - `docs/pm/*.md`
  - `templates/LEDGER-DISCIPLINE.md`
  - `docs/CODE-AUDIT.md`
  - `docs/CLAUDE-CODE-COVERAGE.md`
  - `docs/SUBAGENT-DELEGATION-POLICY.md`
  - `docs/CONTRIBUTION-STYLE.md`
  - `templates/CONTRIBUTION-TICKET.md`
- Record each source's current role, major sections, load moments, standalone
  usefulness, dependencies, and packaging/path assumptions.
- Produce `artifacts/framework-source-inventory.md`.
- Produce `artifacts/source-to-concept-map.md`.
- Produce `artifacts/project01-path-contract-notes.md` after Project 01
  closes.

## Out of Scope

- Editing source files or packaged skill contents.
- Deciding final component boundaries.
- Creating new SKILL.md files.
- Planning implementation slices beyond noting evidence needed by later arcs.
- Rewriting or copyediting source prose.

## Verification Approach

CDC verifies the slice by checking that the produced analysis artifacts cite
actual source paths and cover the required source set. The verification should
use `rg`/`find` over both the source checkout and this slice directory.

## Exit Criteria

- The Project 01 completion gate is explicitly checked before execution.
- Every required source document is represented in the inventory.
- Every inventory entry records role, load moment, standalone usefulness,
  dependencies, and path/package notes.
- The source-to-concept map includes current concepts/disciplines and candidate
  breakout labels without treating them as final.
- Project 01 path/package findings are summarized as constraints for Project 02.
- Open questions are carried forward for Slice 02 and Arc 02.

## Planned Outputs

- `artifacts/framework-source-inventory.md`
- `artifacts/source-to-concept-map.md`
- `artifacts/project01-path-contract-notes.md`
- Slice close set, when executed: `closing-report.md` and
  `cdc-verification.md`
