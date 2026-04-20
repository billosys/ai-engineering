---
concept: Stack Trace
slug: stack-trace
category: error-handling
subcategory: debugging
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exception handling"
chapter_number: 26
pdf_page: null
section: "26.4.3 Error instance property `.stack`"
extraction_confidence: high
aliases:
  - ".stack"
  - "error stack"
prerequisites:
  - error-class
extends: []
related:
  - throw-statement
contrasts_with: []
answers_questions:
  - "How do I see where an error occurred?"
---

# Quick Definition

A stack trace is a string (via `.stack`) showing the chain of function calls active when an `Error` was created, valuable for debugging.

# Core Definition

As described in "Exploring JavaScript" Ch. 26, the `.stack` property is not standardized in ECMAScript but is widely supported. It is usually a string whose format varies between engines. On V8, it shows the error message followed by lines indicating the function, file, and line number at each level of the call stack.

# Prerequisites

- Error class

# Key Properties

1. Non-standard but widely supported.
2. Format varies between engines.
3. Shows call chain at the point of `Error` creation.
4. Named functions appear with their names (aiding debugging).

# Construction / Recognition

```js
function h() { const error = new Error(); console.log(error.stack); }
function g() { h(); }
function f() { g(); }
f();
```

Output (V8):
```
Error
    at h (file.mjs:1:25)
    at g (file.mjs:2:3)
    at f (file.mjs:3:3)
```

# Context & Application

Essential for debugging. Named functions provide better stack traces than anonymous ones.

# Examples

From the source text (Ch. 26, section 26.4.3):

```
Error
    at h (demos/async-js/stack_trace.mjs:2:17)
    at g (demos/async-js/stack_trace.mjs:6:3)
    at f (demos/async-js/stack_trace.mjs:9:3)
```

# Relationships

## Builds Upon
- **Error Class** -- `.stack` is a property of Error instances

# Source Reference

Chapter 26: Exception handling, Section 26.4.3, lines 423-458.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit example with output
- Cross-reference status: verified
