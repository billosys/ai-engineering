---
concept: Writable Streams
slug: writable-streams
category: node-apis
subcategory: streams
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 612
section: "16.5.3 Writing to Streams and Handling Backpressure"
extraction_confidence: high
aliases:
  - Writable stream
prerequisites:
  - node-streams
extends:
  - node-streams
related:
  - readable-streams
  - stream-backpressure
contrasts_with: []
answers_questions:
  - "What is a Node.js stream?"
---

# Quick Definition

Writable streams are data destinations with a `write()` method that accepts strings or Buffers, returning `false` when the internal buffer is full (signaling backpressure), and an `end()` method to signal completion.

# Core Definition

Data is written to a Writable stream via `write(chunk)`, which returns `true` if the buffer has room or `false` if full (backpressure signal). When `write()` returns `false`, stop writing and wait for the "drain" event. The `end()` method signals that no more data will be written. The "finish" event fires when all data has been flushed. An optional callback as the third argument to `write()` is invoked when the data has been flushed (Flanagan, Ch. 16, pp. 612-616).

# Prerequisites

- **node-streams** — Must understand the stream concept.

# Key Properties

1. `write(chunk)` returns boolean indicating buffer capacity.
2. Return value of `false` signals backpressure.
3. "drain" event fires when the buffer has room again.
4. `end()` signals the end of writes; triggers "finish" event.
5. Default encoding is "utf8"; can be changed with `setDefaultEncoding()`.

# Construction / Recognition

```javascript
let output = fs.createWriteStream("numbers.txt");
for(let i = 0; i < 100; i++) { output.write(`${i}\n`); }
output.end();
```

# Context & Application

Used whenever you need to write data incrementally to a file, network socket, or other destination. Understanding backpressure is critical for server reliability.

# Examples

From the source (p. 612): Writing numbers to a file stream, each followed by a newline, then calling `end()`.

# Relationships

## Builds Upon
- **node-streams** — Writable is one of the four stream types

## Enables
- **stream-backpressure** — Write's return value signals backpressure

## Related
- **readable-streams** — Source of data for writable streams

## Contrasts With
- (None)

# Common Errors

- **Error**: Ignoring the return value of `write()` in high-throughput scenarios.
  **Correction**: Check the return value; if `false`, pause writing until the "drain" event.

# Common Confusions

- **Confusion**: `write()` returning `false` means the write failed.
  **Clarification**: The data is still buffered and will be written. `false` is an advisory signal to pause writing.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.5.3, pages 612-616.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Detailed explanation of write() semantics
- Uncertainties: None
- Cross-reference status: Verified
