---
# === CORE IDENTIFICATION ===
concept: Processors
slug: processors

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
section: "Processor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint processor"
  - "custom processor"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - plugins
extends: []
related:
  - parsers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an ESLint processor?"
  - "How can ESLint lint code inside non-JavaScript files?"
  - "What is the difference between a parser and a processor?"
---

# Quick Definition
An ESLint processor extracts JavaScript code from other kinds of files (such as Markdown) so that ESLint can lint the embedded code, or manipulates JavaScript code before parsing.

# Core Definition
A processor is a part of a plugin that extracts JavaScript code from other file types, allowing ESLint to lint embedded code. Alternatively, processors can manipulate JavaScript code before it is parsed by ESLint. Processors enable ESLint to work with files that are not purely JavaScript by extracting the lintable portions.

# Prerequisites
- eslint: Processors extend ESLint's file handling
- plugins: Processors are distributed as part of plugins

# Key Properties
1. **Code extraction** -- Extracts JavaScript from non-JavaScript file types
2. **Pre-parse manipulation** -- Can manipulate JavaScript before parsing
3. **Plugin-bundled** -- Distributed as part of ESLint plugins
4. **File-type targeting** -- Configured to run on specific file extensions

# Construction / Recognition
- Configured in the `processor` property of a config object
- Part of a plugin package (e.g., `@eslint/markdown`)

# Context & Application
Processors are used when projects contain JavaScript embedded in other file types, such as code blocks in Markdown documentation, script sections in HTML files, or code within custom template formats. They allow a single ESLint setup to lint JavaScript across all these contexts.

# Examples
From use/core-concepts/index.md:
- "@eslint/markdown contains a custom processor that lets you lint JavaScript code inside of Markdown code blocks."

From use/core-concepts/glossary.md:
- "`@eslint/markdown` includes a processor that converts the text of code blocks in Markdown files into code that can be linted."

# Relationships
## Builds Upon
- plugins
- eslint

## Related
- parsers

# Common Errors
1. Confusing processors with parsers -- processors extract code from non-JS files; parsers convert code into an AST

# Common Confusions
1. **Processor vs. parser** -- A processor extracts JavaScript from other file types; a parser converts JavaScript into an AST. They operate at different stages of the linting pipeline

# Source Reference
- use/core-concepts/index.md: Custom Processors section
- use/core-concepts/glossary.md: Processor definition

# Verification Notes
- High confidence: Explicitly defined in both source files
