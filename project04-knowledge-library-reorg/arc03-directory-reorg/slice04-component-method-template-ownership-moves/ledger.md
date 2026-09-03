# Slice 04: Component, Method, and Template Ownership Moves

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Component ownership move manifest maps moved substrate from transitional or old paths to accepted `knowledge/<component>/` roots | `rg -n "component ownership move manifest|knowledge/<component>|knowledge/collaboration-framework|knowledge/engineering-methods|knowledge/project-management|knowledge/work-verification|knowledge/testing|knowledge/code-auditing|knowledge/agent-coordination|knowledge/contribution-style|mechanical move" artifacts/component-ownership-move-manifest.md` | serious | slice-plan | open | | Exact component-root accounting. |
| F-2 | Method and template ownership record accounts for `concept-card-method`, owner-local templates, and top-level `templates/GUIDE.md` exception status | `rg -n "method and template ownership|concept-card-method|reserved|authorized live material|templates/GUIDE.md|cross-cutting support|LEDGER-DISCIPLINE.md|CONTRIBUTION-TICKET.md|owner-local template|exception" artifacts/method-and-template-ownership-record.md` | serious | slice-plan | open | | Prevents method and template ownership from being inferred silently. |
| F-3 | Source-prose preservation evidence distinguishes pure moves from required route/link/version edits and records rename-aware evidence | `rg -n "source-prose preservation|pure move|route/link update|version history|git diff --name-status --find-renames|byte-for-byte|cmp|line-level disclosure|no prose rewrite" artifacts/source-prose-preservation-evidence.md` | serious | slice-plan | open | | Keeps mechanical ownership moves from becoming prose rewrites. |
| F-4 | Validation and package-impact evidence records source hygiene, skill/package checks, generated package inspection, and package-path exception handling | `rg -n "validation and package impact|git status --short|git diff --check|make check-skills|make collab-framework|make check-package-paths|generated package inspection|package root|entrypoint|package-path-exceptions.tsv|generated zip not committed" artifacts/validation-and-package-impact-evidence.md` | serious | slice-plan | open | | Confirms package behavior after component ownership moves. |
| F-5 | Compatibility and scope evidence preserves top-level `SKILL.md`, `AGENTS.md`, `CLAUDE.md`, README, Biome, and CCDP boundaries after ownership moves | `rg -n "compatibility|top-level SKILL.md|AGENTS.md|CLAUDE.md|CLAUDE.md -> AGENTS.md|README.md|Biome|CCDP|Arc04|Arc05|route update|scope boundary" artifacts/*.md` | serious | slice-plan | open | | Protects edge cases and later arcs. |
| F-6 | Closing report walks all six rows, states source/planning checkout status, and bubbles findings up to Slice05 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc03|Slice05|package-local link|exception" closing-report.md` | serious | slice-plan | open | | Close-set document; do not create before evidence exists. |

## Closure

Slice remains open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
