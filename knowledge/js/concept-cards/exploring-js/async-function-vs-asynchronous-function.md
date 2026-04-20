---
concept: Async Function vs Asynchronous Function
slug: async-function-vs-asynchronous-function
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.1.3 Asynchronous callable entities"
extraction_confidence: high
aliases: []
prerequisites:
  - async-function
  - asynchronous-programming-overview
extends: []
related:
  - callback-pattern
  - promise
contrasts_with: []
answers_questions:
  - "What is an async function?"
---

# Quick Definition

An "asynchronous function" is any function that delivers results asynchronously (including callback-based and Promise-based functions), while an "async function" specifically refers to a function defined with the `async` keyword that uses `await` syntax.

# Core Definition

"Exploring JavaScript" Ch. 44: "An asynchronous function is any function that delivers its result asynchronously -- for example, a callback-based function or a Promise-based function. An async function is defined via special syntax, involving the keywords async and await. It is also called async/await due to these two keywords. Async functions are based on Promises and therefore also asynchronous functions (which is somewhat confusing)."

# Prerequisites

- **Async function** -- understanding the specific syntax
- **Asynchronous programming overview** -- understanding the broader concept

# Key Properties

1. "Asynchronous function": broad term for any function with async result delivery
2. "Async function": specific syntax with `async` keyword
3. All async functions are asynchronous functions, but not vice versa
4. Callback-based functions are asynchronous but not async functions
5. The terms are "often used interchangeably" despite the distinction

# Construction / Recognition

Asynchronous (callback-based):
```js
function readFile(path, callback) { /* ... */ }
```

Async function:
```js
async function readFile(path) { /* ... */ }
```

# Context & Application

The distinction matters for precise technical communication but is often blurred in practice.

# Examples

From the source: "That being said: These two terms are also often used interchangeably."

(Ch. 44, Section 44.1.3, lines 226-238)

# Relationships

## Builds Upon
- **Async function** -- the specific term
- **Asynchronous programming overview** -- the general concept

# Common Errors

- **Error**: Assuming all asynchronous code uses the `async` keyword
  **Correction**: Callbacks and plain Promise-returning functions are also asynchronous

# Common Confusions

- **Confusion**: "Asynchronous function" and "async function" mean the same thing
  **Clarification**: "Async function" is specifically defined with `async` keyword; "asynchronous function" is any function with async behavior

# Source Reference

Chapter 44: Async functions, Section 44.1.3, lines 221-238.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit clarification in boxout
- Cross-reference status: verified
