---
concept: Async/Await Error Handling
slug: async-error-handling
category: async-programming
subcategory: async-await
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 385
section: "13.3.1 await Expressions"
extraction_confidence: high
aliases: []
prerequisites:
  - async-functions
  - await-expressions
extends: []
related:
  - promise-catch
  - error-classes
contrasts_with: []
answers_questions:
  - "How do I use `async/await` with error handling?"
  - "How do I handle errors in a Promise chain?"
---

# Quick Definition

The pattern of using standard `try/catch` blocks around `await` expressions to handle rejected Promises, restoring synchronous-style error handling to asynchronous code.

# Core Definition

When a Promise rejects, "the await p expression throws the rejection value of p" (p. 385). This means standard try/catch handles async errors: rejected Promises become thrown exceptions caught by catch blocks. Thrown exceptions in async functions become rejected Promises. This unifies sync and async error handling.

# Prerequisites

- **async-functions** — Error handling is within async functions
- **await-expressions** — await converts rejections to thrown exceptions

# Key Properties

1. `await` on a rejected Promise throws the rejection reason
2. Standard `try/catch` catches the thrown rejection
3. Thrown exceptions in async functions reject the returned Promise
4. Combines sync and async error handling in one pattern
5. Replaces `.catch()` for error handling within async functions

# Construction / Recognition

```js
async function fetchData(url) {
    try {
        let response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error("Fetch failed:", error);
        return null;
    }
}
```

# Context & Application

The recommended way to handle errors in async/await code. Provides the familiar try/catch pattern that developers know from synchronous code.

# Examples

From the source text (p. 385-386): "If p is rejected, then the await p expression throws the rejection value of p." Combined with the async function discussion: if an async function "appears to throw an exception, then the Promise object that it returns will be rejected with that exception."

# Relationships

## Builds Upon
- **Async Functions** — Provides the context for async error handling
- **Await Expressions** — Converts rejections to thrown exceptions

## Related
- **Promise.catch()** — The Promise-chain equivalent of try/catch
- **Error Classes** — Errors thrown/caught in async code

# Common Errors

- **Error**: Forgetting to add try/catch around await, leaving rejections unhandled.
  **Correction**: Always wrap await expressions in try/catch, or add a `.catch()` to the async function's return value.

# Common Confusions

- **Confusion**: Thinking try/catch around an async function call (without await) catches its errors.
  **Clarification**: `try { asyncFn() } catch(e) {}` does NOT catch async errors. You must `await` the result: `try { await asyncFn() } catch(e) {}`.

# Source Reference

Chapter 13: Asynchronous JavaScript, Sections 13.3.1-13.3.2, pages 385-387.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
