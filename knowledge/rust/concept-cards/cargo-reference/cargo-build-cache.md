---
# === CORE IDENTIFICATION ===
concept: Cargo Build Cache and Package ID Specifications
slug: cargo-build-cache

# === CLASSIFICATION ===
category: build-system
subcategory: caching-and-identification
tier: intermediate

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "09-build-cache, 10-pkgid-spec"
chapter_number: 9
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "target directory"
  - "build directory"
  - "target dir"
  - "build cache"
  - "Package ID Spec"
  - "pkgid spec"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-build-performance
  - cargo-project-layout
extends: []
related:
  - cargo-external-tools
  - cargo-registries
  - cargo-home
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Where does Cargo store build output and how is the target directory structured?"
  - "What is the difference between final and intermediate build artifacts?"
  - "How does the target directory layout change when using --target?"
  - "What are dep-info files and how do they work?"
  - "How can I share a build cache across workspaces?"
  - "What is a Package ID Specification and how do I use it?"
  - "How do I refer to a specific package version in a dependency graph?"
  - "What is the grammar for Package ID specs?"
---

# Quick Definition

Cargo stores build output in a "target" directory (final artifacts like binaries and docs) and a "build" directory (intermediate artifacts like deps and incremental compilation data). The target directory is structured by profile (`debug/`, `release/`) and optionally by target triple. Package ID Specifications provide a grammar for uniquely referring to any package in a dependency graph, from abbreviated forms like `regex@1.4.3` to fully qualified URLs like `registry+https://github.com/rust-lang/crates.io-index#regex@1.4.3`.

# Core Definition

The source states: "Cargo stores the output of a build into the 'target' and 'build' directories. By default, both directories point to a directory named `target` in the root of your workspace." (Ch. 9). Artifacts are split into two categories: final build artifacts (binaries, docs, timing reports) stored in the target-dir, and intermediate build artifacts (internal to Cargo and rustc) stored in the build-dir.

For Package ID Specifications, the source states: "A specification is a string which is used to uniquely refer to one package within a graph of packages." (Ch. 10). Specs can be fully qualified (e.g., `registry+https://github.com/rust-lang/crates.io-index#regex@1.4.3`) or abbreviated (e.g., `regex`). The abbreviated form works as long as it uniquely identifies a single package in the dependency graph; if ambiguous, additional qualifiers like version (`regex@1.4.3`) can disambiguate.

# Prerequisites

- **Cargo Build Performance** -- understanding build optimization depends on knowing cache structure
- **Cargo Project Layout** -- the target directory sits within the project layout

# Key Properties

1. **Two directory categories**: Target-dir for final artifacts, build-dir for intermediate artifacts
2. **Profile-based layout**: `target/debug/` for dev profile, `target/release/` for release, `target/foo/` for custom profiles
3. **Historical naming**: `dev` and `test` profiles store in `debug/`, `release` and `bench` profiles store in `release/`
4. **Cross-compilation layout**: Using `--target` adds a `<triple>/` subdirectory (e.g., `target/thumbv7em-none-eabihf/debug/`)
5. **RUSTFLAGS sharing**: Without `--target`, build scripts and proc macros share `RUSTFLAGS` with the main build; with `--target` they are built separately
6. **Dep-info files**: `.d` files alongside compiled artifacts in Makefile-like syntax listing file dependencies
7. **Shared cache via sccache**: Third-party tool for sharing built dependencies across workspaces
8. **Package ID abbreviated form**: Just the package name (`regex`) when unambiguous
9. **Package ID version-qualified form**: Name with version (`regex@1.4.3`) to disambiguate
10. **Package ID fully qualified form**: Kind, URL, and fragment (`registry+https://...#regex@1.4.3`)
11. **Package ID grammar**: Supports `registry`, `git`, and `path` kinds with `http`, `git`, `file`, and `ssh` protocols

# Construction / Recognition

## Target Directory Structure (no --target):
```
target/
├── debug/              # dev and test profile output
│   ├── examples/       # example targets
│   ├── deps/           # dependencies (intermediate, in build-dir)
│   ├── incremental/    # rustc incremental cache (intermediate, in build-dir)
│   └── build/          # build script output (intermediate, in build-dir)
├── release/            # release and bench profile output
├── doc/                # rustdoc output (cargo doc)
└── package/            # cargo package output
```

## Target Directory with --target:
```
target/thumbv7em-none-eabihf/debug/    # cross-compiled debug
target/thumbv7em-none-eabihf/release/  # cross-compiled release
```

## Package ID Specification Grammar:
```notrust
spec := pkgname |
        [ kind "+" ] proto "://" hostname-and-path [ "?" query] [ "#" ( pkgname | semver ) ]
query = ( "branch" | "tag" | "rev" ) "=" ref
pkgname := name [ ("@" | ":" ) semver ]
semver := digits [ "." digits [ "." digits [ "-" prerelease ] [ "+" build ]]]

kind = "registry" | "git" | "path"
proto := "http" | "git" | "file" | ...
```

