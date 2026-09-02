# CC Prompt: Arc03 Slice01 Preflight Source Status and Impact Map

You are CC for Project04, Arc03, Slice01:
`arc03-directory-reorg/slice01-preflight-source-status-impact-map`.

Project04 is in Expedited Mode. After your changes, commit your proposed-done
slice packet before CDC review, using explicit file lists for both staging and
commit pathspecs. Do not use `git add .`, do not commit unrelated files, and do
not edit the source checkout.

## Required Reading

Read these files before writing artifacts:

- `project04-knowledge-library-reorg/project-plan.md`
- `project04-knowledge-library-reorg/ledger.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/arc-plan.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/ledger.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/slice-plan.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/ledger.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/closing-report.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/cdc-verification.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/arc03-readiness-packet.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/source-edit-slice-roadmap.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/arc02-decision-summary.md`

Use earlier Arc02 artifacts only when you need contract or validation detail
beneath the handoff.

## Assignment

Create the Slice01 artifact home and three artifacts:

- `project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/artifacts/source-status-impact-map.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/artifacts/validation-command-inventory.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/artifacts/source-edit-authorization-register.md`

This is a preflight-only slice. Inspect the source checkout read-only and
record the baseline needed before later source-edit slices begin.

## Required Content

The source status impact map must include:

- source checkout path, branch/worktree identity, and `status --short`
  baseline;
- planning checkout path, branch/worktree identity, and planning status
  baseline;
- expected source surfaces for later Arc03 slices: `README.md`, `SKILL.md`,
  `docs/`, `knowledge/`, `templates/`, `protocols/ccdp`, `Makefile`,
  `package-path-exceptions.tsv`, generated zips, `AGENTS.md`, `CLAUDE.md`,
  package roots, and source roots;
- any existing source checkout dirt, if present, with a do-not-touch note.

The validation command inventory must map likely Arc03 source-edit surfaces to
commands and review gates, including source `status --short`, source
`diff --check`, `make help`, `make check-skills`, `make check-package-paths`,
`make all`, `make collab-framework`, `make ccdp-package`,
`make check-ccdp-package`, generated package inspection, package-local link
repair, and compatibility review.

The source-edit authorization register must distinguish:

- this preflight-only slice, which is authorized to edit planning files only;
- later source-edit slices, which are not authorized by this slice;
- operator gates for top-level `SKILL.md`, validated shim/replacement/no-shim
  decision, persistent package-path exceptions, accepted warnings, broad
  exceptions, and CCDP package-policy changes.

Preserve Arc02 ordering: top-level `SKILL.md` compatibility before composer
moves, mechanical moves before prose rewrites, package-local link repair before
exceptions, CCDP remains separate, Biome multi-entrypoint behavior remains
explicit, Arc04 owns end-user docs, and Arc05 owns public vocabulary.

## Boundaries

Do not move, delete, rename, or edit source checkout files. Do not edit source
`README.md`, `SKILL.md`, `docs/`, `knowledge/`, `templates/`, `protocols/`,
`Makefile`, package-path exceptions, generated zips, or package contents.

Do not select or implement the top-level `SKILL.md` shim/replacement/no-shim
path. Do not create source-edit commits. Do not write Arc04 end-user docs or
Arc05 public vocabulary.

## Ledger Work

Work against the slice ledger. When the three artifacts satisfy F-1 through
F-5, update the slice `ledger.md` rows to `done` with `attested:` evidence.
Then write `closing-report.md` with:

- row-by-row disposition for all six rows;
- the exact Verify commands run;
- source checkout status;
- artifact placement check;
- silent-drop check;
- Bubble-Up to Arc03;
- What Worked;
- Closure summary with `Rows: 6. Done: 6. Deferred: 0. No-op: 0.`

Do not create `cdc-verification.md`; CDC owns that.

## Verification Commands

Run every Verify command in the slice ledger from:

```bash
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map
```

Also run:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

The source checkout status command should return no output unless unrelated
source dirt already exists. If it does return output, record it exactly and do
not alter the source checkout.

## Required Commit

After the slice packet is proposed-done, commit only the Slice01 files by
explicit path. Use this shape, adjusting only if you created exactly the same
logical files under the same slice:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/artifacts/source-status-impact-map.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/artifacts/validation-command-inventory.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/artifacts/source-edit-authorization-register.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/closing-report.md
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc03 Slice01" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/artifacts/source-status-impact-map.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/artifacts/validation-command-inventory.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/artifacts/source-edit-authorization-register.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice01-preflight-source-status-impact-map/closing-report.md
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
- any Arc03 bubble-up findings or re-entry conditions.
