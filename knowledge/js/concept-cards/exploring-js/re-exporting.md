---
concept: Re-exporting
slug: re-exporting
category: modules
subcategory: exports
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.8 Re-exporting"
extraction_confidence: high
aliases:
  - "re-export"
  - "barrel file"
prerequisites:
  - named-export
extends: []
related:
  - namespace-import
contrasts_with: []
answers_questions:
  - "How do I re-export from another module?"
---

# Quick Definition

Re-exporting allows a module to export entities from another module as if they were its own, using `export { name } from './module.mjs'` or `export * from './module.mjs'`.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, a module can re-export one or more exports of another module. Named re-exports (`export { a as b } from`) select specific exports. Wildcard re-exports (`export * from`) re-export all named exports except the default. Namespace re-exports (ES2020, `export * as ns from`) create a namespace object as a named export.

# Prerequisites

- Named export

# Key Properties

1. Named re-export: `export { name } from './module.mjs'`.
2. Wildcard re-export (ES6): `export * from './module.mjs'` (excludes default).
3. Namespace re-export (ES2020): `export * as ns from './module.mjs'`.
4. Supports renaming: `export { internalFunc as func } from './module.mjs'`.

# Construction / Recognition

```js
export { internalFunc as func } from './internal.mjs';
export * from './internal.mjs';
export * as ns from './internal.mjs';
```

# Context & Application

Commonly used in "barrel" files (index modules) that aggregate exports from multiple sub-modules into a single entry point.

# Examples

From the source text (Ch. 29, section 29.8):

```js
// library.mjs
export {internalFunc as func, INTERNAL_DEF as DEF} from './internal.mjs';
export * from './internal.mjs';
export * as ns from './internal.mjs';
```

# Relationships

## Builds Upon
- **Named Export** -- re-exports are built on the export mechanism

# Common Errors

- **Error**: Expecting `export * from` to include the default export.
  **Correction**: Wildcard re-exports exclude the default export. Use named re-export for defaults.

# Source Reference

Chapter 29: Modules, Section 29.8, lines 1063-1110.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit syntax for all three forms
- Cross-reference status: verified
