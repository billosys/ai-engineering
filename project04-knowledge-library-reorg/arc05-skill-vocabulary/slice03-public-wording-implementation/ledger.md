# Slice 03: Public Wording Implementation

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Public wording implementation map records every edited source file, accepted vocabulary applied, and before/after intent | `rg -n "public wording implementation map|README.md|docs/repository-overview.md|docs/skill-library.md|docs/collaboration-framework.md|docs/knowledge-library-anatomy.md|docs/protocols.md|docs/contributing.md|docs/building-and-installing.md|SKILL.md|accepted vocabulary|before|after" artifacts/public-wording-implementation-map.md` | correctness-grade | slice-plan | open | | Source wording map evidence. |
| F-2 | Authorized public source surfaces reflect accepted skill-kind and topology vocabulary without collapsing the axes | `rg -n "skill kind|domain/tooling|framework/operational|method skill|protocol distribution|protocol package|support material|support template|atomic skill|composite skill|knowledge substrate" /Users/oubiwann/lab/billosys/ai-engineering/README.md /Users/oubiwann/lab/billosys/ai-engineering/docs /Users/oubiwann/lab/billosys/ai-engineering/SKILL.md` | correctness-grade | slice-plan | open | | Accepted vocabulary appears in public source surfaces. |
| F-3 | Vocabulary scan evidence records accepted terms, avoided claims, contextual caveats, and no unqualified prohibited claims | `rg -n "vocabulary scan evidence|accepted terms|avoided claims|atomic means domain|composite means framework|CCDP is a skill|concept-card-method is available|source-root/package-root equivalence|collaboration-framework.*deprecated|no unqualified prohibited claims" artifacts/vocabulary-scan-evidence.md` | serious | slice-plan | open | | Avoid-list scan evidence. |
| F-4 | Source change and validation evidence records source commit, explicit source path list, package/build validation, generated zip handling, and final clean state | `rg -n "source change and validation evidence|source commit|explicit source path list|git status --short|git diff --check|make check-skills|make check-package-paths|make all|make ccdp-package|make check-ccdp-package|generated zip not committed|final source status" artifacts/source-change-and-validation-evidence.md` | serious | slice-plan | open | | Source validation evidence. |
| F-5 | Deferred re-entry notes record any excluded package-facing, metadata, Makefile, package-root, generated-zip, CCDP, template, knowledge-entrypoint, or concept-card-method needs | `rg -n "deferred re-entry notes|package-facing|metadata|Makefile|package root|generated zip|CCDP|templates/GUIDE.md|knowledge entrypoint|concept-card-method|deferred|re-entry" artifacts/deferred-reentry-notes.md` | serious | slice-plan | open | | Out-of-scope disposition evidence. |
| F-6 | Source scope check confirms unauthorized surfaces were not edited | `rg -n "unauthorized surfaces unchanged|Makefile|package-path-exceptions.tsv|generated zips|knowledge.*SKILL|protocols/ccdp|templates/GUIDE.md|source moves|package roots|not edited" artifacts/source-change-and-validation-evidence.md artifacts/deferred-reentry-notes.md` | correctness-grade | slice-plan | open | | Source boundary evidence. |
| F-7 | Closing report walks all seven rows, states source/planning status, and bubbles findings up to Arc05 | `test -f closing-report.md && rg -n "Rows: 7|Done: 7|source checkout|planning checkout|Bubble-Up to Arc05|Slice04|silent-drop|source commit|planning commit" closing-report.md` | serious | slice-plan | open | | Slice close evidence. |

## Closure

Slice remains open.

Rows: 7. Done: 0. Deferred: 0. No-op: 0.
