# CDC Verification: Slice 08 Testing Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice08-testing-guide-split
status: verified-closed
verified-by: CDC
verified-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source_commit_verified: 120c2ceaf26ca656068d9f2ec34c978eefaf04a5
planning_close_packet_verified: 6308c2f7408f3439fa5f8f41f52680232a130385
planning_close_hash_follow_up_verified: 7460153ecb1a8df7e3b34ebdeba3f18370088ec8
```

## Verdict

Slice08 is CDC-verified closed.

The source commit split the testing component into three selective-load guides:

- `knowledge/testing/guides/01-testing-discipline.md`
- `knowledge/testing/guides/02-coverage-hardening.md`
- `knowledge/testing/guides/03-validation-gates.md`

The old `knowledge/testing/guides/CODE-COVERAGE.md` path was preserved by Git
history as a rename to `knowledge/testing/guides/02-coverage-hardening.md`.
No old-path live package entry remains.

## Independent Checks

- Confirmed the source checkout was clean before CDC planning edits.
- Confirmed the planning checkout was clean before CDC planning edits.
- Confirmed source commit `120c2ceaf26ca656068d9f2ec34c978eefaf04a5`
  includes both required co-author trailers.
- Confirmed planning commits `6308c2f7408f3439fa5f8f41f52680232a130385`
  and `7460153ecb1a8df7e3b34ebdeba3f18370088ec8` include both required
  co-author trailers.
- Confirmed the source commit touched the expected testing guide, route-repair,
  Makefile package-list, component-history, public-doc, AGENTS, and release-note
  surfaces.
- Confirmed the testing component now has `SKILL.md`, `version-history.md`, and
  the three accepted numbered guides.
- Re-ran all eight Slice08 ledger verifier commands or stronger equivalent
  checks.
- Re-ran touched-route local Markdown link validation: 10 checked files, 116
  local links checked, 0 missing.
- Re-ran `git diff --check`, `make check-skills`, `make collab-framework`, and
  `make check-package-paths`.
- Inspected `target/skills/collaboration-framework.zip` after a sequential
  rebuild and confirmed it contains 70 entries, all three testing guides, and
  no old `CODE-COVERAGE.md` package path.

## Ledger Walk

| ID | CDC result | Evidence |
|----|------------|----------|
| F-1 | verified | Current testing source, route, package, and history surfaces were inventoried in `artifacts/current-testing-surface-map.md`. |
| F-2 | verified | The three accepted numbered guides exist in source and are mapped in `artifacts/testing-split-map.md`. |
| F-3 | verified | The split map and guide scans preserve testing discipline, hard 95%+ coverage work, warnings/lint/format pressure, tests-must-pass, root-cause repair, progress tracking, and validation-gate routing. |
| F-4 | verified | `artifacts/legacy-code-coverage-disposition.md` records the `git mv` rename from `CODE-COVERAGE.md` to `02-coverage-hardening.md` and old package-entry absence. |
| F-5 | verified | Testing, collaboration-framework, engineering-methods, public docs, AGENTS, release notes, and Makefile routes were repaired or explicitly dispositioned; project-management and work-verification were no-op. |
| F-6 | verified | Source whitespace, skill-description, collaboration-framework package build, focused link, and full package-path validation passed with zero hard failures. |
| F-7 | verified | The generated package contains all three testing guides and omits the old `CODE-COVERAGE.md` path, matching the recorded disposition. |
| F-8 | verified | Closing report records exact source and planning commits, explicit file lists, clean statuses, row walk, and Slice09 bubble-up. |

Rows: 8. Done: 8. Deferred: 0. No-op: 0.

## Bubble-Up to Arc08

Slice09 can proceed to the code-auditing guide split. It should preserve the
post-Slice08 route pattern: focused guides are primary selective-load targets,
and any retained legacy prompt/template material must be explicitly
dispositioned as support material.
