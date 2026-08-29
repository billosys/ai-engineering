# Project 01: Harmonise Paths Ledger

Definition of done: humans and LLMs can use the cloned source tree and the
generated zip/unzipped bundles without rediscovering file locations for project
management, SDLC planning/execution, language-specific best practices, or CCDP
protocol processing.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| P-1 | Arc 01 closes with an accepted distribution path contract. | `test -f project01-harmonise-paths/arc01-distribution-path-contract/closing-report.md && rg -n "Composition verdict: delivered" project01-harmonise-paths/arc01-distribution-path-contract/closing-report.md` | serious | project-plan | done | attested: `arc01-distribution-path-contract/closing-report.md` records `Composition verdict: delivered` after Slice 01, Slice 02, and Slice 03 CDC verification. | Attested by arc close, reproduced at project close. |
| P-2 | Skill bundles use path references that resolve from both source clone entry points and generated zip/unzipped package entry points. | From implementation checkout, run the final package-path validation target over all skill zips and inspect zero unresolved packaged-path failures. | serious | project-plan | open | | Composition row; must be reproduced at project scale. |
| P-3 | Repo-only, provenance-only, and example project paths are explicitly classified instead of left as ambiguous missing package files. | Run the final package-path validation target and inspect its classified exception report. | correctness | project-plan | open | | The final accepted target name is chosen by Arc 01/02. |
| P-4 | Makefile packaging owns any required staging transforms and package-path validation. | `rg -n "check-package-path|package path|staging" Makefile scripts README.md` from implementation checkout. | correctness | project-plan | open | | Exact target/script names are intentionally not fixed before Arc 01. |
| P-5 | CCDP has a documented source and distributable package use path. | `rg -n "ccdp.*zip|CCDP.*package|protocol package" Makefile README.md protocols/ccdp` from implementation checkout. | correctness | project-plan | open | | Detailed in Arc 03 unless reprioritized. |
| P-6 | Release-facing docs explain cloned-source and zip/unzipped workflows. | `rg -n "source clone|zip|unzipped|package root|repo-only" README.md` from implementation checkout. | polish | project-plan | open | | |
