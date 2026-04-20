---
concept: Buffer Type
slug: node-buffer
category: node-apis
subcategory: fundamentals
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 603
section: "16.3 Buffers"
extraction_confidence: high
aliases:
  - Buffer class
  - Node Buffer
prerequisites:
  - node-programming-model
extends: []
related:
  - node-streams
contrasts_with: []
answers_questions:
  - "What is a Node.js stream?"
---

# Quick Definition

Node's Buffer class (a subclass of Uint8Array) represents fixed-length sequences of bytes, designed to interoperate with JavaScript strings through various character encodings like "utf8", "ascii", "hex", and "base64".

# Core Definition

A Buffer is a sequence of bytes, designed for working with binary data from files and the network. Buffer is a subclass of Uint8Array that adds methods for encoding strings to bytes and decoding bytes to strings. Supported encodings include "utf8" (default), "utf16le", "latin1", "ascii", "hex", and "base64". Buffers are created with `Buffer.from()` for existing data or `Buffer.alloc()` for new empty buffers (Flanagan, Ch. 16, pp. 603-605).

# Prerequisites

- **node-programming-model** — Buffer is a Node-specific type.

# Key Properties

1. Subclass of Uint8Array; all typed array methods available.
2. `Buffer.from(string, encoding)` creates a buffer from a string.
3. `buffer.toString(encoding)` converts bytes back to a string.
4. `Buffer.alloc(size)` creates a zero-filled buffer.
5. Buffers are mutable: individual bytes can be read and written.

# Construction / Recognition

```javascript
let b = Buffer.from([0x41, 0x42, 0x43]);
b.toString()       // => "ABC"
b.toString("hex")  // => "414243"
let zeros = Buffer.alloc(1024);
```

# Context & Application

Buffers are encountered whenever reading binary data from files or networks. If you specify an encoding when reading, you get strings instead of Buffers.

# Examples

From the source (p. 604):
```javascript
let computer = Buffer.from("IBM3111", "ascii");
for(let i = 0; i < computer.length; i++) { computer[i]--; }
computer.toString("ascii") // => "HAL2000"
```

# Relationships

## Builds Upon
- **node-programming-model** — Part of Node's core API

## Enables
- **node-streams** — Streams read and write Buffers

## Related
- (Typed arrays in core JavaScript)

## Contrasts With
- (None)

# Common Errors

- **Error**: Expecting `Buffer.from()` to return a copy when passed another Buffer.
  **Correction**: `Buffer.from(buffer)` does create a copy, but `buffer.slice()` returns a view that shares memory.

# Common Confusions

- **Confusion**: Buffers are strings.
  **Clarification**: Buffers are byte sequences. They must be explicitly decoded (with an encoding) to produce strings.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.3, pages 603-605.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear examples with multiple encodings
- Uncertainties: None
- Cross-reference status: Verified
