---
# === CORE IDENTIFICATION ===
concept: Cargo Features
slug: cargo-features

# === CLASSIFICATION ===
category: package-management
subcategory: conditional-compilation
tier: foundational

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "04-features"
chapter_number: 4
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "feature flags"
  - "conditional compilation"
  - "optional dependencies"
  - "Cargo feature flags"
  - "feature unification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-dependency-specification
  - cargo-dependencies
extends: []
related:
  - cargo-build-performance
  - cargo-toml-vs-cargo-lock
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are Cargo features and how do they enable conditional compilation?"
  - "How do I define features in Cargo.toml?"
  - "What is the default feature and how do I control it?"
  - "How do optional dependencies relate to features?"
  - "What is the dep: prefix syntax and when should I use it?"
  - "How do I enable features on dependencies?"
  - "What is feature unification and why must features be additive?"
  - "What is the difference between resolver version 1 and 2 for features?"
  - "How do I inspect which features are enabled in my dependency graph?"
  - "What are the SemVer implications of adding or removing features?"
  - "How do I handle no_std support with features?"
  - "What command-line options control feature selection?"
---

# Quick Definition

Cargo features are named flags defined in the `[features]` table of `Cargo.toml` that enable conditional compilation and optional dependencies. Each feature specifies an array of other features or `dep:` optional dependencies it enables. Features are disabled by default (unless listed in `default`), are unified across the dependency graph (the union of all requested features is built), and must be additive -- enabling a feature should never disable functionality or break existing code.

# Core Definition

The source defines features as a mechanism to "express conditional compilation and optional dependencies" (Ch. 4). Features are declared in the `[features]` table where "each feature specifies an array of other features or optional dependencies that it enables." A feature named `webp = []` enables conditional code via `#[cfg(feature = "webp")]` and the `cfg!` macro, because "Cargo sets features in the package using the `rustc` `--cfg` flag."

**Optional dependencies** implicitly define a same-named feature unless the `dep:` prefix is used. The source explains: "By default, this optional dependency implicitly defines a feature that looks like this: `gif = [\"dep:gif\"]`." Using `dep:` explicitly (available since Rust 1.60) suppresses the implicit feature, which is useful for grouping internal dependencies: `avif = ["dep:ravif", "dep:rgb"]`.

**Feature unification** is the critical design constraint. The source states: "When a dependency is used by multiple packages, Cargo will use the union of all features enabled on that dependency when building it." This means "features should be *additive*. That is, enabling a feature should not disable functionality." For `no_std` support, the source recommends using a `std` feature that enables `std`, rather than a `no_std` feature that disables it.

The **version 2 resolver** (`resolver = "2"`) changes unification behavior: it avoids unifying features across platform-specific deps for non-current targets, between build-dependencies and normal dependencies, and for dev-dependencies unless building targets that need them.

# Prerequisites

- **Cargo Dependency Specification** -- features are defined on dependencies and interact with version requirements and optional deps
- **Cargo Dependencies** -- basic dependency management workflow

# Key Properties

1. **Feature declaration**: `[features]` table; each feature is a name mapping to an array of enabled features/deps
2. **Default feature**: `default = ["ico", "webp"]` enables listed features unless `--no-default-features` or `default-features = false`
3. **Optional dependencies**: `optional = true` on a dependency creates an implicit feature of the same name
4. **dep: prefix**: `dep:crate_name` in feature arrays suppresses the implicit feature (Rust 1.60+)
5. **Dependency features**: enabled via `features = ["derive"]` in dependency declaration or `"package-name/feature-name"` in `[features]`
6. **Weak dependency features**: `"package-name?/feature-name"` only enables a feature if the optional dep is already enabled (Rust 1.60+)
7. **Feature unification**: the union of all requested features is built; features must be additive
8. **Resolver v2**: avoids unifying across platform targets, build-deps vs normal deps, and dev-deps vs normal deps
9. **Conditional compilation**: code uses `#[cfg(feature = "name")]` and `cfg!(feature = "name")`
10. **Build script detection**: features available via `CARGO_FEATURE_<NAME>` environment variable
11. **Command-line control**: `--features`, `--all-features`, `--no-default-features`
12. **SemVer rules**: adding features is safe in minor releases; removing features or moving code behind features is breaking
13. **Mutually exclusive features**: discouraged; use `compile_error!` if unavoidable, prefer feature precedence or runtime options
14. **300 feature limit**: crates.io limits new crates/versions to a maximum of 300 features

# Construction / Recognition

## Defining Features:
```toml
[features]
bmp = []
png = []
ico = ["bmp", "png"]
webp = []
default = ["ico", "webp"]
```

## Conditional Compilation in Code:
```rust
#[cfg(feature = "webp")]
pub mod webp;
```

## Optional Dependency with dep: Prefix:
```toml
[dependencies]
ravif = { version = "0.6.3", optional = true }
rgb = { version = "0.8.25", optional = true }

[features]
avif = ["dep:ravif", "dep:rgb"]
```

## Enabling Dependency Features:
```toml
[dependencies]
serde = { version = "1.0.118", features = ["derive"] }
flate2 = { version = "1.0.3", default-features = false, features = ["zlib-rs"] }
```

## Weak Dependency Features (?/ syntax):
```toml
[dependencies]
serde = { version = "1.0.133", optional = true }
rgb = { version = "0.8.25", optional = true }

[features]
serde = ["dep:serde", "rgb?/serde"]
```

## Enabling Features via [features] Table:
```toml
[dependencies]
jpeg-decoder = { version = "0.1.20", default-features = false }

[features]
parallel = ["jpeg-decoder/rayon"]
```

## Feature Resolver v2:
```toml
[package]
name = "my-package"
version = "1.0.0"
resolver = "2"
```

