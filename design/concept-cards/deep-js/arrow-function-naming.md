---
# === CORE IDENTIFICATION ===
concept: Arrow Function Naming
slug: arrow-function-naming

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
section: "21.2.2 Variable declarations and anonymous functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
  - anonymous-function-expression
extends:
  - anonymous-function-expression
related:
  - function-naming-rules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

Arrow functions follow the same naming inference rules as anonymous function expressions, getting their `.name` from the variable, property, or parameter they are assigned to.

# Core Definition

From "Deep JavaScript" (Ch 21.2.2): "With regard to names, arrow functions are like anonymous function expressions: `const arrowFunc = () => {}; assert.equal(arrowFunc.name, 'arrowFunc');`." And: "From now on, whenever you see an anonymous function expression, you can assume that an arrow function works the same way."

# Prerequisites

- **Function .name property** — Arrow function naming sets `.name`
- **Anonymous function expression** — Arrow functions follow the same rules

# Key Properties

1. Arrow functions are always anonymous (no syntax for naming them)
2. Name is inferred from context identically to anonymous function expressions
3. In the spec, `SetFunctionName()` is not called when creating arrow functions -- engines diverge from spec here

# Construction / Recognition

## To Construct/Create:
1. `const arrowFunc = () => {};` -- name is `'arrowFunc'`

## To Identify/Recognize:
1. An arrow function assigned to a variable, property, or parameter

# Context & Application

Arrow functions are the most common type of anonymous function in modern JavaScript. Their naming behavior is identical to anonymous function expressions.

# Examples

**Example 1** (Ch 21):
```js
const arrowFunc = () => {};
assert.equal(arrowFunc.name, 'arrowFunc');
```

**Example 2** (Ch 21): Spec divergence:
```js
// Most engines create a .name own property for arrow functions,
// even though the spec does not call SetFunctionName() for them:
> Reflect.ownKeys(() => {})
[ 'length', 'name' ]
```

# Relationships

## Builds Upon
- **Anonymous function expression** — Same naming rules

## Related
- **Function naming rules** — Arrow functions are one of many naming contexts

# Common Confusions

- **Confusion**: Arrow functions can't have names
  **Clarification**: While they can't be explicitly named in their syntax, they infer names from context just like anonymous function expressions

# Source Reference

Chapter 21: The property .name of functions (bonus), Sections 21.2.2, 21.5, lines 11437+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly stated equivalence with examples
- Cross-reference status: verified (includes spec divergence note)
