---
# === CORE IDENTIFICATION ===
concept: "Function.prototype.bind() Naming"
slug: bound-function-naming

# === CLASSIFICATION ===
category: functions
subcategory: naming
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The property .name of functions (bonus)"
chapter_number: 21
section: "21.2.10 Other programming constructs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "bound function name"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
extends: []
related:
  - function-naming-rules
  - new-function-naming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

Functions created by `.bind()` have a `.name` property prefixed with `'bound '` followed by the original function's name.

# Core Definition

From "Deep JavaScript" (Ch 21.2.10): "`func.bind()` produces a function whose `.name` is `'bound '+func.name`." The prefix is applied by the spec's `SetFunctionName()` operation.

# Prerequisites

- **Function .name property** — Bound functions have specific naming behavior

# Key Properties

1. Name format: `'bound ' + originalFunctionName`
2. Applies to all functions created via `.bind()`
3. The `'bound '` prefix is added by the spec operation `SetFunctionName()`

# Construction / Recognition

## To Construct/Create:
1. `const bound = func.bind(thisArg, ...args)`

## To Identify/Recognize:
1. A `.name` starting with `'bound '`

# Context & Application

The `'bound '` prefix helps identify bound functions in stack traces, making it clear which functions are partially applied or context-bound versions.

# Examples

**Example 1** (Ch 21):
```js
function func(x) {
  return x
}
const bound = func.bind(undefined, 123);
assert.equal(bound.name, 'bound func');
```

# Relationships

## Builds Upon
- **Function .name property** — Bound functions modify the name with a prefix

## Related
- **Getter/setter naming** — Another prefixed naming pattern
- **new Function() naming** — Another special naming case

# Common Confusions

- **Confusion**: Binding a function changes the original function's name
  **Clarification**: `.bind()` returns a *new* function with the prefixed name; the original is unchanged

# Source Reference

Chapter 21: The property .name of functions (bonus), Section 21.2.10, lines 11437+.

# Verification Notes

- Definition source: direct from source with assertion
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified (references SetFunctionName() spec)
