# Slice 02: Collaboration Framework Entrypoint Relocation

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Entrypoint relocation report records the explicit git mv from root SKILL.md to knowledge/collaboration-framework/SKILL.md, confirms root SKILL.md is absent, and names the source commit | `rg -n "entrypoint relocation|git mv|SKILL.md -> knowledge/collaboration-framework/SKILL.md|root SKILL.md absent|source commit|no component docs moved" artifacts/entrypoint-relocation-report.md` | correctness-grade | slice-plan | open | | Source path move evidence. |
| F-2 | Makefile/package staging report records ALL_SKILL_FILES, CF_FILES, check-skills target behavior, collab-framework package staging, and package root SKILL.md preservation | `rg -n "Makefile|ALL_SKILL_FILES|CF_FILES|check-skills|collab-framework|package root|collaboration-framework/SKILL.md|stage" artifacts/makefile-package-staging-report.md` | correctness-grade | slice-plan | open | | Package behavior evidence. |
| F-3 | Source-reference repair report records all changed README/docs/source references, package-local link repairs, and path-exception disposition | `rg -n "README|docs/skill-library|docs/knowledge-library-anatomy|docs/repository-overview|docs/collaboration-framework|docs/ORIGINS|package-local link|path-exception|assets/packaging/path-exceptions.tsv" artifacts/source-reference-repair-report.md` | serious | slice-plan | open | | Public/source reference evidence. |
| F-4 | Validation report records source diff check, local link validation, make check-skills, make collab-framework, generated package inspection, and final source status | `rg -n "diff --check|local link|check-skills|collab-framework|package inspection|collaboration-framework.zip|final source status|clean" artifacts/validation-report.md` | correctness-grade | slice-plan | open | | Validation evidence. |
| F-5 | Source commit scope is explicit and excludes generated zips/build output | `rg -n "source commit|authorized source files|generated zips|build/|excluded|co-author trailers" artifacts/entrypoint-relocation-report.md artifacts/validation-report.md` | serious | slice-plan | open | | Expedited Mode commit discipline. |
| F-6 | Closing report walks all six rows and bubbles remaining guide-layout work to Slice03 | `test -f closing-report.md && rg -n "Rows: 6|Done:|Deferred:|No-op:|Bubble-Up to Arc07|Slice03|guides|component SKILL.md|verified|proposed" closing-report.md` | serious | slice-plan | open | | Slice close evidence. |

## Closure

Slice is open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
