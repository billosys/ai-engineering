---
# === CORE IDENTIFICATION ===
concept: ESLint Source Code Object
slug: eslint-source-code-object

# === CLASSIFICATION ===
category: architecture
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "contribute/architecture/index.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "SourceCode"
  - "SourceCode class"
  - "ESLint SourceCode"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint-architecture
  - abstract-syntax-tree
extends: []
related:
  - rules
  - parsers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does ESLint represent parsed source code internally?"
  - "What is the SourceCode class?"
  - "How do rules access the AST and source text?"
  - "What methods were removed from SourceCode in v10?"
---

# Quick Definition
The `SourceCode` class represents parsed JavaScript source code and its AST, providing the primary interface through which rules access code structure, tokens, comments, and scope information.

# Core Definition
The `SourceCode` class (`lib/source-code/`) takes in source code text and the Program node of the AST representing that code. It serves as the central data structure that rules interact with during linting. The AST is produced with both line/column and range locations, enabling rules to report precise issue locations and retrieve source text related to any AST node. The `Linter` uses `espree` (or a configured parser) to produce the AST, then wraps it in a `SourceCode` instance. Rules access this object via `context.sourceCode` to inspect tokens, comments, scopes, and relationships between nodes.

# Prerequisites
- eslint-architecture: Understanding ESLint's component structure
- abstract-syntax-tree: Understanding of AST representation

# Key Properties
1. **Dual location tracking** -- The AST includes both line/column and range locations for flexible position reporting
2. **Token and comment access** -- Provides methods to access tokens, comments, and whitespace around nodes
3. **Scope analysis** -- Integrates with scope analysis to track variable declarations, references, and scopes
4. **Public API export** -- Exported as part of `require("eslint")` alongside Linter, ESLint, and RuleTester
5. **Program node range** -- In ESLint v10, the `Program` node range now spans the entire source text including leading/trailing comments and whitespace

# Construction / Recognition
- Created internally by the Linter after parsing source text
- Accessed by rules via `context.sourceCode`
- Contains methods like `getTokenBefore()`, `getTokenAfter()`, `isSpaceBetween()`
- In v10, deprecated methods `getTokenOrCommentBefore()`, `getTokenOrCommentAfter()`, `isSpaceBetweenTokens()`, and `getJSDocComment()` were removed

# Context & Application
The SourceCode object is the primary interface between ESLint's parsing layer and its rule execution layer. Plugin and rule authors must understand SourceCode to write rules that correctly inspect code structure. Integration developers use SourceCode when building tools that analyze ESLint's intermediate representations.

# Examples
From contribute/architecture/index.md:
- "`lib/source-code/` - this module is `SourceCode` class that is used to represent the parsed source code. It takes in source code and the Program node of the AST representing the code."

From use/migrate-to-10.0.0.md (v10 removals):
- `getTokenOrCommentBefore()` replaced by `getTokenBefore(nodeOrToken, { includeComments: true })`
- `isSpaceBetweenTokens()` replaced by `isSpaceBetween()`

# Relationships
## Part Of
- eslint-architecture

## Related
- parsers
- rules
- abstract-syntax-tree

## Contrasts With
- Raw source text (unstructured string vs. structured AST with location data)

# Common Errors
1. Using removed SourceCode methods in v10 -- `getTokenOrCommentBefore()`, `getJSDocComment()`, etc. have been removed
2. Assuming Program.range excludes comments -- in v10, Program.range covers the entire source text

# Common Confusions
1. **SourceCode vs. AST** -- SourceCode wraps the AST plus the raw text, providing convenience methods; the AST alone is just the tree structure
2. **context.getSourceCode() vs. context.sourceCode** -- The method form was deprecated in v9 and removed in v10; use the property form

# Source Reference
- contribute/architecture/index.md: SourceCode class description
- use/migrate-to-10.0.0.md: Removed SourceCode methods and Program node range changes

# Verification Notes
- High confidence: SourceCode is explicitly described in architecture docs
- v10 breaking changes for SourceCode are documented in migration guide
