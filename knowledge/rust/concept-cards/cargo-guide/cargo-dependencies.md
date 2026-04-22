---
# === CORE IDENTIFICATION ===
concept: Cargo Dependencies
slug: cargo-dependencies

# === CLASSIFICATION ===
category: package-management
subcategory: dependency-management
tier: foundational

# === PROVENANCE ===
source: "Cargo Guide"
source_slug: cargo-guide
authors: "The Cargo Team"
chapter: "04-dependencies"
chapter_number: 4
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "adding dependencies"
  - "Cargo.toml dependencies"
  - "crates.io dependencies"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - creating-a-cargo-project
extends: []
related:
  - cargo-toml-vs-cargo-lock
  - cargo-publishing
  - crate
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add a dependency to my Cargo project?"
  - "What is crates.io and how does Cargo use it?"
  - "What does a dependency entry in Cargo.toml look like?"
  - "How does Cargo handle transitive dependencies?"
  - "What happens when I run cargo build after adding a dependency?"
  - "How do I update my dependencies to newer versions?"
  - "How do I use a dependency in my Rust code after adding it?"
---

# Quick Definition

Dependencies in Cargo are declared in the `[dependencies]` section of `Cargo.toml` using the crate name and a SemVer version requirement. Cargo fetches them from crates.io (the default registry), resolves transitive dependencies, and records exact versions in `Cargo.lock`. Running `cargo update` selectively or globally refreshes dependency versions.

# Core Definition

The source explains that "crates.io is the Rust community's central package registry that serves as a location to discover and download packages" and that "`cargo` is configured to use it by default to find requested packages" (Ch. 4). Dependencies are added by listing them in the `[dependencies]` section of `Cargo.toml` with a crate name and version string: "The version string is a SemVer version requirement."

When `cargo build` is run after adding a dependency, Cargo performs multiple steps: it updates the crates.io index, downloads the specified crate and all its transitive dependencies, compiles everything, and updates `Cargo.lock`. As the source states: "`Cargo.lock` contains the exact information about which revision was used for all of these dependencies." Once locked, builds use the same revisions "until you choose to run `cargo update`."

# Prerequisites

- **Creating a Cargo Project** -- you need an existing Cargo project with a `Cargo.toml` before adding dependencies

# Key Properties

1. **crates.io as default registry**: Cargo looks up dependencies on crates.io by default
2. **[dependencies] section**: Dependencies are listed in `Cargo.toml` with name and SemVer version string
3. **Transitive dependency resolution**: Cargo automatically fetches and builds all transitive dependencies
4. **Cargo.lock pinning**: Exact dependency revisions are recorded; rebuilds use the same versions until explicitly updated
5. **cargo update**: Updates all dependencies or a specific one to the latest compatible version
6. **Use in code**: After adding a dependency, import it with `use` statements in your Rust source files
7. **Multiple dependencies**: All dependencies go under a single `[dependencies]` section, not separate sections per crate

# Construction / Recognition

## Adding a Single Dependency:
```toml
[dependencies]
time = "0.1.12"
```

## Adding Multiple Dependencies:
```toml
[package]
name = "hello_world"
version = "0.1.0"
edition = "2024"

[dependencies]
time = "0.1.12"
regex = "0.1.41"
```

## Building After Adding Dependencies:
```console
$ cargo build
      Updating crates.io index
   Downloading memchr v0.1.5
   Downloading libc v0.1.10
   Downloading regex-syntax v0.2.1
   Downloading aho-corasick v0.3.0
   Downloading regex v0.1.41
     Compiling memchr v0.1.5
     Compiling libc v0.1.10
     Compiling regex-syntax v0.2.1
     Compiling aho-corasick v0.3.0
     Compiling regex v0.1.41
     Compiling hello_world v0.1.0 (file:///path/to/package/hello_world)
```

## Updating Dependencies:
```console
$ cargo update         # updates all dependencies
$ cargo update regex   # updates just "regex"
```

# Context & Application

This card covers the guide-level workflow for adding and managing dependencies. It complements the cargo-getting-started cards by providing the narrative context: the role of crates.io as the central registry, the practical steps for adding dependencies to `Cargo.toml`, and the behavior of Cargo when it resolves, downloads, and locks dependency versions. The guide emphasizes the practical workflow -- add to the TOML file, rebuild, and use in code -- along with the lockfile behavior that ensures reproducible builds.

# Examples

**Example 1** (Ch. 4): Adding a dependency on the `time` crate:
```toml
[dependencies]
time = "0.1.12"
```
The source notes: "The version string is a SemVer version requirement."

**Example 2** (Ch. 4): Using a dependency in source code:
```rust
use regex::Regex;

fn main() {
    let re = Regex::new(r"^\d{4}-\d{2}-\d{2}$").unwrap();
    println!("Did our date match? {}", re.is_match("2014-01-01"));
}
```

**Example 3** (Ch. 4): Running the program with dependencies:
```console
$ cargo run
   Running `target/hello_world`
Did our date match? true
```

**Example 4** (Ch. 4): Lockfile pinning behavior:
> "Now, if `regex` gets updated, you will still build with the same revision until you choose to run `cargo update`."

# Relationships

## Builds Upon
- **Creating a Cargo Project** -- dependencies are added to an existing project's `Cargo.toml`

## Enables
- **cargo-toml-vs-cargo-lock** -- understanding the dependency lockfile in more depth
- **cargo-publishing** -- published crates become available as dependencies for others

## Related
- **crate** -- dependencies are crates fetched from a registry
- **cargo-build-performance** -- dependency count and features affect build times

## Contrasts With
- None within this source

# Common Errors

- **Error**: Adding a separate `[dependencies]` header for each crate.
  **Correction**: List all dependencies under a single `[dependencies]` section. The source shows `time` and `regex` together under one `[dependencies]` block.

- **Error**: Expecting dependencies to update automatically on rebuild.
  **Correction**: Cargo uses `Cargo.lock` to pin versions. You must explicitly run `cargo update` to get newer versions.

- **Error**: Forgetting to rebuild after adding a dependency to `Cargo.toml`.
  **Correction**: Run `cargo build` after modifying `Cargo.toml` to download and compile new dependencies.

# Common Confusions

- **Confusion**: Thinking `cargo update` upgrades to any new major version.
  **Clarification**: `cargo update` respects the SemVer version requirement specified in `Cargo.toml`. It updates to the latest compatible version within that range.

- **Confusion**: Thinking you must manually download crate source code.
  **Clarification**: Cargo handles all downloading, extraction, and compilation of dependencies automatically when you run `cargo build`.

- **Confusion**: Wondering where transitive dependencies come from.
  **Clarification**: The build output shows Cargo downloading dependencies-of-dependencies (e.g., `memchr`, `libc`, `regex-syntax`, `aho-corasick` for `regex`). Cargo resolves the entire dependency graph automatically.

# Source Reference

Chapter 4: Dependencies. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 4 -- "crates.io is the Rust community's central package registry"
- Confidence rationale: HIGH -- the source provides complete examples of Cargo.toml, build output, and code usage
- Uncertainties: Advanced dependency specification (git sources, path dependencies, features) is referenced but not detailed in this chapter
- Cross-reference status: crate references cargo-getting-started cards; other slugs are within this extraction set
