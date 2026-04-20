---
# === CORE IDENTIFICATION ===
concept: BigInt Typed Arrays
slug: bigint-typed-arrays

# === CLASSIFICATION ===
category: primitive-types
subcategory: bigints
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Bigints -- arbitrary-precision integers (advanced)"
chapter_number: 20
pdf_page: null
section: "Typed Array and DataView operations for 64-bit values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "BigInt64Array"
  - "BigUint64Array"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bigint-type
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Bigints enable 64-bit integer Typed Arrays (`BigInt64Array` and `BigUint64Array`) and corresponding DataView methods for reading and writing 64-bit values.

# Core Definition

"Thanks to bigints, Typed Arrays and DataViews can support 64-bit values." Two new Typed Array constructors were added: `BigInt64Array` (signed 64-bit) and `BigUint64Array` (unsigned 64-bit). Four DataView methods were also added: `getBigInt64()`, `setBigInt64()`, `getBigUint64()`, `setBigUint64()` (Ch. 20, Section 20.7).

# Prerequisites

- **bigint-type** -- these arrays store bigint values

# Key Properties

1. `BigInt64Array`: signed 64-bit integer typed array
2. `BigUint64Array`: unsigned 64-bit integer typed array
3. DataView: `getBigInt64()`, `setBigInt64()`, `getBigUint64()`, `setBigUint64()`
4. Elements are bigint values, not numbers

# Construction / Recognition

```js
const arr = new BigInt64Array(2);
arr[0] = 123n;
arr[1] = 456n;
```

# Context & Application

Use BigInt typed arrays for efficient storage and manipulation of large arrays of 64-bit integers, such as in binary data processing, cryptography, and interoperability with C/C++ via WebAssembly.

# Examples

From the source text:

Typed Array constructors:
- `BigInt64Array`
- `BigUint64Array`

DataView methods:
- `DataView.prototype.getBigInt64()`
- `DataView.prototype.setBigInt64()`
- `DataView.prototype.getBigUint64()`
- `DataView.prototype.setBigUint64()`

# Relationships

## Builds Upon
- **bigint-type** — stores bigint values

## Enables
- Efficient 64-bit integer array operations

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Storing a regular number in a BigInt64Array
  **Correction**: BigInt typed arrays only accept bigint values. Use `123n`, not `123`.

# Common Confusions

- **Confusion**: Thinking Int32Array was the largest integer typed array
  **Clarification**: BigInt64Array and BigUint64Array support 64-bit integers using bigints.

# Source Reference

Chapter 20: Bigints, Section 20.7, lines 866-878.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit list of new constructors and methods
- Cross-reference status: verified
