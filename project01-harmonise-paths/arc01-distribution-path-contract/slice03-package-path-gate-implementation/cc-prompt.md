# CC Prompt: Slice 03 Package Path Gate Implementation

You are working in the ai-engineering repository.

Implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice path:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation`

Artifact home:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/artifacts/`

## Objective

Complete Slice 03 by implementing the package path gate designed in Slice 02.

The public interface is `make check-package-paths`. The checker entry point is
`scripts/check-package-paths`, a checked-in executable Python 3 script with no
`.py` suffix. Generated zip archives named by `INSTALL_ZIPS` are the
authoritative validation surface.

## Required Inputs

Read these before editing:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/2026.08.29-package-path-audit.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/.gitignore`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/PROJECT-MANAGEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/02-canonical-planning-worktree.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/03-planning-top-down.md`

## Implementation Requirements

Implement:

- `make check-package-paths`;
- `scripts/check-package-paths`;
- `package-path-exceptions.tsv` if current known misses need an explicit
  transitional policy for a non-breaking initial gate;
- parser/schema/current-package evidence captured under the slice
  `artifacts/` directory;
- this slice's updated `ledger.md`;
- this slice's `closing-report.md`.

The checker must:

- scan generated zip archives named by `INSTALL_ZIPS`;
- parse Markdown inline links, image links, reference definitions, same-file
  anchors, `path#anchor` references, fenced code, indented code where feasible,
  conservative code spans, placeholders, and external URLs;
- classify emitted findings as `bundled-reference`, `source-clone-reference`,
  `repo-only/provenance`, `example-project path`, `external URL`,
  `parser false positive`, or `unclassified`;
- avoid using a raw regex pass as the hard-fail gate;
- return 0 for no hard failures, 1 for hard package-path failures, and 2 for
  invocation/schema errors;
- report separate buckets for hard failures, warnings, explicit exceptions,
  skipped external URLs, and parser-suppressed or omitted material;
- avoid filtered-CSV overclaiming: if the checker skips or suppresses a class,
  say that directly.

## Artifact Requirements

Durable evidence from this slice belongs in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/artifacts/`

Expected durable artifacts:

- current `make check-package-paths` transcript or report;
- parser fixture/self-test transcript or report;
- malformed exception schema transcript or report;
- any short implementation note needed to explain artifact contents.

Do not use implementation `workbench/` as the durable home for these artifacts.
Temporary scratch under `/private/tmp` is fine only if the durable evidence is
copied or summarized into this slice's `artifacts/` directory.

## Boundaries

Do not:

- harmonise the 145 current actionable misses except as needed to make the gate
  runnable under an explicit transitional policy;
- edit mature language guide prose;
- add CCDP package targets;
- change package layouts;
- implement URL liveness checks;
- change the collaboration-framework planning methodology;
- stage or commit unrelated planning work, including any sibling planning
  project outside `project01-harmonise-paths`.

## Verification

Run from the implementation checkout:

```sh
rg -n "check-package-paths" Makefile
test -x scripts/check-package-paths
test ! -e scripts/check-package-paths.py
make check-package-paths
make check-skills
make all
git diff --check
```

Also run the checker self-test or fixture command you choose for parser and
schema coverage. Capture durable evidence under the slice `artifacts/`
directory.

Run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|Artifacts|Bubble-up to Arc 01" project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/closing-report.md
```

Before closing, inspect the implementation diff or implementation commit and
confirm the scope boundary: expected implementation paths are `Makefile`,
`scripts/check-package-paths`, `package-path-exceptions.tsv`, and narrowly
scoped permanent test/fixture files if needed.

Close by updating the slice ledger with attested evidence, writing
`closing-report.md`, inventorying artifacts, and adding Bubble-up to Arc 01.
