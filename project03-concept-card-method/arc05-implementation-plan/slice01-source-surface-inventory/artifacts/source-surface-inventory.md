# Source Surface Inventory

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice01-source-surface-inventory
artifact: source-surface-inventory
status: proposed-done
source-checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-branch-observed: main
observed-on: 2026-08-31
```

## Purpose

This inventory records the live source checkout surfaces that Arc05 must plan
against before implementation. It is an input map only: Slice01 does not decide
final layout, does not edit source, and does not select schema syntax, enum
spelling, validator implementation language, Makefile edits, package-list
changes, generated zips policy, release readiness, runtime, GraphRAG, graph
database, ontology database, memory runtime, CCDP service, or live extraction
behavior.

## Accepted Arc04 Inputs

The inventory treats the accepted Arc04 outputs as fixed planning inputs:

- `v40-skill-architecture.md`: establishes the thin SKILL.md wayfinder model,
  focused guides, templates/examples as method assets, validation packaging,
  and version-history expectations.
- `v40-architecture-decision-register.md`: records accepted Arc04 choices and
  rejected alternatives. Slice01 preserves accepted Arc04 decisions rather than
  reopening architecture.
- `arc05-implementation-planning-handoff.md`: hands Arc05 the planning
  questions around source placement, packaging, validation, discoverability,
  release gates, and maintenance ownership.

The Arc04 handoff terms that matter for later planning are: thin SKILL.md,
reason to load, problem ownership, dependency direction, package behavior, and
maintenance ownership.

## Source Checkout

The live implementation source checkout observed for this slice is
`/Users/oubiwann/lab/billosys/ai-engineering` on branch `main`. The checkout was
used for inspection only. `git -C /Users/oubiwann/lab/billosys/ai-engineering
diff --quiet` passed during local verification, so no tracked source edit was
made by Slice01.

Concrete repository-level source paths inspected or named for later planning:

- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/`
- `/Users/oubiwann/lab/billosys/ai-engineering/README.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`
- `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/CLAUDE.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/`

`CLAUDE.md` is a symlink to `AGENTS.md` in the source checkout. This means
future source implementation should update `AGENTS.md` if session instructions
need to change, not create a separate `CLAUDE.md` copy.

## Knowledge Skill Layout

The current `knowledge/` tree contains these top-level domain directories:

- `knowledge/design`
- `knowledge/deno`
- `knowledge/go`
- `knowledge/js`
- `knowledge/rust`
- `knowledge/erlang`
- `knowledge/cobalt`
- `knowledge/cpp`
- `knowledge/biome`
- `knowledge/tailwindcss`

Observed skill entrypoints:

- `knowledge/design/SKILL.md`
- `knowledge/deno/SKILL-js-linter.md`
- `knowledge/go/SKILL.md`
- `knowledge/js/SKILL.md`
- `knowledge/rust/SKILL.md`
- `knowledge/erlang/SKILL.md`
- `knowledge/cobalt/SKILL.md`
- `knowledge/cpp/SKILL.md`
- `knowledge/biome/SKILL-js-linter.md`
- `knowledge/biome/SKILL-web-linter.md`
- `knowledge/tailwindcss/SKILL.md`

The dominant packaged-skill pattern is a domain entrypoint plus guide files in
a sibling `guides/` directory. Examples include `knowledge/rust/guides/`,
`knowledge/go/guides/`, `knowledge/js/guides/`,
`knowledge/erlang/guides/`, `knowledge/cpp/guides/`,
`knowledge/design/guides/`, `knowledge/cobalt/guides/`, and
`knowledge/tailwindcss/guides/`. `knowledge/rust/README.md` is the only local
knowledge README observed in the targeted inspection.

`README.md` describes a broader source anatomy for knowledge areas:
`knowledge/<domain>/SKILL.md`, `guides/`, `concept-cards/`,
`extraction-metadata/`, and `sources/`. Existing package behavior is narrower:
the Makefile package helper copies the chosen SKILL.md entrypoint and sibling
`guides/` into the generated archive. Later slices must account for that
difference if templates, examples, schema files, or validation assets belong in
the packaged concept-card method skill.

No existing top-level `knowledge/*concept*` skill directory was observed during
the targeted source inspection. The current concept-card method material found
in source is historical or framework-adjacent:

