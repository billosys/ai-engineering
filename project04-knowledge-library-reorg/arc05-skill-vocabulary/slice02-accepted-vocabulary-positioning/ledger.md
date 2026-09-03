# Slice 02: Accepted Vocabulary and Positioning Decision

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Accepted public vocabulary records skill-kind and topology terms with public, maintainer-facing, deferred, or avoided status | `rg -n "accepted public vocabulary|skill kind|topology|domain/tooling|framework/operational|method|protocol|support|source/provenance|atomic|composite|public|maintainer-facing|deferred|avoided" artifacts/accepted-public-vocabulary.md` | correctness-grade | slice-plan | open | | Vocabulary decision evidence. |
| F-2 | Example and edge-case positioning records accepted examples and caveats for Rust, collaboration-framework, CCDP, Biome, templates/GUIDE.md, and planned concept-card-method | `rg -n "example and edge-case positioning|Rust|collaboration-framework|CCDP|Biome|templates/GUIDE.md|concept-card-method|planned|atomic|composite|protocol package|multi-entrypoint" artifacts/example-and-edge-case-positioning.md` | correctness-grade | slice-plan | open | | Example and edge-case evidence. |
| F-3 | Public language avoid-list records prohibited or risky claims, including kind/topology collapse, CCDP as skill, concept-card availability, source/package equivalence, and collaboration-framework deprecation | `rg -n "public language avoid-list|atomic means domain|composite means framework|CCDP is a skill|concept-card-method is available|source-root/package-root equivalence|collaboration-framework.*deprecated|prohibited|risky claims" artifacts/public-language-avoid-list.md` | serious | slice-plan | open | | Avoid-list evidence. |
| F-4 | Source edit authorization plan records authorized Slice03 surfaces, excluded surfaces, validation requirements, and no-source-edit status for Slice02 | `rg -n "source edit authorization plan|Slice03|README.md|docs/|SKILL.md|package-facing|excluded surfaces|Makefile|package-path-exceptions|generated zips|source-files-edited: false|no source edit|validation requirements" artifacts/source-edit-authorization-plan.md` | serious | slice-plan | open | | Source-edit authorization evidence. |
| F-5 | Re-entry condition register records future evidence that reopens vocabulary decisions for entrypoints, package roots, Makefile targets, package-path exceptions, generated zip contents, CCDP, Biome, and docs routes | `rg -n "re-entry condition register|entrypoint|package root|Makefile target|package-path exception|generated zip|CCDP|Biome|docs route|README|SKILL.md|future evidence|reopen" artifacts/re-entry-condition-register.md` | serious | slice-plan | open | | Re-entry evidence. |
| F-6 | Closing report walks all six rows, states source/planning status, and bubbles findings up to Arc05 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc05|Slice03|silent-drop|no source commit" closing-report.md` | serious | slice-plan | open | | Slice close evidence. |

## Closure

Slice remains open pending CC execution and CDC verification.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
