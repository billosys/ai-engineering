# Source And Package Root Contract

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice02-accepted-directory-contract
artifact: source-package-root-contract
artifact-status: accepted planning contract
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This artifact defines source root rule and package root rule behavior as
separate axes. A source root is where source material lives in the repository.
A package root is the root exposed by a generated or installed package. The
contract rejects a universal one-source-root-to-one-package-root assumption.

## Global Rules

| Axis | Accepted rule | Notes |
|------|---------------|-------|
| Source root rule | Default skill and method source material lives under `knowledge/<slug>/`. | This covers current domain/tooling skills and accepted future framework/operational or method roots. |
| Package root rule | Package roots follow frontmatter `name:`, accepted component/package names, selected-file package definitions, protocol package behavior, or explicit multi-entrypoint rules. | Package roots do not have to equal source roots. |
| Frontmatter rule | When a source root has a `SKILL.md` or `SKILL*.md`, frontmatter `name:` is the authoritative package identity unless an accepted Makefile target overrides it. | Applies to most current `knowledge/` skills. |
| Selected-file rule | Selected-file packages are explicit exceptions and must list payload files and validation gates. | Applies to current `collaboration-framework`; may become transitional. |
| Multi-entrypoint rule | One source root may expose more than one package root when multiple accepted entrypoints exist. | Applies to Biome. |
| Protocol rule | Protocol packages remain outside installable skill package roots unless an explicit protocol-policy decision changes that. | Applies to CCDP. |

## Surface Contracts

| Surface class | Source root rule | Package root rule | Accepted status |
|---------------|------------------|-------------------|-----------------|
| Current domain/tooling skills | Keep `knowledge/<slug>/`. | Use frontmatter `name:` or current Makefile package target. | Accepted. |
| Framework/operational components | Use `knowledge/<component>/` by default. | Use accepted component package name. | Accepted as planning contract; implementation pending. |
| `collaboration-framework` composer | Target `knowledge/collaboration-framework/` for source material, with top-level `SKILL.md` preserved until a compatibility decision is implemented. | Keep package root `collaboration-framework`; selected-file packaging remains allowed as transitional exception. | Accepted with compatibility exception. |
| Project02 specialist components | Use `knowledge/<component>/` for independently loadable components. | Use component package names from the accepted Project02 architecture. | Accepted as planned roots, not live source. |
| Project03 `concept-card-method` | Reserve `knowledge/concept-card-method/`. | No live package root until implementation; future package root should be `concept-card-method` unless implementation evidence changes it. | Accepted planned method root. |
| Biome | Preserve `knowledge/biome/` as one source root. | Preserve `biome-js-linter` and `biome-linter` package roots or any current validated package roots. | Accepted multi-entrypoint edge case. |
| Support templates | Cross-cutting templates may remain in top-level `templates/`; owner-local templates move under the owning source root. | Package-local under owning package when bundled. | Accepted with explicit exception rows for top-level remnants. |
| CCDP | Keep `protocols/ccdp/`. | Keep CCDP package behavior separate from installable skills; do not add CCDP to `INSTALL_ZIPS`. | Accepted protocol separation. |
| README and compatibility files | Keep top-level. | Not package roots except when explicitly bundled as documentation or package payload. | Accepted compatibility surfaces. |

## Current Edge Cases

### `collaboration-framework`

`collaboration-framework` remains the accepted daily-driver composer from
Project02. The current package may be built from selected files rather than a
single source root, and this remains a valid transitional selected-file rule.
When Arc03 moves source material, the implementation must preserve package
root behavior and installed route wording. It must not make specialist
components disappear behind the composer.

### Biome

Biome is the accepted multi-entrypoint edge case. Its source root may contain
more than one skill entrypoint and may produce more than one package root. The
contract treats this as first-class behavior, not a validation mistake.

### Project03 Planned Method Skill

`concept-card-method` is a Project03 planned method surface, not live source.
The accepted source root is `knowledge/concept-card-method/`, but no current
package, README availability claim, or installed skill route exists until a
later implementation lands it.

### CCDP

CCDP remains separate under `protocols/ccdp/` and is a bridge/integration
protocol package rather than an installable assistant skill package. Skill or
documentation surfaces may route to CCDP, but CCDP must not be absorbed into
skill package roots without an explicit operator decision.

## Validation Routing

Slice03 must turn this contract into a validation matrix. At minimum:

- source root changes route to `make check-skills` when `SKILL.md` or
  `SKILL*.md` files are affected;
- package root changes route to `make check-package-paths` and `make all`;
- composer package changes route to `make collab-framework`;
- CCDP package changes route to `make ccdp-package` and
  `make check-ccdp-package`;
- package-local link changes route to package inspection before path
  exceptions;
- implementation arc source edits include source checkout status and diff
  hygiene checks.

## Boundary

This source/package root contract is not source-edit authorization. It defines
the Arc03 target behavior and the Slice03 migration sequence inputs while
preserving source root, package root, skill kind, and topology as independent
axes. Arc05 owns final public vocabulary.
