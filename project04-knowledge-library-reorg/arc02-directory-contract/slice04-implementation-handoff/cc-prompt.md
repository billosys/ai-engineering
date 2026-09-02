# CC Prompt: Arc02 Slice04 Implementation Handoff

You are CC for Project04, Arc02, Slice04:
`arc02-directory-contract/slice04-implementation-handoff`.

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
- `project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/slice-plan.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/ledger.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice01-decision-surface-inventory/cdc-verification.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/cdc-verification.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/cdc-verification.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/accepted-target-directory-contract.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/source-package-root-contract.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/operator-decision-register.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/migration-sequence-plan.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/validation-and-compatibility-matrix.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/package-path-exception-policy.md`

Use Arc01 close and synthesis artifacts only when you need provenance beneath
the verified Arc02 contract.

## Assignment

Create the Slice04 artifact home and three artifacts:

- `project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/arc03-readiness-packet.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/source-edit-slice-roadmap.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/arc02-decision-summary.md`

The artifacts should synthesize verified Arc02 evidence into an Arc03 handoff.
They should make the next implementation arc easy to open without reopening the
Arc02 directory-contract decisions.

## Required Content

The readiness packet must cover:

- verified Slice01, Slice02, and Slice03 inputs;
- accepted target directory contract and source/package root contract;
- migration sequence and validation matrix;
- package-path exception policy;
- Arc03 entry conditions, source-edit boundaries, validation gates, risks,
  operator gates, and re-entry conditions.

The source-edit slice roadmap must order likely Arc03 source-edit slices. Start
with a preflight/source-status slice, then preserve mechanical moves before
prose rewrites. Include compatibility shim or wrapper work, package/list
updates, package-local link repair, package-path exception handling, validation
gates, and later routing to Arc04 and Arc05 for end-user prose and public
vocabulary.

The decision summary must preserve accepted decisions and unresolved gates,
including:

- top-level `SKILL.md` remains unresolved until Arc03 chooses a validated shim,
  replacement route, or explicit no-shim implementation path;
- persistent package-path exceptions and accepted warnings require operator
  approval;
- `knowledge/biome/` remains a multi-entrypoint source root;
- selected-file `collaboration-framework` packaging remains an explicit
  transitional exception class until replaced or validated;
- CCDP remains separate under `protocols/ccdp/` and must not be added to
  installable skill packages;
- atomic/composite topology remains a separate axis from skill kind.

## Boundaries

Do not move, delete, rename, or edit source checkout files. Do not edit source
`README.md`, `SKILL.md`, `docs/`, `knowledge/`, `templates/`, `protocols/`,
`Makefile`, package-path exceptions, generated zips, or package contents.

Do not close Arc02, do not open Arc03, do not create Arc03 source-edit slice
packets, do not write final end-user docs, and do not finalize Arc05 public
vocabulary.

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
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff
```

Also run:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

The source checkout status command should return no output. If it does not,
report exactly what changed and do not alter the source checkout.

## Required Commit

After the slice packet is proposed-done, commit only the Slice04 files by
explicit path. Use this shape, adjusting only if you created exactly the same
logical files under the same slice:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/arc03-readiness-packet.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/source-edit-slice-roadmap.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/arc02-decision-summary.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/ledger.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/closing-report.md
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc02 Slice04" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- \
  project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/arc03-readiness-packet.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/source-edit-slice-roadmap.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/arc02-decision-summary.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/ledger.md \
  project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/closing-report.md
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
