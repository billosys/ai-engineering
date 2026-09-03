# CC Prompt: Arc05 Slice04 Vocabulary Reconciliation and Close Readiness

You are CC working in Project04 Expedited Mode.

## Context

Project: `project04-knowledge-library-reorg`

Arc: `arc05-skill-vocabulary`

Slice: `slice04-vocabulary-reconciliation`

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
- `arc05-skill-vocabulary/arc-plan.md`
- `arc05-skill-vocabulary/ledger.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/cdc-verification.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/cdc-verification.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/accepted-public-vocabulary.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/public-language-avoid-list.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/re-entry-condition-register.md`
- `arc05-skill-vocabulary/slice03-public-wording-implementation/cdc-verification.md`
- `arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/public-wording-implementation-map.md`
- `arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/vocabulary-scan-evidence.md`
- `arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/source-change-and-validation-evidence.md`
- `arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/deferred-reentry-notes.md`
- `arc05-skill-vocabulary/slice04-vocabulary-reconciliation/slice-plan.md`
- `arc05-skill-vocabulary/slice04-vocabulary-reconciliation/ledger.md`

## Task

Reconcile Arc05 public vocabulary after Slice03 source implementation, validate
README/docs/SKILL consistency and package/path behavior, disposition the
Slice03 CCDP re-entry item, and prepare Arc05 for CDC arc close.

Create these planning artifacts:

- `arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/vocabulary-reconciliation-report.md`
- `arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/navigation-and-link-validation-evidence.md`
- `arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/package-and-build-validation-evidence.md`
- `arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/ccdp-reentry-disposition.md`
- `arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/arc05-close-readiness-report.md`

Update:

- `arc05-skill-vocabulary/slice04-vocabulary-reconciliation/ledger.md`

Add:

- `arc05-skill-vocabulary/slice04-vocabulary-reconciliation/closing-report.md`

Do not create `cdc-verification.md`; CDC owns that after your proposed close.
Do not close Arc05; CDC owns formal arc close after Slice04 is verified.

## Source Edit Policy

Start read-only. If validation finds a narrow public wording or local-link
defect, you may edit only these authorized source surfaces:

- `README.md`
- `docs/repository-overview.md`
- `docs/skill-library.md`
- `docs/collaboration-framework.md`
- `docs/knowledge-library-anatomy.md`
- `docs/protocols.md`
- `docs/contributing.md`
- `docs/building-and-installing.md`
- top-level `SKILL.md`

If you edit source, commit source edits first with an explicit path list.
If no source edit is needed, create no source commit and say so.

Do not edit:

- `protocols/ccdp/**`
- `Makefile`
- `package-path-exceptions.tsv`
- generated zips
- package roots, package lists, package target names, `INSTALL_ZIPS`,
  `ALL_SKILL_FILES`, or `CF_FILES`
- `knowledge/*/SKILL*.md` frontmatter names, descriptions, or categories
- `templates/GUIDE.md`
- source moves or file renames
- `concept-card-method` implementation
- CCDP repackaging as an installable skill

The known Slice03 re-entry item is that `make ccdp-package` can report a stale
assembled CCDP spec. If it still does, record that as a deferred/re-entry item
unless the operator explicitly authorizes `protocols/ccdp/**` edits.

Every assistant-authored commit must include both trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Validation

Run and record:

- source `git status --short --untracked-files=all` before work
- source `git diff --check`
- accepted vocabulary scan over `README.md`, `docs/`, and `SKILL.md`
- avoided/prohibited claim scan over `README.md`, `docs/`, and `SKILL.md`
- local README/docs/SKILL link validation
- README/docs route scan for `docs/`, `knowledge/`, `protocols/`,
  `templates/`, `Makefile`, and package links
- `make check-skills`
- `make check-package-paths`
- `make all`
- CCDP package check disposition: run or inspect enough to determine whether
  `make ccdp-package` / `make check-ccdp-package` are green or still blocked
  by stale assembled protocol output outside authorization
- planning `git diff --check`
- all seven Slice04 ledger verifier commands
- final source and planning `git status --short --untracked-files=all`

If a scan still reports a risky phrase, record whether the match is a quoted
avoid-list item, a caveated "not this" explanation, a valid historical
reference, a deferral, or a remaining defect.

## Optional Source Commit

If source edits are required, commit them with an explicit path list matching
exactly the files you changed. Use this shape and adjust the paths:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering add \
  README.md \
  docs/repository-overview.md \
  docs/skill-library.md \
  docs/collaboration-framework.md \
  docs/knowledge-library-anatomy.md \
  docs/protocols.md \
  docs/contributing.md \
  docs/building-and-installing.md \
  SKILL.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering commit \
  -m "Reconcile Arc05 public vocabulary wording" \
  -- \
  README.md \
  docs/repository-overview.md \
  docs/skill-library.md \
  docs/collaboration-framework.md \
  docs/knowledge-library-anatomy.md \
  docs/protocols.md \
  docs/contributing.md \
  docs/building-and-installing.md \
  SKILL.md
```

Include the required co-author trailers in the source commit message.

## Planning Commit

After source validation, commit only the Slice04 planning close packet with an
explicit file list:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/vocabulary-reconciliation-report.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/navigation-and-link-validation-evidence.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/package-and-build-validation-evidence.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/ccdp-reentry-disposition.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/arc05-close-readiness-report.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/ledger.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/closing-report.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc05 Slice04" \
  -- \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/vocabulary-reconciliation-report.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/navigation-and-link-validation-evidence.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/package-and-build-validation-evidence.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/ccdp-reentry-disposition.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/artifacts/arc05-close-readiness-report.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/ledger.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice04-vocabulary-reconciliation/closing-report.md
```

Include both required trailers in the planning commit message.

## Report

Report:

- source commit hash, or confirmation that no source commit was created;
- planning commit hash;
- artifacts created;
- vocabulary reconciliation result;
- CCDP re-entry disposition;
- Arc05 close-readiness result;
- ledger result;
- validation commands and outcomes;
- final source and planning checkout status;
- whether Slice04 is proposed-done pending CDC verification.
