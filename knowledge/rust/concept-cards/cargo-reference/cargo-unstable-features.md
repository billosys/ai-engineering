---
# === CORE IDENTIFICATION ===
concept: Cargo Unstable Features
slug: cargo-unstable-features

# === CLASSIFICATION ===
category: tooling
subcategory: nightly-features
tier: advanced

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "17-unstable"
chapter_number: 17
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cargo nightly features"
  - "unstable Cargo features"
  - "-Z flags for Cargo"
  - "experimental Cargo features"
  - "Cargo feature flags"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - creating-a-cargo-project
  - cargo-dependencies
extends: []
related:
  - cargo-semver-compatibility
  - cargo-lints-reference
  - cargo-build-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I enable unstable Cargo features?"
  - "What are the three ways to enable unstable features in Cargo?"
  - "What is cargo build-std and how do I use it?"
  - "How do I use single-file Rust scripts with Cargo?"
  - "What is the public-dependency feature?"
  - "How do artifact dependencies work in Cargo?"
  - "What is the SBOM generation feature?"
  - "How do I use path bases for dependencies?"
  - "What unstable Cargo features have been stabilized?"
  - "How do I restrict which unstable features can be used?"
  - "What is the garbage collection feature for Cargo's cache?"
---

# Quick Definition

Cargo's unstable features are experimental capabilities available only on the nightly channel, spanning build system enhancements, resolver options, output control, compilation behavior, rustdoc integration, Cargo.toml extensions, registry features, and more. They are enabled through three mechanisms: `cargo-features` in `Cargo.toml` (for new manifest syntax), `-Z unstable-options` (for new CLI flags), or `-Z <feature>` flags (for complex features). After a stabilization period, features graduate to the stable channel. The chapter catalogs approximately 50 active unstable features and 30+ stabilized ones.

# Core Definition

The source states: "Experimental Cargo features are only available on the nightly channel. You are encouraged to experiment with these features to see if they meet your needs, and if there are any issues or problems." (Ch. 17).

Three activation mechanisms are defined. First, **`cargo-features`** in `Cargo.toml`: "New syntax in Cargo.toml requires a `cargo-features` key at the top of Cargo.toml, before any tables." Second, **`-Z unstable-options`**: "New command-line flags, options, and subcommands require the `-Z unstable-options` CLI option." Third, **`-Z <flag>`**: "used to enable new functionality that may not have an interface, or the interface has not yet been designed." The `-Z` flags can also be set persistently via the `[unstable]` table in `.cargo/config.toml`.

The features are organized into categories: **Build scripts and linking** (metabuild, multiple build scripts, any build script metadata), **Resolver and features** (minimal-versions, public-dependency, msrv-policy, precise-pre-release, SBOM, update-breaking, feature-unification), **Output behavior** (artifact-dir, build-dir-new-layout, different-binary-name), **Compile behavior** (build-std, checksum-freshness, panic-abort-tests, host-config, target-applies-to-host, gc, open-namespaces), **Rustdoc** (rustdoc-map, scrape-examples, output-format), **Cargo.toml extensions** (profile rustflags, codegen-backend, per-package-target, artifact dependencies, trim-paths, lints.cargo, path bases), **Information** (unit-graph, build analysis), **Configuration** (cargo config), **Registries** (publish-timeout, asymmetric-token), and **Other** (gitoxide, script, native-completions, warnings).

# Prerequisites

- **Creating a Cargo Project** -- a project must exist to use unstable features
- **Cargo Dependencies** -- many unstable features affect dependency resolution and management

# Key Properties

