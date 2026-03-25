---
# === CORE IDENTIFICATION ===
concept: Biome
slug: biome

# === CLASSIFICATION ===
category: toolchain
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "index.mdx"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Biome toolchain"
  - "@biomejs/biome"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - biome-check-command
  - concrete-syntax-tree
  - biome-daemon
  - biome-scanner
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Biome?"
  - "What languages does Biome support?"
  - "How does Biome compare to Prettier?"
---

# Quick Definition
Biome is a fast, unified web development toolchain built in Rust that provides formatting, linting, and other code quality tools for JavaScript, TypeScript, JSX, TSX, JSON, HTML, CSS, and GraphQL.

# Core Definition
Biome is a performant web toolchain that combines a formatter, linter, and other tools into a single cohesive package. Built with Rust and an architecture inspired by rust-analyzer, Biome scores 97% compatibility with Prettier for formatting while being approximately 35x faster. It provides detailed and contextualized diagnostics to help developers improve their code.

# Prerequisites
Foundational concept with no prerequisites.

# Key Properties
1. **Multi-tool integration** -- Combines formatting, linting, and other tools in a single toolchain
2. **Performance** -- Built in Rust; approximately 35x faster than Prettier when formatting
3. **Prettier compatibility** -- 97% compatibility with Prettier's formatting output
4. **Multi-language support** -- Supports JavaScript, TypeScript, JSX, TSX, JSON, HTML, CSS, and GraphQL
5. **Zero configuration** -- Works out of the box with no configuration required; extensive options available when needed
6. **Malformed code handling** -- Can format malformed code as you write it in your editor
7. **Actionable diagnostics** -- Outputs detailed, contextualized error messages that explain exactly where and what the problem is

# Construction / Recognition
- Install via package manager: `npm i -D --save-exact @biomejs/biome`
- Format code: `npx @biomejs/biome format --write ./src`
- Lint code: `npx @biomejs/biome lint --write ./src`
- Run all tools at once: `npx @biomejs/biome check --write ./src`

# Context & Application
Biome is used as a replacement for or alternative to combinations of tools like Prettier (formatting) and ESLint (linting). It is designed to handle codebases of any size and integrates with editors through first-party extensions. It is suitable for both individual developers and enterprise teams, with commercial support available.

# Examples
From the Biome homepage (index.mdx):
- Formatting: "Biome is a fast formatter for JavaScript, TypeScript, JSX, TSX, JSON, HTML, CSS and GraphQL that scores 97% compatibility with Prettier"
- Linting: "Biome is a performant linter for JavaScript, TypeScript, JSX, CSS and GraphQL that features [numerous] rules from ESLint, TypeScript ESLint, and other sources"
- Unified: "Not only can you format and lint your code separately, you can do it all at once with a single command!"

# Relationships
## Builds Upon
- Rust programming language
- rust-analyzer architecture (inspiration)

## Enables
- biome-check-command
- biome-scanner
- biome-daemon
- concrete-syntax-tree

## Related
- resilient-parser
- trivia

## Contrasts With
- Prettier (formatter only, slower)
- ESLint (linter only)

# Common Errors
1. Not using `--save-exact` when installing -- Biome recommends exact versions to avoid unexpected changes
2. Running format and lint separately when `check` would accomplish both at once

# Common Confusions
1. **Biome vs. Prettier** -- Biome is not just a formatter; it is a full toolchain that includes linting and more
2. **Configuration required** -- Biome works with zero configuration; configuration is optional, not mandatory

# Source Reference
- index.mdx: Homepage describing Biome's capabilities, performance, and installation

# Verification Notes
- High confidence: Biome is explicitly described throughout the homepage
- All language lists and performance claims taken directly from source text
