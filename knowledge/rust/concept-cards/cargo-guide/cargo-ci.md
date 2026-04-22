---
# === CORE IDENTIFICATION ===
concept: Cargo CI Integration
slug: cargo-ci

# === CLASSIFICATION ===
category: ci-cd
subcategory: continuous-integration
tier: intermediate

# === PROVENANCE ===
source: "Cargo Guide"
source_slug: cargo-guide
authors: "The Cargo Team"
chapter: "08-continuous-integration"
chapter_number: 8
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cargo continuous integration"
  - "Rust CI"
  - "Cargo CI/CD"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-test-command
  - cargo-toml-vs-cargo-lock
extends: []
related:
  - cargo-publishing
  - cargo-build-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set up CI for a Cargo project?"
  - "What does a basic GitHub Actions workflow for Rust look like?"
  - "How do I test against multiple Rust toolchains in CI?"
  - "What is the CI configuration for GitLab CI, builds.sr.ht, and CircleCI?"
  - "How do I verify that my project works with the latest dependency versions?"
  - "How do I verify the correctness of my rust-version field?"
  - "What are the tradeoffs of different approaches to testing latest dependencies?"
---

# Quick Definition

Cargo projects integrate with CI systems through `cargo build --verbose` and `cargo test --verbose` as the core build-and-test steps. The guide provides ready-to-use configurations for GitHub Actions, GitLab CI, builds.sr.ht, and CircleCI, with patterns for testing across multiple toolchains (stable, beta, nightly) and strategies for verifying latest dependency compatibility.

# Core Definition

The source introduces CI integration with: "A basic CI will build and test your projects" (Ch. 8). The fundamental pattern is running `cargo build --verbose` and `cargo test --verbose` in a CI environment with Rust installed. The guide provides complete YAML configurations for four CI services.

A significant portion of the chapter addresses the problem of verifying latest dependencies, since `Cargo.toml` version requirements "generally match a range of versions" and exhaustive testing of all combinations is impractical. The source presents four strategies with tradeoffs: not checking in `Cargo.lock`, running a continue-on-failure CI job, scheduling periodic CI runs, and using dependency update bots like Dependabot or RenovateBot. A concrete GitHub Actions example demonstrates running `cargo update` before building to test against the latest compatible versions.

The chapter also covers verifying the `rust-version` field using third-party tools like `cargo-msrv` and `cargo-hack`.

# Prerequisites

- **Cargo Test Command** -- CI pipelines revolve around `cargo test`
- **Cargo.toml vs Cargo.lock** -- understanding lockfile behavior is essential for the "verifying latest dependencies" patterns

# Key Properties

1. **Core CI pattern**: `cargo build --verbose` followed by `cargo test --verbose`
2. **Multi-toolchain testing**: GitHub Actions uses a strategy matrix for stable, beta, and nightly
3. **Nightly allow-failure**: GitLab CI and builds.sr.ht show how to test nightly without failing the build
4. **Four CI services covered**: GitHub Actions, GitLab CI, builds.sr.ht, CircleCI
5. **Latest dependency verification**: Running `cargo update` before build/test to check compatibility
6. **CARGO_RESOLVER_INCOMPATIBLE_RUST_VERSIONS**: Environment variable to prevent the resolver from limiting dependency selection by Rust version
7. **rust-version verification**: Using `cargo-hack` to check `rust-version` correctness
8. **Dependency update strategies**: Not committing lockfile, continue-on-failure jobs, scheduled runs, or bots (Dependabot, RenovateBot)

# Construction / Recognition

## GitHub Actions (`.github/workflows/ci.yml`):
```yaml
name: Cargo Build & Test

on:
  push:
  pull_request:

env: 
  CARGO_TERM_COLOR: always

jobs:
  build_and_test:
    name: Rust project - latest
    runs-on: ubuntu-latest
    strategy:
      matrix:
        toolchain:
          - stable
          - beta
          - nightly
    steps:
      - uses: actions/checkout@v4
      - run: rustup update ${{ matrix.toolchain }} && rustup default ${{ matrix.toolchain }}
      - run: cargo build --verbose
      - run: cargo test --verbose
```

## GitLab CI (`.gitlab-ci.yml`):
```yaml
stages:
  - build

rust-latest:
  stage: build
  image: rust:latest
  script:
    - cargo build --verbose
    - cargo test --verbose

rust-nightly:
  stage: build
  image: rustlang/rust:nightly
  script:
    - cargo build --verbose
    - cargo test --verbose
  allow_failure: true
```

