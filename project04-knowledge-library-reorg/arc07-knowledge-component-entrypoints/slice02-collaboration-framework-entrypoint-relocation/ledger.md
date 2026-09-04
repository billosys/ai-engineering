# Slice 02: Collaboration Framework Entrypoint Relocation

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Entrypoint relocation report records the explicit git mv from root SKILL.md to knowledge/collaboration-framework/SKILL.md, confirms root SKILL.md is absent, and names the source commit | `rg -n "entrypoint relocation|git mv|SKILL.md -> knowledge/collaboration-framework/SKILL.md|root SKILL.md absent|source commit|no component docs moved" artifacts/entrypoint-relocation-report.md` | correctness-grade | slice-plan | done | attested: `artifacts/entrypoint-relocation-report.md`; source commit `a97aaa6a0682791304bd62cbbeee0b7e4d63fc6f`. | Source path move evidence. |
| F-2 | Makefile/package staging report records ALL_SKILL_FILES, CF_FILES, check-skills target behavior, collab-framework package staging, and package root SKILL.md preservation | `rg -n "Makefile|ALL_SKILL_FILES|CF_FILES|check-skills|collab-framework|package root|collaboration-framework/SKILL.md|stage" artifacts/makefile-package-staging-report.md` | correctness-grade | slice-plan | done | attested: `artifacts/makefile-package-staging-report.md`; `make collab-framework` passed. | Package behavior evidence. |
| F-3 | Source-reference repair report records all changed README/docs/source references, package-local link repairs, and path-exception disposition | `rg -n "README|docs/skill-library|docs/knowledge-library-anatomy|docs/repository-overview|docs/collaboration-framework|docs/ORIGINS|package-local link|path-exception|assets/packaging/path-exceptions.tsv" artifacts/source-reference-repair-report.md` | serious | slice-plan | done | attested: `artifacts/source-reference-repair-report.md`; local README/docs/SKILL link validation passed. | Public/source reference evidence. |
| F-4 | Validation report records source diff check, local link validation, make check-skills, make collab-framework, generated package inspection, and final source status | `rg -n "diff --check|local link|check-skills|collab-framework|package inspection|collaboration-framework.zip|final source status|clean" artifacts/validation-report.md` | correctness-grade | slice-plan | done | attested: `artifacts/validation-report.md`; `git diff --check`, `make check-skills`, `make collab-framework`, focused package-path check, and `make check-package-paths` passed. | Validation evidence. |
| F-5 | Source commit scope is explicit and excludes generated zips/build output | `rg -n "source commit|authorized source files|generated zips|build/|excluded|co-author trailers" artifacts/entrypoint-relocation-report.md artifacts/validation-report.md` | serious | slice-plan | done | attested: `artifacts/entrypoint-relocation-report.md` and `artifacts/validation-report.md`; source commit includes required co-author trailers. | Expedited Mode commit discipline. |
| F-6 | Closing report walks all six rows and bubbles remaining guide-layout work to Slice03 | `test -f closing-report.md && rg -n "Rows: 6|Done:|Deferred:|No-op:|Bubble-Up to Arc07|Slice03|guides|component SKILL.md|verified|proposed" closing-report.md` | serious | slice-plan | done | attested: `closing-report.md`; remaining guides/component SKILL.md work bubbled to Slice03. | Slice close evidence. |

## Closure

Slice is proposed-done pending CDC verification.

Rows: 6. Done: 6. Deferred: 0. No-op: 0.
