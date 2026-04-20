---
concept: Promisification
slug: promisification
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.2.2 Browsers: Promisifying XMLHttpRequest"
extraction_confidence: high
aliases:
  - wrapping callbacks in Promises
prerequisites:
  - promise-constructor
  - callback-pattern
extends: []
related:
  - promise
contrasts_with: []
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

Promisification is the technique of wrapping a callback-based API in a Promise, using `new Promise((resolve, reject) => ...)` to convert callback success/error into Promise fulfillment/rejection.

# Core Definition

"Exploring JavaScript" Ch. 43 demonstrates promisification with the XMLHttpRequest example, where a callback-based API is wrapped in `new Promise()`. Success calls `resolve()`, errors call `reject()`. This pattern enables using callback-based APIs with Promise chains and async/await.

# Prerequisites

- **Promise constructor** -- used to create the wrapper Promise
- **Callback pattern** -- the API being wrapped

# Key Properties

1. Wrap the callback API call inside `new Promise()`
2. Call `resolve(result)` on success
3. Call `reject(error)` on failure
4. Enables legacy APIs to work with async/await
5. Node.js provides `util.promisify()` for automatic promisification

# Construction / Recognition

```js
function httpGet(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.onload = () => {
      if (xhr.status === 200) resolve(xhr.responseText);
      else reject(new Error(xhr.statusText));
    };
    xhr.onerror = () => reject(new Error('Network error'));
    xhr.open('GET', url);
    xhr.send();
  });
}
```

(Ch. 43, Section 43.2.2, lines 1021-1038)

# Context & Application

Essential for integrating older callback-based APIs into modern Promise/async-await code.

# Examples

See construction example above. (Ch. 43, Section 43.2.2, lines 1021-1038)

# Relationships

## Builds Upon
- **Promise constructor** -- the wrapping mechanism
- **Callback pattern** -- the pattern being wrapped

## Related
- **Promise** -- promisification creates Promises

# Common Errors

- **Error**: Forgetting to handle the error case in promisification
  **Correction**: Always call `reject()` for error paths

# Common Confusions

- **Confusion**: All callback APIs should be promisified
  **Clarification**: Many Node.js APIs already have Promise-based versions (e.g., `fs/promises`)

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.2.2, lines 1013-1060.

# Verification Notes

- Definition source: inferred from example (term not explicitly defined)
- Confidence rationale: high -- clear example pattern
- Cross-reference status: verified
