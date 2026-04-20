---
# === CORE IDENTIFICATION ===
concept: Plugins
slug: plugins

# === CLASSIFICATION ===
category: core
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/core-concepts/glossary.md"
chapter_number: null
pdf_page: null
section: "Plugin"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint plugin"
  - "eslint-plugin"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
extends: []
related:
  - rules
  - shareable-configurations
  - parsers
  - processors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an ESLint plugin?"
  - "What can an ESLint plugin contain?"
  - "How do plugins extend ESLint?"
---

# Quick Definition
An ESLint plugin is an npm module that can contain a set of rules, configurations, processors, and languages to extend ESLint's capabilities.

# Core Definition
Plugins are npm packages that extend ESLint with custom rules, configurations, processors, and language support. A popular use case is enforcing best practices for specific frameworks or libraries. Plugins can support JavaScript extensions (like TypeScript), libraries (like React), and frameworks (like Angular). Many plugins provide shareable configs with names like "recommended" that enable a suggested starting set of rules.

# Prerequisites
- eslint: Plugins extend ESLint's functionality

# Key Properties
1. **npm modules** -- Distributed as npm packages
2. **Multi-purpose** -- Can contain rules, configurations, processors, and languages
3. **Framework support** -- Commonly used to enforce framework-specific best practices
4. **Shareable configs** -- Often provide "recommended" configurations
5. **Composable** -- Multiple plugins can be combined in a single config file

# Construction / Recognition
- Installed via npm: `npm install eslint-plugin-react`
- Referenced in config files within the `plugins` property of config objects
- Plugin rules use a namespaced prefix: `"react/jsx-uses-vars": "error"`

# Context & Application
Plugins are the primary extension mechanism for ESLint. They allow the community to create and share rules for specific ecosystems. Most JavaScript frameworks and libraries have associated ESLint plugins that codify best practices.

# Examples
From use/core-concepts/index.md:
- "An ESLint plugin is an npm module that can contain a set of ESLint rules, configurations, processors, and languages."
- "@angular-eslint/eslint-plugin contains best practices for using the Angular framework."

From use/core-concepts/glossary.md:
- `eslint-plugin-solid` provides a shareable recommended config

# Relationships
## Builds Upon
- eslint

## Enables
- rules (custom)
- shareable-configurations
- processors

## Related
- configuration-files
- parsers

# Common Errors
1. Forgetting to include the plugin in the config file's `plugins` property before using its rules
2. Confusing plugin configs with standalone shareable configs -- plugins may contain configs, but not all shareable configs are plugins

# Common Confusions
1. **Plugins vs. shareable configs** -- A plugin is a package that can contain rules, configs, and processors; a shareable config is just a config that can be shared. Plugins often include shareable configs

# Source Reference
- use/core-concepts/index.md: Plugins section
- use/core-concepts/glossary.md: Plugin definition

# Verification Notes
- High confidence: Explicitly defined in both source files