1. **Three enablement mechanisms**: `cargo-features` in `Cargo.toml`, `-Z unstable-options` on CLI, or `-Z <flag>` / `[unstable]` config table
2. **`-Zallow-features`** restricts which unstable features can be used -- passing an empty string disallows all
3. **`build-std`**: Compiles the standard library from source, enabling custom targets and `no_std` builds; requires `rustup component add rust-src`
4. **`script`**: Enables single-file `.rs` packages with embedded manifests in a `---cargo` frontmatter block; supports `#!/usr/bin/env -S cargo +nightly -Zscript`
5. **`public-dependency`**: Marks dependencies as public or private; enables the `exported_private_dependencies` lint; MSRV for `public` field is 1.83
6. **`artifact-dependencies`**: Allows depending on `bin`, `cdylib`, and `staticlib` artifacts with environment variables providing paths at build time
7. **`sbom`**: Generates Software Bill of Materials pre-cursor files (`*.cargo-sbom.json`) alongside compiled artifacts
8. **`gc`**: Enables automatic garbage collection of Cargo's global cache with configurable age/size limits
9. **`trim-paths`**: Sanitizes file paths in binaries; defaults to `none` for dev, `object` for release
10. **`feature-unification`**: Controls feature merging across workspace -- `selected` (default), `workspace` (all members), or `package` (per-package, allowing duplicate builds)

# Construction / Recognition

## Enabling via `cargo-features` (manifest syntax):
```toml
cargo-features = ["test-dummy-unstable"]

[package]
name = "my-package"
version = "0.1.0"
```

## Enabling via `-Z` CLI flag:
```console
$ cargo +nightly build -Z build-std --target x86_64-unknown-linux-gnu
$ cargo +nightly build --artifact-dir=out -Z unstable-options
```

## Enabling via config file:
```toml
# .cargo/config.toml
[unstable]
mtime-on-use = true
build-std = ["core", "alloc"]
```

## Single-file Script with Embedded Manifest:
````rust
#!/usr/bin/env -S cargo +nightly -Zscript
---cargo
[dependencies]
clap = { version = "4.2", features = ["derive"] }
---

use clap::Parser;

#[derive(Parser, Debug)]
#[clap(version)]
struct Args {
    #[clap(short, long, help = "Path to config")]
    config: Option<std::path::PathBuf>,
}

fn main() {
    let args = Args::parse();
    println!("{:?}", args);
}
````

## Artifact Dependencies in Build Scripts:
```toml
[build-dependencies]
some-build-tool = { version = "1.0", artifact = "bin" }
```
```rust
// build.rs
fn main() {
    let tool = std::env::var_os("CARGO_BIN_FILE_SOME_BUILD_TOOL").unwrap();
    std::process::Command::new(tool).arg("do-stuff").status().unwrap();
}
```

## Garbage Collection Configuration:
```toml
# .cargo/config.toml
[unstable]
gc = true

[cache.global-clean]
max-src-age = "1 month"
max-crate-age = "3 months"
max-git-co-age = "1 month"
```

# Context & Application

This chapter serves as both a catalog and documentation hub for Cargo's experimental features. Several of these features represent significant architectural changes to the Rust build ecosystem: `build-std` enables compiling the standard library from source (essential for embedded and custom targets), `script` adds single-file package support (lowering the barrier to Rust for scripting), `public-dependency` adds visibility control to the dependency graph (enabling better API hygiene), and `feature-unification` provides fine-grained control over how features merge across workspaces. The chapter also documents a long history of stabilized features -- from compile progress bars (1.30) through workspace inheritance (1.64) to build-dir support (1.91) -- making it a useful reference for understanding when specific capabilities became available on stable. The `-Zallow-features` mechanism is particularly valuable for CI environments where teams want to restrict which nightly features are permitted.

# Examples

**Example 1** (Ch. 17): Build-std usage for cross-compilation:
> ```console
> $ cargo +nightly run -Z build-std --target x86_64-unknown-linux-gnu
>    Compiling core v0.0.0 (...)
>    ...
>    Compiling foo v0.1.0 (...)
>     Finished dev [unoptimized + debuginfo] target(s) in 21.00s
> ```
> "Here we recompiled the standard library in debug mode with debug assertions."

**Example 2** (Ch. 17): Restricting unstable features:
> "if you pass `-Zallow-features=foo,bar`, you'll continue to be able to pass `-Zfoo` and `-Zbar` to cargo, but you will be unable to pass `-Zbaz`. You can pass an empty string (`-Zallow-features=`) to disallow all unstable features."

