---
concept: util.promisify
slug: util-promisify
category: node-apis
subcategory: fundamentals
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 601
section: "16.2 Node Is Asynchronous by Default"
extraction_confidence: high
aliases:
  - promisify
prerequisites:
  - error-first-callbacks
extends: []
related:
  - fs-module
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
---

# Quick Definition

`util.promisify()` wraps a Node-style error-first callback function and returns a new function that returns a Promise, enabling use with `async`/`await`.

# Core Definition

Because Node is fairly consistent about its error-first callbacks, it is easy to create Promise-based variants of callback-based APIs using the `util.promisify()` wrapper. The returned function converts the error-first callback pattern into a Promise that rejects on error or resolves with the result. In Node 10+, `fs.promises` provides predefined Promise-based filesystem functions, eliminating the need for manual promisification of fs methods (Flanagan, Ch. 16, pp. 601-602).

# Prerequisites

- **error-first-callbacks** — Must understand the callback pattern being wrapped.

# Key Properties

1. Takes a function expecting an error-first callback.
2. Returns a new function that returns a Promise.
3. The Promise rejects with the error or resolves with the result.
4. `fs.promises` provides built-in Promise-based filesystem functions since Node 10.

# Construction / Recognition

```javascript
const util = require("util");
const fs = require("fs");
const readFile = util.promisify(fs.readFile);
async function readConfig(path) {
  let text = await readFile(path, "utf-8");
  return JSON.parse(text);
}
```

# Context & Application

Bridges the gap between Node's legacy callback APIs and modern async/await code. Particularly useful for third-party libraries that only offer callback APIs.

# Examples

From the source (p. 601): Converting `fs.readFile` to a Promise-based function and using it with async/await.

# Relationships

## Builds Upon
- **error-first-callbacks** — Wraps the callback pattern

## Enables
- Modern async/await code with legacy APIs

## Related
- **fs-module** — Common target for promisification

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `util.promisify()` on functions that don't follow the error-first callback convention.
  **Correction**: Only use it with functions whose last argument is a `(err, result)` callback.

# Common Confusions

- **Confusion**: You still need `util.promisify()` for all fs operations.
  **Clarification**: Since Node 10, `fs.promises` provides native Promise-based versions of most fs functions.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.2, pages 601-602.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear example showing the pattern
- Uncertainties: None
- Cross-reference status: Verified
