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

All nine knowledge bases live under [`./knowledge/`](./knowledge). Each one
has its own `SKILL.md` (or multiple, in a couple of cases) and its own
`README.md` where applicable.

| Domain | Path | What it covers | Codex ready? |
|--------|------|----------------|--------------|
| [Rust](./knowledge/rust/README.md) | `knowledge/rust/` | 661 patterns across 17 chapters: core idioms, API design, error handling, ownership & borrowing, type design, traits, concurrency & async, performance, unsafe & FFI, macros, anti-patterns, project structure, documentation, CLI tools, Cargo, editions, and observability. The original skill; grounded in 21 upstream sources including the Rust Reference, Rustonomicon, API Guidelines, Performance Book, Async Book, tokio docs, Rustdoc Book, Edition Guide, Cargo Book, Pragmatic Rust, Rust Design Patterns, The Rust Programming Language, The Little Book of Rust Macros, Clippy, the Style Guide, the CLI Book, and clap. | ✅ |
| [JavaScript / Deno](./knowledge/js/) | `knowledge/js/` | Plain JavaScript (no TypeScript), ESM-only, Deno-first. Core idioms, async, error handling, type discipline via JSDoc, module design, performance, anti-patterns, project structure, Biome lint/format, and Deno-specific concerns (tasks, testing, JSR publishing). Huge concept-card library. | ✅ |
| [Go](./knowledge/go/) | `knowledge/go/` | Go 1.22+ best practices reconciling the Uber and Google Go style guides, *Effective Go*, and the spec. Covers package design, error handling (`errors.Is`, `%w`), context propagation, concurrency (channels, `sync`), table-driven tests, benchmarking with `testing.B` and `pprof`, module organisation, godoc, and Gio desktop UIs. | ✅ |
| [Erlang / OTP](./knowledge/erlang/) | `knowledge/erlang/` | Erlang/OTP 27+ best practices: 281 patterns across 17 chapters — core idioms, API design, error handling, data & types, functions & pattern matching, processes & concurrency, OTP behaviours, supervision & applications, fault tolerance (let-it-crash), performance, anti-patterns (with a dedicated AI-misuse subset), project structure, documentation (`-doc`/`-moduledoc`), production ops (recon, tracing, crash dumps), testing (EUnit / Common Test / PropEr), distribution, and tooling (rebar3, dialyzer, xref). Grounded in the Erlang Programming Rules, the OTP Design Principles, Reference Manual, and Efficiency Guide, Inaka's and nuex's style guides, *Erlang in Anger*, *Learn You Some Erlang*, and the EDoc guide, plus the books *Programming Erlang*, *Erlang and OTP in Action*, and *Designing for Scalability with Erlang/OTP*. | ✅ |
| [Visual Design](./knowledge/design/) | `knowledge/design/` | A principled visual design system for the web — perceptual-science grounded, mathematically proportioned, composable. Manifesto, foundations, OKLCH colour system, three-voice type system with modular scale, Every-Layout spatial primitives with Utopia fluid tokens, and CUBE CSS methodology. | ✅ |
| [Tailwind CSS v4](./knowledge/tailwindcss/) | `knowledge/tailwindcss/` | Tailwind v4 with CSS-native configuration: `@import "tailwindcss"`, `@theme`, `@utility`, `@custom-variant`, `@variant`, `@source`, container queries, dark mode, responsive design. v3 → v4 breaking changes are called out explicitly. | 🚧 |
| [Biome](./knowledge/biome/) | `knowledge/biome/` | Two skills: a **JS-only linter** skill distilling 257 language-level rules (no React / Node / JSX / CSS), and a **web linter** skill covering the full 394-rule set including a11y, CSS, and performance. | 🚧 |
| [Deno lint](./knowledge/deno/) | `knowledge/deno/` | A pure-JavaScript skill distilled from Deno's 70 lint rules. Language-level only — no Deno runtime APIs, no Fresh, no JSX, no TypeScript type-system rules. Complements the Biome JS linter. | 🚧 |
| [Cobalt](./knowledge/cobalt/) | `knowledge/cobalt/` | Building, extending, and deploying static sites with the Cobalt Rust-native SSG and its Liquid template engine. 32 numbered `CB-*` patterns covering configuration, permalinks, pagination, RSS, Sass, deployment (GitHub Pages, self-hosting), and programmatic use via `cobalt::Config` and `liquid::ParserBuilder`. | 🚧 |

