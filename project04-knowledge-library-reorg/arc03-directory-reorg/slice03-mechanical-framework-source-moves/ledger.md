# Slice 03: Mechanical Framework Source Moves

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Mechanical move manifest maps current collaboration-framework payload files from old `docs/`/`templates/` paths to `knowledge/collaboration-framework/` target paths | `rg -n "mechanical move manifest|docs/AI-CONSTITUTION-SUPPLEMENT.md|docs/AI-ENGINEERING-METHODOLOGY.md|docs/PROJECT-MANAGEMENT.md|docs/pm/|docs/CODE-AUDIT.md|docs/CODE-COVERAGE.md|docs/SUBAGENT-DELEGATION-POLICY.md|docs/CONTRIBUTION-STYLE.md|templates/LEDGER-DISCIPLINE.md|templates/CONTRIBUTION-TICKET.md|knowledge/collaboration-framework" artifacts/mechanical-move-manifest.md` | serious | slice-plan | open | | Exact path accounting for source moves. |
| F-2 | Source-prose preservation evidence distinguishes pure moves from required route/link/version edits and records rename-aware diff evidence | `rg -n "source-prose preservation|pure move|route/link update|version history|git diff --name-status --find-renames|byte-for-byte|cmp|line-level disclosure|no prose rewrite" artifacts/source-prose-preservation-evidence.md` | serious | slice-plan | open | | Prevents mechanical move from becoming a rewrite. |
| F-3 | Compatibility route update record re-enters the Slice02 no-shim decision and preserves top-level `SKILL.md`, `README.md`, `AGENTS.md`, and `CLAUDE.md` behavior | `rg -n "compatibility route update|no-shim|top-level SKILL.md|validated shim|replacement route|README.md|AGENTS.md|CLAUDE.md|CLAUDE.md -> AGENTS.md|re-entry condition|route compatibility" artifacts/compatibility-route-update-record.md` | serious | slice-plan | open | | Required because Slice02 deferred route re-entry to the composer move. |
| F-4 | Package validation evidence records Makefile `CF_FILES`, `make check-skills`, `make collab-framework`, `make check-package-paths`, generated package inspection, and exception-path handling | `rg -n "package validation|CF_FILES|make check-skills|make collab-framework|make check-package-paths|collaboration-framework.zip|package root|entrypoint|package-path-exceptions.tsv|existing exception|no new exception|generated zip not committed" artifacts/package-validation-evidence.md` | serious | slice-plan | open | | Preserves package behavior while moving source paths. |
| F-5 | Source checkout status records exact source commit, edited/moved source paths, generated artifact handling, and clean final source status | `rg -n "source checkout|source commit|source-files-edited: true|git status --short|git diff --check|edited source paths|moved source paths|generated zip not committed|clean final source status" artifacts/*.md` | serious | slice-plan | open | | Supports Expedited Mode source/planning commit separation. |
| F-6 | Closing report walks all six rows, states source/planning checkout status, and bubbles findings up to Arc03 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc03|silent-drop|Slice04" closing-report.md` | serious | slice-plan | open | | Close-set document; do not create before evidence exists. |

## Closure

Slice is open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
