---
concept: Typed Array Element Types
slug: typed-array-element-types
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Typed Arrays: handling binary data (advanced)"
chapter_number: 35
pdf_page: null
section: "35.4 Element types"
extraction_confidence: high
aliases:
  - "Uint8"
  - "Int16"
  - "Float32"
  - "Float64"
prerequisites:
  - typed-arrays
extends: []
related:
  - endianness
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Typed Array element types span integers (Int8, Uint8, Uint8Clamped, Int16, Uint16, Int32, Uint32, BigInt64, BigUint64) and floats (Float16, Float32, Float64), each with fixed byte sizes and overflow/underflow behavior.

# Core Definition

Typed Arrays support 12 element types: signed and unsigned integers of 8, 16, 32, and 64 bits; clamped unsigned 8-bit; and floating point of 16, 32, and 64 bits. Integer types handle overflow via modular arithmetic (wrapping). Uint8ClampedArray clamps values to 0-255 instead of wrapping. BigInt64Array and BigUint64Array use bigint values.

# Prerequisites

- **typed-arrays** -- the array types that use these elements

# Key Properties

1. Int8Array: 1 byte, signed (-128 to 127)
2. Uint8Array: 1 byte, unsigned (0 to 255)
3. Uint8ClampedArray: 1 byte, clamped (0 to 255)
4. Int16Array / Uint16Array: 2 bytes
5. Int32Array / Uint32Array: 4 bytes
6. BigInt64Array / BigUint64Array: 8 bytes (bigint)
7. Float16Array / Float32Array / Float64Array: 2/4/8 bytes

# Construction / Recognition

```js
new Uint8Array([255, 256]); // [255, 0] -- overflow wraps
new Uint8ClampedArray([255, 256]); // [255, 255] -- clamped
new Float64Array([3.14]); // [3.14]
```

# Context & Application

Choose the element type based on the data requirements: Uint8 for bytes, Float64 for general numbers, Int32 for integer math, BigInt64 for large integers.

# Examples

```js
const u8 = new Uint8Array(1);
u8[0] = 257;  // 257 % 256 = 1
assert.equal(u8[0], 1);

const clamped = new Uint8ClampedArray(1);
clamped[0] = 257; // clamped to 255
assert.equal(clamped[0], 255);
```

(Chapter 35, Section 35.4, lines 399-600)

# Relationships

## Builds Upon
- **typed-arrays** -- element types define array behavior

## Enables
- Precise binary data manipulation

## Related
- **endianness** -- multi-byte types affected by byte order

## Contrasts With
- None

# Common Errors

- **Error**: Expecting Uint8Array to clamp values like Uint8ClampedArray.
  **Correction**: Uint8Array wraps (modular arithmetic); Uint8ClampedArray clamps.

# Common Confusions

- **Confusion**: BigInt64Array stores regular numbers.
  **Clarification**: BigInt64Array and BigUint64Array store bigint values, not numbers.

# Source Reference

Chapter 35: Typed Arrays, Section 35.4, lines 399-600.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with table
- Cross-reference status: verified
