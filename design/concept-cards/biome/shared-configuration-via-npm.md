---
# === CORE IDENTIFICATION ===
concept: Shared Configuration via NPM
slug: shared-configuration-via-npm

# === CLASSIFICATION ===
category: configuration
subcategory: configuration distribution
tier: advanced

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "guides/big-projects.mdx"
chapter_number: null
pdf_page: null
section: "Exporting a Biome configuration from an NPM package"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "NPM shared config"
  - "biome config package"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-configuration
  - configuration-extends
extends:
  - configuration-extends
related:
  - monorepo-support
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set up Biome in a monorepo?"
---

# Quick Definition
A method for distributing Biome configuration as an NPM package, using the `package.json` `exports` field and Biome's `extends` configuration to resolve configs from `node_modules/`.

# Core Definition
Biome can resolve configuration files from `node_modules/`, enabling organizations to publish shared Biome configurations as NPM packages. The shared package must define an `exports` entry in its `package.json` that maps a specifier to the `biome.json` file. Consuming projects reference the package specifier in their `extends` field. Biome uses the Node.js ESM resolution algorithm to locate the configuration. Specifiers that start with `.` or end with `.json`/`.jsonc` are treated as relative paths and will not be resolved from `node_modules/`.

# Prerequisites
- biome-configuration: Must understand biome.json structure.
- configuration-extends: Must understand how extends works.

# Key Properties
1. The shared package must have an `exports` field mapping a specifier to the biome.json file.
2. Resolution uses the Node.js ESM resolution algorithm.
3. The working directory for resolution is the CLI execution folder or the editor's project root.
4. Relative paths (starting with `.`) and paths ending in `.json`/`.jsonc` bypass `node_modules/` resolution.

# Construction / Recognition
To create and use a shared NPM configuration:

**Publishing side:**
1. Create a package (e.g., `@org/shared-configs`) with a `biome.json`.
2. Add an exports entry: `"./biome": "./biome.json"`.
3. Publish the package.

**Consuming side:**
1. Install the package: `npm install @org/shared-configs`.
2. Set `"extends": ["@org/shared-configs/biome"]` in your `biome.json`.

# Context & Application
Used by organizations maintaining consistent Biome settings across many repositories. Avoids duplicating configuration and ensures updates propagate when the shared package is updated.

# Examples
From the source:

Shared package's `package.json`:
```json
{
  "name": "@org/shared-configs",
  "type": "module",
  "exports": {
    "./biome": "./biome.json"
  }
}
```

Consumer's `biome.json`:
```json
{
  "extends": ["@org/shared-configs/biome"]
}
```

(From guides/big-projects.mdx, "Exporting a Biome configuration from an NPM package" section)

# Relationships
## Builds Upon
- configuration-extends
## Enables
None directly.
## Related
- monorepo-support (shared configs are common in monorepo setups)
## Contrasts With
None.

# Common Errors
1. Starting the specifier with `.` or ending it with `.json`, which causes Biome to treat it as a relative path instead of an NPM package.
2. Forgetting the `exports` field in the shared package's `package.json`.
3. Not installing the shared package before running Biome.

# Common Confusions
1. Thinking Biome uses its own resolution algorithm -- it uses the standard Node.js ESM resolution.

# Source Reference
- guides/big-projects.mdx, "Exporting a Biome configuration from an NPM package" section

# Verification Notes
Explicitly documented with publisher and consumer examples. High confidence.
