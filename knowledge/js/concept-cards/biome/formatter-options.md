---
concept: Formatter Options
slug: formatter-options
category: formatter
subcategory: configuration
tier: intermediate
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "formatter/index.mdx"
chapter_number: null
pdf_page: null
section: "Options"
extraction_confidence: high
aliases:
  - formatter configuration
  - biome formatter settings
prerequisites:
  - biome-formatter
extends:
  - biome-formatter
related:
  - opinionated-formatting
  - prettier-compatibility
contrasts_with: []
answers_questions:
  - "How do I configure the Biome formatter?"
  - "What formatting options does Biome support?"
---

# Quick Definition

Biome's formatter configuration is split into language-agnostic options (indent style, indent width, line width) and language-specific options (semicolons, quote style, trailing commas), all settable via `biome.json` or the CLI.

# Core Definition

Biome separates its formatting options into two tiers. Language-agnostic options apply across all supported languages and control fundamental layout properties. Language-specific options (under keys like `javascript` and `json`) control syntax-level choices particular to that language. Options can be set via the CLI, a `biome.json` configuration file, or (as of v1.9) an `.editorconfig` file. Using a configuration file is recommended to ensure the CLI and LSP apply identical settings.

# Prerequisites

- biome-formatter — understanding what the Biome formatter is and how it runs

# Key Properties

1. **Language-agnostic options** — `indentStyle` (tab/space), `indentWidth` (default: 2), `lineWidth` (default: 80), `lineEnding` (default: lf), `attributePosition`, `formatWithErrors`, `enabled`, `ignore`
2. **JavaScript-specific options** — `arrowParentheses` (always), `bracketSameLine` (false), `bracketSpacing` (true), `jsxQuoteStyle` (double), `quoteProperties` (asNeeded), `semicolons` (always), `trailingCommas` (all)
3. **JSON-specific options** — `trailingCommas` (none)
4. **Multiple configuration sources** — `biome.json`, CLI flags, `.editorconfig`
5. **Defaults favor consistency** — tabs for indentation, 80-character line width, LF line endings

# Construction / Recognition

A minimal `biome.json` configuration:

```json
{
  "formatter": {
    "enabled": true,
    "indentStyle": "tab",
    "indentWidth": 2,
    "lineWidth": 80,
    "lineEnding": "lf"
  },
  "javascript": {
    "formatter": {
      "semicolons": "always",
      "trailingCommas": "all"
    }
  }
}
```

Language-specific options are nested under their language key (e.g., `javascript.formatter`), not under the top-level `formatter` key.

# Context & Application

Formatter options are configured once per project and shared across team members. The recommended approach is a checked-in `biome.json` file, which ensures both CLI and editor integrations produce identical output. The option set is intentionally small, following the opinionated formatting philosophy.

# Examples

From `formatter/index.mdx`, the full default configuration:

- Top-level `formatter` block: `enabled: true`, `formatWithErrors: false`, `indentStyle: "tab"`, `indentWidth: 2`, `lineWidth: 80`, `lineEnding: "lf"`
- `javascript.formatter` block: `arrowParentheses: "always"`, `bracketSameLine: false`, `bracketSpacing: true`, `jsxQuoteStyle: "double"`, `quoteProperties: "asNeeded"`, `semicolons: "always"`, `trailingCommas: "all"`
- `json.formatter` block: `trailingCommas: "none"`

# Relationships

## Builds Upon
- biome-formatter

## Enables
Configuration of project-specific formatting without abandoning the opinionated approach.

## Related
- opinionated-formatting (the philosophy that keeps options minimal)
- prettier-compatibility (many options exist for Prettier migration)

## Contrasts With
None directly, though the limited option set contrasts with fully-configurable formatters like ESLint's formatting rules.

# Common Errors

1. **Placing language-specific options at the top level** — options like `semicolons` must go under `javascript.formatter`, not under the top-level `formatter` key.
2. **Assuming spaces are the default** — Biome defaults to tabs, unlike Prettier which defaults to spaces.
3. **Ignoring `.editorconfig` interaction** — as of v1.9, Biome loads `.editorconfig`, which may override `biome.json` settings unexpectedly.

# Common Confusions

1. **Why so few options?** — The limited option set is intentional, following the opinionated formatting philosophy. Options like `bracketSameLine` and `arrowParentheses` exist only for Prettier compatibility and are considered legacy.
2. **CLI flags vs. config file** — Both work, but a config file is recommended to ensure CLI and LSP consistency.

# Source Reference

- `sources-md/biome/formatter/index.mdx` — Options section, including full default JSON configuration

# Verification Notes

All option names and defaults extracted directly from the source configuration example. The two-tier structure (language-agnostic vs. language-specific) is explicitly stated in the source.
