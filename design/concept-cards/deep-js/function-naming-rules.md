---
# === CORE IDENTIFICATION ===
concept: Function Naming Rules
slug: function-naming-rules

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
section: "21.2 Constructs that provide names for functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "name inference"
  - "automatic function naming"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
extends: []
related:
  - named-function-expression
  - anonymous-function-expression
  - arrow-function-naming
  - method-naming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

Function naming rules are the set of JavaScript constructs that automatically provide names for functions, including variable declarations, assignments, default values, property definitions, and class methods.

# Core Definition

From "Deep JavaScript" (Ch 21.2): JavaScript infers names from numerous contexts. The following constructs set `.name`:

1. Function declarations: name from declaration
2. Variable declarations with anonymous functions: name from variable
3. Assignments: name from assignment target
4. Default values: name from destructured variable or parameter
5. Named function expressions: name from expression (takes precedence)
6. Object literal methods: name from property key
7. Class methods: name from method name
8. Default exports: name is `'default'`

The name is always assigned at creation time and never updated later.

# Prerequisites

- **Function .name property** — These rules determine how `.name` is set

# Key Properties

1. Name inference works for function expressions, arrow functions, and class expressions
2. Named function expression name takes precedence over variable name
3. Getters are prefixed with `'get '`, setters with `'set '`
4. Symbol-keyed methods have the symbol description in square brackets
5. Name is set at creation time only

# Construction / Recognition

## To Construct/Create:
1. Use any of the naming constructs listed above

## To Identify/Recognize:
1. Check `func.name` to see what name was inferred

# Context & Application

Understanding these rules helps predict what names will appear in stack traces. The creation-time-only rule means returning an anonymous function from a factory and later assigning it does not give it a name.

# Examples

**Example 1** (Ch 21): Variable declaration:
```js
const constFunc = function () {};
assert.equal(constFunc.name, 'constFunc');
```

**Example 2** (Ch 21): Named function expression takes precedence:
```js
const varName = function funcName() {};
assert.equal(varName.name, 'funcName');
```

**Example 3** (Ch 21): Creation-time only:
```js
function functionFactory() {
  return function () {}; // name set to '' here
}
const func = functionFactory();
assert.equal(func.name, ''); // not 'func'
```

# Relationships

## Builds Upon
- **Function .name property** — These rules populate `.name`

## Related
- **Named function expression** — One of the naming constructs
- **Arrow function naming** — Arrow functions follow the same inference rules
- **Method naming** — Methods get names from property keys

# Common Errors

- **Error**: Expecting a function to get its name from a later assignment
  **Correction**: Name is only set at creation; a factory-returned function won't pick up the variable name

# Common Confusions

- **Confusion**: All anonymous functions have empty names
  **Clarification**: JavaScript infers names from context (variable declarations, assignments, etc.); truly anonymous functions only result from specific patterns like factory returns

# Source Reference

Chapter 21: The property .name of functions (bonus), Section 21.2, lines 11437+.

# Verification Notes

- Definition source: synthesized from multiple subsections
- Confidence rationale: High -- all rules explicitly demonstrated with assertions
- Cross-reference status: verified
