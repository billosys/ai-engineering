---
concept: Async Iteration over Node.js Streams
slug: async-iteration-node-streams
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Asynchronous iteration"
chapter_number: 45
pdf_page: null
section: "45.3 Async iteration over Node.js streams"
extraction_confidence: high
aliases:
  - stream async iteration
  - pull vs push streams
prerequisites:
  - async-iteration-protocol
  - for-await-of
  - async-generator
extends: []
related:
  - callback-pattern
contrasts_with: []
answers_questions:
  - "How do synchronous and asynchronous iteration protocols differ?"
---

# Quick Definition

Node.js readable streams support asynchronous iteration (since Node.js 10), allowing a shift from callback-based push model (stream pushes data to reader) to async-iteration pull model (reader pulls data from stream) using `for-await-of`.

# Core Definition

"Exploring JavaScript" Ch. 45 contrasts two approaches: callbacks (push -- "the stream is in control and pushes data to the reader") and async iteration (pull -- "the reader is in control and pulls data from the stream"). Async generators are "an elegant tool for transforming data streams."

# Prerequisites

- **Async iteration protocol** -- streams implement it
- **for-await-of** -- primary consumption mechanism
- **Async generator** -- used for stream transformation

# Key Properties

1. Available since Node.js 10
2. Push model (callbacks): stream controls data flow
3. Pull model (async iteration): reader controls data flow
4. Async generators compose stream transformations (e.g., chunks to lines)

# Construction / Recognition

Push (callbacks):
```js
readStream.on('data', (chunk) => { console.log('>>> ' + chunk); });
readStream.on('end', () => { console.log('### DONE ###'); });
```

Pull (async iteration):
```js
for await (const chunk of readStream) {
  console.log('>>> ' + chunk);
}
console.log('### DONE ###');
```

(Ch. 45, Section 45.3.1-45.3.2, lines 524-554)

# Context & Application

Async iteration provides cleaner, more composable stream processing in Node.js. Async generators can be chained as stream transformers.

# Examples

Chunks to lines transformer:
```js
async function* chunksToLines(chunkIterable) {
  let previous = '';
  for await (const chunk of chunkIterable) {
    previous += chunk;
    while (true) {
      const eolIndex = previous.indexOf('\n');
      if (eolIndex < 0) break;
      yield previous.slice(0, eolIndex + 1);
      previous = previous.slice(eolIndex + 1);
    }
  }
  if (previous.length > 0) yield previous;
}
```

(Ch. 45, Section 45.3.3, lines 573-592)

# Relationships

## Builds Upon
- **Async iteration protocol** -- streams are async iterables
- **Async generator** -- used for stream transformation

## Related
- **Callback pattern** -- the older push-based approach

# Common Errors

- **Error**: Not handling the final incomplete line in stream transformation
  **Correction**: After the loop, yield any remaining content (as shown in chunksToLines)

# Common Confusions

- **Confusion**: Async iteration replaces callbacks for all stream use cases
  **Clarification**: Async iteration is for reading; writing and other stream operations still use other APIs

# Source Reference

Chapter 45: Asynchronous iteration, Section 45.3, lines 511-637.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with push vs pull comparison
- Cross-reference status: verified
