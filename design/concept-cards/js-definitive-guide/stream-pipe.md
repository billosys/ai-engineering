---
concept: "Stream pipe()"
slug: stream-pipe
category: node-apis
subcategory: streams
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 610
section: "16.5.1 Pipes"
extraction_confidence: high
aliases:
  - pipe method
  - stream piping
prerequisites:
  - readable-streams
  - writable-streams
extends: []
related:
  - stream-backpressure
  - duplex-transform-streams
contrasts_with: []
answers_questions:
  - "What is a Node.js stream?"
---

# Quick Definition

The `pipe()` method of a Readable stream connects it to a Writable stream, automatically handling data transfer and backpressure, and can be chained through Transform streams to create processing pipelines.

# Core Definition

Instead of manually reading from a Readable and writing to a Writable, you can connect them with `readable.pipe(writable)`. Node handles backpressure automatically when using `pipe()`. Transform streams can be placed in the middle to create multi-stage pipelines (Flanagan, Ch. 16, pp. 610-612).

# Prerequisites

- **readable-streams** — The source of the pipe.
- **writable-streams** — The destination of the pipe.

# Key Properties

1. `readable.pipe(writable)` connects two streams.
2. Backpressure is handled automatically.
3. `pipe()` returns its argument, enabling chaining: `source.pipe(transform).pipe(destination)`.
4. Error handling still requires separate "error" event handlers on each stream.

# Construction / Recognition

```javascript
const fs = require("fs");
const zlib = require("zlib");
fs.createReadStream(filename)
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream(filename + ".gz"));
```

# Context & Application

The simplest and most reliable way to connect streams. Preferred over manual read/write loops because it handles backpressure correctly.

# Examples

From the source (p. 610): A file compression function that pipes a read stream through gzip to a write stream:
```javascript
source.on("error", callback)
  .pipe(gzipper)
  .pipe(destination)
  .on("error", callback)
  .on("finish", callback);
```

# Relationships

## Builds Upon
- **readable-streams** — Source of the pipe
- **writable-streams** — Destination of the pipe

## Enables
- Multi-stage stream processing pipelines

## Related
- **stream-backpressure** — pipe() handles this automatically
- **duplex-transform-streams** — Middle stages of pipe chains

## Contrasts With
- (None)

# Common Errors

- **Error**: Assuming `pipe()` handles errors automatically.
  **Correction**: Register "error" event handlers on each stream in the pipeline.

# Common Confusions

- **Confusion**: `pipe()` copies all data synchronously.
  **Clarification**: `pipe()` sets up an asynchronous data flow. Data is transferred in chunks as it becomes available.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.5.1, pages 610-612.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Multiple examples demonstrating chaining
- Uncertainties: None
- Cross-reference status: Verified
