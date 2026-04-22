# Rust Best Practices Guidelines

> Comprehensive collection of Rust idioms, patterns, and best practices for writing idiomatic, safe, and performant code.

**Last Updated**: 2026-04-22
**Total Patterns**: ~665 across 17 chapters (fifteen single-file, two multi-file)

---

## Document Index

This collection is organized into 17 focused chapters covering all aspects of Rust development:

| Document | Pattern Count | Pattern ID Range | Description |
|----------|--------------|------------------|-------------|
| [01. Core Idioms](./01-core-idioms.md) | 34 | ID-01 to ID-34 | Fundamental Rust patterns, formatting, naming |
| [02. API Design](./02-api-design.md) | 50 | API-01 to API-50 | Designing ergonomic and idiomatic public APIs |
| [03. Error Handling](./03-error-handling.md) | 33 | EH-01 to EH-33 | `Result`, `?`, `thiserror`, `anyhow`, panics vs errors |
| [04. Ownership & Borrowing](./04-ownership-borrowing.md) | 25 | OB-01 to OB-25 | Lifetimes, borrows, RAII/OBRM, drop check, variance |
| [05. Type Design](./05-type-design.md) | 27 | TD-01 to TD-27 | Structs, enums, newtypes, builders, `Pin`, sealed traits |
| [06. Traits](./06-traits.md) | 26 | TR-01 to TR-26 | Trait design, object-safety, auto traits, HRTBs, `dyn` |
| [07. Concurrency & Async](./07-concurrency-async.md) | 50 | CA-01 to CA-50 | Threads, channels, `async`/`await`, `Pin`, `tokio` |
| [08. Performance](./08-performance.md) | 31 | PF-01 to PF-31 | Build config, allocations, hashing, profiling |
| [09. Unsafe & FFI](./09-unsafe-ffi.md) | 32 | US-01 to US-32 | `unsafe` discipline, soundness, `repr(C)`, FFI, asm |
| [10. Macros](./10-macros.md) | 29 | MC-01 to MC-29 | `macro_rules!`, proc macros, `trybuild` |
| [11. Anti-patterns](./11-anti-patterns.md) | 70 | AP-01 to AP-70 | Common pitfalls and how to avoid them |
| [12. Project Structure](./12-project-structure.md) | 30 | PS-01 to PS-30 | Crates, workspaces, `bin`/`lib`/`examples`, MSRV |
| [13. Documentation](./13-documentation.md) | 33 | DC-01 to DC-33 | Doc comments, doctests, intra-doc, `#[doc(…)]` |
| [14. CLI Tools](./14-cli-tools/) | 57 | CLI-\* (9 sub-guides) | Building command-line applications |
| [15. Cargo Mastery](./15-cargo/) | 96 | CG-\* (8 sub-guides) | Package management, builds, publishing, plugins |
| [16. Editions](./16-editions.md) | 24 | ED-01 to ED-24 | Editions 2015 / 2018 / 2021 / 2024, migration |
| [17. Observability](./17-observability.md) | 18 | LO-01 to LO-18 | `tracing`, `log`, metrics, panic hooks, correlation IDs |

---

## Cargo Mastery Guide Collection

