---
concept: Promise.finally()
slug: promise-finally
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 373
section: "13.2.4 More on Promises and Errors"
extraction_confidence: high
aliases:
  - ".finally()"
prerequisites:
  - promise-chaining
extends: []
related:
  - promise-catch
contrasts_with: []
answers_questions:
  - "How do I handle errors in a Promise chain?"
---

# Quick Definition

An ES2018 Promise method whose callback runs when the Promise settles (fulfills or rejects), receiving no arguments, used for cleanup operations like hiding spinners or closing connections, analogous to the `finally` clause in try/catch/finally.

# Core Definition

"If you add a .finally() invocation to your Promise chain, then the callback you pass to .finally() will be invoked when the Promise you called it on settles. Your callback will be invoked if the Promise fulfills or rejects, and it will not be passed any arguments" (p. 373). The return value of the .finally() callback is generally ignored, and the Promise passes through the previous value.

# Prerequisites

- **promise-chaining** — finally() is used in Promise chains

# Key Properties

1. Callback receives no arguments (can't determine fulfill vs. reject)
2. Return value is ignored (Promise passes through)
3. Runs on both fulfillment and rejection
4. If the callback throws, the Promise rejects with that error
5. Returns a new Promise
6. ES2018 feature

# Construction / Recognition

```js
fetch("/api/data")
    .then(processData)
    .catch(handleError)
    .finally(() => hideLoadingSpinner());
```

# Context & Application

Ideal for cleanup code that must run regardless of success or failure: hiding UI elements, closing connections, releasing resources.

# Examples

From the source text (p. 373): Used for cleanup like closing files or network connections. The callback is not passed any arguments, "so you can't find out whether it fulfilled or rejected."

# Relationships

## Builds Upon
- **Promise Chaining** — finally() is a chain operator

## Related
- **Promise.catch()** — catch handles errors; finally handles cleanup

# Common Errors

- **Error**: Trying to use .finally() to access the resolved value.
  **Correction**: .finally() receives no arguments. Use .then() to access values.

# Common Confusions

- **Confusion**: Thinking .finally() replaces .catch().
  **Clarification**: .finally() is for cleanup, not error handling. You still need .catch() for error handling.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.4, page 373.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
