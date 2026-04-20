---
concept: Namespace Import
slug: namespace-import
category: modules
subcategory: imports
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.6.3 Namespace imports"
extraction_confidence: high
aliases:
  - "star import"
  - "import * as"
prerequisites:
  - named-import
extends: []
related:
  - named-import
contrasts_with:
  - named-import
answers_questions:
  - "How do I import all exports from a module at once?"
---

# Quick Definition

A namespace import (`import * as name`) brings all named exports of a module into a single object whose properties are the exports.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, namespace imports are an alternative to named imports. The syntax `import * as myMath from './lib/my-math.mjs'` creates a module namespace object whose properties are the module's named exports.

# Prerequisites

- Named import

# Key Properties

1. Syntax: `import * as name from './module.mjs'`.
2. Creates a namespace object with all named exports as properties.
3. Default export appears as `.default` property.
4. Useful for accessing many exports from one module.

# Construction / Recognition

```js
import * as myMath from './lib/my-math.mjs';
myMath.square(3); // 9
```

# Context & Application

Use when a module has many exports and you want them grouped under a single namespace, or when you want to avoid name collisions.

# Examples

From the source text (Ch. 29, section 29.6.3):

```js
import * as myMath from './lib/my-math.mjs';
assert.equal(myMath.square(3), 9);
assert.deepEqual(Object.keys(myMath), ['LIGHT_SPEED', 'square']);
```

# Relationships

## Contrasts With
- **Named Import** -- named import selects specific exports; namespace import takes all

# Source Reference

Chapter 29: Modules, Section 29.6.3, lines 813-830.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with example
- Cross-reference status: verified
