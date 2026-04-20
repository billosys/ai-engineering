---
# === CORE IDENTIFICATION ===
concept: Plugin Migration to Flat Config
slug: plugin-migration-flat-config

# === CLASSIFICATION ===
category: migration
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/plugin-migration-flat-config.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "plugin flat config migration"
  - "eslint plugin migration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - plugins
  - flat-config-migration
extends: []
related:
  - eslint-v9-migration
  - configuration-files
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I update my ESLint plugin for flat config?"
  - "What changes are needed for plugin processors in flat config?"
  - "How do I export shareable configs from a plugin for flat config?"
  - "How do I handle backwards compatibility between eslintrc and flat config?"
  - "What is the recommended plugin structure for flat config?"
---

# Quick Definition
Plugin migration to flat config involves restructuring ESLint plugins to use a standard object-based entrypoint with `meta`, `configs`, `rules`, and `processors` keys, updating file-extension-named processors, and converting exported configs to flat config format with direct plugin references.

# Core Definition
Beginning in ESLint v9, the default configuration system is flat config, and plugins must be updated for compatibility. The recommended plugin structure uses a single object with `meta`, `configs`, `rules`, and `processors` keys. The `meta` key must include at least `name` and ideally `version` (matching package.json) -- without this, the plugin cannot be used with `--cache` or `--print-config`. Rules require no changes. Processors with file-extension names (e.g., `".md"`) must be renamed to valid identifiers (e.g., `"markdown"`) since file-extension-named processors are no longer automatically applied. Exported configs must reference the plugin object directly in their `plugins` key rather than using string names. Environments must be converted into exported config objects with `languageOptions.globals`.

# Prerequisites
- eslint: Basic ESLint knowledge
- plugins: Understanding of ESLint plugin structure
- flat-config-migration: Understanding the flat config format

# Key Properties
1. **Meta information required** -- Plugins must include `meta.name` and `meta.version` for cache and config printing support
2. **No rule changes needed** -- The rules API is identical between eslintrc and flat config
3. **Processor renaming** -- File-extension-named processors (e.g., `".md"`) must be renamed to valid identifiers
4. **Self-referencing configs** -- Exported configs must reference the plugin object directly: `plugins: { example: plugin }`
5. **Environments become configs** -- Environment definitions are converted to config objects with `languageOptions.globals`
6. **Backwards compatibility** -- Plugins can support both systems by exporting CommonJS, keeping `environments`, and prefixing legacy configs with `legacy-`

# Construction / Recognition
Recommended plugin structure:
```javascript
const plugin = {
  meta: { name: "eslint-plugin-example", version: "1.0.0" },
  configs: {},
  rules: {},
  processors: {}
};
// Assign configs after definition to reference `plugin`
Object.assign(plugin.configs, {
  recommended: {
    plugins: { example: plugin },
    rules: { "example/rule1": "error" }
  }
});
export default plugin;
```

# Context & Application
This migration is essential for plugin maintainers as ESLint v10 removes eslintrc support entirely. Plugins that are not updated will not work with flat config unless users employ the `FlatCompat` utility. The migration also improves the plugin developer experience by making dependencies explicit rather than relying on string-based resolution.

# Examples
From extend/plugin-migration-flat-config.md:

Renaming a file-extension processor:
```javascript
// Before (no longer supported)
processors: { ".md": { preprocess() {}, postprocess() {} } }

// After
processors: { markdown: { preprocess() {}, postprocess() {} } }
```

Converting an environment to a config:
```javascript
Object.assign(plugin.configs, {
  mocha: {
    languageOptions: {
      globals: {
        it: "writeable",
        describe: "writeable"
      }
    }
  }
});
```

Backwards compatibility strategy:
- Export a CommonJS entrypoint
- Keep the `environments` key (ignored in flat config mode)
- Prefix legacy configs with `legacy-` or new ones with `flat/`

# Relationships
## Depends On
- flat-config-migration

## Related
- plugins
- eslint-v9-migration
- eslint-v10-migration

## Contrasts With
- eslintrc plugin format (string-based plugin references, auto-applied file-extension processors)

# Common Errors
1. Forgetting to add `meta.name` and `meta.version` -- causes `--cache` and `--print-config` to fail
2. Keeping file-extension-named processors -- these are no longer valid processor names
3. Not updating exported configs to reference the plugin object directly

# Common Confusions
1. **Rules don't change** -- Despite the config system changing, the rule API is identical
2. **Environments vs. configs** -- Environments don't exist in flat config; they must be converted to config objects with globals

# Source Reference
- extend/plugin-migration-flat-config.md: Full plugin migration guide with examples for each component

# Verification Notes
- High confidence: Dedicated migration guide with comprehensive examples
- All code patterns taken directly from the documentation
