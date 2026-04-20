---
# === CORE IDENTIFICATION ===
concept: let and const Declarations
slug: let-and-const-declarations

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
pdf_page: 70
section: "3.10.1 Declarations with let and const"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - block-scoped variables
  - ES6 variable declaration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variables-overview
  - ecmascript-versioning
extends:
  - variables-overview
related:
  - strict-mode
contrasts_with:
  - var-declarations

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do `let`/`const` relate to `var` in terms of scoping?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

`let` declares block-scoped mutable variables and `const` declares block-scoped immutable bindings (the variable cannot be reassigned), both introduced in ES6 as replacements for the function-scoped `var`.

# Core Definition

"In modern JavaScript (ES6 and later), variables are declared with the let keyword." "To declare a constant instead of a variable, use const instead of let. const works just like let except that you must initialize the constant when you declare it" and "constants cannot have their values changed, and any attempt to do so causes a TypeError." Variables declared with `let` and `const` are "block scoped. This means that they are only defined within the block of code in which the let or const statement appears." (pp. 70-72)

# Prerequisites

- **variables-overview** — Must understand variables conceptually
- **ecmascript-versioning** — let/const are ES6 features

# Key Properties

1. `let`: declares a mutable variable; value can be reassigned
2. `const`: declares an immutable binding; must be initialized; reassignment throws TypeError
3. Both are block-scoped (scoped to enclosing `{}`)
4. Cannot be used before declaration (temporal dead zone)
5. Cannot be re-declared in the same scope (syntax error)
6. Can shadow variables in outer scopes
7. Global `let`/`const` are NOT properties of the global object
8. `const` in for/of and for/in loops: value is constant per iteration
9. Variables are untyped — can hold any value type
10. `let` without initializer has value `undefined`

# Construction / Recognition

```javascript
let i;                           // Declare variable, value is undefined
let message = "hello";           // Declare and initialize
let i = 0, j = 0, k = 0;        // Multiple declarations
let x = 2, y = x*x;             // Initializers can reference prior declarations

const H0 = 74;                   // Must initialize
const C = 299792.458;
// const Z;                      // SyntaxError: missing initializer

for (let i = 0; i < 10; i++) ... // Block-scoped to loop
for (const datum of data) ...     // const per iteration
```

# Context & Application

`let` and `const` are the standard way to declare variables in modern JavaScript. The convention debate: some use `const` only for truly unchanging values; others use `const` by default and switch to `let` only when reassignment is needed.

# Examples

From the source text (pp. 70-72):
```javascript
let message = "hello";
let i = 0, j = 0, k = 0;
let x = 2, y = x*x;             // Initializers can use previously declared variables

const H0 = 74;                   // Hubble constant (km/s/Mpc)
const C = 299792.458;            // Speed of light in a vacuum (km/s)
const AU = 1.496E8;              // Astronomical Unit: distance to the sun (km)

// Block scope
const x = 1;
if (x === 1) {
    let x = 2;                   // Different x inside this block
    console.log(x);              // Prints 2
}
console.log(x);                  // Prints 1
// let x = 3;                    // ERROR! Syntax error trying to re-declare x
```

Loop variables (p. 72):
```javascript
for(let i = 0, len = data.length; i < len; i++) console.log(data[i]);
for(let datum of data) console.log(datum);
for(const datum of data) console.log(datum);  // const per iteration
```

# Relationships

## Builds Upon
- **variables-overview** — let/const are the modern variable declaration keywords

## Enables
- **destructuring-assignment** — Works with let and const declarations
- Block-scoped closures (one of the main motivations for let)

## Related
- **strict-mode** — let/const work consistently in strict mode

## Contrasts With
- **var-declarations** — var is function-scoped, hoisted, and allows redeclaration

# Common Errors

- **Error**: Expecting `const` to make objects immutable.
  **Correction**: `const` prevents reassignment of the binding, but the object's properties can still be changed.

- **Error**: Using `let` before its declaration.
  **Correction**: Unlike `var`, `let` has a temporal dead zone — using it before the `let` statement causes a ReferenceError.

# Common Confusions

- **Confusion**: `let` and `var` behave identically.
  **Clarification**: `let` is block-scoped; `var` is function-scoped. `let` cannot be re-declared; `var` can. `let` is not hoisted the same way as `var`.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.10.1, pages 70-73.

# Verification Notes

- Definition source: Direct quotes from pp. 70-72
- Confidence rationale: High — thoroughly explained
- Uncertainties: None
- Cross-reference status: Verified
