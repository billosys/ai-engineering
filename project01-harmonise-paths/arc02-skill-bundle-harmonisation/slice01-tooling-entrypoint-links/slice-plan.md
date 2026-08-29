# Slice 01: Tooling Entrypoint Links

```yaml
project: project01-harmonise-paths
arc: arc02-skill-bundle-harmonisation
slice: slice01-tooling-entrypoint-links
status: open
opened-on: 2026-08-29
opened-by: CDC
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
artifact-home: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/artifacts
```

## Capability Statement

This slice performs the first package-path warning burn-down using low-risk
entrypoint link harmonisation in smaller/simple skill bundles.

The goal is not to clear every package warning. The goal is to prove the Arc
02 pattern on a small set where source and package can share one reference
form: replace source-root guide references with `guides/...` references that
resolve from both the source skill file location and the generated package
root.

## Inputs

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/closing-report.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`
- targeted skill files under `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/`

## Artifact Home

Durable slice-produced evidence belongs here:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/artifacts/`

Expected artifacts include baseline and post-change package gate summaries,
targeted warning inventories, and diff-scope evidence.

## Scope

In scope:

- establish a baseline warning inventory for targeted files/packages;
- edit small/simple skill entrypoints where `guides/...` is valid in both
  source and package contexts;
- update `package-path-exceptions.tsv` to remove or expire resolved
  transitional rows;
- run the package path gate and show targeted warning reduction;
- keep durable evidence in this slice's `artifacts/` directory;
- update the slice ledger and close report.

Targeted files:

- `knowledge/deno/SKILL-js-linter.md`
- `knowledge/biome/SKILL-js-linter.md`
- `knowledge/biome/SKILL-web-linter.md`
- `knowledge/tailwindcss/SKILL.md`
- `knowledge/cobalt/SKILL.md`

Out of scope:

- mature language guide prose edits;
- Rust, Go, C++, Erlang, or JavaScript/Deno language-pack broad
  harmonisation;
- collaboration-framework/project-management bundle changes;
- generalized staging-transform machinery unless a tiny helper is required for
  this slice and justified in the close report;
- package layout expansion;
- CCDP package work;
- URL liveness checks;
- changes to the collaboration-framework planning spec.

## Verification Approach

The close set must show:

- baseline targeted warnings before edits;
- post-change targeted warning count;
- `make check-package-paths` exits 0 with no new hard failures;
- `make check-skills` passes;
- `make all` passes;
- implementation diff scope stays within the target files,
  `package-path-exceptions.tsv`, and any justified helper/Make changes;
- durable artifacts are under this slice's `artifacts/` directory.

## Close Conditions

This slice closes when targeted entrypoint warnings are reduced, all package
and compatibility checks pass, every ledger row has attested evidence, durable
evidence artifacts live under `artifacts/`, and the close report walks every
row with Bubble-up to Arc 02.
