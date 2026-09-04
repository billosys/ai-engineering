# CDC Verification: Slice 06 Project-Management Example Layout Reconciliation

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice06-project-management-example-layout-reconciliation
status: verified-closed
verified-by: CDC
verified-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source_commit_verified: df2c33e0d882aa89dbd42da3b87737a822903979
planning_close_packet_verified: 96d41b25b6c16f0559eedcc9adf8135fd9828b3f
planning_close_hash_follow_up_verified: 75c0801ca2fc3404274878f82ec109044ba90119
```

## Verdict

Slice06 is CDC-verified closed.

The source commit reconciled the project-management component layout with the
accepted architecture by moving:

- from `knowledge/project-management/guides/09-worked-example-odm.md`
- to `knowledge/project-management/examples/01-worked-example-odm.md`

The move is recorded by Git as a rename. The eight numbered
project-management guides and the `guides/PROJECT-MANAGEMENT.md` wayfinder
remain intact. The old worked-example path remains only in version-history
provenance text, not as a live source path or package entry.

## Independent Checks

- Confirmed the source checkout was clean before CDC planning edits.
- Confirmed the planning checkout was clean before CDC planning edits.
- Confirmed source commit `df2c33e0d882aa89dbd42da3b87737a822903979`
  includes both required co-author trailers.
- Confirmed planning commits `96d41b25b6c16f0559eedcc9adf8135fd9828b3f`
  and `75c0801ca2fc3404274878f82ec109044ba90119` include both required
  co-author trailers.
- Confirmed the source commit touched the expected project-management
  entrypoint, worked-example rename, wayfinder, version history, Makefile
  package list, and collaboration-framework package-history files.
- Confirmed the planning close packet supplied the four expected artifacts,
  the seven-row ledger, and the closing report. The follow-up planning commit
  records the close-packet hash where the first close packet had a pending
  marker.
- Re-ran all seven Slice06 ledger verifier commands or stronger equivalent
  checks.
- Re-ran touched-route local Markdown link validation: 6 checked files, 82
  local links checked, 0 missing.
- Re-ran `git diff --check`, `make check-skills`, `make collab-framework`, and
  `make check-package-paths`.
- Inspected `target/skills/collaboration-framework.zip` after a sequential
  rebuild and confirmed it contains
  `collaboration-framework/knowledge/project-management/examples/01-worked-example-odm.md`,
  omits the old worked-example guide path, and has 62 entries.

## Ledger Walk

| ID | CDC result | Evidence |
|----|------------|----------|
| F-1 | verified | Current project-management layout and the accepted target were compared in the Slice06 artifacts. |
| F-2 | verified | The worked example moved to `examples/01-worked-example-odm.md`; no exception was required. |
| F-3 | verified | The eight numbered project-management guides and the wayfinder remain present under `guides/`. |
| F-4 | verified | Project-management `SKILL.md`, wayfinder, version history, Makefile package route, and collaboration-framework package history were repaired; other scanned surfaces were no-op/dispositioned. |
| F-5 | verified | Source whitespace, skill-description, collaboration-framework package build, local-link, and full package-path validation passed with zero hard failures. |
| F-6 | verified | Rebuilt `collaboration-framework.zip` contains the accepted example path and does not contain `guides/09-worked-example-odm.md`. |
| F-7 | verified | Closing report records exact source and planning commits, explicit file lists, clean statuses, row walk, and Slice07 bubble-up. |

Rows: 7. Done: 7. Deferred: 0. No-op: 0.

## Bubble-Up to Arc08

Slice07 can proceed to the work-verification guide split. It should preserve
the post-Slice06 collaboration-framework package shape: 62 entries, with the
project-management worked example under
`knowledge/project-management/examples/01-worked-example-odm.md`.
