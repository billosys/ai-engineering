---
concept: Live Bindings
slug: live-bindings
category: modules
subcategory: imports
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.9.1 Imports are read-only views on exports"
extraction_confidence: high
aliases:
  - "read-only views"
  - "live imports"
prerequisites:
  - named-import
extends: []
related:
  - ecmascript-module
contrasts_with: []
answers_questions:
  - "How do imports stay synchronized with exports?"
---

# Quick Definition

Imports are live, read-only views on exports: they always reflect the current value of the exported variable but cannot be reassigned by the importer.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, when importing a variable, the connection to the exported variable is live. Changes to the exported value are visible through the import. However, the import binding itself is read-only -- it cannot be reassigned. This behavior is crucial for supporting transparent cyclic imports and is enabled by the static structure of ES modules.

# Prerequisites

- Named import

# Key Properties

1. Imports reflect the current value of exports (live connection).
2. Imports are read-only (cannot be reassigned).
3. Enables transparent support for cyclic imports.
4. Facilitated by the static structure of ESM.

# Construction / Recognition

```js
// counter.mjs
export let counter = 3;
export function incCounter() { counter++; }

// main.mjs
import { counter, incCounter } from './counter.mjs';
assert.equal(counter, 3);
incCounter();
assert.equal(counter, 4); // live!
```

# Context & Application

Understanding live bindings is important for module design, especially when using mutable exports or dealing with cyclic dependencies.

# Examples

From the source text (Ch. 29, section 29.9.1):

```js
import { counter, incCounter } from './counter.mjs';
assert.equal(counter, 3);
incCounter();
assert.equal(counter, 4);
```

# Relationships

## Builds Upon
- **Named Import** -- live bindings apply to named imports

# Common Confusions

- **Confusion**: Thinking imports are copies of exported values.
  **Clarification**: Imports are live views -- they always reflect the current exported value.

# Source Reference

Chapter 29: Modules, Section 29.9.1, lines 1112-1160.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit demonstration with mutable export
- Cross-reference status: verified
