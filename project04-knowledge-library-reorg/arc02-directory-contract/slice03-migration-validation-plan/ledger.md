# Slice 03: Migration Sequence and Validation Plan

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Migration sequence separates mechanical moves, compatibility shims, wrappers, package/list updates, link repair, exception handling, and prose rewrites | `rg -n "migration sequence|mechanical moves before prose rewrites|compatibility shim|wrapper|migration note|package/list update|package-local link repair|package-path exception|prose rewrite|docs/|knowledge/|templates/|protocols/ccdp|README|SKILL.md|AGENTS.md|CLAUDE.md|Makefile" artifacts/migration-sequence-plan.md` | serious | slice-plan | open | | Must make later Arc03 sequencing executable. |
| F-2 | Validation matrix maps accepted surfaces to source status, diff hygiene, skill/package/package-path/composer/CCDP checks, and generated package inspection | `rg -n "validation matrix|status --short|diff --check|make check-skills|make check-package-paths|make all|make collab-framework|make ccdp-package|make check-ccdp-package|package-local|generated package|AGENTS.md|CLAUDE.md" artifacts/validation-and-compatibility-matrix.md` | serious | slice-plan | open | | Must prepare later implementation gates. |
| F-3 | Package-path exception policy requires repair before exceptions and records owner, reason, validation, expiration, operator approval, and re-entry | `rg -n "package-path exception policy|repair before exception|package-local link|narrow|reason|validation command|expiration|no-expiration rationale|owner|operator approval|accepted warning|re-entry condition" artifacts/package-path-exception-policy.md` | serious | slice-plan | open | | Exceptions must be visible debt, not a way to hide broken links. |
| F-4 | Artifacts preserve Slice02 accepted defaults and explicit exception classes | `rg -n "knowledge/<component>|knowledge/collaboration-framework|top-level SKILL.md|validated shim|replacement route|no-shim|Biome|multi-entrypoint|selected-file|collaboration-framework|protocols/ccdp|CCDP remains separate" artifacts/*.md` | serious | slice-plan | open | | Carry Slice02 bubble-up into executable planning. |
| F-5 | Artifacts preserve source-edit boundary and route implementation/public vocabulary to later arcs | `rg -n "source-files-edited: false|not source-edit authorization|Arc03|implementation arc|source-edit slice|Arc05|public vocabulary|planning only|source checkout remains untouched" artifacts/*.md` | correctness-grade | slice-plan | open | | Planning only; source edits remain later-arc work. |
| F-6 | Closing report walks all six rows, states source checkout remains untouched, and bubbles usable findings up to Arc02 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout remains untouched|Bubble-Up to Arc02|silent-drop" closing-report.md` | serious | slice-plan | open | | Close-set document; do not create before evidence exists. |

## Closure

Slice remains open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
