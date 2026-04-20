---
# === CORE IDENTIFICATION ===
concept: Ways to Extend ESLint
slug: ways-to-extend-eslint

# === CLASSIFICATION ===
category: extending
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/ways-to-extend.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint extension points"
  - "extending ESLint"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
extends:
  - eslint
related:
  - custom-rules
  - creating-plugins
  - custom-parsers
  - custom-processors
  - custom-formatters
  - shareable-configurations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the different ways to extend ESLint?"
  - "How do plugins, custom rules, parsers, processors, formatters, and shareable configs relate to each other?"
  - "When should I create a plugin versus a shareable config?"
---

# Quick Definition
ESLint is highly pluggable and provides six primary extension points: plugins (which bundle rules, processors, configs, and languages), custom rules, custom parsers, custom processors, custom formatters, and shareable configurations.

# Core Definition
ESLint's architecture is designed for extensibility. Plugins are the central packaging mechanism: they can contain custom rules, processors, configurations, and language definitions. Shareable configs are pre-defined configurations that can be published independently or as part of a plugin. Custom formatters control how linting results are displayed. Custom parsers extend ESLint to support new language features or non-standard syntax by transforming code into an AST.

# Prerequisites
- Understanding of ESLint core concepts (rules, configuration)

# Key Properties
1. **Plugins** -- Bundle custom rules, processors, configs, and languages into shareable npm packages
2. **Custom Rules** -- Validate code against expectations beyond the built-in rule set
3. **Shareable Configs** -- Pre-defined configurations published as npm packages for reuse across projects
4. **Custom Formatters** -- Control the display format of linting results
5. **Custom Parsers** -- Transform non-standard code into ASTs that ESLint can analyze
6. **Custom Processors** -- Extract lintable code from non-JavaScript files (e.g., JS inside Markdown)

# Construction / Recognition
- Plugins are npm packages following naming conventions: `eslint-plugin-*` or `@scope/eslint-plugin-*`
- Shareable configs are npm packages: `eslint-config-*` or `@scope/eslint-config-*`
- Custom formatters are npm packages: `eslint-formatter-*`
- All extensions integrate through `eslint.config.js` (flat config format)

# Context & Application
Frontend frameworks like React and Vue require custom rules outside of ESLint's core. Plugins like `eslint-plugin-react` bundle framework-specific rules. Shareable configs like `eslint-config-airbnb` bundle entire style guides. Custom parsers like `@typescript-eslint/parser` enable TypeScript linting. Custom formatters like `eslint-formatter-gitlab` output results for specific CI tools.

# Examples
From extend/ways-to-extend.md:
- "Plugins let you add your own ESLint custom rules and custom processors to a project."
- "ESLint shareable configs are pre-defined configurations for ESLint that you can use in your projects."
- "Custom parsers are a way to extend ESLint to support the linting of new language features or custom syntax in your code."

# Relationships
## Enables
- custom-rules
- creating-plugins
- custom-parsers
- custom-processors
- custom-formatters
- shareable-configurations

## Related
- eslint
- rules

# Common Errors
1. Confusing plugins with shareable configs -- plugins can contain configs, but shareable configs can also be published independently
2. Thinking custom parsers are only for new languages -- they can also extend the built-in parser for non-standard syntax

# Source Reference
- extend/ways-to-extend.md: Overview of all ESLint extension points

# Verification Notes
- High confidence: directly summarizes the official overview document
