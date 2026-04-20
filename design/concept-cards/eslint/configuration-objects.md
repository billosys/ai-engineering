---
# === CORE IDENTIFICATION ===
concept: Configuration Objects
slug: configuration-objects

# === CLASSIFICATION ===
category: configuration
subcategory: config structure
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/configuration-files.md"
chapter_number: null
pdf_page: null
section: "Configuration Objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - config object
  - flat config object
  - eslint config object

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - define-config-helper
  - rule-configuration
  - language-options
  - plugin-configuration
  - file-ignoring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What properties can an ESLint configuration object contain?"
  - "How does ESLint determine which config objects apply to a file?"
  - "What is the structure of a flat config object?"
---

# Quick Definition
A configuration object is the fundamental unit of ESLint's flat config system, containing properties like `files`, `ignores`, `rules`, `plugins`, `languageOptions`, and `linterOptions` that define how ESLint should lint a set of files.

# Core Definition
Each configuration object contains all the information ESLint needs to execute on a set of files. An ESLint configuration file (`eslint.config.js`) exports an array of these objects. When multiple configuration objects match a given filename, they are merged (cascaded), with later objects overriding earlier ones on conflict. Objects without `files` or `ignores` automatically apply to any file matched by any other configuration object.

# Prerequisites
- Basic understanding of JavaScript modules (ESM or CommonJS)

# Key Properties
1. `name` -- optional string for identifying the config in error messages and the config inspector
2. `files` -- array of glob patterns indicating which files the config applies to
3. `ignores` -- array of glob patterns for files to exclude; when used alone (without other keys), acts as global ignores
4. `extends` -- array of strings, config objects, or config arrays to inherit from
5. `rules` -- object mapping rule names to severity/options
6. `plugins` -- object mapping plugin namespaces to plugin objects
7. `languageOptions` -- object with `ecmaVersion`, `sourceType`, `globals`, `parser`, `parserOptions`
8. `linterOptions` -- object with `noInlineConfig`, `reportUnusedDisableDirectives`, `reportUnusedInlineConfigs`
9. `processor` -- object or string specifying a processor from a plugin
10. `settings` -- object of shared data available to all rules
11. `basePath` -- string specifying a subdirectory scope for the config

# Construction / Recognition
A minimal config file exporting a single configuration object:
```js
// eslint.config.js
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    files: ["**/*.js"],
    rules: {
      semi: "error",
      "prefer-const": "error",
    },
  },
]);
```

Glob patterns in `files` and `ignores` use minimatch syntax and are evaluated relative to the `eslint.config.js` location.

# Context & Application
Configuration objects are the building blocks of every ESLint setup in the flat config format. Understanding their structure is essential for setting up linting rules, targeting specific file types, integrating plugins, and controlling parser behavior.

# Examples
From `use/configure/configuration-files.md`: A cascading example where two config objects merge `languageOptions.globals` -- all JS files get `MY_CUSTOM_GLOBAL`, while test files additionally get `it` and `describe`.

Config objects without `files` apply universally: a `{ rules: { semi: "error" } }` object applies `semi` to all files matched by any other config.

# Relationships
## Builds Upon
- JavaScript module system (ESM / CommonJS)

## Enables
- rule-configuration (rules are set within config objects)
- language-options (languageOptions property)
- plugin-configuration (plugins property)
- file-ignoring (ignores property)

## Related
- define-config-helper (wraps config arrays for type safety)
- combining-configurations (merging multiple config sources)

# Common Errors
1. Forgetting that config objects without `files` apply to all matched files, not no files
2. Using `ignores` alone with other keys, mistakenly expecting global ignore behavior (global ignores require `ignores` as the only key)
3. Not realizing that later config objects override earlier ones during cascading

# Common Confusions
1. Thinking `ignores` always acts globally -- it only does so when no other keys are present in the same object
2. Confusing `files` glob patterns with `.gitignore` patterns (ESLint uses minimatch, not gitignore syntax)

# Source Reference
- `sources-md/eslint/use/configure/configuration-files.md`, section "Configuration Objects"

# Verification Notes
Extracted from the primary configuration files documentation. All properties listed directly from the official docs.
