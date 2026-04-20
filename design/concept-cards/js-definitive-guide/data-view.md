---
concept: DataView
slug: data-view
category: standard-library
subcategory: binary-data
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 297
section: "11.2.5 DataView and Endianness"
extraction_confidence: high
aliases: []
prerequisites:
  - array-buffer
extends: []
related:
  - typed-arrays
contrasts_with:
  - typed-arrays
answers_questions: []
---

# Quick Definition

A class that provides flexible, endianness-aware read/write access to an ArrayBuffer's raw binary data, with explicit control over byte ordering for each operation.

# Core Definition

"The DataView class defines methods for reading and writing values from an ArrayBuffer with explicitly specified byte ordering" (p. 297). Unlike typed arrays which use the platform's native endianness, DataView allows explicit big-endian or little-endian specification per operation, making it essential for working with network protocols and binary file formats.

# Prerequisites

- **array-buffer** — DataView operates on ArrayBuffer objects

# Key Properties

1. Provides explicit endianness control per read/write operation
2. 10 getter methods (e.g., `getInt16()`, `getFloat64()`) and 10 setter methods
3. Second argument to getters/setters: `false` (default) for big-endian, `true` for little-endian
4. Works at arbitrary byte offsets within the buffer

# Construction / Recognition

```js
let view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
let int = view.getInt32(0);           // Big-endian signed int from byte 0
int = view.getUint32(8, true);        // Little-endian unsigned int from byte 8
view.setUint32(8, int, false);        // Write back in big-endian
```

# Context & Application

Essential for parsing binary file formats (ZIP, JPEG) and network protocols that use big-endian byte ordering, since most modern CPUs are little-endian.

# Examples

From the source text (p. 297-298): Reading with explicit endianness: `view.getInt32(0)` reads big-endian, `view.getInt32(4, false)` also big-endian, `view.getUint32(8, true)` reads little-endian.

# Relationships

## Builds Upon
- **ArrayBuffer** — DataView reads/writes data in an ArrayBuffer

## Related
- **Typed Arrays** — Alternative view type; uses native endianness

## Contrasts With
- **Typed Arrays** — Typed arrays use platform-native endianness; DataView allows explicit endianness control

# Common Errors

- **Error**: Omitting the endianness argument and assuming little-endian.
  **Correction**: DataView defaults to big-endian when the boolean argument is omitted or `false`.

# Common Confusions

- **Confusion**: Thinking DataView and typed arrays always interpret data the same way.
  **Clarification**: Typed arrays use platform-native endianness (usually little-endian on modern CPUs); DataView defaults to big-endian.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.2.5, pages 297-298.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
