# CC Prompt: Slice 01 Source Surface and Implementation Input Inventory

You are CC working in the ai-engineering repository. Complete Project03
Arc05 Slice01:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project03-concept-card-method/arc05-implementation-plan/slice01-source-surface-inventory/`

## Required Context

Read these files before editing:

- `slice-plan.md`
- `ledger.md`
- `../arc-plan.md`
- `../ledger.md`
- `../../project-plan.md`
- `../../ledger.md`
- `../../arc04-skill-architecture/closing-report.md`
- `../../arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md`
- `../../arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-architecture-decision-register.md`
- `../../arc04-skill-architecture/slice05-architecture-synthesis/artifacts/arc05-implementation-planning-handoff.md`

Inspect the live source checkout at:

`/Users/oubiwann/lab/billosys/ai-engineering`

Useful source surfaces to inspect include:

- `knowledge/`
- `README.md`
- `Makefile`
- `package-path-exceptions.tsv`
- `AGENTS.md`
- `CLAUDE.md`
- `workbench/`
- ignored/generated-output conventions such as `build/` and generated zips

## Task

Produce two durable artifacts under `artifacts/`:

- `artifacts/source-surface-inventory.md`
- `artifacts/implementation-input-question-map.md`

The source-surface inventory should map current source facts that Arc05 must
plan against: existing knowledge-skill layout patterns, source paths, README
and library/discoverability surfaces, Makefile/package targets, package-path
exceptions, generated artifact conventions, ignored output conventions, and
version-history expectations.

The implementation-input question map should route open implementation
questions to later slices:

- Slice02: source layout, content sequence, guide files, template files,
  example files, cross-links, and source-edit sequencing.
- Slice03: schema syntax, enum spelling, source support/source span identity,
  validation candidates, validator-code scope, tests, and semantic or human
  review boundaries.
- Slice04: README/library discoverability, Makefile targets, package-list
  changes, package-path checks, generated zips, release gates, package updates,
  and version-history obligations.
- Slice05: implementation-plan synthesis, implementation-slice
  recommendations, deferral register, and Project03 close input.

Preserve accepted Arc04 decisions as inputs. Do not reopen the architecture.

## Scope Fences

Do not edit source checkout files.

Do not decide final source layout, exact filenames, schema syntax, enum
spelling, validator-code implementation language, Makefile target names,
package-list changes, README/library prose, release gates, generated-zip
policy, or implementation slice sequence.

Do not create generated zips, released bundles, validator implementations,
runtime services, GraphRAG, graph database, ontology database, memory runtime,
CCDP service, or live extraction behavior.

## Required Ledger Work

Work against `ledger.md`. When the artifacts are complete:

1. Run or reproduce each Verify command in the ledger.
2. Update every ledger row to `done`, `deferred`, or `no-op`.
3. Fill Evidence and Notes for every row.
4. Write `closing-report.md` with a row-by-row disposition for F-1 through
   F-10.
5. Include a bubble-up section stating whether Slice01 found any need for
   Arc05 re-sequencing, a new slice, or scope correction.
6. Include the closure count:
   `Rows: 10. Done: <n>. Deferred: <n>. No-op: <n>.`

Do not create `cdc-verification.md`. CDC writes that after independent
verification.

## Required Verification Before Reporting Done

From the Slice01 directory, run the ledger checks. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
LC_ALL=C grep -RIn '[^ -~]' slice-plan.md ledger.md cc-prompt.md artifacts closing-report.md
grep -RIn '[[:blank:]]$' slice-plan.md ledger.md cc-prompt.md artifacts closing-report.md
```

The last two commands should print no matches.

## Report Format

Report:

- Files created or updated.
- Whether every ledger row F-1 through F-10 passed.
- Whether source checkout stayed clean.
- Whether planning diff check and Markdown hygiene passed.
- Any deferred/no-op rows with reasons and re-entry conditions.

Leave changes unstaged unless the operator tells you otherwise.
