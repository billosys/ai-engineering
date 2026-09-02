# Slice 03: Migration Sequence and Validation Plan

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice03-migration-validation-plan
status: open
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
artifact-home: artifacts/
operating-mode: expedited
```

## Goal

Turn the verified Slice02 accepted directory and source/package root contracts
into an executable migration sequence, validation and compatibility matrix, and
package-path exception policy for later implementation arcs.

This slice plans how the source edits should happen; it does not perform them.

## Inputs

- `../arc-plan.md` and `../ledger.md`.
- `../slice02-accepted-directory-contract/cdc-verification.md`.
- `../slice02-accepted-directory-contract/artifacts/accepted-target-directory-contract.md`.
- `../slice02-accepted-directory-contract/artifacts/source-package-root-contract.md`.
- `../slice02-accepted-directory-contract/artifacts/operator-decision-register.md`.
- `../slice01-decision-surface-inventory/artifacts/compatibility-obligation-inventory.md`.
- Arc01 and Arc02 earlier artifacts as needed for provenance and validation
  detail.

## In Scope

- Create `artifacts/migration-sequence-plan.md`, ordering source-edit work so
  mechanical moves, compatibility shims, wrapper/migration notes, package/list
  updates, package-local link repair, package-path exception handling, and
  public prose rewrites are not entangled.
- Create `artifacts/validation-and-compatibility-matrix.md`, mapping every
  accepted source/package/compatibility surface to required validation commands
  and source-checkout checks.
- Create `artifacts/package-path-exception-policy.md`, defining when package
  path exceptions are allowed, what evidence they require, what must be tried
  first, and which exceptions require operator approval.
- Preserve the accepted defaults from Slice02:
  `knowledge/<component>/` for Project02 component source roots,
  `knowledge/collaboration-framework/` as the target composer source root,
  top-level `SKILL.md` preserved until a validated shim/replacement/no-shim
  decision exists, Biome as a multi-entrypoint source root, and CCDP under
  `protocols/ccdp/`.
- Route final public vocabulary to Arc05 and source edits to Arc03.

## Out of Scope

- Moving, deleting, renaming, or editing source checkout files.
- Editing source `README.md`, source `SKILL.md`, `docs/`, `knowledge/`,
  `templates/`, `protocols/`, `Makefile`, package-path exceptions, generated
  zips, or package contents.
- Selecting a new target directory contract that contradicts Slice02 without
  recording a re-entry condition.
- Writing final end-user docs or Arc05 public vocabulary.
- Creating Arc03 implementation artifacts beyond inputs needed for Slice04's
  handoff.

## Artifacts

Durable artifacts live under this slice's `artifacts/` directory:

- `artifacts/migration-sequence-plan.md`
- `artifacts/validation-and-compatibility-matrix.md`
- `artifacts/package-path-exception-policy.md`

## Verification Approach

The slice ledger uses grep-verifiable rows against the three artifacts and
closing report. CC should run every Verify command before reporting
proposed-done. CDC will independently rerun them before marking the slice
verified-closed.

## Exit Criteria

- The migration sequence clearly separates mechanical moves, compatibility
  shims, wrapper/migration notes, package/list updates, link repair, exception
  handling, and prose rewrites.
- The validation matrix maps every affected surface to the required command or
  review gate, including source status, diff hygiene, `make check-skills`,
  `make check-package-paths`, `make all`, `make collab-framework`, CCDP gates,
  package-local link checks, generated package inspection, `AGENTS.md`, and
  `CLAUDE.md`.
- The package-path exception policy requires link repair before exceptions and
  names owner, reason, validation command, expiration or no-expiration
  rationale, operator approval, and re-entry condition for exceptions.
- Slice02 accepted defaults and explicit exception classes are preserved.
- No source-edit authorization is implied.
- The source checkout remains untouched.

## Expedited Mode

CC must commit the proposed-done slice packet after his changes using explicit
file paths. CDC will then review, verify, update parent status, commit CDC
changes, and open the next slice immediately if this slice closes.
