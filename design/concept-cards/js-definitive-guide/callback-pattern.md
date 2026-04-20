---
concept: Callback Pattern
slug: callback-pattern
category: async-programming
subcategory: callbacks
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 359
section: "13.1 Asynchronous Programming with Callbacks"
extraction_confidence: high
aliases:
  - "callback function"
  - "callback-based programming"
prerequisites: []
extends: []
related:
  - error-first-callbacks
  - promise-object
contrasts_with:
  - promise-object
answers_questions:
  - "What must I understand before learning about Promises?"
---

# Quick Definition

The fundamental asynchronous programming pattern where a function is passed as an argument to another function and is "called back" when an asynchronous operation completes or an event occurs.

# Core Definition

"A callback is a function that you write and then pass to some other function. That other function then invokes ('calls back') your function when some condition is met or some (asynchronous) event occurs" (p. 359). Callbacks are the basis of event handlers (`addEventListener`), timers (`setTimeout`), and Node I/O operations.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A function passed as an argument to another function
2. Invoked when an asynchronous operation completes or event occurs
3. The basis for event-driven programming in browsers
4. Node.js uses error-first callback convention
5. Nesting callbacks leads to "callback hell"

# Construction / Recognition

```js
setTimeout(checkForUpdates, 60000);
okay.addEventListener('click', applyUpdate);
fs.readFile("config.json", "utf-8", (err, text) => { /* ... */ });
```

# Context & Application

The oldest and most fundamental async pattern in JavaScript. Understanding callbacks is prerequisite to understanding Promises, which were designed to address callback limitations.

# Examples

From the source text (p. 359-363): Timer callback: `setTimeout(checkForUpdates, 60000)`. Event callback: `okay.addEventListener('click', applyUpdate)`. Node file reading: `fs.readFile("config.json", "utf-8", (err, text) => { ... })`.

# Relationships

## Enables
- **Error-First Callbacks** — The Node convention for error handling with callbacks
- **Promise Object** — Promises were designed to improve on callbacks

## Contrasts With
- **Promise Object** — Promises linearize nested callbacks and standardize error handling

# Common Errors

- **Error**: Deeply nesting callbacks, creating "callback hell" (pyramid of doom).
  **Correction**: Use Promises or async/await to flatten nested callbacks into linear chains.

# Common Confusions

- **Confusion**: Thinking exceptions thrown in callbacks can be caught by the calling code.
  **Clarification**: "If an asynchronous function throws an exception, there is no way for that exception to propagate back to the initiator of the asynchronous operation" (p. 364).

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.1, pages 359-363.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
