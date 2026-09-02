# CC Prompt: Arc02 Slice03 Migration Sequence and Validation Plan

You are CC for Project04, Arc02, Slice03:
`arc02-directory-contract/slice03-migration-validation-plan`.

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
- `project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/slice-plan.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/ledger.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/cdc-verification.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/accepted-target-directory-contract.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/source-package-root-contract.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/operator-decision-register.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/artifacts/compatibility-obligation-inventory.md`

Use earlier Arc01/Arc02 artifacts only when you need provenance beneath the
verified Slice02 accepted contract.

## Assignment

Create the Slice03 artifact home and three artifacts:

- `project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/migration-sequence-plan.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/validation-and-compatibility-matrix.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/package-path-exception-policy.md`

The artifacts should make the accepted Slice02 contract executable for later
Arc03 implementation slices without performing any source edits. Preserve these
Slice02 defaults and exceptions:

- `knowledge/<component>/` is the default Project02 component source-root
  family.
- `knowledge/collaboration-framework/` is the target composer source root when
  the composer moves from top-level selected-file packaging.
- Top-level `SKILL.md` is preserved until a validated shim, replacement route,
  or explicit no-shim path is chosen for implementation.
- Selected-file `collaboration-framework` packaging is a transitional
  exception class.
- `knowledge/biome/` is a first-class multi-entrypoint source root.
- `protocols/ccdp/` remains a separate protocol/package surface and must not
  be added to installable skill packages.
- Package-local links are repaired before package-path exceptions are added.
- Persistent package-path exceptions require operator approval.

## Boundaries

Do not move, delete, rename, or edit source checkout files. Do not edit source
`README.md`, `SKILL.md`, `docs/`, `knowledge/`, `templates/`, `protocols/`,
`Makefile`, package-path exceptions, generated zips, or package contents.

Do not write final end-user docs, do not finalize Arc05 public vocabulary, and
do not open Arc03 implementation. This slice plans implementation order and
validation gates only.

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
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan
```

Also run:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

The source checkout status command should return no output. If it does not,
report exactly what changed and do not alter the source checkout.

## Required Commit

After the slice packet is proposed-done, commit only the Slice03 files by
explicit path. Use this shape, adjusting only if you created exactly the same
logical files under the same slice:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/migration-sequence-plan.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/validation-and-compatibility-matrix.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/package-path-exception-policy.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/ledger.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/closing-report.md
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc02 Slice03" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- \
  project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/migration-sequence-plan.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/validation-and-compatibility-matrix.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/package-path-exception-policy.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/ledger.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/closing-report.md
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
