# Migration Sequence Plan

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice03-migration-validation-plan
artifact: migration-sequence-plan
artifact-status: implementation planning input
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This migration sequence makes the verified Slice02 accepted directory and
source/package root contract executable for later Arc03 source-edit slices.
It is planning only, not source-edit authorization. Arc03 owns source-edit
slices, and Arc05 owns final public vocabulary.

## Sequencing Principle

Arc03 source edits should run in small slices with mechanical moves before
prose rewrites. Each implementation slice should touch one coherent surface,
run its validation gates, and record package-local link repair before adding
any package-path exception.

## Ordered Sequence

| Phase | Work class | Planned actions | Required gates |
|-------|------------|-----------------|----------------|
| 0 | preflight | Confirm source checkout status, record touched surfaces, and restate that source-files-edited is intentionally changing only in Arc03. | `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short`; `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check`. |
| 1 | compatibility shim decision | Choose the top-level SKILL.md path: validated shim, replacement route, or explicit no-shim decision. Preserve `AGENTS.md` and `CLAUDE.md` compatibility behavior. | `make check-skills`; `make collab-framework`; route review for `README`, `SKILL.md`, `AGENTS.md`, and `CLAUDE.md`. |
| 2 | mechanical moves | Move source-like framework, method, provenance, and owner-local template material to accepted `knowledge/` roots without prose rewrite. Preserve history with mechanical moves. | source status, source diff hygiene, source-prose preservation review, package impact review. |
| 3 | Project02 component roots | Place framework/operational components under `knowledge/<component>/`; place composer source under `knowledge/collaboration-framework/` when the shim route is ready. | `make check-skills`; `make collab-framework`; component package target review. |
| 4 | Project03 method root | Add or reserve `knowledge/concept-card-method/` only when implementation authorization exists; do not claim package availability early. | `make check-skills`; package target review only after entrypoint exists. |
| 5 | Biome edge-case preservation | Preserve `knowledge/biome/` as a multi-entrypoint source root and verify generated package roots remain correct. | `make check-skills`; `make check-package-paths`; generated package inspection. |
| 6 | CCDP separation | Preserve `protocols/ccdp/`; update only route links or wrapper pages if implementation scope touches them. Do not add CCDP to installable skill packages. | `make ccdp-package`; `make check-ccdp-package`; `INSTALL_ZIPS` review. |
| 7 | wrapper and migration note pass | Add wrapper docs or migration note pages for old human-facing `docs/` routes that now point to moved substrate. | README/docs route review; package-local link checks. |
| 8 | package/list update | Update `Makefile`, `CF_FILES`, `ALL_SKILL_FILES`, `INSTALL_ZIPS`, package targets, and package-local payloads after moved files exist. | `make check-skills`; `make check-package-paths`; `make all`; `make collab-framework` when composer touched. |
| 9 | package-local link repair | Repair package-local link paths inside generated packages and source docs before exceptions. | `make check-package-paths`; generated package inspection. |
| 10 | package-path exception handling | Add only narrow exception rows for intentional residual cases after repair attempts fail or are inappropriate. | policy review against `package-path-exception-policy.md`; operator approval for persistent warnings. |
| 11 | prose rewrite | Rewrite public explanation only after mechanical layout and package behavior are stable. | Arc04/Arc05 gates; README/docs review. |

## Surface Sequencing

| Surface | Sequence rule |
|---------|---------------|
| `docs/` | Move substrate-like files mechanically before rewriting end-user explanation; keep wrapper or migration note routes where old paths were public. |
| `knowledge/` | Add accepted roots only when the owning implementation slice can also update validation lists and package behavior. |
| `templates/` | Move owner-local templates with the owning component, method, skill, or protocol package; keep top-level only for cross-cutting support exceptions. |
| `protocols/ccdp` | Keep separate throughout; update links and protocol package gates without mixing CCDP into installable skill packages. |
| `README` | Keep concise route-map changes separate from source moves; deep public prose belongs to Arc04. |
| `SKILL.md` | Preserve top-level SKILL.md until a validated shim, replacement route, or no-shim decision is accepted for implementation. |
| `AGENTS.md` | Update only when accepted paths or validation commands change; preserve planning/source checkout distinction and commit trailers. |
| `CLAUDE.md` | Preserve symlink compatibility intent unless an explicit implementation decision changes it. |
| `Makefile` | Update after target files exist so `CF_FILES`, `ALL_SKILL_FILES`, `INSTALL_ZIPS`, and package targets can be validated against real paths. |

## Compatibility Classes

- Compatibility shim: a top-level or old-path file that preserves load or
  reader behavior while source material moves to its accepted root.
- Wrapper: a reader-facing file that routes from an old public path to the new
  source or explanation path.
- Migration note: a dated note explaining whether an old path is deprecated,
  transitional, or retained as an explicit exception.
- Package/list update: Makefile, package manifest, or package list changes
  that synchronize generated packages with accepted source roots.
- Package-local link repair: relative link updates inside package payloads so
  generated packages validate without broad exceptions.
- Package-path exception: a visible, reasoned residual warning or allowed
  divergence after repair has been attempted.

## Re-Entry Conditions

- Re-enter Slice02 if a later implementation slice cannot preserve the
  accepted `knowledge/<component>/` default without violating Project02
  component roles or composer behavior.
- Re-enter the top-level SKILL.md decision before moving composer source if no
  validated shim, replacement route, or no-shim path can preserve load routes.
- Re-enter CCDP policy only if protocol package validation proves
  `protocols/ccdp` cannot remain separate.
- Re-enter package-path exception policy if package-local link repair requires
  broad exceptions rather than narrow rows.
