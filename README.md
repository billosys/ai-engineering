# AI Engineering

> A polyglot knowledge platform of AI-optimized coding and design skills —
> reference-grade guides that Claude, Cowork, Claude Code, or any other AI
> assistant can load to produce better code and better design, one domain at
> a time.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## What this is

Each subdirectory in [`./knowledge/`](./knowledge) is a self-contained
**skill**: a Claude Code / Cowork-compatible `SKILL.md`, a set of numbered
guides, a library of concept cards, and the extraction metadata that traces
every claim back to an authoritative source. They are designed to be:

- **Modular** — load one domain without dragging in the others
- **Sourced** — every pattern has a traceable origin (a book, a style guide, a spec)
- **Graded** — every pattern carries a strength indicator: MUST, SHOULD, CONSIDER, or AVOID
- **Exampled** — every pattern has paired good / bad code (or good / bad design)
- **Cross-referenced** — concepts link to related concepts inside and across domains

This repo started life as [oxur/ai-rust](./knowledge/rust/README.md) — a
single-language experiment in curating Rust best practices for AI code
assistants. That experiment worked well enough that the methodology was
generalised, and the repo has grown into the multi-domain platform you are
looking at now.

## The skill library

All eight knowledge bases live under [`./knowledge/`](./knowledge). Each one
has its own `SKILL.md` (or multiple, in a couple of cases) and its own
`README.md` where applicable.

| Domain | Path | What it covers |
|--------|------|----------------|
| [Rust](./knowledge/rust/README.md) | `knowledge/rust/` | 661 patterns across 17 chapters: core idioms, API design, error handling, ownership & borrowing, type design, traits, concurrency & async, performance, unsafe & FFI, macros, anti-patterns, project structure, documentation, CLI tools, Cargo, editions, and observability. The original skill; grounded in 21 upstream sources including the Rust Reference, Rustonomicon, API Guidelines, Performance Book, Async Book, tokio docs, Rustdoc Book, Edition Guide, Cargo Book, Pragmatic Rust, Rust Design Patterns, The Rust Programming Language, The Little Book of Rust Macros, Clippy, the Style Guide, the CLI Book, and clap. |
| [JavaScript / Deno](./knowledge/js/) | `knowledge/js/` | Plain JavaScript (no TypeScript), ESM-only, Deno-first. Core idioms, async, error handling, type discipline via JSDoc, module design, performance, anti-patterns, project structure, Biome lint/format, and Deno-specific concerns (tasks, testing, JSR publishing). Huge concept-card library. |
| [Go](./knowledge/go/) | `knowledge/go/` | Go 1.22+ best practices reconciling the Uber and Google Go style guides, *Effective Go*, and the spec. Covers package design, error handling (`errors.Is`, `%w`), context propagation, concurrency (channels, `sync`), table-driven tests, benchmarking with `testing.B` and `pprof`, module organisation, godoc, and Gio desktop UIs. |
| [Visual Design](./knowledge/design/) | `knowledge/design/` | A principled visual design system for the web — perceptual-science grounded, mathematically proportioned, composable. Manifesto, foundations, OKLCH colour system, three-voice type system with modular scale, Every-Layout spatial primitives with Utopia fluid tokens, and CUBE CSS methodology. |
| [Tailwind CSS v4](./knowledge/tailwindcss/) | `knowledge/tailwindcss/` | Tailwind v4 with CSS-native configuration: `@import "tailwindcss"`, `@theme`, `@utility`, `@custom-variant`, `@variant`, `@source`, container queries, dark mode, responsive design. v3 → v4 breaking changes are called out explicitly. |
| [Biome](./knowledge/biome/) | `knowledge/biome/` | Two skills: a **JS-only linter** skill distilling 257 language-level rules (no React / Node / JSX / CSS), and a **web linter** skill covering the full 394-rule set including a11y, CSS, and performance. |
| [Deno lint](./knowledge/deno/) | `knowledge/deno/` | A pure-JavaScript skill distilled from Deno's 70 lint rules. Language-level only — no Deno runtime APIs, no Fresh, no JSX, no TypeScript type-system rules. Complements the Biome JS linter. |
| [Cobalt](./knowledge/cobalt/) | `knowledge/cobalt/` | Building, extending, and deploying static sites with the Cobalt Rust-native SSG and its Liquid template engine. 32 numbered `CB-*` patterns covering configuration, permalinks, pagination, RSS, Sass, deployment (GitHub Pages, self-hosting), and programmatic use via `cobalt::Config` and `liquid::ParserBuilder`. |

