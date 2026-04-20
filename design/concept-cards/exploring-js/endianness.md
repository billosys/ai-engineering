---
concept: Endianness
slug: endianness
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Typed Arrays: handling binary data (advanced)"
chapter_number: 35
pdf_page: null
section: "35.4.2 Endianness"
extraction_confidence: high
aliases:
  - "byte order"
  - "big-endian"
  - "little-endian"
prerequisites:
  - typed-arrays
  - array-buffer
extends: []
related:
  - data-view
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Endianness is the byte order in which multi-byte values are stored in memory: big-endian stores the most significant byte first, while little-endian stores the least significant byte first; Typed Arrays use the platform's native endianness while DataViews allow explicit endianness control.

# Core Definition

Endianness determines the order in which bytes of multi-byte values are stored. Big-endian stores the most significant byte at the lowest address; little-endian stores the least significant byte first. Typed Arrays use the platform's native byte order. DataViews let you specify endianness explicitly, making them essential for cross-platform binary format handling.

# Prerequisites

- **typed-arrays** -- context for byte ordering
- **array-buffer** -- where bytes are stored

# Key Properties

1. Big-endian: most significant byte first (network byte order)
2. Little-endian: least significant byte first (x86/ARM)
3. Typed Arrays: platform-native endianness
4. DataViews: configurable endianness per operation

# Construction / Recognition

```js
// DataView with explicit endianness
const dv = new DataView(new ArrayBuffer(2));
dv.setInt16(0, 256, false); // big-endian
dv.setInt16(0, 256, true);  // little-endian
```

# Context & Application

Endianness matters when reading/writing binary network protocols, file formats, or sharing data between different architectures.

# Examples

```js
// Check platform endianness
const buf = new ArrayBuffer(2);
new Uint16Array(buf)[0] = 0x0102;
const bytes = new Uint8Array(buf);
// Big-endian: [1, 2]; Little-endian: [2, 1]
```

(Chapter 35, Section 35.4.2)

# Relationships

## Builds Upon
- **typed-arrays** -- byte-level interpretation
- **array-buffer** -- raw storage

## Enables
- Cross-platform binary data handling

## Related
- **data-view** -- provides endianness control

## Contrasts With
- None

# Common Errors

- **Error**: Assuming all platforms use the same endianness.
  **Correction**: Use DataView for portable binary format handling.

# Common Confusions

- **Confusion**: Endianness affects single-byte values.
  **Clarification**: Endianness only matters for multi-byte values (Int16, Int32, Float64, etc.).

# Source Reference

Chapter 35: Typed Arrays, Section 35.4.2.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
