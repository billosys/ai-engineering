---
concept: Node Streams
slug: node-streams
category: node-apis
subcategory: streams
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 608
section: "16.5 Streams"
extraction_confidence: high
aliases:
  - Node.js streams
  - streaming I/O
prerequisites:
  - node-eventemitter
  - node-buffer
extends: []
related:
  - readable-streams
  - writable-streams
  - duplex-transform-streams
  - stream-pipe
  - stream-backpressure
contrasts_with: []
answers_questions:
  - "What is a Node.js stream?"
---

# Quick Definition

Node streams are abstractions for processing data incrementally in chunks rather than loading entire datasets into memory, with four types: Readable, Writable, Duplex, and Transform.

# Core Definition

Streams are Node's solution for processing data that is too large to fit in memory or that arrives incrementally. Node supports four basic stream types: Readable (data sources like `fs.createReadStream()`), Writable (data sinks like `fs.createWriteStream()`), Duplex (both readable and writable, like network sockets), and Transform (readable and writable where written data becomes readable in transformed form, like compression streams). Streams use internal buffers to handle the mismatch between read and write speeds (Flanagan, Ch. 16, pp. 608-610).

# Prerequisites

- **node-eventemitter** — Streams are EventEmitters.
- **node-buffer** — Streams read and write Buffers by default.

# Key Properties

1. Four types: Readable, Writable, Duplex, Transform.
2. Default to reading/writing Buffers; call `setEncoding()` for strings.
3. Streams use internal buffers to handle speed mismatches.
4. Event-based API: "data", "end", "error", "drain", "readable" events.
5. In Node 12+, Readable streams are async iterators (usable with `for await`).

# Construction / Recognition

```javascript
const fs = require("fs");
let readable = fs.createReadStream("input.txt");
let writable = fs.createWriteStream("output.txt");
readable.pipe(writable);
```

# Context & Application

Essential for file processing, network I/O, and any scenario where data should be processed incrementally rather than loaded entirely into memory.

# Examples

From the source (p. 608): A non-streaming `copyFile()` that reads the entire file into memory is contrasted with a streaming version using `pipe()` that processes data in chunks.

# Relationships

## Builds Upon
- **node-eventemitter** — Streams are EventEmitters
- **node-buffer** — Default data type for streams

## Enables
- **readable-streams** — Specific Readable API
- **writable-streams** — Specific Writable API
- **stream-pipe** — Connecting streams
- **stream-backpressure** — Flow control

## Related
- **duplex-transform-streams** — Combined stream types

## Contrasts With
- (None)

# Common Errors

- **Error**: Reading an entire large file into memory instead of streaming it.
  **Correction**: Use `fs.createReadStream()` and process data in chunks.

# Common Confusions

- **Confusion**: Streams and Promises are competing patterns.
  **Clarification**: Streams handle incremental data flow; Promises handle single async results. They complement each other (async iteration bridges both).

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.5, pages 608-610.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Foundational section with clear taxonomy
- Uncertainties: None
- Cross-reference status: Verified
