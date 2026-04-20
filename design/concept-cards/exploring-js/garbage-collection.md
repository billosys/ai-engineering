---
# === CORE IDENTIFICATION ===
concept: Garbage Collection
slug: garbage-collection

# === CLASSIFICATION ===
category: types-values
subcategory: memory
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.6.2 Objects are passed by identity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - GC
  - automatic memory management

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-passed-by-identity
extends: []
related:
  - objects-overview
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

JavaScript uses garbage collection to automatically manage memory: objects that are no longer referenced are eventually removed from memory.

# Core Definition

"JavaScript uses *garbage collection* to automatically manage memory." (Ch. 14, &sect;14.6.2). When an object is no longer referenced by any variable or property, it becomes *garbage*. JavaScript will "automatically *garbage-collect* it (remove it from memory), at some point in time (possibly never if there is enough free memory)."

# Prerequisites

- **objects-passed-by-identity** -- GC relates to object identity/reference tracking

# Key Properties

1. Automatic: no manual memory management needed
2. Objects with no remaining references become garbage
3. Garbage collection timing is non-deterministic
4. May never collect if enough free memory exists
5. Applies to objects on the heap

# Construction / Recognition

```js
let obj = { prop: 'value' };
obj = {};
// Old { prop: 'value' } is now garbage
```

# Context & Application

Garbage collection means JavaScript developers don't need to manually free memory. Understanding it helps prevent memory leaks from unintended references.

# Examples

From the source text (Ch. 14, &sect;14.6.2):
```js
let obj = { prop: 'value' };
obj = {};
// Now the old value { prop: 'value' } is garbage
```

# Relationships

## Builds Upon
- **objects-passed-by-identity** -- references determine object lifetime

## Enables
- Automatic memory management

## Related
- **objects-overview** -- GC applies to objects

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Assuming objects are immediately freed when no longer referenced.
  **Correction**: GC runs at the engine's discretion; timing is non-deterministic.

# Common Confusions

- **Confusion**: Thinking setting a variable to `null` immediately frees memory.
  **Clarification**: It makes the old value eligible for GC, but collection happens at an unspecified time.

# Source Reference

Chapter 14: Values, Section 14.6.2, lines 299-312.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with example
- Cross-reference status: verified
