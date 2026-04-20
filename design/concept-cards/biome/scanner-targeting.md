---
# === CORE IDENTIFICATION ===
concept: Scanner Targeting
slug: scanner-targeting

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
section: "Scanner targeting"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "scanner optimization"
  - "folder targeting"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-scanner
extends:
  - biome-scanner
related:
  - biome
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Biome optimize which folders to scan?"
  - "How does the scanner work in monorepos?"
---

# Quick Definition
Scanner targeting is Biome's optimization strategy that limits file system scanning to only the folders relevant to the current operation, skipping adjacent or unrelated directories in large monorepos.

# Core Definition
When project rules are not enabled, the scanner automatically targets only the folders that are relevant for a given session. If Biome is run from within a specific subfolder of a monorepo, the scanner only scans the path from the repository root down to the target folder (and its descendants), skipping sibling directories entirely. This optimization does not apply when project domain rules are enabled.

# Prerequisites
- biome-scanner: Must understand what the scanner does and its three purposes

# Key Properties
1. **Path-based targeting** -- Only scans folders along the path from repository root to the working directory
2. **Automatic skipping** -- Adjacent folders not on the target path are automatically skipped
3. **node_modules exclusion** -- `node_modules/` directories are always skipped
4. **Conditional optimization** -- Disabled when project domain linter rules are enabled
5. **Configuration-aware** -- Respects folders excluded by user configuration

# Construction / Recognition
Scanner targeting is automatic and requires no explicit configuration. It activates when:
- Running Biome from a subdirectory of a monorepo
- Project domain rules are NOT enabled

# Context & Application
Scanner targeting is particularly valuable in large monorepos where a full file system crawl would be expensive. By limiting the scan to only the relevant directory hierarchy, Biome avoids unnecessary I/O and speeds up initialization.

# Examples
From internals/architecture.mdx, "Scanner targeting" section:

Running `biome check` from inside `packages/foo/` causes only these folders to be scanned:
- The root folder of the repository
- The `packages/` folder
- The `packages/foo/` folder
- Any folders under `packages/foo/`, except `node_modules/` or those excluded by configuration

"Other folders that may be adjacent to either `packages/` or `packages/foo/` will be automatically skipped."

Similarly, running `biome format packages/bar/src/index.ts` from the repository root targets the `packages/bar/src/` folder.

# Relationships
## Builds Upon
- biome-scanner

## Enables
- Efficient monorepo support
- Fast initialization in large projects

## Related
- biome

## Contrasts With
- Full recursive file system scanning (which would scan all directories)

# Common Errors
1. Expecting targeting optimizations when project domain rules are enabled -- those rules disable this optimization
2. Running from the repository root and expecting only a subfolder to be scanned -- the scanner follows the path hierarchy

# Common Confusions
1. **Targeting vs. file filtering** -- Targeting determines which directories are *crawled*; file filtering (via includes/excludes) determines which files within those directories are *processed*

# Source Reference
- internals/architecture.mdx: "Scanner targeting" section

# Verification Notes
- High confidence: Explicitly described with concrete examples in the source
