---
# === CORE IDENTIFICATION ===
concept: Configuration Files
slug: configuration-files

# === CLASSIFICATION ===
category: core
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/core-concepts/glossary.md"
chapter_number: null
pdf_page: null
section: "Config File (Configuration File)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "config file"
  - "configuration file"
  - "eslint.config.js"
  - "eslint config"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
extends: []
related:
  - flat-config
  - rules
  - plugins
  - shareable-configurations
  - severity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an ESLint configuration file?"
  - "What goes in eslint.config.js?"
  - "What is a config array?"
  - "What is a config object?"
---

# Quick Definition
An ESLint configuration file is a JavaScript file (named `eslint.config.(c|m)js`) that exports a config array of config objects specifying rules, plugins, parsers, and file targeting for a project.

# Core Definition
A configuration file contains preferences for how ESLint should parse files and run rules. Each config file exports a config array -- an array of config objects that are evaluated in order, where later objects may override settings specified in earlier objects. Each config object may include properties describing which files to run on, how to handle different file types, which plugins to include, and how to run rules. Config files can include built-in rules, enforcement levels, plugins with custom rules, shareable configurations, and file targeting.

# Prerequisites
- eslint: Configuration files configure ESLint behavior

# Key Properties
1. **Named convention** -- Files are named `eslint.config.(c|m)?js`
2. **Config array** -- Exports an array of config objects
3. **Ordered evaluation** -- Config objects are evaluated in order; later objects override earlier ones
4. **Config objects** -- Each object specifies files, plugins, rules, and other settings
5. **defineConfig helper** -- Can use `defineConfig()` from `eslint/config` for authoring

# Construction / Recognition
```js
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    rules: {
      "prefer-const": "error",
    },
  },
]);
```

# Context & Application
Configuration files are the primary way to set up ESLint for a project. They define which rules are active, at what severity, with what options, and for which files. They also specify plugins, parsers, and processors. The flat config format (current) consolidates all configuration into a single file.

# Examples
From use/core-concepts/glossary.md:
- A config file enabling `prefer-const` at error severity using `defineConfig`
- An override config object targeting `*.test.js` files to disable `no-unused-expressions`

# Relationships
## Builds Upon
- eslint

## Enables
- rules (configuration)
- plugins (loading)
- parsers (specification)
- severity (assignment)

## Related
- flat-config
- shareable-configurations

# Common Errors
1. Using legacy `.eslintrc.*` format instead of the current `eslint.config.js` flat config format
2. Not understanding that config objects are evaluated in order -- placement matters for overrides

# Common Confusions
1. **Config array vs. config object** -- The file exports an array (config array); each element is a config object with specific settings
2. **Flat config vs. legacy config** -- Current format uses a single `eslint.config.js`; legacy format used `.eslintrc.*` files that could be nested in subdirectories

# Source Reference
- use/core-concepts/index.md: Configuration Files section
- use/core-concepts/glossary.md: Config File, Config Array, Config Object definitions

# Verification Notes
- High confidence: Explicitly defined in both source files with examples
