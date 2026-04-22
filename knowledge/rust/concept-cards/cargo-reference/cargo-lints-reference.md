---
# === CORE IDENTIFICATION ===
concept: Cargo Lints Reference
slug: cargo-lints-reference

# === CLASSIFICATION ===
category: tooling
subcategory: diagnostics
tier: intermediate

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "16-lints"
chapter_number: 16
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cargo lints"
  - "Cargo lint system"
  - "[lints.cargo] table"
  - "Cargo-specific lints"
  - "Cargo diagnostics"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - creating-a-cargo-project
  - cargo-dependencies
extends: []
related:
  - cargo-semver-compatibility
  - cargo-unstable-features
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What lints does Cargo provide for Cargo.toml?"
  - "How do I configure Cargo lints in my project?"
  - "What lint groups does Cargo define?"
  - "How do I detect unused dependencies with Cargo lints?"
  - "What is the future-incompat report and how do I use it?"
  - "How do I view build timing information?"
  - "What does the unused_workspace_dependencies lint check?"
  - "How do I inherit workspace lints in a package?"
  - "What naming convention lints does Cargo provide?"
---

# Quick Definition

Cargo provides its own lint system (currently unstable, requiring nightly) for checking `Cargo.toml` manifests. Lints are organized into eight groups (complexity, correctness, nursery, pedantic, perf, restriction, style, suspicious) with varying default levels. Key lints detect unused dependencies, unused workspace fields, naming convention violations, redundant metadata, and unknown lint names. Additionally, Cargo provides two stabilized diagnostic features: future incompatibility reports (which warn about dependency code that will break in future Rust versions) and build timing reports (which produce HTML visualizations of compilation concurrency and duration).

# Core Definition

The Cargo lint system is configured through the `[lints.cargo]` table in `Cargo.toml`, following the same pattern as `[lints.rust]` and `[lints.clippy]`. Workspace-level lints can be defined in `[workspace.lints.cargo]` and inherited by member packages via `[lints] workspace = true`.

The source defines eight lint groups: `cargo::correctness` (default: deny), `cargo::complexity` (default: warn), `cargo::perf` (default: warn), `cargo::style` (default: warn), `cargo::suspicious` (default: warn), `cargo::pedantic` (default: allow), `cargo::restriction` (default: allow), and `cargo::nursery` (default: allow).

**Future incompatibility reports** (Ch. 14) are a stabilized feature where "Cargo checks for future-incompatible warnings in all dependencies. These are warnings for changes that may become hard errors in the future." Reports can be viewed via `cargo report future-incompatibilities --id ID` or by building with `--future-incompat-report`. The frequency of these notices is controlled by `[future-incompat-report] frequency` in `.cargo/config.toml`.

**Build timings** (Ch. 15) are a stabilized feature invoked with `cargo build --timings`, producing an HTML report in `target/cargo-timings/` with unit-level duration graphs, concurrency visualization, and codegen timing breakdowns.

# Prerequisites

- **Creating a Cargo Project** -- lints apply to `Cargo.toml` in existing projects
- **Cargo Dependencies** -- many lints check dependency declarations and features

# Key Properties

1. **Currently unstable**: The lint system requires nightly and `-Zcargo-lints` to use
2. **Eight lint groups** with different default levels: correctness (deny), complexity/perf/style/suspicious (warn), pedantic/restriction/nursery (allow)
3. **`unused_dependencies`** (warn): Detects dependencies not used by any Cargo targets; has limitations with dev-dependencies and cross-package checking
4. **`unused_workspace_dependencies`** (warn): Flags `[workspace.dependencies]` entries that no package has inherited
5. **`unused_workspace_package_fields`** (warn): Flags `[workspace.package]` fields that no package has inherited
6. **`missing_lints_inheritance`** (warn): Catches packages that forgot to set `[lints] workspace = true` when `[workspace.lints]` exists
7. **`unknown_lints`** (warn): Detects misspelled or non-existent lint names in `[lints.cargo]`
8. **Naming convention lints**: `non_kebab_case_bins` (warn), plus allow-by-default `non_kebab_case_features`, `non_kebab_case_packages`, `non_snake_case_features`, `non_snake_case_packages`
9. **`implicit_minimum_version_req`** (allow, pedantic): Flags version requirements like `serde = "1"` that should be `serde = "1.0.219"` for clarity
10. **`blanket_hint_mostly_unused`** (warn): Catches misapplication of `hint-mostly-unused = true` to all packages via wildcard

# Construction / Recognition

## Configuring Cargo Lints:
```toml
# In Cargo.toml
[lints.cargo]
unused_dependencies = "warn"
implicit_minimum_version_req = "warn"
```

## Workspace Lint Inheritance:
```toml
# In workspace root Cargo.toml
[workspace.lints.cargo]
unused_dependencies = "warn"

# In member Cargo.toml
[lints]
workspace = true
```

## Suppressing a Specific Lint:
```toml
[lints.cargo]
non_kebab_case_bins = "allow"
```

## Configuring `unused_dependencies` Ignores:
```toml
[lints.cargo]
unused_dependencies = { level = "warn", ignore = ["pinned-transitive-dep"] }
```

## Viewing Future Incompatibility Reports:
```console
$ cargo build
warning: the following packages contain code that will be rejected by a future
         version of Rust: rental v0.5.5
note: to see what the problems were, use the option `--future-incompat-report`

$ cargo report future-incompatibilities --id 1
```

## Configuring Future Incompat Frequency:
```toml
# .cargo/config.toml
[future-incompat-report]
frequency = "always"  # or "never"
```

