# Slice 01: CCDP Distribution Inventory

```yaml
project: project01-harmonise-paths
arc: arc03-ccdp-distribution-package
slice: slice01-ccdp-distribution-inventory
status: open
opened-on: 2026-08-29
opened-by: CDC
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
artifact-home: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts
depends-on:
  - arc02-skill-bundle-harmonisation
```

## Capability Statement

This slice inventories the current CCDP distribution surface before any package
target is designed or implemented.

The output should answer: what CCDP materials exist, what builds them, what a
reader needs in source and package contexts, which references would break in a
standalone package, and which materials are source/provenance/workbench rather
than distribution content.

## Inputs

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/README.md`

## Artifact Home

Durable slice-produced evidence belongs here:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts/`

Expected artifacts include:

- current CCDP file inventory;
- current CCDP build-target inventory;
- generated assembled-spec check;
- path/reference scan of `protocols/ccdp` Markdown, JSON notes, and README
  references;
- candidate package contents table;
- excluded/provenance/workbench material notes;
- package-risk map for Slice 02.

## Scope

In scope:

- inventory `protocols/ccdp/src/`,
  `protocols/ccdp/composite-cognition-dispatch-protocol.md`,
  `protocols/ccdp/json/`, `protocols/ccdp/visual-guide/`,
  `protocols/ccdp/templates/`, `protocols/ccdp/prompts/`, and relevant
  workbench/review material;
- inspect root and CCDP Make targets related to CCDP assembly;
- run the existing CCDP assembly gate needed for confidence in the inventory;
- identify reader entrypoint candidates for a future CCDP package;
- identify source-only, provenance-only, and workbench-only material that
  should probably not ship;
- identify path references that would be invalid from a zipped/unzipped CCDP
  package unless transformed, moved, or documented;
- produce durable evidence under `artifacts/`;
- update the slice ledger and close report.

Out of scope:

- implementing a CCDP zip/package target;
- editing protocol prose, JSON examples, or assembler code;
- changing skill-bundle packaging;
- changing `package-path-exceptions.tsv` unless the inventory discovers a
  documented checker/reporting defect and the operator approves;
- URL liveness checks;
- release/adoption README changes.

## Verification Approach

The close set must show:

- inventory of CCDP files and build targets;
- proof that the existing CCDP assembly target still runs, or a precise blocked
  reason with re-entry condition;
- path/reference scan results and package-risk classification;
- candidate package contents and excluded material rationale;
- no implementation edits outside the inventory scope;
- durable artifacts under this slice's `artifacts/` directory;
- ledger row updates and a close report with Bubble-up to Arc 03.

## Close Conditions

This slice closes when the CCDP distribution surface is inventoried well enough
to design the package contract in Slice 02, the existing CCDP build baseline is
checked or explicitly blocked, every ledger row has attested evidence, durable
evidence artifacts live under `artifacts/`, and the close report walks every
row with Bubble-up to Arc 03.
