---
# === CORE IDENTIFICATION ===
concept: ESLint
slug: eslint

# === CLASSIFICATION ===
category: core
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "about/index.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "eslint"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - rules
  - configuration-files
  - plugins
  - parsers
contrasts_with:
  - formatters-linting

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is ESLint?"
  - "Why was ESLint created?"
  - "What is a JavaScript linter?"
  - "What is ESLint's design philosophy?"
---

# Quick Definition
ESLint is a configurable, open source JavaScript linter that helps developers find and fix problems in their code without executing it.

# Core Definition
ESLint is a static analysis tool originally created by Nicholas C. Zakas in June 2013. It allows developers to discover problems with their JavaScript code -- from potential runtime bugs to best-practice violations to styling issues -- without executing the code. The primary reason ESLint was created was to allow developers to create their own linting rules. ESLint is designed to have all rules completely pluggable: the default rules are written just like any plugin rules, following the same pattern for both rules and tests.

# Prerequisites
Foundational concept with no prerequisites.

# Key Properties
1. **Configurable** -- All rules are pluggable; nothing is hardcoded
2. **Pluggable architecture** -- Rule API and Formatter API are used by both bundled and custom implementations
3. **Agenda free** -- Does not promote any particular coding style
4. **Standalone rules** -- Every rule is independent; any rule can be turned off or on
5. **Three severity levels** -- Each rule can be set to off, warning, or error individually
6. **Node.js runtime** -- Written using Node.js for fast execution and easy npm installation
7. **Dynamic loading** -- Rules can be dynamically loaded at any point in time

# Construction / Recognition
- Install via npm
- Configure using `eslint.config.js` (flat config format)
- Run from CLI or use editor integrations
- Extend with plugins containing custom rules

# Context & Application
ESLint is used across JavaScript and web development projects to enforce code quality, catch bugs early, and maintain consistent coding practices. It integrates with editors and CI/CD pipelines. JavaScript, being dynamic and loosely-typed, is especially prone to developer error, making linting particularly valuable since there is no compilation step to catch issues.

# Examples
From about/index.md:
- "ESLint is an open source JavaScript linting utility originally created by Nicholas C. Zakas in June 2013."
- "The primary reason ESLint was created was to allow developers to create their own linting rules."

From use/core-concepts/index.md:
- "ESLint is a configurable JavaScript linter. It helps you find and fix problems in your JavaScript code."

# Relationships
## Enables
- rules
- configuration-files
- plugins
- parsers
- processors
- formatters-linting

## Related
- static-analysis
- abstract-syntax-tree

## Contrasts With
- Prettier (formatter, not linter)
- TypeScript (type checker, not linter)

# Common Errors
1. Thinking ESLint requires configuration to start -- it ships with built-in rules usable immediately
2. Confusing ESLint with a formatter -- ESLint is a linter; it has deprecated its formatting rules in favor of dedicated formatters

# Common Confusions
1. **ESLint vs. Prettier** -- ESLint is a linter that checks for code problems; Prettier is a formatter that reformats code appearance
2. **ESLint vs. TypeScript** -- ESLint checks patterns via rules on a single file's AST; TypeScript performs full type checking across files

# Source Reference
- about/index.md: Origin, philosophy, and design principles of ESLint
- use/core-concepts/index.md: "What is ESLint?" overview section

# Verification Notes
- High confidence: ESLint is explicitly defined in multiple source files
- Philosophy and design principles taken directly from about/index.md
