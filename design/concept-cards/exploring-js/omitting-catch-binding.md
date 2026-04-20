---
concept: Omitting the Catch Binding
slug: omitting-catch-binding
category: error-handling
subcategory: exceptions
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exception handling"
chapter_number: 26
pdf_page: null
section: "26.3.2.1 Omitting the `catch` binding"
extraction_confidence: high
aliases:
  - "catch without parameter"
  - "optional catch binding"
prerequisites:
  - try-catch-finally
extends: []
related: []
contrasts_with: []
answers_questions:
  - "Can I catch an error without using the error variable?"
---

# Quick Definition

Since ES2019, the `catch` clause parameter can be omitted when the thrown value is not needed: `try { ... } catch { ... }`.

# Core Definition

As described in "Exploring JavaScript" Ch. 26, since ES2019, we can omit the `catch` parameter if we are not interested in the value that was thrown. The syntax is `catch { ... }` without `(err)`.

# Prerequisites

- Try-catch-finally

# Key Properties

1. Introduced in ES2019.
2. Syntax: `catch { ... }` (no parameter).
3. Useful when only checking if an error occurred, not what it was.

# Construction / Recognition

```js
try {
  riskyOperation();
} catch {
  // error occurred, but we don't need the error value
}
```

# Context & Application

Useful for simple presence-checking of errors, e.g., implementing `assert.throws()`.

# Examples

From the source text (Ch. 26, section 26.3.2.1):

```js
function throws(func) {
  try {
    func();
  } catch {
    return; // everything OK
  }
  throw new Error('Function didn\'t throw an exception!');
}
```

# Relationships

## Builds Upon
- **Try-Catch-Finally** -- simplified catch syntax

# Source Reference

Chapter 26: Exception handling, Section 26.3.2.1, lines 233-267.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit syntax with example
- Cross-reference status: verified
