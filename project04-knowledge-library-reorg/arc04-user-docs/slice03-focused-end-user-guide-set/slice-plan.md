# Slice 03: Focused End-User Guide Set

```yaml
project: project04-knowledge-library-reorg
arc: arc04-user-docs
slice: slice03-focused-end-user-guide-set
status: open
opened-by: CDC
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: true
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Expand the seven focused `docs/*.md` stubs created by Slice02 into usable
end-user guides that explain the repository's materials without turning
`docs/` back into the raw knowledge substrate.

## Scope

In scope:

- Expand `docs/repository-overview.md`.
- Expand `docs/skill-library.md`.
- Expand `docs/collaboration-framework.md`.
- Expand `docs/knowledge-library-anatomy.md`.
- Expand `docs/building-and-installing.md`.
- Expand `docs/protocols.md`.
- Expand `docs/contributing.md`.
- Preserve the concise README orientation and update README navigation only if
  the guide expansion exposes a narrow consistency defect.
- Repair `docs/ORIGINS.md` only if a narrow route or link defect is discovered
  while expanding the focused guides.
- Use practical, provisional skill-language examples only where needed for
  reader clarity.

Out of scope:

- Finalizing public skill-kind or atomic/composite vocabulary; Arc05 owns that.
- Moving knowledge substrate back into `docs/`.
- Moving source files between `docs/`, `knowledge/`, `templates/`, or
  `protocols/`.
- Changing `Makefile`, package roots, package-path exceptions, `SKILL.md`, or
  generated zips unless a narrow documentation-link defect creates an explicit
  operator gate.
- Expanding Slice04 reconciliation; Slice04 owns final link/navigation
  reconciliation after guide content lands.

## Expected Artifacts

- `artifacts/focused-guide-expansion-map.md`
- `artifacts/docs-content-boundary-evidence.md`
- `artifacts/readme-navigation-preservation.md`
- `artifacts/source-change-and-validation-evidence.md`

## Verification Approach

CC will commit source edits first, then commit the planning close packet. The
source commit must explicitly list every edited source file. Generated zips
must not be committed.

Required validation includes:

- source `git status --short --untracked-files=all`;
- source `git diff --check`;
- targeted README/docs route checks carried forward from Slice02;
- `find docs -maxdepth 2 -type f | sort`;
- README/docs heading scan;
- `make check-skills`;
- `make check-package-paths`;
- `make all`;
- `make ccdp-package`;
- `make check-ccdp-package`;
- planning `git diff --check`;
- all six Slice03 ledger verifier commands;
- final source and planning `git status --short`.

## Exit Criteria

- The seven focused guide files provide enough context for an end user to
  understand what the repository contains, when to use each major surface, and
  where the actual material substrate lives.
- The guide set preserves the `docs/` versus `knowledge/` boundary.
- The README remains a concise orientation and route map.
- Skill-kind and atomic/composite language remains provisional and explicitly
  bounded for Arc05.
- Source and planning commits use explicit file lists and required trailers.
- Source and planning worktrees finish clean.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc04.
