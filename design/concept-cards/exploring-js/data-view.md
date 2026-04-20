---
concept: DataView
slug: data-view
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Typed Arrays: handling binary data (advanced)"
chapter_number: 35
pdf_page: null
section: "35.3 Using DataViews"
extraction_confidence: high
aliases:
  - "DataView"
prerequisites:
  - array-buffer
extends: []
related:
  - typed-arrays
contrasts_with:
  - typed-arrays
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

A DataView provides heterogeneous, byte-offset-based access to an ArrayBuffer, allowing reads and writes of different numeric types at arbitrary positions, unlike Typed Arrays which are homogeneous.

# Core Definition

DataViews let us interpret ArrayBuffer data as various types (Uint8, Int16, Float16, etc.) that we can read and write at any byte offset. They provide getter/setter methods like `.getInt16(offset)` and `.setUint8(offset, value)`. DataViews are useful when a binary format contains mixed types.

# Prerequisites

- **array-buffer** -- DataViews wrap ArrayBuffers

# Key Properties

1. Introduced in ES2015 (ES6)
2. Heterogeneous access -- different types at different offsets
3. Byte-offset-based access (not index-based)
4. Supports endianness control
5. No array-like indexing

# Construction / Recognition

```js
const dv = new DataView(new ArrayBuffer(4));
dv.setUint8(0, 5);
dv.getInt16(0); // reads 2 bytes as Int16
```

# Context & Application

Use DataViews when binary data contains mixed types (e.g., a file format header with different field sizes). Use Typed Arrays when all elements share one type.

# Examples

```js
const dataView = new DataView(new ArrayBuffer(4));
assert.equal(dataView.getInt16(0), 0);
assert.equal(dataView.getUint8(0), 0);
dataView.setUint8(0, 5);
```

(Chapter 35, Section 35.3, lines 387-397)

# Relationships

## Builds Upon
- **array-buffer** -- wraps an ArrayBuffer

## Enables
- Mixed-type binary data processing

## Related
- **typed-arrays** -- alternative view (homogeneous)

## Contrasts With
- **typed-arrays** -- Typed Arrays are indexed and homogeneous; DataViews are offset-based and heterogeneous

# Common Errors

- **Error**: Using a DataView when all data is the same type.
  **Correction**: For uniform data, a Typed Array is simpler and more performant.

# Common Confusions

- **Confusion**: DataViews and Typed Arrays are interchangeable.
  **Clarification**: Typed Arrays provide array-like indexed access for uniform types; DataViews provide offset-based access for mixed types.

# Source Reference

Chapter 35: Typed Arrays, Section 35.3, lines 387-397.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
