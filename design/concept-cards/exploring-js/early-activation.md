---
# === CORE IDENTIFICATION ===
concept: Early Activation
slug: early-activation

# === CLASSIFICATION ===
category: variables-scope
subcategory: activation
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.8.2 Function declarations and early activation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - function hoisting

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
  - variable-scope
extends: []
related:
  - temporal-dead-zone
  - hoisting
contrasts_with:
  - temporal-dead-zone

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

Early activation means function declarations are available throughout their scope, even before the declaration appears in the code, because they are executed when entering their scope.

# Core Definition

"A function declaration is always executed when entering its scope, regardless of where it is located within that scope." (Ch. 13, &sect;13.8.2). This allows calling a function before its declaration. Functions declared via `const`/`let` (arrow functions) are NOT early-activated; they are subject to the TDZ. A pitfall: early-activated functions should not access `const`/`let` variables that haven't been initialized yet.

# Prerequisites

- **function-declarations** -- only function declarations are early-activated
- **variable-scope** -- early activation occurs at scope entry

# Key Properties

1. Function declarations are activated when scope is entered
2. Can be called before the declaration in source code
3. Only function declarations (not const/let arrow functions)
4. Pitfall: accessing const/let variables before their initialization
5. In modules, order rarely matters since functions are called after full body execution

# Construction / Recognition

```js
assert.equal(funcDecl(), 123); // OK -- called before declaration
function funcDecl() { return 123; }
```

# Context & Application

Early activation enables writing code where helper functions appear after the main logic, improving readability. However, it can lead to subtle bugs when combined with TDZ variables.

# Examples

From the source text (Ch. 13, &sect;13.8.2):
```js
assert.equal(funcDecl(), 123); // OK
function funcDecl() { return 123; }
```

Not early-activated (arrow function):
```js
assert.throws(
  () => arrowFunc(), // before declaration
  ReferenceError
);
const arrowFunc = () => { return 123 };
```

Pitfall with const:
```js
funcDecl();
const MY_STR = 'abc';
function funcDecl() {
  assert.throws(() => MY_STR, ReferenceError); // MY_STR is in TDZ
}
```

# Relationships

## Builds Upon
- **function-declarations** -- only these are early-activated
- **variable-scope** -- activation happens at scope entry

## Enables
- Flexible function ordering in code

## Related
- **hoisting** -- var's partial early activation

## Contrasts With
- **temporal-dead-zone** -- const/let are not early-activated

# Common Errors

- **Error**: Calling an early-activated function that accesses a const/let before its declaration.
  **Correction**: Ensure the function call occurs after all variables it uses are declared.

# Common Confusions

- **Confusion**: Thinking all functions are early-activated.
  **Clarification**: Only `function` declarations are early-activated. Arrow functions and function expressions assigned to const/let are not.

# Source Reference

Chapter 13: Variables and assignment, Section 13.8.2, lines 886-985.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed with positive, negative, and pitfall examples
- Cross-reference status: verified
