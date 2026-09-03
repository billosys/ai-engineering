# CC Prompt: Project04 Arc03 Slice04

You are working in Project04, Arc03, Slice04:
`arc03-directory-reorg/slice04-component-method-template-ownership-moves`.

Project04 is in Expedited Mode. Commit after your changes before CDC review.
Use explicit file lists for every `git add` and `git commit -- <paths>` command;
do not stage broad directories.

## Read First

Read these planning files before touching source:

- `project-plan.md`
- `ledger.md`
- `arc03-directory-reorg/arc-plan.md`
- `arc03-directory-reorg/ledger.md`
- `arc03-directory-reorg/slice04-component-method-template-ownership-moves/slice-plan.md`
- `arc03-directory-reorg/slice04-component-method-template-ownership-moves/ledger.md`
- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`
- `arc02-directory-contract/slice02-accepted-directory-contract/artifacts/accepted-target-directory-contract.md`
- `arc03-directory-reorg/slice03-mechanical-framework-source-moves/cdc-verification.md`

## Source Checkout

Use source checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Start by recording source status. The expected source tip includes:

- CC Slice03 source commit `99cebae1e98004164e4ea6735c4a68bc60c233da`
- CDC Slice03 compatibility repair commit `27cc255`

Do not edit the planning checkout until after your source commit is complete.

## Task

Mechanically place accepted Project02 component substrate, authorized method
material, and owner-local templates under their owning `knowledge/` roots while
preserving source prose and package behavior.

The ownership direction is:

- `knowledge/collaboration-framework/`: daily-driver composer/posture material
- `knowledge/engineering-methods/`: methodology, substrate, process, gates
- `knowledge/project-management/`: planning and close lifecycle
- `knowledge/work-verification/`: ledger/evidence discipline and template
- `knowledge/testing/`: coverage and validation-gate discipline
- `knowledge/code-auditing/`: diagnosis-only audit discipline
- `knowledge/agent-coordination/`: CC/CDC/operator and delegation material
- `knowledge/contribution-style/`: contribution prose and ticket template
- `knowledge/concept-card-method/`: reserved unless already-authorized live
  Project03/Project05 material exists in this checkout

Keep the move mechanical. Preserve original prose. If final guide decomposition
would require rewriting, preserve original file names under the owner root and
record the later decomposition as Arc04/Arc05 or later-component work.

Move owner-local templates when ownership is clear:

- `LEDGER-DISCIPLINE.md` belongs with `work-verification`
- `CONTRIBUTION-TICKET.md` belongs with `contribution-style`

Keep top-level `templates/GUIDE.md` in place unless you can prove a single
owning root. If it remains, record it as a cross-cutting support exception.

Do not move domain/tooling skill roots, Biome entrypoints, CCDP source,
`docs/ORIGINS.md`, or generated zips. Do not rewrite README or final public
skill vocabulary in this slice.

## Required Artifacts

Create these planning artifacts after the source commit:

- `arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/component-ownership-move-manifest.md`
- `arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/method-and-template-ownership-record.md`
- `arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/source-prose-preservation-evidence.md`
- `arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/validation-and-package-impact-evidence.md`

Then update:

- `arc03-directory-reorg/slice04-component-method-template-ownership-moves/ledger.md`
- `arc03-directory-reorg/slice04-component-method-template-ownership-moves/closing-report.md`

Do not create `cdc-verification.md`.

## Validation

Run the applicable source checks and record exact outcomes:

- source `git status --short`
- source `git diff --check`
- rename-aware source move review with `git diff --name-status --find-renames`
- source-prose preservation checks, including `cmp` where possible
- `make check-skills`
- `make collab-framework`
- `make check-package-paths`
- generated package inspection for affected package roots
- planning `git diff --check`

If package/list changes are required, update the exact package paths involved
and rerun the relevant package checks. If a persistent package-path exception
or accepted warning is needed, stop and record an operator gate instead of
adding a broad exception.

## Commit Instructions

Commit source first from `/Users/oubiwann/lab/billosys/ai-engineering`.

Use explicit file lists. The exact source file list depends on your mechanical
move manifest. Your commands must name every changed source path explicitly,
including moved-from/moved-to paths as applicable, such as:

```bash
git add <exact changed source file 1> <exact changed source file 2> ...
git commit -m "Complete Project04 Arc03 Slice04 source ownership moves" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- <exact changed source file 1> <exact changed source file 2> ...
```

Then commit the planning close packet from
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`.

Use this exact planning path list:

```bash
git add \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/component-ownership-move-manifest.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/method-and-template-ownership-record.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/source-prose-preservation-evidence.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/validation-and-package-impact-evidence.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/closing-report.md

git commit -m "Complete Project04 Arc03 Slice04" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/component-ownership-move-manifest.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/method-and-template-ownership-record.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/source-prose-preservation-evidence.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/artifacts/validation-and-package-impact-evidence.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice04-component-method-template-ownership-moves/closing-report.md
```

Final report should include source commit hash, planning commit hash, validation
summary, and any Slice05 bubble-up.
