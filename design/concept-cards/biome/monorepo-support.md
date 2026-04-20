---
# === CORE IDENTIFICATION ===
concept: Monorepo Support
slug: monorepo-support

# === CLASSIFICATION ===
category: configuration
subcategory: project structure
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "guides/big-projects.mdx"
chapter_number: null
pdf_page: null
section: "Monorepo"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "multiple configuration files"
  - "nested configuration"
  - "workspace configuration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-configuration
  - configuration-file-resolution
extends: []
related:
  - configuration-extends
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set up Biome in a monorepo?"
  - "What must I know before setting up monorepo configuration?"
---

# Quick Definition
Biome's native support for monorepos through multiple nested configuration files, a root configuration concept, and the `"extends": "//"` microsyntax that lets packages inherit from the root configuration.

# Core Definition
Since Biome v2, monorepos are supported out of the box. A monorepo setup uses a **root configuration** (`biome.json` at the repository root) that defines base options, plus **nested configurations** in individual packages. Nested configurations must set `"root": false` to indicate they are not standalone. The `"extends": "//"` microsyntax tells a nested configuration to inherit all settings from the root configuration, regardless of directory depth. Packages can selectively override inherited settings or choose not to extend the root at all. When `"extends": "//"` is used, `"root": false` is implied and can be omitted.

# Prerequisites
- biome-configuration: Must understand biome.json structure.
- configuration-file-resolution: Must understand how Biome discovers config files.

# Key Properties
1. Root configuration at repository root sets base options for the entire monorepo.
2. Nested configs must declare `"root": false` (or use `"extends": "//"`).
3. `"extends": "//"` inherits from the root configuration regardless of nesting depth.
4. Using `"extends": "//"` implicitly sets `"root": false`.
5. Packages can omit `"extends": "//"` to use completely independent settings.
6. Biome can be run from the monorepo root or from individual packages.
7. Vendored folders or Git submodules with their own `biome.json` may need to be excluded via `files.includes`.

# Construction / Recognition
To set up a monorepo:
1. Create a root `biome.json` with shared options (formatter, linter rules).
2. In each package needing customization, create a `biome.json` with `"extends": "//"`.
3. Override specific settings in the package config (e.g., disable a rule, change formatting).
4. For packages that should not inherit root settings, set `"root": false` without `"extends": "//"`.
5. Run `biome` commands from root or individual packages -- Biome respects all settings.

# Context & Application
Used in monorepos and workspaces where different packages may have different formatting or linting needs. The root config establishes organization-wide standards while allowing package-level flexibility.

# Examples
From the source, a root configuration:

```json
{
  "linter": { "enabled": true, "rules": { "recommended": true } },
  "formatter": { "lineWidth": 120, "indentStyle": "space", "indentWidth": 6 }
}
```

A package that extends root but disables one rule:

```json
{
  "extends": "//",
  "linter": { "rules": { "suspicious": { "noConsole": "off" } } }
}
```

A package with completely independent settings (no root inheritance):

```json
{
  "root": false,
  "formatter": { "lineWidth": 100 }
}
```

(From guides/big-projects.mdx, "Monorepo" section)

# Relationships
## Builds Upon
- biome-configuration
- configuration-file-resolution
## Enables
- configuration-extends (monorepo uses the extends mechanism)
## Related
- configuration-extends (general extends functionality)
## Contrasts With
None.

# Common Errors
1. Forgetting `"root": false` in nested configs that don't use `"extends": "//"`.
2. Having a vendored project with its own `biome.json` that lacks `"root": false`, causing configuration conflicts.
3. Expecting `"extends": "//"` to merge deeply -- later settings override earlier ones.

# Common Confusions
1. Thinking `"extends": "//"` is a file path -- it is a special microsyntax meaning "root configuration."
2. Confusing `"root": false` (this is a nested config) with root directory placement.

# Source Reference
- guides/big-projects.mdx, "Monorepo" section and "Use multiple configuration files" section

# Verification Notes
Thoroughly documented with step-by-step instructions and multiple examples. High confidence.
