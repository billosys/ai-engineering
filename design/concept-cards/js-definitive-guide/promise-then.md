---
concept: Promise.then() Method
slug: promise-then
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 365
section: "13.2.1 Using Promises"
extraction_confidence: high
aliases:
  - ".then()"
prerequisites:
  - promise-object
extends: []
related:
  - promise-chaining
  - promise-catch
contrasts_with: []
answers_questions:
  - "What is a Promise?"
---

# Quick Definition

The primary method on Promise objects for registering callback functions that will be invoked when the Promise is fulfilled (first argument) or rejected (optional second argument), returning a new Promise to enable chaining.

# Core Definition

"You can think of the then() method as a callback registration method" (p. 366). `then()` takes one or two arguments: a fulfillment handler and an optional rejection handler. It always returns a new Promise, enabling chaining. Each function registered with `then()` will be invoked only once, and always asynchronously.

# Prerequisites

- **promise-object** — then() is a method on Promise objects

# Key Properties

1. First argument: function called when Promise fulfills (receives fulfillment value)
2. Second argument (optional): function called when Promise rejects (receives rejection reason)
3. Always returns a new Promise (enables chaining)
4. Callbacks are invoked asynchronously, even if the Promise is already settled
5. The return value of the callback determines the fate of the returned Promise

# Construction / Recognition

```js
getJSON("/api/user/profile").then(displayUserProfile);
getJSON(url).then(displayUserProfile, handleProfileError);
```

# Context & Application

The fundamental building block of Promise-based programming. Typically, the two-argument form is replaced by chaining `.then()` with `.catch()`.

# Examples

From the source text (p. 365-366): `getJSON("/api/user/profile").then(displayUserProfile)` — the function is called when the JSON data is available. Can register multiple callbacks by calling `then()` multiple times on the same Promise.

# Relationships

## Builds Upon
- **Promise Object** — then() is the primary Promise API method

## Enables
- **Promise Chaining** — Each then() returns a new Promise
- **Promise.catch()** — catch() is shorthand for then(null, handler)

# Common Errors

- **Error**: Forgetting to return a value from a `.then()` callback, especially with curly braces.
  **Correction**: Arrow functions with curly braces need explicit `return`. `.then(x => { doSomething(x) })` returns undefined; use `.then(x => { return doSomething(x) })` or `.then(x => doSomething(x))`.

# Common Confusions

- **Confusion**: Thinking multiple `.then()` calls create a chain.
  **Clarification**: Calling `.then()` multiple times on the *same* Promise registers parallel handlers. Chaining requires calling `.then()` on the *returned* Promise.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.1, pages 365-367.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
