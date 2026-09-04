# CDC Verification: Slice 03 Collaboration-Framework Posture Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice03-collaboration-framework-posture-split
status: verified-closed
verified-by: CDC
verified-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source_commit_verified: e7ba785bf8c48ef061f69f9d90d176030b62dfc4
planning_close_packet_verified: 5de33d7fcd49d6de80737f730d3e92f69ea4089b
planning_close_hash_follow_up_verified: 00855d161d264534c25a673bd9c2b5eeb0cf70a4
```

## Verdict

Slice03 is CDC-verified closed.

The source commit split the former collaboration-framework posture monolith
into the four operator-approved numbered guides:

- `knowledge/collaboration-framework/guides/01-posture-and-ethics.md`
- `knowledge/collaboration-framework/guides/02-structural-pulls.md`
- `knowledge/collaboration-framework/guides/03-collaborative-rights.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`

The old `AI-CONSTITUTION-SUPPLEMENT.md` filename is no longer present as a
live source or package route. Remaining mentions are provenance/disposition
mentions inside the split guides and sibling history.

The collaboration-framework component history now lives at
`knowledge/collaboration-framework/version-history.md`. The route-table guide
contains only a pointer back to that sibling history, not a new guide-local
component history.

## Independent Checks

- Confirmed the source checkout was clean before CDC planning edits.
- Confirmed the planning checkout was clean before CDC planning edits.
- Confirmed source commit `e7ba785bf8c48ef061f69f9d90d176030b62dfc4`
  includes both required co-author trailers.
- Confirmed planning commits `5de33d7fcd49d6de80737f730d3e92f69ea4089b`
  and `00855d161d264534c25a673bd9c2b5eeb0cf70a4` include both required
  co-author trailers.
- Confirmed the source commit touched the expected collaboration-framework
  split, route, package-list, public-doc, methodology-link, and sibling-history
  files.
- Confirmed the planning close packet supplied the four expected artifacts,
  the eight-row ledger, and the closing report. The follow-up planning commit
  records the close-packet hash where the first close packet had a pending
  marker.
- Re-ran all eight Slice03 ledger verifier commands or stronger equivalent
  checks.
- Re-ran touched-route local Markdown link validation: 9 checked files, 98
  local links checked, 0 missing.
- Re-ran `git diff --check`, `make check-skills`, `make collab-framework`, and
  `make check-package-paths`.
- Inspected `target/skills/collaboration-framework.zip` after a sequential
  rebuild and confirmed it contains the package-root `SKILL.md`, the four
  numbered posture guides, and `knowledge/collaboration-framework/version-history.md`;
  the old monolith path is absent.

## Ledger Walk

| ID | CDC result | Evidence |
|----|------------|----------|
| F-1 | verified | The four approved numbered posture guides exist; the old monolith path is absent as a live load target and retained only in provenance/disposition text. |
| F-2 | verified | The split map and source guides preserve the monolith's main semantic sections while making posture, structural-pull, rights, and route-table material independently loadable. |
| F-3 | verified | `knowledge/collaboration-framework/SKILL.md` routes to the four numbered guides and keeps the Slice02 Expedited Mode guardrail language. |
| F-4 | verified | `knowledge/collaboration-framework/version-history.md` exists as the sibling component history, with former supplement history reconciled there. |
| F-5 | verified | README/docs/AGENTS/SKILL/release-note references were repaired or dispositioned; remaining old filename mentions are provenance/disposition only. |
| F-6 | verified | Source whitespace, skill-description, collaboration-framework package build, local-link, and full package-path validation passed. |
| F-7 | verified | Rebuilt `collaboration-framework.zip` contains the four numbered guides and does not contain `guides/AI-CONSTITUTION-SUPPLEMENT.md`. |
| F-8 | verified | Closing report records exact source and planning commits, explicit file lists, clean statuses, row walk, and Slice04 bubble-up. |

Rows: 8. Done: 8. Deferred: 0. No-op: 0.

## Bubble-Up to Arc08

Slice04 can proceed to the engineering-methods guide split. It must preserve
the Slice02 Expedited Mode guardrails and the Slice03 collaboration-framework
posture routes while replacing the old engineering-methods monolith route with
the six accepted numbered guides and a sibling engineering-methods
`version-history.md`.
