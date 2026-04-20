---
# === CORE IDENTIFICATION ===
concept: Biome Linter
slug: biome-linter

# === CLASSIFICATION ===
category: linter
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "linter/index.mdx"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Biome lint"
  - "biome lint command"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome
extends:
  - biome
related:
  - lint-rules
  - lint-rule-groups
  - linter-domains
  - safe-fixes
  - unsafe-fixes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Biome linter?"
  - "How do I run the Biome linter?"
  - "What languages does the Biome linter support?"
---

# Quick Definition
The Biome linter is a static analysis tool that finds and fixes common errors in code and helps developers write better, modern code across multiple languages.

# Core Definition
Biome's linter statically analyzes code to find and fix common errors and to help write better, modern code. It supports multiple languages and provides a large number of rules. Unlike other linters, Biome does not provide rules that check for code formatting -- the Biome formatter handles all formatting decisions. The linter is invoked via the CLI with `biome lint` or as part of the unified `biome check` command.

# Prerequisites
- biome (understanding of the Biome toolchain)

# Key Properties
1. **Static analysis** -- Analyzes code without executing it to detect problems
2. **Multi-language support** -- Works across JavaScript, TypeScript, JSX, CSS, and GraphQL
3. **Language-agnostic rules** -- Some rules work across more than one language (e.g., `noUselessEscapeInString` reports in both JavaScript and CSS)
4. **Code fixes** -- Many rules provide automatic code fixes, classified as safe or unsafe
5. **Recommended defaults** -- Ships with recommended rules enabled by default, varying by language
6. **No formatting rules** -- Formatting is delegated entirely to the Biome formatter
7. **Editor integration** -- First-class LSP integration for diagnostics and code actions

# Construction / Recognition
- Run on all project files: `biome lint`
- Run on specific directories: `biome lint ./src ./public`
- Apply safe fixes: `biome lint --write ./src`
- Apply safe and unsafe fixes: `biome lint --write --unsafe ./src`
- Skip specific rules: `biome lint --skip=style --skip=suspicious/noExplicitAny`
- Run only specific rules: `biome lint --only=style/useNamingConvention --only=a11y`

# Context & Application
The Biome linter is used during development and CI to enforce code quality, catch bugs, and maintain consistency. It integrates with LSP-compatible editors for real-time diagnostics. Configuration is done through `biome.json`. Globs are not supported as CLI arguments -- use the `includes` configuration instead.

# Examples
From linter/index.mdx:
- "Biome's linter statically analyzes your code to find and fix common errors and to help you write better, modern code."
- Running the linter: `biome lint` runs on all files from the project root
- The linter can be combined with formatting via `biome check`

# Relationships
## Builds Upon
- biome

## Enables
- lint-rules
- lint-rule-groups
- safe-fixes
- unsafe-fixes
- linter-domains
- linter-plugins

## Related
- rule-severity
- rule-pillars

## Contrasts With
- ESLint (JavaScript-only, plugin-based architecture)

# Common Errors
1. Passing globs as CLI arguments -- Biome does not support globs; shell expansion is used instead, which has performance costs and limits
2. Expecting formatting rules from the linter -- Biome separates linting and formatting concerns

# Common Confusions
1. **lint vs. check** -- `biome lint` runs only linting, while `biome check` runs linting and formatting together
2. **Glob support** -- Biome itself does not support globs; any expansion is performed by the shell

# Source Reference
- linter/index.mdx: Opening paragraphs and CLI usage sections

# Verification Notes
- High confidence: Directly described in the opening of linter/index.mdx
- CLI commands taken verbatim from source
