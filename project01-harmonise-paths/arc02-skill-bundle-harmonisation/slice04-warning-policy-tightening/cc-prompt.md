# CC Prompt: Slice 04 Warning Policy Tightening

You are working in the ai-engineering repository.

Implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice path:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening`

Artifact home:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/artifacts/`

## Objective

Complete Arc 02 Slice 04 by tightening the package-path warning policy after
the entrypoint-warning classes have been burned down. The goal is not
necessarily zero warnings; the goal is an honest, explicit, auditable warning
surface where resolved transitional rows are retired, permanent non-bundled
references are narrowly documented, and real package usability work remains
visible for later arcs or projects.

The source baseline includes:

- `09d1550` - package path gate and tooling link harmonisation;
- `0c5997e` - collaboration-framework link harmonisation;
- `a8decce` - mature entrypoint staging transforms.

## Required Inputs

Read these before editing:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`

## Baseline Requirement

Before editing, run `make check-package-paths` and save a warning baseline
under this slice's `artifacts/` directory.

CDC verification for Slice 03 reproduced:

- `hard failures: 0`
- `warnings: 295`
- `explicit exceptions: 3`
- 89 `bundled-reference` warning rows
- 146 `repo-only/provenance` warning rows
- 26 `source-clone-reference` warning rows
- 25 `example-project path` warning rows
- 9 parser false-positive warning rows

Rebuild and classify the baseline yourself from generated package output.

## Artifact Requirements

Durable evidence from this slice belongs in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/artifacts/`

Expected artifacts:

- current warning baseline from `make check-package-paths`;
- warning policy classification by package/class/disposition;
- transitional exception disposition notes;
- exception diff scope notes;
- later-arc backlog notes for unresolved package usability issues;
- post-change `make check-package-paths` transcript or summary;
- `scripts/check-package-paths --check-exceptions-only` transcript or summary;
- `make check-skills` transcript or summary;
- `make all` transcript or summary;
- implementation diff-scope inventory;
- planning artifact inventory.

Temporary scratch under `/private/tmp` is fine only if durable evidence is
copied or summarized into this slice's `artifacts/` directory.

## Boundaries

Do not:

- hide unresolved package usability defects behind package-wide, document-wide,
  or class-wide broad exceptions;
- rewrite mature language guide prose broadly;
- move mature language guide directory trees;
- add CCDP package targets;
- perform URL liveness checks;
- change collaboration-framework methodology content except for tiny
  package-warning-policy wording if the slice proves it is required;
- close Arc 02 yourself; leave Arc 02 close to CDC after this slice is
  proposed-done;
- stage or commit unrelated planning work, including any sibling planning
  project outside `project01-harmonise-paths`.

Small implementation changes are allowed only when they directly serve this
slice:

- `package-path-exceptions.tsv` updates;
- small checker reporting/policy fixes if classification exposes a checker
  false-positive or policy mismatch;
- tiny source/package fixes when clearly safer than a permanent exception and
  explicitly supported by the classification.

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

Run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|F-10|Artifacts|Bubble-up to Arc 02" project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/closing-report.md
```

Before closing, update the slice ledger with attested evidence. The close
report must walk F-1 through F-10, name the implementation commit or current
diff state, inventory artifacts, and Bubble-up to Arc 02. In the bubble-up,
say whether Arc 02 is ready for CDC close or whether another iteration slice
is needed.
