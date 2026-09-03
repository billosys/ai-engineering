# Project 04: Knowledge Library Reorganization

```yaml
project: project04-knowledge-library-reorg
status: active
depends-on:
  - project02-collab-breakout:operator-accepted-architecture
  - project03-concept-card-method
blocks:
  - end-user documentation split from source/materials documentation
  - source/package path clarity for the growing knowledge library
  - README decomposition into durable topic guides
  - future knowledge-library onboarding for users and maintainers
related:
  - /Users/oubiwann/lab/billosys/ai-engineering
  - /Users/oubiwann/lab/billosys/ai-engineering/README.md
  - /Users/oubiwann/lab/billosys/ai-engineering/docs
  - /Users/oubiwann/lab/billosys/ai-engineering/knowledge
  - /Users/oubiwann/lab/billosys/ai-engineering/templates
  - /Users/oubiwann/lab/billosys/ai-engineering/protocols
  - project02-collab-breakout
  - project03-concept-card-method
```

## Planning Substrate

Planning artifacts live on orphan branch `planning`, worktree
`.worktrees/planning`, under `project04-knowledge-library-reorg/`, per
`docs/PROJECT-MANAGEMENT.md`.

The implementation checkout is the source repository's `main` worktree at
`/Users/oubiwann/lab/billosys/ai-engineering`. This project is planning-only
until an implementation arc explicitly authorizes source edits.

Slice-generated durable artifacts live under the owning slice's `artifacts/`
directory unless the operator records an override.

## Operating Mode

Project04 is in Expedited Mode as of 2026-09-02.

- CC must commit proposed-done slice changes before CDC review, using explicit
  file lists for staging and commit pathspecs.
- CDC must commit CDC review, verification, and planning updates after each
  review/change set, then report the result to the operator.
- When evidence is in place for a full slice close, close it immediately.
- After a slice closes, open the next slice immediately and report the
  `cc-prompt.md` path relative to this project directory.
- After the last slice of an arc closes, continue to formal arc close, then
  open the next roadmap-provided arc and its first slice.

## Definition of Done

The project is done when the repository has a clear, tested, and documented
split between:

- `docs/` as end-user documentation about the repository's materials, packages,
  methods, protocols, and knowledge library; and
- `knowledge/` as the raw and derived knowledge-library substrate consumed by
  domain, tooling, framework, and method skills.

Specifically:

- The current `docs/`, `knowledge/`, `templates/`, `protocols/`, `README.md`,
  `SKILL.md`, package lists, and package-path exceptions are inventoried from
  the live source checkout before any moves are planned.
- Every source-like or substrate-like document currently under `docs/` has an
  accepted target home, with the default hypothesis that framework and method
  source material moves under `knowledge/` unless an explicit exception is
  recorded.
- The top-level README is shortened into an orientation document, and the
  deeper subject explanations move into focused end-user docs under `docs/`.
- The project establishes public language for skill categories: domain/tooling
  skills, framework/operational skills, method skills, and any category the
  inventory shows should be named or explicitly rejected.
- The project establishes a separate skill-topology distinction between
  atomic skills and composite skills. A Rust programming-language skill is the
  initial candidate anchor for an atomic skill; `collaboration-framework` is
  the accepted anchor for a composite skill because Project02 defines it as a
  daily-driver composer over specialist components.
- Source/package behavior remains valid after path changes: package-local
  links, generated zip roots, installed skill entrypoints, CCDP package
  separation, README links, and validation commands still agree.
- Compatibility surfaces are preserved or deliberately migrated: `AGENTS.md`,
  `CLAUDE.md` symlinks, Make targets, package-path exceptions, release notes,
  protocol entrypoints, and skill load paths remain clear.
- The final repository layout lets an end user start in `README.md`, follow
  `docs/` for explanation, and follow `knowledge/` for the actual knowledge
  library materials without path or category ambiguity.

## Boundaries

In scope:

- Directory reorganization for `docs/` material whose role is actually source
  material, framework substrate, methodology substrate, extraction guidance,
  templates, or skill-library knowledge rather than end-user documentation.
- README decomposition into focused user-facing docs such as repository
  overview, skill library, collaboration framework, knowledge-library anatomy,
  building/installing, protocols, and contribution guidance.
