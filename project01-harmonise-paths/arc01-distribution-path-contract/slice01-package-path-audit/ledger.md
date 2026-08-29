# Slice 01: Package Path Audit Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | The audit identifies the exact top-level zip set under review from the current Makefile. | `rg -n "^INSTALL_ZIPS|\\.zip" Makefile` and inspect the report's "Zip set" section. | correctness | slice-plan | open | | |
| F-2 | The audit inspects actual generated zip contents rather than only source Markdown. | Inspect the report for `unzip -l` or equivalent archive-inspection evidence across the zip set. | serious | slice-plan | open | | |
| F-3 | The audit reproduces package-context path misses for bundled Markdown references. | Inspect the report for a repeatable scan command or script plus counts by zip. | serious | slice-plan | open | | |
| F-4 | Each observed mismatch is classified as bundled-reference, source-clone-reference, repo-only/provenance, example-project path, external URL, or parser false positive. | Inspect the report's classification table and confirm no unclassified miss bucket remains. | correctness | slice-plan | open | | If the class names change, the report must map old to new. |
| F-5 | The report recommends a path contract that supports both cloned-source and zip/unzipped use. | `rg -n "Path contract|source clone|package root|repo-only|staging" workbench/2026.08.29-package-path-audit.md` | serious | slice-plan | open | | |
| F-6 | The report distinguishes source edits, staging-time transforms, package layout changes, validation exceptions, and CCDP package work. | `rg -n "Disposition by fix type|source edit|staging|package layout|validation|CCDP" workbench/2026.08.29-package-path-audit.md` | correctness | slice-plan | open | | |
| F-7 | The close report walks every ledger row and bubbles findings up to Arc 01. | `test -f project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/closing-report.md && rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|Bubble-up to Arc 01" project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/closing-report.md` | correctness | slice-plan | open | | |