## Detecting Mutually Exclusive Features:
```rust
#[cfg(all(feature = "foo", feature = "bar"))]
compile_error!("feature \"foo\" and feature \"bar\" cannot be enabled at the same time");
```

# Context & Application

This card covers the complete feature system as specified in the Cargo Reference. Features are the primary mechanism for conditional compilation in the Rust ecosystem, enabling crates to offer optional functionality without forcing all users to compile everything. The additive constraint and unification behavior are the most consequential design decisions: they mean any package in a dependency graph can enable features on shared dependencies, and those features cannot be "un-enabled" by other packages. This has major implications for crate design -- the `no_std` vs `std` feature pattern, the `dep:` prefix for hiding internal optional deps, and the resolver v2 for avoiding unwanted cross-context unification are all responses to real-world problems arising from the unification model. The "Features Examples" section provides practical patterns including minimizing build times (syn, regex, winapi), no_std support, proc-macro companions, and nightly-only gating.

# Examples

**Example 1** (Ch. 4): Features enabling other features (ICO requires BMP and PNG):
```toml
[features]
bmp = []
png = []
ico = ["bmp", "png"]
webp = []
```

**Example 2** (Ch. 4): The dep: prefix hiding internal optional dependencies:
```toml
[dependencies]
ravif = { version = "0.6.3", optional = true }
rgb = { version = "0.8.25", optional = true }

[features]
avif = ["dep:ravif", "dep:rgb"]
```
> "This also avoids creating the implicit `ravif` and `rgb` features, since we don't want users to enable those individually as they are internal details to our crate."

**Example 3** (Ch. 4): Feature unification with winapi:
> "If your package depends on a package `foo` which enables the 'fileapi' and 'handleapi' features of `winapi`, and another dependency `bar` which enables the 'std' and 'winnt' features of `winapi`, then `winapi` will be built with all four of those features enabled."

**Example 4** (Ch. 4): Correct no_std pattern using a `std` feature:
```rust
#![no_std]

#[cfg(feature = "std")]
extern crate std;

#[cfg(feature = "std")]
pub fn function_that_requires_std() {
    // ...
}
```
> "Do **not** use a `no_std` feature. Instead, use a `std` feature that *enables* `std`."

**Example 5** (Ch. 4): Inspecting resolved features:
```console
$ cargo tree -e features          # show features in dependency graph
$ cargo tree -f "{p} {f}"         # compact view with features per package
$ cargo tree -e features -i foo   # invert: show how features flow into "foo"
```

# Relationships

## Builds Upon
- **Cargo Dependency Specification** -- features interact with dependency syntax (`optional`, `features`, `default-features`)
- **Cargo Dependencies** -- features extend basic dependency management with conditionality

## Enables
- Conditional compilation patterns in library crates
- Optional functionality without mandatory compile-time cost
- no_std / std dual-support crate design

## Related
- **cargo-build-performance** -- feature count and unification affect build times; workspace feature unification is a performance technique
- **cargo-toml-vs-cargo-lock** -- feature resolution affects what gets locked

## Contrasts With
- None within this source

# Common Errors

- **Error**: Creating a `no_std` feature that disables `std` functionality.
  **Correction**: Features must be additive. "Do **not** use a `no_std` feature. Instead, use a `std` feature that *enables* `std`."

- **Error**: Assuming `default-features = false` on your dependency guarantees defaults are off.
  **Correction**: "If another dependency includes `flate2` without specifying `default-features = false`, then the default features will be enabled" due to feature unification.

- **Error**: Removing a feature in a minor version release.
  **Correction**: Removing a feature is a SemVer-incompatible change. "The following should usually **not** be done in a minor release: Remove a feature or optional dependency."

- **Error**: Using `"package-name/feature-name"` syntax on an optional dependency when you only want to enable a feature if it is already active.
  **Correction**: `"package-name/feature-name"` also enables the optional dependency. Use `"package-name?/feature-name"` (weak dependency syntax) to only enable the feature if the dep is already enabled by something else.

# Common Confusions

- **Confusion**: Thinking optional dependencies and features are separate concepts.
  **Clarification**: "By default, this optional dependency implicitly defines a feature that looks like this: `gif = [\"dep:gif\"]`." An optional dependency IS a feature unless the `dep:` prefix is used to suppress the implicit feature.

- **Confusion**: Thinking features are scoped per-package-use in the dependency graph.
  **Clarification**: "When a dependency is used by multiple packages, Cargo will use the union of all features enabled on that dependency when building it." Features are globally unified per dependency version.

- **Confusion**: Thinking resolver v2 eliminates all unwanted feature unification.
  **Clarification**: Resolver v2 only avoids unification in three specific cases (cross-platform, build-deps, dev-deps). Normal dependencies from different packages still have their features unified. A tradeoff is "it can increase build times because the dependency is built multiple times."

- **Confusion**: Thinking `--all-features` only affects the current package.
  **Clarification**: `--all-features` "activates all features of all packages selected on the command line," which may include multiple workspace members.

# Source Reference

Chapter 4: Features -- sections on the [features] section, default feature, optional dependencies, dependency features, command-line options, feature unification, mutually exclusive features, feature resolver version 2, build scripts, required features, SemVer compatibility, and feature documentation. Also includes Features Examples appendix covering real-world patterns. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 4 -- "Cargo 'features' provide a mechanism to express conditional compilation and optional dependencies"
- Confidence rationale: HIGH -- the source provides comprehensive syntax, semantics, design rationale, and real-world examples (syn, regex, winapi, wasm-bindgen, serde)
- Uncertainties: The `dep:` and `?/` syntax require Rust 1.60+; resolver behavior may evolve in future editions
- Cross-reference status: References cargo-dependency-specification (Ch. 3), cargo-dependencies (guide-level), cargo-build-performance
