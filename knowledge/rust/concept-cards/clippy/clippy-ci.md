---
# === CORE IDENTIFICATION ===
concept: Clippy CI/CD Integration
slug: clippy-ci

# === CLASSIFICATION ===
category: ci-cd
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "02-cicd"
chapter_number: 2
pdf_page: null
section: "Continuous Integration"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "clippy CI"
  - "clippy continuous integration"
  - "clippy GitHub Actions"
  - "clippy GitLab CI"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
  - cargo-clippy
  - clippy-lint-levels
extends: []
related:
  - clippy-lint-groups
  - clippy-configuration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I run Clippy in CI?"
  - "How do I make Clippy fail the CI build on warnings?"
  - "How do I set up Clippy in GitHub Actions?"
  - "How do I set up Clippy in GitLab CI?"
  - "How do I set up Clippy in Travis CI?"
  - "Which Rust toolchain should I use for Clippy in CI?"
  - "What is RUSTFLAGS=-Dwarnings?"
---

# Quick Definition

Clippy is commonly run in CI/CD pipelines with `-Dwarnings` to ensure lint violations prevent builds from passing. The documentation provides ready-to-use configurations for GitHub Actions, GitLab CI, and Travis CI.

# Core Definition

Running Clippy in CI is recommended with `-Dwarnings` so that Clippy lint violations cause the build to fail with a non-zero exit code. This can be done either by passing `-D warnings` after `--` to `cargo clippy`, or by setting the environment variable `RUSTFLAGS="-Dwarnings"` which applies to all cargo commands.

Two key recommendations from the documentation:

1. **Use the same toolchain for Clippy and compilation**: Use stable Clippy for stable-compiled crates, nightly Clippy for nightly-compiled crates. This ensures maximum compatibility.
2. **Consider adding nightly Clippy**: New lints are first added to the nightly toolchain. Running nightly Clippy in CI (as an optional, non-blocking check) helps the Clippy project find and fix bugs before they reach stable.

Each CI provider has a slightly different setup, but the core pattern is the same: install Clippy (if not pre-installed), set `RUSTFLAGS="-Dwarnings"`, and run `cargo clippy --all-targets --all-features`.

# Prerequisites

- **clippy** -- Clippy must be available on the CI runner
- **cargo-clippy** -- The `cargo clippy` command is what CI invokes
- **clippy-lint-levels** -- Understanding `-Dwarnings` and how lint levels work

# Key Properties

1. `-Dwarnings` makes all warnings (including Clippy lints) into errors, failing the build
2. `RUSTFLAGS="-Dwarnings"` applies deny-warnings globally to all cargo commands
3. Use the same Rust toolchain for Clippy as for compilation (stable with stable, nightly with nightly)
4. GitHub hosted runners have Clippy pre-installed with the latest stable Rust
5. GitLab CI uses the `rust:latest` Docker image and requires `rustup component add clippy`
6. Travis CI requires explicit `rustup component add clippy` in `before_script`
7. `--all-targets --all-features` ensures comprehensive lint coverage in CI

# Construction / Recognition

## To Set Up Clippy in CI:
1. Ensure Clippy is installed (pre-installed on GitHub runners, needs explicit install elsewhere)
2. Set `RUSTFLAGS="-Dwarnings"` or pass `-D warnings` after `--`
3. Run `cargo clippy --all-targets --all-features`

## To Recognize Clippy CI Configuration:
1. Look for `cargo clippy` in CI workflow files
2. Look for `RUSTFLAGS: "-Dwarnings"` in environment configuration
3. Look for `rustup component add clippy` in setup steps

# Context & Application

Integrating Clippy into CI ensures that code quality standards are enforced automatically before code is merged. The `-Dwarnings` pattern is the standard approach, converting all lint warnings into build-breaking errors.

The recommendation to match toolchains is important because Clippy lints can vary between stable and nightly. Running stable Clippy on nightly-only code (or vice versa) can produce false positives or miss lints.

For teams that want to contribute to the Clippy ecosystem, running nightly Clippy as a non-blocking CI check helps identify false positives and bugs early, before they reach stable users.

# Examples

**Example 1**: GitHub Actions configuration:
```yml
on: push
name: Clippy check

# Make sure CI fails on all warnings, including Clippy lints
env:
  RUSTFLAGS: "-Dwarnings"

jobs:
  clippy_check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Run Clippy
        run: cargo clippy --all-targets --all-features
```

**Example 2**: GitLab CI configuration:
```yml
# Make sure CI fails on all warnings, including Clippy lints
variables:
  RUSTFLAGS: "-Dwarnings"

clippy_check:
  image: rust:latest
  script:
    - rustup component add clippy
    - cargo clippy --all-targets --all-features
```

**Example 3**: Travis CI configuration:
```yml
language: rust
rust:
  - stable
  - beta
before_script:
  - rustup component add clippy
script:
  - cargo clippy --all-targets --all-features -- -D warnings
  - cargo test
```

# Relationships

## Builds Upon
- **clippy** -- CI runs the Clippy tool
- **cargo-clippy** -- CI invokes `cargo clippy`
- **clippy-lint-levels** -- `-Dwarnings` uses the deny lint level

## Related
- **clippy-lint-groups** -- CI typically runs with `clippy::all` (the default) and optionally additional groups
- **clippy-configuration** -- A `clippy.toml` in the repository is automatically picked up during CI runs

# Common Errors

- **Error**: Not installing Clippy explicitly in GitLab CI or Travis CI and getting a "subcommand not found" error.
  **Correction**: Unlike GitHub hosted runners, other CI environments may not have Clippy pre-installed. Add `rustup component add clippy` to the setup step.

- **Error**: Using `RUSTFLAGS="-Dwarnings"` and finding that dependency crate warnings also fail the build.
  **Correction**: `RUSTFLAGS` applies to all compilations including dependencies. If this is too strict, pass `-D warnings` only to `cargo clippy -- -Dwarnings` instead.

# Common Confusions

- **Confusion**: Thinking `RUSTFLAGS="-Dwarnings"` only affects Clippy lints.
  **Clarification**: `RUSTFLAGS` applies to the entire Rust compiler invocation. This means all `rustc` warnings (dead code, unused variables, etc.) also become errors, not just Clippy lints.

- **Confusion**: Believing nightly Clippy is required for CI.
  **Clarification**: Stable Clippy is recommended for CI. The documentation suggests nightly Clippy only as an optional, additional check to help the Clippy project catch bugs early.

# Source Reference

Chapter 2 (CI/CD), all sections of 02-cicd.md. "Continuous Integration" introduction at lines 1-18. GitHub Actions at lines 22-43. GitLab CI at lines 47-63. Travis CI at lines 67-88.

# Verification Notes

- `-Dwarnings` recommendation: Directly from source -- "run Clippy on CI with -Dwarnings"
- `RUSTFLAGS` approach: Directly from source -- "set the env var RUSTFLAGS=\"-Dwarnings\""
- Toolchain matching: Directly from source -- "use Clippy from the same toolchain, that you use for compiling"
- Nightly recommendation: Directly from source about helping with bug reports
- All three CI configurations: Directly from source YAML examples
- GitHub pre-installed: Directly stated -- "GitHub hosted runners using the latest stable version of Rust have Clippy pre-installed"
- Confidence: HIGH -- all CI configurations and recommendations directly from source
- Cross-references: All slugs verified against planned extractions
