---
concept: Error Classes and Custom Errors
slug: error-classes
category: standard-library
subcategory: error-handling
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 322
section: "11.5 Error Classes"
extraction_confidence: high
aliases:
  - "Error object"
  - "custom errors"
prerequisites: []
extends: []
related:
  - promise-catch
contrasts_with: []
answers_questions: []
---

# Quick Definition

JavaScript's `Error` class and its built-in subclasses (`TypeError`, `RangeError`, etc.) for signaling errors with stack traces, plus the ability to create custom Error subclasses with domain-specific properties.

# Core Definition

"JavaScript does define an Error class, and it is traditional to use instances of Error or a subclass when signaling an error with throw" (p. 322). Error objects have `message`, `name`, and (non-standard but universal) `stack` properties. Built-in subclasses: `EvalError`, `RangeError`, `ReferenceError`, `SyntaxError`, `TypeError`, `URIError`. Custom subclasses can add properties like HTTP status codes.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `message` — the error description passed to the constructor
2. `name` — the error type name (e.g., "Error", "TypeError")
3. `stack` — stack trace (non-standard but universally supported)
4. Stack trace captures where Error was created, not where it was thrown
5. Custom subclasses can add domain-specific properties

# Construction / Recognition

```js
throw new Error("something went wrong");
class HTTPError extends Error {
    constructor(status, statusText, url) {
        super(`${status} ${statusText}: ${url}`);
        this.status = status;
        this.statusText = statusText;
        this.url = url;
    }
    get name() { return "HTTPError"; }
}
```

# Context & Application

Used whenever an error condition needs to be signaled. Custom Error subclasses are valuable for API design, allowing callers to distinguish different error types with `instanceof`.

# Examples

From the source text (p. 322-323): Custom `HTTPError` class with `status`, `statusText`, and `url` properties: `new HTTPError(404, "Not Found", "http://example.com/")`. Error has `status` of 404, `message` of "404 Not Found: http://example.com/", and `name` of "HTTPError".

# Relationships

## Enables
- **Promise error handling** — Errors are the standard rejection values in Promise chains

# Common Errors

- **Error**: Throwing a string instead of an Error object: `throw "error"`.
  **Correction**: Always throw Error objects to get stack traces: `throw new Error("error")`.

# Common Confusions

- **Confusion**: Thinking the stack trace shows where the error was thrown.
  **Clarification**: The stack trace captures where the Error object was *created* (`new Error()`), not where `throw` is called. Create the Error immediately before throwing.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.5, pages 322-323.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
