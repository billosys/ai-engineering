# CC Prompt: Slice 03 Mature Entrypoint Staging Transforms

You are working in the ai-engineering repository.

Implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice path:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms`

Artifact home:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/artifacts/`

## Objective

Complete Arc 02 Slice 03 by harmonising mature language skill entrypoint
package paths without restructuring mature guide prose. Prefer a narrow
Make/script-friendly package staging transform when source-root references are
correct in the source clone but package-invalid after bundling.

The source baseline includes:

- `09d1550` - package path gate and tooling link harmonisation;
- `0c5997e` - collaboration-framework link harmonisation.

## Required Inputs

Read these before editing:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`

Potential mature entrypoint/package targets:

- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/rust/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/go/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/cpp/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/erlang/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/js/SKILL.md`

Inspect others only if the generated package baseline shows they are
entrypoint candidates.

## Baseline Requirement

Before editing, run `make check-package-paths` and save a mature-language
`bundled-reference` warning inventory under this slice's `artifacts/`
directory.

The Slice 02 CDC verification saw total package warnings at 402 and remaining
`bundled-reference` warnings concentrated in:

- `rust-guidelines`: 37 rows;
- `javascript-deno-guidelines`: 157 rows;
- `cpp-guidelines`: 2 rows.

Rebuild and classify the baseline yourself. In particular, separate entrypoint
staging-transform candidates from guide-internal path warnings and missing
asset/layout warnings. Do not convert this slice into a broad guide rewrite.

## Artifact Requirements

Durable evidence from this slice belongs in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/artifacts/`

Expected artifacts:

- baseline mature-language bundled-reference inventory;
- mature warning classification table or notes;
- transform candidate inventory;
- post-change mature-entrypoint warning inventory;
- staged/source target resolution checks;
- `make check-package-paths` transcript or summary;
- `scripts/check-package-paths --check-exceptions-only` transcript or summary;
- `make check-skills` transcript or summary;
- `make all` transcript or summary;
- implementation diff-scope inventory.

Temporary scratch under `/private/tmp` is fine only if durable evidence is
copied or summarized into this slice's `artifacts/` directory.

## Boundaries

Do not:

- rewrite mature language guide prose broadly;
- move mature guide directory trees;
- fix guide-internal link warnings unless the fix is necessary to prove a
  narrowly targeted entrypoint transform and is explicitly justified;
- add missing image/assets or expand package layout without operator approval;
- edit collaboration-framework bundle files;
- add CCDP package targets;
- check URL liveness;
- stage or commit unrelated planning work, including any sibling planning
  project outside `project01-harmonise-paths`.

## Verification

Run from the implementation checkout:

```sh
make check-package-paths
scripts/check-package-paths --check-exceptions-only
make check-skills
make all
git diff --check
git status --short --untracked-files=all
```

Also produce generated-package checks showing targeted staged entrypoint paths
resolve inside the zip files and source-checkout checks showing the source
entrypoints still point at real source files where source-root paths were
preserved.

Run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|F-10|Artifacts|Bubble-up to Arc 02" project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/closing-report.md
```

Before closing, update the slice ledger with attested evidence. The close
report must walk F-1 through F-10, name the implementation commit or current
diff state, inventory artifacts, and Bubble-up to Arc 02.
