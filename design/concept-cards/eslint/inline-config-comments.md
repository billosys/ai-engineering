---
# === CORE IDENTIFICATION ===
concept: Inline Config Comments
slug: inline-config-comments

# === CLASSIFICATION ===
category: rules-config
subcategory: inline configuration
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/rules.md"
chapter_number: null
pdf_page: null
section: "Use configuration comments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - configuration comments
  - eslint comments
  - "/* eslint */ comments"
  - inline config

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rule-configuration
extends: []
related:
  - disable-directives
  - global-declarations
contrasts_with:
  - disable-directives

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure a rule for a single file using comments?"
  - "What is the syntax for ESLint inline configuration comments?"
  - "How do I add a description to an inline config comment?"
  - "How can I prevent inline config comments from being used?"
---

# Quick Definition
Inline config comments are `/* eslint */` block comments placed inside source files that configure rule severity and options for that specific file, taking the highest priority over all configuration file settings.

# Core Definition
Inline configuration comments use the `/* eslint rule: severity */` syntax to override rule settings within a single file. They support the same severity levels and array-based options as configuration files. These comments have the highest priority and are applied after all configuration file settings. They can include descriptions separated by `--` for documentation purposes. The `noInlineConfig` linter option and `reportUnusedInlineConfigs` setting can control their behavior.

# Prerequisites
- rule-configuration (understanding severity levels and options)

# Key Properties
1. Syntax: `/* eslint eqeqeq: "off", curly: "error" */`
2. Options use array literal syntax: `/* eslint quotes: ["error", "double"], curly: 2 */`
3. Highest priority -- overrides all configuration file settings
4. Descriptions separated by `--`: `/* eslint semi: "error" -- Reason here */`
5. Can be disabled project-wide via `linterOptions.noInlineConfig: true`
6. Unused inline configs can be reported via `linterOptions.reportUnusedInlineConfigs`
7. Cannot load plugins -- plugins must be loaded in the config file

# Construction / Recognition
Basic inline config:
```js
/* eslint eqeqeq: "off", curly: "error" */
```

With options:
```js
/* eslint quotes: ["error", "double"], curly: 2 */
```

With description:
```js
/* eslint eqeqeq: "off", curly: "error" -- Here's why this is necessary. */
```

Global variable declarations also use inline comments:
```js
/* global var1, var2:writable */
```

# Context & Application
Inline config comments are used when a specific file needs different rule settings than the project-wide configuration. They are useful for exceptions but should be used sparingly. The ESLint documentation recommends preferring configuration files over inline comments for consistent project-wide rule handling.

# Examples
From `use/configure/rules.md`: Plugin rules can be used in config comments if the plugin is loaded in the config file:
```js
/* eslint "example/rule1": "error" */
```

Disabling inline config project-wide:
```js
export default defineConfig([{
  linterOptions: { noInlineConfig: true },
}]);
```

# Relationships
## Builds Upon
- rule-configuration (uses the same severity and options format)

## Enables
- Per-file rule overrides without changing config files

## Related
- global-declarations (`/* global */` comments for declaring globals)

## Contrasts With
- disable-directives: Inline config comments (`/* eslint */`) set rule severity; disable directives (`/* eslint-disable */`) suppress rule reporting entirely. They are different comment types with different purposes.

# Common Errors
1. Trying to load plugins via inline comments -- plugins must be in the config file
2. Starting description lines with `*` after the separator (breaks parsing)
3. Not realizing inline configs override everything from config files

# Common Confusions
1. Mixing up `/* eslint rule: "off" */` (inline config) with `/* eslint-disable rule */` (disable directive) -- they have different semantics
2. Thinking `reportUnusedInlineConfigs` and `reportUnusedDisableDirectives` are the same setting

# Source Reference
- `sources-md/eslint/use/configure/rules.md`, sections "Use configuration comments", "Configuration Comment Descriptions", "Report unused eslint inline config comments"

# Verification Notes
Extracted from rules configuration documentation. The distinction between inline config and disable directives is clearly documented.
