---
# === CORE IDENTIFICATION ===
concept: Clippy Configuration
slug: clippy-configuration

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
  - "clippy.toml"
  - ".clippy.toml"
  - "clippy configuration file"
  - "CLIPPY_CONF_DIR"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
  - cargo-clippy
extends: []
related:
  - clippy-lint-levels
  - clippy-lint-groups
  - clippy-msrv
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure Clippy with a TOML file?"
  - "Where does Clippy look for its configuration file?"
  - "What is the difference between clippy.toml and .clippy.toml?"
  - "How does CLIPPY_CONF_DIR work?"
  - "How do I extend default list values in clippy.toml?"
  - "How do I disable Clippy documentation links?"
  - "How do I conditionally exclude code from Clippy analysis?"
---

# Quick Definition

Clippy can be configured via a TOML file named `clippy.toml` or `.clippy.toml` that controls lint-specific parameters like thresholds, allowed names, and feature gates. The file is searched for in a priority-ordered set of directories and supports a `".."` syntax to extend default list values.

# Core Definition

Some Clippy lints accept configuration parameters that fine-tune their behavior. These parameters are set in a TOML file named `clippy.toml` or `.clippy.toml` (both names are equivalent). The file uses a simple `variable = value` format.

The configuration file is located by searching in priority order:
1. The directory specified by the `CLIPPY_CONF_DIR` environment variable
2. The directory specified by `CARGO_MANIFEST_DIR` (the directory containing `Cargo.toml`)
3. The current working directory

If the chosen directory does not contain a configuration file, Clippy walks up the directory tree, searching each parent directory until it finds one or reaches the filesystem root.

**Important note:** The documentation states that the configuration file is unstable and may be deprecated in the future.

For list-type configurations with default values, the special value `".."` extends the defaults instead of replacing them.

Additionally, code sections can be conditionally excluded from Clippy analysis using `#[cfg(not(clippy))]`, though this should be a last resort when `#[allow(clippy::all)]` is insufficient.

# Prerequisites

- **clippy** -- The configuration file tunes Clippy's behavior
- **cargo-clippy** -- Configuration is typically used alongside cargo-based Clippy runs

# Key Properties

1. Configuration file can be named `clippy.toml` or `.clippy.toml`
2. File uses simple TOML `variable = value` syntax
3. Search order: `CLIPPY_CONF_DIR` > `CARGO_MANIFEST_DIR` > current directory
4. Walks up the directory tree if the config file is not found in the initial directory
5. The `".."` value in lists extends defaults rather than replacing them
6. The `CLIPPY_DISABLE_DOCS_LINKS` environment variable suppresses lint documentation links
7. `#[cfg(not(clippy))]` can conditionally exclude code from Clippy analysis (last resort)
8. The configuration file is marked as unstable -- it may be deprecated in the future

# Construction / Recognition

## To Create a Clippy Configuration:
1. Create a file named `clippy.toml` or `.clippy.toml` in your project root (next to `Cargo.toml`)
2. Add configuration values: `avoid-breaking-exported-api = false`
3. For list values, use `".."` to extend defaults: `disallowed-names = ["bar", ".."]`

## To Override Configuration Location:
1. Set `CLIPPY_CONF_DIR=/path/to/config/dir` before running `cargo clippy`
2. Clippy will search that directory first

## To Exclude Code from Clippy:
1. Preferred: `#[allow(clippy::all)]` on the item
2. Last resort: `#[cfg(not(clippy))]` with a stub implementation under `#[cfg(clippy)]`

# Context & Application

The `clippy.toml` file is useful for project-wide tuning of lint behavior that goes beyond simple enable/disable. For example, configuring which names are disallowed, setting thresholds for complexity lints, or controlling API-breaking lint behavior.

The directory walk-up behavior means monorepos can place a single `clippy.toml` at the repository root, and all nested crates will inherit it unless they provide their own override.

The `".."` extension syntax is particularly valuable for list-type configurations where you want to add project-specific entries without losing the sensible defaults (e.g., adding custom disallowed names on top of the built-in defaults).

# Examples

**Example 1**: Basic clippy.toml configuration:
```toml
avoid-breaking-exported-api = false
disallowed-names = ["toto", "tata", "titi"]
```

**Example 2**: Extending default list values with `".."`:
```toml
# default of disallowed-names is ["foo", "baz", "quux"]
disallowed-names = ["bar", ".."] # -> ["bar", "foo", "baz", "quux"]
```

**Example 3**: Conditionally excluding code from Clippy (last resort):
```rust
#[cfg(not(clippy))]
include!(concat!(env!("OUT_DIR"), "/my_big_function-generated.rs"));

#[cfg(clippy)]
fn my_big_function(_input: &str) -> Option<MyStruct> {
    None
}
```

**Example 4**: Overriding configuration directory via environment variable:
```bash
CLIPPY_CONF_DIR=/path/to/config cargo clippy
```

# Relationships

## Builds Upon
- **clippy** -- Configuration files tune Clippy's lint behavior
- **cargo-clippy** -- Configuration is loaded when Clippy runs

## Enables
- **clippy-msrv** -- The `msrv` setting is one of the configuration options in `clippy.toml`

## Related
- **clippy-lint-levels** -- Configuration files complement lint levels; levels control severity while config tunes behavior
- **clippy-lint-groups** -- Some configuration options affect lints within specific groups

# Common Errors

- **Error**: Naming the file `clippy.conf` or `clippy.cfg` instead of `clippy.toml`.
  **Correction**: The file must be named exactly `clippy.toml` or `.clippy.toml` (with the leading dot).

- **Error**: Replacing default list values when intending to extend them.
  **Correction**: Use `".."` in the list to extend defaults: `disallowed-names = ["my-name", ".."]` keeps the built-in defaults while adding `"my-name"`.

# Common Confusions

- **Confusion**: Thinking `clippy.toml` and `.clippy.toml` have different behaviors or precedences.
  **Clarification**: Both names are equivalent. Clippy looks for either name in the same directory. Use whichever naming convention your project prefers (the dot-prefixed form hides the file in Unix directory listings).

- **Confusion**: Expecting `clippy.toml` to support lint level configuration (allow/warn/deny).
  **Clarification**: `clippy.toml` only configures lint-specific parameters (thresholds, allowed names, etc.). Lint levels are configured via CLI flags, source attributes, or `Cargo.toml`'s `[lints.clippy]` section.

# Source Reference

Chapter 1 (Getting Started), "Configuring Clippy" section (lines 184-331 of 01-getting-started.md). Configuration file search priority at lines 188-198. The `".."` extension syntax at lines 210-218. Conditional compilation exclusion at lines 314-331.

# Verification Notes

- File names: Directly stated -- `clippy.toml` or `.clippy.toml`
- Search order: Three-step priority directly from source with directory walk-up behavior
- Unstable note: Directly quoted from source -- "The configuration file is unstable and may be deprecated in the future"
- Extension syntax: Example directly from source showing `["bar", ".."]` expanding defaults
- `CLIPPY_DISABLE_DOCS_LINKS`: Directly mentioned in source at line 220
- `cfg(not(clippy))`: Example directly from source with implementation stub pattern
- Confidence: HIGH -- all content directly from source documentation
- Cross-references: All slugs verified against planned extractions
