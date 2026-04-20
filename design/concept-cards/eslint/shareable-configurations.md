---
# === CORE IDENTIFICATION ===
concept: Shareable Configurations
slug: shareable-configurations

# === CLASSIFICATION ===
category: extending
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/shareable-configs.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "shareable config"
  - "shared config"
  - "eslint-config-*"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - configuration-files
extends:
  - eslint
related:
  - creating-plugins
  - rules
  - flat-config
contrasts_with:
  - creating-plugins

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a shareable ESLint configuration?"
  - "How do you create and publish a shareable config?"
  - "How do you use and override a shareable config?"
  - "Can a single package export multiple configs?"
  - "What naming conventions should shareable configs follow?"
---

# Quick Definition
A shareable ESLint configuration is an npm package that exports a configuration object or array, enabling teams to reuse consistent linting settings across multiple projects.

# Core Definition
Shareable configs are npm packages that export configuration objects or arrays from their main entry point. They can contain anything a configuration file can: rules, language options, globals, plugins, and more. Shareable configs allow teams and communities to standardize ESLint settings rather than each project independently configuring hundreds of rules.

Naming conventions:
- **Unscoped**: `eslint-config-*` (e.g., `eslint-config-myconfig`)
- **Scoped**: `@scope/eslint-config` or `@scope/eslint-config-*`

Published with `eslint` as a peer dependency (>= 9) and keywords `["eslint", "eslintconfig"]`. If the config depends on plugins or custom parsers, those should be listed as `dependencies` in `package.json`.

Users import the config and apply it via `extends` in `defineConfig()`. Settings from the shareable config can be overridden by adding rules or other options after the `extends` entry. A single package can export multiple configs by creating additional files beyond the main entry point.

Shareable configs are frequently provided alongside plugins -- many plugins include configs with names like "recommended" that enable their suggested starting set of rules.

# Prerequisites
- configuration-files: Shareable configs are consumed within ESLint config files

# Key Properties
1. **npm package** -- Simply an npm module exporting config objects/arrays
2. **Naming conventions** -- `eslint-config-*` or `@scope/eslint-config-*` for discovery
3. **extends mechanism** -- Applied via `extends` in defineConfig
4. **Override support** -- Users can override any setting from the shared config
5. **Multiple configs** -- One package can export several config files
6. **Plugin-bundled** -- Plugins can also include shareable configs in their `configs` property
7. **Composable** -- Multiple shareable configs can be combined in a config array

# Construction / Recognition
```js
// index.js
export default [{
    languageOptions: { globals: { MyGlobal: true } },
    rules: { semi: [2, "always"] }
}];
```

Usage:
```js
import { defineConfig } from "eslint/config";
import myconfig from "eslint-config-myconfig";

export default defineConfig([{
    files: ["**/*.js"],
    extends: [myconfig]
}]);
```

# Context & Application
Shareable configs are widely used to distribute organizational style guides. For example, `eslint-config-airbnb` enforces the Airbnb JavaScript style guide. Unlike plugins, standalone shareable configs cannot include custom rules -- they only configure existing rules. However, plugins can bundle configs that reference the plugin's own rules.

# Examples
From extend/shareable-configs.md:
- Default export: `export default [{ rules: { semi: [2, "always"] } }]`
- Multiple configs: separate files like `my-special-config.js` imported individually
- Overriding: add `rules` after `extends` to override specific settings

From use/core-concepts/index.md:
- "eslint-config-airbnb-base implements the popular Airbnb JavaScript style guide."

# Relationships
## Builds Upon
- configuration-files

## Related
- creating-plugins (plugins can bundle configs)
- rules
- flat-config

## Contrasts With
- creating-plugins (plugins contain rules; standalone shareable configs only configure them)

# Common Errors
1. Trying to use shareable configs with the `--config` CLI flag -- this is not supported
2. Exporting a single object when an array is expected (or vice versa) -- document usage clearly
3. Forgetting to list plugin dependencies as `dependencies` rather than `peerDependencies`
4. Mixing multiple conflicting shareable configs without understanding config array ordering

# Common Confusions
1. **Shareable config vs. plugin** -- A shareable config is a set of configuration settings; a plugin can contain rules, configs, and processors. Plugins often include shareable configs, but they are distinct concepts.

# Source Reference
- extend/shareable-configs.md: Creating, publishing, using, and overriding shareable configurations
- use/core-concepts/index.md: Shareable Configurations overview
- use/core-concepts/glossary.md: Shareable Config definition

# Verification Notes
- High confidence: directly extracted from official documentation; merged content from core concepts and extending docs
