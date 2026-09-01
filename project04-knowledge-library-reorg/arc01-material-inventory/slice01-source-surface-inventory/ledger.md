# Slice 01: Source Surface Inventory

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Current source checkout top-level surfaces and key subtrees are inventoried | `rg -n "README.md|SKILL.md|docs/|knowledge/|templates/|protocols/|Makefile|package-path-exceptions.tsv|scripts/|assets/|site/|workbench/" artifacts/current-source-surface-map.md` | serious | slice-plan | done | reproduced: CDC reran the Verify command on 2026-09-01 and observed matches; see `cdc-verification.md`. | |
| F-2 | `docs/` files and directories are classified by current material role | `rg -n "docs/|end-user documentation|framework/operational|method material|extraction guidance|design/dev|project-management|source-like|substrate-like" artifacts/material-role-classification.md` | serious | slice-plan | done | reproduced: CDC reran the Verify command on 2026-09-01 and observed matches; see `cdc-verification.md`. | |
| F-3 | `knowledge/` files and directories are classified by current material role | `rg -n "knowledge/|domain/tooling|skill entrypoint|guides/|concept-cards/|extraction-metadata|sources/|tools/|workbench/" artifacts/material-role-classification.md` | serious | slice-plan | done | reproduced: CDC reran the Verify command on 2026-09-01 and observed matches; see `cdc-verification.md`. | |
| F-4 | Source validation, package, link, and compatibility surfaces affected by future moves are mapped | `rg -n "Makefile|package-path-exceptions.tsv|check-skills|check-package-paths|generated zip|INSTALL_ZIPS|ALL_SKILL_FILES|README link|AGENTS.md|CLAUDE.md|CCDP" artifacts/source-validation-surface-map.md` | serious | slice-plan | done | reproduced: CDC reran the Verify command on 2026-09-01 and observed matches; see `cdc-verification.md`. | |
| F-5 | Artifacts identify Project02/Project03 imported project-level materials as later inputs without treating them as source inventory | `rg -n "Project02|Project03|imported artifact|later Slice02 input|not source inventory" artifacts/current-source-surface-map.md artifacts/material-role-classification.md artifacts/source-validation-surface-map.md` | correctness-grade | slice-plan | done | reproduced: CDC reran the Verify command on 2026-09-01 and observed matches; see `cdc-verification.md`. | |
| F-6 | Early atomic/composite observations are either source-backed or explicitly deferred to Slice03 | `rg -n "atomic|composite|Rust|collaboration-framework|deferred to Slice03|source-backed" artifacts/material-role-classification.md artifacts/current-source-surface-map.md` | correctness-grade | slice-plan | done | reproduced: CDC reran the Verify command on 2026-09-01 and observed matches; see `cdc-verification.md`. | |
| F-7 | No source checkout files are edited by this slice | `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short` | serious | slice-plan | done | reproduced: CDC reran the Verify command on 2026-09-01 and observed no output; see `cdc-verification.md`. | Expected result met: no changes attributable to this slice in the source checkout. |

## What Worked

- Required reading in the prompt cleanly separated source checkout inspection
  from planning checkout artifact writes.
- Depth-limited `find` plus targeted `rg` avoided treating the very large
  `knowledge/` and `workbench/` trees as undifferentiated file dumps.
- Recording source commands inside each artifact gives CDC concrete rerun
  handles for attested evidence.

## Closure

Verified-closed by CDC on 2026-09-01. See `cdc-verification.md`.

Rows: 7. Done: 7. Deferred: 0. No-op: 0.
