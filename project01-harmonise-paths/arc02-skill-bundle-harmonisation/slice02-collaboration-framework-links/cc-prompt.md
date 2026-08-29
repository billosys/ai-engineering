# CC Prompt: Slice 02 Collaboration Framework Links

You are working in the ai-engineering repository.

Implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Slice path:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links`

Artifact home:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/artifacts/`

## Objective

Complete Arc 02 Slice 02 by harmonising collaboration-framework bundle path
references. Use source edits where one relative spelling resolves in both the
source checkout and the generated package; use narrow staging transforms only
where the evidence proves source semantics and package semantics must differ.

Do not chase every warning mechanically. Classify first, then fix the
high-confidence package-invalid framework references and make intentional
non-bundled references explicit.

The source baseline includes the package path gate and Slice 01 tooling link
work committed on `main` at `09d1550`.

## Required Inputs

Read these before editing:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`

Framework source files likely to need inspection:

- `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/PROJECT-MANAGEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/AI-ENGINEERING-METHODOLOGY.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/CODE-AUDIT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/SUBAGENT-DELEGATION-POLICY.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/`
- `/Users/oubiwann/lab/billosys/ai-engineering/templates/LEDGER-DISCIPLINE.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/templates/CONTRIBUTION-TICKET.md`

## Baseline Requirement

Before editing, run `make check-package-paths` and save a
collaboration-framework-scoped warning inventory under this slice's
`artifacts/` directory.

The Slice 01 post-change gate showed framework warnings beginning around the
`collaboration-framework.zip` output, including high-confidence candidates
such as:

- `docs/pm/06-confirmation-protocol.md` -> `docs/PROJECT-MANAGEMENT.md`
- `docs/pm/version-history.md` -> `docs/PROJECT-MANAGEMENT.md`
- `docs/AI-ENGINEERING-METHODOLOGY.md` -> `SKILL.md`

Rebuild the baseline yourself; do not rely only on this prompt.

## Artifact Requirements

Durable evidence from this slice belongs in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/artifacts/`

Expected artifacts:

- baseline collaboration-framework warning inventory;
- warning classification table or notes;
- post-change collaboration-framework warning inventory;
- targeted warning burn-down or disposition summary;
- `make check-package-paths` transcript or summary;
- `scripts/check-package-paths --check-exceptions-only` transcript or summary;
- `make check-skills` transcript or summary;
- `make all` transcript or summary;
- implementation diff-scope inventory.

Temporary scratch under `/private/tmp` is fine only if durable evidence is
copied or summarized into this slice's `artifacts/` directory.

## Boundaries

Do not:

- change methodology substance, posture, or project-management semantics;
- edit mature Rust, Go, C++, Erlang, or JavaScript/Deno language-guide prose;
- edit non-framework skill bundles in this slice;
- add CCDP package targets;
- expand package layout unless the evidence shows that is the smallest correct
  fix and the operator approves;
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

Also produce a framework-scoped warning comparison from the package-path
output. A useful starting point is:

```sh
rg -n "collaboration-framework|docs/pm/|docs/AI-ENGINEERING-METHODOLOGY.md|docs/CODE-AUDIT.md|templates/LEDGER-DISCIPLINE.md|SKILL.md" <package-path-output>
```

Run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|Artifacts|Bubble-up to Arc 02" project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/closing-report.md
```

Before closing, update the slice ledger with attested evidence. The close
report must walk F-1 through F-9, name the implementation commit or current
diff state, inventory artifacts, and Bubble-up to Arc 02.
