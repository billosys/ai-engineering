---
concept: Async Functions
slug: async-functions
category: async-programming
subcategory: async-await
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 386
section: "13.3.2 async Functions"
extraction_confidence: high
aliases:
  - "async function"
  - "async keyword"
prerequisites:
  - promise-object
extends: []
related:
  - await-expressions
  - promise-chaining
contrasts_with: []
answers_questions:
  - "How does `async/await` relate to Promises?"
  - "How do I use `async/await` with error handling?"
---

# Quick Definition

Functions declared with the `async` keyword that always return a Promise, where normal return values become fulfillment values and thrown exceptions become rejection reasons, enabling the use of `await` inside the function body.

# Core Definition

"Declaring a function async means that the return value of the function will be a Promise even if no Promise-related code appears in the body of the function" (p. 386). "If an async function appears to return normally, then the Promise object that is the real return value of the function will resolve to that apparent return value. And if an async function appears to throw an exception, then the Promise object that it returns will be rejected with that exception."

# Prerequisites

- **promise-object** — Async functions are syntactic sugar over Promises

# Key Properties

1. Declared with `async` keyword before `function`
2. Always returns a Promise
3. Normal return value → Promise fulfills with that value
4. Thrown exception → Promise rejects with that error
5. Enables use of `await` within the function body
6. Works with function declarations, expressions, arrow functions, and methods

# Construction / Recognition

```js
async function getHighScore() {
    let response = await fetch("/api/user/profile");
    let profile = await response.json();
    return profile.highScore;
}
// Usage:
getHighScore().then(displayHighScore).catch(console.error);
displayHighScore(await getHighScore());
```

# Context & Application

The modern way to write asynchronous code in JavaScript. Async functions make Promise-based code look synchronous, dramatically improving readability.

# Examples

From the source text (p. 386-387): `async function getHighScore()` uses await to fetch and parse JSON, then returns the high score. The caller can use either `.then()` or `await` to get the result.

# Relationships

## Builds Upon
- **Promise Object** — Async functions return Promises

## Enables
- **Await Expressions** — The await keyword can only be used inside async functions

## Related
- **Promise Chaining** — Async/await provides an alternative to .then() chains

# Common Errors

- **Error**: Using `await` at the top level of a non-module script.
  **Correction**: `await` can only be used inside `async` functions (or at the top level of ES modules in newer environments).

# Common Confusions

- **Confusion**: Thinking async functions block execution while waiting.
  **Clarification**: "The code remains asynchronous, and the await simply disguises this fact" (p. 386). Other code continues to run while the async function is awaiting.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.3.2, pages 386-387.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
