---
# === CORE IDENTIFICATION ===
concept: Rule Configuration
slug: rule-configuration

# === CLASSIFICATION ===
category: rules-config
subcategory: rule severity
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/configure/rules.md"
chapter_number: null
pdf_page: null
section: "Rule Severities"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - configuring rules
  - rule severity
  - rules configuration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - configuration-objects
extends: []
related:
  - inline-config-comments
  - disable-directives
  - plugin-configuration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set rule severity in ESLint?"
  - "What are the three severity levels for ESLint rules?"
  - "How do I pass options to an ESLint rule?"
  - "How does rule merging work across config objects?"
---

# Quick Definition
Rule configuration controls which ESLint rules are active and at what severity level (`"off"`, `"warn"`, or `"error"`), optionally with rule-specific options, set via the `rules` property in configuration objects or via inline configuration comments.

# Core Definition
Rules are the core building block of ESLint. Each rule validates whether code meets an expectation and defines what happens when it does not. Rule configuration sets the severity and options for each rule. The three severity levels are: `"off"` (or `0`) to disable, `"warn"` (or `1`) to report without affecting exit code, and `"error"` (or `2`) to report and cause a non-zero exit code. Rules can accept additional options via array syntax: `["error", "option1", { optionKey: value }]`.

# Prerequisites
- configuration-objects (rules live inside config objects)

# Key Properties
1. Three severity levels: `"off"`/`0`, `"warn"`/`1`, `"error"`/`2`
2. Options passed as array: first element is severity, subsequent elements are rule-specific options
3. When multiple config objects specify the same rule, later objects override earlier ones
4. Overriding with just a severity string preserves existing options (e.g., `"warn"` keeps previously set options)
5. Plugin rules use `namespace/rule-name` format (e.g., `"example/rule1"`)
6. Configuration comments have the highest priority, applied after all file settings

# Construction / Recognition
Setting rules in a config file:
```js
export default defineConfig([
  {
    rules: {
      semi: "error",
      "no-unused-vars": "error",
      "prefer-const": ["error", { ignoreReadBeforeAssign: true }],
    },
  },
]);
```

Cascading: a later config can override just the severity while preserving options:
```js
// First config sets: semi: ["error", "never"]
// Second config sets: semi: "warn"
// Result: semi: ["warn", "never"]
```

# Context & Application
Rule configuration is the primary mechanism for customizing ESLint behavior. Rules are typically set to `"error"` for CI enforcement and `"warn"` when introducing new rules gradually or when rules may have false positives.

# Examples
From `use/configure/rules.md`: Disabling rules for test files by using a subsequent config object with `files: ["*-test.js", "*.spec.js"]` and setting the rule to `"off"`.

Plugin rules require the plugin namespace prefix:
```js
rules: {
  "example/rule1": "warn",
}
```

# Relationships
## Builds Upon
- configuration-objects (rules are a property of config objects)

## Enables
- Code quality enforcement in CI pipelines
- Gradual rule adoption via warn-then-error strategy

## Related
- inline-config-comments (per-file rule overrides via comments)
- disable-directives (suppressing rules for specific code)
- plugin-configuration (plugin rules use namespace/rule format)

# Common Errors
1. Using numeric severity (0/1/2) instead of strings -- both work but strings are clearer
2. Forgetting the namespace prefix for plugin rules
3. Assuming config comment rules can load plugins -- plugins must be loaded in the config file first

# Common Confusions
1. Thinking `"warn"` affects the exit code -- it does not; only `"error"` causes non-zero exit
2. Not realizing that overriding with just a severity string preserves previously configured options

# Source Reference
- `sources-md/eslint/use/configure/rules.md`, sections "Rule Severities", "Use Configuration Files", "Rules from Plugins"

# Verification Notes
Extracted from the rules configuration documentation. Severity behavior and cascading rules verified against examples.
