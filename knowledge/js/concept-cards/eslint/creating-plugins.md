---
# === CORE IDENTIFICATION ===
concept: Creating Plugins
slug: creating-plugins

# === CLASSIFICATION ===
category: extending
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/plugins.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint plugin"
  - "eslint-plugin"
  - "plugin authoring"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - custom-rules
extends:
  - eslint
related:
  - shareable-configurations
  - custom-processors
  - language-system
contrasts_with:
  - shareable-configurations

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you create an ESLint plugin?"
  - "What can a plugin contain?"
  - "What naming conventions should ESLint plugins follow?"
  - "How do you bundle configurations inside a plugin?"
---

# Quick Definition
An ESLint plugin is a JavaScript object that exposes custom rules, configurations, processors, and/or language definitions under a standardized structure for distribution as an npm package.

# Core Definition
A plugin is a JavaScript object with four optional top-level properties: `meta` (plugin name, version, and namespace), `rules` (custom rule definitions), `configs` (named configurations), and `processors` (named processors). Plugins can also include `languages` for non-JS linting support.

The `meta` object should contain `name` (matching the npm package name), `version`, and `namespace` (the prefix users employ to access the plugin's rules, e.g., `"example"` for `eslint-plugin-example`). The namespace enables `defineConfig()` to locate the plugin even when a user assigns a different key.

Rules are exported as key-value pairs where the key is the rule ID (must not contain `/`) and the value is the rule object. Configs can be arrays of config objects or single objects, and can reference the plugin itself for self-contained recommended presets.

# Prerequisites
- Understanding of ESLint rules
- Understanding of ESLint configuration

# Key Properties
1. **meta** -- Plugin name, version, and namespace for debugging, caching, and defineConfig discovery
2. **rules** -- Object mapping rule IDs to rule objects
3. **configs** -- Named configurations that can include the plugin's own rules
4. **processors** -- Named processor objects with preprocess/postprocess methods
5. **languages** -- Named language objects for non-JS linting (ESLint v9.7.0+)

# Construction / Recognition
```js
const plugin = {
    meta: {
        name: "eslint-plugin-example",
        version: "1.2.3",
        namespace: "example"
    },
    configs: {},
    rules: { "dollar-sign": { create(context) { /* ... */ } } },
    processors: {}
};
export default plugin;
```

# Context & Application
Plugins are the primary distribution mechanism for ESLint extensions. They are published to npm with `eslint` as a peer dependency (>=10.0.0) and keywords `["eslint", "eslintplugin", "eslint-plugin"]`. Users import plugins into `eslint.config.js`, assign them a namespace in the `plugins` key, and reference their rules as `"namespace/rule-id"`.

# Examples
From extend/plugins.md:
- Naming: unscoped packages begin with `eslint-plugin-`, scoped packages use `@scope/eslint-plugin-*`
- Bundled config: `Object.assign(plugin.configs, { recommended: [{ plugins: { example: plugin }, rules: { "example/dollar-sign": "error" } }] })`
- Usage: `extends: ["example/recommended"]` in defineConfig

From extend/custom-rule-tutorial.md:
- `const plugin = { rules: { "enforce-foo-bar": fooBarRule } };`

# Relationships
## Contains
- custom-rules
- shareable-configurations
- custom-processors
- language-system

## Related
- eslint

# Common Errors
1. Using `/` in a rule ID -- rule IDs in plugins must not contain `/`
2. Forgetting to list eslint as a peer dependency -- users need eslint installed separately
3. Assuming a plugin config is auto-applied -- users must explicitly include plugin configs in their configuration

# Common Confusions
1. **Plugin vs. shareable config** -- A plugin bundles rules, processors, and configs; a shareable config is just configuration. A plugin can contain shareable configs, but configs can also be published standalone.

# Source Reference
- extend/plugins.md: Complete plugin structure, naming conventions, config bundling, publishing guidelines
- extend/custom-rule-tutorial.md: Step-by-step tutorial showing plugin creation

# Verification Notes
- High confidence: directly extracted from the official plugins documentation
