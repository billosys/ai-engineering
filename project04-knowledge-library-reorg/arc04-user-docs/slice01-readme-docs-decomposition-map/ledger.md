# Slice 01: README and Docs Decomposition Map

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | README source surface map records current README sections, existing docs surfaces, and post-Arc03 source anchors | `rg -n "README source surface|README.md|docs/|knowledge/|protocols/ccdp|SKILL.md|Makefile|package" artifacts/readme-source-surface-map.md` | serious | slice-plan | open | | Source surface map evidence. |
| F-2 | End-user docs decomposition plan proposes focused docs with audience, purpose, source inputs, and docs versus knowledge boundary | `rg -n "end-user docs decomposition|audience|purpose|source inputs|docs/|knowledge/|repository overview|skill library|collaboration framework|knowledge library|build|install|protocol|contribution" artifacts/end-user-docs-decomposition-plan.md` | serious | slice-plan | open | | Target docs set evidence. |
| F-3 | Arc04 doc edit sequence assigns later slices, source-edit status, validation gates, and dependency order | `rg -n "doc edit sequence|Slice02|Slice03|Slice04|source-files-edited|README orientation|focused docs|validation|dependency" artifacts/arc04-doc-edit-sequence.md` | serious | slice-plan | open | | Later slice sequence evidence. |
| F-4 | Public language boundary register separates Arc04 provisional wording from Arc05 final skill-kind and atomic/composite vocabulary | `rg -n "public language boundary|Arc05|provisional|skill kind|atomic|composite|domain|tooling|framework|operational|method|protocol|support" artifacts/public-language-boundary-register.md` | serious | slice-plan | open | | Arc05 boundary evidence. |
| F-5 | Docs validation command inventory records source status, README/docs link checks, package-path checks, and package validation surfaces for later source-edit slices | `rg -n "validation command inventory|git status --short|README links|docs links|make check-skills|make check-package-paths|make all|make ccdp-package|make check-ccdp-package|package validation" artifacts/docs-validation-command-inventory.md` | serious | slice-plan | open | | Validation inventory evidence. |
| F-6 | Closing report walks all six rows, states source/planning status, and bubbles findings up to Arc04 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc04|Slice02|silent-drop|no source commit" closing-report.md` | serious | slice-plan | open | | Slice close evidence. |

## Closure

Slice remains open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
