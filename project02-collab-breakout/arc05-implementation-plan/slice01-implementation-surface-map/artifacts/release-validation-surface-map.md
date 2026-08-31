# Release Validation Surface Map

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice01-implementation-surface-map
status: proposed-done
source-files-edited: false
```

## Package And Build Surface

Read-only inspection of the current source checkout shows these release
surfaces:

| Surface | Current fact | Planning consequence |
|---------|--------------|----------------------|
| `INSTALL_ZIPS` | Current install zips include `collaboration-framework.zip` plus the existing domain/tooling skill zips. | New accepted component zips are not represented yet. Slice03 must plan the package list change. |
| `ALL_SKILL_FILES` | Current validation list includes top-level `SKILL.md` plus domain/tooling `SKILL.md` files. | New component `SKILL.md` entrypoints must be added before `make check-skills` covers them. |
| `CF_FILES` | Current collaboration-framework bundle includes top-level `SKILL.md`, posture, methodology, PM docs, audit, coverage, delegation, contribution, and templates. | This explicit list is the main current monolith surface to split or recompose. |
| `collaboration-framework.zip` | Current generated zip root is `collaboration-framework/`; it contains the monolithic `CF_FILES` set. | Keep root name for the accepted composer, but plan content reduction and routes. |
| `make collab-framework` | Builds current top-level skill package and validates top-level `SKILL.md` description. | Must still validate composer behavior after breakout. |
| `make all` | Builds all skill bundles, including the current collaboration framework and domain/tooling bundles. | Must include accepted component packages after implementation. |
| `make check-skills` | Validates every listed `SKILL.md` description length. | Must include all accepted component entrypoints. |
| `make check-package-paths` | Builds all zips and validates package-context Markdown paths using `package-path-exceptions.tsv`. | Must run after Markdown links, package contents, Makefile package lists, or path exceptions change. |
| `package-path-exceptions.tsv` | Contains warnings and explicit exceptions, including current `collaboration-framework.zip` source-only/provenance placeholders. | Prefer package-local link repairs; add exceptions only with explicit classification and rationale. |
| generated zip artifacts | Root-level `*.zip` files are ignored by `.gitignore` and are release artifacts, not ordinary source changes. | Implementation slices should not commit generated zips unless release policy changes. |

## CCDP Boundary

CCDP is separate from the accepted collaboration-framework component set.

| Surface | Current fact | Planning consequence |
|---------|--------------|----------------------|
| `CCDP_NAME := ccdp` | Makefile defines CCDP as a separate protocol package. | Preserve CCDP separation. |
| `make ccdp-package` | Builds `ccdp.zip` with one `ccdp/` package root. | Do not fold CCDP into `INSTALL_ZIPS`. |
| `make check-ccdp-package` | Validates zipped and unzipped CCDP package shape and package-local links. | Run only when CCDP source/package surfaces are touched. |
| `ccdp.zip` | Current generated zip root is `ccdp/`. | Adjacent protocol distribution, not an accepted Project02 skill component. |
| `protocols/ccdp/` | Source protocol tree includes README, assembled spec, chapters, JSON corpus, visual guide, templates, and tool source. | Keep source references separate from skill package roots. |

## README And SKILL.md Release Surface

| Surface | Current state | Required Slice03 planning question |
|---------|---------------|------------------------------------|
| `README.md` collaboration-framework section | Describes one `/collaboration-framework` skill and one composed framework body. | How should README introduce eight components while preserving the daily-driver composer? |
| `README.md` building/installing section | Documents `make all`, `make skills`, `make collab-framework`, `make install`, `make check-skills`, and `make check-package-paths`. | Which new component build targets and package names should appear? |
| `README.md` CCDP section | Documents source clone CCDP entrypoints and `ccdp.zip` package use. | Preserve CCDP separation and do not make CCDP look like a skill component. |
| Top-level `SKILL.md` | Current monolithic entrypoint with `name: collaboration-framework` and `version: 1.4.1`. | Plan composer entrypoint, route table, and version bump/`version-history.md` split. |
| Component `SKILL.md` files | Do not exist yet for seven new component roots. | Slice02 must plan entrypoint files before Slice03 plans validation list changes. |

## Validation Command Matrix

| Change type | Validation command | Owner after breakout |
|-------------|--------------------|----------------------|
| Component or composer `SKILL.md` description/frontmatter changes | `make check-skills` | `engineering-methods` gate, per-component contract field. |
| Package contents, Markdown links, package-local references, package list, or exceptions | `make check-package-paths` | `engineering-methods` gate, per-component contract field. |
| Composer package behavior | `make collab-framework` plus `make check-package-paths` | `collaboration-framework` with `engineering-methods` gate. |
| Full skill package release surface | `make all` plus `make check-package-paths` | `engineering-methods` release gate. |
| CCDP protocol package changes | `make ccdp-package` and `make check-ccdp-package` | CCDP package owner, outside Project02 component set. |

## Package-Path Gate Inputs For Slice02 And Slice03

- Every accepted component contract must name source path, package path, zip
  root, package-local links, README route, `SKILL.md` route, Makefile package
  list impact, generated zip behavior, validation commands, component owner,
  and version-history responsibility.
- `engineering-methods` owns the source/package/release gate documentation,
  but every component owns its own package/source contract.
- Existing `collaboration-framework.zip` references to `knowledge/<domain>`
  placeholders are explicit source-only/provenance exceptions today; new
  component packages should avoid inheriting those exceptions blindly.
- Generated zip behavior remains a validation surface, not a planning
  assertion.
