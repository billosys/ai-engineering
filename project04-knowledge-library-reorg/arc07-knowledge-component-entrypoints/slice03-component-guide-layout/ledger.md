# Slice 03: Component Guide Layout and Standalone Entrypoints

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Component guide move report records every explicit git mv path pair, confirms legacy docs/ directories were removed with rmdir, and confirms templates remain in templates/ | `rg -n "component guide move|git mv|AI-CONSTITUTION-SUPPLEMENT|SUBAGENT-DELEGATION-POLICY|CODE-AUDIT|CONTRIBUTION-STYLE|AI-ENGINEERING-METHODOLOGY|PROJECT-MANAGEMENT|CODE-COVERAGE|docs/pm|guides|rmdir|templates/" artifacts/component-guide-move-report.md` | correctness-grade | slice-plan | open | | Mechanical layout evidence. |
| F-2 | Component entrypoint report records concise component-root SKILL.md files, distinguishes wayfinders from long guides, and confirms no separate installable packages were added | `rg -n "component entrypoint|SKILL.md|agent-coordination|code-auditing|contribution-style|engineering-methods|project-management|testing|work-verification|wayfinder|no separate installable" artifacts/component-entrypoint-report.md` | correctness-grade | slice-plan | open | | Entrypoint contract evidence. |
| F-3 | Reference and package repair report records README/docs/AGENTS/component link repairs, Makefile CF_FILES/ALL_SKILL_FILES updates, package-path exception disposition, and the engineering-methods ../SKILL.md repair | `rg -n "README|docs/|AGENTS.md|Makefile|CF_FILES|ALL_SKILL_FILES|package-path|assets/packaging/path-exceptions.tsv|engineering-methods|../SKILL.md|package-local" artifacts/reference-and-package-repair-report.md` | correctness-grade | slice-plan | open | | Link/package repair evidence. |
| F-4 | Validation report records source diff check, local link validation, make check-skills, make collab-framework, make check-package-paths, generated package inspection, and final source status | `rg -n "diff --check|local link|check-skills|collab-framework|check-package-paths|package inspection|collaboration-framework.zip|final source status|clean" artifacts/validation-report.md` | correctness-grade | slice-plan | open | | Validation evidence. |
| F-5 | Source commit scope is explicit and excludes generated zips/build output | `rg -n "source commit|authorized source files|generated zips|build/|excluded|co-author trailers" artifacts/component-guide-move-report.md artifacts/validation-report.md` | serious | slice-plan | open | | Expedited Mode commit discipline. |
| F-6 | Closing report walks all six rows and bubbles remaining reconciliation or release-note work to Slice04 | `test -f closing-report.md && rg -n "Rows: 6|Done:|Deferred:|No-op:|Bubble-Up to Arc07|Slice04|reconciliation|release notes|verified|proposed" closing-report.md` | serious | slice-plan | open | | Slice close evidence. |

## Closure

Slice is open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
