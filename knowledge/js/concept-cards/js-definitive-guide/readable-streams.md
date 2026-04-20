---
concept: Readable Streams
slug: readable-streams
category: node-apis
subcategory: streams
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 615
section: "16.5.4 Reading Streams with Events"
extraction_confidence: high
aliases:
  - Readable stream
  - flowing mode
  - paused mode
prerequisites:
  - node-streams
extends:
  - node-streams
related:
  - writable-streams
  - stream-pipe
  - async-iteration-streams
contrasts_with: []
answers_questions:
  - "What is a Node.js stream?"
---

# Quick Definition

Readable streams are data sources with two modes: flowing mode (data pushed via "data" events) and paused mode (data pulled via `read()` calls after "readable" events), both emitting "end" when complete and "error" on failure.

# Core Definition

Readable streams have two modes. In flowing mode, data arrives as "data" events (registering a "data" handler activates this mode); the stream pushes chunks automatically. In paused mode, the stream emits "readable" events and you pull data by calling `read()` repeatedly until it returns null. Both modes emit "end" when the stream is exhausted and "error" on failure. In Node 12+, Readable streams are also async iterators, enabling `for await` loops (Flanagan, Ch. 16, pp. 615-617).

# Prerequisites

- **node-streams** — Must understand the stream concept.

# Key Properties

1. Flowing mode: register "data" handler, chunks are pushed automatically.
2. Paused mode: wait for "readable" event, call `read()` repeatedly until null.
3. "end" event signals no more data.
4. `setEncoding()` makes the stream return strings instead of Buffers.
5. `pause()` and `resume()` control flow in flowing mode.

# Construction / Recognition

```javascript
// Flowing mode
let input = fs.createReadStream(filename);
input.on("data", (chunk) => { /* process chunk */ });
input.on("end", () => { /* done */ });

// Paused mode
input.on("readable", () => {
  let chunk;
  while(chunk = input.read()) { /* process */ }
});
```

# Context & Application

Choose flowing mode for simple piping/processing. Choose paused mode when you need fine-grained control over when data is consumed. Prefer async iteration (for/await) when possible.

# Examples

From the source (p. 615-617): A SHA256 hash computation using paused mode, reading chunks until `read()` returns null, then computing the hash on "end".

# Relationships

## Builds Upon
- **node-streams** — Readable is one of the four stream types

## Enables
- **stream-pipe** — Readable streams are piped to writable streams
- **async-iteration-streams** — Readable streams are async iterators

## Related
- **writable-streams** — The other end of a data pipeline

## Contrasts With
- (None)

# Common Errors

- **Error**: Not draining the buffer completely in paused mode.
  **Correction**: Call `read()` in a loop until it returns null to ensure future "readable" events fire.

# Common Confusions

- **Confusion**: Flowing and paused modes can be used simultaneously.
  **Clarification**: A stream is in one mode at a time. Do not mix the two event-based APIs.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.5.4, pages 615-617.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Both modes clearly explained with examples
- Uncertainties: None
- Cross-reference status: Verified
