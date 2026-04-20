---
concept: Typed Arrays
slug: typed-arrays
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Typed Arrays: handling binary data (advanced)"
chapter_number: 35
pdf_page: null
section: "35.1 The Typed Array API: containers for binary data"
extraction_confidence: high
aliases:
  - "TypedArray"
  - "Uint8Array"
  - "Int16Array"
  - "Float32Array"
prerequisites:
  - array-creation
extends: []
related:
  - array-buffer
  - data-view
contrasts_with:
  - array-creation
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Typed Arrays are Array-like views over binary data (ArrayBuffers) where all elements have the same fixed numeric type (e.g., Uint8, Int16, Float32), providing efficient handling of binary data for WebGL, WebGPU, WebAssembly, and file processing.

# Core Definition

The Typed Array API stores binary data in ArrayBuffer instances. Typed Arrays are view objects that let us access the data as an indexed sequence of elements that all have the same type. Available types include Uint8Array, Int8Array, Uint16Array, Int16Array, Uint32Array, Int32Array, Float16Array, Float32Array, Float64Array, BigInt64Array, BigUint64Array, and Uint8ClampedArray. Typed Arrays were originally created for WebGL and standardized in ES6.

# Prerequisites

- **array-creation** -- understanding regular arrays for comparison

# Key Properties

1. Introduced in ES2015 (ES6), originally spec'd in 2011
2. All elements have the same numeric type
3. Backed by an ArrayBuffer (accessed via `.buffer`)
4. Initialized with zeros (unlike regular Arrays)
5. Fixed length derived from ArrayBuffer (no holes)
6. Support most Array methods (.map, .filter, etc.)
7. Type coercion on assignment (e.g., 257 in Uint8Array becomes 1)

# Construction / Recognition

```js
const ta1 = new Uint8Array([0, 1, 2]);
const ta2 = Uint8Array.of(0, 1, 2);
const ta3 = Uint8Array.from([0, 1, 2]);
const ta4 = new Uint8Array(3); // length, filled with 0
```

# Context & Application

Use Typed Arrays when working with binary data: image manipulation, network protocols, WebGL/WebGPU, WebAssembly memory, or when all elements are known to be the same numeric type.

# Examples

```js
const ta = new Uint8Array(1);
ta[0] = 257;
assert.equal(ta[0], 1); // overflow: 257 % 256

ta[0] = '2';
assert.equal(ta[0], 2); // string coerced to number

const int16 = new Int16Array(2);
assert.deepEqual(int16.buffer, new ArrayBuffer(4)); // 4 bytes
```

(Chapter 35, Section 35.1-35.2, lines 94-385)

# Relationships

## Builds Upon
- **array-creation** -- Typed Arrays resemble regular Arrays

## Enables
- Binary data processing
- Interop with native APIs

## Related
- **array-buffer** -- the underlying data storage
- **data-view** -- alternative binary data access

## Contrasts With
- **array-creation** -- regular arrays have dynamic types and can have holes

# Common Errors

- **Error**: Expecting Typed Arrays to behave identically to regular Arrays.
  **Correction**: Typed Arrays have no `.concat()`, no holes, fixed length, type coercion on assignment, and elements are always numbers or bigints.

# Common Confusions

- **Confusion**: Typed Arrays can hold any JavaScript value.
  **Clarification**: Typed Arrays only hold numeric values of a fixed type. Non-numeric values are coerced.

# Source Reference

Chapter 35: Typed Arrays, Section 35.1-35.2, lines 94-385.

# Verification Notes

- Definition source: direct
- Confidence rationale: Extensively defined with class diagram
- Cross-reference status: verified
