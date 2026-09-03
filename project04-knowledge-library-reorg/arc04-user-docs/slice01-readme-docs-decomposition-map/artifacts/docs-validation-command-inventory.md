# Docs Validation Command Inventory

Date: 2026-09-02
Slice: Arc04 Slice01 README and docs decomposition map

## validation command inventory

This inventory records validation commands for later Arc04 README/docs source
edit slices. Slice01 itself is read-only for source.

## Source Status Commands

- `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short --untracked-files=all`
- `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check`

## README links and docs links

Candidate checks for README/docs link repair slices:

- `rg -n "\\[[^\\]]+\\]\\([^\\)]+\\)|https?://|docs/|knowledge/|protocols/|templates/|Makefile|package" README.md docs`
- `rg -n "docs/dev|docs/design|CODE-AUDIT|AI-ENGINEERING|PROJECT-MANAGEMENT|SUBAGENT|LEDGER-DISCIPLINE|CONTRIBUTION-TICKET|templates/" README.md docs`
- `find docs -maxdepth 2 -type f | sort`
- `rg -n "^#{1,4} " README.md docs`

Later slices may add a dedicated Markdown link checker if the repository has
one by then. If not, use targeted `rg`, `test -e`, and package-path validation
for every touched link.

## Package Validation Surfaces

Run package-facing checks after documentation source edits that touch package,
skill, protocol, or source-root references:

- `make check-skills`
- `make check-package-paths`
- `make all`
- `make ccdp-package`
- `make check-ccdp-package`

`make help` remains the quick source of current command names.

## Current Read-Only Findings

Observed before Slice01 planning edits:

- source `git status --short --untracked-files=all`: clean
- current `docs/` file list: `docs/ORIGINS.md`
- README links include `docs/ORIGINS.md`, `knowledge/`, `Makefile`,
  `protocols/ccdp`, and `templates/GUIDE.md`
- stale README/docs route candidates include `docs/dev`, old framework doc
  paths in `docs/ORIGINS.md`, and moved template paths

These findings define later Arc04 validation targets. They do not authorize
source edits in Slice01.