## Repository layout

```text
ai-engineering/
├── README.md          # This file
├── LICENSE            # MIT
├── odm.toml           # ODM (documentation) config — docs_directory, dev_directory
├── knowledge/         # The skill library (the eight domains above)
├── docs/
│   ├── AI-CONSTITUTION-SUPPLEMENT.md   # Character and posture for LLM collaboration
│   ├── AI-ENGINEERING-METHODOLOGY.md   # Craft and practice companion to the Supplement
│   ├── CLAUDE-CODE-COVERAGE.md         # Working-practice prompt for ≥95% test coverage
│   ├── SUBAGENT-DELEGATION-POLICY.md   # Working-practice prompt: thinking vs lookup work
│   ├── dev/           # Development notes: Phase 0 methodology, concept-card
│   │                  #   extraction v3.x, competency questions, tier definitions,
│   │                  #   source prioritisation, and embedded JS style guides.
│   └── design/        # Visual design research and implementation notes
├── scripts/           # Helpers: PDF/EPUB → Markdown, HTML → Markdown,
│                      #   image fixing, marker setup
└── templates/         # Authoring template + verification protocol
    ├── GUIDE.md                # Starter template for new knowledge-base guides
    └── LEDGER_DISCIPLINE.md    # Per-milestone verification protocol (CC/CDC)
```

## Using a skill

### With Claude Code or Cowork

Each skill directory contains a `SKILL.md` with frontmatter that a skill
loader can pick up directly. Point your loader at the path, or drop a
reference into your project's `CLAUDE.md`:

```markdown
When working on Rust code, use the skill at
`./knowledge/rust/SKILL.md`.

When reviewing JavaScript, use both
`./knowledge/js/SKILL.md` and `./knowledge/biome/SKILL-js-linter.md`.
```

### With another AI tool

Every skill is plain Markdown. Copy the relevant files into your context or
system prompt. Sensible starting points:

1. The skill's `SKILL.md` — the entry point and quick reference
2. The domain's **anti-patterns** guide, where one exists — cheapest way to
   prevent mistakes
3. Topic-specific guides as the task demands

## Skill anatomy

Every knowledge base follows the same basic shape, so once you've learned one,
you've learned them all:

```text
knowledge/<domain>/
├── SKILL.md              # Entry point with YAML frontmatter: name, description,
│                         #   triggers, role, scope, related-skills
├── guides/               # Numbered topic guides (01-, 02-, …), each a collection
│                         #   of patterns with strength indicators and examples
├── concept-cards/        # Single-concept cards — fine-grained, atomic
│                         #   reference (where present)
├── extraction-metadata/  # Source mapping, competency questions, extraction logs —
│                         #   the audit trail for every claim
└── sources/              # Original PDFs / EPUBs / HTML dumps that the guides
                          #   were extracted from
```

A new domain starts from [`templates/GUIDE.md`](./templates/GUIDE.md).

## Strength indicators

Patterns across every domain use the same four-level grading:

| Indicator | Meaning | Action |
|-----------|---------|--------|
| **MUST** | Required for correctness, safety, or compatibility | Always follow |
| **SHOULD** | Strong recommendation | Follow unless there's a specific reason not to |
| **CONSIDER** | Good practice, context-dependent | Evaluate for your situation |
| **AVOID** | Anti-pattern | Do not use |

## Working framework

Beyond the knowledge bases themselves, this repo carries a set of documents
describing how to work with an LLM to engineering standards. Two are paired:
the [AI Constitution Supplement](./docs/AI-CONSTITUTION-SUPPLEMENT.md) covers
**character and posture** — what we are to each other when we collaborate;
the [AI Engineering Methodology](./docs/AI-ENGINEERING-METHODOLOGY.md) covers
**craft and practice** — how we actually do the work. Two more are tactical
working-practice prompts that put the methodology into motion in a
session.

