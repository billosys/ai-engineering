# Material Role Classification

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice01-source-surface-inventory
artifact: material-role-classification
artifact-status: slice inventory evidence
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
created-on: 2026-09-01
source-files-edited: false
```

## Classification Boundary

This artifact classifies current material roles only. It does not decide final
target homes and does not finalize atomic/composite terminology. When a role is
ambiguous, the ambiguity is recorded as a later Arc01/Arc02 input.

## Role Vocabulary Used Here

- `end-user documentation`: reader-facing explanation, orientation, or public
  wayfinding.
- `knowledge substrate`: raw or derived material used to build durable skill
  knowledge.
- `skill entrypoint`: `SKILL.md` or `SKILL*.md` files loaded by an assistant.
- `framework/operational`: collaboration framework, project management,
  ledger, audit, testing, delegation, or contribution discipline.
- `method material`: reusable process for producing or checking knowledge.
- `extraction guidance`: prompts, howtos, taxonomies, competency questions, and
  validation criteria for converting sources into concept cards or guides.
- `design/dev`: research, history, or generated design-development material.
- `protocol distribution`: CCDP source/package material, not an installable
  assistant skill.
- `template/support asset`: reusable templates, images, scripts, static site
  files, or package support.
- `scratch/workbench material`: provenance, staging, release notes, audits, or
  copied source corpora not treated as a package entrypoint.

## `docs/` Material Roles

| Current path | Current role | Classification notes |
|--------------|--------------|----------------------|
| `docs/AI-CONSTITUTION-SUPPLEMENT.md` | framework/operational; source-like; substrate-like | Framework posture source used by top-level `SKILL.md` and `Makefile` `CF_FILES`. |
| `docs/AI-ENGINEERING-METHODOLOGY.md` | framework/operational; method material; source-like; substrate-like | Methodology source; also defines the knowledge substrate and process-rigour model. |
| `docs/PROJECT-MANAGEMENT.md` | framework/operational; project-management; source-like | Wayfinder for PM split files. Bundled in `collaboration-framework.zip`. |
| `docs/pm/` | framework/operational; project-management; source-like | Detailed PM mechanics: scales, planning worktree, top-down planning, slice/arc close, confirmation, anti-patterns, maintenance, worked example, version history. |
| `docs/CODE-AUDIT.md` | framework/operational; method material; source-like | Diagnosis-only audit discipline and output contract. |
| `docs/CODE-COVERAGE.md` | framework/operational; method material; source-like | Coverage/testing hardening discipline; current filename already uses product-neutral coverage language. |
| `docs/SUBAGENT-DELEGATION-POLICY.md` | framework/operational; method material; source-like | Delegation policy and agent-coordination support. |
| `docs/CONTRIBUTION-STYLE.md` | framework/operational; method material; source-like | Upstream contribution voice and workflow guidance. |
| `docs/ORIGINS.md` | end-user documentation; framework history | Reader-facing origin story with links to framework materials and `knowledge/`. |
| `docs/dev/0001-0016...` | extraction guidance; method material; design/dev | Phase 0 visual-design knowledge-engineering prompts/specs. This is source-like guidance, not merely end-user docs. |
| `docs/dev/concept-cards/` | extraction guidance; method material; source-like | Concept-card extraction and re-extraction prompts/howtos. Several files explicitly route output to `knowledge/<kb>/...`. |
| `docs/dev/js/` | extraction guidance; design/dev; source-like | Historical generated JavaScript guide instruction files; source-like process/provenance material, not current public docs. |
| `docs/design/index.md` | design/dev; generated index; end-user-adjacent | ODM-generated design document index, not a framework bundle dependency. |
| `docs/design/.odm/` | template/support asset; generated state | ODM support state for `docs/design/`. |
| `docs/design/06-final/` | design/dev; research | Final design/research documents seeding later knowledge work. |

Early classification: current `docs/` is mixed. It contains some end-user
documentation (`ORIGINS.md`, design index material), but much of the tree is
framework/operational source or method/extraction guidance. That is the
source-backed tension Project04 must resolve before turning `docs/` into
reader-facing documentation about repository materials.

## `knowledge/` Material Roles

| Current path | Current role | Classification notes |
|--------------|--------------|----------------------|
| `knowledge/rust/` | domain/tooling skill substrate; skill entrypoint; candidate atomic anchor | Has `SKILL.md`, `README.md`, `guides/`, `concept-cards/`, `extraction-metadata/`, `sources/`; Makefile packages `rust-guidelines.zip`. |
| `knowledge/go/` | domain/tooling skill substrate; skill entrypoint | Has `SKILL.md`, `guides/`, `concept-cards/`, `extraction-metadata/`, `sources/`; Makefile packages `go-guidelines.zip`. |
| `knowledge/cpp/` | domain/tooling skill substrate; skill entrypoint | Has `SKILL.md`, `guides/`, `extraction-metadata/`, `sources/`, `tools/`; Makefile packages `cpp-guidelines.zip`. |
| `knowledge/js/` | domain/tooling skill substrate; skill entrypoint | Has `SKILL.md`, `guides/`, `concept-cards/`, `extraction-metadata/`, `sources/`; Makefile packages `javascript-deno-guidelines.zip`. |
| `knowledge/erlang/` | domain/tooling skill substrate; skill entrypoint | Has `SKILL.md`, `guides/`, `concept-cards/`, `extraction-metadata/`, `sources/`, `tools/`, `workbench/`; Makefile packages `erlang-guidelines.zip`. |
| `knowledge/cobalt/` | tooling skill substrate; skill entrypoint | Has `SKILL.md`, `guides/`, `concept-cards/`, `extraction-metadata/`, `sources/`; Makefile packages `cobalt-guidelines.zip`. |
| `knowledge/design/` | domain/tooling skill substrate; skill entrypoint | Has `SKILL.md`, `guides/`, `concept-cards/`, `sources/`; Makefile packages `visual-design-system.zip`. |
| `knowledge/tailwindcss/` | tooling skill substrate; skill entrypoint | Has `SKILL.md`, `guides/`; Makefile packages `tailwindcss.zip`. |
| `knowledge/deno/` | tooling/linting skill substrate; skill entrypoint | Has `SKILL-js-linter.md`, `guides/`, `extraction-metadata/`; Makefile packages `deno-js-linter.zip`. |
| `knowledge/biome/` | tooling/linting skill substrate; multiple skill entrypoints | Has `SKILL-js-linter.md`, `SKILL-web-linter.md`, `guides/js-linter/`, `guides/web-linter/`, `extraction-metadata/`; Makefile packages two zips. |

Observed recurring `knowledge/` roles:

- `SKILL.md` / `SKILL*.md`: skill entrypoint and route table.
- `guides/`: packaged, LLM-facing derived guidance.
- `concept-cards/`: atomic concept-card substrate where present.
- `extraction-metadata/`: provenance, competency questions, taxonomies, and
  extraction/reconciliation records.
- `sources/`: upstream source material, often repo-only provenance and not part
  of generated skill zips.
- `tools/`: regeneration/validation support for some domains.
- `workbench/`: source-only provenance or staging where present.

## Skill Kind and Topology Observations

Source-backed skill kind observations:

- Current packaged `knowledge/*` skills are mostly domain/tooling skills:
  Rust, Go, C++, JavaScript/Deno, Erlang/OTP, Cobalt, visual design,
  Tailwind CSS, Deno lint, and Biome linting.
- Top-level `SKILL.md` is a framework/operational skill entrypoint with
  frontmatter category `meta-skills`, not a domain/tooling skill.
- A future method-skill source root is planned by Project04 for
  `concept-card-method`, but no live `knowledge/concept-card-method/` root was
  observed in Slice01.
- CCDP is currently a protocol distribution, not a skill kind in the
  installable-skill package list.

Source-backed early topology observations:

- `knowledge/rust/SKILL.md` is source-backed as the candidate atomic example:
  one coherent primary load reason, one skill entrypoint, and a domain-local
  `guides/` payload.
- Top-level `collaboration-framework` is source-backed as the accepted
  composite example: the README component table and `SKILL.md` route table
  describe a daily-driver composer over specialized framework/operational
  components.
- `knowledge/biome/` is a useful Slice03 topology test case because one source
  root contains two installable skill entrypoints and two guide subtrees.
- `knowledge/js/` plus `knowledge/deno/` and `knowledge/biome/` expose a
  category/topology risk: domain language guidance, runtime guidance, and
  linter guidance are adjacent but separately packaged.

Final atomic/composite classification is deferred to Slice03. This file only
records source-backed early observations.

## `templates/` Material Roles

| Current path | Current role | Classification notes |
|--------------|--------------|----------------------|
| `templates/GUIDE.md` | template/support asset; method support | README points contributors to this for new guide work. |
| `templates/LEDGER-DISCIPLINE.md` | framework/operational; work-verification; template/support asset | Bundled by `CF_FILES`; source of ledger protocol. |
| `templates/CONTRIBUTION-TICKET.md` | framework/operational; contribution method; template/support asset | Bundled by `CF_FILES`; ticket template paired with contribution style. |

## `protocols/` Material Roles

| Current path | Current role | Classification notes |
|--------------|--------------|----------------------|
| `protocols/ccdp/README.md` | protocol distribution; package entrypoint | README for standalone CCDP package and source checkout. |
| `protocols/ccdp/src/` | protocol distribution source | RFC-style chapter source for assembled protocol. |
| `protocols/ccdp/composite-cognition-dispatch-protocol.md` | generated/assembled protocol distribution | Assembled specification checked by CCDP package validation. |
| `protocols/ccdp/json/` | protocol distribution; examples/canonical corpus | JSON corpus, manifest, findings, examples, and inventory. |
| `protocols/ccdp/visual-guide/` | protocol distribution; static doc support | HTML visual guide and source reference. |
| `protocols/ccdp/templates/` | protocol template/support asset | RFC XML template material included in `ccdp.zip`. |
| `protocols/ccdp/tools/ccdp-assembler/` | protocol tooling | Rust assembler source and Cargo files included in `ccdp.zip`; `target/` excluded. |
| `protocols/ccdp/prompts/` | scratch/workbench material | Source-only prompt material excluded from package per README and package checker. |
| `protocols/ccdp/workbench/` | scratch/workbench material | Source-only review/provenance material excluded from package per README and package checker. |

## Validation and Compatibility Roles

| Surface | Current role | Move sensitivity |
|---------|--------------|------------------|
| `Makefile` | package/release gate | High: lists `CF_FILES`, `ALL_SKILL_FILES`, `INSTALL_ZIPS`, per-skill package targets, and CCDP package contents. |
| `package-path-exceptions.tsv` | package/link compatibility gate | High: path exceptions use current source/package paths and package names. |
| `scripts/check-package-paths` | generated zip link validator | High: maps package roots to `knowledge/<domain>` and recognizes `docs/`, `templates/`, root files, and repo-only paths. |
| `scripts/stage-skill-entrypoint` | package-only entrypoint transform | Medium/high: currently special-cases `knowledge/rust/SKILL.md` and `knowledge/js/SKILL.md`. |
| `scripts/check-skill-description.sh` | skill entrypoint metadata validator | Medium: follows `ALL_SKILL_FILES`; affected by new or moved `SKILL*.md` files. |
| `scripts/check-ccdp-package` | CCDP package validator | Medium/high if protocol paths move; separate from skill packages. |
| `AGENTS.md` and `CLAUDE.md` | compatibility and workflow instructions | High: name source/planning, packaging, validation, and CCDP paths. |
| `README.md` | end-user documentation and link surface | High: links directly to `knowledge/`, `docs/`, `templates/`, and `protocols/`. |

## Imported Planning Material Boundary

The Project02 imported artifact set is a later Slice02 input and not source
inventory:

- `operator-accepted-architecture.md`
- `component-file-layout-plan.md`
- `package-target-plan.md`
- `skill-entrypoint-validation-plan.md`
- `readme-wayfinding-plan.md`
- `migration-compatibility-plan.md`
- `package-path-link-exception-plan.md`
- `implementation-sequence-roadmap.md`

Project03 method-skill vocabulary and `concept-card-method` planning are also
later Slice02 inputs. They are not a substitute for the live source inventory
recorded in this Slice01 artifact set.

