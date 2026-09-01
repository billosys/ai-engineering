# Current Source Surface Map

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice01-source-surface-inventory
artifact: current-source-surface-map
artifact-status: slice inventory evidence
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
created-on: 2026-09-01
source-files-edited: false
```

## Purpose

This artifact records the current live source checkout surface before Project04
plans any docs/knowledge-library moves. It is source inventory only: it does
not decide final target homes, rename material, or substitute imported planning
artifacts for source evidence.

## Evidence Commands

Commands run from the planning checkout unless the command itself names the
source checkout:

- `git worktree list`
- `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short`
- `git -C /Users/oubiwann/lab/billosys/ai-engineering ls-tree --name-only HEAD`
- `ls -la /Users/oubiwann/lab/billosys/ai-engineering`
- `find /Users/oubiwann/lab/billosys/ai-engineering/docs -maxdepth 3 -type d`
- `find /Users/oubiwann/lab/billosys/ai-engineering/knowledge -maxdepth 3 -type d`
- `find /Users/oubiwann/lab/billosys/ai-engineering/protocols -maxdepth 4 -type d`
- `find /Users/oubiwann/lab/billosys/ai-engineering/workbench -maxdepth 2 -type d`
- `find /Users/oubiwann/lab/billosys/ai-engineering/scripts -maxdepth 2 -type f`
- `find /Users/oubiwann/lab/billosys/ai-engineering/templates -maxdepth 2 -type f`
- `find /Users/oubiwann/lab/billosys/ai-engineering/assets -maxdepth 3 -type f`
- `find /Users/oubiwann/lab/billosys/ai-engineering/site -maxdepth 3 -type f`
- `rg -n "^name:|category:" /Users/oubiwann/lab/billosys/ai-engineering/knowledge/*/SKILL*.md /Users/oubiwann/lab/billosys/ai-engineering/SKILL.md`
- `rg -n "^CF_FILES|^ALL_SKILL_FILES|^INSTALL_ZIPS|^CCDP|^check-skills|^check-package-paths|^ccdp|^ccdp-package|^check-ccdp-package|^skills:|^all:|stage-skill-entrypoint|package-path-exceptions.tsv|docs/|templates/|knowledge/|protocols/" /Users/oubiwann/lab/billosys/ai-engineering/Makefile`

## Worktree and Source State

- Implementation checkout:
  `/Users/oubiwann/lab/billosys/ai-engineering`, branch `main`, observed at
  worktree commit `4ce7fcf`.
- Planning checkout:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`, branch
  `planning`, observed at worktree commit `454f37e`.
- Source checkout status before artifact writing:
  `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short` produced
  no output.
- `CLAUDE.md` in the source checkout is a symlink to `AGENTS.md`.

## Top-Level Source Surfaces

| Surface | Observed state | Current role |
|---------|----------------|--------------|
| `README.md` | Top-level repository orientation, skill library description, build/install instructions, repository layout, CCDP overview, named links to assets and repo docs. | User-facing documentation and link surface. |
| `SKILL.md` | Top-level `name: collaboration-framework`, category `meta-skills`; contains route table to framework docs/templates and domain skill routing text. | Composite skill entrypoint and framework source surface. |
| `AGENTS.md` | Standing session instructions for source checkout; names repo role, planning worktree, domain skill loading, packaging, validation, and CCDP commands. | Compatibility and workflow instruction surface. |
| `CLAUDE.md` | Symlink to `AGENTS.md`. | Compatibility alias; future moves must preserve symlink intent. |
| `docs/` | Root framework docs, `pm/`, `dev/`, `dev/concept-cards/`, `dev/js/`, `design/`. | Mixed framework/operational source, method/extraction guidance, and design/dev history. |
| `knowledge/` | Domain/tooling skill roots plus substrate directories: `SKILL*.md`, `guides/`, `concept-cards/`, `extraction-metadata/`, `sources/`, and some `tools/`/`workbench/`. | Current knowledge-library substrate and packaged specialist skill source. |
| `templates/` | `GUIDE.md`, `LEDGER-DISCIPLINE.md`, `CONTRIBUTION-TICKET.md`. | Reusable template/support material; two files are bundled in `collaboration-framework.zip`. |
| `protocols/` | `ccdp/` with source chapters, assembled spec, JSON corpus, visual guide, package Makefile, templates, tools, prompts, workbench. | Protocol distribution source, separate from installable skill zips. |
| `Makefile` | Packaging, install, skill validation, package-path validation, and CCDP package targets. | Build/package/validation contract. |
| `package-path-exceptions.tsv` | TSV exception register for generated package path checker. | Package/link compatibility gate. |
| `scripts/` | Validation scripts and extraction/conversion helpers. | Validation, package staging, and knowledge-source processing support. |
| `assets/` | Logo images under `assets/images/`. | README/site visual assets. |
| `site/` | Static HTML pages including protocol/CCDP pages. | Published static site surface. |
| `workbench/` | Release notes, audit material, and large source/workbench corpora including Erlang and OTP material. | Scratch/provenance/workbench material, not packaged skill entrypoints. |

The source checkout also contains generated zip artifacts at the top level
(`collaboration-framework.zip`, per-skill zips, and `ccdp.zip`). They are
release/package outputs, not source directories, but they are affected by
future path moves through the Makefile and validation scripts.

## `docs/` Subtree Surface

Observed directories:

- `docs/`
- `docs/pm/`
- `docs/design/`
- `docs/design/.odm/`
- `docs/design/06-final/`
- `docs/dev/`
- `docs/dev/js/`
- `docs/dev/concept-cards/`

Observed root files:

- `docs/AI-CONSTITUTION-SUPPLEMENT.md`
- `docs/AI-ENGINEERING-METHODOLOGY.md`
- `docs/PROJECT-MANAGEMENT.md`
- `docs/CODE-AUDIT.md`
- `docs/CODE-COVERAGE.md`
- `docs/SUBAGENT-DELEGATION-POLICY.md`
- `docs/CONTRIBUTION-STYLE.md`
- `docs/ORIGINS.md`

Observed `docs/pm/` files:

- `01-scales-of-work.md`
- `02-canonical-planning-worktree.md`
- `03-planning-top-down.md`
- `04-closing-slices.md`
- `05-closing-arcs.md`
- `06-confirmation-protocol.md`
- `07-anti-patterns.md`
- `08-maintenance.md`
- `09-worked-example-odm.md`
- `version-history.md`

Observed `docs/dev/` surfaces:

- Numbered Phase 0 visual-design knowledge-engineering files
  `0001` through `0016`.
- `docs/dev/concept-cards/` extraction and re-extraction guides/prompts
  `0001` through `0012`.
- `docs/dev/js/` historical JavaScript guide-generation instruction files
  `0001` through `0015`.

Observed `docs/design/` surfaces:

- `docs/design/index.md`, an ODM-generated design document index.
- `docs/design/06-final/0001-research-foundation-for-a-visual-design-knowledge-base.md`.
- `docs/design/06-final/0002-go-llm-coding-guides-the-real-contenders.md`.
- `docs/design/.odm/`, generated/state support for the design index.

## `knowledge/` Subtree Surface

Observed top-level skill/material roots:

- `knowledge/biome/`
- `knowledge/cobalt/`
- `knowledge/cpp/`
- `knowledge/deno/`
- `knowledge/design/`
- `knowledge/erlang/`
- `knowledge/go/`
- `knowledge/js/`
- `knowledge/rust/`
- `knowledge/tailwindcss/`

Observed skill entrypoints and frontmatter names:

| Source path | Skill name | Frontmatter category |
|-------------|------------|----------------------|
| `knowledge/rust/SKILL.md` | `rust-guidelines` | `systems-programming` |
| `knowledge/go/SKILL.md` | `go-guidelines` | `systems-programming` |
| `knowledge/cpp/SKILL.md` | `cpp-guidelines` | `systems-programming` |
| `knowledge/js/SKILL.md` | `javascript-deno-guidelines` | `web-frontend` |
| `knowledge/erlang/SKILL.md` | `erlang-guidelines` | `systems-programming` |
| `knowledge/cobalt/SKILL.md` | `cobalt-guidelines` | `static-sites` |
| `knowledge/design/SKILL.md` | `visual-design-system` | `web-frontend` |
| `knowledge/tailwindcss/SKILL.md` | `tailwindcss` | `web-frontend` |
| `knowledge/deno/SKILL-js-linter.md` | `deno-js-linter` | `linting` |
| `knowledge/biome/SKILL-js-linter.md` | `biome-js-linter` | `linting` |
| `knowledge/biome/SKILL-web-linter.md` | `biome-linter` | `linting` |

Observed recurring knowledge-substrate directories:

- `guides/`: packaged LLM-facing guidance for each skill where present.
- `concept-cards/`: single-concept extracted cards where present.
- `extraction-metadata/`: competency questions, extraction logs, taxonomies,
  and derivation records.
- `sources/`: upstream source material in `md/`, `pdf/`, `html/`, `txt/`, or
  `epub/`, depending on domain.
- `tools/`: present in `knowledge/cpp/` and `knowledge/erlang/`.
- `workbench/`: present in `knowledge/erlang/`; `knowledge/rust/SKILL.md`
  references a `knowledge/rust/workbench/` provenance surface, but no
  top-level `knowledge/rust/workbench/` directory was observed in the
  `find ... -maxdepth 2 -type d` pass.
- `knowledge/rust/README.md`: domain README present only for Rust among the
  `find ... -maxdepth 2 -type f` pass.

## Other Key Subtrees

### `templates/`

Observed files:

- `templates/GUIDE.md`
- `templates/LEDGER-DISCIPLINE.md`
- `templates/CONTRIBUTION-TICKET.md`

### `protocols/`

Observed primary protocol root:

- `protocols/ccdp/`

Observed CCDP source/package surfaces:

- `protocols/ccdp/README.md`
- `protocols/ccdp/Makefile`
- `protocols/ccdp/composite-cognition-dispatch-protocol.md`
- `protocols/ccdp/src/`
- `protocols/ccdp/json/`
- `protocols/ccdp/visual-guide/`
- `protocols/ccdp/templates/`
- `protocols/ccdp/tools/ccdp-assembler/`
- `protocols/ccdp/prompts/`
- `protocols/ccdp/workbench/`

The root README states that `protocols/ccdp/workbench/` and
`protocols/ccdp/prompts/` are source-only and intentionally excluded from
`ccdp.zip`.

### `scripts/`

Observed files:

- `scripts/check-ccdp-package`
- `scripts/check-package-paths`
- `scripts/check-skill-description.sh`
- `scripts/count-patterns.sh`
- `scripts/fix-neo-riemannian-images.py`
- `scripts/html-file-to-md.sh`
- `scripts/process-epub.sh`
- `scripts/process-pdf.sh`
- `scripts/setup-marker.sh`
- `scripts/split-neo-riemannian.py`
- `scripts/stage-skill-entrypoint`

### `assets/`

Observed files:

- `assets/images/logo-y250.png`
- `assets/images/logo-x1672.png`

### `site/`

Observed files:

- `site/index.html`
- `site/protocols/index.html`
- `site/protocols/ccdp/index.html`
- `site/protocols/ccdp/visual-guide/index.html`

### `workbench/`

Observed top-level workbench directories include:

- `workbench/erlang-otp-action/`
- `workbench/erlang-in-anger/`
- `workbench/design-scale-erlang-otp/`
- `workbench/programming-erlang/`
- `workbench/otp/`
- `workbench/learn-you-some-erlang/`
- `workbench/erlang-guidelines/`

Observed top-level workbench files include release notes and audit/review
material, for example `RELEASE-0.4.0.md`, `RELEASE-0.4.1.md`,
`RELEASE-0.5.0.md`, `CODE-AUDIT.md`, `RUST-CODE-AUDIT.md`, and
`hermes-compatibility-review.md`.

## Imported Project02/Project03 Planning Inputs

Project04 planning contains imported project-level artifacts under
`project04-knowledge-library-reorg/artifacts/`:

- `operator-accepted-architecture.md`
- `component-file-layout-plan.md`
- `package-target-plan.md`
- `skill-entrypoint-validation-plan.md`
- `readme-wayfinding-plan.md`
- `migration-compatibility-plan.md`
- `package-path-link-exception-plan.md`
- `implementation-sequence-roadmap.md`

These are imported artifact and later Slice02 input material. They are not
source inventory and do not substitute for inspecting
`/Users/oubiwann/lab/billosys/ai-engineering`.

Project03 `concept-card-method` is a project dependency named by the Project04
plan, but no live `knowledge/concept-card-method/` source root was observed in
this Slice01 source-surface inventory. Its accepted method-skill facts remain a
later Slice02 input, not live source-surface evidence for this slice.

## Source-Backed Early Topology Observations

These observations are deliberately early and deferred to Slice03 for final
classification:

- Rust is source-backed as a candidate atomic anchor: `knowledge/rust/SKILL.md`
  names `rust-guidelines`, routes one coherent Rust load reason, and is packaged
  by the Makefile as `rust-guidelines.zip` from `knowledge/rust/SKILL.md` plus
  `knowledge/rust/guides/`.
- `collaboration-framework` is source-backed as the accepted composite anchor:
  top-level `SKILL.md` names `collaboration-framework`, the README contains a
  framework component map, and `Makefile` packages a framework bundle from
  top-level `SKILL.md` plus selected `docs/` and `templates/` files.
- Current source frontmatter categories (`systems-programming`, `web-frontend`,
  `linting`, `static-sites`, `meta-skills`) do not yet encode Project04's
  proposed kind axis (`domain/tooling`, `framework/operational`, `method`,
  `protocol/support`) or topology axis (`atomic`, `composite`). Final topology
  classification is deferred to Slice03.

