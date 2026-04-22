# Rust AI Guidelines

> A comprehensive, AI-optimized reference for writing idiomatic Rust code.

This is the Rust domain of the [billosys/ai-engineering](../../README.md)
knowledge base — the one that started it all. It has since grown into a full
reference of **561 patterns across 15 collections**, covering everything from
core idioms to Cargo plugin authoring.

## Overview

This directory contains a curated collection of Rust best practices, idioms,
patterns, and anti-patterns specifically structured for AI assistants (Claude,
GPT, Copilot, etc.) to reference when generating, refactoring, or reviewing
Rust code.

**Key features:**

- **561 patterns** across 15 focused collections
- **Strength indicators** (MUST, SHOULD, CONSIDER, AVOID) for clear prioritization
- **Code examples** for every pattern (good and bad)
- **Anti-patterns section** — critical for preventing common AI-generated mistakes
- **Modular structure** — load only what you need to conserve context
- **Cross-referenced** — patterns link to related guidance
- **Dedicated CLI and Cargo tracks** — a full chapter each for command-line
  application design and Cargo mastery

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
3. Topic-specific guides as needed

## Directory Structure

```text
knowledge/rust/
├── README.md                         # This file
├── SKILL.md                          # Claude Code / Cowork skill definition
├── guides/                           # The guidelines
│   ├── README.md                     # Full document index (561 patterns)
│   ├── 01-core-idioms.md             # 42 patterns — essential Rust idioms
│   ├── 02-api-design.md              # 59 patterns — public API design
│   ├── 03-error-handling.md          # 32 patterns — Result, Option, error types
│   ├── 04-ownership-borrowing.md     # 19 patterns — lifetimes, borrowing
│   ├── 05-type-design.md             # 27 patterns — structs, enums, newtypes
│   ├── 06-traits.md                  # 26 patterns — trait design
│   ├── 07-concurrency-async.md       # 20 patterns — async, threading
│   ├── 08-performance.md             # 22 patterns — optimization
│   ├── 09-unsafe-ffi.md              # 22 patterns — unsafe code, FFI
│   ├── 10-macros.md                  # 20 patterns — declarative & proc macros
│   ├── 11-anti-patterns.md           # 80 patterns — what NOT to do (critical!)
│   ├── 12-project-structure.md       # 31 patterns — crate organization
│   ├── 13-documentation.md           # 35 patterns — doc comments, rustdoc
│   ├── 14-cli-tools/                 # 52 patterns — CLI application design
│   └── 15-cargo/                     # 74 patterns — 6 sub-guides for Cargo
├── extraction-metadata/              # Source mapping and extraction logs
└── sources/                          # Original PDFs/EPUBs processed for extraction
```

See [`guides/README.md`](./guides/README.md) for the full, per-pattern
document index with pattern ID ranges and priority ratings.

## Document Priority

| Document | Description | Priority |
|----------|-------------|----------|
| [01-core-idioms](guides/01-core-idioms.md) | Essential patterns for everyday Rust | Critical |
| [02-api-design](guides/02-api-design.md) | Designing public APIs | Critical |
| [03-error-handling](guides/03-error-handling.md) | Result, Option, thiserror, anyhow | Critical |
| [04-ownership-borrowing](guides/04-ownership-borrowing.md) | Lifetimes, borrow checker strategies | Critical |
| [11-anti-patterns](guides/11-anti-patterns.md) | **What NOT to do** | Critical |
| [05-type-design](guides/05-type-design.md) | Structs, enums, newtypes, generics | Important |
| [06-traits](guides/06-traits.md) | Trait design and implementation | Important |
| [07-concurrency-async](guides/07-concurrency-async.md) | Async/await, Send/Sync, threading | Important |
| [08-performance](guides/08-performance.md) | Optimization without sacrificing clarity | Important |
| [09-unsafe-ffi](guides/09-unsafe-ffi.md) | Safe wrappers around unsafe code | Specialized |
| [10-macros](guides/10-macros.md) | macro_rules! and proc macros | Specialized |
| [14-cli-tools](guides/14-cli-tools/) | Building command-line applications | Specialized |
| [15-cargo](guides/15-cargo/) | Cargo mastery: builds, plugins, publishing | Specialized |
| [12-project-structure](guides/12-project-structure.md) | Crate and module organization | Reference |
| [13-documentation](guides/13-documentation.md) | Doc comments and rustdoc | Reference |

## Usage Patterns

### For new code

```text
Load: 11-anti-patterns.md → 01-core-idioms.md → topic-specific guides
```

### For refactoring

```text
Load: 11-anti-patterns.md → scan for violations → apply fixes from relevant guides
```

### For code review

```text
Load: 11-anti-patterns.md → check each pattern → report violations with IDs
```

### For API design

```text
Load: 02-api-design.md → 05-type-design.md → 03-error-handling.md
```

### For CLI applications

```text
Load: 14-cli-tools/ → 15-cargo/04-cargo-publishing.md → 13-documentation.md
```

## Strength Indicators

Every pattern includes a strength indicator:

| Indicator | Meaning | Action |
|-----------|---------|--------|
| **MUST** | Required for correctness or safety | Always follow |
| **SHOULD** | Strong recommendation | Follow unless specific reason not to |
| **CONSIDER** | Good practice, context-dependent | Evaluate for your situation |
| **AVOID** | Anti-pattern | Do not use |

## Contributing

Contributions are welcome. Please:

1. Follow the existing pattern format
2. Include code examples (good AND bad where applicable)
3. Add appropriate strength indicators
4. Cross-reference related patterns
5. Update pattern counts in the READMEs

## Sources and Acknowledgments

This reference synthesizes and builds upon the excellent work of many in the
Rust community.

### Primary sources

| Source | Description | License |
|--------|-------------|---------|
| [cheats.rs](https://cheats.rs/) | Comprehensive Rust cheat sheet by Ralf Biedert | CC BY-SA 4.0 |
| [Rust Design Patterns](https://rust-unofficial.github.io/patterns/) | Unofficial Rust design patterns book | MPL-2.0 |
| [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/) | Official Rust API design guidelines | MIT/Apache-2.0 |
| [Clippy Documentation](https://doc.rust-lang.org/clippy/) | Rust linter documentation | MIT/Apache-2.0 |
| [The Rust Style Guide](https://doc.rust-lang.org/nightly/style-guide/) | Official Rust formatting guide | MIT/Apache-2.0 |
| [Asynchronous Programming in Rust](https://rust-lang.github.io/async-book/) | Official async Rust book | MIT/Apache-2.0 |
| [The Little Book of Rust Macros](https://veykril.github.io/tlborm/) | Comprehensive macro guide | CC BY-SA 4.0 |
| [The Cargo Book](https://doc.rust-lang.org/cargo/) | Official Cargo reference | MIT/Apache-2.0 |

### Additional references

- [The Rust Programming Language](https://doc.rust-lang.org/book/) (The Book)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [The Rustonomicon](https://doc.rust-lang.org/nomicon/) (unsafe Rust)
- [Effective Rust](https://www.lurklurk.org/effective-rust/) by David Drysdale
- [Rust for Rustaceans](https://rust-for-rustaceans.com/) by Jon Gjengset

### Tools used in creation

This reference was created through a collaboration between human curation and
AI synthesis:

- **Claude** (Anthropic) — Document synthesis, pattern extraction, and formatting
- **Claude Code / Cowork** — PDF processing and cross-referencing

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
