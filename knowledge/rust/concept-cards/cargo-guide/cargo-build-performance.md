---
# === CORE IDENTIFICATION ===
concept: Cargo Build Performance
slug: cargo-build-performance

# === CLASSIFICATION ===
category: performance
subcategory: build-optimization
tier: advanced

# === PROVENANCE ===
source: "Cargo Guide"
source_slug: cargo-guide
authors: "The Cargo Team"
chapter: "11-build-performance"
chapter_number: 11
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "build optimization"
  - "Cargo build speed"
  - "optimizing Rust compile times"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - creating-a-cargo-project
  - cargo-project-layout
  - cargo-toml-vs-cargo-lock
extends: []
related:
  - cargo-ci
  - cargo-home
  - cargo-test-command
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can I speed up Cargo builds?"
  - "What debug information settings reduce build times?"
  - "What is the Cranelift codegen backend and how does it help?"
  - "How do I use an alternative linker like mold or LLD?"
  - "What is the parallel frontend and how do I enable it?"
  - "How do I remove unused dependencies to improve build times?"
  - "What are the tradeoffs of each build performance technique?"
  - "Where can I override Cargo defaults for build performance?"
---

# Quick Definition

Cargo build performance can be optimized through configuration and code organization changes. Key techniques include reducing debug information in the dev profile, using the Cranelift codegen backend, enabling the parallel compiler frontend, switching to a faster linker (mold, LLD, wild), resolving features for the whole workspace, and removing unused dependencies and features. Each technique involves specific tradeoffs.

# Core Definition

The source states: "Cargo configuration options and source code organization patterns can help improve build performance, by prioritizing it over other aspects which may not be as important for your circumstances." (Ch. 11). The chapter emphasizes measurement: "be sure to measure these changes against the workflows you actually care about" since "some of these approaches might actually make build performance worse for your use-case."

The source identifies three configuration locations: `Cargo.toml` (available to all contributors), `$WORKSPACE_ROOT/.cargo/config.toml` (available to all contributors but path-sensitive), and `$CARGO_HOME/.cargo/config.toml` (per-developer defaults). It then presents six categories of optimization, each with a recommendation, configuration example, and explicit tradeoff analysis.

The workflows to optimize include: compiler feedback during development (`cargo check`), test feedback (`cargo test`), and CI builds.

# Prerequisites

- **Creating a Cargo Project** -- a project must exist before optimizing its build
- **Cargo Project Layout** -- understanding project structure for workspace organization
- **Cargo.toml vs Cargo.lock** -- understanding `Cargo.toml` profiles and configuration

# Key Properties

1. **Measure before optimizing**: The source warns that optimizations can be counterproductive for specific use cases
2. **Three configuration locations**: `Cargo.toml`, workspace `.cargo/config.toml`, and `$CARGO_HOME/.cargo/config.toml`
3. **Reduce debug info**: `debug = "line-tables-only"` for workspace, `debug = false` for dependencies
4. **Cranelift backend**: Faster code generation but requires nightly and produces slower runtime code
5. **Parallel frontend**: `-Zthreads=8` enables multi-threaded compilation (nightly only)
6. **Alternative linkers**: mold, LLD, or wild can significantly reduce link times
7. **Workspace feature unification**: `feature-unification = "workspace"` reduces rebuilds (nightly only)
8. **Remove unused dependencies**: Tools like cargo-machete, cargo-udeps, cargo-shear
9. **Remove unused features**: Tools like cargo-features-manager, cargo-unused-features
10. **Custom debugging profile**: Create a `[profile.debugging]` that inherits from `dev` with full debug info

# Construction / Recognition

## Reducing Debug Information:
```toml
[profile.dev]
debug = "line-tables-only"

[profile.dev.package."*"]
debug = false

[profile.debugging]
inherits = "dev"
debug = true
```

## Using Cranelift Backend (nightly):
```console
$ rustup component add rustc-codegen-cranelift-preview --toolchain nightly
```
```toml
[profile.dev]
codegen-backend = "cranelift"
```

## Enabling Parallel Frontend (nightly):
```toml
[build]
rustflags = "-Zthreads=8"
```

## Alternative Linker (mold on Linux):
```toml
[target.'cfg(target_os = "linux")']
# mold, if you have GCC 12+
rustflags = ["-C", "link-arg=-fuse-ld=mold"]
```

## Workspace Feature Unification (nightly):
```toml
[resolver]
feature-unification = "workspace"
```

# Context & Application

