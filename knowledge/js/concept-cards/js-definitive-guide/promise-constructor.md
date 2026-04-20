---
concept: Promise Constructor
slug: promise-constructor
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 380
section: "13.2.6 Making Promises"
extraction_confidence: high
aliases:
  - "new Promise()"
  - "Promise executor"
prerequisites:
  - promise-object
extends: []
related:
  - promise-resolve-reject
contrasts_with: []
answers_questions:
  - "What is a Promise?"
---

# Quick Definition

The `new Promise((resolve, reject) => {...})` constructor that creates a Promise whose fate is controlled by calling the provided `resolve()` and `reject()` functions, enabling wrapping of callback-based APIs as Promises.

# Core Definition

"You invoke the Promise() constructor and pass a function as its only argument. The function you pass should be written to expect two parameters, which, by convention, should be named resolve and reject" (p. 380). The constructor synchronously calls this "executor" function, giving it control over when and how the resulting Promise settles.

# Prerequisites

- **promise-object** — Understanding Promise states and semantics

# Key Properties

1. Takes an executor function: `(resolve, reject) => { ... }`
2. Executor runs synchronously during construction
3. `resolve(value)` — fulfills (or resolves to) the Promise
4. `reject(reason)` — rejects the Promise
5. If resolve is passed a Promise, the new Promise "locks onto" that Promise
6. Can resolve/reject synchronously, but settlement is still async

# Construction / Recognition

```js
function wait(duration) {
    return new Promise((resolve, reject) => {
        if (duration < 0) reject(new Error("Time travel not yet implemented"));
        setTimeout(resolve, duration);
    });
}
```

# Context & Application

Used to convert callback-based or event-based APIs into Promise-based APIs. The primary way to create Promises "from scratch" when no existing Promise-returning function is available.

# Examples

From the source text (p. 380-382): The `wait()` function wraps setTimeout in a Promise. The Node `getJSON()` function wraps http.get() with event handlers, calling `resolve()` on success and `reject()` on error.

# Relationships

## Builds Upon
- **Promise Object** — The constructor creates Promises

## Related
- **Promise.resolve/reject** — Static methods for creating already-settled Promises

# Common Errors

- **Error**: Calling both `resolve()` and `reject()`, or calling one multiple times.
  **Correction**: Only the first call to resolve or reject has effect. Subsequent calls are silently ignored.

# Common Confusions

- **Confusion**: Thinking `resolve()` always fulfills the Promise.
  **Clarification**: `resolve(anotherPromise)` locks onto that Promise — the new Promise may still reject if `anotherPromise` rejects. The functions are named resolve/reject, not fulfill/reject.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.6, pages 380-382.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
