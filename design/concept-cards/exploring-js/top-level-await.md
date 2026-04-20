---
concept: Top-Level Await
slug: top-level-await
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.3.1 Using await at the top levels of modules"
extraction_confidence: high
aliases:
  - module-level await
prerequisites:
  - await-operator
  - async-function
extends:
  - await-operator
related: []
contrasts_with: []
answers_questions:
  - "How do I use async/await to write asynchronous code?"
---

# Quick Definition

Top-level await (ES2022) allows using the `await` keyword at the top level of modules (outside any async function), enabling modules to perform asynchronous initialization.

# Core Definition

"Exploring JavaScript" Ch. 44: "We can use await at the top levels of modules." This was introduced in ES2022. Example use case includes dynamically importing modules with fallback.

# Prerequisites

- **Await operator** -- top-level await extends where `await` can be used
- **Async function** -- understanding how `await` works

# Key Properties

1. Introduced in ES2022
2. Only available in modules (not scripts)
3. Allows await outside of async functions at module top level
4. Importing module waits for the awaited Promise to settle

# Construction / Recognition

```js
let mylib;
try {
  mylib = await import('https://primary.example.com/mylib');
} catch {
  mylib = await import('https://secondary.example.com/mylib');
}
```

(Ch. 44, Section 44.3.1, lines 365-375)

# Context & Application

Used for module initialization that requires async operations: dynamic imports with fallback, loading configuration, establishing connections.

# Examples

See construction example above. (Ch. 44, Section 44.3.1, lines 369-374)

# Relationships

## Builds Upon
- **Await operator** -- extends to module top level

# Common Errors

- **Error**: Using top-level await in a script (non-module) context
  **Correction**: Top-level await is only available in modules

# Common Confusions

- **Confusion**: Top-level await blocks the entire application
  **Clarification**: It only blocks modules that depend on the current module

# Source Reference

Chapter 44: Async functions, Section 44.3.1, lines 363-378.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with example
- Cross-reference status: verified
