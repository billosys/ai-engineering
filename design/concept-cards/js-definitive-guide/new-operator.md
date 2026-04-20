---
# === CORE IDENTIFICATION ===
concept: The new Operator
slug: new-operator

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 85
section: "4.6 Object Creation Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "object creation expression"
  - "constructor call"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - invocation-expressions
extends: []
related:
  - constructor-functions
  - prototype-objects
contrasts_with:
  - invocation-expressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the prototype chain?"
---

# Quick Definition

The `new` operator creates a new object and invokes a constructor function to initialize it. The value of the expression is the newly created object.

# Core Definition

"An *object creation expression* creates a new object and invokes a function (called a constructor) to initialize the properties of that object. Object creation expressions are like invocation expressions except that they are prefixed with the keyword new." (Ch. 4, §4.6)

# Prerequisites

- **invocation-expressions** — Object creation expressions are a form of invocation prefixed with `new`.

# Key Properties

1. Syntax: `new Constructor(args)`.
2. If no arguments are passed, the empty parentheses can be omitted: `new Object`, `new Date`.
3. The value of the expression is the newly created object.
4. The newly created object's prototype is set to the constructor's `prototype` property.

# Construction / Recognition

```js
new Object()
new Point(2,3)
new Date       // Parentheses optional when no arguments
```

# Context & Application

The `new` operator is the primary mechanism for creating instances from constructor functions and, by extension, from classes. It sets up the prototype chain that enables inheritance.

# Examples

From the source text (§4.6, p. 85):

```js
new Object()    // Create an empty object: same as {}.
new Array()     // Create an empty array: same as [].
new Date()      // Create a Date object representing the current time
new Map()       // Create a Map object for key/value mapping
```

# Relationships

## Builds Upon
- **invocation-expressions** — `new` extends function invocation with object creation

## Enables
- **constructor-functions** — `new` is the mechanism that invokes constructors
- **prototype-objects** — `new` sets the prototype of the created object

## Related
- **object-literals** — Alternative way to create objects without `new`

## Contrasts With
- **invocation-expressions** — Regular invocation calls a function; `new` invocation creates an object, sets its prototype, calls the constructor with `this` bound to the new object

# Common Errors

- **Error**: Calling a constructor without `new`, causing unexpected behavior.
  **Correction**: Always use `new` with constructor functions (or use `class` syntax which enforces it).

# Common Confusions

- **Confusion**: Believing `new` is only for built-in types.
  **Clarification**: You can define your own constructor functions and use `new` with them to create custom objects.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.6, page 85.

# Verification Notes

- Definition source: Direct quote from §4.6
- Confidence rationale: High — clearly defined
- Uncertainties: Constructor details deferred to Ch. 9
- Cross-reference status: Verified against §6.2.2
