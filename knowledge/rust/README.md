# Rust AI Guidelines

> A comprehensive, AI-optimized reference for writing idiomatic Rust code.

This is the Rust domain of the [billosys/ai-engineering](../../README.md)
knowledge base — the one that started it all. It has since grown into a full
reference of **~665 patterns across 17 chapters**, covering everything from
core idioms to unsafe-FFI soundness, async runtimes, macros, editions,
observability, CLI authoring, and full Cargo mastery.

## Overview

This directory contains a curated collection of Rust best practices, idioms,
patterns, and anti-patterns specifically structured for AI assistants (Claude,
GPT, Copilot, etc.) to reference when generating, refactoring, or reviewing
Rust code.

**Key features:**

- **~665 patterns** across 17 focused chapters
- **Strength indicators** (MUST, SHOULD, CONSIDER, AVOID) for clear prioritization
- **Paired ✅ GOOD / ❌ BAD code examples** for every pattern
- **70-entry anti-patterns chapter** — critical for preventing common AI-generated mistakes
- **Modular structure** — load only what you need to conserve context
- **Cross-referenced** — every pattern links to related guidance by ID
- **21 upstream sources** reconciled — Rust Reference, Rustonomicon, API
  Guidelines, Performance Book, Async Book, Rustdoc, Edition Guide, Cargo
  Book, tokio tutorial, Pragmatic Rust, Rust Design Patterns, clap, and more
- **Dedicated CLI and Cargo tracks** — a full chapter each for command-line
  application design and Cargo mastery
- **Dedicated Editions and Observability chapters** — for edition migration
  and production instrumentation

## Quick Start

### For Claude Code / Cowork users

Point your skill loader or `CLAUDE.md` at the SKILL definition at the root of
this directory:

```text
knowledge/rust/SKILL.md
```

Or reference the guides directly from your project instructions:

```markdown
When writing Rust code, follow the guidelines in
`.../knowledge/rust/guides/`. Always check `11-anti-patterns.md` before
writing new code.
```

### For other AI tools

Copy the relevant markdown files into your context or system prompt. Start
with:

1. `guides/11-anti-patterns.md` (what NOT to do)
2. `guides/01-core-idioms.md` (essential patterns)
3. Topic-specific chapters as needed

## Directory Structure

```text
knowledge/rust/
├── README.md                         # This file
├── SKILL.md                          # Claude Code / Cowork skill definition
├── guides/                           # The guidelines (normative artefact)
│   ├── README.md                     # Full document index
│   ├── 01-core-idioms.md             # 34 patterns — essential Rust idioms
│   ├── 02-api-design.md              # 50 patterns — public API design
│   ├── 03-error-handling.md          # 33 patterns — Result, ?, thiserror, anyhow
│   ├── 04-ownership-borrowing.md     # 25 patterns — lifetimes, borrows, RAII/OBRM
│   ├── 05-type-design.md             # 27 patterns — structs, enums, newtypes, Pin
│   ├── 06-traits.md                  # 26 patterns — trait design, object-safety, HRTBs
│   ├── 07-concurrency-async.md       # 50 patterns — threads, channels, async, tokio, Pin
│   ├── 08-performance.md             # 31 patterns — build config, allocs, profiling
│   ├── 09-unsafe-ffi.md              # 32 patterns — unsafe discipline, FFI, inline asm
│   ├── 10-macros.md                  # 29 patterns — macro_rules!, proc macros, trybuild
│   ├── 11-anti-patterns.md           # 70 patterns — what NOT to do (critical!)
│   ├── 12-project-structure.md       # 30 patterns — crates, workspaces, MSRV
│   ├── 13-documentation.md           # 33 patterns — rustdoc, doctests, intra-doc
│   ├── 14-cli-tools/                 # 57 patterns — 9 sub-guides for CLI development
│   ├── 15-cargo/                     # 96 patterns — 8 sub-guides for Cargo mastery
│   ├── 16-editions.md                # 24 patterns — editions 2015/2018/2021/2024, migration
│   └── 17-observability.md           # 18 patterns — tracing, metrics, panic hooks
├── concept-cards/                    # 384 single-pattern cards (source-of-truth extracts)
│   └── AUDIENCE.md                   # Notes on specialist card sets
├── extraction-metadata/              # Source mapping, extraction logs, style analysis
├── sources/                          # 21 upstream guides in markdown form (ground truth)
└── workbench/                        # Provenance, review reports, regeneration plans
```

See [`guides/README.md`](./guides/README.md) for the full, per-pattern
document index with pattern ID ranges.

## Document Priority

