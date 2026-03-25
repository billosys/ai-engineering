---
# === CORE IDENTIFICATION ===
concept: Biome CLI
slug: biome-cli

# === CLASSIFICATION ===
category: integration
subcategory: command-line interface
tier: foundational

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "guides/getting-started.mdx"
chapter_number: null
pdf_page: null
section: "Command-line interface"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "command-line interface"
  - "biome commands"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - biome-configuration
  - biome-ci-command
  - vcs-integration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I install and set up Biome?"
  - "What distinguishes `biome format`, `biome lint`, and `biome check`?"
  - "How does biome.json configuration relate to CLI options?"
---

# Quick Definition
Biome's command-line interface provides distinct commands for formatting (`biome format`), linting (`biome lint`), and combined checking (`biome check`), along with initialization and migration utilities.

# Core Definition
The Biome CLI is the primary way to interact with Biome outside of editor integrations. It provides four main operational commands: `biome format` (runs only the formatter), `biome lint` (runs only the linter with safe fixes), `biome check` (runs the formatter, linter, and import organizer together), and `biome ci` (a CI-optimized variant of check). The `--write` flag applies changes to files. Biome is installed as an NPM dev dependency (`@biomejs/biome`) or as a standalone executable. Configuration is initialized via `biome init`, which generates a starter `biome.json`.

# Prerequisites
Foundational concept with no prerequisites.

# Key Properties
1. `biome format` -- runs only the formatter.
2. `biome lint` -- runs only the linter, can apply safe fixes with `--write`.
3. `biome check` -- runs formatter, linter, and import organizer together.
4. `biome ci` -- CI-optimized variant of check (no write capability).
5. `--write` flag applies fixes/formatting to files in place.
6. `biome init` generates a starter configuration file.
7. Available via NPM (`npx @biomejs/biome`) or as a standalone binary.
8. Supports pnpm, yarn, bun, and deno package managers.
9. Version should be pinned with `-E` flag during installation.

# Construction / Recognition
To get started with Biome CLI:
1. Install: `npm i -D -E @biomejs/biome`.
2. Initialize: `npx @biomejs/biome init`.
3. Format: `npx @biomejs/biome format --write`.
4. Lint: `npx @biomejs/biome lint --write`.
5. Check all: `npx @biomejs/biome check --write`.

# Context & Application
The CLI is used in local development workflows, CI pipelines, and git hooks. The separation of `format`, `lint`, and `check` commands allows teams to run specific tools independently or together as needed.

# Examples
From the source:

```shell
# Format all files
npx @biomejs/biome format --write

# Lint files and apply safe fixes
npx @biomejs/biome lint --write

# Format, lint, and organize imports of all files
npx @biomejs/biome check --write

# Format, lint, and organize imports of specific files
npx @biomejs/biome check --write <files>
```

(From guides/getting-started.mdx, "Command-line interface" section)

# Relationships
## Builds Upon
None -- this is a foundational concept.
## Enables
- biome-ci-command (CI-specific variant)
- vcs-integration (CLI flags like --changed, --staged)
- git-hooks-integration (CLI is invoked from hooks)
## Related
- biome-configuration (CLI options mirror config options)
## Contrasts With
None.

# Common Errors
1. Running `biome check` without `--write` and expecting files to be modified.
2. Not pinning the Biome version (omitting `-E`), leading to inconsistent behavior across team members.

# Common Confusions
1. Confusing `biome check` with `biome ci` -- `check` is for local use with write capability; `ci` is for CI without write.
2. Thinking `biome format` also lints -- it only formats. Use `biome check` for both.
3. Confusing `biome lint --write` (applies safe fixes) with formatting -- linting fixes are code corrections, not style changes.

# Source Reference
- guides/getting-started.mdx, "Usage" and "Command-line interface" sections

# Verification Notes
Directly documented with examples for multiple package managers. High confidence.
