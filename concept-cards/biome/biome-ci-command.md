---
# === CORE IDENTIFICATION ===
concept: Biome CI Command
slug: biome-ci-command

# === CLASSIFICATION ===
category: integration
subcategory: continuous integration
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "recipes/continuous-integration.mdx"
chapter_number: null
pdf_page: null
section: "biome check VS biome ci"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "biome ci"
  - "CI command"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-cli
  - biome-configuration
extends:
  - biome-cli
related:
  - vcs-integration
  - git-hooks-integration
contrasts_with:
  - biome-cli

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set up Biome in CI?"
  - "What distinguishes `biome check` from `biome ci`?"
---

# Quick Definition
The `biome ci` command is a CI-optimized variant of `biome check` that disables write/fix options, integrates with CI runners (e.g., GitHub annotations), and automatically uses `--changed` instead of `--staged` when VCS is enabled.

# Core Definition
`biome ci` is a dedicated CLI command for Continuous Integration environments. It runs all of Biome's checks (formatting, linting, import organization) but differs from `biome check` in several ways: it provides no `--write` or `--fix` options (ensuring CI is read-only), it integrates with specific CI runners (e.g., printing diagnostics as GitHub annotations), it allows controlling the number of threads, and when VCS integration is enabled, it uses `--changed` instead of `--staged` (since remote repositories have no concept of staged files).

# Prerequisites
- biome-cli: Must understand the basic Biome commands.
- biome-configuration: Must understand biome.json setup.

# Key Properties
1. No `--write` or `--fix` flags -- CI is strictly read-only / check-only.
2. Integrates with CI runners (e.g., GitHub annotations for diagnostics).
3. Uses `--changed` (not `--staged`) when VCS integration is enabled.
4. Allows controlling thread count for CI resource management.
5. Supports GitLab CI with `--reporter=gitlab` for code quality reports.
6. A first-party GitHub Action (`biomejs/setup-biome@v2`) is available.

# Construction / Recognition
To set up Biome in CI:

**GitHub Actions:**
```yaml
steps:
  - uses: actions/checkout@v5
  - uses: biomejs/setup-biome@v2
    with:
      version: latest
  - run: biome ci .
```

**GitLab CI:**
```yaml
lint:
  image:
    name: ghcr.io/biomejs/biome:latest
    entrypoint: [""]
  script:
    - biome ci --reporter=gitlab --colors=off > code-quality.json
```

# Context & Application
Used in pull request checks and continuous integration pipelines. Ensures code quality is enforced without modifying source files. The GitHub annotations feature provides inline feedback on pull requests.

# Examples
From the source, a GitHub Actions workflow:

```yaml
name: Code quality
on:
  push:
  pull_request:
jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
        with:
          persist-credentials: false
      - uses: biomejs/setup-biome@v2
        with:
          version: latest
      - run: biome ci .
```

If the Biome configuration extends an NPM package, Node.js setup and dependency installation must precede the Biome step.

(From recipes/continuous-integration.mdx)

# Relationships
## Builds Upon
- biome-cli (ci is a specialized variant of check)
## Enables
None directly.
## Related
- vcs-integration (VCS enables --changed behavior in CI)
- git-hooks-integration (hooks and CI are complementary checks)
## Contrasts With
- biome-cli (`biome check` supports --write; `biome ci` does not)

# Common Errors
1. Using `biome check` in CI instead of `biome ci`, missing CI-specific features like annotations.
2. Using `--staged` with `biome ci` -- it is not supported.
3. Forgetting to install Node.js dependencies when the Biome config extends an NPM package.

# Common Confusions
1. Thinking `biome ci` and `biome check` are identical -- `ci` has runner integrations and no write mode.
2. Assuming `biome ci` requires VCS integration -- it works without it, but gains `--changed` behavior with it.

# Source Reference
- recipes/continuous-integration.mdx, all sections

# Verification Notes
Explicitly documented with complete CI workflow examples. High confidence.
