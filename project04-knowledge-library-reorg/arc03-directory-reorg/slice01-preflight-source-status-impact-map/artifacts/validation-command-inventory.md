# Validation Command Inventory

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice01-preflight-source-status-impact-map
artifact: validation-command-inventory
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This validation command inventory maps likely Arc03 source-edit surfaces to
the commands and review gates later implementation slices must select from.
It records gates only; it does not authorize source edits.

## Command Baseline

`make -C /Users/oubiwann/lab/billosys/ai-engineering help` confirms these
relevant targets exist in the source checkout:

- `make help`
- `make check-skills`
- `make check-package-paths`
- `make all`
- `make collab-framework`
- `make ccdp-package`
- `make check-ccdp-package`

The Makefile also exposes `INSTALL_ZIPS`, `ALL_SKILL_FILES`, and `CF_FILES`,
which are review surfaces for package/list updates and collaboration-framework
selected-file packaging.

## Gate Families

| Gate family | Commands and reviews | Applies when |
|-------------|----------------------|--------------|
| Source hygiene | `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short`; `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check` | Every source-edit slice before and after edits. |
| Skill entrypoint checks | `make help`; `make check-skills`; entrypoint/frontmatter review | Any change to `SKILL.md`, `knowledge/<component>/SKILL.md`, `knowledge/deno/SKILL-js-linter.md`, or Biome entrypoints. |
| Package path checks | `make check-package-paths`; package-local link repair; exception-policy review | Any move affecting Markdown links, package-local paths, owner-local templates, or generated package contents. |
| Full package checks | `make all`; generated package inspection of zip contents | Any change to package roots, `INSTALL_ZIPS`, `ALL_SKILL_FILES`, Makefile package lists, or bundled payloads. |
| Collaboration-framework checks | `make collab-framework`; `CF_FILES` review; top-level route review | Any change to top-level `SKILL.md`, `docs/pm/`, framework docs, framework templates, or selected-file transitional packaging. |
| CCDP checks | `make ccdp-package`; `make check-ccdp-package`; `INSTALL_ZIPS` review | Any `protocols/ccdp` packaging or route-link change. CCDP remains separate from installable skill packages. |
| Compatibility review | README/SKILL route review; `AGENTS.md` and `CLAUDE.md` compatibility review; wrapper and migration note review | Any top-level compatibility change or public route movement. |

## Surface-To-Gate Map

| Source-edit surface | Required validation gate candidates |
|---------------------|-------------------------------------|
| `README.md` | Source status, source `diff --check`, route-map review, compatibility review, Arc04 handoff review for end-user docs prose. |
| Top-level `SKILL.md` | Source status, source `diff --check`, `make check-skills`, `make collab-framework`, compatibility review, selected shim/replacement/no-shim evidence. |
| `docs/` | Source status, source `diff --check`, `make collab-framework` when `CF_FILES` content changes, package-local link repair, `make check-package-paths`, source-prose preservation review. |
| `knowledge/` | Source status, source `diff --check`, `make check-skills`, `make all` if package payloads change, package target review, package-local link repair, generated package inspection. |
| `knowledge/biome/` | Source status, source `diff --check`, `make check-skills`, `make check-package-paths`, `make all`, generated package inspection, Biome multi-entrypoint review. |
| `templates/` | Source status, source `diff --check`, package-local link repair, `make check-package-paths`, cross-cutting versus owner-local template review. |
| `protocols/ccdp` | Source status, source `diff --check`, `make ccdp-package`, `make check-ccdp-package`, CCDP package-policy review, `INSTALL_ZIPS` review. |
| `Makefile` | Source status, source `diff --check`, `make help`, `make check-skills`, `make check-package-paths`, `make all`, targeted package target review. |
| `package-path-exceptions.tsv` | Source status, source `diff --check`, package-local link repair evidence, exception-policy review, operator approval record for persistent package-path exception or accepted warning rows, `make check-package-paths`. |
| Generated zips | Generated package inspection, `make all`, `make collab-framework` for composer packages, `make ccdp-package` and `make check-ccdp-package` for CCDP, archive root/content review. |
| `AGENTS.md` and `CLAUDE.md` | Source status, source `diff --check`, compatibility review, route review; preserve symlink or compatibility behavior if present. |

## Ordering Constraints

- Run source status before any later source-edit slice starts.
- Resolve top-level `SKILL.md` compatibility before composer moves.
- Preserve mechanical moves before prose rewrites.
- Perform package/list updates after moved files exist.
- Perform package-local link repair before exceptions.
- Keep CCDP remains separate under `protocols/ccdp`.
- Preserve Biome multi-entrypoint package behavior explicitly.
- Route Arc04 end-user docs work and Arc05 public vocabulary work outside
  Arc03 source-move validation.
