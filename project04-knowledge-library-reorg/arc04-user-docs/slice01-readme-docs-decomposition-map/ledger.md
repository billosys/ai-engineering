# Slice 01: README and Docs Decomposition Map

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | README source surface map records current README sections, existing docs surfaces, and post-Arc03 source anchors | `rg -n "README source surface|README.md|docs/|knowledge/|protocols/ccdp|SKILL.md|Makefile|package" artifacts/readme-source-surface-map.md` | serious | slice-plan | done | attested: `artifacts/readme-source-surface-map.md` | Source surface map evidence records current README sections, `docs/`, and post-Arc03 anchors. |
| F-2 | End-user docs decomposition plan proposes focused docs with audience, purpose, source inputs, and docs versus knowledge boundary | `rg -n "end-user docs decomposition|audience|purpose|source inputs|docs/|knowledge/|repository overview|skill library|collaboration framework|knowledge library|build|install|protocol|contribution" artifacts/end-user-docs-decomposition-plan.md` | serious | slice-plan | done | attested: `artifacts/end-user-docs-decomposition-plan.md` | Target focused docs set and boundary recorded. |
| F-3 | Arc04 doc edit sequence assigns later slices, source-edit status, validation gates, and dependency order | `rg -n "doc edit sequence|Slice02|Slice03|Slice04|source-files-edited|README orientation|focused docs|validation|dependency" artifacts/arc04-doc-edit-sequence.md` | serious | slice-plan | done | attested: `artifacts/arc04-doc-edit-sequence.md` | Later Slice02-Slice04 sequence recorded with source-edit status and validation. |
| F-4 | Public language boundary register separates Arc04 provisional wording from Arc05 final skill-kind and atomic/composite vocabulary | `rg -n "public language boundary|Arc05|provisional|skill kind|atomic|composite|domain|tooling|framework|operational|method|protocol|support" artifacts/public-language-boundary-register.md` | serious | slice-plan | done | attested: `artifacts/public-language-boundary-register.md` | Arc05 vocabulary boundary and operator gate recorded. |
| F-5 | Docs validation command inventory records source status, README/docs link checks, package-path checks, and package validation surfaces for later source-edit slices | `rg -n "validation command inventory|git status --short|README links|docs links|make check-skills|make check-package-paths|make all|make ccdp-package|make check-ccdp-package|package validation" artifacts/docs-validation-command-inventory.md` | serious | slice-plan | done | attested: `artifacts/docs-validation-command-inventory.md` | Validation commands and known stale route targets recorded. |
| F-6 | Closing report walks all six rows, states source/planning status, and bubbles findings up to Arc04 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc04|Slice02|silent-drop|no source commit" closing-report.md` | serious | slice-plan | done | attested: `closing-report.md` | Slice close evidence records source/planning status, bubble-up, and no source commit. |

## Closure

Slice is proposed closed for CDC verification.

Rows: 6. Done: 6. Deferred: 0. No-op: 0.
