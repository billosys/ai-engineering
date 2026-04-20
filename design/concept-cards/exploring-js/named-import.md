---
concept: Named Import
slug: named-import
category: modules
subcategory: imports
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.6.2 Named imports"
extraction_confidence: high
aliases:
  - "named imports"
prerequisites:
  - named-export
extends: []
related:
  - namespace-import
  - default-import
contrasts_with:
  - namespace-import
  - default-import
answers_questions:
  - "How do I import and export modules?"
---

# Quick Definition

A named import selectively brings specific named exports from a module into the current scope, using curly braces syntax with optional renaming via `as`.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, named imports use the syntax `import { name1, name2 as alias } from './module.mjs'`. They can rename imports via `as`. Named imports are not destructuring despite similar syntax: renaming uses `as` (not `:`), and nesting is not allowed. Imports are read-only live views on exports.

# Prerequisites

- Named export

# Key Properties

1. Syntax: `import { name } from './module.mjs'`.
2. Renaming: `import { name as alias } from './module.mjs'`.
3. Not destructuring despite similar appearance.
4. Imports are read-only views (can't reassign).
5. Live bindings: reflect current exported value.

# Construction / Recognition

```js
import { square, LIGHT_SPEED } from './lib/my-math.mjs';
import { square as sq } from './lib/my-math.mjs';
```

# Context & Application

The most common import style. Use when you need specific exports from a module. Supports tree-shaking by bundlers.

# Examples

From the source text (Ch. 29, section 29.6.2):

```js
import {square} from './lib/my-math.mjs';
assert.equal(square(3), 9);
```

# Relationships

## Builds Upon
- **Named Export** -- named imports consume named exports

## Contrasts With
- **Namespace Import** -- imports everything as one object vs. specific items
- **Default Import** -- different syntax, no curly braces

# Common Confusions

- **Confusion**: Named imports use destructuring.
  **Clarification**: They look similar but differ: renaming uses `as` not `:`, and they can't be nested.

# Source Reference

Chapter 29: Modules, Section 29.6.2, lines 754-800.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit syntax and distinction from destructuring
- Cross-reference status: verified
