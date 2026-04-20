---
# === CORE IDENTIFICATION ===
concept: Named Function Expression
slug: named-function-expression

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
section: "21.2.5 Named function expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "NFE"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
extends: []
related:
  - anonymous-function-expression
  - function-naming-rules
contrasts_with:
  - anonymous-function-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

A named function expression is a function expression with an explicit name that sets the `.name` property and is accessible as a local variable only inside the function body.

# Core Definition

From "Deep JavaScript" (Ch 21.2.5): "The name of a named function expression is used to set up the `.name` property." The expression name takes precedence over other names: "Because it comes first, the function expression's name `funcName` takes precedence over other names (in this case, the name `varName` of the variable). However, the name of a function expression is still only a variable inside the function expression."

# Prerequisites

- **Function .name property** — Named function expressions set `.name`

# Key Properties

1. Syntax: `function funcName() { ... }` used as an expression (not declaration)
2. The expression name takes precedence over the variable name for `.name`
3. The name is only accessible as a variable inside the function body
4. Outside the function, the name is not defined (throws `ReferenceError`)

# Construction / Recognition

## To Construct/Create:
1. `const varName = function funcName() { ... };`

## To Identify/Recognize:
1. A function expression (assigned to variable, passed as argument, etc.) that has an explicit name

# Context & Application

Named function expressions are useful for self-referencing recursion inside the function body and for providing meaningful stack trace names regardless of how the function is assigned.

# Examples

**Example 1** (Ch 21): Name precedence and scope:
```js
const varName = function funcName() {
  assert.equal(funcName.name, 'funcName');
};
varName();
assert.equal(varName.name, 'funcName'); // expression name wins

assert.throws(
  () => funcName,
  /^ReferenceError: funcName is not defined$/
);
```

# Relationships

## Builds Upon
- **Function .name property** — Sets `.name` to the expression name

## Related
- **Function naming rules** — One of many naming constructs

## Contrasts With
- **Anonymous function expression** — Has no explicit name; `.name` inferred from context

# Common Errors

- **Error**: Trying to access the function expression name outside the function
  **Correction**: The name is only a local variable inside the function body

# Common Confusions

- **Confusion**: The variable name and expression name are the same thing
  **Clarification**: `const varName = function funcName() {}` has two different names; `funcName` takes precedence for `.name` but is only accessible inside the function

# Source Reference

Chapter 21: The property .name of functions (bonus), Section 21.2.5, lines 11437+.

# Verification Notes

- Definition source: direct from source text with examples
- Confidence rationale: Explicitly demonstrated with assertions
- Cross-reference status: verified