- root `SKILL.md` mentions concept cards in the collaboration-framework
  method.
- `workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md`
- `workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`

Those workbench files are useful source inputs for v4.0 migration planning, but
they are not an existing v4.0 method skill layout.

## README and Library Discoverability

`README.md` is the repository-level discoverability surface for installed
skills and source layout. It currently explains:

- the skill library under `knowledge/`;
- the expected knowledge anatomy including `SKILL.md`, `guides/`,
  `concept-cards/`, `extraction-metadata/`, and `sources/`;
- package targets and install behavior;
- `make check-skills`, `make check-package-paths`, and `make clean`;
- the repository layout for root `SKILL.md`, `Makefile`, `knowledge/`,
  `protocols/`, `docs/`, `templates/`, and `scripts/`;
- CCDP package behavior as separate from `make all`, `make skills`, and
  `make install`.

Slice04 should decide README/library discoverability prose and source version
history obligations after Slice02 and Slice03 establish what must be packaged.

## Makefile and Package Surfaces

The root `Makefile` is the source boundary for package targets, generated
archive creation, install lists, and verification targets. Observed facts:

- `BUILD := build`.
- `INSTALL_DIR ?= $(HOME)/.agents/skills`.
- `CHECK_SKILL := ./scripts/check-skill-description.sh`.
- `INSTALL_ZIPS` currently lists the generated zip outputs installed by
  `make install`.
- `ALL_SKILL_FILES` currently lists each skill entrypoint checked by
  `make check-skills`.
- `pack_skill` packages a selected skill entrypoint plus a sibling `guides/`
  directory into a zip named from the skill frontmatter `name:`.
- `scripts/stage-skill-entrypoint` performs the staged SKILL.md transformation
  for packaged archives.
- `check-package-paths: all` runs `./scripts/check-package-paths --exceptions
  package-path-exceptions.tsv $(INSTALL_ZIPS)`.
- `make clean` removes `/build` and root `/*.zip` generated artifacts.

Observed package targets from `make help` include `collab-framework`, `rust`,
`go`, `cpp`, `js`, `erlang`, `cobalt`, `design`, `tailwindcss`, `deno`,
`biome`, `skills`, `all`, `check-skills`, `check-package-paths`, `ccdp`,
`ccdp-package`, `check-ccdp-package`, `install`, `uninstall`, and `clean`.

The generated archive convention is a root generated zip named after the skill
frontmatter `name:`. Generated zips such as `rust-guidelines.zip` and
`collaboration-framework.zip` are ignored outputs. The intermediate `build/`
directory is also an ignored output. Existing `.gitignore` entries include
`/build` and `/*.zip`.

`package-path-exceptions.tsv` is the package-path exception control surface.
Its columns are `package`, `document`, `target`, `classification`,
`disposition`, `reason`, `source`, and `expires`. Current rows include allowed
package-path warnings or exceptions for existing packages. Slice04 should
decide whether concept-card method packaging requires new exception rows or
whether source links should be structured to avoid them.

## Generated Outputs and Ignored Outputs

Ignored outputs observed from the source checkout include generated archives at
the repository root and ignored working directories such as `.worktrees/`,
`workbench/`, `.claude/`, and protocol build output. No `build/` directory was
present during the targeted inspection, but `/build` is ignored and `make clean`
is defined to remove it.

Later implementation plans should distinguish source files from generated
archives. Package verification should use generated archives, not only source
tree scans, because package-path checks validate the transformed packaged
layout.

## Version History Expectations

The standing planning instructions require source version history updates when
framework or project-management source docs change. Arc04 also preserves
version history as part of the v4.0 concept-card method. Later slices should
identify the source version history file or files that must change when the
v4.0 method skill is implemented.

At minimum, Slice04 should route source version history obligations for the new
or changed SKILL.md and guides. If templates, examples, schema notes, or
validator guidance become source files, Slice04 should also decide whether
their local history entries or an enclosing versioned file must be updated.

## Planning Consequences

Slice01 did not find a source-surface fact that requires Arc05 re-sequencing, a
new slice, or a scope correction. The key constraint for later slices is that
current package behavior copies SKILL.md plus `guides/`; any accepted method
assets outside `guides/` need an explicit packaging plan, a deliberate no-op,
or a source layout that fits the existing package contract.
