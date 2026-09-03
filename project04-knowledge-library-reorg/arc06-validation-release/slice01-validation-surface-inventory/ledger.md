# Slice 01: Validation Surface Inventory and Gate Plan

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Current validation surface map records source checkout, planning checkout, README/docs/SKILL links, Make targets, package outputs, install smoke, CCDP package, and operator acceptance surfaces | `rg -n "validation surface map|source checkout|planning checkout|README|docs/|SKILL.md|Make target|package output|install smoke|CCDP|operator acceptance" artifacts/current-validation-surface-map.md` | serious | slice-plan | open | | Complete final validation surface inventory. |
| F-2 | Package/install command matrix records package-path checks, package builds, generated package inspections, temporary install smoke commands, expected outputs, and pass/fail disposition | `rg -n "package/install command matrix|check-package-paths|make all|package inspection|generated package|temporary install|INSTALL_DIR|expected output|pass|fail" artifacts/package-install-command-matrix.md` | correctness-grade | slice-plan | open | | Final installable-skill command plan. |
| F-3 | CCDP freshness repair decision map records current make ccdp-package/check-ccdp-package behavior, stale assembled-spec evidence if present, repair options, authorization needed, and protocol/package separation | `rg -n "CCDP freshness|make ccdp-package|make check-ccdp-package|stale assembled|repair option|authorization|protocol/package separation|protocols/ccdp" artifacts/ccdp-freshness-repair-decision-map.md` | correctness-grade | slice-plan | open | | CCDP re-entry decision evidence. |
| F-4 | Source-edit authorization register records later-slice path permissions, no-edit surfaces, generated artifact handling, and operator gates | `rg -n "source-edit authorization|later slice|path permission|no-edit|generated artifact|operator gate|protocols/ccdp|package-path-exceptions|Makefile|README|docs/" artifacts/source-edit-authorization-register.md` | serious | slice-plan | open | | Arc06 repair boundary evidence. |
| F-5 | Release-readiness risk register records blockers, warnings, no-op confirmations, re-entry items, and acceptance prerequisites | `rg -n "release-readiness risk|blocker|warning|no-op|re-entry|acceptance prerequisite|operator acceptance|Arc06" artifacts/release-readiness-risk-register.md` | serious | slice-plan | open | | Risk and acceptance evidence. |
| F-6 | Closing report walks all six rows, states source/planning status, and bubbles findings up to Arc06 | `test -f closing-report.md && rg -n "Rows: 6|Done:|Deferred:|No-op:|source checkout|planning checkout|Bubble-Up to Arc06|validation surface|package/install|CCDP|silent-drop" closing-report.md` | serious | slice-plan | open | | Slice close evidence. |

## Closure

Slice remains open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
