---
# === CORE IDENTIFICATION ===
concept: Rules
slug: rules

# === CLASSIFICATION ===
category: rules
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/core-concepts/glossary.md"
chapter_number: null
pdf_page: null
section: "Rule"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint rules"
  - "lint rules"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - abstract-syntax-tree
extends: []
related:
  - severity
  - violations
  - plugins
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an ESLint rule?"
  - "What do ESLint rules check?"
  - "Can I create custom ESLint rules?"
  - "What are logical vs. stylistic rules?"
---

# Quick Definition
A rule is code that checks an AST for expected patterns and creates a violation when its expectation is not met.

# Core Definition
Rules are the core building block of ESLint. A rule validates whether code meets a certain expectation and defines what to do if it does not. Rules can also contain additional configuration options specific to that rule. ESLint contains hundreds of built-in rules, and users can create custom rules or use rules from plugins. Each rule is standalone, can be individually turned off or on, and can be set to a warning or error.

# Prerequisites
- eslint: The linter that executes rules
- abstract-syntax-tree: Rules operate on AST representations of code

# Key Properties
1. **AST-based checking** -- Rules inspect the AST to find expected or problematic patterns
2. **Configurable** -- Each rule can have its own options in addition to severity
3. **Standalone** -- Every rule is independent; no rule is "too important to turn off"
4. **Optional fixes** -- Rules may provide automatic fixes and/or suggestions
5. **Categorized** -- Rules are either logical (detect bugs/unused code) or stylistic (enforce preferences)

# Construction / Recognition
- Built-in rules are used like: `"prefer-const": "error"`
- Plugin rules use a prefix: `"@typescript-eslint/no-unused-vars": "warn"`
- Custom rules follow the same API as built-in rules

# Context & Application
Rules are configured in ESLint configuration files with a severity level and optional rule-specific options. They are run against the AST of each source file during linting. The combined violations from all rules form the linting report.

# Examples
From use/core-concepts/index.md:
- "the `semi` rule lets you specify whether or not JavaScript statements should end with a semicolon"

From use/core-concepts/glossary.md:
- Logical rules: `no-undef` (likely crashes), `no-sparse-arrays` (unintended behavior), `no-unused-vars` (unused code)
- Stylistic rules: enforce formatting preferences, naming conventions, or consistent syntax choices

# Relationships
## Builds Upon
- abstract-syntax-tree
- esquery-and-selectors

## Enables
- rule-fixes
- rule-suggestions
- violations

## Related
- severity
- configuration-files
- plugins

# Common Errors
1. Not understanding that rules must be individually enabled or included via a shareable config -- ESLint does not enable all rules by default
2. Confusing rule severity with rule options -- severity controls reporting level; options configure rule behavior

# Common Confusions
1. **Logical vs. stylistic rules** -- Logical rules detect bugs and problems; stylistic rules enforce preferences. ESLint has frozen stylistic rule features
2. **Built-in vs. plugin rules** -- Both follow the same API; plugin rules are loaded from external npm packages

# Source Reference
- use/core-concepts/index.md: Rules as core building block
- use/core-concepts/glossary.md: Rule, Logical Rule, Stylistic (Rule) definitions

# Verification Notes
- High confidence: Rules are explicitly defined in both source files
- Rule categories (logical, stylistic) taken from glossary
