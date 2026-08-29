# CC Prompt: Slice 01 Package Path Audit

You are implementing Slice 01 for
`project01-harmonise-paths/arc01-distribution-path-contract`.

## Planning Inputs

Read these files first:

1. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
2. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/ledger.md`
3. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/arc-plan.md`
4. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/ledger.md`
5. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/slice-plan.md`
6. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/ledger.md`

Work in the implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Objective

Create an evidence-backed package path audit report at:

`workbench/2026.08.29-package-path-audit.md`

The report must inventory the generated zip packages, reproduce package-context
path misses, classify the misses, and recommend a concrete source/package path
contract for later implementation slices.

## Required Investigation

1. Read the top-level `Makefile`, especially `INSTALL_ZIPS`, `CF_FILES`, and
   `pack_skill`.
2. Inspect current zip files and, if needed, rebuild them with the existing
   Make targets before scanning.
3. Scan Markdown inside each generated zip for references that appear to point
   at repo-root files but do not resolve inside the package root.
4. Classify each mismatch as one of:
   - bundled-reference
   - source-clone-reference
   - repo-only/provenance
   - example-project path
   - external URL
   - parser false positive
5. Recommend which later fixes should be:
   - source edits
   - staging-time Make/Bash transforms
   - package layout changes
   - validation exceptions
   - CCDP package work

## Boundaries

Do not bulk-edit mature language guides or skill files in this slice. Do not
add the final validation gate. Do not add CCDP package targets. This slice is
diagnosis plus contract.

A small temporary audit script under `/private/tmp` is acceptable. If you use
one, include the script or enough command detail in the report for CDC to
reproduce the scan.

## Ledger and Close

As you work, update:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/ledger.md`

with `attested` evidence for every completed row.

When finished, write:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/closing-report.md`

The closing report must walk every row F-1 through F-7 and include a
`Bubble-up to Arc 01` section that states what Slice 02 should do next.