| Document | Description | Priority |
|----------|-------------|----------|
| [01-core-idioms](guides/01-core-idioms.md) | Essential patterns for everyday Rust | Critical |
| [02-api-design](guides/02-api-design.md) | Designing public APIs | Critical |
| [03-error-handling](guides/03-error-handling.md) | Result, Option, thiserror, anyhow | Critical |
| [04-ownership-borrowing](guides/04-ownership-borrowing.md) | Lifetimes, borrows, RAII/OBRM | Critical |
| [11-anti-patterns](guides/11-anti-patterns.md) | **What NOT to do** (70 traps) | Critical |
| [05-type-design](guides/05-type-design.md) | Structs, enums, newtypes, generics, `Pin` | Important |
| [06-traits](guides/06-traits.md) | Trait design, object-safety, HRTBs | Important |
| [07-concurrency-async](guides/07-concurrency-async.md) | Threads, `async`, `tokio`, cancellation | Important |
| [08-performance](guides/08-performance.md) | Build config, allocs, profiling | Important |
| [13-documentation](guides/13-documentation.md) | Doc comments, doctests, intra-doc links | Important |
| [17-observability](guides/17-observability.md) | `tracing`, metrics, panic hooks | Important |
| [09-unsafe-ffi](guides/09-unsafe-ffi.md) | `unsafe` soundness, FFI, layout | Specialized |
| [10-macros](guides/10-macros.md) | `macro_rules!` and proc macros | Specialized |
| [14-cli-tools](guides/14-cli-tools/) | Building command-line applications | Specialized |
| [15-cargo](guides/15-cargo/) | Cargo mastery: builds, plugins, publishing | Specialized |
| [16-editions](guides/16-editions.md) | Edition mechanics and migration | Specialized |
| [12-project-structure](guides/12-project-structure.md) | Crate and module organization | Reference |

## Usage Patterns

### For new code

```text
Load: 11-anti-patterns.md → 01-core-idioms.md → topic-specific chapters
```

### For refactoring

```text
Load: 11-anti-patterns.md → scan for violations → apply fixes from relevant chapters
```

### For code review

```text
Load: 11-anti-patterns.md → check each pattern → report violations with IDs
```

### For API design

```text
Load: 02-api-design.md → 05-type-design.md → 06-traits.md → 13-documentation.md
```

### For async services

```text
Load: 07-concurrency-async.md → 03-error-handling.md → 17-observability.md
```

### For unsafe work

```text
Load: 09-unsafe-ffi.md → 04-ownership-borrowing.md → 11-anti-patterns.md (AP-60..AP-70)
```

### For CLI applications

```text
Load: 14-cli-tools/ → 03-error-handling.md → 15-cargo/04-cargo-publishing.md → 13-documentation.md
```

### For edition migration

```text
Load: 16-editions.md → run `cargo fix --edition` → review diff → bump edition in Cargo.toml
```

## Strength Indicators

Every pattern includes a strength indicator:

| Indicator | Meaning | Action |
|-----------|---------|--------|
| **MUST** | Required for correctness, safety, or soundness | Always follow |
| **SHOULD** | Strong recommendation | Follow unless specific reason not to |
| **CONSIDER** | Good practice, context-dependent | Evaluate for your situation |
| **AVOID** | Anti-pattern | Do not use |

## Contributing

Contributions are welcome. Please:

1. Follow the existing pattern format (see any existing guide chapter or
   `extraction-metadata/GUIDE_ANALYSIS.md`)
2. Include paired ✅ GOOD / ❌ BAD code examples where applicable
3. Add appropriate strength indicators
4. Cross-reference related patterns using `See also: PREFIX-NN`
5. Update pattern counts in `guides/README.md` and the top-level README

## Sources and Acknowledgments

This reference synthesizes and builds upon the excellent work of many in the
Rust community. The 2026-04 regeneration reconciled 21 upstream sources and
384 concept cards into the current 17-chapter structure.

### Primary upstream sources

