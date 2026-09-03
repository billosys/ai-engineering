# CC Prompt: Project04 Arc03 Slice05

You are working in Project04, Arc03, Slice05:
`arc03-directory-reorg/slice05-package-link-edge-reconciliation`.

Project04 is in Expedited Mode. Commit after your changes before CDC review.
Use explicit file lists for every `git add` and `git commit -- <paths>` command;
do not stage broad directories.

## Read First

Read these planning files before touching source:

- `project-plan.md`
- `ledger.md`
- `arc03-directory-reorg/arc-plan.md`
- `arc03-directory-reorg/ledger.md`
- `arc03-directory-reorg/slice05-package-link-edge-reconciliation/slice-plan.md`
- `arc03-directory-reorg/slice05-package-link-edge-reconciliation/ledger.md`
- `arc03-directory-reorg/slice04-component-method-template-ownership-moves/cdc-verification.md`
- `arc02-directory-contract/slice03-migration-validation-plan/artifacts/validation-and-compatibility-matrix.md`
- `arc02-directory-contract/slice03-migration-validation-plan/artifacts/package-path-exception-policy.md`

## Source Checkout

Use source checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Start by recording source status. The expected source tip includes Slice04
source commit `873a5502acef9c087cefd78d468cf6d123a27341`.

## Task

Reconcile package links, package lists, package-path exceptions, Biome
multi-entrypoint behavior, and CCDP separation after the accepted directory
moves.

The first rule for this slice is: repair package-local links before adding or
widening exceptions. Slice04 exposed affected-package hard failures during
implementation, and narrow package-local link repair cleared them. Use that as
the default pattern.

Inspect and reconcile:

- `Makefile`
- `SKILL.md`
- `package-path-exceptions.tsv`
- generated `collaboration-framework.zip`
- generated Biome package roots: `biome-js-linter.zip` and `biome-linter.zip`
- CCDP package/list surfaces under `protocols/ccdp/`
- package-local links and warning families reported by package-path checks

Preserve:

- top-level `SKILL.md` as the collaboration-framework package entrypoint unless
  validation proves a new compatibility decision is required;
- `AGENTS.md` and `CLAUDE.md -> AGENTS.md`;
- `README.md` for Arc04;
- public skill-kind and atomic/composite vocabulary for Arc05;
- `knowledge/biome/` as a multi-entrypoint source root;
- `protocols/ccdp/` as a separate protocol package surface;
- generated zips as ignored release artifacts.

If no source edits are required, record `source-files-edited: false` and do not
create a source commit. If source edits are required, commit only those exact
files before writing the planning close packet.

## Required Artifacts

Create these planning artifacts:

- `arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/package-link-repair-inventory.md`
- `arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/biome-and-ccdp-edge-case-validation.md`
- `arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/package-path-exception-register.md`
- `arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/source-change-and-validation-evidence.md`

Then update:

- `arc03-directory-reorg/slice05-package-link-edge-reconciliation/ledger.md`
- `arc03-directory-reorg/slice05-package-link-edge-reconciliation/closing-report.md`

Do not create `cdc-verification.md`.

## Validation

Run and record exact outcomes:

- source `git status --short --untracked-files=all`
- source `git diff --check`
- `make check-skills`
- `make collab-framework`
- `make check-package-paths`
- `make all`
- generated package inspection for affected package roots
- package-path exception review
- CCDP package/list validation as applicable from the Makefile
- planning `git diff --check`

If a persistent package-path exception or accepted warning needs operator
approval, stop and record the gate instead of silently broadening the exception
surface.

## Commit Instructions

If source files change, commit source first from
`/Users/oubiwann/lab/billosys/ai-engineering`, using explicit file lists:

```bash
git add <exact changed source file 1> <exact changed source file 2> ...
git commit -m "Complete Project04 Arc03 Slice05 source reconciliation" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- <exact changed source file 1> <exact changed source file 2> ...
```

Then commit the planning close packet from
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning` with this
exact planning path list:

```bash
git add \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/package-link-repair-inventory.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/biome-and-ccdp-edge-case-validation.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/package-path-exception-register.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/source-change-and-validation-evidence.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/closing-report.md

git commit -m "Complete Project04 Arc03 Slice05" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/package-link-repair-inventory.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/biome-and-ccdp-edge-case-validation.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/package-path-exception-register.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/artifacts/source-change-and-validation-evidence.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice05-package-link-edge-reconciliation/closing-report.md
```

Final report should include source commit hash if any, planning commit hash,
validation summary, and Slice06 bubble-up.
