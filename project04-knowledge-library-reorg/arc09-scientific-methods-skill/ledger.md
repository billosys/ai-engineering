# Arc 09: Scientific Methods Skill

## Arc Ledger

Capability: Arc09 adds `scientific-methods` as a live method skill, packages
it as an installable zip, documents it for users, and adds
collaboration-framework wayfinding without folding it into the composed
framework package.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 records the operator-approved CDC-direct execution override and exact source scope | `test -f slice01-scientific-methods-skill-implementation/closing-report.md && rg -n "CDC-direct|operator override|source commit|a2122ab|explicit source file list|same-context" slice01-scientific-methods-skill-implementation/closing-report.md` | serious | operator-reentry | done | `slice01-scientific-methods-skill-implementation/closing-report.md` records the direct execution override, exact source commit, explicit source file list, and same-context verification limitation. | Preserves process truth without pretending a formal CC handoff occurred. |
| A-2 | Slice01 creates a live scientific-methods method skill with guides, templates, version history, and package support | `test -f slice01-scientific-methods-skill-implementation/artifacts/source-change-summary.md && rg -n "scientific-methods|SKILL.md|version-history|guides|templates|Makefile|scientific-methods.zip|method skill" slice01-scientific-methods-skill-implementation/artifacts/source-change-summary.md` | correctness-grade | operator-reentry | done | `artifacts/source-change-summary.md` records the new method skill, guide set, templates, Makefile target, and package support. | Confirms the new skill exists as a live package surface. |
| A-3 | Slice01 adds collaboration-framework and public README/docs wayfinding for scientific-methods without bundling it into collaboration-framework.zip | `test -f slice01-scientific-methods-skill-implementation/artifacts/source-change-summary.md && rg -n "collaboration-framework|wayfinding|load separately|README|docs/skill-library|docs/collaboration-framework|not bundled" slice01-scientific-methods-skill-implementation/artifacts/source-change-summary.md` | correctness-grade | operator-reentry | done | `artifacts/source-change-summary.md` records collaboration-framework trigger routing, public docs, README updates, and the independent-package decision. | Keeps scientific-methods adjacent to, not absorbed by, the collaboration framework. |
| A-4 | Slice01 validation passes with the new package baseline and install smoke | `test -f slice01-scientific-methods-skill-implementation/artifacts/validation-results.md && rg -n "git diff --check|git diff --cached --check|make check-skills|make scientific-methods|make check-package-paths|13 zips|222 packaged Markdown|0 hard failures|install smoke|13 SKILL|no ccdp" slice01-scientific-methods-skill-implementation/artifacts/validation-results.md` | correctness-grade | source-validation | done | `artifacts/validation-results.md` records whitespace, skill metadata, link, package-path, zip inspection, and isolated install-smoke evidence. | Confirms package/install behavior after adding the method skill. |
| A-5 | Arc09 closes with source commit, planning record, row walk, final statuses, and Project04 bubble-up | `test -f closing-report.md && rg -n "Composition verdict: delivered|source commit|a2122ab|Rows: 5|Done: 5|Project04 bubble-up|source status|planning status" closing-report.md` | serious | ledger-discipline | done | `closing-report.md` records the source commit, row walk, final statuses, and Project04 bubble-up. | Arc close is recorded without changing Arc08 review status. |

## Closure

Arc is closed by CDC-direct operator override.

Rows: 5. Done: 5. Deferred: 0. No-op: 0.