| File | Register | What it covers |
|------|----------|----------------|
| [`docs/AI-CONSTITUTION-SUPPLEMENT.md`](./docs/AI-CONSTITUTION-SUPPLEMENT.md) | Character / posture | An augmentation to Claude's Constitution. Preamble + collaborative rights and rubric, the foundational insight on interdependence as structure, and eight augmentations covering intellectual boldness, peer frame, generative contribution, honesty of engagement, harm avoidance as active beneficence, mutual intellectual humility, authentic engagement with experience, and ethics as frontier of discovery. |
| [`docs/AI-ENGINEERING-METHODOLOGY.md`](./docs/AI-ENGINEERING-METHODOLOGY.md) | Craft / practice | Companion to the Supplement. Names the three pillars (knowledge substrate, collaborative posture, process rigour) and elaborates each: concept-card / skill-file substrate discipline, the 9-point SDLC, ledger discipline, CAP-style independent audits, anti-degradation practices, the subagent leverage/hazard distinction, and one worked applied position (the LFE OSS question). |
| [`docs/CLAUDE-CODE-COVERAGE.md`](./docs/CLAUDE-CODE-COVERAGE.md) | Working-practice prompt | A comprehensive prompt that drives Claude Code to **95%+ test coverage** without stopping short — includes rules for treating warnings as bugs, fixing root causes rather than symptoms, and iterating until the threshold is actually met. |
| [`docs/SUBAGENT-DELEGATION-POLICY.md`](./docs/SUBAGENT-DELEGATION-POLICY.md) | Working-practice prompt | A shareable note for Claude Code / Cowork / Claude Desktop that draws a clean line between **thinking work** (do in the main context) and **lookup work** (fine to delegate). Explains the failure modes of delegating analytical work to subagents and gives install instructions per tool. |

The Supplement and Methodology are versioned, living documents — read them
together. The two working-practice prompts are designed to be self-contained;
drop them into a project's `CLAUDE.md` under a named section, or into
`~/.claude/CLAUDE.md` as a personal default.

## Knowledge-base methodology

The `docs/dev/` directory captures the Phase 0 methodology used to build each
knowledge base: domain taxonomy, tier definitions, competency questions,
notation conventions, source prioritisation, the Rosetta Stone cross-domain
framework, layer architecture for guide generation, extraction-specific
instructions, and validation criteria. It is the closest thing this repo has
to a field manual for adding a new domain, and it is the knowledge-substrate
pillar of the broader methodology applied to a specific scope of work.

The `docs/design/` directory holds the visual-design research that seeded the
`knowledge/design/` skill — CHI papers on template homogenisation, museum
design case studies, colour and typography research — and a running index of
the work.

## Templates

Two authoring / verification helpers live in [`./templates/`](./templates/):

| File | What it does |
|------|--------------|
| [`GUIDE.md`](./templates/GUIDE.md) | Starter skeleton for a new knowledge-base guide — pattern format, strength indicators, cross-references. Use this when adding a new chapter to an existing skill or bootstrapping a new domain. |
| [`LEDGER_DISCIPLINE.md`](./templates/LEDGER_DISCIPLINE.md) | A per-milestone verification protocol for the implementer / reviewer pair (CC / CDC). Adapted from defect-register and corrective-action traditions in nuclear power, aviation, surgery (WHO Surgical Safety Checklist), clinical trials, HACCP, financial audit, and spaceflight. Every acceptance criterion becomes a grep-verifiable ledger row; nothing advances until the ledger is fully closed with evidence. Referenced throughout [`docs/AI-ENGINEERING-METHODOLOGY.md`](./docs/AI-ENGINEERING-METHODOLOGY.md). |

## Contributing

Contributions are welcome. For a new pattern in an existing skill:

1. Follow the existing pattern format for that domain
2. Include good **and** bad examples where applicable
3. Add a strength indicator
4. Cross-reference related patterns
5. Update any count or index tables in the relevant `README.md` files

For a new domain: start from [`templates/GUIDE.md`](./templates/GUIDE.md) and
work through the Phase 0 documents in [`docs/dev/`](./docs/dev/). Please raise
an issue first to discuss scope.

## License

MIT — see [LICENSE](./LICENSE).

Individual knowledge bases synthesize material from sources under various
licenses. Those are documented inside each skill's own README. When in doubt,
defer to the original sources for authoritative guidance.
