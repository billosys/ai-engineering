---
concept: ArrayBuffer
slug: array-buffer
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Typed Arrays: handling binary data (advanced)"
chapter_number: 35
pdf_page: null
section: "35.1.2 The core classes: ArrayBuffer, Typed Arrays, DataView"
extraction_confidence: high
aliases:
  - "ArrayBuffer"
  - "SharedArrayBuffer"
prerequisites: []
extends: []
related:
  - typed-arrays
  - data-view
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

An ArrayBuffer is a fixed-length block of binary data (a byte sequence) that cannot be accessed directly -- it must be wrapped in a Typed Array or DataView to read/write its contents.

# Core Definition

The Typed Array API stores binary data in instances of ArrayBuffer. An ArrayBuffer itself is a black box: to access its data, it must be wrapped in a view object (Typed Array or DataView). ArrayBuffers are initialized with zeros. ES2024 added resizable ArrayBuffers and transfer/detach operations. SharedArrayBuffer (ES2017) allows concurrent access from multiple agents.

# Prerequisites

Foundational concept for binary data handling.

# Key Properties

1. Introduced in ES2015 (ES6)
2. Fixed-length byte sequence (resizable since ES2024)
3. Cannot be read/written directly -- requires a view
4. Initialized with zeros
5. Can be transferred between agents (ES2024)
6. SharedArrayBuffer enables concurrent access (ES2017)

# Construction / Recognition

```js
const buf = new ArrayBuffer(4); // 4 bytes, all zeros
const view = new Uint8Array(buf); // access via Typed Array
```

# Context & Application

ArrayBuffers are the fundamental storage for all binary data in JavaScript. They are used with WebGL, WebGPU, WebAssembly, file APIs, and network protocols.

# Examples

```js
const buf = new ArrayBuffer(4);
const ta = new Int16Array(buf); // 2 elements of 2 bytes each
assert.equal(ta.length, 2);
ta[0] = 42;
```

(Chapter 35, Section 35.1.2, lines 144-198)

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **typed-arrays** -- views over ArrayBuffer
- **data-view** -- alternative view

## Related
- **typed-arrays** -- primary way to access ArrayBuffer data

## Contrasts With
- None

# Common Errors

- **Error**: Trying to read data directly from an ArrayBuffer.
  **Correction**: Wrap it in a Typed Array or DataView first.

# Common Confusions

- **Confusion**: ArrayBuffer and Array are related.
  **Clarification**: ArrayBuffer is raw binary storage with no Array methods. It is fundamentally different from Array.

# Source Reference

Chapter 35: Typed Arrays, Section 35.1.2, lines 144-198.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