**Example 3** (Ch. 17): Feature unification modes:
> "`selected`: Merge dependency features from all packages specified for the current build."
> "`workspace`: Merge dependency features across all workspace members, regardless of which packages are specified."
> "`package`: Dependency features are considered on a package-by-package basis, preferring duplicate builds."

**Example 4** (Ch. 17): SBOM generation:
> "The generated output files are in JSON format and follow the naming scheme `<artifact>.cargo-sbom.json`. The JSON file contains information about dependencies, target, features and the used rustc compiler."

**Example 5** (Ch. 17): Path bases for portable dependency paths:
> Given `[path-bases] dev = "/home/user/dev/rust/libraries/"` in config and `foo = { base = "dev", path = "foo" }` in Cargo.toml, the dependency resolves to `/home/user/dev/rust/libraries/foo`. A built-in `workspace` base points to the workspace root.

# Relationships

## Builds Upon
- **Creating a Cargo Project** -- unstable features modify how projects are built and configured
- **Cargo Dependencies** -- many features (public-dependency, artifact-dependencies, feature-unification) change dependency behavior

## Enables
- Cross-compilation to custom targets via build-std
- Single-file Rust scripting via script
- SBOM compliance via sbom
- Cache management via gc
- Fine-grained feature control via feature-unification

## Related
- **cargo-semver-compatibility** -- update-breaking allows SemVer-incompatible upgrades via `cargo update --breaking`
- **cargo-lints-reference** -- the `[lints.cargo]` system is itself an unstable feature documented in this chapter
- **cargo-build-performance** -- several unstable features (build-std, feature-unification, codegen-backend, hint-mostly-unused) directly affect build performance

## Contrasts With
- None within this source

# Common Errors

- **Error**: Trying to use `-Z` flags on stable Rust.
  **Correction**: All `-Z` flags require a nightly toolchain. Use `cargo +nightly` or set the default toolchain to nightly.

- **Error**: Placing `cargo-features` below the `[package]` table.
  **Correction**: "New syntax in Cargo.toml requires a `cargo-features` key at the top of Cargo.toml, before any tables."

- **Error**: Using `build-std` without installing the rust-src component.
  **Correction**: "You must install libstd's source code through `rustup component add rust-src`."

- **Error**: Expecting `public-dependency` to work without the `-Zpublic-dependency` flag or `[unstable]` config.
  **Correction**: The feature requires explicit enablement. Additionally, the `public` field in dependencies requires MSRV 1.83+.

# Common Confusions

- **Confusion**: Thinking all `-Z` features require the same enablement mechanism.
  **Clarification**: There are three distinct mechanisms: `cargo-features` for manifest syntax, `-Z unstable-options` for new CLI flags/options, and `-Z <flag>` for complex features. Each feature documents which mechanism it uses.

- **Confusion**: Thinking unstable features are permanently unstable.
  **Clarification**: Most features follow a stabilization path -- they are experimented with on nightly, then stabilized for stable Rust. The chapter documents 30+ already-stabilized features. A few (like `allow-features` and `compile-time-deps`) are permanently unstable.

- **Confusion**: Thinking `cargo script` creates a full Cargo project.
  **Clarification**: Single-file packages are self-contained `.rs` files with optional embedded manifests. They use a separate target directory at `$CARGO_HOME/target/<hash>` and cannot define workspaces, multiple targets, or build scripts.

- **Confusion**: Thinking `feature-unification = "workspace"` is always better than "selected".
  **Clarification**: Workspace unification "trades correctness for build speed" -- a package activating a feature can mask bugs in other packages that should activate it but do not.

# Source Reference

Chapter 17: Unstable Features -- "List of unstable features" covering all active unstable features organized by category, plus "Stabilized and removed features" documenting the history of graduated features. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 17 opening paragraphs and the feature catalog
- Confidence rationale: HIGH -- the source provides specific enablement instructions, code examples, and tracking issue links for every feature
- Uncertainties: Unstable features may be stabilized, changed, or removed at any time. The specific set of features and their behavior is a snapshot; the source links to tracking issues for current status.
- Cross-reference status: Prerequisites reference cards from other extraction sets; related cards are within this extraction set