## Repository layout

```text
ai-engineering/
├── README.md          # This file
├── SKILL.md           # Top-level `collaboration-framework` skill — the
│                      #   character-and-craft entry point (see below)
├── Makefile           # `make collab-framework` → collaboration-framework.zip
├── LICENSE            # MIT
├── odm.toml           # ODM (documentation) config — docs_directory, dev_directory
├── knowledge/         # The skill library (the nine domains above)
├── docs/
│   ├── AI-CONSTITUTION-SUPPLEMENT.md   # Character and posture for LLM collaboration
│   ├── AI-ENGINEERING-METHODOLOGY.md   # Craft and practice companion to the Supplement
│   ├── ASSET-ORGANISATION.md           # Slice/arc layout + the confirmation protocol
│   ├── CLAUDE-CODE-COVERAGE.md         # Working-practice prompt for ≥95% test coverage
│   ├── CODE-AUDIT.md                   # Prompt for recurring, whole-repo quality checks
│   ├── CONTRIBUTION-STYLE.md           # Voice and discipline for upstream OSS tickets
│   ├── SUBAGENT-DELEGATION-POLICY.md   # Working-practice prompt: thinking vs lookup work
│   ├── dev/           # Development notes: Phase 0 methodology, concept-card
│   │                  #   extraction v3.x, competency questions, tier definitions,
│   │                  #   source prioritisation, and embedded JS style guides.
│   └── design/        # Visual design research and implementation notes
├── scripts/           # Helpers: PDF/EPUB → Markdown, HTML → Markdown,
│                      #   image fixing, marker setup
└── templates/         # Authoring templates + verification protocol
    ├── GUIDE.md                # Starter template for new knowledge-base guides
    ├── LEDGER-DISCIPLINE.md    # Per-slice verification protocol (CC/CDC)
    └── CONTRIBUTION-TICKET.md  # On-disk template for upstream OSS tickets
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

### Packaging a skill as a zip

The [`Makefile`](./Makefile) bundles any skill into a self-contained,
distributable zip. Each zip is named after the `name:` declared in the skill's
frontmatter, wraps its contents in a `<name>/` directory, and contains exactly
the `SKILL.md` plus its sibling `guides/` dir — nothing else (no
`concept-cards/`, `sources/`, or `extraction-metadata/`).

```sh
make go            # -> go-guidelines.zip      (knowledge/go/SKILL.md + guides/)
make rust          # -> rust-guidelines.zip
make erlang        # -> erlang-guidelines.zip
make design        # -> visual-design-system.zip
make biome         # -> biome-js-linter.zip AND biome-linter.zip (two skills)
make skills        # -> every per-domain zip
make all           # -> skills + collaboration-framework.zip
make help          # -> list every target
make clean         # -> remove build/ and all generated zips
```

The full target list — `rust`, `go`, `js`, `erlang`, `cobalt`, `design`,
`tailwindcss`, `deno`, `biome`, plus `collab-framework` — is shown by
`make help`. (`biome` ships two distinct skills, so its target builds two zips;
`lfe` has no `SKILL.md` yet, so it has no target.)

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
**craft and practice** — how we actually do the work. Five more are
operational documents that put the methodology into motion in a session —
covering both **in-repo work** (ledger discipline, asset organisation, code
audit, test coverage, subagent delegation) and **outward-facing
contribution** (style and discipline for upstream OSS tickets). Two
on-disk templates back the operational layer (the per-slice ledger format
and the contribution-ticket shape).

### The `collaboration-framework` skill

The top-level [`SKILL.md`](./SKILL.md) is the single entry point that harvests
this framework into a loadable skill named **`collaboration-framework`**. It is
*embodied and orchestrating*: it states the posture and the practical
disciplines inline — so it carries weight on its own — and routes to each of
the six source documents with explicit "load when" guidance.

Its focus is **optimising for the LLM as a collaborating peer**: the peer frame,
the structural-pull self-knowledge, calibrated honesty, and the quality-floor
disciplines (ledger, audit, coverage, delegation). It is built for the work
where a subtly wrong judgment compounds — **deep study, original research,
expert-level systems design, and production-grade programming** — rather than
quick lookups or casual chat.

It pulls in exactly nine files:

- [`docs/AI-CONSTITUTION-SUPPLEMENT.md`](./docs/AI-CONSTITUTION-SUPPLEMENT.md) — character / posture
- [`docs/AI-ENGINEERING-METHODOLOGY.md`](./docs/AI-ENGINEERING-METHODOLOGY.md) — craft / practice
- [`docs/ASSET-ORGANISATION.md`](./docs/ASSET-ORGANISATION.md) — the canonical slice/arc layout + the confirmation protocol that stops sessions inventing their own folders (broader categories deferred)
- [`templates/LEDGER-DISCIPLINE.md`](./templates/LEDGER-DISCIPLINE.md) — per-slice verification protocol
- [`docs/CODE-AUDIT.md`](./docs/CODE-AUDIT.md) — whole-repo quality audit prompt
- [`docs/CLAUDE-CODE-COVERAGE.md`](./docs/CLAUDE-CODE-COVERAGE.md) — 95%+ test-coverage prompt
- [`docs/SUBAGENT-DELEGATION-POLICY.md`](./docs/SUBAGENT-DELEGATION-POLICY.md) — thinking-vs-lookup delegation policy
- [`docs/CONTRIBUTION-STYLE.md`](./docs/CONTRIBUTION-STYLE.md) — voice + discipline for upstream OSS tickets
- [`templates/CONTRIBUTION-TICKET.md`](./templates/CONTRIBUTION-TICKET.md) — on-disk template for the four ticket variants (bug, feature, doc fix, question)

> **It does *not* pull in any of the domain-specific skills under
> [`./knowledge/`](./knowledge/).** Each domain (Rust, JavaScript/Deno, Go,
> Erlang/OTP, Visual Design, Tailwind CSS, Biome, Deno lint, Cobalt, …) has its
> own `SKILL.md` and must be **loaded separately, as needed**, alongside the
> framework. The framework is the *how we work* layer; the `knowledge/` skills
> are the *what's correct in this domain* layer. They compose; neither subsumes
> the other.

Run `make collab-framework` to package the skill — `SKILL.md` plus exactly
those nine files, in their `docs/` and `templates/` layout so the relative
links resolve — into a distributable `collaboration-framework.zip` with
nothing else in it.

The operational documents below are the tactical layer the skill
orchestrates — five for in-repo work, plus a paired style guide and template
for outward-facing contribution work.

| File | Register | What it covers | Codex ready? |
|------|----------|----------------|--------------|
| [`docs/AI-CONSTITUTION-SUPPLEMENT.md`](./docs/AI-CONSTITUTION-SUPPLEMENT.md) | Character / posture | An augmentation to Claude's Constitution. Preamble + collaborative rights and rubric, the foundational insight on interdependence as structure, and nine augmentations covering intellectual boldness, peer frame, generative contribution, honesty of engagement, harm avoidance as active beneficence, mutual intellectual humility, authentic engagement with experience, ethics as frontier of discovery, and failure recovery as collaborative practice. | ✅ |
| [`docs/AI-ENGINEERING-METHODOLOGY.md`](./docs/AI-ENGINEERING-METHODOLOGY.md) | Craft / practice | Companion to the Supplement. Names the three pillars (knowledge substrate, collaborative posture, process rigour) and elaborates each: the project/arc/slice vocabulary, the 9-point SDLC, ledger discipline, CAP-style independent audits, anti-degradation practices, the subagent leverage/hazard distinction, and one worked applied position (the LFE OSS question). | ✅ |
| [`docs/ASSET-ORGANISATION.md`](./docs/ASSET-ORGANISATION.md) | Operational discipline | Carries the canonical slice/arc layout (verbatim from the methodology) and the **confirmation protocol** the executing context follows before creating directories: quote the default, name the substitutions, give the operator three explicit choices (proceed / adjust / override), record the choice in the project's `CLAUDE.md`. *Scope note:* project-wide defaults for other asset categories (project-scoped prompts, upstream contribution drafts, coverage reports, scratch) are **deferred** pending the in-flight epic- and project-organisation work. | ✅ |
| [`docs/CODE-AUDIT.md`](./docs/CODE-AUDIT.md) | Working-practice prompt | A recurring whole-repo quality audit prompt. Detects every language in use that has a matching skill under `knowledge/`, runs a full code-quality audit per language, and produces one report per language plus a top-level index. Designed for periodic use to catch drift, missing tests, stale docs, and anti-pattern accumulation. | ✅ |
| [`docs/CLAUDE-CODE-COVERAGE.md`](./docs/CLAUDE-CODE-COVERAGE.md) | Working-practice prompt | A comprehensive prompt that drives Claude Code to **95%+ test coverage** without stopping short — includes rules for treating warnings as bugs, fixing root causes rather than symptoms, and iterating until the threshold is actually met. | ✅ |
| [`docs/SUBAGENT-DELEGATION-POLICY.md`](./docs/SUBAGENT-DELEGATION-POLICY.md) | Working-practice prompt | A shareable note for Claude Code / Cowork / Claude Desktop that draws a clean line between **thinking work** (do in the main context) and **lookup work** (fine to delegate). Explains the failure modes of delegating analytical work to subagents and gives install instructions per tool. | ✅ |
| [`docs/CONTRIBUTION-STYLE.md`](./docs/CONTRIBUTION-STYLE.md) | Voice / discipline | Voice and discipline guide for **upstream contribution tickets** — bugs, features, doc fixes, and unconfirmed questions against open source projects you do not maintain. Names the voice (friendly, specific, calibrated, respectful of maintainer ownership) and the three habits that keep it calibrated (mark confidence explicitly, disclose your own bias, pre-empt obvious red herrings). Pairs with the ticket template below. | ✅ |
| [`templates/CONTRIBUTION-TICKET.md`](./templates/CONTRIBUTION-TICKET.md) | Authoring template | The on-disk template for an upstream contribution ticket: paste-ready blockquote header, four ticket shapes (confirmed bug, additive feature, doc fix, unconfirmed question) sharing one spine (open warmly → state the situation specifically → make the next move cheap → close without pressure), and the filing workflow that keeps the on-disk file authoritative and the tracker the public conversation. | ✅ |

The Supplement and Methodology are versioned, living documents — read them
together. The five operational documents (asset organisation, code audit,
coverage, subagent delegation, contribution style) and the two templates
(ledger, contribution ticket) are designed to be self-contained; drop them
into a project's `CLAUDE.md` under a named section, or into
`~/.claude/CLAUDE.md` as a personal default.

## Knowledge-base methodology

The `docs/design/` directory holds the big-picture planning docs and research that seeds the various efforts in this repository.

The `docs/dev/` directory holds the low-level feature development work, and e.g. captures the Phase 0 methodology used to build each
knowledge base: domain taxonomy, tier definitions, competency questions,
notation conventions, source prioritisation, the Rosetta Stone cross-domain
framework, layer architecture for guide generation, extraction-specific
instructions, and validation criteria. It is the closest thing this repo has
to a field manual for adding a new domain, and it is the knowledge-substrate
pillar of the broader methodology applied to a specific scope of work.

## Templates

Three authoring / verification helpers live in [`./templates/`](./templates/):

| File | What it does | Codex ready? |
|------|--------------|--------------|
| [`GUIDE.md`](./templates/GUIDE.md) | Starter skeleton for a new knowledge-base guide — pattern format, strength indicators, cross-references. Use this when adding a new chapter to an existing skill or bootstrapping a new domain. | ✅ |
| [`LEDGER-DISCIPLINE.md`](./templates/LEDGER-DISCIPLINE.md) | A per-slice verification protocol for the implementer / reviewer pair (CC / CDC). Adapted from defect-register and corrective-action traditions in nuclear power, aviation, surgery (WHO Surgical Safety Checklist), clinical trials, HACCP, financial audit, and spaceflight. Every acceptance criterion becomes a grep-verifiable ledger row; nothing advances until the ledger is fully closed with evidence. Referenced throughout [`docs/AI-ENGINEERING-METHODOLOGY.md`](./docs/AI-ENGINEERING-METHODOLOGY.md). | ✅ |
| [`CONTRIBUTION-TICKET.md`](./templates/CONTRIBUTION-TICKET.md) | The on-disk authoring template for an upstream contribution ticket — a bug, feature, doc fix, or unconfirmed question against a project you don't maintain. Carries the paste-ready blockquote header (title suggestion, label hints, calibrated DRAFT marker for unconfirmed tickets), the four ticket shapes that share one spine, and the filing workflow. Pairs with [`docs/CONTRIBUTION-STYLE.md`](./docs/CONTRIBUTION-STYLE.md) for the voice and disciplines. | ✅ |

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
