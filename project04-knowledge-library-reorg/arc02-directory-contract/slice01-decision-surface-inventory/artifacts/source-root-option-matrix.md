# Source Root Option Matrix

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice01-decision-surface-inventory
artifact: source-root-option-matrix
artifact-status: option inventory
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This matrix compares viable source root and package root options for Arc02. It
does not select the final contract. Source root and package root are separate
decisions: a source root is where repository material lives; a package root is
what generated zips expose after packaging.

## Global Option Families

| Option | Source root shape | Package root shape | Strengths | Risks | Best fit |
|--------|-------------------|--------------------|-----------|-------|----------|
| A | `knowledge/<slug>/` for all skill substrate, including domain/tooling, framework/operational, and method skills. | Package root follows frontmatter `name:` or accepted package name. | Aligns with Project04 `knowledge/` substrate direction and current domain/tooling roots. | May need wrapper docs and compatibility notes for current top-level `SKILL.md` and framework material in `docs/`. | Current domain/tooling skills and planned method skills. |
| B | Top-level component roots for Project02 framework components. | Package root equals component root. | Matches Project02 implementation-plan hypothesis and direct component names. | Weakens the `knowledge/` as substrate contract unless Arc02 records top-level roots as an explicit exception. | Framework/operational components if operator prefers component roots beside `knowledge/`. |
| C | `knowledge/framework/<component>/` and `knowledge/methods/<method>/` family roots. | Package root follows component or skill name, not necessarily the nested source path. | Keeps substrate under `knowledge/` while grouping framework and method families. | Adds depth and requires package path checker/source candidate support if generated roots differ. | Planned Project02 components and Project03 method skill if Arc02 wants family grouping. |
| D | Hybrid with `docs/` wrappers, `knowledge/` substrate roots, `protocols/ccdp/` protocol root, and top-level compatibility shim(s). | Package roots follow existing frontmatter/component/protocol package names. | Preserves current source-reader routes while moving source-like substrate where accepted. | More compatibility surfaces; needs explicit deprecation/wrapper policy. | Migration from current monolithic framework source to accepted roots. |
| E | Selected-file package roots independent from source roots. | Package root assembled from files in several source locations. | Matches current `collaboration-framework.zip` behavior. | Harder to reason about package-local links and ownership; can obscure provenance. | Transitional composer package only, if Arc02 records the exception. |

## Surface Matrix

| Surface | Current/planned state | Skill kind | Topology | Source root options to test | Package root options to test | Recommendation status |
|---------|-----------------------|------------|----------|-----------------------------|------------------------------|-----------------------|
| Current domain/tooling skills | live source under `knowledge/rust`, `knowledge/go`, `knowledge/cpp`, `knowledge/js`, `knowledge/erlang`, `knowledge/cobalt`, `knowledge/design`, `knowledge/tailwindcss`, `knowledge/deno`, and `knowledge/biome`. | domain/tooling | mostly atomic; Biome root is composite with atomic package entries. | Keep `knowledge/<domain>`; add family grouping only if Arc02 needs it. | Keep package root from frontmatter or current Makefile target. | Planner recommendation: preserve current roots unless a contract defect is found. |
| Project02 framework/operational components | planned surface, not live source as separate roots. | framework/operational | mix of composite, atomic operational method, and bridge/integration. | `knowledge/<component>`; `knowledge/framework/<component>`; top-level `<component>`; wrapper docs over roots. | Component package root from accepted component name. | Operator decision required. |
| `collaboration-framework` composer | live source is top-level `SKILL.md` plus selected `docs/` and `templates/`; accepted composite. | framework/operational | composite | `knowledge/collaboration-framework`; `knowledge/framework/collaboration-framework`; top-level `collaboration-framework`; transitional top-level `SKILL.md` shim. | Keep `collaboration-framework` package root; avoid forcing package root to equal old source shape. | Operator decision required for top-level compatibility. |
| Planned `concept-card-method` | planned surface, not live source. | method | provisional atomic with composite pressure. | `knowledge/concept-card-method`; `knowledge/methods/concept-card-method`; defer source root until implementation. | Future `concept-card-method` package root only after implementation. | Operator decision required before public availability claims. |
| CCDP | live source under `protocols/ccdp`; separate package. | protocol/package | bridge/integration | Keep `protocols/ccdp`; add `docs/` wrapper; link from method/framework guides. | Keep `ccdp` package root and `ccdp.zip`, outside `INSTALL_ZIPS`. | Accepted fact unless protocol policy is reopened. |
| Top-level `templates/` | live source support payloads. | support/template plus owner-specific framework/operational roles. | atomic support surfaces unless accepted entrypoints appear. | Keep top-level for cross-cutting templates; move owner-local templates under component/method roots; wrapper from `docs/`. | Package-local under owning package where bundled. | Operator decision required for cross-cutting exceptions. |
| `docs/` framework source | live source-like framework/operational and method material. | framework/operational or method/source provenance. | varies by owning component or method. | Move to owning `knowledge` or component roots; remain with exception; wrapper docs over moved source. | Package root depends on owner package. | Operator decision required per file family. |
| `docs/dev/` extraction guidance | live source-like method/extraction guidance and design/dev provenance. | method or source/provenance. | application/task bundle or method support, depending on accepted owner. | Move under method/knowledge roots; keep as provenance; wrapper docs. | Only package if an accepted skill or method owns it. | Operator decision required for current/public status. |
| `knowledge/biome/` | live source with two `SKILL*.md` files and two generated package roots. | domain/tooling | multi-entrypoint source root; atomic package entries. | Preserve one source root; split into per-package roots; keep common root with package-local guide subtrees. | Keep `biome-js-linter` and `biome-linter` package roots. | Edge case must be explicit in accepted contract. |
| `README`, `AGENTS.md`, `CLAUDE.md` | live compatibility and route surfaces. | not skill kinds. | compatibility surfaces, not topology owners. | Keep at top level with updated routes; add wrappers or migration notes. | Not package roots except as explicitly bundled. | Preserve as compatibility surfaces. |

## Package Root Decision Rules To Test

- frontmatter rule: package root follows `name:` in `SKILL.md` or
  `SKILL*.md`. This fits many current `knowledge/*` packages.
- component-name rule: package root follows accepted Project02 component name.
  This fits planned specialist packages.
- selected-file rule: package root is assembled from selected files. This fits
  current `collaboration-framework` but should be exceptional.
- protocol rule: package root follows protocol package behavior, outside
  installable skill behavior. This fits CCDP.
- multi-entrypoint rule: one source root may produce more than one package root.
  This fits Biome and prevents one-root-one-package assumptions.

## Edge Cases

- Biome: live source has multiple entrypoints and package roots, so Arc02 must
  not assume source root equals package root.
- Current `collaboration-framework`: live source is selected-file packaging
  from top-level `SKILL.md`, `docs/`, and `templates/`, while Project02 plans a
  componentized future.
- Project03 `concept-card-method`: planned surface, not live source, so Arc02
  can reserve a root without claiming current package behavior.
- CCDP: bridge/integration protocol package, not an installable skill package.
- `docs/dev/`: may be source/provenance, method material, or task bundle
  material depending on the accepted owner; folder placement alone is not
  decisive.

## Non-Selection Boundary

This matrix is an option inventory. Slice02 owns accepted contract selection,
and later implementation arcs own source edits. Any selected option must still
carry validation obligations for `Makefile`, `ALL_SKILL_FILES`, `INSTALL_ZIPS`,
`CF_FILES`, package-local links, generated packages, `AGENTS.md`, `CLAUDE.md`,
README, and CCDP checks.
