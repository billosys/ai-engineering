# Validation And Compatibility Matrix

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice03-migration-validation-plan
artifact: validation-and-compatibility-matrix
artifact-status: implementation planning input
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This validation matrix maps accepted Slice02 surfaces to the command, review,
and compatibility gates that later Arc03 source-edit slices must run. It is
planning only and does not edit the source checkout.

## Global Gates

Every Arc03 source-edit slice should run:

- `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short` before
  and after source edits to disclose the exact touched source surfaces.
- `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check` before
  commit for diff hygiene.

## Matrix

| Surface or change | Required validation gates | Compatibility review |
|-------------------|---------------------------|----------------------|
| `SKILL.md`, `SKILL*.md`, frontmatter, descriptions, or source roots | `make check-skills`; source `status --short`; source `diff --check`. | Verify every live entrypoint appears in `ALL_SKILL_FILES`; check installed-skill route wording. |
| Domain/tooling skills under `knowledge/<slug>/` | `make check-skills`; `make check-package-paths` when package roots or links change. | Confirm package root follows frontmatter or accepted Makefile target. |
| Project02 components under `knowledge/<component>/` | `make check-skills`; component target review; `make all` when packages are generated. | Confirm component packages preserve Project02 accepted roles and independent loadability. |
| `knowledge/collaboration-framework/` composer source | `make collab-framework`; `make check-skills`; `make check-package-paths`; generated package inspection. | Confirm selected-file transitional packaging or replacement packaging preserves daily-driver composer behavior. |
| Top-level SKILL.md compatibility surface | `make collab-framework`; `make check-skills`; README/SKILL route review. | Confirm validated shim, replacement route, or explicit no-shim decision before moving the composer source. |
| Biome multi-entrypoint source root | `make check-skills`; `make check-package-paths`; generated package inspection. | Confirm `knowledge/biome/` can still generate each expected package root. |
| Project03 `concept-card-method` planned root | `make check-skills` after entrypoint exists; package checks only after package target exists. | Confirm it remains Project03 planned/not live source until implementation lands. |
| `templates/` cross-cutting or owner-local moves | package-local link review; `make check-package-paths`; `make all` if bundled packages change. | Confirm owner-local templates live with their owner and top-level remnants have explicit exceptions. |
| `protocols/ccdp` | `make ccdp-package`; `make check-ccdp-package`; source `diff --check` if touched. | Confirm CCDP remains separate from `INSTALL_ZIPS` and installable skill package behavior. |
| `README.md` | README route review; `make check-package-paths` if links to package paths change. | Confirm README stays a concise route map; defer deep prose to Arc04. |
| `docs/` wrappers and migration notes | README/docs route review; package-local link checks when packaged. | Confirm wrappers route rather than duplicate moved source prose. |
| `AGENTS.md` | Instruction review; source/planning checkout boundary review. | Confirm validation commands, package paths, and commit trailer convention remain current. |
| `CLAUDE.md` | Symlink or compatibility review. | Confirm symlink intent remains unless explicitly changed. |
| `Makefile`, `CF_FILES`, `ALL_SKILL_FILES`, `INSTALL_ZIPS`, package targets | `make check-skills`; `make check-package-paths`; `make all`; `make collab-framework` when composer payload changes. | Confirm generated package lists match accepted source roots and CCDP is not in installable skill zips. |
| Package-local links | `make check-package-paths`; generated package inspection. | Repair links before package-path exceptions. |
| Generated package payloads | generated package inspection; `make check-package-paths`; `make all`. | Treat generated package output as authoritative package evidence. |

## Generated Package Inspection

Generated package inspection means checking the generated zip or unpacked
package root for:

- expected `SKILL.md` or `SKILL*.md` entrypoints;
- package-local relative links;
- expected support files and templates;
- absence of source-only planning files unless intentionally bundled;
- expected package root names after frontmatter, selected-file,
  multi-entrypoint, or protocol rules are applied.

## Compatibility Obligations

- Package-local links must be repaired before package-path exceptions.
- Selected-file `collaboration-framework` packaging remains a transitional
  exception class until replacement package behavior is validated.
- `knowledge/biome/` remains a multi-entrypoint source root.
- `protocols/ccdp` remains separate and must not be added to `INSTALL_ZIPS`.
- `AGENTS.md` and `CLAUDE.md` are compatibility surfaces, not skill kinds.
- Public vocabulary for skill kind and topology remains Arc05 work.

## Re-Entry Conditions

- Re-enter migration sequencing if a source-edit slice cannot isolate
  mechanical moves from prose rewrites.
- Re-enter package policy if generated package roots contradict accepted
  source/package root rules.
- Re-enter CCDP policy only if CCDP validation cannot preserve protocol
  separation.
- Re-enter Slice02 if the top-level SKILL.md compatibility decision cannot be
  implemented without changing the accepted directory contract.
