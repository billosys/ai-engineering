---
# === CORE IDENTIFICATION ===
concept: defineConfig Helper
slug: define-config-helper

# === CLASSIFICATION ===
category: configuration
subcategory: config helpers
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/configuration-files.md"
chapter_number: null
pdf_page: null
section: "Configuration File"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - defineConfig
  - defineConfig()
  - eslint defineConfig

# === TYPED RELATIONSHIPS ===
prerequisites:
  - configuration-objects
extends: []
related:
  - configuration-objects
  - combining-configurations
  - file-ignoring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is defineConfig() and why should I use it?"
  - "How do I get type-safe ESLint configuration?"
  - "What helpers does eslint/config export?"
---

# Quick Definition
`defineConfig()` is a helper function imported from `"eslint/config"` that wraps a configuration array to provide type safety and editor autocompletion when authoring ESLint flat config files.

# Core Definition
The `defineConfig()` function accepts an array of configuration objects and returns it in a form that provides type information for editors and TypeScript. It is the recommended way to define ESLint configuration in flat config files. The companion `globalIgnores()` helper, also exported from `"eslint/config"`, creates a configuration object that acts as a global ignore pattern.

# Prerequisites
- configuration-objects (understanding what goes inside the array)

# Key Properties
1. Imported from `"eslint/config"` (ESM: `import { defineConfig } from "eslint/config"`, CJS: `const { defineConfig } = require("eslint/config")`)
2. Accepts an array of configuration objects, strings, or nested arrays
3. Provides type checking and autocompletion in editors
4. Does not alter runtime behavior -- purely a developer experience improvement
5. `globalIgnores()` is a companion helper for creating global ignore config objects

# Construction / Recognition
ESM usage:
```js
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    rules: {
      semi: "error",
    },
  },
]);
```

CommonJS usage:
```js
const { defineConfig } = require("eslint/config");

module.exports = defineConfig([
  {
    rules: {
      semi: "error",
    },
  },
]);
```

Using `globalIgnores()`:
```js
import { defineConfig, globalIgnores } from "eslint/config";

export default defineConfig([
  globalIgnores([".config/", "dist/"]),
  {
    rules: { semi: "error" },
  },
]);
```

# Context & Application
`defineConfig()` is used in virtually every modern ESLint configuration file. It appears at the top level as the default export wrapper. It is especially valuable in TypeScript config files (`eslint.config.ts`) where type checking catches misconfigurations at authoring time.

# Examples
From `use/configure/configuration-files.md`: Every example in the documentation uses `defineConfig()` to wrap the exported configuration array.

# Relationships
## Builds Upon
- configuration-objects (the objects inside the array)

## Enables
- Type-safe configuration authoring
- Editor autocompletion for config properties

## Related
- file-ignoring (globalIgnores companion helper)
- combining-configurations (defineConfig accepts nested arrays and extends)

# Common Errors
1. Forgetting to wrap the config array with `defineConfig()` (config still works but loses type safety)
2. Passing a single object instead of an array to `defineConfig()`

# Common Confusions
1. Thinking `defineConfig()` changes runtime behavior -- it is purely for developer experience
2. Confusing `globalIgnores()` with the `ignores` property inside a config object

# Source Reference
- `sources-md/eslint/use/configure/configuration-files.md`, section "Configuration File"

# Verification Notes
Extracted from configuration files documentation. Every code example in the docs uses defineConfig().
