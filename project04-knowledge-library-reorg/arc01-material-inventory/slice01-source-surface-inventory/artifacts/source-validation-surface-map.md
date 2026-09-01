# Source Validation Surface Map

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice01-source-surface-inventory
artifact: source-validation-surface-map
artifact-status: slice inventory evidence
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
created-on: 2026-09-01
source-files-edited: false
```

## Purpose

This artifact maps the package, validation, link, and compatibility surfaces
that future Project04 moves will affect. It is a source-backed risk map, not an
implementation plan.

## Evidence Commands

- `rg -n "^CF_FILES|^ALL_SKILL_FILES|^INSTALL_ZIPS|^CCDP|^check-skills|^check-package-paths|^ccdp|^ccdp-package|^check-ccdp-package|^skills:|^all:|stage-skill-entrypoint|package-path-exceptions.tsv|docs/|templates/|knowledge/|protocols/" /Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `sed -n '1,260p' /Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `sed -n '260,580p' /Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `sed -n '1,240p' /Users/oubiwann/lab/billosys/ai-engineering/scripts/check-skill-description.sh`
- `sed -n '1,260p' /Users/oubiwann/lab/billosys/ai-engineering/scripts/stage-skill-entrypoint`
- `sed -n '1,240p' /Users/oubiwann/lab/billosys/ai-engineering/scripts/check-ccdp-package`
- `sed -n '240,380p' /Users/oubiwann/lab/billosys/ai-engineering/scripts/check-ccdp-package`
- `rg -n "^#|^##|docs/|knowledge/|templates/|protocols/|Makefile|package-path|check-skills|check-package-paths|INSTALL_ZIPS|ALL_SKILL_FILES|README|AGENTS|CLAUDE|CCDP|skill|Skill|composite|atomic|framework|method" /Users/oubiwann/lab/billosys/ai-engineering/README.md /Users/oubiwann/lab/billosys/ai-engineering/SKILL.md /Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md /Users/oubiwann/lab/billosys/ai-engineering/Makefile /Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`

## Makefile Package and Validation Surface

| Makefile surface | Observed role | Future move impact |
|------------------|---------------|--------------------|
| `INSTALL_ZIPS` | Lists installable skill zips, currently including `collaboration-framework.zip` and per-domain/tooling zips. | Any new component or moved skill package must update install behavior deliberately. |
| `ALL_SKILL_FILES` | Enumerates every packaged `SKILL.md` / `SKILL*.md` for `check-skills`. | Moving or adding skill entrypoints requires list updates or validation will miss/fail. |
| `CF_FILES` | Explicit list for `collaboration-framework.zip`: top-level `SKILL.md`, selected `docs/pm`, root framework docs, and templates. | High-risk for Project04: moving framework/operational material requires package list and relative-link updates. |
| `pack_skill` macro | Packages a `knowledge/<domain>/SKILL*.md` plus sibling `guides/` under a zip root named by skill frontmatter. | Assumes domain/tooling source roots under `knowledge/`; new method/composite roots need explicit design. |
| `skills` target | Aggregates Rust, Go, C++, JS, Erlang, Cobalt, Design, Tailwind CSS, Deno, and Biome. | Skill set changes require target updates. |
| `all` target | Builds `skills` plus `collab-framework`. | Project04 package topology changes may need to distinguish framework components from domain/tooling skill packages. |
| `check-skills` | Runs `scripts/check-skill-description.sh` over `ALL_SKILL_FILES`. | Entry-point moves or new component skills must remain in the check surface. |
| `check-package-paths` | Builds all zips and runs `scripts/check-package-paths --exceptions package-path-exceptions.tsv $(INSTALL_ZIPS)`. | Path moves must be validated against generated zip layout, not source layout alone. |
| `ccdp`, `ccdp-package`, `check-ccdp-package` | Assembles and validates the standalone CCDP distribution. | CCDP remains separate from installable skill zips unless a later protocol-package decision changes that. |

## Script Validation Surface

### `scripts/check-package-paths`

Current behavior observed from source:

- Validates package-context Markdown paths inside generated skill zips.
- Loads TSV exceptions with schema:
  `package`, `document`, `target`, `classification`, `disposition`, `reason`,
  `source`, `expires`.
- Knows generated skill packages through `DOMAIN_BY_PACKAGE`, mapping package
  roots such as `rust-guidelines`, `go-guidelines`, `javascript-deno-guidelines`,
  `biome-js-linter`, and `biome-linter` back to `knowledge/<domain>`.
- Treats `docs/dev/`, `extraction-metadata/`, `sources/`, `tools/`,
  `workbench/`, `AGENTS.md`, `CLAUDE.md`, and similar paths as repo-only or
  provenance surfaces when classifying references.
- Special-cases `collaboration-framework` package paths for top-level
  `SKILL.md`, `docs/`, and `templates/`.
- Allows classified warnings and explicit exceptions but returns failure if any
  hard failure remains.

Future move impact:

- Moving framework material out of `docs/` will require updating the
  `collaboration-framework` alternates and exception expectations if package
  local links change.
- Moving or adding `knowledge/` roots changes the domain/package mapping and
  the source-candidate logic.
- Moving repo-only provenance paths changes exception rows and the
  `looks_repo_only` classification assumptions.
- Generated zip output is the validation target; source-only scans are weaker
  evidence.

### `scripts/check-skill-description.sh`

Current behavior observed from source:

- Validates that each supplied skill file starts with YAML frontmatter and has
  a `description`.
- Enforces max description length `1023`.
- Labels errors with the skill name read from `name:`.

Future move impact:

- Any new or moved `SKILL.md` / `SKILL*.md` must be present in `ALL_SKILL_FILES`
  or this guard will not cover it.

### `scripts/stage-skill-entrypoint`

