# Slice 04: Vocabulary Reconciliation and Arc Close Readiness

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Vocabulary reconciliation report records README/docs/SKILL consistency for accepted skill kind, topology, examples, and docs/knowledge boundaries | `rg -n "vocabulary reconciliation report|README.md|docs/|SKILL.md|skill kind|topology|domain/tooling|framework/operational|method skill|protocol distribution|atomic skill|composite skill|docs/|knowledge/" artifacts/vocabulary-reconciliation-report.md` | correctness-grade | slice-plan | open | | Public wording consistency evidence. |
| F-2 | Vocabulary scan confirms accepted terms and no unqualified prohibited claims across public source surfaces | `rg -n "accepted vocabulary scan|avoided claim scan|no unqualified prohibited claims|atomic means domain|composite means framework|CCDP is a skill|concept-card-method is available|source-root/package-root equivalence|collaboration-framework.*deprecated" artifacts/vocabulary-reconciliation-report.md` | serious | slice-plan | open | | Vocabulary scan evidence. |
| F-3 | Navigation and link validation evidence records local README/docs/SKILL link checks and route scans | `rg -n "navigation and link validation evidence|local link validation|README.md|docs/|SKILL.md|links checked|missing: 0|docs/|knowledge/|protocols/|templates/|Makefile|package" artifacts/navigation-and-link-validation-evidence.md` | serious | slice-plan | open | | Link and route evidence. |
| F-4 | Package and build validation evidence records check-skills, check-package-paths, make all, generated zip handling, and final source status | `rg -n "package and build validation evidence|make check-skills|make check-package-paths|make all|generated zip|not committed|git diff --check|final source status|hard failures: 0" artifacts/package-and-build-validation-evidence.md` | serious | slice-plan | open | | Build/package evidence. |
| F-5 | CCDP re-entry disposition records whether ccdp package checks are green or explicitly deferred because protocols/ccdp edits are outside Arc05 Slice04 authorization | `rg -n "CCDP re-entry disposition|make ccdp-package|make check-ccdp-package|protocols/ccdp|stale assembled|deferred|re-entry|outside authorization|no unauthorized protocol edit" artifacts/ccdp-reentry-disposition.md` | correctness-grade | slice-plan | open | | CCDP disposition evidence. |
| F-6 | Arc05 close-readiness report records slice status, arc ledger readiness, source/planning cleanliness, and any remaining re-entry items for Arc06 | `rg -n "Arc05 close-readiness report|Slice01|Slice02|Slice03|Slice04|arc ledger|close readiness|source checkout|planning checkout|Arc06|re-entry|ready for CDC arc close" artifacts/arc05-close-readiness-report.md` | serious | slice-plan | open | | Arc close readiness evidence. |
| F-7 | Closing report walks all seven rows, states source/planning status, and bubbles findings up to Arc05 | `test -f closing-report.md && rg -n "Rows: 7|Done:|Deferred:|No-op:|source checkout|planning checkout|Bubble-Up to Arc05|arc close|silent-drop|source commit|planning commit" closing-report.md` | serious | slice-plan | open | | Slice close evidence. |

## Closure

Slice remains open.

Rows: 7. Done: 0. Deferred: 0. No-op: 0.
