---
concept: Resizable and Transferable ArrayBuffers
slug: resizable-array-buffers
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Typed Arrays: handling binary data (advanced)"
chapter_number: 35
pdf_page: null
section: "35.6 Resizing ArrayBuffers"
extraction_confidence: high
aliases:
  - "resizable ArrayBuffer"
  - "transferable ArrayBuffer"
  - "detaching"
prerequisites:
  - array-buffer
  - typed-arrays
extends:
  - array-buffer
related: []
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

ES2024 added resizable ArrayBuffers (grow/shrink) and the ability to transfer ArrayBuffer data between contexts (detaching the source), enabling zero-copy data passing and dynamic buffer management.

# Core Definition

ES2024 introduced two important ArrayBuffer features: (1) Resizable ArrayBuffers, created with a `maxByteLength` option, can be resized via `.resize()`. SharedArrayBuffers can only grow, not shrink. (2) Transferring moves ArrayBuffer data to a new buffer, detaching the original (making it zero-length and unusable). Transfer methods include `.transfer()`, `.transferToFixedLength()`, and `structuredClone()` with transfer option.

# Prerequisites

- **array-buffer** -- the base concept being extended
- **typed-arrays** -- views affected by resizing/detaching

# Key Properties

1. Introduced in ES2024
2. `new ArrayBuffer(length, {maxByteLength})` -- resizable
3. `.resize(newLength)` -- change buffer size
4. `.transfer()` -- move data to new buffer, detach original
5. Detached buffers have `.byteLength` of 0
6. SharedArrayBuffers can only grow (not shrink)

# Construction / Recognition

```js
const buf = new ArrayBuffer(4, {maxByteLength: 8});
buf.resize(8); // grow
buf.resize(2); // shrink

const newBuf = buf.transfer(); // buf is now detached
```

# Context & Application

Resizable buffers are useful for dynamic data accumulation. Transfer is useful for zero-copy data passing to Web Workers and for security (ensuring a buffer can't be accessed after handoff).

# Examples

```js
const buf = new ArrayBuffer(4, {maxByteLength: 16});
assert.equal(buf.byteLength, 4);
assert.equal(buf.resizable, true);
buf.resize(8);
assert.equal(buf.byteLength, 8);
```

(Chapter 35, Sections 35.6-35.7)

# Relationships

## Builds Upon
- **array-buffer** -- extends ArrayBuffer capabilities

## Enables
- Dynamic buffer management
- Zero-copy data passing

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Accessing a detached ArrayBuffer.
  **Correction**: After `.transfer()`, the source buffer is detached and has byteLength 0. All access throws.

# Common Confusions

- **Confusion**: Resizable ArrayBuffers can grow without limit.
  **Clarification**: They can only grow up to `maxByteLength` specified at creation.

# Source Reference

Chapter 35: Typed Arrays, Sections 35.6-35.7.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2024 markers
- Cross-reference status: verified