- Re-thinking and re-writing how this repo talks about skills and whether it
  distinguishes domain/tooling, framework/operational, method, protocol, and
  support-surface categories.
- Assessing what makes a skill atomic versus composite, how that topology
  relates to skill categories, and what the distinction changes for loading,
  packaging, README wording, and source layout.
- Updating package, validation, link, and discoverability surfaces required by
  accepted path moves.
- Coordinating with Project02's accepted collaboration-framework component map
  and Project03's method-skill vocabulary.

Out of scope until an accepted implementation plan:

- Moving source files, editing source `README.md`, changing `SKILL.md`, moving
  framework docs, changing Makefile/package lists, changing package-path
  exceptions, or generating new zips.
- Treating `docs/` cleanup as permission to rewrite source prose. Mechanical
  moves must preserve content unless a specific doc-rewrite slice says
  otherwise.
- Folding CCDP into the skill library without a separate protocol-package
  decision. CCDP is related, but currently packaged separately from installable
  skills.
- Re-opening Project02 component architecture or Project03 method-skill
  architecture except to consume their accepted outputs.
- Treating "atomic" as a synonym for "domain" or "composite" as a synonym for
  "framework" before Arc01/Arc05 evidence supports that model.
- Creating a runtime knowledge database, search service, graph store, or memory
  protocol implementation.

## Project-Level Inputs

The following imported artifacts are project-level inputs copied from Project02
planning. They are evidence to assess, not source-edit authorization:

- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`
- `artifacts/package-target-plan.md`
- `artifacts/skill-entrypoint-validation-plan.md`
- `artifacts/readme-wayfinding-plan.md`
- `artifacts/migration-compatibility-plan.md`
- `artifacts/package-path-link-exception-plan.md`
- `artifacts/implementation-sequence-roadmap.md`
- `artifacts/external-ontology-rubric-research.md`

Project04 must preserve the accepted Project02 facts that
`collaboration-framework` is a daily-driver composer, that specialist
components can be independently loadable, and that CCDP remains a separate
protocol distribution unless a later project explicitly changes that package
policy.

The external ontology rubric research is a Project04 planning input, not an
accepted taxonomy. Arc01 Slice03 must test its proposed kind/topology model
against the live source tree before Arc05 turns any language into public docs.

## Working Hypothesis

The likely target model is:

- `README.md`: short repository orientation and pointer map.
- `docs/`: user-facing documentation about what exists, how to choose it, how
  to install/build it, and how the parts relate.
- `knowledge/`: source and derived knowledge materials, including domain
  skills, method skills, and likely framework/operational skill source
  materials after Project02's component architecture is applied.
- `protocols/`: protocol distributions whose package behavior is not the same
  as installable assistant skills, unless this project explicitly accepts a
  different protocol-library model.
- `templates/`: reusable skeletons only if they remain cross-cutting; otherwise
  templates move under the owning knowledge or protocol surface.

Skill language likely needs two independent axes:

- **Kind axis:** what the skill is about, such as domain/tooling,
  framework/operational, method, or another accepted category.
- **Topology axis:** whether the skill is atomic or composite.

An atomic skill owns one coherent load reason and should satisfy that primary
load reason without requiring a second skill. It may reference, recommend, or
route to adjacent skills, but its core contract stands alone. `knowledge/rust`
is the initial anchor example to test against this definition.

A composite skill owns orchestration across multiple loadable units. It may
carry a compact local posture, adapter, or route table, but its main value is
selecting, sequencing, or composing other skills/components. The imported
Project02 architecture treats `collaboration-framework` as the anchor example:
the daily-driver composer over `engineering-methods`, `project-management`,
`work-verification`, `testing`, `code-auditing`, `agent-coordination`, and
`contribution-style`.

The kind and topology axes should not be collapsed. A method skill may be
atomic if it teaches one reusable method end to end; a framework skill may be
composite if it exists to route across specialized components. Arc01 and Arc05
must test the full library before Project04 turns these examples into public
taxonomy.

This is a hypothesis, not a source-edit instruction. Arc01 must test it against
the live tree and Project02/Project03 evidence before Arc02 authorizes moves.

## Arc Roadmap

### Arc 01: Repository Material Inventory and Classification

Status: closed on 2026-09-02.

Capability: produce a source-backed inventory of current `docs/`,
`knowledge/`, `templates/`, `protocols/`, README, skill, and packaging
surfaces, classifying each file or directory by role: end-user documentation,
knowledge substrate, skill entrypoint, framework/operational material, method
material, protocol distribution, template/support asset, packaging gate, or
scratch/workbench material.

The inventory must also classify every current and planned skill surface by
skill kind and skill topology. It should treat Rust as a candidate atomic skill
anchor and `collaboration-framework` as the accepted composite skill anchor,
then test whether other surfaces fit those anchors, require subtypes, or expose
bad category assumptions.

This arc should also recover and assess prior proposals or assumptions about
moving materials under `knowledge/`, including Project02 source/package
analysis and Project03 method-skill architecture.

Detailed arc planning and closure evidence lives under
`arc01-material-inventory/`. Slice01, `slice01-source-surface-inventory`,
Slice02, `slice02-imported-architecture-integration`, Slice03,
`slice03-skill-topology-classification`, and Slice04,
`slice04-arc01-synthesis`, are verified-closed. Arc01 is closed and provides
the source-backed inventory/classification base for Arc02.

### Arc 02: Target Directory Contract and Migration Plan

Status: closed on 2026-09-02.

Expected capability: define the accepted target layout, path-contract rules,
exception list, compatibility strategy, and migration sequence for turning
`docs/` into user documentation and `knowledge/` into the repository's
knowledge-library substrate.

Arc02 must decide which materials move, which remain, which need wrapper docs,
which get package-local path exceptions, and where the Project02 component
architecture and Project03 method-skill plan land. It must also decide whether
atomic and composite skills share the same source-root convention under
`knowledge/`, or whether composite/component groups need an additional
directory contract.

Detailed arc planning and closure evidence lives under
`arc02-directory-contract/`. Slice01,
`slice01-decision-surface-inventory`, is verified-closed. Slice02,
`slice02-accepted-directory-contract`, is verified-closed. Slice03,
`slice03-migration-validation-plan`, is verified-closed. Slice04,
`slice04-implementation-handoff`, is verified-closed. Arc02 is closed and
provides the accepted directory contract and migration plan for Arc03.

### Arc 03: Directory Reorganization Implementation

Status: closed on 2026-09-02.

Expected capability: execute the accepted file moves and link updates in
implementation-sized slices while preserving source history, minimizing prose
changes, and keeping package/build validation green after each slice.

This arc preferred mechanical moves first and reserved rewrite work for later
arcs so path breakage and content edits were not entangled.

Detailed arc planning and closure evidence lives under
`arc03-directory-reorg/`. Slice01 through Slice06 are verified-closed. Arc03
closed with accepted directory reorganization source edits landed, package
roots inspected, and path/link/package validation green.

### Arc 04: README Decomposition and End-User Documentation

Status: closed on 2026-09-03.

Expected capability: split the current README into a concise top-level
orientation plus focused `docs/*.md` end-user guides that explain the
repository, skill library, collaboration framework, build/install workflow,
protocol distribution, and contribution paths.

The resulting `docs/` tree should explain the materials without becoming the
material substrate itself.

Detailed arc planning and closure evidence lives under `arc04-user-docs/`.
Slice01, `slice01-readme-docs-decomposition-map`, Slice02,
`slice02-readme-orientation-rewrite`, Slice03,
`slice03-focused-end-user-guide-set`, and Slice04,
`slice04-doc-link-navigation-reconciliation`, are verified-closed. Arc04 is
closed and provides the README/docs public documentation base for Arc05.

### Arc 05: Skill Vocabulary, Atomicity, and Public Positioning

Status: active as of 2026-09-03.

Expected capability: settle the public language for the repo's skill types and
support surfaces, including whether to distinguish domain/tooling skills,
framework/operational skills, method skills, protocol packages, and templates;
and separately whether to distinguish atomic skills from composite skills.

This arc should rewrite README/docs/SKILL wayfinding only after Arc01 and
Arc02 define the actual categories present in the source tree.

Detailed arc planning is open under `arc05-skill-vocabulary/`. Slice01,
`slice01-public-language-surface-inventory`, is open as a read-only public
language inventory and evidence synthesis before accepted vocabulary decisions
or source wording edits.

### Arc 06: Validation, Packaging, and Release Readiness

Status: not yet planned in detail.

Expected capability: verify that the reorganized repository works as a source
checkout, packaged skill library, installed Codex skill set, and CCDP protocol
package, with path checks, package checks, README/docs links, and operator
acceptance all reconciled.

This arc closes the project only after the final layout is demonstrably usable
from the end-user entrypoints and the package/install entrypoints.

## Current Status

Project04 is active and operating in Expedited Mode. Arc01,
`arc01-material-inventory`, Arc02, `arc02-directory-contract`, and Arc03,
`arc03-directory-reorg`, are closed. Arc03 landed the accepted directory
reorganization implementation, with path/link/package validation green.

Arc04, `arc04-user-docs`, is closed. It delivered the concise README
orientation, focused end-user docs, and final README/docs reconciliation.

Arc05, `arc05-skill-vocabulary`, is active. Slice01,
`slice01-public-language-surface-inventory`, is verified-closed. Slice02,
`slice02-accepted-vocabulary-positioning`, is open.

Arc05 source edits are authorized only through opened Arc05 slice prompts.
Arc05 owns final public skill-kind and atomic/composite vocabulary.

The next execution action is CC completion of:
`arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/cc-prompt.md`.

## Version History

### v1.23 - 2026-09-03

Recorded Arc05 Slice01 as verified-closed after CDC reproduced all six ledger
rows, checked the planning commit, and confirmed no source commit was created.
Opened Slice02, `slice02-accepted-vocabulary-positioning`, to decide accepted
public vocabulary, examples, avoid-list, source-edit authorization, and
re-entry conditions before any source wording implementation begins.

### v1.22 - 2026-09-03

Recorded Arc04 Slice04 as verified-closed, closed Arc04 after CDC reproduced
the arc-level composition row, and marked project ledger row P-4 done. Opened
Arc05, `arc05-skill-vocabulary`, and opened Slice01,
`slice01-public-language-surface-inventory`, as a read-only inventory and
evidence synthesis before accepted public vocabulary decisions or source
wording edits.

### v1.21 - 2026-09-02

Recorded Arc04 Slice03 as verified-closed after CDC reproduced all six ledger
rows, checked the source and planning commits, reran README/docs and package
validation gates, and confirmed the focused guide set now explains repository,
skill library, collaboration framework, knowledge library, build/install,
protocol, and contribution routes. Opened Slice04,
`slice04-doc-link-navigation-reconciliation`, as the final Arc04 slice for
documentation link/navigation reconciliation and Arc04 close readiness.

### v1.20 - 2026-09-02

Recorded Arc04 Slice02 as verified-closed after CDC reproduced all six ledger
rows, checked the source and planning commits, reran the README/docs and
package validation gates, and confirmed the concise README orientation with
seven focused docs stubs. Opened Slice03,
`slice03-focused-end-user-guide-set`, to expand those stubs into usable
end-user guides while preserving the `docs/` versus `knowledge/` boundary and
leaving final skill vocabulary work to Arc05.

### v1.0 - 2026-09-01

Initial roadmap opened from operator direction to clean up `docs/` so it
contains user documentation about the repository's materials, while moving
actual material substrate into `knowledge/` where appropriate. The project
records the `knowledge/` move as a working hypothesis to test against the live
source tree, Project02 accepted framework architecture, and Project03
method-skill vocabulary before source edits begin.

### v1.1 - 2026-09-01

Recorded imported Project02 architecture and implementation-planning materials
as project-level inputs. Added the atomic/composite skill-topology axis as a
separate planning concern from domain/tooling/framework/method skill kind, with
Rust as the initial atomic anchor and `collaboration-framework` as the accepted
composite anchor.

### v1.2 - 2026-09-01

Opened Arc01, `arc01-material-inventory`, and Slice01,
`slice01-source-surface-inventory`, for the read-only source inventory pass
that will ground later directory-contract and skill-topology decisions.

### v1.3 - 2026-09-01

Added `artifacts/external-ontology-rubric-research.md` as project-level
research input for non-tautological skill/knowledge, kind/topology, and
atomic/composite classification. The research remains input for Arc01 Slice03
and Arc05, not an accepted public taxonomy.

### v1.4 - 2026-09-01

Recorded Slice01 as verified-closed and opened Arc01 Slice02,
`slice02-imported-architecture-integration`, for imported Project02/Project03
architecture integration and Arc02 question preparation.

### v1.5 - 2026-09-01

Recorded Slice02 as verified-closed. Arc01 is ready for Slice03 planning,
which will classify skill kind and atomic/composite topology using the
source inventory, imported-architecture integration packet, and external
ontology rubric input.

### v1.6 - 2026-09-01

Opened Arc01 Slice03, `slice03-skill-topology-classification`, for the
skill-kind/topology decision instrument, classification matrix, and public
language implication artifacts.

### v1.7 - 2026-09-01

Recorded Arc01 Slice03 as verified-closed. Arc01 is ready to plan Slice04,
which will synthesize the source inventory, imported-architecture integration,
and skill-topology classification into Arc02 directory-contract readiness
inputs.

### v1.8 - 2026-09-01

Opened Arc01 Slice04, `slice04-arc01-synthesis`, for the Arc02 readiness
packet, directory-contract requirements list, and Arc01 synthesis decision
register.

### v1.9 - 2026-09-02

Recorded Arc01 Slice04 as verified-closed. Arc01 has completed all planned
child slices and is ready for formal arc close before Arc02 opens.

### v1.10 - 2026-09-02

Closed Arc01 after CDC reproduced the arc-level composition row. Project ledger
row P-1 is done; Arc02 is the next planning action and remains unopened until
its target directory-contract packet is created.

### v1.11 - 2026-09-02

Recorded Project04 Expedited Mode. Opened Arc02,
`arc02-directory-contract`, and Slice01,
`slice01-decision-surface-inventory`, for the decision surface inventory that
will feed the accepted target directory contract.

### v1.12 - 2026-09-02

Recorded Arc02 Slice01 as verified-closed after CDC reproduced all six ledger
rows. Opened Slice02, `slice02-accepted-directory-contract`, to select the
accepted target directory contract and source/package root contract while
preserving source-edit authorization boundaries.

### v1.13 - 2026-09-02

Recorded Arc02 Slice02 as verified-closed after CDC reproduced all six ledger
rows. Opened Slice03, `slice03-migration-validation-plan`, to translate the
accepted directory/source/package contract into migration sequencing,
validation gates, compatibility policy, and package-path exception policy.

### v1.14 - 2026-09-02

Recorded Arc02 Slice03 as verified-closed after CDC reproduced all six ledger
rows. Opened Slice04, `slice04-implementation-handoff`, to prepare the Arc03
implementation readiness packet, source-edit slice roadmap, and Arc02 decision
summary from verified Arc02 evidence.

### v1.15 - 2026-09-02

Recorded Arc02 Slice04 as verified-closed, closed Arc02 after CDC reproduced
the arc-level composition row, marked project ledger row P-2 done, opened
Arc03, `arc03-directory-reorg`, and opened Slice01,
`slice01-preflight-source-status-impact-map`, as a preflight-only baseline
before source-edit slices.

### v1.16 - 2026-09-02

Recorded Arc03 Slice01 as verified-closed after CDC reproduced all six ledger
rows. Opened Slice02, `slice02-top-level-compatibility-decision`, as the
top-level `SKILL.md` compatibility gate before collaboration-framework
composer source material moves.

### v1.17 - 2026-09-02

Recorded Arc03 Slice02 as verified-closed after CDC reproduced all six ledger
rows and reran `make check-skills`, `make collab-framework`, and package
entrypoint inspection. Opened Slice03,
`slice03-mechanical-framework-source-moves`, as the first source-edit move
slice for the current selected-file collaboration-framework payload.

### v1.18 - 2026-09-02

Closed Arc03 after CDC verified Slice06 and reproduced the arc-level
composition row. Marked project ledger row P-3 done, opened Arc04,
`arc04-user-docs`, and opened Slice01,
`slice01-readme-docs-decomposition-map`, as the read-only README/docs
decomposition map before user-facing documentation source edits begin.

### v1.19 - 2026-09-02

Recorded Arc04 Slice01 as verified-closed after CDC reproduced all six ledger
rows and confirmed no source commit was created. Opened Slice02,
`slice02-readme-orientation-rewrite`, as the first README/docs source-edit
slice to rewrite the top-level README orientation and repair stale post-Arc03
documentation routes discovered by Slice01.
