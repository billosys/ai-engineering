---
# === CORE IDENTIFICATION ===
concept: Global Declarations
slug: global-declarations

# === CLASSIFICATION ===
category: configuration
subcategory: language settings
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/language-options.md"
chapter_number: null
pdf_page: null
section: "Specify Globals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - globals configuration
  - global variables
  - languageOptions.globals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - language-options
extends: []
related:
  - configuration-objects
  - inline-config-comments
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I tell ESLint about global variables like window or process?"
  - "What is the difference between writable and readonly globals?"
  - "How do I use the globals npm package with ESLint?"
  - "How do I declare globals inline with comments?"
---

# Quick Definition
Global declarations tell ESLint which global variables exist at runtime, using `languageOptions.globals` in config files or `/* global */` comments in source files, so rules like `no-undef` can correctly identify undefined variables.

# Core Definition
ESLint makes no assumptions about what global variables exist in the execution environment. The `languageOptions.globals` property accepts an object mapping variable names to access levels: `"writable"` (can be reassigned), `"readonly"` (cannot be reassigned), or `"off"` (explicitly mark as unavailable). ECMAScript standard built-in globals are automatically enabled based on `ecmaVersion`, but environment-specific globals (browser, Node.js, Jest) must be configured manually or via the `globals` npm package.

# Prerequisites
- language-options (globals are set within languageOptions)

# Key Properties
1. Config file syntax: `languageOptions: { globals: { varName: "writable" | "readonly" | "off" } }`
2. Comment syntax: `/* global var1, var2:writable */`
3. `"off"` disables a global (useful for removing a global from a predefined set)
4. The `globals` npm package provides predefined sets: `globals.browser`, `globals.node`, `globals.jest`, etc.
5. Multiple global sets can be spread together: `{ ...globals.browser, ...globals.jest }`
6. Legacy values `true`/`"writeable"` map to `"writable"`; `false`/`"readable"` map to `"readonly"` (deprecated)

# Construction / Recognition
Config file:
```js
import globals from "globals";
import { defineConfig } from "eslint/config";

export default defineConfig([{
  languageOptions: {
    globals: {
      ...globals.browser,
      ...globals.jest,
      MY_APP_GLOBAL: "readonly",
    },
  },
}]);
```

Inline comment:
```js
/* global var1, var2:writable */
```

Disabling a specific global:
```js
languageOptions: {
  globals: { Promise: "off" },
}
```

# Context & Application
Global declarations are essential for rules like `no-undef` that check whether variables are defined. Without proper globals configuration, ESLint reports false positives for legitimate runtime globals like `window`, `document`, `process`, or test framework helpers like `describe` and `it`.

# Examples
From `use/configure/language-options.md`: Adding browser and Jest globals simultaneously using the `globals` package spread syntax.

From `use/configure/configuration-files.md`: Cascading globals -- test files get `it` and `describe` in addition to project-wide globals through config object merging.

# Relationships
## Builds Upon
- language-options (globals are a sub-property of languageOptions)

## Enables
- Accurate `no-undef` rule behavior
- Environment-specific linting (browser, Node, test)

## Related
- inline-config-comments (`/* global */` comments serve the same purpose inline)
- configuration-objects (globals merge during config cascading)

# Common Errors
1. Not installing the `globals` npm package and trying to use `globals.browser`
2. Using deprecated boolean values (`true`/`false`) instead of `"writable"`/`"readonly"`
3. Forgetting to configure test globals, causing `no-undef` errors for `describe`/`it`

# Common Confusions
1. Thinking ESLint automatically knows about browser or Node.js globals -- it does not
2. Confusing `"writable"` (the variable can be reassigned) with "the variable exists"

# Source Reference
- `sources-md/eslint/use/configure/language-options.md`, section "Specify Globals"

# Verification Notes
Extracted from language options documentation. The globals package integration and spread pattern verified against examples.
