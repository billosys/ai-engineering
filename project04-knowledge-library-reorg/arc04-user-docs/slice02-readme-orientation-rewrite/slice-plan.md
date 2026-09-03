# Slice 02: README Orientation Rewrite

```yaml
project: project04-knowledge-library-reorg
arc: arc04-user-docs
slice: slice02-readme-orientation-rewrite
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

Rewrite the top-level `README.md` into a concise repository orientation that
matches the post-Arc03 layout, points readers toward focused `docs/` guides,
and repairs stale documentation routes discovered by Slice01.

## Scope

In scope:

- Edit `README.md` as the primary source file.
- Keep README concise: orient, name the repository shape, provide quick
  build/install/package commands, and route deeper explanations to `docs/`.
- Create minimal focused-doc stubs under `docs/` if needed so README links do
  not point to missing files before Slice03 expands the guide set.
- Preserve the `docs/` versus `knowledge/` distinction.
- Preserve CCDP as a separate protocol distribution under `protocols/ccdp/`.
- Use only provisional practical language for skill kinds and atomic/composite
  topology; Arc05 owns final public vocabulary.
- Repair stale README routes discovered by Slice01, including `docs/dev`,
  former framework docs under `docs/`, and moved template paths.

Out of scope:

- Expanding the full focused guide content; Slice03 owns that.
- Finalizing public skill-kind or atomic/composite vocabulary; Arc05 owns that.
- Moving source material between `docs/`, `knowledge/`, `templates/`, or
  `protocols/`.
- Changing `Makefile`, package roots, package-path exceptions, or generated
  zips unless a narrow README route defect requires a documented follow-up
  gate rather than a silent change.
- Rewriting `docs/ORIGINS.md` unless a narrow link repair is needed to keep
  README navigation coherent.

## Expected Artifacts

- `artifacts/readme-orientation-change-map.md`
- `artifacts/readme-route-repair-evidence.md`
- `artifacts/focused-doc-stub-register.md`
- `artifacts/source-change-and-validation-evidence.md`

## Verification Approach

CC will commit source edits first, then commit the planning close packet. The
source commit must explicitly list every edited source file. Generated zips
must not be committed.

Required validation includes:

- source `git status --short --untracked-files=all`;
- source `git diff --check`;
- targeted README/docs route checks from Slice01;
- `make check-skills`;
- `make check-package-paths`;
- `make all`;
- `make ccdp-package`;
- `make check-ccdp-package`;
- planning `git diff --check`;
- final source and planning `git status --short`.

## Exit Criteria

- `README.md` is a concise orientation rather than the long subject-matter
  home for framework, skill-library, build/install, CCDP, and contribution
  explanations.
- README routes to existing `docs/` files, minimal stubs created in this
  slice, or existing source/package entrypoints.
- Stale README routes from Slice01 are repaired or explicitly recorded with a
  re-entry condition.
- Arc05 vocabulary boundaries are preserved.
- Source and planning commits use explicit file lists and required trailers.
- Source and planning worktrees finish clean.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc04.
