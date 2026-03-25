---
# === CORE IDENTIFICATION ===
concept: Biome Configuration
slug: biome-configuration

# === CLASSIFICATION ===
category: configuration
subcategory: configuration file structure
tier: foundational

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "guides/configure-biome.mdx"
chapter_number: null
pdf_page: null
section: "Configuration file structure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "biome.json"
  - "biome.jsonc"
  - "Biome config"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - configuration-file-resolution
  - file-includes-and-excludes
  - well-known-files
  - biome-cli
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I install and set up Biome?"
  - "How does biome.json configuration relate to CLI options?"
---

# Quick Definition
A Biome configuration file (`biome.json` or `biome.jsonc`) defines formatting, linting, and assist settings for a project, organized by tool and optionally by language.

# Core Definition
Biome is configured via a file named `biome.json` or `biome.jsonc`, typically placed at the project root alongside `package.json`. The configuration is organized around Biome's three tools -- formatter, linter, and assist -- all of which are enabled by default. Options that apply across languages are placed in the tool's top-level field (e.g., `formatter.indentStyle`), while language-specific options go under `<language>.<tool>` fields (e.g., `javascript.formatter.quoteStyle`). Language-specific settings can override general tool settings. Tools can also be enabled or disabled per language.

# Prerequisites
Foundational concept with no prerequisites.

# Key Properties
1. Configuration uses JSON (`biome.json`) or JSON with comments (`biome.jsonc`).
2. Three tool sections: `formatter`, `linter`, and `assist`, all enabled by default.
3. Each tool can be disabled globally via `<tool>.enabled: false`.
4. General options live in the tool field; language-specific overrides live in `<language>.<tool>`.
5. Biome refers to all JavaScript variants (TypeScript, JSX, TSX) as `javascript`.
6. Many configuration options are also available as CLI flags.
7. A `$schema` field can be set for editor autocompletion.

# Construction / Recognition
To create a Biome configuration:
1. Run `biome init` to generate a starter `biome.json`.
2. Set general tool options at the tool level (e.g., `formatter.indentStyle`).
3. Override for specific languages under `<language>.<tool>` (e.g., `javascript.formatter.lineWidth`).
4. Disable tools globally or per language by setting `enabled: false`.

# Context & Application
Used in every Biome-enabled project. The configuration file ensures consistent behavior across CLI invocations and editor integrations for all team members.

# Examples
From the source, a configuration that sets general formatter options, overrides for JavaScript, and disables JSON formatting:

```json
{
  "formatter": {
    "indentStyle": "space",
    "lineWidth": 100
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "single",
      "lineWidth": 120
    }
  },
  "json": {
    "formatter": {
      "enabled": false
    }
  }
}
```

(From guides/configure-biome.mdx, "Configuration file structure" section)

# Relationships
## Builds Upon
None -- this is a foundational concept.
## Enables
- configuration-file-resolution (how Biome finds this file)
- file-includes-and-excludes (which files the config applies to)
- monorepo-support (multiple config files in large projects)
## Related
- biome-cli (CLI options mirror many config options)
- well-known-files (special parsing for certain files)
## Contrasts With
None.

# Common Errors
1. Forgetting that `biome.json` uses strict JSON (no comments), while `biome.jsonc` allows comments.
2. Placing language-specific options at the tool level instead of under `<language>.<tool>`.
3. Not realizing that all three tools are enabled by default; explicitly enabling them is redundant.

# Common Confusions
1. Confusing `javascript` with only JavaScript -- it covers TypeScript, JSX, and TSX as well.
2. Assuming CLI options always override config file settings, or vice versa, without checking the precedence rules.

# Source Reference
- guides/configure-biome.mdx, "Configuration file structure" section

# Verification Notes
Directly documented with explicit examples in the source. High confidence.
