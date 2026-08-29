# CC Prompt: Slice 04 CCDP Reader Guidance

You are working in the ai-engineering repository.

Implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice path:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance`

Artifact home:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance/artifacts/`

## Objective

Update CCDP reader guidance so a human or LLM can consume CCDP from either the
source clone or `ccdp.zip`/an unzipped `ccdp/` package without guessing file
locations.

This is a reader-guidance slice. Keep the changes focused on documentation and
package README maintainability.

## Required Inputs

Read these before editing:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/closing-report.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/artifacts/package-path-semantics.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/README.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-ccdp-package`
- `/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/`

## Implementation Requirements

Update source guidance so:

- the root README distinguishes installable skill zips from `ccdp.zip`;
- the root README documents `make ccdp-package` and `make check-ccdp-package`;
- source-clone CCDP entrypoints are explicit and correct;
- package/unzipped CCDP entrypoints are explicit and correct;
- the package README remains package-local and clear;
- changed guidance does not send readers to excluded workbench/prompts material
  unless it is explicitly labelled as excluded/provenance/source-only.

Strongly consider adding `protocols/ccdp/README.md` as a protocol-root
entrypoint whose relative links work both in the source tree and after staging
as `ccdp/README.md`. If that is the cleanest implementation, update the package
staging in `Makefile` to copy that README instead of maintaining inline README
prose in a `printf` block.

## Boundaries

Do not:

- implement CCDP runtime behavior;
- rewrite protocol semantics;
- include `protocols/ccdp/workbench/` or `protocols/ccdp/prompts/` in
  `ccdp.zip`;
- fold CCDP into `INSTALL_ZIPS`, `install`, or the skill-bundle `all` target;
- check URL liveness;
- close Arc 03;
- edit or stage unrelated planning work, including `project02-collab-breakout`.

## Verification

Run from `/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
make ccdp-package
make check-ccdp-package
unzip -p ccdp.zip ccdp/README.md
make check-package-paths
make all
make ccdp
git diff --check
git status --short --untracked-files=all
```

Run targeted checks over changed guidance for source/package path correctness.
At minimum, search the changed docs for `protocols/ccdp`, `ccdp.zip`,
`ccdp/README.md`, `workbench`, `prompts`, `/Users/`, and `/private/tmp`, and
explain any intentional source-only or local-temp references.

Run from `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

```sh
git diff --check
git diff --cached --check
find project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|F-10|Artifacts|Bubble-up to Arc 03" project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance/closing-report.md
```

## Close Requirements

Update the Slice 04 ledger with attested evidence for F-1 through F-10.

Create `closing-report.md` in the slice directory. It must:

- name the implementation commit or current diff state;
- inventory durable artifacts under `artifacts/`;
- walk every ledger row F-1 through F-10;
- include Bubble-up to Arc 03;
- say whether Arc 03 can proceed to formal close or whether a remediation
  slice is required.