Current behavior observed from source:

- Stages skill entrypoints for packaging.
- Applies package-only guide-reference transforms for:
  - `knowledge/rust/SKILL.md`
  - `knowledge/js/SKILL.md`
- Copies other entrypoints unchanged.

Future move impact:

- If Rust or JavaScript entrypoints move, the transform keys must move with
  them.
- If future method/framework components use source-path guide references, they
  may need their own transform or, preferably, package-local links in source.

### `scripts/check-ccdp-package`

Current behavior observed from source:

- Validates standalone `ccdp.zip`.
- Requires files including `ccdp/README.md`,
  `ccdp/composite-cognition-dispatch-protocol.md`, `ccdp/src/README.md`,
  `ccdp/json/MANIFEST.md`, `ccdp/visual-guide/index.html`,
  `ccdp/templates/draft-rfcxml-general-template-standard-00.xml-edited.md`,
  `ccdp/tools/ccdp-assembler/Cargo.toml`, `ccdp/tools/ccdp-assembler/Cargo.lock`,
  and `ccdp/Makefile`.
- Requires prefixes including `ccdp/src/`, `ccdp/json/canonical/`,
  `ccdp/json/examples/`, `ccdp/json/inventory/`, and
  `ccdp/tools/ccdp-assembler/src/`.
- Excludes `ccdp/workbench/`, `ccdp/prompts/`, and
  `ccdp/tools/ccdp-assembler/target/`.
- Checks package-local README links and re-runs extracted assembly.

Future move impact:

- CCDP package behavior is explicitly separate from skill zip behavior. Any
  Project04 decision that changes protocol paths must update this validator and
  the CCDP Makefile in the same implementation slice.

## Link and Compatibility Surfaces

| Surface | Current link/compatibility role | Future move impact |
|---------|---------------------------------|--------------------|
| `README.md` | Links to `knowledge/`, `docs/ORIGINS.md`, `templates/GUIDE.md`, `docs/dev/`, `protocols/ccdp/*`, assets, and GitHub badges. | README must be updated after accepted moves and rechecked for links. |
| `SKILL.md` | Uses relative links into `docs/` and `templates/`; routes to `knowledge/<domain>/SKILL.md` examples. | Moving framework docs/templates requires package-local link repair and likely route wording changes. |
| `AGENTS.md` | Names planning worktree, `knowledge/<domain>`, `Makefile`, `package-path-exceptions.tsv`, `protocols/ccdp/src/`, and validation commands. | Compatibility instructions must track any path or validation command changes. |
| `CLAUDE.md` | Symlink to `AGENTS.md`. | Symlink target must remain intentional; do not replace with a copied file. |
| `package-path-exceptions.tsv` | Current exceptions include `collaboration-framework.zip` references to `knowledge/<slug>/SKILL*.md`, `knowledge/<domain>/SKILL.md`, and domain package provenance exceptions. | Path/category moves must update or expire rows; broad exceptions should not hide real package-local link breakage. |
| Generated zips | Skill zips and `ccdp.zip` exist at source root. | Generated archives are authoritative evidence for package paths; source changes alone are incomplete. |
| `site/` | Static publication files, including CCDP visual guide page. | Protocol/doc moves may affect static site source or deployment references. |
| `assets/` | README logo named-link targets. | Asset moves require README link updates. |

## Future Move Risk Matrix

| Proposed future surface change | Must check |
|--------------------------------|------------|
| Move framework/operational docs out of `docs/` | `CF_FILES`, top-level `SKILL.md` links, README, `check-package-paths`, `package-path-exceptions.tsv`, AGENTS/CLAUDE instructions. |
| Add framework component packages | `INSTALL_ZIPS`, `ALL_SKILL_FILES`, new Makefile package targets, `check-skill-description.sh`, generated zip roots, package path checker mappings/exceptions. |
| Move method/extraction guidance into `knowledge/` | README, docs/dev links, concept-card extraction guides, future method skill entrypoint, package-path exceptions for provenance-only paths. |
| Move or split `templates/` | `CF_FILES`, framework/package-local links, contribution/work-verification package payloads, README contributor guidance. |
| Change `knowledge/` domain roots | `pack_skill` calls, `DOMAIN_BY_PACKAGE`, `stage-skill-entrypoint` transforms, README skill library links, package-path exceptions. |
| Change CCDP paths | Root Makefile `ccdp*` targets, `protocols/ccdp/Makefile`, `scripts/check-ccdp-package`, README CCDP links, static `site/protocols/ccdp/` material. |
| Rename compatibility files | `AGENTS.md`, `CLAUDE.md` symlink, `check-package-paths` repo-only path classifier, source checkout standing instructions. |

## Imported Project02/Project03 Boundary

The Project02 imported artifact set under
`project04-knowledge-library-reorg/artifacts/` is relevant to later Slice02
validation-surface planning, especially package targets, skill entrypoint
validation, README wayfinding, migration compatibility, package-path/link
exceptions, and implementation sequencing. It is imported artifact material
and later Slice02 input, not source inventory.

Project03 `concept-card-method` is relevant to future method-skill validation
surfaces, but no live source root was observed in Slice01. It remains a later
Slice02 input and Slice03 topology/classification input.

## Early Atomic/Composite Validation Observation

The validation surface currently encodes package shape more than topology:

- `pack_skill` assumes a `knowledge/<domain>/SKILL*.md` plus `guides/` package
  shape.
- `CF_FILES` encodes `collaboration-framework` as a selected-file composite
  bundle from top-level `SKILL.md`, `docs/`, and `templates/`.
- No current validator reads an explicit `atomic` or `composite` field from
  skill frontmatter.

Final topology validation requirements are therefore deferred to Slice03 and
later Arc02/Arc05 decisions.

