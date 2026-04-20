---
concept: Tree-Shaking
slug: tree-shaking
category: web-development
subcategory: tooling
tier: foundational
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Next steps: overview of web development"
chapter_number: 49
pdf_page: null
section: "49.3.1.3 Bundlers"
extraction_confidence: high
aliases:
  - dead code elimination
prerequisites:
  - bundlers
extends: []
related:
  - javascript-tools-overview
contrasts_with: []
answers_questions:
  - "What JavaScript-related tools should I know about?"
---

# Quick Definition

Tree-shaking is a form of dead code elimination used by bundlers: only module exports that are actually imported somewhere (across all code, considering transitive imports) are included in the output.

# Core Definition

"Exploring JavaScript" Ch. 49: "Tree-shaking is a form of dead code elimination: only those module exports are put in the output that are imported somewhere (across all code, while considering transitive imports)." Also referenced in Ch. 47 regarding date library selection: "Tree-shaking can considerably reduce the size of a library."

# Prerequisites

- **Bundlers** -- tree-shaking is performed by bundlers

# Key Properties

1. Eliminates unused module exports from output
2. Considers transitive imports (imports of imports)
3. Functions are more amenable to tree-shaking than classes
4. Significantly reduces bundle size for large libraries

# Construction / Recognition

Not directly demonstrated with code. Tree-shaking happens automatically during the bundling process when using ES module syntax (`import`/`export`).

# Context & Application

Critical for keeping web application bundle sizes small. Particularly important when using large utility libraries where only a few functions are needed.

# Examples

From Ch. 47: "Tree-shaking can considerably reduce the size of a library. It is a technique of only deploying those exports of a library to a web server that are imported somewhere."

(Ch. 47, Section 47.1.1, lines 88-92)

# Relationships

## Builds Upon
- **Bundlers** -- tree-shaking is a bundler optimization

## Related
- **JavaScript tools overview** -- part of the build toolchain

# Common Errors

- **Error**: Using `require()` (CommonJS) instead of `import` (ES modules)
  **Correction**: Use ES module syntax for tree-shaking to work effectively

# Common Confusions

- **Confusion**: Tree-shaking removes all unused code
  **Clarification**: It specifically removes unused exports; side effects in modules may prevent removal

# Source Reference

Chapter 49: Next steps: overview of web development, Section 49.3.1.3, lines 310-313.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition
- Cross-reference status: verified against Ch. 47 reference
