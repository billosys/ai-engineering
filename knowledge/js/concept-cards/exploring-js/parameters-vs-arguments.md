---
concept: Parameters vs Arguments
slug: parameters-vs-arguments
category: functions
subcategory: parameters
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.6.1 Terminology: parameters vs. arguments"
extraction_confidence: high
aliases:
  - "formal parameters"
  - "actual arguments"
prerequisites: []
extends: []
related:
  - parameter-default-values
  - rest-parameters
contrasts_with: []
answers_questions:
  - "What is the difference between parameters and arguments?"
---

# Quick Definition

Parameters are the variables in a function definition; arguments are the actual values passed in a function call.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, *parameters* are part of a function definition (also called formal parameters), while *arguments* are part of a function call (also called actual arguments). JavaScript does not complain about mismatches: extra arguments are ignored, and missing parameters are set to `undefined`.

# Prerequisites

- Foundational concept with no prerequisites

# Key Properties

1. Parameters: in definitions (formal parameters).
2. Arguments: in calls (actual arguments).
3. Extra arguments are silently ignored.
4. Missing parameters get `undefined`.

# Construction / Recognition

```js
function foo(x, y) { return [x, y]; }  // x, y are parameters
foo('a', 'b', 'c');  // 'a', 'b', 'c' are arguments; 'c' is ignored
foo('a');             // y is undefined
```

# Context & Application

Understanding this distinction helps with parameter default values, rest parameters, and debugging argument mismatches.

# Examples

From the source text (Ch. 27, section 27.6.3):

```js
function foo(x, y) { return [x, y]; }
assert.deepEqual(foo('a', 'b', 'c'), ['a', 'b']);
assert.deepEqual(foo('a'), ['a', undefined]);
```

# Relationships

## Enables
- **Parameter Default Values** -- defaults fill missing arguments
- **Rest Parameters** -- collect extra arguments

# Source Reference

Chapter 27: Callable values, Section 27.6.1-27.6.3, lines 1137-1197.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit terminology section
- Cross-reference status: verified
