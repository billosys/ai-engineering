---
concept: Tree Shaking
slug: tree-shaking
category: tooling
subcategory: bundling
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 660
section: "17.5 Code Bundling"
extraction_confidence: high
aliases:
  - dead code elimination
prerequisites:
  - code-bundlers
extends:
  - code-bundlers
related: []
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

Tree shaking is a bundler optimization that analyzes which exports from imported modules are actually used and omits unused code from the final bundle, reducing file size.

# Core Definition

When you import a module into your program but only use a few of its features, a good bundler tool can analyze the code to determine which parts are unused and omit them from the bundle. This feature goes by the whimsical name of "tree-shaking" (Flanagan, Ch. 17, p. 660).

# Prerequisites

- **code-bundlers** — Tree shaking is a bundler feature.

# Key Properties

1. Removes unused exports from the bundle.
2. Relies on static analysis of ES6 `import`/`export` syntax.
3. Does not work well with CommonJS `require()` (dynamic, not statically analyzable).
4. Results in smaller bundle sizes.

# Construction / Recognition

Tree shaking is automatic in modern bundlers when using ES6 module syntax. No special code is needed -- just use `import`/`export` consistently.

# Context & Application

Important for production builds where bundle size directly affects page load time and user experience.

# Examples

From the source (p. 660): If you import a library but only use one function, tree shaking removes all other unused functions from the bundle.

# Relationships

## Builds Upon
- **code-bundlers** — A bundler optimization

## Enables
- Smaller bundle sizes for faster page loads

## Related
- (None)

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `require()` (CommonJS) and expecting tree shaking to work.
  **Correction**: Tree shaking works best with ES6 `import`/`export` syntax, which is statically analyzable.

# Common Confusions

- **Confusion**: Tree shaking removes all unused code.
  **Clarification**: Tree shaking works at the module export level. Side-effectful code may be retained even if its exports are unused.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.5, page 660.

# Verification Notes

- Definition source: Direct quote from source
- Confidence rationale: Concise, clear definition
- Uncertainties: None
- Cross-reference status: Verified