The **15-cargo/** directory contains 8 specialized guides covering all aspects of Cargo:

| Guide | Patterns | Pattern Range | Use When |
|-------|----------|---------------|----------|
| [📦 Cargo Basics](./15-cargo/01-cargo-basics.md) | 14 | CG-B-01 to CG-B-14 | Creating packages, managing dependencies, workspaces |
| [⚙️ Build System](./15-cargo/02-cargo-build-system.md) | 15 | CG-BS-01 to CG-BS-15 | Features, profiles, build scripts, optimization |
| [🔌 Cargo Plugins](./15-cargo/03-cargo-plugins.md) | 12 | CG-P-01 to CG-P-12 | Building custom cargo subcommands and tools |
| [📤 Publishing](./15-cargo/04-cargo-publishing.md) | 12 | CG-PUB-01 to CG-PUB-12 | Publishing to crates.io, SemVer, versioning |
| [⚙️ Configuration](./15-cargo/05-cargo-configuration.md) | 12 | CG-CF-01 to CG-CF-12 | `.cargo/config.toml`, environment variables |
| [🚀 Advanced](./15-cargo/06-cargo-advanced.md) | 12 | CG-A-01 to CG-A-12 | CI/CD, optimization, unstable features |
| [🔍 Lints & Formatters](./15-cargo/07-lints-and-formatters.md) | 9 | CG-L-\* / CG-F-\* | `[lints]` table, clippy/rustfmt policy, CI enforcement |
| [📚 Manifest & Workspace Advanced](./15-cargo/08-manifest-and-workspace-advanced.md) | 10 | CG-M-\* / CG-W-\* / CG-ECO-\* | Inheritance, resolver v3, `dep:` prefix, umbrella crates |

**Quick Navigation**: See [15-cargo/README.md](./15-cargo/README.md) for a comprehensive decision tree and troubleshooting guide.

---

## CLI Tools Guide Collection

The **14-cli-tools/** directory contains comprehensive guidance for building command-line applications:

| Section | Patterns | Pattern Range | Topics Covered |
|---------|----------|---------------|----------------|
| [🚀 Project Setup](./14-cli-tools/01-project-setup.md) | 4 | CLI-01 to CLI-04 | Binary structure, Cargo.toml, lib/bin separation |
| [⚙️ Argument Parsing](./14-cli-tools/02-argument-parsing.md) | 13 | CLI-05..15, 53, 54 | Clap derive, flags, subcommands, ValueEnum, ArgAction |
| [❌ Error Handling](./14-cli-tools/03-error-handling.md) | 7 | CLI-16..20, 55, 56 | Exit codes, messages, stderr, `ExitCode`, `BrokenPipe` |
| [🎨 Output & UX](./14-cli-tools/04-output-and-ux.md) | 10 | CLI-21..28, 57, 58 | Human/machine output, progress, colors, human-panic, dialoguer |
| [⚙️ Configuration](./14-cli-tools/05-configuration.md) | 5 | CLI-29 to CLI-33 | Config files, precedence, XDG directories |
| [🧪 Testing](./14-cli-tools/06-testing.md) | 5 | CLI-34 to CLI-38 | `assert_cmd`, integration tests, snapshots |
| [📦 Distribution](./14-cli-tools/07-distribution.md) | 5 | CLI-39..42, 59 | Binary size, cross-compilation, `clap_mangen` |
| [🔧 Advanced Topics](./14-cli-tools/08-advanced-topics.md) | 4 | CLI-43 to CLI-46 | Signals, completions, cross-platform, piping |
| [⚠️ Common Pitfalls](./14-cli-tools/09-common-pitfalls.md) | 4 | CLI-49 to CLI-52 | Anti-patterns to avoid |

**Quick Navigation**: See [14-cli-tools/README.md](./14-cli-tools/README.md) for complete pattern index and examples.

---

## Pattern Strength Indicators

Each pattern includes a strength indicator that guides how strictly it should be followed:

- **MUST**: Critical patterns that should always be followed (safety, correctness, or strong conventions)
- **SHOULD**: Strong recommendations for idiomatic code (best practices)
- **CONSIDER**: Useful patterns to consider based on context (trade-offs exist)
- **AVOID**: Anti-patterns that should be avoided (common mistakes)

---

## Pattern Format

Each pattern follows a consistent structure:

```markdown
## XX-NN: Pattern Name

**Strength**: MUST | SHOULD | CONSIDER | AVOID

**Summary**: One-line description of the pattern.

[Code examples demonstrating the pattern, usually paired ✅ GOOD and ❌ BAD]

**Rationale**: Why this pattern matters.

**See also**: Cross-references to related patterns (e.g. `TR-17`, `AP-22`)
```

Chapters end with a **Summary Table** of all patterns, a **Related Guidelines**
list, and an **External References** section pointing at the upstream sources.

---

## How to Use This Guide

### For New Rustaceans

Start with these foundational documents:

1. **11-anti-patterns.md** — Avoid common mistakes from day one
2. **01-core-idioms.md** — Fundamental Rust idioms
3. **04-ownership-borrowing.md** — Master Rust's ownership system
4. **03-error-handling.md** — Handle errors the Rust way
5. **15-cargo/01-cargo-basics.md** — Create and manage Rust projects

### For Intermediate Developers

Focus on these areas to level up:

1. **02-api-design.md** — Design better libraries and interfaces
2. **05-type-design.md** — Leverage the type system (newtypes, typestate, `Pin`)
3. **06-traits.md** — Master trait-based design, object-safety, HRTBs
4. **07-concurrency-async.md** — `async`/`await`, `Pin`, cancellation safety
5. **08-performance.md** — Profile first, then optimise
6. **15-cargo/02-cargo-build-system.md** — Features, profiles, build scripts

### For Advanced Practitioners

Explore specialized topics:

1. **09-unsafe-ffi.md** — `unsafe` soundness, `repr(C)`, `MaybeUninit`, Miri
2. **10-macros.md** — `macro_rules!` hygiene, proc macros, `trybuild`
3. **12-project-structure.md** — Architect large workspaces and libraries
4. **16-editions.md** — Edition-specific features and migration
5. **17-observability.md** — Production instrumentation with `tracing`
6. **15-cargo/06-cargo-advanced.md** — Build optimisation, CI/CD, unstable features

### For Library Authors

Essential guides for publishing crates:

1. **02-api-design.md** — Design ergonomic public APIs
2. **13-documentation.md** — Document your crate effectively
3. **15-cargo/04-cargo-publishing.md** — Publish to crates.io
4. **15-cargo/07-lints-and-formatters.md** — Enforce quality in CI
5. **15-cargo/08-manifest-and-workspace-advanced.md** — Manifest inheritance, `dep:` prefix

### For CLI Tool Developers

Complete guide to building command-line applications:

1. **14-cli-tools/01-project-setup.md** — Set up CLI project structure
2. **14-cli-tools/02-argument-parsing.md** — Parse arguments with `clap` derive
3. **14-cli-tools/03-error-handling.md** — Exit codes, `ExitCode`, `BrokenPipe`
4. **14-cli-tools/04-output-and-ux.md** — TTY detection, colours, prompts
5. **14-cli-tools/06-testing.md** — `assert_cmd` integration tests
6. **14-cli-tools/07-distribution.md** — Release builds, man pages, `cargo-binstall`

### For Service Authors

Patterns for long-running async servers:

1. **07-concurrency-async.md** — `tokio`, `select!`, structured concurrency
2. **03-error-handling.md** — `thiserror` for typed errors, `anyhow` for app-layer
3. **17-observability.md** — `tracing` spans, metrics, panic hooks
4. **08-performance.md** — Allocations, profiling, build config

### For All Developers

Essential reference materials:

1. **11-anti-patterns.md** — Comprehensive anti-pattern catalog (70 patterns)
2. **13-documentation.md** — Document your code effectively
3. **15-cargo/README.md** — Quick reference for cargo workflows

---

## Quick Stats

- **Total Patterns**: ~665
- **Chapters**: 17 (fifteen single-file, two multi-file collections)
- **CLI Tools Patterns**: 57 across 9 focused sections
- **Cargo Mastery Patterns**: 96 across 8 specialized guides
- **Upstream Sources Reconciled**: 21
- **Concept Cards (source extracts)**: 384
- **Code Examples**: 1,000+ `rust`, `bash`, `toml`, `console` code blocks

---

## Sources

This collection merges and consolidates patterns from multiple authoritative Rust resources:

- **The Rust Reference** — the language reference
- **The Rustonomicon** — `unsafe` Rust (drives most of chapter 09)
- **The Rust API Guidelines** — official API design conventions
- **The Rust Performance Book** — performance methodology and lore
- **The Async Book** and **Async Reference** — `Future`/`Pin`/`async fn` mechanics
- **The Tokio Tutorial** — reference async runtime idioms
- **The Rustdoc Book** — rustdoc features, doctests, intra-doc links
- **The Rust Edition Guide** — edition mechanics and per-edition behaviour
- **The Cargo Book** (Reference, Guide, Getting Started) — Cargo end-to-end
- **The Rust Design Patterns** book — community pattern catalog
- **Pragmatic Rust Guidelines** — library/application/AI-design guidelines
- **The Rust Programming Language** ("The Book") — canonical beginner + intermediate material
- **The Little Book of Rust Macros** — macro mechanics and techniques
- **Clippy Documentation** — the Rust linter and its lints
- **The Rust Style Guide** — official formatting rules
- **Command Line Applications in Rust** — CLI development book
- **Clap Documentation** — reference argument parser
- Production Rust codebases and the crates.io ecosystem

All patterns have been deduplicated, merged, and organized for maximum clarity and utility.

---

## Contributing

These guidelines represent current best practices as of 2026-04-22. The Rust ecosystem evolves rapidly:

- Patterns marked **MUST** are stable and unlikely to change
- Patterns marked **SHOULD** represent current consensus
- Patterns marked **CONSIDER** may have evolving trade-offs
- Patterns marked **AVOID** identify well-established anti-patterns

When Rust evolves (new language features, edition changes, ecosystem shifts), these patterns should be reviewed and updated accordingly.

---

## Cross-References

Patterns frequently reference each other across documents. Look for **See also** sections to explore related concepts. Common cross-cutting themes include:

- **Soundness and memory safety**: OB-\*, US-\*, AP-60..AP-70
- **Zero-cost abstractions**: TR-04, TR-25, PF-02, PF-06
- **API ergonomics**: API-\*, TD-\*, TR-\*, DC-\*
- **Compile-time guarantees**: TD-\*, TR-\*, MC-\*
- **Build optimization**: PF-01..PF-06, CG-BS-06, CG-A-01, CG-A-02
- **Publishing workflow**: CG-PUB-\*, API-\*, DC-\*, CG-L-\*
- **Project organization**: PS-\*, CG-B-10..14, CG-W-\*
- **CLI development**: CLI-\*, EH-\*, API-\*, PS-\*
- **Async and concurrency**: CA-\*, AP-18..AP-25, LO-\*
- **`unsafe` and FFI**: US-\*, OB-15..OB-25, AP-60..AP-70
- **Observability**: LO-\*, AP-22, DC-11
- **Edition migration**: ED-\*, AP-65..AP-66

---

## License

This is a compilation and synthesis of publicly available Rust best practices. Individual patterns may reference specific sources. Use freely for learning and reference.

---

*For the latest Rust language features and edition-specific guidance, always consult the official [Rust documentation](https://doc.rust-lang.org/) and chapter 16-editions.md.*
