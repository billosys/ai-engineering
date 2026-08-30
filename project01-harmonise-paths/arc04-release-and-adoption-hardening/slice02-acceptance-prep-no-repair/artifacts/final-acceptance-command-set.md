# Final Acceptance Command Set

Purpose: exact command set for Arc 04 Slice 03 and Project 01 close.

Run from `/Users/oubiwann/lab/billosys/ai-engineering`.

## Source Checkout Commands

1. `git status --short --branch --untracked-files=all`
   - Expected: no tracked source changes.
   - Current acceptable branch line: `## main...origin/main [ahead 3]`.
2. `make help`
   - Expected: exits 0.
   - Expected discoverability: skill bundle targets, `make all`,
     `make install`, `make check-package-paths`, `make ccdp`,
     `make ccdp-package`, and `make check-ccdp-package`.
3. `make check-package-paths`
   - Expected: exits 0.
   - Expected summary counts:
     - zips scanned: 12
     - Markdown files scanned: 171
     - hard failures: 0
     - warnings: 295
     - explicit exceptions: 3
     - skipped external URLs: 656
4. `make check-ccdp-package`
   - Expected: exits 0.
   - Expected summary counts:
     - Markdown files scanned: 42
     - package references checked: 14
     - protocol syntax skipped: 91
     - external URLs skipped: 4
     - shape errors: 0
     - README errors: 0
     - Markdown path failures: 0
   - Expected behavior: extracted-package rebuild succeeds and matches the
     packaged assembled spec.
5. `scripts/check-package-paths --check-exceptions-only`
   - Expected: exits 0.
   - Expected output: `exception schema ok: package-path-exceptions.tsv`.
6. `make all`
   - Expected: exits 0 and builds all per-domain skill zips plus
     `collaboration-framework.zip`.
7. `make ccdp-package`
   - Expected: exits 0.
   - Expected package shape: `ccdp.zip` with one `ccdp/` root and 122 entries.
8. `make ccdp`
   - Expected: exits 0 and does not create tracked assembled-spec drift.
9. `rg -n "source clone|zip|unzipped|install|package root|repo-only|provenance|check-package-paths|check-ccdp-package|ccdp.zip|protocol package" README.md Makefile package-path-exceptions.tsv protocols/ccdp/README.md scripts/check-package-paths scripts/check-ccdp-package`
   - Expected: exits 0 with matches proving workflow, package, provenance, and
     checker language is visible in the release/adoption surface.
10. `git diff --check`
    - Expected: exits 0.
11. `git status --short --branch --untracked-files=all`
    - Expected: no tracked source changes after all build/check commands.

## Planning Worktree Commands

Run from `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`.

1. `git diff --check`
   - Expected: exits 0.
2. `git diff --cached --check`
   - Expected: exits 0 when Slice 03 or project-close artifacts are staged.
3. `find project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/artifacts -maxdepth 2 -type f -print`
   - Expected: all durable Slice 03 artifacts live under its `artifacts/`
     directory.
4. `test -f project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/closing-report.md`
   - Expected: exits 0.
5. `rg -n "A-2|A-3|A-4|A-5|A-6|P-2|P-3|P-4|P-6|Artifacts|Bubble-up to Project 01|Project 01 close" project01-harmonise-paths/arc04-release-and-adoption-hardening/slice03-project-close-readiness/closing-report.md`
   - Expected: exits 0 and proves the close report walks the rows needed for
     Arc 04/project-close readiness.

## Failure Conditions

Any of these should stop close-readiness and route to repair:

- a hard failure from `make check-package-paths`;
- any CCDP shape, README, Markdown path, or extracted rebuild failure;
- invalid package-path exception schema;
- tracked source drift after `make ccdp` or package builds;
- missing release-surface grep evidence for one of the required workflows;
- missing Slice 03 artifacts or row-walk evidence.
