---
concept: Async Iteration over Streams
slug: async-iteration-streams
category: node-apis
subcategory: streams
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 612
section: "16.5.2 Asynchronous Iteration"
extraction_confidence: high
aliases:
  - for/await streams
  - stream async iterator
prerequisites:
  - readable-streams
extends: []
related:
  - stream-pipe
contrasts_with: []
answers_questions:
  - "What is a Node.js stream?"
---

# Quick Definition

In Node 12+, Readable streams are asynchronous iterators, allowing `for await (let chunk of stream)` loops to read data with clean, structured code that resembles synchronous processing.

# Core Definition

Readable streams implement the async iterator protocol in Node 12 and later, enabling `for/await` loops to read chunks from a stream. This approach is almost as easy as `pipe()` but allows per-chunk processing. When combined with `setEncoding()`, the chunks are strings rather than Buffers (Flanagan, Ch. 16, pp. 612-613).

# Prerequisites

- **readable-streams** — Async iteration applies to Readable streams.

# Key Properties

1. Available in Node 12+.
2. Use `for await (let chunk of stream)` to read chunks.
3. Combine with `setEncoding()` to get string chunks.
4. Structured like synchronous code within an `async` function.

# Construction / Recognition

```javascript
async function grep(source, destination, pattern) {
  source.setEncoding("utf8");
  for await (let chunk of source) {
    // process chunk
  }
}
```

# Context & Application

The preferred modern approach for processing stream data when you need per-chunk logic beyond what `pipe()` provides.

# Examples

From the source (p. 612): An async `grep()` function that reads lines from a source stream, checks them against a pattern, and writes matching lines to a destination.

# Relationships

## Builds Upon
- **readable-streams** — Readable streams are the async iterable

## Enables
- Clean, structured stream processing code

## Related
- **stream-pipe** — Alternative when no per-chunk processing is needed

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `for await` outside of an `async` function.
  **Correction**: `for await` is only valid inside `async` functions.

# Common Confusions

- **Confusion**: Async iteration handles backpressure automatically.
  **Clarification**: When reading, backpressure is handled. But when writing to a destination within the loop, you must handle write backpressure yourself.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.5.2, pages 612-613.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear example with grep implementation
- Uncertainties: None
- Cross-reference status: Verified
