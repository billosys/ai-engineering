---
# === CORE IDENTIFICATION ===
concept: Variables Overview
slug: variables-overview

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: variables
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Introduction to JavaScript"
chapter_number: 1
pdf_page: 22
section: "1.3 A Tour of JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
extends: []
related:
  - let-and-const-declarations
  - var-declarations
  - type-system-overview
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do `let`/`const` relate to `var` in terms of scoping?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

Variables in JavaScript are symbolic names for values, declared with `let`, `const`, or `var`, and are untyped — any variable can hold any type of value.

# Core Definition

As introduced in Chapter 1: "A variable is a symbolic name for a value. Variables are declared with the let keyword." JavaScript variables are untyped: "declarations do not specify what kind of values will be assigned" (p. 40). Constants are declared with `const`, and the older `var` keyword is also available. (pp. 22, 40)

# Prerequisites

- **javascript-language-overview** — Variables are a fundamental part of the language

# Key Properties

1. Three declaration keywords: `let`, `const`, `var`
2. Variables are untyped — can hold values of any type
3. `let` declares a mutable variable
4. `const` declares an immutable binding (the value cannot be reassigned)
5. `var` is the pre-ES6 declaration keyword with different scoping rules
6. Undeclared variables get the value `undefined`

# Construction / Recognition

```javascript
let x;            // Declare a variable named x
x = 0;            // Assign a value
let y = 1;        // Declare and initialize
const z = "hi";   // Declare a constant
```

# Context & Application

Variables are used throughout all JavaScript programs to store and manipulate values. Choosing between `let`, `const`, and `var` is one of the first decisions a JavaScript programmer makes.

# Examples

From the source text (p. 22):
```javascript
let x;                    // Declare a variable named x.
x = 0;                    // Now the variable x has the value 0
x = 1;                    // Numbers.
x = 0.01;                 // Numbers can be integers or reals.
x = "hello world";        // Strings of text in quotation marks.
x = true;                 // A Boolean value.
x = null;                 // Null is a special value that means "no value."
x = undefined;            // Undefined is another special value like null.
```

# Relationships

## Builds Upon
- **javascript-language-overview** — Variables are a core language feature

## Enables
- **let-and-const-declarations** — Detailed treatment of modern variable declaration
- **var-declarations** — Detailed treatment of legacy variable declaration
- **destructuring-assignment** — Advanced variable assignment syntax

## Related
- **type-system-overview** — Variables are untyped but hold typed values

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming JavaScript variables have fixed types like in Java or C.
  **Correction**: JavaScript variables are untyped — "it is perfectly legal (but generally poor programming style) in JavaScript to assign a number to a variable and then later assign a string to that variable" (p. 73).

# Common Confusions

- **Confusion**: `let` and `var` are interchangeable.
  **Clarification**: They have significantly different scoping rules; `let` is block-scoped while `var` is function-scoped.

# Source Reference

Chapter 1: Introduction to JavaScript, Section 1.3, page 22. Also Chapter 3, Section 3.10, page 70.

# Verification Notes

- Definition source: Direct quotes from pp. 22, 40, 73
- Confidence rationale: High — introduced clearly in Ch 1, detailed in Ch 3
- Uncertainties: None
- Cross-reference status: Verified across Ch 1 and Ch 3