## Dep-info File Example:
```Makefile
# Example dep-info file found in target/debug/foo.d
/path/to/myproj/target/debug/foo: /path/to/myproj/src/lib.rs /path/to/myproj/src/main.rs
```

# Context & Application

The build cache structure is fundamental to understanding Cargo's behavior during development. The split between final and intermediate artifacts (which may be stored separately via `build.build-dir` config) enables cleaner workflows where end-user artifacts can be separated from Cargo-internal data. The `--target` flag's effect on RUSTFLAGS sharing is a subtle but important detail: without it, build scripts and proc macros share flags with the main compilation, which can cause unexpected behavior. Package ID specs are used throughout Cargo's CLI (in `cargo update`, `cargo clean`, `cargo build -p`, `cargo metadata` output) and in JSON messages, making them essential for scripting and tooling integration.

# Examples

**Example 1** (Ch. 9): Configuring the target directory location:
> "To change the location of the target-dir, you can set the `CARGO_TARGET_DIR` environment variable, the `build.target-dir` config value, or the `--target-dir` command-line flag."

**Example 2** (Ch. 9): Dep-info file usage:
> "These are intended to be used with external build systems so that they can detect if Cargo needs to be re-executed."

**Example 3** (Ch. 9): Shared cache with sccache:
> "A third party tool, sccache, can be used to share built dependencies across different workspaces."
> Setup: "set `RUSTC_WRAPPER` environment variable to `sccache` before invoking Cargo."

**Example 4** (Ch. 10): Abbreviated Package ID for crates.io:
The spec `regex@1.4` matches `regex` version `1.4.*`, while `regex@1.4.3` matches exactly version `1.4.3`.

**Example 5** (Ch. 10): Git dependency Package ID specs:
`https://github.com/rust-lang/cargo#cargo-platform@0.1.2` identifies the `cargo-platform` package at version `0.1.2` within the Cargo monorepo.

**Example 6** (Ch. 10): Local package specs:
`file:///path/to/my/project/foo#1.1.8` identifies a local package `foo` at version `1.1.8`.

# Relationships

## Builds Upon
- **Cargo Build Performance** -- cache structure directly affects build optimization strategies
- **Cargo Project Layout** -- the target directory is part of the overall project layout

## Enables
- Integration with external build systems via dep-info files
- Precise package identification in complex dependency graphs
- Cross-workspace cache sharing via sccache

## Related
- **cargo-external-tools** -- JSON messages use Package ID specs in the `package_id` field
- **cargo-registries** -- fully qualified Package ID specs include registry URLs
- **cargo-home** -- the Cargo home caches downloaded dependencies separately from the build cache

## Contrasts With
- None within this source

# Common Errors

- **Error**: Expecting `dev` profile output in a `target/dev/` directory.
  **Correction**: "For historical reasons, the `dev` and `test` profiles are stored in the `debug` directory, and the `release` and `bench` profiles are stored in the `release` directory."

- **Error**: Using `--target` and expecting build scripts to share `RUSTFLAGS` with the main build.
  **Correction**: "With the `--target` flag, build scripts and proc macros are built separately (for the host architecture), and do not share `RUSTFLAGS`."

- **Error**: Assuming an ambiguous Package ID spec will match a specific package.
  **Correction**: "Most commands generate an error if more than one package could be referred to with the same specification." Add version qualifiers to disambiguate.

# Common Confusions

- **Confusion**: Thinking the build-dir internal layout is stable and can be relied upon.
  **Clarification**: "The build-dir layout is considered internal to Cargo, and is subject to change." Only final artifacts in the target-dir have a stable layout.

- **Confusion**: Thinking the `target` directory and the `build` directory are always the same.
  **Clarification**: By default both point to the `target` directory, but the build-dir can be configured separately via `CARGO_BUILD_BUILD_DIR` or `build.build-dir`.

- **Confusion**: Thinking Package ID specs output by Cargo are always abbreviated.
  **Clarification**: "Package ID specifications output by cargo, for example in cargo metadata output, are fully qualified." Abbreviated forms are for user input.

- **Confusion**: Thinking dep-info file paths are always relative.
  **Clarification**: "The paths in the file are absolute by default." Use the `build.dep-info-basedir` config option for relative paths.

# Source Reference

Chapter 9: Build Cache -- sections "Dep-info files" and "Shared cache." Chapter 10: Package ID Specifications -- sections "Specification grammar," "Example specifications," and "Brevity of specifications." No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 9 -- "Cargo stores the output of a build into the 'target' and 'build' directories" and Ch. 10 -- "A specification is a string which is used to uniquely refer to one package within a graph of packages"
- Confidence rationale: HIGH -- both chapters provide clear structural documentation with concrete examples
- Uncertainties: The build-dir layout is explicitly marked as internal and subject to change
- Cross-reference status: All slugs reference cards within this extraction set or related extraction sets
