# Slice 02: Top-Level Compatibility Decision

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Decision artifact selects validated shim, replacement route, or explicit no-shim path and records rationale/re-entry | `rg -n "top-level SKILL.md|validated shim|replacement route|no-shim|selected path|rationale|re-entry condition|collaboration-framework|composer" artifacts/top-level-skill-compatibility-decision.md` | serious | slice-plan | open | | Gating decision before composer moves. |
| F-2 | Implementation record lists exact source files touched or no source edits, and preserves allowed source scope | `rg -n "source-files-edited:|source files touched|SKILL.md|Makefile|README.md|AGENTS.md|CLAUDE.md|docs/|knowledge/|templates/|protocols/ccdp|not touched|scope boundary" artifacts/compatibility-implementation-record.md` | serious | slice-plan | open | | Prevents broad source movement in the compatibility slice. |
| F-3 | Validation evidence map records source status/diff, make check-skills, make collab-framework, and route/package behavior for chosen path | `rg -n "validation evidence|status --short|diff --check|make check-skills|make collab-framework|collaboration-framework.zip|package root|route review|entrypoint" artifacts/validation-evidence-map.md` | serious | slice-plan | open | | Validates the selected compatibility path. |
| F-4 | Artifacts preserve Arc02/Arc03 ordering: top-level compatibility before composer moves, mechanical moves before prose rewrites, package-local repair before exceptions | `rg -n "before composer moves|mechanical moves before prose rewrites|package-local link repair before exceptions|not source-edit authorization beyond this slice|Arc04|Arc05" artifacts/*.md` | correctness-grade | slice-plan | open | | Keeps later move/rewrite/package work separated. |
| F-5 | Source checkout status is recorded and any source edits are committed separately or explicitly absent | `rg -n "source checkout|status --short|source commit|no source edits|source-files-edited: false|source-files-edited: true|explicit source scope" artifacts/*.md` | serious | slice-plan | open | | Supports Expedited Mode and source/planning commit separation. |
| F-6 | Closing report walks all six rows, states source/planning checkout status, and bubbles findings up to Arc03 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc03|silent-drop" closing-report.md` | serious | slice-plan | open | | Close-set document; do not create before evidence exists. |

## Closure

Slice is open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
