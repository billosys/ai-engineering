---
# === CORE IDENTIFICATION ===
concept: Cargo Manifest Reference
slug: cargo-manifest-reference

# === CLASSIFICATION ===
category: package-management
subcategory: manifest-format
tier: intermediate

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "01-manifest"
chapter_number: 1
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cargo.toml reference"
  - "manifest format"
  - "Cargo.toml specification"
  - "package manifest"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - creating-a-cargo-project
  - cargo-manifest
extends:
  - cargo-dependencies
related:
  - cargo-workspaces
  - cargo-publishing
  - cargo-project-layout
  - cargo-toml-vs-cargo-lock
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are all the sections available in a Cargo.toml manifest?"
  - "What fields are required vs optional in [package]?"
  - "How do I configure targets like [lib], [[bin]], [[test]], and [[bench]]?"
  - "How does Cargo auto-discover targets from the filesystem layout?"
  - "What is the [lints] section and how do I use it?"
  - "How do I set the exclude and include fields for publishing?"
  - "What crate types are available and how do I set them?"
  - "How does the rust-version field work and what policies should I follow?"
---

# Quick Definition

The Cargo.toml manifest file is the complete specification for a Rust package, written in TOML format. It contains the `[package]` section with metadata fields, target tables (`[lib]`, `[[bin]]`, `[[example]]`, `[[test]]`, `[[bench]]`), dependency sections, and configuration for profiles, features, lints, and workspaces.

# Core Definition

The source states: "The `Cargo.toml` file for each package is called its *manifest*. It is written in the TOML format. It contains metadata that is needed to compile the package" (Ch. 1). Every manifest consists of these top-level sections: `cargo-features` (unstable), `[package]`, target tables (`[lib]`, `[[bin]]`, `[[example]]`, `[[test]]`, `[[bench]]`), dependency tables (`[dependencies]`, `[dev-dependencies]`, `[build-dependencies]`, `[target]`), `[badges]`, `[features]`, `[lints]`, `[hints]`, `[patch]`, `[replace]`, `[profile]`, and `[workspace]`.

The `[package]` section is the primary section. "The only field required by Cargo is `name`" (Ch. 1), though publishing to a registry requires additional fields. Key fields include: `name` (alphanumeric, `-`, or `_`), `version` (SemVer with three numeric parts, optional since Rust 1.75), `edition` (defaults to 2015 if omitted; `cargo new` uses the latest stable edition, currently 2024), `rust-version` (minimum supported Rust toolchain version), `description`, `license`/`license-file` (SPDX 2.3 expressions for `license`), `publish` (restrict or prevent registry publishing), `build` (build script path, defaults to `"build.rs"`), `links` (native library name), and `exclude`/`include` (gitignore-style patterns controlling which files are packaged).

Cargo targets correspond to source files compiled into crates. The source explains: "Packages can have library, binary, example, test, and benchmark targets. The list of targets can be configured in the Cargo.toml manifest, often inferred automatically by the directory layout of the source files" (Ch. 1, Cargo Targets section). All target tables support common configuration fields: `name`, `path`, `test`, `doctest`, `bench`, `doc`, `harness`, `crate-type`, `required-features`, and `edition`. The `crate-type` field accepts values: `bin`, `lib`, `rlib`, `dylib`, `cdylib`, `staticlib`, and `proc-macro`.

The `[lints]` section (MSRV: 1.74) allows overriding lint levels from `rustc` and `clippy` with levels `forbid`, `deny`, `warn`, and `allow`, plus a `priority` field for controlling precedence among lint groups.

# Prerequisites

- **Creating a Cargo Project** -- you must have a Cargo project initialized before working with its manifest
- **Cargo Manifest** -- basic understanding of what Cargo.toml is and its role in a project

# Key Properties

