---
# === CORE IDENTIFICATION ===
concept: Parsers
slug: parsers

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
section: "Parser"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint parser"
  - "custom parser"
  - "Espree"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - abstract-syntax-tree
extends: []
related:
  - plugins
  - estree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an ESLint parser?"
  - "What is Espree?"
  - "How does ESLint parse TypeScript?"
  - "Can ESLint parse non-standard JavaScript?"
---

# Quick Definition
An ESLint parser is an object containing a method that reads source code strings and converts them into an AST that ESLint can evaluate; Espree is the built-in default parser.

# Core Definition
Parsers convert source code strings into an abstract syntax tree (AST) in a standardized format. By default, ESLint uses the built-in Espree parser, which generates an AST compatible with standard JavaScript runtimes and versions. Custom parsers let ESLint parse non-standard JavaScript syntax, such as TypeScript. Custom parsers are often included as part of shareable configurations or plugins, so they typically do not need to be configured directly.

# Prerequisites
- eslint: Parsers are used by ESLint to read source code
- abstract-syntax-tree: Parsers produce ASTs

# Key Properties
1. **Source-to-AST conversion** -- Reads source code strings and produces an AST
2. **Espree default** -- ESLint's built-in parser, compatible with standard JavaScript
3. **Custom parsers** -- Enable parsing of non-standard syntax (e.g., TypeScript, JSX)
4. **Plugin-bundled** -- Often distributed as part of plugins or shareable configs
5. **Configurable** -- Can be specified per config object for different file types

# Construction / Recognition
- Default: Espree (no configuration needed for standard JavaScript)
- TypeScript: `@typescript-eslint/parser`
- Configured in the `parser` property of a config object

# Context & Application
Parsers are essential for ESLint to understand the code it is linting. For standard JavaScript, the default Espree parser suffices. When working with TypeScript, Flow, or other JavaScript dialects, a custom parser must be configured to produce a valid AST that ESLint's rules can operate on.

# Examples
From use/core-concepts/index.md:
- "By default, ESLint uses the built-in Espree parser, which is compatible with standard JavaScript runtimes and versions."
- "@typescript-eslint/parser is a custom parser included in the typescript-eslint project that lets ESLint parse TypeScript code."

# Relationships
## Builds Upon
- abstract-syntax-tree
- estree

## Related
- plugins
- configuration-files

# Common Errors
1. Forgetting to configure a TypeScript parser when linting TypeScript files -- ESLint will fail to parse TS-specific syntax with Espree
2. Configuring a custom parser globally when it is only needed for specific file types

# Common Confusions
1. **Parser vs. plugin** -- A parser converts source code to an AST; a plugin provides rules. They are separate concerns, though often bundled together

# Source Reference
- use/core-concepts/index.md: Parsers section
- use/core-concepts/glossary.md: Parser definition

# Verification Notes
- High confidence: Explicitly defined in both source files with the same content
