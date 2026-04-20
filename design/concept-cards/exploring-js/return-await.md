---
concept: return await Pattern
slug: return-await
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.6.3 The pros and cons of return await"
extraction_confidence: high
aliases:
  - return await vs return
prerequisites:
  - async-function
  - await-operator
extends: []
related:
  - async-function-return-semantics
contrasts_with: []
answers_questions:
  - "How do I use async/await to write asynchronous code?"
---

# Quick Definition

`return await promise` inside an async function unwraps the Promise before re-wrapping it, which is technically redundant but has the advantage of behaving correctly inside `try-catch` blocks where plain `return promise` would bypass the catch.

# Core Definition

"Exploring JavaScript" Ch. 44 gives three reasons to prefer `return await`: "The code fragment is easier to move around. We don't depend on a feature of Promises that is slightly obscure: resolving unwraps Promises. It behaves better inside a try-catch statement."

# Prerequisites

- **Async function** -- pattern occurs in async functions
- **Await operator** -- `await` unwraps the Promise

# Key Properties

1. `return await` unwraps then re-wraps the Promise (seemingly redundant)
2. Critical inside try/catch: `return await rejectedPromise` triggers the catch block
3. Plain `return rejectedPromise` bypasses catch (the rejection passes through)
4. Code with `return await` is easier to refactor

# Construction / Recognition

With `return await` -- catch works:
```js
async function f() {
  try {
    return await Promise.reject('error');
  } catch (err) {
    return 'Caught an error: ' + err;
  }
}
f().then(result => assert.equal(result, 'Caught an error: error'));
```

Without `return await` -- catch bypassed:
```js
async function f() {
  try {
    return Promise.reject('error');
  } catch (err) {
    return 'Caught an error: ' + err;
  }
}
f().catch(reason => assert.equal(reason, 'error'));
```

(Ch. 44, Section 44.6.3, lines 706-737)

# Context & Application

Always use `return await` inside try/catch blocks when returning Promise-based results. Outside try/catch, either form is acceptable.

# Examples

See construction examples above. (Ch. 44, Section 44.6.3, lines 706-737)

# Relationships

## Builds Upon
- **Async function** -- context for this pattern
- **Await operator** -- the mechanism

## Related
- **Async function return semantics** -- this is a subtlety of return behavior

# Common Errors

- **Error**: Using plain `return` with a potentially rejected Promise inside try/catch
  **Correction**: Use `return await` to ensure the rejection is caught

# Common Confusions

- **Confusion**: `return await` is always unnecessary
  **Clarification**: Inside try/catch, `return await` is necessary for correct error handling

# Source Reference

Chapter 44: Async functions, Section 44.6.3, lines 675-737.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with both correct and incorrect examples
- Cross-reference status: verified
