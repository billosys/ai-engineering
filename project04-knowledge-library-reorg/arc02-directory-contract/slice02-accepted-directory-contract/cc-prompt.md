# CC Prompt: Arc02 Slice02 Accepted Directory and Root Contract

You are CC for Project04, Arc02, Slice02:
`arc02-directory-contract/slice02-accepted-directory-contract`.

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
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/slice-plan.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/ledger.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/cdc-verification.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/target-contract-decision-surface.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/source-root-option-matrix.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/compatibility-obligation-inventory.md`

Use Arc01 close and Slice04 synthesis artifacts only when you need provenance
beneath the verified Slice01 decision surface.

## Assignment

Create the Slice02 artifact home and three artifacts:

- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/accepted-target-directory-contract.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/source-package-root-contract.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/operator-decision-register.md`

This slice should select a full evidence-backed contract, not merely restate
Slice01's options. Use conservative defaults from the verified evidence:

- `docs/` is user-facing explanation about repository materials.
- `knowledge/` is the default substrate home for skill source material,
  including current domain/tooling skills and planned framework/method skills
  where preservation constraints allow.
- `protocols/ccdp/` remains a separate protocol/package surface.
- Source roots and package roots are separate contract axes.
- Top-level compatibility surfaces such as `README.md`, `SKILL.md`,
  `AGENTS.md`, and `CLAUDE.md` remain top-level unless a later implementation
  arc explicitly changes them.
- Biome-style multi-entrypoint source roots and selected-file
  `collaboration-framework` packaging are first-class exceptions, not mistakes.

For every D-1 through D-12 decision from Slice01, record one disposition in
`operator-decision-register.md`: accepted, adjusted, rejected, or operator
decision required. If a choice still needs operator approval before source
edits, say so explicitly. Do not leave unlabeled unresolved decisions.

## Boundaries

Do not move, delete, rename, or edit source checkout files. Do not edit source
`README.md`, `SKILL.md`, `docs/`, `knowledge/`, `templates/`, `protocols/`,
`Makefile`, package-path exceptions, generated zips, or package contents.

Do not claim Project02 component roots or Project03 `concept-card-method` are
live source before implementation. Do not move CCDP into installable skill
packages. Do not finalize public taxonomy language for Arc05.

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
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract
```

Also run:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

The source checkout status command should return no output. If it does not,
report exactly what changed and do not alter the source checkout.

## Required Commit

After the slice packet is proposed-done, commit only the Slice02 files by
explicit path. Use this shape, adjusting only if you created exactly the same
logical files under the same slice:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/accepted-target-directory-contract.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/source-package-root-contract.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/operator-decision-register.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/ledger.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/closing-report.md
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc02 Slice02" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- \
  project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/accepted-target-directory-contract.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/source-package-root-contract.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/operator-decision-register.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/ledger.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/closing-report.md
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
