---
# === CORE IDENTIFICATION ===
concept: Error Handling in Async Code
slug: error-handling-in-async

# === CLASSIFICATION ===
category: asynchronous-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Asynchronous Programming"
chapter_number: 11
pdf_page: null
section: "Failure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - async error handling
  - promise error handling

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - reject
  - try-catch
extends:
  - try-catch
related:
  - catch-method
  - async-function
  - await-keyword
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before using promises and async/await?"
---

# Quick Definition
Error handling in asynchronous code uses promise rejection and `catch` methods (or try/catch with async/await) to propagate and handle failures across asynchronous operations.

# Core Definition
"One of the most pressing problems with the callback style of asynchronous programming is that it makes it extremely difficult to ensure failures are properly reported to the callbacks." Promises address this: "They can be either resolved (the action finished successfully) or rejected (it failed). Resolve handlers (as registered with `then`) are called only when the action is successful, and rejections are propagated to the new promise returned by `then`." (Eloquent JavaScript, Ch. 11, lines 335-368)

# Prerequisites
- **Promise**: Understanding resolution and rejection
- **Try/catch**: Understanding synchronous exception handling

# Key Properties
1. Callback-style error handling uses error-first conventions and is fragile
2. Promise rejections propagate through chains until caught by a `catch`
3. Async/await allows using standard try/catch for async errors
4. Unhandled rejections are detected and reported by the environment
5. Each callback runs on its own call stack, so try/catch around `setTimeout` does not catch errors inside the callback

# Construction / Recognition
With promises:
```javascript
new Promise((_, reject) => reject(new Error("Fail")))
  .then(value => console.log("Handler 1:", value))
  .catch(reason => {
    console.log("Caught failure " + reason);
    return "nothing";
  })
  .then(value => console.log("Handler 2:", value));
```

With async/await:
```javascript
try {
  await withTimeout(joinWifi(networkID, newCode), 50);
  return newCode;
} catch (failure) {
  if (failure == "Timed out") { /* handle */ }
}
```

# Context & Application
Proper error handling is essential in async code because failures in network requests, file I/O, and other operations are common and must be handled gracefully.

# Examples
From the source, demonstrating that try/catch cannot catch async errors:
```javascript
try {
  setTimeout(() => {
    throw new Error("Woosh");
  }, 20);
} catch (e) {
  // This will not run
  console.log("Caught", e);
}
```
(lines 974-982)

"Asynchronous behavior happens on its own empty function call stack. This is one of the reasons that, without promises, managing exceptions across asynchronous code is so hard." (lines 967-969)

# Relationships
## Builds Upon
- Synchronous try/catch and promise rejection
## Enables
- Robust async applications that handle failures gracefully
## Related
- `catch` method on promises
- `await` keyword (converts rejections to thrown exceptions)
## Contrasts With
- Synchronous try/catch (which works on a single call stack)

# Common Errors
- **Error**: Wrapping `setTimeout` in try/catch expecting to catch callback errors
  **Correction**: Use promises or async/await; callbacks run on a separate call stack

# Common Confusions
- **Confusion**: Promise `catch` is the same as try/catch
  **Clarification**: Promise `catch` is a method that registers a rejection handler; with async/await, standard try/catch works because `await` converts rejections to thrown exceptions

# Source Reference
Chapter 11: Asynchronous Programming, Sections "Failure" and "The event loop", lines 325-449, 967-982 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: synthesized from multiple sections
- Confidence rationale: Thoroughly covered across multiple sections
- Cross-reference status: verified
