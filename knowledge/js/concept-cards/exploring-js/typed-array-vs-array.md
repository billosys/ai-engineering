---
concept: Typed Arrays vs. Normal Arrays
slug: typed-array-vs-array
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Typed Arrays: handling binary data (advanced)"
chapter_number: 35
pdf_page: null
section: "35.2.5 Typed Arrays vs. normal Arrays"
extraction_confidence: high
aliases: []
prerequisites:
  - typed-arrays
  - array-creation
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Typed Arrays differ from normal Arrays in six ways: they have buffers (elements stored in ArrayBuffers), are initialized with zeros, have homogeneous element types with coercion, derive their fixed length from their buffer, have no holes, and lack `.concat()`.

# Core Definition

Typed Arrays have a `.length`, support bracket access `[]`, and have most standard Array methods. They differ from normal Arrays: elements stored in an associated ArrayBuffer, initialized with zeros, all elements share one type (coercion on set), length derived from buffer (never changes), no holes, and no `.concat()` method.

# Prerequisites

- **typed-arrays** -- understanding Typed Arrays
- **array-creation** -- for comparison

# Key Properties

1. Buffer-backed storage via ArrayBuffer
2. Initialized with zeros (vs. holes for `new Array(n)`)
3. Homogeneous type with coercion (257 in Uint8 becomes 1)
4. Fixed length
5. No holes possible
6. No `.concat()` (use `.set()` workaround)

# Construction / Recognition

```js
const ta = new Uint8Array(1);
ta[0] = 257;       // overflow: becomes 1
ta[0] = '2';       // coercion: becomes 2
typeof ta[0];      // 'number'
ta.buffer;         // ArrayBuffer
```

# Context & Application

Understanding these differences is essential when choosing between regular Arrays and Typed Arrays, or when porting code between them.

# Examples

```js
// Initialized with zeros
assert.deepEqual(new Uint8Array(4), Uint8Array.of(0, 0, 0, 0));

// Type coercion
const ta = new Uint8Array(1);
ta[0] = 257;
assert.equal(ta[0], 1); // 257 % 256

// Fixed length
const ta2 = new Uint16Array(2);
assert.equal(ta2.length, 2);
assert.deepEqual(ta2.buffer, new ArrayBuffer(4));
```

(Chapter 35, Section 35.2.5, lines 316-385)

# Relationships

## Builds Upon
- **typed-arrays** -- the comparison subject
- **array-creation** -- the comparison target

## Enables
- Informed choice between Array types

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Expecting Typed Array elements to store non-numeric values.
  **Correction**: All values are coerced to the array's numeric type.

# Common Confusions

- **Confusion**: Typed Arrays and normal Arrays have the same methods.
  **Clarification**: Typed Arrays lack `.concat()`, `.push()`, `.pop()`, and other length-changing methods.

# Source Reference

Chapter 35: Typed Arrays, Section 35.2.5, lines 316-385.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly enumerated differences
- Cross-reference status: verified
