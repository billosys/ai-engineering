# CC Prompt: Arc02 Slice01 Decision Surface Inventory

You are CC for Project04, Arc02, Slice01:
`arc02-directory-contract/slice01-decision-surface-inventory`.

Project04 is in Expedited Mode. After your changes, commit your proposed-done
slice packet before CDC review, using explicit file lists for both staging and
commit pathspecs. Do not use `git add .`, do not commit unrelated files, and do
not edit the source checkout.

## Required Reading

Read these files before writing artifacts:

- `project04-knowledge-library-reorg/project-plan.md`
- `project04-knowledge-library-reorg/ledger.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/arc-plan.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/ledger.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/slice-plan.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/ledger.md`
- `project04-knowledge-library-reorg/arc01-material-inventory/closing-report.md`
- `project04-knowledge-library-reorg/arc01-material-inventory/slice04-arc01-synthesis/artifacts/arc02-readiness-packet.md`
- `project04-knowledge-library-reorg/arc01-material-inventory/slice04-arc01-synthesis/artifacts/directory-contract-requirements.md`
- `project04-knowledge-library-reorg/arc01-material-inventory/slice04-arc01-synthesis/artifacts/arc01-synthesis-decision-register.md`

Use earlier Arc01 artifacts only as needed for source-backed detail beneath the
Slice04 synthesis.

## Assignment

Create the Slice01 artifact home and three artifacts:

- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/target-contract-decision-surface.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/source-root-option-matrix.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/compatibility-obligation-inventory.md`

The artifacts must make the Arc02 decision surface explicit without choosing
the final contract. Preserve these distinctions throughout:

- accepted fact vs working hypothesis;
- operator decision required vs planner recommendation;
- planned surface vs live source;
- source-edit risk vs source-edit authorization;
- skill kind vs topology;
- atomic vs composite vs bridge/integration vs application/task bundle.

Do not move, delete, rename, or edit source checkout files. Do not edit source
`README.md`, `SKILL.md`, `docs/`, `knowledge/`, `templates/`, `protocols/`,
`Makefile`, package-path exceptions, generated zips, or package contents.

## Ledger Work

Work against the slice ledger. When the three artifacts satisfy F-1 through
F-5, update the slice `ledger.md` rows to `done` with `attested:` evidence.
Then write `closing-report.md` with:

- row-by-row disposition for all six rows;
- the exact Verify commands run;
- source checkout status;
- artifact placement check;
- silent-drop check;
- Bubble-Up to Arc02;
- What Worked;
- Closure summary with `Rows: 6. Done: 6. Deferred: 0. No-op: 0.`

Do not create `cdc-verification.md`; CDC owns that.

## Verification Commands

Run every Verify command in the slice ledger from:

```bash
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory
```

Also run:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

The source checkout status command should return no output. If it does not,
report exactly what changed and do not alter the source checkout.

## Required Commit

After the slice packet is proposed-done, commit only the Slice01 files by
explicit path. Use this shape, adjusting only if you created exactly the same
logical files under the same slice:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/target-contract-decision-surface.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/source-root-option-matrix.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/compatibility-obligation-inventory.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/ledger.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/closing-report.md
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc02 Slice01" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- \
  project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/target-contract-decision-surface.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/source-root-option-matrix.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/compatibility-obligation-inventory.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/ledger.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/closing-report.md
```

Do not include the opening `slice-plan.md` or `cc-prompt.md` in your close
commit unless you intentionally edited them and report why.

## Report

Report:

- commit SHA;
- files created or updated;
- ledger rows done/deferred/no-op;
- verification commands and results;
- source checkout status;
- any Arc02 bubble-up findings or re-entry conditions.