## Generating Build Timing Reports:
```console
$ cargo build --timings
# Produces target/cargo-timings/cargo-timing.html
```

# Context & Application

The Cargo lint system fills an important gap between Rust compiler lints (which check code) and Clippy lints (which check code patterns) by providing lints specifically for `Cargo.toml` manifests and project configuration. The `unused_dependencies` lint is particularly valuable for maintaining clean dependency graphs, though the source is careful to document its limitations: it cannot check dev-dependencies without building all relevant targets, it has false positives with transitive dependency pinning, and it only checks selected packages. The future-incompat report and build timings features, though small in scope, are already stabilized and provide essential project maintenance capabilities -- the former for proactive dependency health monitoring, the latter for diagnosing build performance bottlenecks through its unit-level timing graphs, concurrency visualization, and codegen timing breakdown.

# Examples

**Example 1** (Ch. 16): The `unused_dependencies` lint detection scope:
> "cargo check will lint [build-dependencies] and [dependencies]"
> "cargo check --all-targets will still only lint [build-dependencies] and [dependencies] and not [dev-dependencies]"
Note: There is no way to select all cargo targets that use `[dev-dependencies]`, so they remain unchecked.

**Example 2** (Ch. 16): The `implicit_minimum_version_req` lint rationale:
> "Version requirements without an explicit full version can be misleading about the actual minimum supported version. For example, serde = '1' has an implicit minimum bound of 1.0.0. If your code actually requires features from 1.0.219, the implicit minimum bound of 1.0.0 gives a false impression about compatibility."

**Example 3** (Ch. 16): The `missing_lints_inheritance` lint:
> "Many people mistakenly think that workspace.lints is implicitly inherited when it is not."

**Example 4** (Ch. 14): Future incompat report usage:
> "A full report can be displayed with the cargo report future-incompatibilities --id ID command, or by running the build again with the --future-incompat-report flag. The developer should then update their dependencies to a version where the issue is fixed."

**Example 5** (Ch. 15): Tips for addressing build times from the timings report:
> "Look for slow dependencies... Look for a crate being built multiple times with different versions... Split large crates into smaller pieces... If there are a large number of crates bottlenecked on a single crate, focus your attention on improving that one crate to improve parallelism."

# Relationships

## Builds Upon
- **Creating a Cargo Project** -- lints apply to `Cargo.toml` manifests
- **Cargo Dependencies** -- several lints check dependency usage and configuration

## Enables
- Cleaner dependency graphs through unused dependency detection
- Consistent naming conventions across workspaces
- Proactive response to future Rust compatibility changes
- Build performance diagnosis through timing reports

## Related
- **cargo-semver-compatibility** -- SemVer rules inform why clean dependency management matters
- **cargo-unstable-features** -- the lint system itself is currently an unstable feature enabled via `-Zcargo-lints`

## Contrasts With
- None within this source

# Common Errors

- **Error**: Expecting `[workspace.lints.cargo]` to automatically apply to all workspace members.
  **Correction**: Each member package must explicitly opt in with `[lints] workspace = true`. The `missing_lints_inheritance` lint catches this mistake.

- **Error**: Expecting `unused_dependencies` to catch unused dev-dependencies.
  **Correction**: "As there is no way to select all cargo targets that use [dev-dependencies], they are unchecked." Only `[dependencies]` and `[build-dependencies]` are linted.

- **Error**: Applying `hint-mostly-unused = true` globally via `[profile.dev.package."*"]`.
  **Correction**: The `blanket_hint_mostly_unused` lint warns that "Misapplication to crates that don't fit that criteria will slow down the build rather than speeding it up. It should be selectively applied."

- **Error**: Using Cargo lints on stable Rust.
  **Correction**: "Cargo's linting system is unstable and can only be used on nightly toolchains" with the `-Zcargo-lints` flag.

# Common Confusions

- **Confusion**: Thinking Cargo lints and Clippy lints are the same system.
  **Clarification**: Cargo lints check `Cargo.toml` manifests (dependency usage, naming, workspace configuration). Clippy lints check Rust source code. Both use the `[lints]` table but under different tool prefixes: `[lints.cargo]` vs `[lints.clippy]`.

- **Confusion**: Thinking `unused_dependencies` has no false positives.
  **Clarification**: "There can be false positives when depending on a transitive dependency to activate a feature." For false positives from pinning, move the dependency to the `target."cfg(false)".dependencies` table.

- **Confusion**: Thinking the future-incompat report requires nightly.
  **Clarification**: Future incompatibility reports are a stabilized feature (since Rust 1.59). They work on stable Rust and are displayed automatically at the end of builds.

- **Confusion**: Thinking `--timings` requires nightly.
  **Clarification**: The `--timings` flag was stabilized in Rust 1.60. The unstable part (`-Zsection-timings`) extends it with per-section compiler timing data.

# Source Reference

Chapter 16: Lints -- all lint group definitions and individual lint descriptions. Chapter 14: Future incompat report -- configuration and usage. Chapter 15: Timings -- `--timings` flag, HTML report structure, graph interpretation, and optimization tips. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 16 lint group table and individual lint descriptions; Ch. 14 and Ch. 15 opening sections
- Confidence rationale: HIGH -- all lints have explicit descriptions, default levels, and code examples directly from the source
- Uncertainties: The Cargo lint system is unstable and may change before stabilization; specific lints may be added or removed. Ch. 14/15 content is stable.
- Cross-reference status: Prerequisites reference cards from other extraction sets; related cards are within this extraction set
