# public language surface map

## Scope

This read-only inventory records current wording in the public language
surfaces Arc05 may later preserve, revise, or explicitly defer. It does not
accept final vocabulary and does not authorize source edits.

source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

Current source status:

```sh
git status --short --untracked-files=all
```

Result: clean output.

## README.md

README.md currently describes AI Engineering as "a library of Markdown skills,
guides, methods, templates, and protocol material for LLM coding assistants."
It names the top-level split:

- docs/ explains the repository for human readers
- knowledge/ stores source and derived material consumed by skills and packages
- protocols/ stores protocol distributions such as CCDP

README.md current wording also includes:

- "programming and tooling skill packages" for Rust, Go, Erlang/OTP, C++,
  JavaScript/Deno, Cobalt, Tailwind CSS, Visual Design, Biome, and Deno lint
- top-level `collaboration-framework` skill wording
- reusable support material such as `templates/GUIDE.md`
- CCDP under `protocols/ccdp/`
- CCDP packaged separately from installable skills
- practical wayfinding caveat that skill-category and topology language is
  still provisional until Project04 Arc05 settles it

## docs/

docs/ current wording:

- `docs/repository-overview.md`: "installable Markdown skills, supporting
  guides, reusable templates" and the docs/ versus knowledge/ boundary
- `docs/skill-library.md`: "collection of Markdown skills and guide material
  in knowledge/" plus current package table, "domain or tooling skill,"
  "collaboration framework," package/source distinction, and planned method
  material caveat
- `docs/collaboration-framework.md`: top-level skill for rigorous human/LLM
  engineering work, "daily-driver composer," component source paths, and
  provisional Arc05 category-language boundary
- `docs/knowledge-library-anatomy.md`: knowledge/ as knowledge substrate;
  entrypoints, guides, concept-cards, extraction metadata, sources, templates,
  examples, tools, and workbench; source roots larger than package roots; Biome
  and Deno exceptions; CCDP not under knowledge/
- `docs/building-and-installing.md`: skill package commands, per-domain and
  tooling skill zips, package roots named from frontmatter, package-path
  validation, install commands, and separate CCDP commands
- `docs/protocols.md`: protocol distribution language for CCDP, not an
  installable assistant skill; protocol source and package entrypoints
- `docs/contributing.md`: source material, package behavior, user-facing
  explanation, protocol material, new skill surface requirements, and category
  or topology wording routed to Project04 planning
- `docs/ORIGINS.md`: historical collaboration-framework provenance and links
  to current knowledge/ component material

## SKILL.md

The top-level SKILL.md public entrypoint currently names:

- `name: collaboration-framework`
- category metadata: `meta-skills`
- description language: "house framework," "working with an LLM to engineering
  standards," "operational layer," "sustained, high-stakes sessions," and
  "Does NOT load domain skills under ./knowledge/ -- loaded separately"
- source route table to knowledge/collaboration-framework,
  knowledge/engineering-methods, knowledge/project-management,
  knowledge/work-verification, knowledge/testing, knowledge/code-auditing,
  knowledge/agent-coordination, and knowledge/contribution-style

Current wording supports the accepted composite anchor but still needs Arc05
to decide how public docs should name kind and topology.

## knowledge/.*/SKILL Entrypoints

Current knowledge skill entrypoints:

| Source entrypoint | Package/frontmatter name | Current wording class |
|---|---|---|
| `knowledge/rust/SKILL.md` | `rust-guidelines` | Rust best practices, idioms, anti-patterns, APIs, concurrency, unsafe, Cargo, rustdoc, toolchain work. |
| `knowledge/go/SKILL.md` | `go-guidelines` | Go best practices, package APIs, errors, context, concurrency, tests, profiling, modules, Gio. |
| `knowledge/cpp/SKILL.md` | `cpp-guidelines` | C++ Core Guidelines, RAII, ownership, classes, templates, concurrency, CMake/tooling. |
| `knowledge/js/SKILL.md` | `javascript-deno-guidelines` | JavaScript and Deno best practices, Deno-first conventions, Biome, no-Node boundary. |
| `knowledge/erlang/SKILL.md` | `erlang-guidelines` | Erlang/OTP best practices, BEAM, supervision, fault tolerance, distributed Erlang, rebar3. |
| `knowledge/cobalt/SKILL.md` | `cobalt-guidelines` | Cobalt static site generation, Liquid templates, deployment, Rust extension context. |
| `knowledge/design/SKILL.md` | `visual-design-system` | Visual design principles, colour, typography, layout, spatial composition. |
| `knowledge/tailwindcss/SKILL.md` | `tailwindcss` | Tailwind CSS v4 utility-first styling and CSS-native configuration. |
| `knowledge/deno/SKILL-js-linter.md` | `deno-js-linter` | JavaScript/ECMAScript linting guidance from Deno lint rules. |
| `knowledge/biome/SKILL-js-linter.md` | `biome-js-linter` | JavaScript/ECMAScript linting guidance from Biome lint rules. |
| `knowledge/biome/SKILL-web-linter.md` | `biome-linter` | JavaScript/TypeScript/JSX/CSS linting guidance from Biome lint rules. |

The metadata categories visible in current frontmatter include
systems-programming, web-frontend, linting, static-sites, and meta-skills.
Those are current wording and package metadata, not an Arc05 accepted kind
taxonomy.

## Package Metadata

package metadata and package-facing names are currently visible in Makefile:

- `INSTALL_ZIPS`: collaboration-framework.zip, rust-guidelines.zip,
  go-guidelines.zip, cpp-guidelines.zip, javascript-deno-guidelines.zip,
  erlang-guidelines.zip, cobalt-guidelines.zip, visual-design-system.zip,
  tailwindcss.zip, deno-js-linter.zip, biome-js-linter.zip, biome-linter.zip
- `ALL_SKILL_FILES`: top-level SKILL.md and knowledge/*/SKILL*.md entrypoints
- `CF_FILES`: selected-file collaboration-framework package payload
- `pack_skill`: one skill file plus sibling guides/ directory into a package
  root named from entrypoint frontmatter
- CCDP package names: `CCDP_NAME := ccdp`, `CCDP_ZIP := ccdp.zip`

## Protocol and Support Surfaces

protocol wording:

- `docs/protocols.md` and `protocols/ccdp/README.md` call CCDP a protocol
  distribution/package, not an installable assistant skill.
- CCDP package entrypoints are `ccdp.zip`, `ccdp/README.md`, assembled
  protocol spec, source chapters, JSON material, visual guide, templates, and
  assembler source.

support wording:

- `README.md`, `docs/contributing.md`, and
  `docs/knowledge-library-anatomy.md` name `templates/GUIDE.md` as reusable or
  cross-cutting support material.
- Owner-local templates under knowledge/ are described as templates owned by
  that knowledge surface.

## Current Wording Risks

- "programming and tooling skill packages" is useful current wording, but it
  does not yet settle whether Arc05 should publish "domain/tooling skill" as
  the accepted phrase.
- "methods" appears in README.md, but `concept-card-method` is still planned,
  not a live installable skill.
- "daily-driver composer" appears only in collaboration-framework-focused
  docs; Slice02 should decide whether that is the public composite example.
- Metadata categories are not aligned one-to-one with the Project04 kind axis.
