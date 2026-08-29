# CC Prompt: Slice 02 CCDP Package Contract Design

You are working in the ai-engineering repository.

Implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice path:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design`

Artifact home:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts/`

## Objective

Complete Arc 03 Slice 02 by designing the CCDP package contract. Use the Slice
01 inventory to choose the package shape, contents, entrypoint, path semantics,
validation strategy, and generated-output freshness policy that Slice 03 will
implement.

This is a design slice only. Do not implement a CCDP package target yet.

## Required Inputs

Read these before writing the design:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts/ccdp-file-inventory.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts/package-risk-map.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts/candidate-package-contents.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts/excluded-material.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts/slice02-design-inputs.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/`

## Required Design Decisions

The design must decide, not merely list options:

- archive name;
- package root directory;
- package entrypoint;
- whether Slice 03 implements a read-only package, a rebuild-capable package,
  or multiple targets;
- exact package contents and exclusions;
- package-local path semantics for every included area;
- required staging transforms or package-local generated files;
- generated-output freshness policy for
  `protocols/ccdp/composite-cognition-dispatch-protocol.md`;
- validation/checker strategy, including zip and unzipped checks;
- handling for JSON Pointers and protocol slash paths so they are not treated
  as filesystem paths;
- Slice 03 implementation outline and proposed ledger anchors.

## Artifact Requirements

Durable evidence from this slice belongs in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts/`

Expected artifacts:

- `ccdp-package-contract-design.md` or equivalent design report;
- package decision matrix;
- package contents manifest draft;
- package path semantics table;
- generated-output freshness decision;
- validation/checker strategy;
- Slice 03 implementation inputs;
- implementation/planning diff and status evidence;
- artifact inventory.

Temporary scratch under `/private/tmp` is fine only if durable evidence is
copied or summarized into this slice's `artifacts/` directory.

## Boundaries

Do not:

- implement a CCDP zip/package target;
- edit CCDP protocol prose, JSON examples, visual-guide files, assembler code,
  root README, root Makefile, CCDP Makefile, or `package-path-exceptions.tsv`;
- move CCDP files;
- check URL liveness;
- close Arc 03;
- stage or commit unrelated planning work, including sibling projects outside
  `project01-harmonise-paths`.

If you believe the generated assembled-spec drift must be fixed before package
implementation, record that as a Slice 03 prerequisite or a repair slice
recommendation. Do not repair it inside this design slice.

## Verification

Run from the implementation checkout:

```sh
git diff --check
git status --short --untracked-files=all
```

If you run an assembly check, avoid leaving the tracked assembled spec dirty.
For example, use the CCDP-local target with a temporary output path:

```sh
make -C protocols/ccdp ccdp-rfc OUTPUT=/private/tmp/ccdp-slice02-assembled.md
```

Run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|F-10|Artifacts|Bubble-up to Arc 03" project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/closing-report.md
```

Before closing, update the slice ledger with attested evidence. The close
report must walk F-1 through F-10, name the implementation commit or current
diff state, inventory artifacts, and Bubble-up to Arc 03. In the bubble-up,
say whether Slice 03 can proceed to package implementation or whether a repair
slice is needed first.
