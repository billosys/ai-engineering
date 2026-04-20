---
concept: setTimeout and setInterval
slug: set-timeout-set-interval
category: standard-library
subcategory: timers
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 340
section: "11.10 Timers"
extraction_confidence: high
aliases:
  - "timers"
  - "clearTimeout"
  - "clearInterval"
prerequisites: []
extends: []
related:
  - callback-pattern
contrasts_with: []
answers_questions: []
---

# Quick Definition

Global timer functions that schedule code execution: `setTimeout()` runs a function once after a delay, and `setInterval()` runs a function repeatedly at a specified interval, both returning IDs that can cancel execution via `clearTimeout()`/`clearInterval()`.

# Core Definition

"web browsers have defined two functions—setTimeout() and setInterval()—that allow programs to ask the browser to invoke a function after a specified amount of time has elapsed or to invoke the function repeatedly at a specified interval" (p. 340). Both return an opaque value used with `clearTimeout()`/`clearInterval()` to cancel scheduled execution.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `setTimeout(fn, ms)` — invokes `fn` once after `ms` milliseconds
2. `setInterval(fn, ms)` — invokes `fn` repeatedly every `ms` milliseconds
3. Both return an ID for cancellation
4. `clearTimeout(id)` / `clearInterval(id)` cancel scheduled execution
5. `setTimeout` with `ms=0` schedules execution "as soon as possible" (not immediately)
6. Not part of ECMAScript standard but universally supported

# Construction / Recognition

```js
setTimeout(() => { console.log("Ready..."); }, 1000);
let clock = setInterval(() => {
    console.clear();
    console.log(new Date().toLocaleTimeString());
}, 1000);
setTimeout(() => { clearInterval(clock); }, 10000);
```

# Context & Application

Fundamental to asynchronous programming. Used for delayed execution, polling, animation, debouncing, and throttling. Understanding timers is prerequisite to understanding Promises and async/await.

# Examples

From the source text (p. 340-341): Three consecutive `setTimeout()` calls print "Ready...", "set...", "go!" after 1, 2, and 3 seconds. Digital clock: `setInterval` updates the console every second, `setTimeout` stops it after 10 seconds.

# Relationships

## Enables
- **Callback Pattern** — Timers are a fundamental example of callback-based asynchrony
- **Promise-based wait** — Timers are wrapped in Promises for async/await usage

# Common Errors

- **Error**: Expecting `setTimeout(fn, 0)` to execute `fn` immediately.
  **Correction**: Even with delay 0, the function is scheduled and may not run for 10ms or more depending on system load.

# Common Confusions

- **Confusion**: Thinking `setInterval` guarantees exact timing between invocations.
  **Clarification**: `setInterval` schedules at approximate intervals. If the callback takes longer than the interval, invocations may queue up or drift.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.10, pages 340-341.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
