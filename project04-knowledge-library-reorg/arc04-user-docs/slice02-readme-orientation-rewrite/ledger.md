# Slice 02: README Orientation Rewrite

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | README orientation change map records source files edited, keep/move/rewrite outcomes, and concise README scope | `rg -n "README orientation change map|README.md|source files edited|keep|move|rewrite|concise orientation|quick start|focused docs" artifacts/readme-orientation-change-map.md` | serious | slice-plan | done | `artifacts/readme-orientation-change-map.md`; verifier command passes. | README rewrite map evidence. |
| F-2 | README route repair evidence records stale route repairs for docs/dev, former framework docs under docs, moved template paths, and current docs/knowledge/protocol links | `rg -n "README route repair evidence|docs/dev|former framework docs|moved template paths|docs/|knowledge/|protocols/ccdp|templates/GUIDE.md|no stale route" artifacts/readme-route-repair-evidence.md` | serious | slice-plan | done | `artifacts/readme-route-repair-evidence.md`; verifier command passes. | Stale-route repair evidence. |
| F-3 | Focused doc stub register records every new or touched docs file, whether it is a minimal stub or existing doc, and its Slice03 expansion status | `rg -n "focused doc stub register|docs/repository-overview.md|docs/skill-library.md|docs/collaboration-framework.md|docs/knowledge-library-anatomy.md|docs/building-and-installing.md|docs/protocols.md|docs/contributing.md|minimal stub|Slice03" artifacts/focused-doc-stub-register.md` | serious | slice-plan | done | `artifacts/focused-doc-stub-register.md`; verifier command passes. | README link-target evidence. |
| F-4 | Source change and validation evidence records source commit, explicit source path list, diff/status checks, package checks, generated zip handling, and final clean state | `rg -n "source change and validation evidence|source commit|explicit source path list|git status --short|git diff --check|make check-skills|make check-package-paths|make all|make ccdp-package|make check-ccdp-package|generated zip not committed|final source status" artifacts/source-change-and-validation-evidence.md` | serious | slice-plan | done | `artifacts/source-change-and-validation-evidence.md`; verifier command passes. | Source validation evidence. |
| F-5 | Arc05 vocabulary boundary remains preserved in README/docs wording and recorded in the source evidence | `rg -n "Arc05 vocabulary boundary|provisional|skill kind|atomic|composite|domain/tooling|framework/operational|method|protocol distribution|not finalized" artifacts/*.md` | serious | slice-plan | done | `artifacts/source-change-and-validation-evidence.md`; verifier command passes. | Vocabulary boundary evidence. |
| F-6 | Closing report walks all six rows, states source/planning status, and bubbles findings up to Arc04 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc04|Slice03|silent-drop|source commit" closing-report.md` | serious | slice-plan | done | `closing-report.md`; verifier command passes. | Slice close evidence. |

## Closure

Slice is verified-closed by CDC. The README orientation rewrite, focused doc
stub creation, route repair evidence, source validation evidence, and Arc05
vocabulary boundary were independently reproduced in `cdc-verification.md`.

Rows: 6. Done: 6. Deferred: 0. No-op: 0.
