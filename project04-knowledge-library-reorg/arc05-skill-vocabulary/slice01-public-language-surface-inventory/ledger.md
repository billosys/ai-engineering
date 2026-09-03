# Slice 01: Public Language Surface Inventory

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Current public-language surface map records README, docs, SKILL, knowledge skill entrypoints, package metadata, and protocol/support wording surfaces | `rg -n "public language surface map|README.md|docs/|SKILL.md|knowledge/.*/SKILL|package metadata|protocol|support|current wording" artifacts/current-public-language-surface-map.md` | serious | slice-plan | open | | Public wording surface inventory. |
| F-2 | Classification evidence synthesis records external ontology rubric, Arc01 topology classification, Arc02 contract, Arc03 layout, Arc04 docs, and evidence status boundaries | `rg -n "classification evidence synthesis|external ontology rubric|Arc01|Arc02|Arc03|Arc04|skill kind|topology|atomic|composite|evidence status|not accepted taxonomy" artifacts/classification-evidence-synthesis.md` | correctness-grade | slice-plan | open | | Evidence synthesis. |
| F-3 | Terminology decision question register records answerable questions for kind, topology, examples, avoid-list, planned surfaces, and re-entry conditions | `rg -n "terminology decision question register|skill kind|topology|atomic|composite|examples|avoid-list|planned surfaces|re-entry conditions|Slice02" artifacts/terminology-decision-question-register.md` | serious | slice-plan | open | | Slice02 decision question evidence. |
| F-4 | Source edit impact map records possible README/docs/SKILL/package-facing edits, no-source-edit status for Slice01, and authorization boundary for later slices | `rg -n "source edit impact map|README.md|docs/|SKILL.md|package-facing|source-files-edited: false|no source edit|authorization boundary|later slices" artifacts/source-edit-impact-map.md` | serious | slice-plan | open | | Source impact evidence. |
| F-5 | Arc05 validation command inventory records source status, wording scans, README/docs links, package checks, check-skills, check-package-paths, make all, CCDP package checks, and planning checks | `rg -n "Arc05 validation command inventory|git status --short|wording scan|README/docs links|make check-skills|make check-package-paths|make all|make ccdp-package|make check-ccdp-package|planning git diff --check" artifacts/arc05-validation-command-inventory.md` | serious | slice-plan | open | | Validation command evidence. |
| F-6 | Closing report walks all six rows, states source/planning status, and bubbles findings up to Arc05 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc05|Slice02|silent-drop|no source commit" closing-report.md` | serious | slice-plan | open | | Slice close evidence. |

## Closure

Slice remains open pending CC execution and CDC verification.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
