---
# === CORE IDENTIFICATION ===
concept: Clippy Lint Levels
slug: clippy-lint-levels

# === CLASSIFICATION ===
category: configuration
subcategory: null
tier: foundational

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
  - "allow warn deny forbid"
  - "lint severity"
  - "lint configuration"
  - "clippy allow"
  - "clippy deny"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
  - cargo-clippy
extends: []
related:
  - clippy-lint-groups
  - clippy-configuration
  - clippy-ci
  - lint-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the lint levels in Clippy?"
  - "How do I suppress a Clippy lint?"
  - "How do I make a Clippy lint an error?"
  - "What is the difference between allow, warn, deny, and forbid?"
  - "Where can I configure lint levels -- CLI, source, or Cargo.toml?"
  - "How do I scope a lint level to a single function or module?"
---

# Quick Definition

Clippy lint levels (`allow`, `warn`, `deny`, `forbid`) control the severity of lint violations, determining whether a lint is suppressed, emits a warning, causes an error, or is permanently locked as an error. Levels can be configured via command line flags, source code attributes, or `Cargo.toml`.

# Core Definition

Clippy uses the standard Rust lint level system with four levels:

- **allow** -- Suppresses the lint entirely; no output is produced
- **warn** -- The lint emits a warning but does not cause a build failure
- **deny** -- The lint emits an error, causing Clippy to exit with a non-zero code
- **forbid** -- Like `deny`, but cannot be overridden by downstream `allow` attributes

Lint levels can be configured in three places, each with different granularity:

1. **Command line flags**: `-A` (allow), `-W` (warn), `-D` (deny) passed after `--` to `cargo clippy`
2. **Source code attributes**: `#[allow(...)]`, `#[warn(...)]`, `#[deny(...)]` on items, modules, or crate-level with `#![...]`
3. **Cargo.toml**: The `[lints.clippy]` section for project-wide configuration

The source notes that `allow` means to suppress the lint, `warn` will only emit a warning, and `deny` will emit an error when triggered. An error causes Clippy to exit with a non-zero code, making it most useful in CI/CD scripts.

# Prerequisites

- **clippy** -- Lint levels configure Clippy's behavior
- **cargo-clippy** -- The primary interface through which lint level flags are passed

# Key Properties

1. Four lint levels: `allow` (suppress), `warn` (advisory), `deny` (error), `forbid` (locked error)
2. Command line flags use single-letter shorthand: `-A` (allow), `-W` (warn), `-D` (deny)
3. Source attributes can scope lint levels to the whole crate (`#![...]`), a module, or a single item (`#[...]`)
4. Clippy lint names use the `clippy::` prefix: `clippy::style`, `clippy::box_default`, etc.
5. The `[lints.clippy]` section in `Cargo.toml` provides a persistent, file-based way to set lint levels
6. `-D warnings` denies all warnings including rustc built-in warnings, not just Clippy lints
7. Lint levels can be applied to individual lints or to entire lint groups

# Construction / Recognition

## To Set Lint Levels via CLI:
1. Allow a lint: `cargo clippy -- -A clippy::lint_name`
2. Warn on a lint: `cargo clippy -- -W clippy::lint_name`
3. Deny a lint: `cargo clippy -- -D clippy::lint_name`
4. Deny all warnings: `cargo clippy -- -Dwarnings`

## To Set Lint Levels via Source Attributes:
1. Crate-level allow: `#![allow(clippy::style)]`
2. Item-level warn: `#[warn(clippy::box_default)]`
3. Item-level deny: `#[deny(clippy::single_match, clippy::box_vec)]`
4. Multiple lint groups: `#![warn(clippy::all, clippy::pedantic)]`

## To Set Lint Levels via Cargo.toml:
1. Add a `[lints.clippy]` section
2. Set individual lints: `enum_glob_use = "deny"`

# Context & Application

Lint level configuration is central to integrating Clippy into a project's workflow. The three configuration methods serve different use cases:

- **CLI flags** are best for one-off runs and CI pipelines where lint levels should be enforced globally
- **Source attributes** allow fine-grained, per-item control, which is ideal for allowing specific lints in code where they are intentionally violated
- **Cargo.toml** provides a project-wide default that lives in version control alongside the code

The documentation explicitly encourages using `#[allow(..)]` attributes throughout code. Clippy is designed to be opinionated, and suppressing lints that do not apply to a specific context is expected behavior.

# Examples

**Example 1**: Command line lint configuration with multiple levels:
```bash
cargo clippy -- -Aclippy::style -Wclippy::box_default -Dclippy::perf
```

**Example 2**: Source code attributes at crate and item level:
```rust
#![allow(clippy::style)]

#[warn(clippy::box_default)]
fn main() {
    let _ = Box::<String>::new(Default::default());
    // ^ warning: `Box::new(_)` of default value
}
```

**Example 3**: Allowing all lints and selectively enabling specific ones via CLI:
```bash
cargo clippy -- -A clippy::all -W clippy::useless_format -W clippy::needless_return
```

**Example 4**: Configuring lint levels in Cargo.toml:
```toml
[lints.clippy]
enum_glob_use = "deny"
```

**Example 5**: Denying all warnings for CI (affects both Clippy and rustc lints):
```bash
cargo clippy -- -Dwarnings
```

# Relationships

## Builds Upon
- **clippy** -- Lint levels configure Clippy's behavior
- **cargo-clippy** -- CLI flags are passed through `cargo clippy`

## Enables
- **clippy-ci** -- CI pipelines use `-Dwarnings` to enforce lint compliance
- **clippy-lint-groups** -- Lint levels can be applied to entire groups, not just individual lints

## Related
- **clippy-configuration** -- `clippy.toml` provides additional configuration beyond lint levels
- **lint-declaration** -- How lints are defined internally, including their default lint levels

# Common Errors

- **Error**: Using `-D warnings` and being surprised that `dead_code` and other rustc warnings also fail the build.
  **Correction**: `-D warnings` applies to all warnings from any source. If you only want to deny Clippy lints, use `-D clippy::all` or target specific groups.

- **Error**: Placing `#[allow(clippy::some_lint)]` at the crate level with `#[...]` instead of `#![...]`.
  **Correction**: Crate-level attributes require the inner attribute syntax with `!`: `#![allow(clippy::some_lint)]`.

# Common Confusions

- **Confusion**: Thinking `deny` and `forbid` are the same.
  **Clarification**: `deny` emits an error but can be overridden by a more specific `allow` attribute on an inner item. `forbid` cannot be overridden and locks the lint level.

- **Confusion**: Believing lint levels set in `Cargo.toml` override source code attributes.
  **Clarification**: Source code attributes (`#[allow(...)]`) take precedence over `Cargo.toml` settings, just as they do for rustc lints. `Cargo.toml` sets the baseline, and attributes provide local overrides.

# Source Reference

Chapter 1 (Getting Started), "Configuring Clippy" section, subsections "Allowing/Denying Lints" (lines 223-284 of 01-getting-started.md). Also "Lint configuration" under "Usage" (lines 47-80). Cargo.toml configuration at lines 272-284.

# Verification Notes

- Definition: The four lint levels (allow, warn, deny, forbid) are standard Rust lint levels applied to Clippy
- CLI flag syntax: Directly from source examples -- `-A`, `-W`, `-D` flags
- Source attribute syntax: Examples taken directly from the documentation
- Cargo.toml syntax: Directly from the source showing `[lints.clippy]` section
- Note about `-D warnings`: The source explicitly warns this includes rustc warnings
- Confidence: HIGH -- all content directly from source documentation
- Cross-references: All slugs verified against planned extractions