1. **TOML format**: The manifest is written in TOML; Cargo warns about unrecognized keys (except under `package.metadata`)
2. **Only `name` required**: The `name` field is the sole mandatory field; registries require additional fields like `version`, `description`, and `license`
3. **SemVer versioning**: The `version` field uses Semantic Versioning with three numeric parts plus optional pre-release and metadata
4. **Edition field**: Controls which Rust edition the package compiles with; defaults to 2015 if absent, but `cargo new` uses 2024
5. **Five target types**: `[lib]` (singular), `[[bin]]`, `[[example]]`, `[[test]]`, `[[bench]]` (all array-of-tables using double brackets)
6. **Target auto-discovery**: Cargo infers targets from the filesystem layout by default; can be disabled with `autolib`, `autobins`, `autoexamples`, `autotests`, `autobenches` set to `false`
7. **A package can have only one library**: The `[lib]` target is unique; its name defaults to the package name with dashes replaced by underscores
8. **Three dependency sections**: `[dependencies]` (library deps), `[dev-dependencies]` (examples, tests, benchmarks), `[build-dependencies]` (build scripts)
9. **License as SPDX expression**: The `license` field uses SPDX 2.3 license expressions with `AND`, `OR`, and `WITH` operators
10. **Include/exclude use gitignore patterns**: Patterns support `*`, `?`, `[]`, `**/`, `/**`, and `!` negation
11. **Metadata table is freeform**: `package.metadata` is ignored by Cargo and can store configuration for external tools
12. **Lints section scoping**: Lint configuration only applies to the current package, not dependencies

# Construction / Recognition

## Creating a Complete Cargo.toml:

```toml
[package]
name = "my-package"
version = "1.0.0"
edition = "2024"
rust-version = "1.56"
description = "A short description"
license = "MIT OR Apache-2.0"
repository = "https://github.com/user/repo"
keywords = ["example", "demo"]
categories = ["development-tools"]
publish = true

[lib]
name = "my_package"
path = "src/lib.rs"
crate-type = ["lib"]

[[bin]]
name = "my-tool"
path = "src/bin/tool.rs"
required-features = ["cli"]

[dependencies]
serde = "1.0"

[dev-dependencies]
tempfile = "3.0"

[build-dependencies]
cc = "1.0"

[lints.rust]
unsafe_code = "forbid"

[lints.clippy]
enum_glob_use = "deny"
```

## Recognizing Target Configuration Fields:

Each target (`[lib]`, `[[bin]]`, `[[example]]`, `[[test]]`, `[[bench]]`) supports:
- `name` -- artifact name (required for all except `[lib]`)
- `path` -- source file location
- `test`, `bench`, `doc`, `doctest` -- boolean flags
- `harness` -- whether to use the libtest harness (default: `true`)
- `crate-type` -- only for libraries and examples
- `required-features` -- only for bins, examples, tests, benchmarks (not lib)

## Default Source File Locations:

- Library: `src/lib.rs`
- Default binary: `src/main.rs`
- Additional binaries: `src/bin/*.rs`
- Examples: `examples/*.rs`
- Integration tests: `tests/*.rs`
- Benchmarks: `benches/*.rs`

# Context & Application

This card covers the authoritative reference for the Cargo.toml manifest format. It complements the guide-level `cargo-manifest` card (from cargo-getting-started) by providing the complete field inventory, target configuration system, and advanced sections like `[lints]` and `[hints]`. The manifest reference is essential when you need to go beyond the basics -- configuring crate types for FFI (`cdylib`, `staticlib`), disabling auto-discovery for unusual project layouts, setting lint policies, or preparing a crate for publishing with complete metadata.

The `rust-version` field (MSRV: 1.56) is particularly noteworthy for library authors: it enables `cargo add` to auto-select compatible dependency versions, drives the resolver's version selection, and causes clear diagnostics when users attempt to compile on an unsupported toolchain. The source recommends choosing a Rust version support policy such as "N-2" (latest with a 2-release grace window) and documenting it.

The `[hints]` section (MSRV: 1.90) is a newer addition with no stable hints yet. Unlike profiles, hints are always safe for Cargo to ignore.

# Examples

**Example 1** (Ch. 1, The `[package]` section): Minimal manifest:
```toml
[package]
name = "hello_world"
version = "0.1.0"
```

**Example 2** (Ch. 1, The `license` field): SPDX license expressions:
```toml
license = "MIT OR Apache-2.0"
license = "LGPL-2.1-only AND MIT AND BSD-2-Clause"
license = "GPL-2.0-or-later WITH Bison-exception-2.2"
```

**Example 3** (Ch. 1, Cargo Targets): Full target configuration overview:
```toml
[lib]
name = "foo"
path = "src/lib.rs"
test = true
doctest = true
bench = true
doc = true
proc-macro = false
harness = true
crate-type = ["lib"]
required-features = []
```

**Example 4** (Ch. 1, The `[lints]` section): Configuring lint levels:
```toml
[lints.rust]
unsafe_code = "forbid"

[lints.clippy]
enum_glob_use = "deny"
```
The source explains: "The `priority` is a signed integer that controls which lints or lint groups override other lint groups: lower (particularly negative) numbers have lower priority."

