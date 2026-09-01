# CC Prompt: Project04 Arc01 Slice01 Source Surface Inventory

You are CC for Project04, Arc01, Slice01 in the ai-engineering planning
worktree.

## Context

Project04 is reorganizing the repository so `docs/` becomes user-facing
documentation about the repository's materials, while `knowledge/` becomes the
raw and derived knowledge-library substrate. The project also needs to separate
skill kind from skill topology:

- skill kind: what a skill is about, such as domain/tooling,
  framework/operational, method, protocol/support, or another accepted
  category;
- skill topology: whether the skill is atomic or composite.

Rust is the initial candidate atomic skill anchor. `collaboration-framework`
is the accepted composite anchor because Project02 defines it as the
daily-driver composer over specialist components.

## Required Reading

Read these planning files first:

- `project04-knowledge-library-reorg/project-plan.md`
- `project04-knowledge-library-reorg/ledger.md`
- `project04-knowledge-library-reorg/arc01-material-inventory/arc-plan.md`
- `project04-knowledge-library-reorg/arc01-material-inventory/ledger.md`
- `project04-knowledge-library-reorg/arc01-material-inventory/slice01-source-surface-inventory/slice-plan.md`
- `project04-knowledge-library-reorg/arc01-material-inventory/slice01-source-surface-inventory/ledger.md`

Then inspect the source checkout at:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Task

Perform a read-only inventory of the live source checkout. Produce these
durable artifacts in:

`project04-knowledge-library-reorg/arc01-material-inventory/slice01-source-surface-inventory/artifacts/`

Required artifacts:

- `current-source-surface-map.md`
- `material-role-classification.md`
- `source-validation-surface-map.md`

The artifacts must cover:

- top-level source surfaces: `README.md`, `SKILL.md`, `AGENTS.md`,
  `CLAUDE.md`, `docs/`, `knowledge/`, `templates/`, `protocols/`, `Makefile`,
  `package-path-exceptions.tsv`, `scripts/`, `assets/`, `site/`, and
  `workbench/`;
- current `docs/` material roles;
- current `knowledge/` material roles;
- package, validation, link, and compatibility surfaces affected by future
  moves;
- the Project02/Project03 imported project-level artifacts as later Slice02
  inputs, clearly marked as not a substitute for live source inventory;
- only source-backed early observations about atomic/composite skill topology,
  with final topology classification deferred to Slice03.

## Hard Boundaries

- Do not edit the source checkout.
- Do not move, delete, rename, or rewrite source files.
- Do not decide final target homes for files.
- Do not finalize atomic/composite terminology.
- Do not write close artifacts until the inventory artifacts exist.

## Verification

Update the slice ledger with attested evidence for every row. Each `done` row
must point to the artifact and command/grep evidence that satisfies it.

Before handing back, run the ledger Verify commands from the slice directory.
Also run source checkout status:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short
```

Then write `closing-report.md` with a row-by-row ledger walk and a bubble-up to
Arc01. Leave `cdc-verification.md` for CDC.
