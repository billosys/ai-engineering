---
concept: Fetch API
slug: fetch-api
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.2.3 Fetch API"
extraction_confidence: high
aliases:
  - fetch()
prerequisites:
  - promise
extends: []
related:
  - promise-chaining
  - async-function
contrasts_with: []
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

The Fetch API is a Promise-based interface for making HTTP requests, available on most JavaScript platforms. `fetch(url)` returns a `Promise<Response>`, and `response.text()` returns a `Promise<string>`.

# Core Definition

"Exploring JavaScript" Ch. 43: "Most JavaScript platforms support Fetch, a Promise-based API for downloading data. Think of it as a Promise-based version of XMLHttpRequest." The API: `fetch(str): Promise<Response>` where `Response extends Body` and `Body` has `text(): Promise<string>`.

# Prerequisites

- **Promise** -- Fetch returns Promises

# Key Properties

1. Promise-based HTTP client
2. `fetch(url)` returns `Promise<Response>`
3. `response.text()` returns `Promise<string>` for body content
4. Available in browsers and most runtimes
5. Replaces XMLHttpRequest for modern code

# Construction / Recognition

```js
fetch('http://example.com/textfile.txt')
  .then(response => response.text())
  .then(text => assert.equal(text, 'Content of textfile.txt'));
```

(Ch. 43, Section 43.2.3, lines 1096-1101)

# Context & Application

Fetch is the standard way to make HTTP requests in modern JavaScript. Commonly used with async/await.

# Examples

With async/await:
```js
async function fetchJsonAsync(url) {
  const request = await fetch(url);
  const text = await request.text();
  return JSON.parse(text);
}
```

(Ch. 44, Section 44.1, lines 75-84)

# Relationships

## Builds Upon
- **Promise** -- Fetch is Promise-based

## Related
- **Promise chaining** -- Fetch results are typically chained
- **Async function** -- Fetch is commonly used with async/await

# Common Errors

- **Error**: Not checking `response.ok` before reading the body
  **Correction**: Fetch does not reject on HTTP errors (404, 500); check `response.ok`

# Common Confusions

- **Confusion**: Fetch rejects on HTTP error status codes
  **Clarification**: Fetch only rejects on network errors; HTTP errors (404, 500) resolve normally

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.2.3, lines 1073-1115.

# Verification Notes

- Definition source: direct from source text with type signatures
- Confidence rationale: explicit section with type definitions
- Cross-reference status: verified against Ch. 44
