# Slice 02: CCDP Package Contract Design

```yaml
project: project01-harmonise-paths
arc: arc03-ccdp-distribution-package
slice: slice02-ccdp-package-contract-design
status: open
opened-on: 2026-08-29
opened-by: CDC
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
artifact-home: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts
depends-on:
  - arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory
```

## Capability Statement

This slice designs the CCDP package contract from the Slice 01 inventory. It
chooses the package shape, entrypoint, contents, exclusions, path semantics,
validation strategy, and generated-output freshness policy that Slice 03 will
implement.

This is a design slice. It must not implement the package target.

## Inputs

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts/`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/`

## Artifact Home

Durable slice-produced evidence belongs here:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts/`

Expected artifacts include a package contract design report, contents manifest
draft, path semantics table, validation strategy, generated-output freshness
decision, implementation-slice input notes, and status/check transcripts.

## Scope

In scope:

- choose the CCDP archive name and root directory;
- choose the package entrypoint strategy;
- decide whether the first package is read-only, rebuild-capable, or both as
  separate targets;
- define required package contents and explicitly excluded material;
- define package-local path semantics for the assembled spec, source chapters,
  JSON corpus, visual guide/reference, templates, tools, and package entrypoint;
- decide how to handle `src/README.md` references to `../tools/`;
- decide whether root README material is excluded, transformed, or distilled
  into a CCDP-local entrypoint;
- decide the generated-output freshness policy for
  `composite-cognition-dispatch-protocol.md`;
- define the package validation/checker strategy, including how to avoid
  treating JSON Pointers and protocol slash paths as filesystem paths;
- produce Slice 03 implementation recommendations and ledger candidates;
- update this slice's ledger and close report.

Out of scope:

- implementing a CCDP zip/package target;
- editing implementation source, protocol prose, JSON examples, visual guide,
  assembler code, README, Makefile, or `package-path-exceptions.tsv`;
- moving CCDP files;
- checking URL liveness;
- release/adoption guidance that belongs to Arc 04;
- closing Arc 03.

## Verification Approach

The close set must show:

- a design report derived from Slice 01 inventory evidence;
- explicit decisions for archive name, package root, entrypoint, contents,
  exclusions, read-only/rebuild-capable semantics, generated-output freshness,
  path semantics, and validation/checker policy;
- no unresolved blocking question required before Slice 03 implementation;
- Slice 03 implementation recommendations and proposed ledger anchors;
- implementation checkout remains clean;
- durable artifacts live under this slice's `artifacts/` directory;
- close report walks every ledger row with Bubble-up to Arc 03.

## Close Conditions

This slice closes when the CCDP package contract is specific enough for Slice
03 implementation, every design decision listed in scope has an explicit
disposition, unresolved work is either routed or blocked with re-entry
conditions, every ledger row has attested evidence, durable artifacts live
under `artifacts/`, and the close report walks every row with Bubble-up to Arc
03.
