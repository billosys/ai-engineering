---
concept: Duplex and Transform Streams
slug: duplex-transform-streams
category: node-apis
subcategory: streams
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 609
section: "16.5 Streams"
extraction_confidence: high
aliases:
  - Duplex stream
  - Transform stream
prerequisites:
  - readable-streams
  - writable-streams
extends:
  - node-streams
related:
  - stream-pipe
contrasts_with: []
answers_questions:
  - "What is a Node.js stream?"
---

# Quick Definition

Duplex streams combine a Readable and Writable stream into one object (e.g., network sockets), while Transform streams are a special Duplex where data written to the stream becomes readable in transformed form (e.g., compression, encryption).

# Core Definition

Duplex streams are both readable and writable. Network sockets returned by `net.connect()` are Duplex: writing sends data across the network, reading receives data from the other end. Transform streams are also readable and writable, but differ in that data written to a Transform stream becomes readable from the same stream in transformed form. `zlib.createGzip()` returns a Transform that compresses written data; `crypto.createCipheriv()` returns one that encrypts (Flanagan, Ch. 16, pp. 609-610).

# Prerequisites

- **readable-streams** — Transform/Duplex streams are readable.
- **writable-streams** — Transform/Duplex streams are writable.

# Key Properties

1. Duplex: independent read and write sides (like a network socket).
2. Transform: write side feeds into read side with a transformation.
3. Custom Transform streams implement the `_transform(chunk, encoding, callback)` method.
4. `_flush(callback)` is called before the stream closes, for final processing.
5. Transform streams are particularly useful in pipe chains.

# Construction / Recognition

```javascript
const zlib = require("zlib");
source.pipe(zlib.createGzip()).pipe(destination);
```

# Context & Application

Transform streams are the key to building processing pipelines. Custom Transform streams enable any data transformation (filtering, mapping, encoding) in a streaming fashion.

# Examples

From the source (p. 610-613): A `GrepStream` custom Transform that filters lines matching a regex, implementing `_transform()` and `_flush()` methods.

# Relationships

## Builds Upon
- **readable-streams** — Duplex/Transform are readable
- **writable-streams** — Duplex/Transform are writable

## Enables
- **stream-pipe** — Transform streams are the middle stages of pipe chains

## Related
- **node-streams** — Part of the stream taxonomy

## Contrasts With
- (None - this card contrasts Duplex with Transform)

# Common Errors

- **Error**: Not calling the callback in `_transform()`.
  **Correction**: Always call `callback(null, output)` (or `callback(error)`) to signal completion.

# Common Confusions

- **Confusion**: Duplex and Transform are the same thing.
  **Clarification**: In a Duplex stream, the read and write sides are independent. In a Transform stream, written data flows through a transformation and becomes readable output.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.5, pages 609-613.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear distinction with GrepStream example
- Uncertainties: None
- Cross-reference status: Verified
