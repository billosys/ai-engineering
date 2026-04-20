---
# === CORE IDENTIFICATION ===
concept: Arrow Function
slug: arrow-function

# === CLASSIFICATION ===
category: functions
subcategory: function-forms
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Arrow functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - arrow notation
  - fat arrow function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - expression
extends:
  - function-expression
related:
  - function-expression
  - function-declaration
  - higher-order-function
contrasts_with:
  - function-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes an arrow function from a regular function?"
  - "How do I define and call a function?"
---

# Quick Definition

An arrow function is a concise notation for creating function values using `=>` instead of the `function` keyword, added in 2015 to make small function expressions less verbose.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 289-293 of 03-functions.md): "There's a third notation for functions, which looks very different from the others. Instead of the `function` keyword, it uses an arrow (`=>`) made up of an equal sign and a greater-than character." The arrow comes after the parameter list and is followed by the body. Further (lines 335-338): "Arrow functions were added in 2015, mostly to make it possible to write small function expressions in a less verbose way."

# Prerequisites

- **function-definition**: Arrow functions are a form of function definition.
- **expression**: Arrow functions are expressions that produce function values.

# Key Properties

1. Uses `=>` instead of the `function` keyword.
2. Parameters come **before** the arrow; the body comes **after**.
3. Single parameter: parentheses can be omitted (`x => x * x`).
4. Single-expression body: braces and `return` can be omitted -- the expression is implicitly returned.
5. No parameters: use empty parentheses (`() => { ... }`).
6. Apart from a minor detail (discussed in Ch 6 regarding `this`), they do the same thing as `function` expressions.

# Construction / Recognition

## To Construct/Create:
```javascript
// Full form
const roundTo = (n, step) => {
  let remainder = n % step;
  return n - remainder + (remainder < step / 2 ? 0 : step);
};

// Concise forms
const square1 = (x) => { return x * x; };
const square2 = x => x * x;
const horn = () => { console.log("Toot"); };
```

## To Identify/Recognize:
- The `=>` token between parameters and body.

# Context & Application

Arrow functions are the preferred syntax for small inline functions, especially when passing functions as arguments to higher-order functions like `map`, `filter`, and `reduce`. They are used extensively in Chapter 5.

# Examples

**Example 1** (Ch 3, lines 315-318 of 03-functions.md):
```javascript
const square1 = (x) => { return x * x; };
const square2 = x => x * x;
```

**Example 2** (Ch 3, lines 325-329 of 03-functions.md) -- no parameters:
```javascript
const horn = () => {
  console.log("Toot");
};
```

**Example 3** (Ch 3, summary line 942):
```javascript
// A less verbose function value
let h = a => a % 3;
```

# Relationships

## Builds Upon
- **function-expression** -- Arrow functions are a concise form of function expression.

## Enables
- **higher-order-function** -- Arrow functions make it convenient to pass inline functions.
- **closure** -- Arrow functions can capture outer bindings just like regular functions.

## Related
- **function-declaration** -- Another way to define functions (but not interchangeable).

## Contrasts With
- **function-expression** -- Arrow functions are more concise but differ slightly in `this` binding (discussed in Ch 6).

# Common Errors

- **Error**: Writing `n => {prop: n}` expecting it to return an object.
  **Correction**: The braces are interpreted as a function body. Wrap the object in parentheses: `n => ({prop: n})`.

# Common Confusions

- **Confusion**: Arrow functions are exactly identical to `function` expressions.
  **Clarification**: "Apart from a minor detail, which we'll discuss in Chapter 6, they do the same thing." The minor detail relates to how `this` is handled.

# Source Reference

Chapter 3: Functions, Section "Arrow functions", lines 286-338 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 289-293 and 335-338)
- Confidence rationale: Explicit dedicated section
- Cross-reference status: verified against Ch 4 object braces discussion (lines 302-311 of Ch 4)
