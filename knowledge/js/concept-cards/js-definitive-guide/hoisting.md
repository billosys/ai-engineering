---
# === CORE IDENTIFICATION ===
concept: Hoisting
slug: hoisting

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: variables
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 74
section: "3.10.2 Variable Declarations with var"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - variable hoisting
  - declaration hoisting

# === TYPED RELATIONSHIPS ===
prerequisites:
  - var-declarations
extends: []
related:
  - let-and-const-declarations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is hoisting?"
  - "How do `let`/`const` relate to `var` in terms of scoping?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

Hoisting is the behavior where `var` declarations are "lifted" to the top of their enclosing function, so the variable exists (with value `undefined`) from the start of the function, even before the line where it is declared.

# Core Definition

"One of the most unusual features of var declarations is known as hoisting. When a variable is declared with var, the declaration is lifted up (or 'hoisted') to the top of the enclosing function. The initialization of the variable remains where you wrote it, but the definition of the variable moves to the top of the function. So variables declared with var can be used, without error, anywhere in the enclosing function. If the initialization code has not run yet, then the value of the variable may be undefined, but you won't get an error if you use the variable before it is initialized." (p. 74)

# Prerequisites

- **var-declarations** — Hoisting is a specific behavior of var

# Key Properties

1. Only the declaration is hoisted, not the initialization
2. Using a hoisted variable before initialization yields `undefined`
3. Hoisted to the top of the enclosing function (not block)
4. `let` and `const` are NOT hoisted in the same way — they have a temporal dead zone
5. Using a `let`/`const` variable before declaration causes ReferenceError
6. Hoisting is "one of the important misfeatures that let corrects" (p. 74)

# Construction / Recognition

```javascript
// What you write:
function example() {
    console.log(x);    // undefined (not ReferenceError)
    var x = 10;
    console.log(x);    // 10
}

// What JavaScript sees:
function example() {
    var x;              // Declaration hoisted to top
    console.log(x);    // undefined
    x = 10;            // Initialization stays here
    console.log(x);    // 10
}
```

# Context & Application

Hoisting is one of the most common sources of bugs in pre-ES6 JavaScript. It allows variables to be used before they appear to be declared, which can lead to subtle errors where variables unexpectedly have the value `undefined`. This behavior was one of the key motivations for introducing `let` and `const` in ES6.

# Examples

From the source text (p. 74):

"When a variable is declared with var, the declaration is lifted up (or 'hoisted') to the top of the enclosing function. The initialization of the variable remains where you wrote it."

```javascript
// This is a source of bugs:
function f() {
    console.log(x);  // undefined, not an error
    var x = 5;
}

// Versus let, which corrects this:
function g() {
    console.log(y);  // ReferenceError!
    let y = 5;
}
```

# Relationships

## Builds Upon
- **var-declarations** — Hoisting is a property of var declarations

## Enables
- Understanding legacy code behavior and bugs

## Related
- **let-and-const-declarations** — let corrects hoisting by introducing temporal dead zone

## Contrasts With
- Temporal dead zone behavior of let/const — accessing before declaration causes ReferenceError

# Common Errors

- **Error**: Assuming a variable is not yet defined because its `var` declaration appears later in the code.
  **Correction**: Due to hoisting, the variable exists from the start of the function with value `undefined`.

# Common Confusions

- **Confusion**: `let` and `const` are also hoisted.
  **Clarification**: While technically `let`/`const` declarations are processed early, they enter a "temporal dead zone" where accessing them before the declaration throws a ReferenceError. This is effectively "not hoisted" from the programmer's perspective.

- **Confusion**: Hoisting moves the entire `var x = 5;` statement to the top.
  **Clarification**: Only the declaration (`var x`) is hoisted. The initialization (`x = 5`) stays in its original position.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.10.2, page 74.

# Verification Notes

- Definition source: Direct quote from p. 74
- Confidence rationale: High — clearly defined in the source
- Uncertainties: None
- Cross-reference status: Verified
