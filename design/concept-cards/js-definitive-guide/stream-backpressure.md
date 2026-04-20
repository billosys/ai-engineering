---
concept: Stream Backpressure
slug: stream-backpressure
category: node-apis
subcategory: streams
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 613
section: "16.5.3 Writing to Streams and Handling Backpressure"
extraction_confidence: high
aliases:
  - back pressure
  - flow control
prerequisites:
  - writable-streams
  - readable-streams
extends: []
related:
  - stream-pipe
contrasts_with: []
answers_questions:
  - "What is a Node.js stream?"
---

# Quick Definition

Backpressure is a flow-control mechanism where a Writable stream's `write()` returns `false` to signal its buffer is full, telling the producer to pause until a "drain" event indicates capacity is available again.

# Core Definition

When `write()` returns `false`, the stream buffer is full -- this is backpressure. The proper response is to stop calling `write()` until the stream emits a "drain" event. In flowing mode on the read side, call `pause()` on the Readable, then `resume()` on "drain". Failing to respond to backpressure causes unbounded memory growth and can be a security vulnerability (denial-of-service via memory exhaustion). The `pipe()` method handles backpressure automatically (Flanagan, Ch. 16, pp. 613-616).

# Prerequisites

- **writable-streams** — Backpressure originates from writable streams.
- **readable-streams** — The readable side must respond to backpressure.

# Key Properties

1. `write()` returns `false` when the internal buffer is full.
2. "drain" event signals buffer has room again.
3. Ignoring backpressure can cause memory exhaustion.
4. `pipe()` handles backpressure automatically.
5. Security risk: an attacker can exploit unhandled backpressure to crash a server.

# Construction / Recognition

```javascript
function write(stream, chunk, callback) {
  let hasMoreRoom = stream.write(chunk);
  if (hasMoreRoom) {
    setImmediate(callback);
  } else {
    stream.once("drain", callback);
  }
}
```

# Context & Application

Critical for any high-throughput Node application, especially servers that stream data to clients. A server that ignores backpressure is vulnerable to denial-of-service attacks.

# Examples

From the source (p. 615-616): A streaming `copyFile()` implementation that pauses the input stream when `output.write()` returns `false` and resumes it on the "drain" event.

# Relationships

## Builds Upon
- **writable-streams** — `write()` return value signals backpressure
- **readable-streams** — `pause()`/`resume()` respond to backpressure

## Enables
- Reliable, memory-efficient streaming

## Related
- **stream-pipe** — Handles backpressure automatically

## Contrasts With
- (None)

# Common Errors

- **Error**: Ignoring the return value of `write()` and continuing to write.
  **Correction**: Check the return value; if `false`, wait for "drain" before writing more.

# Common Confusions

- **Confusion**: Backpressure means data was lost.
  **Clarification**: Data is still buffered internally. Backpressure is an advisory signal to slow down.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.5.3, pages 613-616.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Security implications explicitly noted
- Uncertainties: None
- Cross-reference status: Verified
