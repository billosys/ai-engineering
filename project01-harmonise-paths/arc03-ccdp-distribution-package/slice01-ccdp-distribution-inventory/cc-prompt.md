# CC Prompt: Slice 01 CCDP Distribution Inventory

You are working in the ai-engineering repository.

Implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice path:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory`

Artifact home:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts/`

## Objective

Complete Arc 03 Slice 01 by inventorying the current CCDP distribution surface.
This is a diagnosis/design-input slice only: do not implement a CCDP package
target yet.

The goal is to give Slice 02 enough evidence to design a first-class CCDP
distribution package that works both from the source clone and from a
zipped/unzipped package context.

## Required Inputs

Read these before collecting evidence:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/README.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/`

## Artifact Requirements

Durable evidence from this slice belongs in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts/`

Expected artifacts:

- `ccdp-file-inventory.*`: current file inventory for `protocols/ccdp`;
- `ccdp-build-targets.*`: current root and CCDP-local build target inventory;
- `ccdp-assembly-check.*`: transcript or summary from the existing CCDP
  assembly gate;
- `ccdp-path-reference-scan.*`: Markdown/JSON-note/README path-reference scan;
- `package-risk-map.*`: classification of references that would break or need
  policy in a standalone package;
- `candidate-package-contents.*`: recommended package contents table;
- `excluded-material.*`: source/provenance/workbench material proposed for
  exclusion or later handling;
- `slice02-design-inputs.*`: design questions and recommendations for the next
  slice;
- implementation/planning diff and status evidence.

Temporary scratch under `/private/tmp` is fine only if durable evidence is
copied or summarized into this slice's `artifacts/` directory.

## Boundaries

Do not:

- implement a CCDP zip/package target;
- edit CCDP protocol prose, JSON examples, visual-guide files, assembler code,
  root packaging lists, README, or `package-path-exceptions.tsv`;
- change skill-bundle packaging;
- check URL liveness;
- stage or commit unrelated planning work, including sibling projects outside
  `project01-harmonise-paths`.

If the existing CCDP assembly gate fails, record the failure exactly and
classify whether package design can continue or must wait for a repair slice.

## Suggested Evidence Commands

From the implementation checkout:

```sh
find protocols/ccdp -maxdepth 4 -type f -print
rg -n "ccdp|CCDP|protocol|package|zip" Makefile README.md protocols/ccdp/Makefile protocols/ccdp -g '*.md' -g 'Makefile'
make ccdp
git diff --check
git status --short --untracked-files=all
```

Add any focused scans needed to identify path-like Markdown links, code spans,
JSON note references, and package-risk candidates. Prefer structured or
repeatable scripts over one-off manual counting when the inventory grows.

From the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|Artifacts|Bubble-up to Arc 03" project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/closing-report.md
```

Before closing, update the slice ledger with attested evidence. The close
report must walk F-1 through F-9, name the implementation commit or current
diff state, inventory artifacts, and Bubble-up to Arc 03. In the bubble-up,
say whether Slice 02 can proceed to package contract design or whether an
iteration/repair slice is needed first.