| Source | Description | License |
|--------|-------------|---------|
| [The Rust Reference](https://doc.rust-lang.org/reference/) | The language reference | MIT/Apache-2.0 |
| [The Rustonomicon](https://doc.rust-lang.org/nomicon/) | `unsafe` Rust — the definitive guide | MIT/Apache-2.0 |
| [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/) | Official API design guidelines | MIT/Apache-2.0 |
| [The Rust Performance Book](https://nnethercote.github.io/perf-book/) | Performance optimization techniques | CC0 / MPL-2.0 |
| [Asynchronous Programming in Rust](https://rust-lang.github.io/async-book/) | The official async book | MIT/Apache-2.0 |
| [Async Reference](https://rust-lang.github.io/async-fundamentals-initiative/) | Async fundamentals / `Pin` / `Future` | MIT/Apache-2.0 |
| [Tokio Tutorial](https://tokio.rs/tokio/tutorial) | The reference async runtime | MIT |
| [The Rustdoc Book](https://doc.rust-lang.org/rustdoc/) | Rustdoc features and doctests | MIT/Apache-2.0 |
| [The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/) | Editions 2015 / 2018 / 2021 / 2024 | MIT/Apache-2.0 |
| [The Cargo Book](https://doc.rust-lang.org/cargo/) | Cargo reference, guide, getting-started | MIT/Apache-2.0 |
| [Rust Design Patterns](https://rust-unofficial.github.io/patterns/) | Community-maintained pattern catalog | MPL-2.0 |
| [Pragmatic Rust](https://github.com/ralfbiedert/pragmatic-rust-guidelines) | Library/app/AI-design guidelines | MIT/Apache-2.0 |
| [The Rust Programming Language](https://doc.rust-lang.org/book/) | "The Book" | MIT/Apache-2.0 |
| [The Little Book of Rust Macros](https://veykril.github.io/tlborm/) | Comprehensive macro guide | CC BY-SA 4.0 |
| [Clippy Documentation](https://doc.rust-lang.org/clippy/) | Rust linter and lint catalog | MIT/Apache-2.0 |
| [The Rust Style Guide](https://doc.rust-lang.org/nightly/style-guide/) | Official formatting guide | MIT/Apache-2.0 |
| [Command Line Applications in Rust](https://rust-cli.github.io/book/) | CLI development guide | MIT/Apache-2.0 |
| [Clap Documentation](https://docs.rs/clap) | The reference argument parser | MIT/Apache-2.0 |
| [The Compiler Dev Guide](https://rustc-dev-guide.rust-lang.org/) | rustc contributor guide (specialist; see `concept-cards/AUDIENCE.md`) | MIT/Apache-2.0 |

### Additional references

- [Effective Rust](https://www.lurklurk.org/effective-rust/) by David Drysdale
- [Rust for Rustaceans](https://rust-for-rustaceans.com/) by Jon Gjengset
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- Production Rust codebases and the crates.io ecosystem

### Tools used in creation

This reference was created through a collaboration between human curation and
AI synthesis:

- **Claude** (Anthropic) — Document synthesis, pattern extraction, reconciliation
- **Claude Code / Cowork** — Source processing, parallel subagent orchestration

## History

This directory started life as a standalone repository (`oxur/ai-rust`) — the
first experiment in compiling language best practices into a form that AI
coding assistants could actually consume. It grew, the approach worked, and
the methodology was generalised to cover other languages and domains
(JavaScript/Deno, Go, visual design, Tailwind, Biome, Cobalt, …), at which
point the repository was folded into [`billosys/ai-engineering`](../../README.md)
as one knowledge base among many.

| Version | Date | Notes |
|---------|------|-------|
| 1.0.0 | 2024-12-31 | Initial release (as `oxur/ai-rust`) |
| 2.0.0 | 2026-01-09 | Expanded to 561 patterns; CLI and Cargo tracks added |
| 2.1.0 | 2026-04 | Absorbed into `billosys/ai-engineering` as `knowledge/rust/` |
| 2.2.0 | 2026-04-22 | Full regeneration from 21 sources and 384 concept cards; added 16-editions, 17-observability, expanded 07-concurrency-async (~+150%), 09-unsafe-ffi (~+45%), 11-anti-patterns (consolidated to 70), 13-documentation (+rustdoc); now ~665 patterns across 17 chapters |

## License

This project is licensed under the MIT License — see the [LICENSE](../../LICENSE)
at the repository root for details.

The content synthesizes information from multiple sources with various licenses
(see Sources above). Original pattern descriptions and code examples in this
repository are MIT licensed. When in doubt, refer to the original sources for
authoritative guidance.

## Related Projects

- [rust-clippy](https://github.com/rust-lang/rust-clippy) — The official Rust linter
- [rustfmt](https://github.com/rust-lang/rustfmt) — The official Rust formatter
- [cargo-deny](https://github.com/EmbarkStudios/cargo-deny) — Cargo plugin for linting dependencies
- [cargo-semver-checks](https://github.com/obi1kenobi/cargo-semver-checks) — Automated SemVer checks
- [cargo-msrv](https://github.com/foresterre/cargo-msrv) — MSRV discovery and verification
- [miri](https://github.com/rust-lang/miri) — Interpreter for `unsafe` Rust; essential for soundness CI
