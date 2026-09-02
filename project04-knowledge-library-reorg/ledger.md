# Project 04: Knowledge Library Reorganization

## Project Ledger

Definition of done: the repository has a clear, tested, and documented split
between `docs/` as end-user documentation about the repository's materials and
`knowledge/` as the raw and derived knowledge-library substrate consumed by
atomic and composite skills across domain/tooling, framework/operational, and
method categories.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| P-1 | Arc 01 closes with a source-backed inventory and role classification for current docs, knowledge, templates, protocols, README, skill, and packaging surfaces, including skill kind and atomic/composite topology | `test -f arc01-material-inventory/closing-report.md && rg -n "Composition verdict: delivered|docs|knowledge|templates|protocols|README|classification|prior proposal|atomic|composite|skill kind|topology" arc01-material-inventory/closing-report.md` | serious | project-plan | done | attested: Arc01 `closing-report.md` records `Composition verdict: delivered`; CDC reproduced the row Verify command on 2026-09-02. | Child-arc closure plus inventory composition evidence. |
| P-2 | Arc 02 closes with an accepted target directory contract, migration plan, compatibility strategy, explicit exception list, and source-root decision for atomic and composite skills | `test -f arc02-directory-contract/closing-report.md && rg -n "Composition verdict: delivered|target layout|migration plan|compatibility|exception|path contract|atomic|composite|source root" arc02-directory-contract/closing-report.md` | serious | project-plan | done | attested: Arc02 `closing-report.md` records `Composition verdict: delivered`; CDC reproduced the row Verify command on 2026-09-02. | Child-arc closure plus target-layout acceptance evidence. |
| P-3 | Arc 03 closes with accepted directory reorganization source edits landed and path/link/package validations passing | `test -f arc03-directory-reorg/closing-report.md && rg -n "Composition verdict: delivered|file moves|README links|package-path|make check" arc03-directory-reorg/closing-report.md` | serious | project-plan | open | | Child-arc closure plus source validation evidence. |
| P-4 | Arc 04 closes with README split into concise orientation and focused end-user docs under docs | `test -f arc04-user-docs/closing-report.md && rg -n "Composition verdict: delivered|README|end-user|docs/|orientation|focused" arc04-user-docs/closing-report.md` | correctness-grade | project-plan | open | | Child-arc closure plus documentation composition evidence. |
| P-5 | Arc 05 closes with accepted public skill vocabulary and wayfinding for domain/tooling, framework/operational, method, protocol, support, atomic, and composite surfaces | `test -f arc05-skill-vocabulary/closing-report.md && rg -n "Composition verdict: delivered|domain|tooling|framework|operational|method|protocol|support|atomic|composite" arc05-skill-vocabulary/closing-report.md` | correctness-grade | project-plan | open | | Child-arc closure plus terminology acceptance evidence. |
| P-6 | Arc 06 closes with validation, packaging, installability, CCDP package separation, and operator acceptance reconciled after the final layout | `test -f arc06-validation-release/closing-report.md && rg -n "Composition verdict: delivered|check-skills|check-package-paths|install|ccdp|operator acceptance|reconciled" arc06-validation-release/closing-report.md` | serious | project-plan | open | | Child-arc closure plus final acceptance evidence. |
| P-7 | Project-level acceptance demo shows a user can orient from README into docs for explanation and into knowledge for actual material substrate without path/category or atomic/composite ambiguity | `rg -n "docs/.*user|knowledge/.*substrate|skill library|build|install|protocol|atomic|composite" /Users/oubiwann/lab/billosys/ai-engineering/README.md /Users/oubiwann/lab/billosys/ai-engineering/docs` | serious | project-plan | open | | Project-scale composition row; must be reproduced at project close. |

## Closure

Project remains open.

Rows: 7. Done: 2. Deferred: 0. No-op: 0.
