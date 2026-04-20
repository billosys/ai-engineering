---
concept: Stream
slug: stream
category: server-side
subcategory: node-core
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Node.js"
chapter_number: 20
pdf_page: null
section: "Streams"
extraction_confidence: high
aliases:
  - readable stream
  - writable stream
  - Node stream
prerequisites:
  - nodejs
  - event-handler
extends: []
related:
  - request-handling
  - response-writing
  - file-system-module
contrasts_with: []
answers_questions:
  - "What are streams in Node.js?"
  - "How do I process data piece by piece in Node?"
---

# Quick Definition
Streams are objects that process data piece-by-piece rather than all at once: writable streams accept data via `write()` and `end()`, while readable streams emit data via "data" and "end" events, connected by `pipe()`.

# Core Definition
The response object "is an example of a writable stream object, which is a widely used concept in Node. Such objects have a `write` method that can be passed a string or a `Buffer` object" (Ch. 20, "Streams"). "Readable streams [...] have `'data'` and `'end'` events. The first is fired every time data comes in, and the second is called whenever the stream is at its end."

# Prerequisites
- **Node.js**: Streams are a Node concept
- **Event handlers**: Readable streams use events

# Key Properties
1. Writable: `write(data)`, `end()`, pipe target
2. Readable: "data" event (chunks), "end" event (finished)
3. `pipe(writable)` connects readable to writable
4. `createReadStream` / `createWriteStream` for file streams
5. HTTP request = readable; HTTP response = writable

# Construction / Recognition
```javascript
// Reading stream
request.on("data", chunk =>
  response.write(chunk.toString().toUpperCase()));
request.on("end", () => response.end());

// Piping
from.pipe(to);
```

# Context & Application
Streams enable processing large files/data without loading everything into memory. Essential for file servers, video streaming, and data processing pipelines.

# Examples
File server using streams:
```javascript
return {body: createReadStream(path), type: lookup(path)};
// Later: body.pipe(response)
```

# Relationships
## Builds Upon
- nodejs, event-handler
## Enables
- Efficient file serving, data processing, piping
## Related
- request-handling, response-writing, file-system-module
## Contrasts With
- Loading entire file into memory (readFile)

# Common Errors
- **Error**: Not handling stream errors
  **Correction**: Always listen for "error" events on streams

# Common Confusions
- **Confusion**: All Node I/O is streaming
  **Clarification**: Functions like readFile load the entire file; only createReadStream/createWriteStream are streaming

# Source Reference
Chapter 20: Node.js, Section "Streams", lines 546-616 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Both types explained with pipe
- Cross-reference status: verified
