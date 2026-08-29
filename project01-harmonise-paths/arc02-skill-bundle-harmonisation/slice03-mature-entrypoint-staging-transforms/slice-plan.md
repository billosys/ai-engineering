# Slice 03: Mature Entrypoint Staging Transforms

```yaml
project: project01-harmonise-paths
arc: arc02-skill-bundle-harmonisation
slice: slice03-mature-entrypoint-staging-transforms
status: open
opened-on: 2026-08-29
opened-by: CDC
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
artifact-home: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/artifacts
depends-on:
  - arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links
```

## Capability Statement

This slice harmonises package-path warnings for mature language skill
entrypoints without restructuring mature guide prose.

The likely winning pattern is a Make/script-friendly package staging transform:
preserve source-root references in mature `knowledge/<domain>/SKILL*.md` files
where those references are useful from the source clone, but rewrite them in
the staged package copy so packaged readers see paths that resolve from the
generated package root. Source edits are allowed only where one spelling is
clearly valid in both contexts and does not churn mature guide prose.

## Inputs

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`
- mature skill entrypoints under `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/`

## Artifact Home

Durable slice-produced evidence belongs here:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/artifacts/`

Expected artifacts include the mature-entrypoint warning baseline, transform
candidate inventory, post-change package-path transcript, staged-package
target checks, compatibility check transcripts, and implementation scope
evidence.

## Scope

In scope:

- establish a generated-package baseline for mature language bundle
  `bundled-reference` warnings;
- classify remaining mature-language `bundled-reference` warnings into:
  entrypoint source-root references, entrypoint package-root references that
  should point under `guides/`, guide-internal references, missing packaged
  assets, or non-target warnings;
- add or refine narrowly scoped package-stage transforms for mature language
  entrypoints where source-root `knowledge/<domain>/guides/**` references
  should package as `guides/**`;
- update `package-path-exceptions.tsv` to retire transformed transitional
  rows without hiding unresolved mature-guide warnings;
- prove the staged package entrypoint paths resolve in generated zips;
- keep durable evidence in this slice's `artifacts/` directory;
- update the slice ledger and close report.

Initial Slice 02 CDC evidence showed total package warnings at 402 and
remaining `bundled-reference` warnings concentrated in:

- `rust-guidelines`: 37 rows, including many `SKILL.md` entrypoint references
  to `14-cli-tools/**` and `15-cargo/**` that should package under `guides/`;
- `javascript-deno-guidelines`: 157 rows, including source-root
  `knowledge/js/guides/**` entrypoint references and guide-internal path
  warnings that must be classified separately;
- `cpp-guidelines`: 2 guide image references, probably asset/package-layout or
  guide-link work rather than entrypoint staging.

Out of scope:

- broad mature guide prose rewrites;
- moving mature guide directory trees;
- fixing every guide-internal warning in Rust, JavaScript/Deno, C++, Go, or
  Erlang;
- package layout expansion unless the evidence proves a missing asset is the
  smallest correct fix and the operator accepts it;
- collaboration-framework bundle changes;
- CCDP package work;
- URL liveness checks.

## Verification Approach

The close set must show:

- baseline mature-entrypoint warning inventory before edits;
- classification of candidate versus non-candidate mature-language warnings;
- package-stage transform or source-edit evidence for targeted entrypoint
  rows;
- generated zip target checks proving staged entrypoint references resolve;
- `make check-package-paths` exits 0 with no new hard failures;
- transformed mature-entrypoint warning count decreases or receives explicit
  policy disposition;
- `scripts/check-package-paths --check-exceptions-only` passes;
- `make check-skills` passes;
- `make all` passes;
- implementation diff scope stays within Make/script staging code,
  `package-path-exceptions.tsv`, and explicitly targeted entrypoint files if
  any source edits are justified;
- durable artifacts are under this slice's `artifacts/` directory.

## Close Conditions

This slice closes when mature-language entrypoint package warnings have a
measurable burn-down or explicit policy disposition, package/staging behavior
is proven against generated zips, all package and compatibility checks pass,
every ledger row has attested evidence, durable evidence artifacts live under
`artifacts/`, and the close report walks every row with Bubble-up to Arc 02.
