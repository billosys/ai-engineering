---
# === CORE IDENTIFICATION ===
concept: Block Scope
slug: block-scope

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
pdf_page: 71
section: "3.10.1 Declarations with let and const"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - lexical scope
  - block-level scope

# === TYPED RELATIONSHIPS ===
prerequisites:
  - let-and-const-declarations
extends: []
related:
  - var-declarations
  - hoisting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do `let`/`const` relate to `var` in terms of scoping?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

Block scope means that variables declared with `let` and `const` are only accessible within the enclosing pair of curly braces (`{}`), including function bodies, if/else blocks, loops, and other compound statements.

# Core Definition

"The scope of a variable is the region of your program source code in which it is defined. Variables and constants declared with let and const are block scoped. This means that they are only defined within the block of code in which the let or const statement appears." "If a variable or constant is declared within a set of curly braces, then those curly braces delimit the region of code in which the variable or constant is defined." Variables in for/for-in/for-of loops "have the loop body as their scope, even though they technically appear outside of the curly braces." (pp. 71-72)

# Prerequisites

- **let-and-const-declarations** — Block scope applies to let and const

# Key Properties

1. Defined by enclosing curly braces (`{}`)
2. Applies to let, const declarations
3. Does NOT apply to var (which is function-scoped)
4. Includes function bodies, if/else, while, for, and explicit blocks
5. Loop variables declared in for/for-in/for-of have the loop body as scope
6. Top-level declarations have global scope (file scope in modules, document scope in scripts)
7. Nested scopes can shadow outer variables with the same name
8. It is a syntax error to re-declare a variable in the same scope

# Construction / Recognition

```javascript
const x = 1;
if (x === 1) {
    let x = 2;              // Different x, scoped to this block
    console.log(x);         // 2
}
console.log(x);             // 1: back in outer scope
// let x = 3;               // ERROR! Can't re-declare in same scope

for (let i = 0; i < 10; i++) {
    // i is scoped to this loop body
}
// i is not defined here
```

# Context & Application

Block scoping is the standard in modern JavaScript and is one of the main reasons to prefer `let`/`const` over `var`. It is essential for understanding closures, which capture variables from their enclosing scope.

# Examples

From the source text (pp. 71-72):
```javascript
const x = 1;                // Global constant
if (x === 1) {
    let x = 2;              // Inside a block x can refer to a different value
    console.log(x);         // Prints 2
}
console.log(x);             // Prints 1: we're back in the global scope now
let x = 3;                  // ERROR! Syntax error trying to re-declare x
```

Loop scope:
```javascript
for(let i = 0, len = data.length; i < len; i++) console.log(data[i]);
for(let datum of data) console.log(datum);
for(let property in object) console.log(property);
```

# Relationships

## Builds Upon
- **let-and-const-declarations** — These keywords create block-scoped variables

## Enables
- Closures with correct per-iteration binding in loops
- Predictable variable lifetime

## Related
- **var-declarations** — var uses function scope, not block scope
- **hoisting** — let/const have temporal dead zone; var is hoisted past block boundaries

## Contrasts With
- Function scope (var) — var ignores block boundaries

# Common Errors

- **Error**: Expecting a `var` declared in a block to be scoped to that block.
  **Correction**: `var` is function-scoped, not block-scoped. Only `let` and `const` respect block boundaries.

# Common Confusions

- **Confusion**: Block scope and function scope are the same thing.
  **Clarification**: Block scope is defined by any `{}` pair (if, for, while, etc.). Function scope is only defined by function bodies. `var` uses function scope; `let`/`const` use block scope.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.10.1, pages 71-72.

# Verification Notes

- Definition source: Direct quotes from pp. 71-72
- Confidence rationale: High — clearly explained
- Uncertainties: None
- Cross-reference status: Verified
