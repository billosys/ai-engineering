---
concept: Error-First Callbacks
slug: error-first-callbacks
category: node-apis
subcategory: fundamentals
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 601
section: "16.2 Node Is Asynchronous by Default"
extraction_confidence: high
aliases:
  - Node callbacks
  - callback convention
prerequisites:
  - node-programming-model
extends: []
related:
  - util-promisify
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
---

# Quick Definition

Node's error-first callback convention passes a callback function as the last argument, where the callback's first parameter is an error (null if no error occurred) and the second parameter is the result data.

# Core Definition

Node was created before JavaScript had Promises, so asynchronous Node APIs are callback-based. The last argument is a callback function. Node uses error-first callbacks: the first argument is normally null when no error occurred, and the second argument is the data or response. The error argument is first to make it impossible to omit checking for errors (Flanagan, Ch. 16, pp. 601-602).

# Prerequisites

- **node-programming-model** — Must understand Node's async model.

# Key Properties

1. Callback is always the last argument to the async function.
2. First callback parameter is the error (null on success).
3. Second callback parameter is the result data.
4. The error-first convention makes error checking unavoidable.
5. Can be converted to Promises with `util.promisify()`.

# Construction / Recognition

```javascript
const fs = require("fs");
fs.readFile(path, "utf8", (err, text) => {
  if (err) { console.error(err); return; }
  console.log(text);
});
```

# Context & Application

The original async pattern for all of Node's core APIs. Modern code increasingly uses the Promise-based alternatives (e.g., `fs.promises`), but understanding this pattern is essential for reading existing Node code.

# Examples

From the source (p. 601):
```javascript
fs.readFile(path, "utf8", (err, text) => {
  if (err) { console.error(err); callback(null); return; }
  let data = null;
  try { data = JSON.parse(text); } catch(e) { console.error(e); }
  callback(data);
});
```

# Relationships

## Builds Upon
- **node-programming-model** — The callback pattern is central to Node's async model

## Enables
- **util-promisify** — Converts error-first callbacks to Promises

## Related
- **node-eventemitter** — Event-based alternative for APIs needing multiple callbacks

## Contrasts With
- (None)

# Common Errors

- **Error**: Forgetting to check the error parameter.
  **Correction**: Always check if `err` is non-null before using the data parameter.

# Common Confusions

- **Confusion**: Error-first callbacks are obsolete.
  **Clarification**: While Promise-based alternatives exist (e.g., `fs.promises`), many Node APIs and third-party libraries still use this pattern.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.2, pages 601-602.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Foundational Node concept clearly explained
- Uncertainties: None
- Cross-reference status: Verified
