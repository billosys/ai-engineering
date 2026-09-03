# Slice 03: Focused End-User Guide Set

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Focused guide expansion map records every expanded guide, source inputs, and the role each doc now serves | `rg -n "focused guide expansion map|docs/repository-overview.md|docs/skill-library.md|docs/collaboration-framework.md|docs/knowledge-library-anatomy.md|docs/building-and-installing.md|docs/protocols.md|docs/contributing.md|expanded|source inputs" artifacts/focused-guide-expansion-map.md` | serious | slice-plan | open | | Guide expansion map evidence. |
| F-2 | Docs content boundary evidence shows docs explain repository materials while knowledge remains the substrate, without duplicating source material or finalizing Arc05 vocabulary | `rg -n "docs content boundary evidence|docs/|knowledge/|explain|substrate|not duplicated|Arc05|provisional|atomic|composite|skill kind" artifacts/docs-content-boundary-evidence.md` | correctness-grade | slice-plan | open | | Docs versus knowledge boundary evidence. |
| F-3 | README navigation preservation evidence records that README stays concise and points to focused docs without long subject-matter expansion | `rg -n "README navigation preservation|README.md|concise orientation|focused docs|Start Here|no long subject-matter expansion|links resolve|Slice04" artifacts/readme-navigation-preservation.md` | serious | slice-plan | open | | README preservation evidence. |
| F-4 | Source change and validation evidence records source commit, explicit source path list, link checks, package checks, generated zip handling, and final clean state | `rg -n "source change and validation evidence|source commit|explicit source path list|git status --short|git diff --check|README links|docs links|make check-skills|make check-package-paths|make all|make ccdp-package|make check-ccdp-package|generated zip not committed|final source status" artifacts/source-change-and-validation-evidence.md` | serious | slice-plan | open | | Source validation evidence. |
| F-5 | Public vocabulary boundary remains preserved across guide wording and is recorded for Arc05 follow-up | `rg -n "public vocabulary boundary|Arc05|provisional|skill kind|atomic|composite|domain/tooling|framework/operational|method|protocol distribution|not finalized" artifacts/*.md` | serious | slice-plan | open | | Vocabulary boundary evidence. |
| F-6 | Closing report walks all six rows, states source/planning status, and bubbles findings up to Arc04 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc04|Slice04|silent-drop|source commit" closing-report.md` | serious | slice-plan | open | | Slice close evidence. |

## Closure

Slice remains open pending CC execution and CDC verification.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
