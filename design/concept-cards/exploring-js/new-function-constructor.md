---
concept: new Function() Constructor
slug: new-function-constructor
category: functions
subcategory: dynamic-evaluation
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Evaluating code dynamically: `eval()`, `new Function()` (advanced)"
chapter_number: 28
pdf_page: null
section: "28.2 `new Function()`"
extraction_confidence: high
aliases:
  - "Function constructor"
  - "new Function"
prerequisites:
  - eval-function
extends: []
related:
  - eval-function
contrasts_with:
  - eval-function
answers_questions:
  - "How can I create a function from a string of code?"
---

# Quick Definition

`new Function()` creates a function object from strings specifying parameters and a body, always executing in global context.

# Core Definition

As described in "Exploring JavaScript" Ch. 28, `new Function('param1', ..., 'paramN', 'funcBody')` creates a function equivalent to `function(param1, ..., paramN) { funcBody }`. It always executes in global context and provides a clean interface to evaluated code. Functions created this way are in sloppy mode by default. Preferred over `eval()` for dynamic code evaluation.

# Prerequisites

- eval() function (to understand the alternative)

# Key Properties

1. Always executes in global context (no access to local variables).
2. Provides a clean function interface.
3. Created functions are in sloppy mode by default.
4. Preferred over `eval()` when dynamic evaluation is necessary.
5. Security risk: same as `eval()`, may be disabled by CSP.

# Construction / Recognition

```js
const times = new Function('a', 'b', 'return a * b');
times(3, 4); // 12
```

# Context & Application

Used in rare cases where code must be generated dynamically. Prefer over `eval()` because it runs in global scope and has a clean function interface.

# Examples

From the source text (Ch. 28, section 28.2):

```js
const times1 = new Function('a', 'b', 'return a * b');
const times2 = function (a, b) { return a * b };
// times1 and times2 are equivalent
```

# Relationships

## Contrasts With
- **eval() Function** -- `eval()` can access local scope; `new Function()` always uses global scope

# Common Errors

- **Error**: Expecting `new Function()` to access local variables.
  **Correction**: `new Function()` always runs in global scope; use closures for local access.

# Source Reference

Chapter 28: Evaluating code dynamically, Section 28.2-28.3, lines 73-144.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit equivalence and recommendation shown
- Cross-reference status: verified
