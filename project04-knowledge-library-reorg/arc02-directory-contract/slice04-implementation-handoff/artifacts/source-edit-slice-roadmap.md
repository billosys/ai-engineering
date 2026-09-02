# Source-Edit Slice Roadmap

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice04-implementation-handoff
artifact: source-edit-slice-roadmap
artifact-status: implementation handoff input
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This roadmap proposes likely Arc03 source-edit slices. It is planning only and
not source-edit authorization. Arc03 implementation planning may refine slice
boundaries, but should preserve this order unless a re-entry condition is met.

## Roadmap

| Order | Proposed Arc03 slice | Primary work | Required validation gate |
|-------|----------------------|--------------|--------------------------|
| 1 | Preflight source status and impact map | Record source status, touched surfaces, package targets, known generated package roots, and exact validation commands before edits. | `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short`; source `diff --check`; no source edits beyond approved preflight artifacts. |
| 2 | Top-level SKILL.md compatibility decision | Select and implement validated shim, replacement route, or explicit no-shim path before moving composer source. | `make check-skills`; `make collab-framework`; README/SKILL route review. |
| 3 | Mechanical move: collaboration-framework source | Move composer/framework substrate toward `knowledge/collaboration-framework/` while preserving package root behavior and source prose. | source status; source `diff --check`; `make collab-framework`; package-local link review. |
| 4 | Mechanical move: Project02 component roots | Add framework/operational component source roots under `knowledge/<component>/` where accepted, preserving component roles and independent loadability. | `make check-skills`; component target review; `make all` if package targets are added. |
| 5 | Mechanical move: method/provenance material | Move accepted method/source/provenance material under its owning `knowledge/` root, including only authorized Project03 `concept-card-method` material. | `make check-skills` after entrypoints exist; preservation review; package target review. |
| 6 | Template ownership pass | Move owner-local templates under owning source roots and preserve top-level `templates/` only for cross-cutting support exceptions. | package-local link repair; `make check-package-paths`; `make all` if bundled payloads change. |
| 7 | Biome multi-entrypoint validation pass | Preserve `knowledge/biome/` as a multi-entrypoint source root and confirm generated package roots. | `make check-skills`; `make check-package-paths`; generated package inspection. |
| 8 | CCDP separation pass | Keep `protocols/ccdp/` separate while updating any wrapper or route links that reference it. | `make ccdp-package`; `make check-ccdp-package`; `INSTALL_ZIPS` review. |
| 9 | Wrapper and migration note pass | Add wrapper and migration note routes for moved public paths without duplicating moved source prose. | README/docs route review; package-local link checks. |
| 10 | Package/list update pass | Synchronize `Makefile`, `CF_FILES`, `ALL_SKILL_FILES`, `INSTALL_ZIPS`, and package targets after moved files exist. | `make check-skills`; `make check-package-paths`; `make all`; `make collab-framework` if composer touched. |
| 11 | Package-local link repair pass | Repair relative links inside generated packages and source docs before exceptions. | `make check-package-paths`; generated package inspection. |
| 12 | Package-path exception pass | Add narrow exceptions only after repair attempts fail or are inappropriate; obtain operator approval for persistent exceptions or accepted warnings. | exception-policy review; operator approval record; `make check-package-paths`. |
| 13 | Arc03 implementation reconciliation | Confirm the moved layout, package roots, validation gates, and compatibility surfaces compose before Arc03 close. | source status; source `diff --check`; `make all`; package inspection. |
| 14 | Later prose/doc routing | Route README/end-user docs prose to Arc04 and public skill kind/topology wording to Arc05. | Arc04 and Arc05 planning gates, not Arc03 source-move gates. |

## Ordering Rules

- Start with preflight and source status.
- Resolve the top-level `SKILL.md` compatibility shim, replacement route, or
  no-shim path before moving composer source.
- Keep mechanical move work before prose rewrite work.
- Keep wrapper and migration note work separate from source-prose rewrites.
- Perform package/list update work after moved files exist.
- Attempt package-local link repair before adding any package-path exception.
- Keep CCDP under `protocols/ccdp/` and outside installable skill packages.
- Preserve Arc04 for end-user docs and Arc05 for public vocabulary.

## Validation Gate Families

- Source hygiene: source status, source `diff --check`, source-prose
  preservation review.
- Skill gates: `make check-skills`, entrypoint/frontmatter review, installed
  route review.
- Package gates: `make check-package-paths`, `make all`, generated package
  inspection, package-local link repair.
- Composer gates: `make collab-framework`, `CF_FILES` review, selected-file
  transitional packaging review.
- CCDP gates: `make ccdp-package`, `make check-ccdp-package`, `INSTALL_ZIPS`
  review.
- Compatibility gates: `README`, `SKILL.md`, `AGENTS.md`, `CLAUDE.md`,
  wrapper, and migration note review.

## Re-Entry Conditions

- Re-enter Arc02 if the roadmap cannot preserve mechanical moves before prose
  rewrites.
- Re-enter the accepted contract if generated package behavior contradicts the
  source/package root separation.
- Re-enter operator gates if persistent package-path exceptions, accepted
  warnings, or top-level `SKILL.md` decisions remain unresolved.

This roadmap does not open Arc03 and does not create Arc03 source-edit slice
packets.
