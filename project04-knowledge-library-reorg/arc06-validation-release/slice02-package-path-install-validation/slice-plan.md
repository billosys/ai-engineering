# Slice 02: Package, Path, and Install Validation

```yaml
project: project04-knowledge-library-reorg
arc: arc06-validation-release
slice: slice02-package-path-install-validation
status: verified-closed
opened-by: CDC
opened-on: 2026-09-03
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: optional-narrow-repair
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Validate the final installable skill package path after Project04's
docs/knowledge reorganization: source checks, package-path checks, generated
package inspection, and isolated install smoke testing.

## Scope

In scope:

- Source and planning checkout cleanliness.
- README/docs/SKILL local link validation if package/install evidence depends
  on these public routes.
- `make check-skills`.
- `make check-package-paths`.
- `make all`.
- Generated installable skill zip root and entrypoint inspection.
- `make install` into an isolated temporary `INSTALL_DIR`.
- Inspection of installed skill roots and expected `SKILL*.md` entrypoints.
- Warning-only package-path disposition for release readiness.
- Narrow package/path/install source repairs if validation exposes a defect.

Out of scope:

- Editing `protocols/ccdp/**`.
- Refreshing CCDP assembled protocol output.
- Treating `ccdp.zip` as an installable skill package.
- Implementing `concept-card-method`.
- Reopening Arc02 directory contract, Arc03 source moves, Arc04 docs
  decomposition, or Arc05 vocabulary decisions.
- Committing generated zips or `build/` artifacts.
- Closing Arc06 or Project04.

## Expected Artifacts

- `artifacts/package-path-build-validation-report.md`
- `artifacts/generated-package-inspection-report.md`
- `artifacts/isolated-install-smoke-report.md`
- `artifacts/package-warning-disposition.md`
- `artifacts/slice03-ccdp-readiness-handoff.md`

## Verification Approach

CC should start read-only. If `make check-package-paths`, `make all`,
generated package inspection, or isolated install smoke testing exposes a
package/path/install defect, make only the narrow repair authorized by this
slice and commit the source edit first with an explicit file list. If no
source repair is needed, create no source commit and say so explicitly.

Required validation includes:

- source `git status --short --untracked-files=all` before work;
- source `git diff --check`;
- README/docs/SKILL local-link validation;
- `make check-skills`;
- `make check-package-paths`;
- `make all`;
- generated installable skill package inspection for the 12 expected
  installable skill zips;
- isolated install smoke test using a temporary `INSTALL_DIR`;
- installed skill root and `SKILL*.md` entrypoint inspection;
- generated zip/build artifact handling, confirming ignored outputs are not
  committed;
- CCDP handoff confirmation that `protocols/ccdp/**` and `ccdp.zip` remain
  outside Slice02 repair scope;
- planning `git diff --check`;
- all six Slice02 ledger verifier commands;
- final source and planning `git status --short --untracked-files=all`.

## Exit Criteria

- Package-path/build validation is green for installable skill packages, with
  hard failures: 0.
- Generated package inspection confirms the expected roots and entrypoints for
  all installable skill zips.
- Isolated install smoke testing proves the installable skill set unpacks into
  the expected temporary install directory with expected entrypoints.
- Package-path warnings are explicitly dispositioned for release readiness.
- CCDP package freshness remains routed to Slice03, with no unauthorized
  protocol edits or `ccdp.zip` acceptance in Slice02.
- Source and planning commits, if any, use explicit file lists and required
  trailers.
- Source and planning worktrees finish clean.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc06.

## CDC Close

Verified-closed on 2026-09-03. CDC reproduced all six ledger rows, checked
CC's planning commit scope and required trailers, reran source/package/link
validation, reran generated package inspection, and reproduced isolated install
smoke in `/private/tmp/ai-engineering-install-cdc.9zAHUG`.