**Example 5** (Ch. 1, The `exclude` and `include` fields):
```toml
[package]
exclude = ["/ci", "images/", ".*"]
```
```toml
[package]
include = ["/src", "COPYRIGHT", "/examples", "!/examples/big_example"]
```

**Example 6** (Ch. 1, Target auto-discovery): Disabling auto-discovery for an unusual layout where `src/bin/` is a module, not binaries:
```toml
[package]
autobins = false
```

# Relationships

## Builds Upon
- **Creating a Cargo Project** -- the manifest is created by `cargo new`/`cargo init`
- **Cargo Manifest** -- this card is the reference-level detail for the getting-started concept

## Enables
- **Cargo Workspaces** -- workspace configuration is a section within the manifest
- **Cargo Publishing** -- publishing requires complete manifest metadata

## Related
- **Cargo Dependencies** -- `[dependencies]` is a major manifest section, covered in its own reference chapter
- **Cargo Project Layout** -- target auto-discovery depends on filesystem layout conventions
- **Cargo.toml vs Cargo.lock** -- the manifest declares intent; the lockfile records exact resolutions

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `version = "1.0"` with only two components.
  **Correction**: SemVer requires three numeric parts: `version = "1.0.0"`.

- **Error**: Declaring multiple `[dependencies]` sections for different crates.
  **Correction**: All dependencies go under a single `[dependencies]` header. Multiple entries are listed as separate key-value pairs within that section.

- **Error**: Setting `crate-type` on a `[[bin]]` or `[[test]]` target.
  **Correction**: The `crate-type` field can only be specified for libraries (`[lib]`) and examples (`[[example]]`). Binaries, tests, and benchmarks are always the `"bin"` crate type.

- **Error**: Adding `required-features` to `[lib]`.
  **Correction**: The `required-features` field has no effect on `[lib]`; it only applies to `[[bin]]`, `[[bench]]`, `[[test]]`, and `[[example]]`.

- **Error**: Exceeding crates.io limits for `keywords` (max 5, max 20 chars each, ASCII only) or `categories` (max 5, must match slugs from crates.io/category_slugs).
  **Correction**: Check constraints before publishing; use `cargo package --list` to verify file inclusion.

# Common Confusions

- **Confusion**: Thinking `[lib]` uses double brackets like `[[lib]]`.
  **Clarification**: Since a package can have only one library, `[lib]` is a regular TOML table. The double-bracket form (`[[bin]]`, `[[example]]`, etc.) is TOML's array-of-tables syntax, used for targets where multiple are allowed.

- **Confusion**: Believing the `edition` field defaults to the latest edition if omitted.
  **Clarification**: If `edition` is absent from `Cargo.toml`, the 2015 edition is assumed for backwards compatibility. However, `cargo new` always sets it explicitly to the current latest (2024).

- **Confusion**: Thinking `include` and `exclude` can be used together.
  **Clarification**: The options are mutually exclusive; setting `include` overrides any `exclude`. Use the `!` prefix operator within `include` patterns for exclusions.

- **Confusion**: Assuming `[lints]` settings apply to dependencies.
  **Clarification**: Cargo only applies lint configuration to the current package. Dependencies are protected by `--cap-lints`.

- **Confusion**: Thinking `package.metadata` needs specific formatting.
  **Clarification**: The `package.metadata` table is completely ignored by Cargo and will not generate warnings. External tools define their own schema within it.

# Source Reference

Chapter 1: The Manifest Format (including Cargo Targets and Rust Version subsections), from the Cargo Reference. Online documentation with no page numbers. Key sections: The `[package]` section (all fields), Cargo Targets (library, binaries, examples, tests, benchmarks, configuring a target, target auto-discovery), The `[lints]` section, The `[hints]` section, The `[badges]` section, Dependency sections, The `[profile.*]` sections, and Rust Version (support expectations, setting and updating policies).

# Verification Notes

- Definition: Direct from Ch. 1 opening paragraph and section headings
- Key Properties: All derived from explicit field descriptions in the source
- Target configuration: Comprehensive table reproduced from source (Ch. 1, "Configuring a target")
- Crate types: Enumerated directly from source table
- Lint section: MSRV and field descriptions directly from source
- Rust-version: Extensive coverage synthesized from the dedicated subsection
- Confidence: HIGH -- this is the official reference documentation with explicit, unambiguous field definitions
- Cross-references: Slugs reference cards from cargo-getting-started, cargo-guide, and cargo-reference sets
