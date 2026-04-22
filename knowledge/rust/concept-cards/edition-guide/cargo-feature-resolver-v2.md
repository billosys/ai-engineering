---
concept: Default Cargo Feature Resolver v2
slug: cargo-feature-resolver-v2
category: edition-2021
subcategory: null
tier: intermediate
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "04-rust-2021"
chapter_number: 4
pdf_page: null
section: "Default Cargo feature resolver"
extraction_confidence: high
aliases:
  - "resolver v2"
  - "feature resolver 2"
  - "Cargo resolver 2"
prerequisites:
  - rust-2021-edition
extends: []
related:
  - edition-migration
contrasts_with: []
answers_questions:
  - "What is Cargo's feature resolver v2?"
  - "Why might dependencies build differently in Rust 2021?"
  - "How does resolver v2 change feature unification?"
  - "Why does my project fail to build after upgrading to Rust 2021?"
---

# Quick Definition

In Rust 2021, setting `edition = "2021"` in `Cargo.toml` automatically implies `resolver = "2"`. The v2 resolver no longer merges features across all dependency kinds -- build-dependencies, proc-macros, platform-specific dependencies, and dev-dependencies each get their own feature resolution, potentially causing some dependencies to be built with fewer features than before.

# Core Definition

"Since Rust 1.51.0, Cargo has opt-in support for a new feature resolver which can be activated with `resolver = "2"` in `Cargo.toml`. Starting in Rust 2021, this will be the default. That is, writing `edition = "2021"` in `Cargo.toml` will imply `resolver = "2"`. [...] The new feature resolver no longer merges all requested features for crates that are depended on in multiple ways." (Edition Guide, Ch. 4: Rust 2021, "Default Cargo feature resolver")

# Prerequisites

- **Rust 2021 Edition** (`rust-2021-edition`) -- resolver v2 becoming the default is part of the 2021 edition changes

# Key Properties

1. `edition = "2021"` implies `resolver = "2"` in `Cargo.toml`
2. The resolver is a global workspace setting; it is ignored in dependencies
3. Only the top-level package's resolver setting matters
4. Virtual workspaces still require explicit `resolver = "2"` in the `[workspace]` definition
5. Features enabled on platform-specific dependencies for non-current targets are ignored
6. Build-dependencies and proc-macros do not share features with normal dependencies
7. Dev-dependencies do not activate features unless building a target that needs them (tests, examples)
8. A dependency may be built multiple times with different feature sets

# Construction / Recognition

## To Diagnose Resolver v2 Build Failures:
1. Run `cargo fix --edition` and read the report about changed features
2. Use `cargo tree -d` to find packages built multiple times
3. Use `cargo tree -f '{p} {f}'` to see which features each package uses
4. Use `cargo tree -e features -i <package>` to see how features flow into a dependency
5. Add missing features explicitly to your dependency declarations
6. For proc-macro issues, add the dependency as a `[build-dependencies]` with required features

## To Identify the Resolver Version:
1. Check for `resolver = "2"` in `Cargo.toml`
2. Check for `edition = "2021"` or later, which implies resolver v2
3. For virtual workspaces, the resolver field must be explicit

# Context & Application

The v1 resolver unified all features for a given dependency regardless of how it was depended upon. This meant a crate used as both a normal dependency (without default features) and a build-dependency (with default features) would get all features merged together. This was often convenient but could lead to unexpected compile times and binary sizes.

The v2 resolver separates feature resolution by dependency kind. The most common breakage pattern occurs when a crate `A` depends on crate `B` with limited features, but another crate in the dependency tree depends on `B` as a build-dependency with more features. Under v1, `A` got the extra features for free. Under v2, `A` only gets the features it explicitly requested.

A real-world example from the source involves `diesel` and `diesel_migrations`: the `diesel_migrations` proc-macro internally depends on `diesel`, and under v2, the proc-macro's copy of `diesel` does not automatically get the "postgres" feature enabled by the normal dependency. The fix is to add `diesel` as a `[build-dependencies]` entry with the required features.

# Examples

**Example 1** (Feature divergence, "Build failures" subsection):

```toml
# Your Cargo.toml
[dependencies]
bstr = { version = "0.2.16", default-features = false }

# Another package's Cargo.toml (in your dependency tree)
[build-dependencies]
bstr = "0.2.16"
```

Under v1, `bstr` was built once with all features merged. Under v2, your copy of `bstr` has no features, so methods requiring the "unicode" feature (like `words_with_breaks`) are missing. The fix:

```toml
[dependencies]
bstr = { version = "0.2.16", default-features = false, features = ["unicode"] }
```

**Example 2** (Proc-macro dependency, "Build failures" subsection):

```toml
[dependencies]
diesel = { version = "1.4.7", features = ["postgres"] }
diesel_migrations = "1.4.0"

# Fix: add diesel as a build-dependency so the proc-macro gets the feature
[build-dependencies]
diesel = { version = "1.4.7", features = ["postgres"] }
```

**Example 3** (Exploring features with cargo tree, "Exploring features" subsection):

```console
# Find packages built multiple times
cargo tree -d

# See features for each package
cargo tree -f '{p} {f}'

# See how features flow into a specific package
cargo tree -e features -i bstr
```

# Relationships

## Builds Upon
- **rust-2021-edition** -- resolver v2 becomes default as part of the 2021 edition

## Enables
- No downstream concepts directly

## Related
- **edition-migration** -- `cargo fix --edition` reports feature changes during migration

## Contrasts With
- None explicitly stated (implicitly contrasts with resolver v1 behavior)

# Common Errors

- **Error**: Assuming `cargo fix --edition` will automatically fix resolver-related build failures.
  **Correction**: There are no automated migration tools for the resolver change. `cargo fix --edition` only reports which dependencies will be built with different features. You must manually add the required features to your dependency declarations.

- **Error**: Setting `resolver = "2"` in a dependency crate's `Cargo.toml` expecting it to take effect.
  **Correction**: The resolver setting is only honored for the top-level package of the workspace. It is ignored in dependencies.

# Common Confusions

- **Confusion**: Thinking resolver v2 removes features from dependencies.
  **Clarification**: Resolver v2 does not remove features. It stops merging features across different dependency kinds. If your crate never relied on features "leaking" from build-dependencies or other dependency kinds, the change has no effect.

- **Confusion**: Thinking virtual workspaces automatically get resolver v2 with `edition = "2021"`.
  **Clarification**: Virtual workspaces do not have a package with an edition field. You must still explicitly set `resolver = "2"` in the `[workspace]` definition of a virtual workspace.

- **Confusion**: Thinking a dependency being built twice means something is wrong.
  **Clarification**: Under resolver v2, it is normal for a dependency to appear twice in `cargo tree -d` output -- once for normal use and once for build/proc-macro use, potentially with different features.

# Source Reference

Chapter 4: Rust 2021, "Default Cargo feature resolver" section. Covers the resolver default change, workspace behavior, migration diagnostics, build failure scenarios (with `bstr` and `diesel` examples), and feature exploration with `cargo tree`.

# Verification Notes

- Definition source: Direct quotation from "Default Cargo feature resolver" section, "Details" subsection
- Key Properties: All from explicit statements in the source, including the three unification rules
- Confidence rationale: HIGH -- the source provides detailed documentation including real-world examples and diagnostic commands
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set or Agent A's set
