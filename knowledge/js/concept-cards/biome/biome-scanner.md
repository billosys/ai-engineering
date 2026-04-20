---
# === CORE IDENTIFICATION ===
concept: Biome Scanner
slug: biome-scanner

# === CLASSIFICATION ===
category: architecture
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "internals/architecture.mdx"
chapter_number: null
pdf_page: null
section: "Scanner"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "scanner"
  - "file system crawler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome
extends: []
related:
  - scanner-targeting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Biome Scanner?"
  - "How does Biome discover configuration files in monorepos?"
---

# Quick Definition
The Biome scanner is the component responsible for crawling the file system to discover configuration files, ignore files, and project metadata needed before processing begins.

# Core Definition
Biome has a scanner that is responsible for crawling the file system to extract important metadata about projects. The scanner serves three specific purposes: discovering nested `biome.json`/`biome.jsonc` configuration files in monorepos, discovering nested `.gitignore` files when the `vcs.useIgnoreFile` setting is enabled, and indexing `package.json` manifests and source files when project domain linter rules are enabled.

# Prerequisites
- biome: Must understand what Biome is and its role as a toolchain

# Key Properties
1. **Configuration discovery** -- Finds nested `biome.json`/`biome.jsonc` files in monorepos
2. **Ignore file discovery** -- Finds nested `.gitignore` files when VCS ignore is enabled
3. **Project indexing** -- Indexes `package.json` manifests and source files for project domain linter rules
4. **Configurable** -- Can be configured through the `files.includes` setting

# Construction / Recognition
The scanner runs automatically as part of Biome's initialization phase. Its behavior depends on:
- Whether project domain rules are enabled (affects targeting optimization)
- The `vcs.useIgnoreFile` setting (affects `.gitignore` discovery)
- The `files.includes` configuration setting

# Context & Application
The scanner is essential for monorepo support, where multiple `biome.json` configuration files may exist at different levels of the directory hierarchy. It runs before the actual formatting/linting phase to establish the project context, including which files should be included or excluded from processing.

# Examples
From internals/architecture.mdx, "Scanner" section:
- "To discover nested `biome.json`/`biome.jsonc` files in monorepos."
- "To discover nested `.gitignore` files if the `vcs.useIgnoreFile` setting is enabled."
- "To index `package.json` manifests as well as source files in a project if any rules from the project domain are enabled."

# Relationships
## Builds Upon
- biome

## Enables
- scanner-targeting
- Monorepo configuration resolution
- VCS-aware file filtering

## Related
- scanner-targeting

## Contrasts With
- N/A

# Common Errors
1. Not realizing the scanner behavior changes when project domain rules are enabled (targeting optimizations are disabled)

# Common Confusions
1. **Scanner vs. parser** -- The scanner crawls the file system for metadata; the parser processes individual source files into syntax trees. They operate at different stages.

# Source Reference
- internals/architecture.mdx: "Scanner" section

# Verification Notes
- High confidence: Explicitly defined in the architecture documentation with clear enumeration of purposes
