# CDC Verification: Slice 07 Work-Verification Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice07-work-verification-guide-split
status: verified-closed
verified-by: CDC
verified-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source_commit_verified: 2a092d76090387a12e34d08e895084ee5389dbb2
planning_close_packet_verified: b71f07916184344fd529cb3f8c07755938e074f5
planning_close_hash_follow_up_verified: fa31b01ca8537ede9cbe23e51e7cc4e3254ad16d
```

## Verdict

Slice07 is CDC-verified closed.

The source commit split the work-verification component into five selective-load
guides:

- `knowledge/work-verification/guides/01-ledger-discipline.md`
- `knowledge/work-verification/guides/02-evidence-strength.md`
- `knowledge/work-verification/guides/03-row-closure.md`
- `knowledge/work-verification/guides/04-silent-drop-checks.md`
- `knowledge/work-verification/guides/05-independent-verification.md`

`knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` remains packaged
as the retained full protocol and copyable ledger-table support asset. The
focused guides are now the primary live routes for selective loading.

## Independent Checks

- Confirmed the source checkout was clean before CDC planning edits.
- Confirmed the planning checkout was clean before CDC planning edits.
- Confirmed source commit `2a092d76090387a12e34d08e895084ee5389dbb2`
  includes both required co-author trailers.
- Confirmed planning commits `b71f07916184344fd529cb3f8c07755938e074f5`
  and `fa31b01ca8537ede9cbe23e51e7cc4e3254ad16d` include both required
  co-author trailers.
- Confirmed the source commit touched the expected work-verification guide,
  retained-template, route-repair, Makefile package-list, component-history,
  public-doc, AGENTS, and release-note surfaces.
- Confirmed the work-verification component now has `SKILL.md`,
  `version-history.md`, five numbered guides, and retained
  `templates/LEDGER-DISCIPLINE.md`.
- Re-ran all eight Slice07 ledger verifier commands or stronger equivalent
  checks.
- Re-ran touched-route local Markdown link validation: 21 checked files, 178
  local links checked, 0 missing.
- Re-ran `git diff --check`, `make check-skills`, `make collab-framework`, and
  `make check-package-paths`.
- Inspected `target/skills/collaboration-framework.zip` after a sequential
  rebuild and confirmed it contains 68 entries, all five work-verification
  guides, and retained `templates/LEDGER-DISCIPLINE.md`.

## Ledger Walk

| ID | CDC result | Evidence |
|----|------------|----------|
| F-1 | verified | Current work-verification source, route, package, and history surfaces were inventoried in `artifacts/current-work-verification-surface-map.md`. |
| F-2 | verified | The five accepted numbered guides exist in source and are mapped in `artifacts/work-verification-split-map.md`. |
| F-3 | verified | The split map and guide scans preserve ledger format, evidence strengths, row closure, CC/CDC protocol, silent-drop checks, arc/project composition, and independent verification. |
| F-4 | verified | `artifacts/template-retention-disposition.md` records that `templates/LEDGER-DISCIPLINE.md` is retained as the full protocol/copyable-table support asset. |
| F-5 | verified | Work-verification, collaboration-framework, project-management, engineering-methods, public docs, AGENTS, release notes, and Makefile routes were repaired or explicitly dispositioned. |
| F-6 | verified | Source whitespace, skill-description, collaboration-framework package build, focused link, and full package-path validation passed with zero hard failures. |
| F-7 | verified | The generated package contains all five work-verification guides and the retained template, matching the recorded disposition. |
| F-8 | verified | Closing report records exact source and planning commits, explicit file lists, clean statuses, row walk, and Slice08 bubble-up. |

Rows: 8. Done: 8. Deferred: 0. No-op: 0.

## Bubble-Up to Arc08

Slice08 can proceed to the testing guide split. It should preserve the
post-Slice07 route pattern: focused guides are primary selective-load targets,
and any retained legacy prompt/template material must be explicitly
dispositioned as support material.
