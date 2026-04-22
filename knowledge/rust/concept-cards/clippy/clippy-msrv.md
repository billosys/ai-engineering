---
# === CORE IDENTIFICATION ===
concept: Clippy MSRV Configuration
slug: clippy-msrv

# === CLASSIFICATION ===
category: configuration
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "01-getting-started"
chapter_number: 1
pdf_page: null
section: "Configuring Clippy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "minimum supported Rust version"
  - "msrv"
  - "clippy msrv"
  - "clippy::msrv"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
  - clippy-configuration
extends: []
related:
  - cargo-clippy
  - clippy-lint-levels
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I tell Clippy my project's minimum supported Rust version?"
  - "How does MSRV affect Clippy lints?"
  - "Where do I set the MSRV for Clippy?"
  - "Can I set MSRV as a source attribute?"
  - "Which Clippy lints are affected by MSRV?"
---

# Quick Definition

Clippy's MSRV (Minimum Supported Rust Version) configuration allows projects to disable lints that suggest using features from newer Rust versions than the project supports. It is set via `msrv` in `clippy.toml` or as a crate-level attribute.

# Core Definition

Projects that need to support older Rust versions can configure Clippy's MSRV setting to automatically disable lints that would suggest using features not available in the target Rust version. This prevents Clippy from recommending code patterns that would break compatibility with the project's minimum supported Rust version.

The MSRV can be specified in two ways:

1. **In `clippy.toml`**: Set `msrv = "1.30.0"` (or without patch version: `msrv = "1.30"`)
2. **As a crate-level attribute**: `#![clippy::msrv = "1.30.0"]` (requires the unstable `custom_inner_attributes` feature)

When MSRV is configured, lints that recommend using features introduced after the specified version are automatically suppressed. For example, if MSRV is set to 1.30, a lint suggesting use of a feature added in Rust 1.40 would be silenced.

# Prerequisites

- **clippy** -- MSRV is a Clippy-specific configuration
- **clippy-configuration** -- MSRV is set in `clippy.toml`, Clippy's configuration file

# Key Properties

1. Set via `msrv = "1.30.0"` in `clippy.toml` or `.clippy.toml`
2. Patch version can be omitted: `msrv = "1.30"` is equivalent to `msrv = "1.30.0"`
3. Can also be set as a crate attribute: `#![clippy::msrv = "1.30.0"]`
4. The attribute form requires the unstable `custom_inner_attributes` feature
5. Disables lints that suggest using features not available in the specified Rust version
6. The full list of MSRV-aware lints is available on the Clippy lint list site

# Construction / Recognition

## To Configure MSRV in clippy.toml:
1. Add `msrv = "1.56.0"` to your `clippy.toml` file
2. The patch version is optional: `msrv = "1.56"` works the same

## To Configure MSRV as a Source Attribute:
1. Add the unstable feature gate: `#![feature(custom_inner_attributes)]`
2. Add the MSRV attribute: `#![clippy::msrv = "1.56.0"]`

## To Find MSRV-Aware Lints:
1. Visit https://rust-lang.github.io/rust-clippy/master/index.html#msrv
2. Each listed lint indicates which Rust version feature it depends on

# Context & Application

MSRV configuration is essential for library authors and projects that guarantee compatibility with older Rust versions. Without MSRV configuration, Clippy might suggest replacing working code with idioms that require newer compiler versions, which would break the project's compatibility guarantee.

For example, many crates in the ecosystem support Rust versions several releases behind the latest stable. Clippy's MSRV awareness ensures that its suggestions remain compatible with the project's support policy.

The `clippy.toml` approach is preferred for most projects because it does not require an unstable compiler feature. The attribute approach is useful for testing or for projects already on nightly.

# Examples

**Example 1**: Setting MSRV in clippy.toml:
```toml
msrv = "1.30.0"
```

**Example 2**: Setting MSRV with abbreviated version (no patch):
```toml
msrv = "1.30"
```

**Example 3**: Setting MSRV as a crate-level attribute (requires nightly):
```rust
#![feature(custom_inner_attributes)]
#![clippy::msrv = "1.30.0"]

fn main() {
    // Clippy will not suggest features newer than Rust 1.30
}
```

# Relationships

## Builds Upon
- **clippy** -- MSRV configuration affects Clippy lint behavior
- **clippy-configuration** -- MSRV is a configuration option set in `clippy.toml`

## Related
- **cargo-clippy** -- MSRV affects which lints are reported when running `cargo clippy`
- **clippy-lint-levels** -- MSRV effectively sets certain lints to `allow` when the feature they require is newer than the MSRV

# Common Errors

- **Error**: Setting MSRV in `Cargo.toml` instead of `clippy.toml` and expecting Clippy to respect it.
  **Correction**: Clippy reads MSRV from `clippy.toml` (or via the crate attribute), not from `Cargo.toml`'s `rust-version` field. Set it explicitly in `clippy.toml`.

- **Error**: Using the attribute form (`#![clippy::msrv = "1.30.0"]`) on stable Rust and getting a compiler error.
  **Correction**: The attribute form requires `#![feature(custom_inner_attributes)]`, which is only available on nightly. Use `clippy.toml` for stable Rust projects.

# Common Confusions

- **Confusion**: Thinking MSRV disables all lints that mention newer Rust features.
  **Clarification**: MSRV only affects lints that are explicitly MSRV-aware. Not all lints check the MSRV setting. The full list of MSRV-aware lints is documented on the Clippy lint list.

- **Confusion**: Believing MSRV and `rust-version` in `Cargo.toml` are the same thing for Clippy.
  **Clarification**: Clippy has its own MSRV configuration in `clippy.toml`. While `Cargo.toml`'s `rust-version` field serves a similar purpose for cargo, Clippy reads its own setting independently.

# Source Reference

Chapter 1 (Getting Started), "Configuring Clippy" section, subsection "Specifying the minimum supported Rust version" at lines 286-312 of 01-getting-started.md.

# Verification Notes

- `clippy.toml` syntax: Directly from source -- `msrv = "1.30.0"`
- Abbreviated version: Directly stated -- "you can also omit the patch version"
- Attribute syntax: Directly from source with the `custom_inner_attributes` feature gate
- Unstable feature note: Directly stated -- "custom_inner_attributes is an unstable feature"
- MSRV-aware lint list: Referenced with link to Clippy lint list filtered by msrv
- Confidence: HIGH -- all content directly from source documentation
- Cross-references: All slugs verified against planned extractions
