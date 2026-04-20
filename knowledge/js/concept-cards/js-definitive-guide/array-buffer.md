---
concept: ArrayBuffer
slug: array-buffer
category: standard-library
subcategory: binary-data
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 294
section: "11.2.2 Creating Typed Arrays"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related:
  - typed-arrays
  - data-view
contrasts_with: []
answers_questions: []
---

# Quick Definition

An opaque reference to a fixed-size chunk of raw binary memory that cannot be read or written directly, but can be accessed through typed array or DataView views.

# Core Definition

"An ArrayBuffer is an opaque reference to a chunk of memory. You can create one with the constructor; just pass in the number of bytes of memory you'd like to allocate" (p. 294). Multiple typed arrays can share the same ArrayBuffer, providing different views of the same underlying data.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Represents a fixed-size block of raw binary data
2. Cannot read or write bytes directly — requires a view (typed array or DataView)
3. Multiple views can share the same buffer
4. `byteLength` property gives the buffer size

# Construction / Recognition

```js
let buffer = new ArrayBuffer(1024*1024);  // One megabyte
let asbytes = new Uint8Array(buffer);      // View as bytes
let asints = new Int32Array(buffer);        // View as 32-bit ints
```

# Context & Application

Used when multiple typed arrays need to share the same underlying memory, or when working with binary protocols that require different interpretations of the same data.

# Examples

From the source text (p. 294-295): Creating multiple views of one buffer: `new Uint8Array(buffer)` views it as bytes, `new Int32Array(buffer)` views it as 32-bit integers. Views share memory: changes through one view are visible through others.

# Relationships

## Enables
- **Typed Arrays** — Typed arrays use ArrayBuffer as their underlying storage
- **DataView** — DataView provides flexible access to ArrayBuffer data

## Related
- **Typed Arrays** — Every typed array has an underlying ArrayBuffer
- **DataView** — An alternative view type for ArrayBuffer

# Common Errors

- **Error**: Trying to use `buffer[0]` to access bytes directly.
  **Correction**: ArrayBuffer does not support indexing. Use a typed array view or DataView to access the data.

# Common Confusions

- **Confusion**: Setting `buffer[0] = 255` and expecting it to modify the binary data.
  **Clarification**: This sets a regular JavaScript object property, not a byte in the buffer. Use a typed array view instead.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.2.2, pages 294-297.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High — well explained
- Uncertainties: None
- Cross-reference status: Verified
