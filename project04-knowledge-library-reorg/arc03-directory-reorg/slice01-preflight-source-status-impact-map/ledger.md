# Slice 01: Preflight Source Status and Impact Map

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Source status impact map records source/planning baselines, worktree identity, and preflight-only boundary | `rg -n "source status baseline|planning status baseline|main checkout|planning checkout|worktree|status --short|source-files-edited: false|preflight-only" artifacts/source-status-impact-map.md` | serious | slice-plan | open | | Must establish the baseline before source moves. |
| F-2 | Impact map names expected Arc03 source, package, compatibility, and generated artifact surfaces | `rg -n "README.md|SKILL.md|docs/|knowledge/|templates/|protocols/ccdp|Makefile|package-path-exceptions.tsv|generated zips|AGENTS.md|CLAUDE.md|package roots|source roots" artifacts/source-status-impact-map.md` | serious | slice-plan | open | | Must show likely blast radius before edits. |
| F-3 | Validation command inventory maps source-edit surfaces to status, diff, skill, package, framework, CCDP, and generated package gates | `rg -n "validation command inventory|git .*status --short|diff --check|make help|make check-skills|make check-package-paths|make all|make collab-framework|make ccdp-package|make check-ccdp-package|generated package inspection" artifacts/validation-command-inventory.md` | serious | slice-plan | open | | Must make later implementation checks explicit. |
| F-4 | Source-edit authorization register distinguishes preflight from later source-edit slices and names operator gates | `rg -n "source-edit authorization register|preflight-only|not authorized now|authorized later|operator gate|top-level SKILL.md|validated shim|replacement route|no-shim|persistent package-path exception|accepted warning" artifacts/source-edit-authorization-register.md` | serious | slice-plan | open | | Must prevent accidental source edits from preflight. |
| F-5 | Artifacts preserve Arc02 ordering and Arc04/Arc05 separation | `rg -n "mechanical moves before prose rewrites|package-local link repair before exceptions|Arc04|end-user docs|Arc05|public vocabulary|CCDP remains separate|Biome multi-entrypoint" artifacts/*.md` | correctness-grade | slice-plan | open | | Must keep implementation from absorbing later prose/vocabulary work. |
| F-6 | Closing report walks all six rows, states source checkout remains untouched, and bubbles usable findings up to Arc03 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout remains untouched|Bubble-Up to Arc03|silent-drop" closing-report.md` | serious | slice-plan | open | | Close-set document; do not create before evidence exists. |

## Closure

Slice remains open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
