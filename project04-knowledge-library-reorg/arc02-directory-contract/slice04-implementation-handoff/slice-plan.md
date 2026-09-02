# Slice 04: Arc02 Implementation Handoff

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice04-implementation-handoff
status: open
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
artifact-home: artifacts/
operating-mode: expedited
```

## Goal

Synthesize verified Arc02 evidence into an Arc03 implementation readiness
packet, ordered source-edit slice roadmap, and Arc02 decision summary.

This slice prepares the implementation handoff; it does not edit the source
checkout and does not open Arc03.

## Inputs

- `../arc-plan.md` and `../ledger.md`.
- `../slice01-decision-surface-inventory/cdc-verification.md`.
- `../slice02-accepted-directory-contract/cdc-verification.md`.
- `../slice03-migration-validation-plan/cdc-verification.md`.
- `../slice02-accepted-directory-contract/artifacts/accepted-target-directory-contract.md`.
- `../slice02-accepted-directory-contract/artifacts/source-package-root-contract.md`.
- `../slice02-accepted-directory-contract/artifacts/operator-decision-register.md`.
- `../slice03-migration-validation-plan/artifacts/migration-sequence-plan.md`.
- `../slice03-migration-validation-plan/artifacts/validation-and-compatibility-matrix.md`.
- `../slice03-migration-validation-plan/artifacts/package-path-exception-policy.md`.
- Arc01 close and synthesis artifacts as needed for provenance beneath the
  accepted Arc02 contract.

## In Scope

- Create `artifacts/arc03-readiness-packet.md`, summarizing the verified
  Slice01-Slice03 evidence, accepted directory/source/package contract,
  migration sequence, validation obligations, compatibility policy, operator
  gates, risks, and Arc03 entry conditions.
- Create `artifacts/source-edit-slice-roadmap.md`, proposing ordered Arc03
  source-edit slices that begin with preflight/source status, preserve
  mechanical moves before prose rewrites, handle compatibility shims and
  wrappers, repair package-local links before exceptions, and run the relevant
  validation gates after each source-edit slice.
- Create `artifacts/arc02-decision-summary.md`, summarizing accepted contract
  decisions, explicit exceptions, unresolved operator gates, re-entry
  conditions, and what Arc02 has and has not authorized.
- Preserve the source-edit boundary: Arc03 owns implementation, Arc04 owns
  README/end-user documentation prose, and Arc05 owns public skill vocabulary.
- Prepare Arc02 arc-close composition evidence without prematurely writing the
  arc closing report.

## Out of Scope

- Moving, deleting, renaming, or editing source checkout files.
- Editing source `README.md`, source `SKILL.md`, `docs/`, `knowledge/`,
  `templates/`, `protocols/`, `Makefile`, package-path exceptions, generated
  zips, or package contents.
- Closing Arc02, opening Arc03, or creating Arc03 source-edit slice packets.
- Writing final end-user documentation or final public skill vocabulary.
- Deciding persistent package-path exceptions without operator approval.

## Artifacts

Durable artifacts live under this slice's `artifacts/` directory:

- `artifacts/arc03-readiness-packet.md`
- `artifacts/source-edit-slice-roadmap.md`
- `artifacts/arc02-decision-summary.md`

## Verification Approach

The slice ledger uses grep-verifiable rows against the three artifacts and
closing report. CC should run every Verify command before reporting
proposed-done. CDC will independently rerun them before marking the slice
verified-closed.

## Exit Criteria

- The Arc03 readiness packet consumes verified Slice01-Slice03 evidence and
  clearly states the accepted contract, migration sequence, validation matrix,
  exception policy, risks, operator gates, and entry conditions.
- The source-edit roadmap orders preflight, mechanical moves, compatibility
  shims/wrappers, package/list/link updates, validation, and later prose work
  without authorizing source edits in this slice.
- The decision summary names accepted decisions, explicit exception classes,
  unresolved operator gates, and re-entry conditions.
- Arc03 implementation, Arc04 end-user docs, and Arc05 public vocabulary remain
  separate later-arc responsibilities.
- The source checkout remains untouched.

## Expedited Mode

CC must commit the proposed-done slice packet after his changes using explicit
file paths. CDC will then review, verify, update parent status, commit CDC
changes, and proceed to Arc02 close if this final Arc02 slice closes.
