# Slice 03: CCDP Package Freshness and Protocol Validation

```yaml
project: project04-knowledge-library-reorg
arc: arc06-validation-release
slice: slice03-ccdp-package-validation
status: verified-closed
opened-by: CDC
opened-on: 2026-09-03
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: optional-ccdp-repair
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Resolve the Arc06 CCDP package freshness blocker and validate CCDP as a
standalone protocol package after Project04's final layout and wording work.

## Scope

In scope:

- Source and planning checkout cleanliness.
- Reproducing the current CCDP package freshness failure.
- Refreshing `protocols/ccdp/composite-cognition-dispatch-protocol.md` with
  `make -C protocols/ccdp ccdp-rfc` if the assembled document is stale.
- Narrow CCDP package/freshness repairs under `protocols/ccdp/**`, the source
  `Makefile` CCDP targets, or `scripts/check-ccdp-package` only if evidence
  shows the freshness check or package validator is defective.
- `make ccdp-package`.
- `make check-ccdp-package`.
- Inspection of generated `ccdp.zip` as a protocol package.
- Confirmation that CCDP remains separate from installable skill packages.
- Final source/package checks needed after CCDP repair.

Out of scope:

- Repackaging CCDP as an installable skill.
- Editing installable skill package roots or generated installable skill zips.
- Reopening Arc02 directory contract, Arc03 source moves, Arc04 docs
  decomposition, Arc05 vocabulary decisions, or Slice02 installability
  findings.
- Implementing `concept-card-method`.
- Broad CCDP prose rewrites unrelated to assembled-spec freshness or package
  validation.
- Committing generated `ccdp.zip` or `build/` artifacts.
- Closing Arc06 or Project04.

## Expected Artifacts

- `artifacts/ccdp-freshness-repair-report.md`
- `artifacts/ccdp-package-validation-report.md`
- `artifacts/protocol-package-separation-report.md`
- `artifacts/source-change-and-generated-artifact-report.md`
- `artifacts/release-readiness-handoff.md`

## Verification Approach

CC should first reproduce the current CCDP package failure. If the failure is
the known stale assembled spec, run `make -C protocols/ccdp ccdp-rfc` and
commit the refreshed source file first with an explicit path list. If evidence
shows a different CCDP package/freshness defect, make only the narrow
authorized repair and record why.

If the operator explicitly decides to accept the stale CCDP package state
instead of repairing it, record that disposition. Otherwise, the expected path
is repair and green CCDP package validation.

Required validation includes:

- source `git status --short --untracked-files=all` before work;
- source `git diff --check`;
- reproduce `make ccdp-package` before repair or explain why already green;
- `make -C protocols/ccdp ccdp-rfc` if stale assembled output is present;
- inspect source diff for authorized CCDP files only;
- `make ccdp-package`;
- `make check-ccdp-package`;
- inspect generated `ccdp.zip` root and expected protocol package contents;
- `make check-skills`;
- `make check-package-paths`;
- generated artifact handling, confirming `ccdp.zip`, installable zips, and
  `build/` remain ignored and untracked unless a separate release process
  explicitly asks otherwise;
- planning `git diff --check`;
- all six Slice03 ledger verifier commands;
- final source and planning `git status --short --untracked-files=all`.

## Exit Criteria

- CCDP freshness is repaired or explicitly accepted with operator disposition.
- `make ccdp-package` and `make check-ccdp-package` are green, unless the
  operator explicitly accepts a weaker final disposition.
- `ccdp.zip` inspection confirms CCDP is a protocol package with expected
  protocol contents, not an installable skill package.
- Any source commit is limited to authorized CCDP/package-check files and uses
  the required trailers.
- Generated `ccdp.zip`, installable zips, and `build/` outputs are not
  committed.
- Source/package validation remains green after CCDP repair or disposition.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc06.

## CDC Close

Verified-closed on 2026-09-04. CDC reproduced all six ledger rows, checked
CC's source and planning commit scopes and required trailers, reran CCDP
package validation, inspected `ccdp.zip`, and confirmed the former CCDP
freshness blocker is resolved.