This chapter provides a comprehensive guide to build performance optimization that goes beyond simple tips. Each technique is presented with explicit tradeoffs (marked with checkmarks and crosses), making it clear that build speed comes at the cost of other properties (debug quality, runtime performance, stability, or Rust version requirements). Many of the most effective techniques (Cranelift, parallel frontend, feature unification) require nightly Rust, which limits their applicability in production environments. The emphasis on measurement and workflow-specific optimization makes this a practical reference rather than a prescriptive checklist.

# Examples

**Example 1** (Ch. 11): Debug info reduction tradeoffs:
> Trade-offs:
> - Faster code generation (`cargo build`)
> - Faster link times
> - Smaller disk usage of the `target` directory
> - Requires a full rebuild to have a high-quality debugger experience

**Example 2** (Ch. 11): Parallel frontend threading recommendation:
> "The value of `n` should be chosen according to the number of cores available on your system, although there are diminishing returns. We recommend using at most `8` threads."

**Example 3** (Ch. 11): Why linking can dominate build times:
> "While dependencies may be built in parallel, linking all of your dependencies happens at once at the end of your build, which can make linking dominate your build times, especially for incremental rebuilds."

**Example 4** (Ch. 11): Removing unused dependencies:
> "When changing code, it can be easy to miss that a dependency is no longer used and can be removed."
The source recommends periodically reviewing with tools like cargo-machete, cargo-udeps, or cargo-shear.

**Example 5** (Ch. 11): Feature unification benefit:
> "you may need to build and test various packages within the application, which can cause extraneous rebuilds because different sets of features may be activated for common dependencies."

# Relationships

## Builds Upon
- **Creating a Cargo Project** -- build performance applies to existing projects
- **Cargo Project Layout** -- workspace organization affects build performance
- **Cargo.toml vs Cargo.lock** -- profiles and configuration are specified in `Cargo.toml`

## Enables
- Faster development iteration cycles
- Faster CI builds

## Related
- **cargo-ci** -- CI builds are one of the three workflows to optimize
- **cargo-home** -- cache management in the Cargo home affects build performance
- **cargo-test-command** -- `cargo test` is one of the workflows to optimize

## Contrasts With
- None within this source

# Common Errors

- **Error**: Applying all optimizations blindly without measuring impact.
  **Correction**: "Be sure to measure these changes against the workflows you actually care about... some of these approaches might actually make build performance worse for your use-case."

- **Error**: Using Cranelift or parallel frontend on stable Rust.
  **Correction**: Both require nightly Rust and unstable features. Cranelift needs `-Z codegen-backend` and parallel frontend needs `-Zthreads`.

- **Error**: Configuring mold linker in `Cargo.toml` expecting it to work on all platforms.
  **Correction**: The mold configuration is Linux-specific. Use `[target.'cfg(target_os = "linux")']` to scope it properly.

- **Error**: Removing dependency features without checking for behavioral impact.
  **Correction**: "Extra caution is needed because features may also be used for desired behavior or performance changes which may not always be obvious from compiling or testing."

# Common Confusions

- **Confusion**: Thinking `debug = false` means no debugging is possible.
  **Clarification**: The source creates a `[profile.debugging]` that inherits from dev with `debug = true` as an opt-in: "Provide an opt-in for when debugging via `--profile debugging`."

- **Confusion**: Thinking alternative linkers always help.
  **Clarification**: "Often, the linker Rust uses is already fairly fast and the gains from switching may not be worth it, but it is not always the case." The benefit depends on platform and project characteristics.

- **Confusion**: Thinking workspace `.cargo/config.toml` behaves identically to `Cargo.toml`.
  **Clarification**: "Unlike `Cargo.toml`, this is sensitive to what directory you invoke `cargo` from." The behavior depends on the current working directory.

- **Confusion**: Thinking feature-unification has no downsides.
  **Clarification**: "A package activating a feature can mask bugs in other packages that should activate it but don't." Feature unification trades correctness for build speed.

# Source Reference

Chapter 11: Optimizing Build Performance -- sections "Cargo and Compiler Configuration" (debug info, Cranelift, parallel frontend, alternative linker, feature unification) and "Reducing Built Code" (unused dependencies, unused features). No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 11 -- "Cargo configuration options and source code organization patterns can help improve build performance"
- Confidence rationale: HIGH -- the source provides specific configuration examples with explicit tradeoff analysis for each technique
- Uncertainties: Nightly-only features may stabilize or change; the source notes several open tracking issues (e.g., #15931, #12738, #15813)
- Cross-reference status: All slugs reference cards within this extraction set
