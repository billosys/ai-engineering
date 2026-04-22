---
concept: Cargo Changes 2024
slug: cargo-changes-2024
category: edition-2024
subcategory: null
tier: intermediate
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "05-rust-2024"
chapter_number: 5
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "cargo 2024"
  - "resolver v3"
  - "rust-version aware resolver"
  - "cargo table consistency"
  - "cargo edition 2024"
prerequisites:
  - rust-editions
related:
  - rust-2024-edition
contrasts_with: []
extends: []
answers_questions:
  - "What changed in Cargo for the Rust 2024 Edition?"
  - "What is Cargo resolver v3?"
  - "How does the Rust-version aware resolver work?"
  - "Which Cargo.toml keys were removed in Rust 2024?"
  - "What is the unused inherited default-features change?"
---

# Quick Definition

Cargo in the 2024 Edition introduces three changes: a Rust-version aware dependency resolver (resolver v3, implied by `edition = "2024"`), removal of deprecated table and key name variants in `Cargo.toml` (enforcing hyphens over underscores), and rejecting unused inherited `default-features = false` when the workspace does not specify `default-features = false`.

# Core Definition

**1. Rust-version aware resolver (resolver v3):** Setting `edition = "2024"` in `Cargo.toml` implies `resolver = "3"`, which in turn implies `resolver.incompatible-rust-version = "fallback"` in `.cargo/config.toml`. This means Cargo considers `package.rust-version` when selecting dependency versions, preferring versions compatible with your declared Rust version and falling back to incompatible versions only when no compatible version exists.

This is available since Rust 1.84.0 as an opt-in. In 2024, it becomes the default. The resolver is a global workspace setting -- it is only honored for the top-level package. Virtual workspaces must explicitly set `resolver = "3"` in the `[workspace]` definition.

**2. Table and key name consistency:** Several table and key names that had both underscore and hyphen variants now only allow the hyphen form:
- `[project]` removed, use `[package]`
- `default_features` removed, use `default-features`
- `crate_type` removed, use `crate-type`
- `proc_macro` removed, use `proc-macro`
- `dev_dependencies` removed, use `dev-dependencies`
- `build_dependencies` removed, use `build-dependencies`

**3. Reject unused inherited default-features:** When using workspace dependency inheritance, specifying `default-features = false` in a package dependency is an error if the workspace definition does not also specify `default-features = false`. This prevents the confusing situation where `default-features = false` appears to disable defaults but has no effect because the workspace already enables them.

# Prerequisites

- **Rust editions** -- understanding edition-gated tooling changes

# Key Properties

1. `edition = "2024"` implies `resolver = "3"` (Rust-version aware dependency resolution)
2. Resolver v3 is available since Rust 1.84.0 as opt-in; 2024 makes it the default
3. The resolver is a global workspace setting, ignored in dependencies
4. Virtual workspaces must explicitly set `resolver = "3"`
5. Six underscore-named tables/keys are removed in favor of hyphen equivalents
6. `[project]` table is removed in favor of `[package]`
7. Inherited `default-features = false` is rejected when the workspace uses the default (`true`)
8. All three changes can be auto-fixed by `cargo fix --edition`
9. Projects should verify against latest dependencies in CI after adopting resolver v3

# Construction / Recognition

## Enabling Resolver v3 Explicitly (for virtual workspaces):

```toml
[workspace]
resolver = "3"
members = ["crate1", "crate2"]
```

## Fixing Table/Key Names:

Before (2021):

```toml
[dev_dependencies]
rand = { version = "0.8.5", default_features = false }
```

After (2024):

```toml
[dev-dependencies]
rand = { version = "0.8.5", default-features = false }
```

## Fixing Inherited Default-Features:

Workspace `Cargo.toml`:

```toml
[workspace.dependencies]
regex = "1.10.4"
```

Package `Cargo.toml` -- ERROR in 2024:

```toml
[dependencies]
regex = { workspace = true, default-features = false }  # ERROR
```

Fix option 1 -- remove `default-features` from the package (it had no effect anyway):

```toml
[dependencies]
regex = { workspace = true }
```

Fix option 2 -- set `default-features = false` in the workspace definition:

```toml
[workspace.dependencies]
regex = { version = "1.10.4", default-features = false }
```

# Context & Application

The resolver v3 change is the most impactful for production environments. Without Rust-version awareness, `cargo update` could select a dependency version that requires a newer Rust compiler than specified in `rust-version`, causing CI failures. With resolver v3, Cargo prefers compatible versions, reducing surprise breakage.

The table/key consistency change is straightforward cleanup. The underscore variants were either historical artifacts (`[project]` was an early name for `[package]`) or inadvertent implementation artifacts. Enforcing a single style reduces confusion.

The inherited default-features change catches a common mistake: specifying `default-features = false` in a package when the workspace does not, which has no effect. Previous editions only warned; 2024 makes it an error.

# Examples

**Example 1** (resolver v3): With `edition = "2024"` and `rust-version = "1.80"`, Cargo will prefer dependency versions that declare compatibility with Rust 1.80, falling back to newer-requiring versions only when necessary.

**Example 2** (table consistency): `cargo fix --edition` automatically renames `[dev_dependencies]` to `[dev-dependencies]` and `default_features` to `default-features` in `Cargo.toml`.

**Example 3** (inherited default-features): Previous editions warned: "default-features is ignored for regex, since default-features was not specified for workspace.dependencies.regex." In 2024, this becomes a hard error.

# Relationships

## Related
- **rust-2024-edition** -- these are the Cargo changes in the 2024 edition

# Common Errors

- **Error**: Expecting virtual workspaces to automatically use resolver v3 when member crates specify `edition = "2024"`.
  **Correction**: Virtual workspaces must explicitly set `resolver = "3"` in the `[workspace]` definition. The edition of member crates does not affect the workspace resolver.

- **Error**: Not verifying against latest dependencies in CI after adopting resolver v3.
  **Correction**: Resolver v3 may pin to older dependency versions. Run CI with both `--locked` (for reproducibility) and without locks (to catch bugs in latest deps), as recommended by the Cargo documentation.

# Common Confusions

- **Confusion**: Thinking resolver v3 prevents ever using dependencies that require newer Rust.
  **Clarification**: Resolver v3 uses "fallback" mode: it prefers compatible versions but falls back to incompatible ones when no compatible version exists. It does not hard-block newer dependencies.

- **Confusion**: Thinking the table/key changes affect runtime behavior.
  **Clarification**: These are purely syntactic. `[dev_dependencies]` and `[dev-dependencies]` always meant the same thing; only the name is standardized.

# Source Reference

Rust Edition Guide, Chapter 5: Rust 2024. Three sections under "Cargo": "Cargo: Rust-version aware resolver," "Cargo: Table and key name consistency," and "Cargo: Reject unused inherited default-features." The resolver section references `package.rust-version` and `resolver.incompatible-rust-version = "fallback"` configuration.

# Verification Notes

- Resolver v3 details: from "Rust-version aware resolver" section
- Key/table removals: complete list from "Table and key name consistency" section
- Inherited default-features: from "Reject unused inherited default-features" section with the warning message
- Virtual workspace caveat: directly stated in the resolver section
- Confidence: HIGH -- all information directly from the edition guide
- Cross-references: slugs verified against this extraction set
