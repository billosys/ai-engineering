# CC Prompt: Slice 01 Tooling Entrypoint Links

You are working in the ai-engineering repository.

Implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice path:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links`

Artifact home:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/artifacts/`

## Objective

Complete Arc 02 Slice 01 by harmonising low-risk tooling/simple skill
entrypoint guide references. Use path spellings that resolve in both the source
checkout and generated package root, then prove the package-path warning
burn-down with `make check-package-paths`.

Important baseline note: Arc 01 Slice 03's package-path gate is currently
verified as an implementation working-tree diff. Preserve the current
`Makefile`, `scripts/check-package-paths`, and `package-path-exceptions.tsv`
state unless the operator commits it before you begin.

## Required Inputs

Read these before editing:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/closing-report.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`

## Target Files

Target only these entrypoint files unless the ledger forces a tiny supporting
change:

- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/deno/SKILL-js-linter.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/biome/SKILL-js-linter.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/biome/SKILL-web-linter.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/tailwindcss/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/cobalt/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`

Expected source edit pattern:

- replace `knowledge/deno/guides/...` with `guides/...`;
- replace `knowledge/biome/guides/js-linter/...` with
  `guides/js-linter/...`;
- replace `knowledge/biome/guides/web-linter/...` with
  `guides/web-linter/...`;
- replace `knowledge/tailwindcss/guides/...` with `guides/...`;
- replace `knowledge/cobalt/guides/...` with `guides/...`.

Only make these edits where the target file actually exists in the source
checkout and will be bundled under the same package-local path.

## Artifact Requirements

Durable evidence from this slice belongs in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/artifacts/`

Expected artifacts:

- baseline targeted warning inventory;
- post-change targeted warning inventory;
- `make check-package-paths` transcript or summary;
- `make check-skills` transcript or summary;
- `make all` transcript or summary;
- implementation diff-scope inventory.

Temporary scratch under `/private/tmp` is fine only if durable evidence is
copied or summarized into this slice's `artifacts/` directory.

## Boundaries

Do not:

- edit mature Rust, Go, C++, Erlang, or JavaScript/Deno language-guide prose;
- edit collaboration-framework/project-management bundle files in this slice;
- add generalized staging transforms unless a tiny helper is required and
  justified in the close report;
- add CCDP package targets;
- change package layout;
- check URL liveness;
- change the collaboration-framework planning spec;
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

Also inspect targeted references:

```sh
! rg -n "knowledge/(deno|biome|tailwindcss|cobalt)/guides" knowledge/deno/SKILL-js-linter.md knowledge/biome/SKILL-js-linter.md knowledge/biome/SKILL-web-linter.md knowledge/tailwindcss/SKILL.md knowledge/cobalt/SKILL.md
```

Run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|Artifacts|Bubble-up to Arc 02" project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/closing-report.md
```

Before closing, update the slice ledger with attested evidence. The close
report must walk F-1 through F-8, name the implementation commit or current
diff state, inventory artifacts, and Bubble-up to Arc 02.
