---
concept: Named Parameters
slug: named-parameters
category: functions
subcategory: parameters
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.6.6 Named parameters"
extraction_confidence: high
aliases:
  - "simulated named parameters"
  - "options object"
prerequisites:
  - parameter-default-values
extends: []
related:
  - rest-parameters
contrasts_with: []
answers_questions:
  - "How do I simulate named parameters in JavaScript?"
---

# Quick Definition

JavaScript lacks native named parameters but simulates them via destructured object parameters, where each property acts as a named argument.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, JavaScript doesn't have real named parameters. The official simulation uses destructuring on an object parameter: `function f({start=0, end=-1, step=1})`. To make the whole parameter optional, add a default of `{}`: `function f({start=0, end=-1, step=1} = {})`. Named parameters are self-documenting, order-independent, and handle optional parameters gracefully.

# Prerequisites

- Parameter default values
- Destructuring (conceptual)

# Key Properties

1. Simulated via destructuring of an object parameter.
2. Arguments are order-independent.
3. Callers can provide any subset of optional parameters.
4. Add `= {}` as default to make the entire options object optional.
5. More self-documenting than positional parameters.

# Construction / Recognition

```js
function selectEntries({start=0, end=-1, step=1} = {}) {
  return {start, end, step};
}
selectEntries({start: 3, end: 20, step: 2});
```

# Context & Application

Used for functions with many optional parameters or when parameter meanings are unclear from position alone. Common in configuration-style APIs.

# Examples

From the source text (Ch. 27, section 27.6.7):

```js
function selectEntries({start=0, end=-1, step=1} = {}) {
  return {start, end, step};
}
assert.deepEqual(selectEntries(), { start: 0, end: -1, step: 1 });
```

# Relationships

## Builds Upon
- **Parameter Default Values** -- used for individual property defaults
- **Destructuring** -- enables extracting named properties from the argument

# Common Errors

- **Error**: Omitting `= {}` as the parameter default, causing `TypeError` when called with no arguments.
  **Correction**: Add `= {}` to make the entire options object optional.

# Source Reference

Chapter 27: Callable values, Section 27.6.6-27.6.7, lines 1300-1392.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit pattern with rationale
- Cross-reference status: verified
