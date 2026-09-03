# CC Prompt: Arc04 Slice02 README Orientation Rewrite

You are CC working in Project04 Expedited Mode.

## Context

Project: `project04-knowledge-library-reorg`

Arc: `arc04-user-docs`

Slice: `slice02-readme-orientation-rewrite`

Source checkout:
`/Users/oubiwann/lab/billosys/ai-engineering`

Planning checkout:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Project directory:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg`

## Required Reading

Read these files before working:

- `project-plan.md`
- `ledger.md`
- `arc04-user-docs/arc-plan.md`
- `arc04-user-docs/ledger.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/cdc-verification.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/readme-source-surface-map.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/end-user-docs-decomposition-plan.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/arc04-doc-edit-sequence.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/public-language-boundary-register.md`
- `arc04-user-docs/slice01-readme-docs-decomposition-map/artifacts/docs-validation-command-inventory.md`
- `arc04-user-docs/slice02-readme-orientation-rewrite/slice-plan.md`
- `arc04-user-docs/slice02-readme-orientation-rewrite/ledger.md`

## Task

Rewrite the top-level `README.md` into a concise repository orientation that
matches the post-Arc03 layout and routes deeper explanations to focused
`docs/` guides.

You may create minimal focused-doc stubs if README links need them before
Slice03 expands the guide content. Keep stubs minimal: title, purpose, and a
short note that Slice03 will expand the guide. Do not move knowledge substrate
into `docs/`.

Create these planning artifacts:

- `arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/readme-orientation-change-map.md`
- `arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/readme-route-repair-evidence.md`
- `arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/focused-doc-stub-register.md`
- `arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/source-change-and-validation-evidence.md`

Update:

- `arc04-user-docs/slice02-readme-orientation-rewrite/ledger.md`

Add:

- `arc04-user-docs/slice02-readme-orientation-rewrite/closing-report.md`

Do not create `cdc-verification.md`; CDC owns that after your proposed close.

## Source Edit Policy

Source edits are authorized for:

- `README.md`
- any minimal `docs/*.md` stubs needed so README links resolve
- a narrow `docs/ORIGINS.md` route repair only if the README rewrite touches
  that navigation path and the repair is needed for coherence

Do not edit `knowledge/**`, `Makefile`, `package-path-exceptions.tsv`,
`SKILL.md`, generated zips, or CCDP source files unless you stop and record an
operator gate. Do not finalize Arc05 vocabulary.

Commit source edits first, before planning edits, using explicit file paths in
both staging and commit commands. Do not commit generated zips.

Every assistant-authored commit must include both trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Validation

Run and record:

- source `git status --short --untracked-files=all`
- source `git diff --check`
- targeted route checks:
  - `rg -n "\\[[^\\]]+\\]\\([^\\)]+\\)|https?://|docs/|knowledge/|protocols/|templates/|Makefile|package" README.md docs`
  - `rg -n "docs/dev|docs/design|CODE-AUDIT|AI-ENGINEERING|PROJECT-MANAGEMENT|SUBAGENT|LEDGER-DISCIPLINE|CONTRIBUTION-TICKET|templates/" README.md docs`
  - `find docs -maxdepth 2 -type f | sort`
  - `rg -n "^#{1,4} " README.md docs`
- `make check-skills`
- `make check-package-paths`
- `make all`
- `make ccdp-package`
- `make check-ccdp-package`
- planning `git diff --check`
- all six Slice02 ledger verifier commands
- final source and planning `git status --short`

If a targeted route check still reports stale strings, record whether the
match is repaired historical context, a deliberate Arc05 deferral, or a
remaining defect.

## Source Commit

Commit source edits with explicit paths. The exact path list depends on whether
you create stubs, but it must list every source file explicitly. Example shape:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering add \
  README.md \
  docs/repository-overview.md \
  docs/skill-library.md \
  docs/collaboration-framework.md \
  docs/knowledge-library-anatomy.md \
  docs/building-and-installing.md \
  docs/protocols.md \
  docs/contributing.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering commit \
  -m "Rewrite README orientation for Project04 Arc04" \
  -- \
  README.md \
  docs/repository-overview.md \
  docs/skill-library.md \
  docs/collaboration-framework.md \
  docs/knowledge-library-anatomy.md \
  docs/building-and-installing.md \
  docs/protocols.md \
  docs/contributing.md
```

Include the required co-author trailers in the source commit message. Adjust
the path list to exactly match the files you edited.

## Planning Commit

After source commit and validation, commit only the Slice02 planning close
packet with an explicit file list:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/readme-orientation-change-map.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/readme-route-repair-evidence.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/focused-doc-stub-register.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/source-change-and-validation-evidence.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/ledger.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/closing-report.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc04 Slice02" \
  -- \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/readme-orientation-change-map.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/readme-route-repair-evidence.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/focused-doc-stub-register.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/artifacts/source-change-and-validation-evidence.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/ledger.md \
  project04-knowledge-library-reorg/arc04-user-docs/slice02-readme-orientation-rewrite/closing-report.md
```

Include both required trailers in the planning commit message.

## Report

Report:

- source commit hash;
- planning commit hash;
- source files edited;
- ledger result;
- validation commands and outcomes;
- final source and planning checkout status;
- whether Slice02 is proposed-done pending CDC verification.
