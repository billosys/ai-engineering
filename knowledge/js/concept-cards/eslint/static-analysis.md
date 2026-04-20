---
# === CORE IDENTIFICATION ===
concept: Static Analysis
slug: static-analysis

# === CLASSIFICATION ===
category: static-analysis
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/core-concepts/glossary.md"
chapter_number: null
pdf_page: null
section: "Static Analysis"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "static code analysis"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - eslint
  - abstract-syntax-tree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is static analysis?"
  - "How does static analysis differ from dynamic analysis?"
  - "What are the main types of static analysis tools?"
  - "Is ESLint a static analysis tool?"
---

# Quick Definition
Static analysis is the process of analyzing source code without building or running it; linters, formatters, and type checkers are all examples of static analysis tools.

# Core Definition
Static analysis examines source code without executing it to find problems, enforce patterns, or transform formatting. Linters such as ESLint, code formatters (like Prettier and dprint), and type checkers (like TypeScript) are all static analysis tools. Static analysis is distinct from dynamic analysis, which evaluates source code after it is built and executed -- unit tests, integration tests, and end-to-end tests are common examples of dynamic analysis.

# Prerequisites
Foundational concept with no prerequisites.

# Key Properties
1. **No execution required** -- Analyzes code without building or running it
2. **Three tool categories** -- Linters (pattern checking), formatters (code style), type checkers (type correctness)
3. **Complements dynamic analysis** -- Static and dynamic analysis serve different purposes; both are valuable
4. **AST-based** -- Static analysis tools typically convert code into an AST for examination

# Construction / Recognition
- Linters: Check code against rules (ESLint)
- Formatters: Reformat code appearance without changing logic (Prettier, dprint)
- Type checkers: Build full understanding of project types and data shapes (TypeScript)

# Context & Application
Static analysis is particularly valuable for JavaScript because, as a dynamic and loosely-typed language, JavaScript has no compilation step to catch errors. Static analysis tools fill this gap by finding problems before code is executed. ESLint is one of the most widely used static analysis tools in the JavaScript ecosystem.

# Examples
From use/core-concepts/glossary.md:
- "The process of analyzing source code without building or running it."
- "Linters such as ESLint, formatters, and type checkers are examples of static analysis tools."
- "Static analysis is different from dynamic analysis, which is the process of evaluating source code after it is built and executed."

From about/index.md:
- "Code linting is a type of static analysis that is frequently used to find problematic patterns or code that doesn't adhere to certain style guidelines."

# Relationships
## Enables
- eslint (linter)
- abstract-syntax-tree (core technique)

## Related
- rules
- parsers

# Common Errors
1. Thinking static analysis replaces testing -- static analysis and dynamic analysis (testing) are complementary approaches

# Common Confusions
1. **Linter vs. formatter vs. type checker** -- All are static analysis tools but serve different purposes: linters check patterns, formatters adjust style, type checkers verify types. ESLint is a linter, not a formatter or type checker
2. **Static vs. dynamic analysis** -- Static analysis examines code without running it; dynamic analysis (tests) evaluates running code

# Source Reference
- use/core-concepts/glossary.md: Static Analysis, Linter, Formatter (Tool), Type Checker definitions
- about/index.md: Linting as static analysis

# Verification Notes
- High confidence: Explicitly defined in the glossary with clear distinctions between tool types
