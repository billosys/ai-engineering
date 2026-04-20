---
concept: Typed Arrays
slug: typed-arrays
category: standard-library
subcategory: binary-data
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 292
section: "11.2 Typed Arrays and Binary Data"
extraction_confidence: high
aliases:
  - TypedArray
prerequisites: []
extends: []
related:
  - array-buffer
  - data-view
contrasts_with: []
answers_questions: []
---

# Quick Definition

Fixed-length, numerically-typed array objects (like `Uint8Array`, `Float64Array`) that provide efficient access to binary data, with elements restricted to a specific numeric type and size.

# Core Definition

Typed arrays are "much closer to the low-level arrays" of languages like C and Java (p. 292). There are 11 typed array types (e.g., `Int8Array`, `Uint8Array`, `Float64Array`, `BigInt64Array`). Elements have a fixed numeric type and size, the array length cannot change, and elements are initialized to 0.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Fixed length — cannot grow or shrink after creation
2. All elements are numbers of a specific type (8-64 bits, signed/unsigned/float)
3. Elements initialized to 0 on creation
4. Implement most Array methods except those that change length (`push`, `pop`, `splice`)
5. Not technically Arrays — `Array.isArray()` returns `false`
6. Backed by an `ArrayBuffer`

# Construction / Recognition

```js
let bytes = new Uint8Array(1024);
let matrix = new Float64Array(9);
let white = Uint8ClampedArray.of(255, 255, 255, 0);
let ints = Uint32Array.from(white);
```

# Context & Application

Used for binary data processing, WebGL, audio/video processing, network protocols, and any scenario requiring low-level numeric data manipulation. Significantly faster and more memory-efficient than regular arrays for numeric data.

# Examples

From the source text (p. 295-296): A sieve of Eratosthenes using `Uint8Array` runs "more than four times faster and use eight times less memory" than with a regular Array. Also: `let ints = new Int16Array(10); ints.fill(3).map(x=>x*x).join("")` produces `"9999999999"`.

# Relationships

## Related
- **ArrayBuffer** — The underlying binary data storage for typed arrays
- **DataView** — An alternative way to read/write ArrayBuffer data with explicit endianness

# Common Errors

- **Error**: Expecting typed arrays to auto-resize like regular arrays with `push()`.
  **Correction**: Typed arrays have fixed length. Methods like `push()`, `pop()`, and `splice()` are not implemented.

# Common Confusions

- **Confusion**: Thinking values outside the type's range will cause errors.
  **Clarification**: Values are silently truncated or wrapped. `Uint8Array.of(1.23, 2.99, 45000)` produces `[1, 2, 200]`. `Uint8ClampedArray` clamps to 0-255 instead of wrapping.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.2, pages 292-298.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High — extensive coverage
- Uncertainties: None
- Cross-reference status: Verified
