# CC Prompt: Arc03 Slice02 Top-Level Compatibility Decision

You are CC for Project04 Arc03 Slice02,
`slice02-top-level-compatibility-decision`.

Project04 is in Expedited Mode. Commit your own changes before CDC review, and
use explicit file lists for every `git add` and `git commit -- <paths>` command.
Do not use broad staging.

## Read First

From the planning checkout:

- `project04-knowledge-library-reorg/project-plan.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/arc-plan.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/ledger.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/cdc-verification.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/slice-plan.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/ledger.md`

From the source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`,
inspect only what the slice needs:

- `SKILL.md`
- `Makefile`
- `README.md`
- `AGENTS.md`
- `CLAUDE.md` symlink behavior

## Assignment

Select and validate the top-level `SKILL.md` compatibility path before any
collaboration-framework composer source material moves.

Choose exactly one selected path:

- **validated shim**: top-level `SKILL.md` remains a thin compatibility
  entrypoint that can route to the accepted future
  `knowledge/collaboration-framework/` composer source while preserving the
  `collaboration-framework` package/load behavior.
- **replacement route**: packaging/source routing makes a new root
  authoritative while preserving the generated `collaboration-framework.zip`
  root and entrypoint behavior.
- **no-shim**: top-level `SKILL.md` remains authoritative for now, with a
  rationale and re-entry condition for revisiting the decision when composer
  source material moves.

This slice may edit source files only when the selected path requires it. The
allowed source scope is limited to `SKILL.md`, `Makefile`, `README.md`,
`AGENTS.md`, and `CLAUDE.md` symlink behavior or compatibility references.
Do not move composer source material. Do not move or edit `docs/`, `knowledge/`,
`templates/`, `protocols/ccdp`, `package-path-exceptions.tsv`, or generated
zips unless you stop for operator approval first.

## Required Artifacts

Create these under this slice's `artifacts/` directory:

- `artifacts/top-level-skill-compatibility-decision.md`
- `artifacts/compatibility-implementation-record.md`
- `artifacts/validation-evidence-map.md`

The implementation record must say either `source-files-edited: false` or
`source-files-edited: true` and list exact source files touched.

## Validation

Run and record:

- source checkout `git status --short`
- source checkout `git diff --check` if source files changed
- `make check-skills`
- `make collab-framework`
- route/package review for `collaboration-framework.zip`, including package
  root and entrypoint behavior for the selected path
- planning checkout `git diff --check`

If `make collab-framework` changes only ignored/generated zip output, record
that fact and do not commit generated zips. If it produces a tracked source
change, stop and record the unexpected condition before committing it.

## Ledger and Close

Update `ledger.md` row by row with attested evidence. Then write
`closing-report.md` with:

- a capability verdict;
- artifact inventory;
- row-by-row ledger walk for all six rows;
- source checkout status and source commit, or explicit no-source-edit status;
- planning checkout status;
- silent-drop check;
- Bubble-Up to Arc03.

Do not create `cdc-verification.md`; CDC owns that.

## Commit Instructions

If you edit source files, commit source changes first from the source checkout.
Use only the exact touched source paths. Example shape:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering add SKILL.md Makefile README.md AGENTS.md CLAUDE.md
git -C /Users/oubiwann/lab/billosys/ai-engineering commit -m "Implement Project04 Arc03 Slice02 compatibility decision" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- SKILL.md Makefile README.md AGENTS.md CLAUDE.md
```

Adjust the path list to only the source files you actually touched.

Then commit the planning close packet from the planning checkout with this
exact path scope:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/artifacts/top-level-skill-compatibility-decision.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/artifacts/compatibility-implementation-record.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/artifacts/validation-evidence-map.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/closing-report.md

git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit -m "Complete Project04 Arc03 Slice02" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/artifacts/top-level-skill-compatibility-decision.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/artifacts/compatibility-implementation-record.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/artifacts/validation-evidence-map.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/closing-report.md
```

If you made no source edits, say so in the close report and commit only the
planning close packet.
