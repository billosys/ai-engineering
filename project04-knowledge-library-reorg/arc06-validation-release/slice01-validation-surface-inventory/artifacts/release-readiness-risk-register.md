# release-readiness risk register

## Summary

Arc06 is validation/release-readiness work. Most installable skill validation
surfaces are green now, but final release readiness is not complete while CCDP
package freshness remains unresolved and install smoke testing has not yet been
run in an isolated directory.

## Risks

| ID | Risk | Type | Current evidence | Readiness effect | Next owner |
| --- | --- | --- | --- | --- | --- |
| R-1 | CCDP assembled spec is stale | blocker | `make ccdp-package` and `make check-ccdp-package` fail with `protocols/ccdp/composite-cognition-dispatch-protocol.md is stale` | blocks final CCDP package validation and Arc06 close unless repaired or explicitly accepted | Slice03 |
| R-2 | Temporary install smoke test has not yet run | acceptance prerequisite | Slice01 produced command plan only | blocks final installability claim until run | Slice02 |
| R-3 | `make check-package-paths` warning-only findings remain visible | warning | command exits 0 with hard failures: 0 and warnings for JavaScript/Deno shorthand, repo-only/provenance references, source-clone references, example paths, and parser false positives | does not block package-path gate now, but should be reviewed for final release notes or acceptance | Slice02 / Slice04 |
| R-4 | Existing ignored `ccdp.zip` may be stale relative to source | warning/blocker if used | `ccdp.zip` exists as ignored output, but current `make ccdp-package` cannot refresh it | do not treat existing `ccdp.zip` as current release evidence | Slice03 |
| R-5 | Generated installable skill zips are ignored outputs | no-op confirmation | `git status --ignored -- '*.zip' build` shows zips ignored; `git ls-files '*.zip'` is empty | generated zips are not committed unless release process explicitly asks | Slice04 |
| R-6 | Operator acceptance remains open | acceptance prerequisite | Arc06 Slice04 is planned for release readiness and operator acceptance | Project04 cannot close until final acceptance evidence is reconciled | Slice04 |

## Current Green Gates

- source `git status --short --untracked-files=all`: clean.
- planning `git status --short --untracked-files=all`: clean before Slice01
  edits.
- source `git diff --check`: pass.
- planning `git diff --check`: pass before Slice01 edits.
- README/docs/SKILL local link validation: 104 checked, missing: 0.
- route scan over README/docs/SKILL: pass with expected route references.
- `make check-skills`: pass.
- `make check-package-paths`: pass with hard failures: 0.
- `make all`: pass.
- generated installable package inspection: pass for all twelve installable
  skill packages.

## Blockers

- blocker: CCDP freshness remains unresolved.

## Warnings

- warning: package-path warning-only output remains visible.
- warning: existing ignored `ccdp.zip` must not be used as final evidence until
  `make ccdp-package` refreshes it successfully.

## No-Op Confirmations

- no-op: Slice01 made no source edits.
- no-op: Slice01 did not repair CCDP.
- no-op: Slice01 did not run default `make install` against
  `~/.agents/skills`.
- no-op: Slice01 did not stage or commit generated zips.

## Acceptance Prerequisites

- Slice02 must run package/path/install validation, including isolated
  `INSTALL_DIR` smoke testing.
- Slice03 must repair or explicitly disposition CCDP package freshness.
- Slice04 must reconcile operator acceptance against README/docs, skill
  package, install, CCDP, source checkout, and planning checkout evidence.
