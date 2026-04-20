---
concept: Deno in CI
slug: deno-in-ci
category: platform
subcategory: continuous integration
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/continuous_integration.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Deno CI/CD"
  - "Deno continuous integration"
  - "Deno GitHub Actions"
prerequisites:
  - deno-cli
extends: []
related:
  - deno-stability-and-releases
  - deno-in-docker
contrasts_with: []
answers_questions:
  - "How do I set up CI for a Deno project?"
  - "How do I cache Deno dependencies in CI?"
  - "How do I run Deno tests across multiple platforms?"
---

# Quick Definition

Deno's built-in tools (`deno test`, `deno lint`, `deno fmt`, `deno coverage`) integrate directly into CI pipelines, with official GitHub Actions support via `denoland/setup-deno@v2` including dependency caching.

# Core Definition

"Deno's built-in tools make it easy to set up Continuous Integration (CI) pipelines for your projects. Testing, linting and formatting your code can all be done with the corresponding commands `deno test`, `deno lint` and `deno fmt`. In addition, you can generate code coverage reports from test results with `deno coverage` in pipelines."

A basic GitHub Actions pipeline involves checking out the repository and installing Deno via `denoland/setup-deno@v2`. GitHub provides an official starter workflow for Deno. The concepts apply to other CI providers (Azure Pipelines, CircleCI, GitLab).

# Prerequisites

- **deno-cli** -- CI pipelines invoke Deno CLI subcommands.

# Key Properties

1. **Official GitHub Actions setup** -- `denoland/setup-deno@v2` installs Deno with version pinning and optional caching.
2. **Built-in toolchain** -- No additional CI tooling needed; `deno fmt --check`, `deno lint`, `deno test`, and `deno coverage` are all built-in.
3. **Dependency caching** -- `cache: true` on `setup-deno` preserves dependencies between runs, keyed by `deno.lock`.
4. **Cross-platform matrix** -- Matrix strategy across `ubuntu-latest`, `macos-latest`, `windows-latest`.
5. **Canary testing** -- Include a canary Deno version in the matrix to catch breaking changes early.
6. **Coverage reports** -- `deno coverage --lcov` generates reports compatible with Codecov, Coveralls, etc.

# Construction / Recognition

## Basic GitHub Actions workflow:
```yaml
name: Build
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: denoland/setup-deno@v2
        with:
          deno-version: v2.x
      - run: deno fmt --check
      - run: deno lint
      - run: deno test --allow-all --coverage=cov/
      - run: deno coverage --lcov cov/ > cov.lcov
```

## With caching enabled:
```yaml
- uses: denoland/setup-deno@v2
  with:
    cache: true
```

## Cross-platform matrix:
```yaml
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
```

# Context & Application

- **Open-source projects**: Standard CI setup for Deno projects on GitHub.
- **Enterprise**: LTS version pinning and caching for stable pipelines.
- **Quality gates**: Enforce formatting, linting, type checking, and test coverage in PRs.

# Examples

**Example 1** (from source): Conditional coverage upload (Linux only).
```yaml
- name: Generate coverage report
  if: matrix.os == 'ubuntu-latest'
  run: deno coverage --lcov cov > cov.lcov
```
(Section: "Reducing repetition")

**Example 2** (from source): Caching with custom hash key.
```yaml
- uses: denoland/setup-deno@v2
  with:
    cache-hash: ${{ hashFiles('**/deno.json') }}
```
(Section: "Caching dependencies")

**Example 3** (from source): Including canary in the test matrix.
```yaml
include:
  - deno-version: canary
    os: ubuntu-latest
    canary: true
```
(Section: "Cross-platform workflows")

# Relationships

## Builds Upon
- **deno-cli** -- CI pipelines are sequences of Deno CLI commands.

## Enables
- Automated quality assurance (formatting, linting, testing, coverage).
- Cross-platform verification of Deno projects.

## Related
- **deno-stability-and-releases** -- Canary and LTS versions are used in CI matrices.
- **deno-in-docker** -- Docker-based CI can use official Deno images.

# Common Errors

- **Error**: `deno fmt` fails on Windows due to CRLF line endings from `actions/checkout`.
  **Correction**: Configure git before checkout: `git config --system core.autocrlf false` and `git config --system core.eol lf`.

- **Error**: CI builds are slow due to re-downloading dependencies on every run.
  **Correction**: Enable `cache: true` on `denoland/setup-deno@v2`.

# Common Confusions

- **Confusion**: A separate testing framework or linter is needed for CI.
  **Clarification**: Deno's built-in `deno test`, `deno lint`, and `deno fmt` replace external tools.

# Source Reference

- runtime/reference/continuous_integration.md: Full CI pipeline documentation including GitHub Actions setup, cross-platform workflows, caching, and coverage.

# Verification Notes

- High confidence: Detailed YAML examples and explanations directly from source.
- Windows CRLF issue documented with explicit workaround from source.
