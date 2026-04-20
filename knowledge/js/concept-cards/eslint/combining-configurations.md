---
# === CORE IDENTIFICATION ===
concept: Combining Configurations
slug: combining-configurations

# === CLASSIFICATION ===
category: configuration
subcategory: config composition
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/combine-configs.md"
chapter_number: null
pdf_page: null
section: "Apply a Config Object"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - merging configs
  - config composition
  - extends
  - config arrays
  - shareable configurations

# === TYPED RELATIONSHIPS ===
prerequisites:
  - configuration-objects
  - define-config-helper
extends: []
related:
  - plugin-configuration
  - rule-configuration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I combine multiple ESLint configurations?"
  - "What is the difference between extends and cascading?"
  - "How do I apply a shareable config to specific files?"
  - "How do I use predefined configs like js/recommended?"
---

# Quick Definition
Combining configurations in ESLint uses the `extends` key to inherit from predefined configs, shareable config packages, and plugin configs, alongside cascading (multiple config objects in the array) for file-specific overrides.

# Core Definition
ESLint flat config supports two composition patterns: extends and cascading. The `extends` key within a configuration object accepts an array of strings (plugin config names), config objects, or config arrays, merging their rules, plugins, and language options into the current object. Cascading uses multiple config objects in the exported array, where later objects override earlier ones for matching files. Extends is for reusing external/shared configurations; cascading is for file-specific or directory-specific rule adjustments.

# Prerequisites
- configuration-objects (the unit being combined)
- define-config-helper (wraps the config array)

# Key Properties
1. `extends` accepts: strings (`"pluginName/configName"`), config objects, and config arrays
2. Predefined configs: `js/recommended` (from `@eslint/js` plugin) and `js/all`
3. Shareable config packages (e.g., `eslint-config-example`) can be used directly in `extends`
4. Plugin configs referenced by string require the plugin to be registered in `plugins` first
5. Cascading: later config objects override earlier ones on conflict
6. When using `extends`, always include a `files` key to avoid unintended global application
7. `basePath` can scope multiple extended configs to a subdirectory

# Construction / Recognition
Using predefined config with overrides:
```js
import js from "@eslint/js";
import { defineConfig } from "eslint/config";

export default defineConfig([{
  files: ["**/*.js"],
  plugins: { js },
  extends: ["js/recommended"],
  rules: { "no-unused-vars": "warn" },
}]);
```

Applying a shareable config array:
```js
import exampleConfigs from "eslint-config-example";
import { defineConfig } from "eslint/config";

export default defineConfig([{
  files: ["**/*.js"],
  extends: [exampleConfigs],
  rules: { "no-unused-vars": "warn" },
}]);
```

Cascading for file-specific rules:
```js
export default defineConfig([
  { rules: { semi: "error" } },
  { files: ["tests/**"], rules: { semi: "off" } },
]);
```

# Context & Application
Most real-world ESLint configurations combine multiple sources: a recommended base config, plugin-specific configs, and project-specific overrides. Understanding the interaction between extends (inheritance) and cascading (file-based overrides) is key to building maintainable config files.

# Examples
From `use/configure/configuration-files.md`: When to use extends vs cascading -- extends for reusing/inheriting configs, cascading for file-specific rules, progressive configuration, and directory-based settings.

From `use/configure/combine-configs.md`: A config object or config array imported from another module can be applied to a subset of files using `files` + `extends`.

# Relationships
## Builds Upon
- configuration-objects (the units being combined)
- define-config-helper (the top-level wrapper)

## Enables
- Modular, maintainable configuration from multiple sources

## Related
- plugin-configuration (plugin configs are a primary extends source)
- rule-configuration (rules are what gets merged/overridden)

# Common Errors
1. Omitting `files` when using `extends`, causing the extended config to apply to all files
2. Not registering a plugin in `plugins` before referencing its config by string in `extends`
3. Assuming cascading adds to rule options (later objects replace, not deep-merge, rule configs)

# Common Confusions
1. Thinking `extends` and cascading are interchangeable -- extends is for inheriting configs, cascading is for file-specific overrides
2. Not realizing that `js/all` changes with every ESLint release and is not recommended for production

# Source Reference
- `sources-md/eslint/use/configure/combine-configs.md`, all sections
- `sources-md/eslint/use/configure/configuration-files.md`, sections "Extending Configurations", "When to Use Extends vs Cascading"

# Verification Notes
Extracted from combine-configs and configuration-files documentation. The extends vs cascading guidance verified against both sources.
