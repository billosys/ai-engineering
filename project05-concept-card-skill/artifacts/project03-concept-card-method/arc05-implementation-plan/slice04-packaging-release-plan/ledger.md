# Slice 04: Packaging, Discoverability, and Release Gates

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice04 open set exists with slice plan, ledger, prompt, and artifact home | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && test -d artifacts` | correctness-grade | slice-plan | done | closing-report.md | Local CC verification passed on 2026-08-31. |
| F-2 | Required Slice04 planning artifacts are produced under the slice-local artifact home | `test -f artifacts/v40-package-update-plan.md && test -f artifacts/v40-discoverability-plan.md && test -f artifacts/v40-release-gate-plan.md && test -f artifacts/v40-version-history-plan.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-package-update-plan.md; artifacts/v40-discoverability-plan.md; artifacts/v40-release-gate-plan.md; artifacts/v40-version-history-plan.md | Artifact home is `artifacts/`. |
| F-3 | Package update plan covers Makefile, package lists, generated archives, install/clean behavior, package-path checks, exceptions, and package boundaries | `rg -n "Makefile|package target|package list|INSTALL_ZIPS|ALL_SKILL_FILES|generated archive|generated zip|install|clean|package-path|exception|package update boundary" artifacts/v40-package-update-plan.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-package-update-plan.md | Package mechanics row verified locally. |
| F-4 | Discoverability plan covers README, skill library, metadata, load reason, promise boundary, adjacent routing, and operator package expectations | `rg -n "README|skill library|description|metadata|tag|reason to load|promise boundary|adjacent|operator|package expectation|discoverability" artifacts/v40-discoverability-plan.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-discoverability-plan.md | Discoverability row verified locally. |
| F-5 | Release gate plan covers skill checks, package-path checks, generated zip checks, cleanliness, installability, documentation-only validator scope, and release-readiness evidence | `rg -n "check-skills|package-path|generated zip|source checkout|planning checkout|installability|documentation-only validator|release-readiness evidence|release gate" artifacts/v40-release-gate-plan.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-release-gate-plan.md | Release gate row verified locally. |
| F-6 | Version history plan names obligations for all changed source surfaces | `rg -n "SKILL.md|guide|template|example|validation documentation|support document|README|Makefile|package-path exception|version history|source version-history" artifacts/v40-version-history-plan.md` | correctness-grade | slice-plan | done | closing-report.md; artifacts/v40-version-history-plan.md | Source history row verified locally. |
| F-7 | Artifacts preserve Slice02 package-compatible guides layout and Slice03 documentation-only validator-code scope | `rg -n "Slice02|guides/|package-compatible|SKILL.md plus sibling guides|Slice03|documentation-only validator|validator-code scope|executable validator-code deferred" artifacts/v40-package-update-plan.md artifacts/v40-discoverability-plan.md artifacts/v40-release-gate-plan.md artifacts/v40-version-history-plan.md` | serious | arc-plan | done | closing-report.md; artifacts/ | Continuity row verified locally. |
| F-8 | Artifacts route implementation synthesis, implementation slices, deferral register, and Project03 close input to Slice05 | `rg -n "Slice05|implementation-plan synthesis|implementation slice|deferral register|Project03 close input|source edit sequence" artifacts/v40-package-update-plan.md artifacts/v40-discoverability-plan.md artifacts/v40-release-gate-plan.md artifacts/v40-version-history-plan.md` | serious | slice-plan | done | closing-report.md; artifacts/ | Later-slice routing row verified locally. |
| F-9 | Artifacts keep source edits, implementation, package release, executable validator-code, runtime services, generated zips, and release readiness out of scope | `rg -n "out of scope|does not edit source|source implementation|package release|executable validator-code|runtime|GraphRAG|graph database|ontology database|memory runtime|CCDP service|live extraction|generated zips|release readiness" slice-plan.md artifacts/v40-package-update-plan.md artifacts/v40-discoverability-plan.md artifacts/v40-release-gate-plan.md artifacts/v40-version-history-plan.md` | serious | operator constraint | done | closing-report.md; slice-plan.md; artifacts/ | Planning-only row verified locally. |
| F-10 | Artifacts distinguish planned release gates from actual release evidence or release claims | `rg -n "planned release gate|not release evidence|does not claim release readiness|future implementation|evidence required before claiming|not a release" artifacts/v40-release-gate-plan.md artifacts/v40-package-update-plan.md artifacts/v40-discoverability-plan.md` | serious | operator constraint | done | closing-report.md; artifacts/v40-release-gate-plan.md; artifacts/v40-package-update-plan.md; artifacts/v40-discoverability-plan.md | Prevents overclaiming. |
| F-11 | Source checkout remains clean | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | operator constraint | done | closing-report.md | Source checkout was not modified. |
| F-12 | New and modified Slice04 Markdown is ASCII-clean and has no trailing whitespace | `LC_ALL=C grep -RIn '[^ -~]' slice-plan.md ledger.md cc-prompt.md artifacts || true; grep -RIn '[[:blank:]]$' slice-plan.md ledger.md cc-prompt.md artifacts || true` | polish | repo hygiene | done | closing-report.md | Verification printed no matches. |

## What Worked

- Planning package-compatible assets under `guides/` avoided a package
  behavior change while preserving Slice02 and Slice03 decisions.
- Treating generated zip output as future evidence, not current release
  evidence, kept release-readiness claims calibrated.
- Naming version-history owners by source surface made the implementation
  history work visible before source edits begin.

## Closure

Status: proposed-done pending independent CDC verification.

Rows: 12. Done: 12. Deferred: 0. No-op: 0.
