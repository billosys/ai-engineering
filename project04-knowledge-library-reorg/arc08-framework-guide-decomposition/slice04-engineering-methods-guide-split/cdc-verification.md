# CDC Verification: Slice 04 Engineering-Methods Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice04-engineering-methods-guide-split
status: verified-closed
verified-by: CDC
verified-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source_commit_verified: 0ad843dfff6e01bdc68a566e9b8907ac76da88b6
planning_close_packet_verified: 7e392b81cebd5e6845b3dcca71a8786de61684c4
planning_close_hash_follow_up_verified: 61e25ca8208d578a64701a87e17358f02486c183
```

## Verdict

Slice04 is CDC-verified closed.

The source commit split the former engineering-methods monolith into the six
accepted numbered guides:

- `knowledge/engineering-methods/guides/01-engineering-methodology.md`
- `knowledge/engineering-methods/guides/02-knowledge-substrate.md`
- `knowledge/engineering-methods/guides/03-process-rigour.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/guides/05-component-boundary-analysis.md`
- `knowledge/engineering-methods/guides/06-source-package-release-gates.md`

The old `AI-ENGINEERING-METHODOLOGY.md` filename is no longer present as a live
source or package route. Remaining mentions are provenance/disposition mentions
inside sibling version-history files.

The engineering-methods component history now lives at
`knowledge/engineering-methods/version-history.md`. The former monolith's
embedded version history was reconciled into that sibling history file.

## Independent Checks

- Confirmed the source checkout was clean before CDC planning edits.
- Confirmed the planning checkout was clean before CDC planning edits.
- Confirmed source commit `0ad843dfff6e01bdc68a566e9b8907ac76da88b6`
  includes both required co-author trailers.
- Confirmed planning commits `7e392b81cebd5e6845b3dcca71a8786de61684c4`
  and `61e25ca8208d578a64701a87e17358f02486c183` include both required
  co-author trailers.
- Confirmed the source commit touched the expected engineering-methods split,
  route, package-list, public-doc, component-link, and sibling-history files.
- Confirmed the planning close packet supplied the four expected artifacts,
  the eight-row ledger, and the closing report. The follow-up planning commit
  records the close-packet hash where the first close packet had a pending
  marker.
- Re-ran all eight Slice04 ledger verifier commands or stronger equivalent
  checks.
- Re-ran touched-route local Markdown link validation: 21 checked files, 200
  local links checked, 0 missing.
- Re-ran `git diff --check`, `make check-skills`, `make collab-framework`, and
  `make check-package-paths`.
- Inspected `target/skills/collaboration-framework.zip` after a sequential
  rebuild and confirmed it contains the six numbered engineering-methods
  guides and `knowledge/engineering-methods/version-history.md`; the old
  monolith path is absent.

## Ledger Walk

| ID | CDC result | Evidence |
|----|------------|----------|
| F-1 | verified | The six accepted numbered engineering-methods guides exist; the old monolith path is absent as a live load target and retained only in version-history provenance/disposition text. |
| F-2 | verified | The split map, source guides, and sibling history preserve the monolith's major semantic sections while making methodology, substrate, process, routing, boundary, and release-gate material independently loadable. |
| F-3 | verified | `knowledge/engineering-methods/SKILL.md`, `knowledge/collaboration-framework/SKILL.md`, and `knowledge/collaboration-framework/guides/04-component-route-table.md` route to the six numbered guides and keep Slice02/Slice03 guardrails. |
| F-4 | verified | `knowledge/engineering-methods/version-history.md` exists as the sibling component history, with former monolith history reconciled there and no engineering-methods component history under `guides/`. |
| F-5 | verified | README/docs/AGENTS/SKILL/release-note references were repaired or dispositioned; remaining old filename mentions are provenance/disposition only. |
| F-6 | verified | Source whitespace, skill-description, collaboration-framework package build, local-link, and full package-path validation passed. |
| F-7 | verified | Rebuilt `collaboration-framework.zip` contains the six numbered guides and does not contain `guides/AI-ENGINEERING-METHODOLOGY.md`; package entry count was 56. |
| F-8 | verified | Closing report records exact source and planning commits, explicit file lists, clean statuses, row walk, and Slice05 bubble-up. |

Rows: 8. Done: 8. Deferred: 0. No-op: 0.

## Bubble-Up to Arc08

Slice05 can proceed to remaining framework component version-history
normalization for `work-verification`, `testing`, `code-auditing`,
`agent-coordination`, and `contribution-style`.

The project-level component layout plan also contains broader component guide
decomposition proposals for several of those components, including splitting
the old agent-coordination delegation policy into focused guides. Because the
operator flagged that broader vision-plan work for later review, Slice05 should
record those proposals as a deferred re-entry surface and should not silently
expand version-history normalization into guide-body splitting.
