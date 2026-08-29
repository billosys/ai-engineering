# CC Prompt: Slice 03 CCDP Package Implementation

You are working in the ai-engineering repository.

Implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice path:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation`

Artifact home:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/artifacts/`

## Objective

Implement the CCDP distribution package selected by Slice 02.

The target package is `ccdp.zip`, containing exactly one `ccdp/` archive root.
The package must be rebuild-capable and usable read-only after unzip, with a
generated package-local `ccdp/README.md` as the entrypoint.

## Required Inputs

Read these before editing:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts/ccdp-package-contract-design.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts/package-contents-manifest-draft.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts/package-path-semantics.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts/generated-output-freshness-decision.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts/validation-checker-strategy.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts/slice03-implementation-inputs.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/`

## Implementation Requirements

Implement in the source checkout:

- `make ccdp-package`;
- `make check-ccdp-package`;
- `scripts/check-ccdp-package`;
- staging into `build/ccdp/`;
- `ccdp.zip` with one `ccdp/` root;
- generated package-local `ccdp/README.md`;
- required package contents from the Slice 02 manifest;
- required exclusions from the Slice 02 manifest;
- package-local Markdown path validation for zipped/unzipped CCDP use;
- protocol-syntax filtering for JSON Pointers, slash-prefixed protocol paths,
  elision comments, and field paths;
- extracted-package non-mutating assembly validation.

Generated assembled-spec freshness is a hard requirement. Before packaging,
compare temporary assembly output against the committed
`protocols/ccdp/composite-cognition-dispatch-protocol.md`. If there is drift,
update the committed assembled spec as a named pre-package step inside this
slice, rerun the freshness check, and only package once the committed spec is
fresh.

## Boundaries

Do not:

- implement CCDP runtime behavior;
- include `protocols/ccdp/workbench/` or `protocols/ccdp/prompts/`;
- include Cargo `target/` output;
- copy the root repository README or root Makefile into the package unchanged;
- fold `ccdp.zip` into `INSTALL_ZIPS` or the skill-bundle `all` target unless
  the existing Makefile architecture forces it and you document why;
- check URL liveness;
- rewrite protocol prose except for generated assembled-spec refresh required
  by the freshness gate;
- edit or stage unrelated planning work, including `project02-collab-breakout`.

## Verification

Run from `/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
make ccdp-package
make check-ccdp-package
unzip -l ccdp.zip
make check-package-paths
make all
git diff --check
git status --short --untracked-files=all
```

Also ensure the package validator proves:

- `ccdp.zip` exists;
- all zip entries are under one `ccdp/` root;
- required contents are present;
- excluded materials are absent;
- Markdown paths resolve after unzip from the package context;
- protocol syntax is not treated as filesystem paths;
- extracted package assembly succeeds with a temporary output path.

Run from `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

```sh
git diff --check
git diff --cached --check
find project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|F-10|F-11|F-12|Artifacts|Bubble-up to Arc 03" project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/closing-report.md
```

## Close Requirements

Update the Slice 03 ledger with attested evidence for F-1 through F-12.

Create `closing-report.md` in the slice directory. It must:

- name the implementation commit or current diff state;
- inventory durable artifacts under `artifacts/`;
- walk every ledger row F-1 through F-12;
- include Bubble-up to Arc 03;
- say whether Slice 04 reader guidance can proceed, whether Arc 03 can close,
  or whether a repair slice is required.