## Latest Dependencies Verification (GitHub Actions):
```yaml
jobs:
  latest_deps:
    name: Latest Dependencies
    runs-on: ubuntu-latest
    continue-on-error: true
    env:
      CARGO_RESOLVER_INCOMPATIBLE_RUST_VERSIONS: allow
    steps:
      - uses: actions/checkout@v4
      - run: rustup update stable && rustup default stable
      - run: cargo update --verbose
      - run: cargo build --verbose
      - run: cargo test --verbose
```

# Context & Application

This chapter provides practical, copy-paste CI configurations for the major CI services. The multi-toolchain matrix pattern ensures projects work on stable Rust while also catching potential issues in beta and nightly without blocking releases. The "verifying latest dependencies" section is particularly valuable because it addresses a real-world challenge: how to balance deterministic builds (via `Cargo.lock`) with staying current on dependencies. The source evaluates four approaches with their tradeoffs, making it clear there is no single right answer. This card complements the lockfile card by showing how CI strategies interact with lockfile management.

# Examples

**Example 1** (Ch. 8): builds.sr.ht configuration (`.build.yml`) showing stable and nightly testing with documentation:
```yaml
image: archlinux
packages:
  - rustup
sources:
  - <your repo>
tasks:
  - setup: |
      rustup toolchain install nightly stable
      cd <your project>/
      rustup run stable cargo fetch
  - stable: |
      rustup default stable
      cd <your project>/
      cargo build --verbose
      cargo test --verbose
  - nightly: |
      rustup default nightly
      cd <your project>/
      cargo build --verbose ||:
      cargo test --verbose  ||:
  - docs: |
      cd <your project>/
      rustup run stable cargo doc --no-deps
      rustup run nightly cargo doc --no-deps ||:
```

**Example 2** (Ch. 8): CircleCI configuration:
```yaml
version: 2.1
jobs:
  build:
    docker:
      - image: cimg/rust:1.77.2
    steps:
      - checkout
      - run: cargo test
```

**Example 3** (Ch. 8): Considerations for testing latest dependency versions:
> "When testing the latest versions some considerations are:
> - Minimizing external factors affecting local development or CI
> - Rate of new dependencies being published
> - Level of risk a project is willing to accept
> - CI costs, including indirect costs like if a CI service has a maximum for parallel runners"

**Example 4** (Ch. 8): Verifying `rust-version` with cargo-hack:
```yaml
jobs:
  msrv:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: taiki-e/install-action@cargo-hack
    - run: cargo hack check --rust-version --workspace --all-targets --ignore-private
```

# Relationships

## Builds Upon
- **Cargo Test Command** -- `cargo test --verbose` is the central CI step
- **Cargo.toml vs Cargo.lock** -- lockfile management directly affects CI strategy for dependency verification

## Enables
- **cargo-publishing** -- CI verification is typically a prerequisite before publishing

## Related
- **cargo-build-performance** -- CI build times can be reduced with caching and build optimization techniques

## Contrasts With
- None within this source

# Common Errors

- **Error**: Not enabling color output, leading to hard-to-read CI logs.
  **Correction**: Set `CARGO_TERM_COLOR: always` as shown in the GitHub Actions example.

- **Error**: Having nightly failures block the entire CI pipeline.
  **Correction**: Use `allow_failure: true` (GitLab), `continue-on-error: true` (GitHub Actions), or `||:` (builds.sr.ht) for nightly jobs.

- **Error**: Running `cargo update` in the main CI job, causing non-deterministic builds.
  **Correction**: Keep the latest-deps verification as a separate job with `continue-on-error: true`, not part of the primary build pipeline.

# Common Confusions

- **Confusion**: Thinking CI should always test with the very latest dependencies.
  **Clarification**: The source presents four approaches with different tradeoffs. The primary CI job should typically use `Cargo.lock` for determinism, with a separate optional job for testing latest versions.

- **Confusion**: Thinking `cargo-hack check --rust-version` tests runtime behavior.
  **Clarification**: As the source explains, "`cargo check` is used as most issues contributors will run into are API availability and not behavior."

- **Confusion**: Thinking not committing `Cargo.lock` is the best way to test latest dependencies.
  **Clarification**: The source notes this "comes at the cost of determinism" and "depending on PR velocity, many versions may go untested." Other approaches offer better tradeoffs.

# Source Reference

Chapter 8: Continuous Integration -- sections "Getting Started" (GitHub Actions, GitLab CI, builds.sr.ht, CircleCI), "Verifying Latest Dependencies," and "Verifying `rust-version`." No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 8 -- "A basic CI will build and test your projects"
- Confidence rationale: HIGH -- the source provides complete, ready-to-use CI configurations with clear explanations
- Uncertainties: CI caching strategies (for `$CARGO_HOME` or `target/`) are not covered in this chapter (see the cargo-home card)
- Cross-reference status: All slugs reference cards within this extraction set
