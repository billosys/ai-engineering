---
# === CORE IDENTIFICATION ===
concept: Biome Check Command
slug: biome-check-command

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
section: "Everything all at once"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "biome check"
  - "check command"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you run all Biome tools at once?"
  - "What is the biome check command?"
---

# Quick Definition
The `check` command is Biome's unified command that runs all tools -- formatter, linter, and more -- simultaneously on your codebase in a single invocation.

# Core Definition
The Biome check command allows developers to run formatting, linting, and all other integrated tools at once rather than invoking each tool separately. Every tool integrates seamlessly with the others to create a cohesive toolchain experience. The `--write` flag applies fixes automatically.

# Prerequisites
- biome: Must understand what Biome is and have it installed

# Key Properties
1. **Unified execution** -- Runs all Biome tools (format, lint, etc.) in a single command
2. **Seamless integration** -- All tools integrate with each other cohesively
3. **Write mode** -- Supports `--write` flag to apply fixes automatically
4. **Path targeting** -- Accepts a path argument to specify which files/directories to process

# Construction / Recognition
Usage:
```shell
npx @biomejs/biome check --write ./src
```
This runs all tools on the `./src` directory and writes fixes back to the files.

# Context & Application
The check command is the recommended way to use Biome in most workflows. Rather than running `biome format` and `biome lint` separately, `biome check` combines them into a single pass. This is useful in CI pipelines and pre-commit hooks where you want comprehensive code quality checking with minimal configuration.

# Examples
From index.mdx, section "Everything all at once":
- "Not only can you format and lint your code separately, you can do it all at once with a single command!"
- "Every tool integrates seamlessly with others to create a cohesive toolchain for web projects."
- Usage: `npx @biomejs/biome check --write ./src`

# Relationships
## Builds Upon
- biome

## Enables
- Unified CI/CD code quality pipelines

## Related
- biome

## Contrasts With
- Running `biome format` and `biome lint` separately

# Common Errors
1. Forgetting the `--write` flag when you intend fixes to be applied to files
2. Not specifying a path, which may cause Biome to process unintended files

# Common Confusions
1. **check vs. format/lint** -- `check` is not a different tool; it runs all the same tools that `format` and `lint` run, just combined into one invocation

# Source Reference
- index.mdx: "Everything all at once" section

# Verification Notes
- High confidence: Explicitly described with usage example in the source
