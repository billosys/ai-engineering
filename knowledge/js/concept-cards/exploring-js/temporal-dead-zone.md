---
# === CORE IDENTIFICATION ===
concept: Temporal Dead Zone
slug: temporal-dead-zone

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
section: "13.8.1 const and let: temporal dead zone"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - TDZ

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable-scope
  - let-declaration
  - const-declaration
extends: []
related:
  - var-declaration
  - early-activation
contrasts_with:
  - hoisting

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
  - "How do I declare and use variables with proper scoping?"
---

# Quick Definition

The temporal dead zone (TDZ) is the time between entering a variable's scope and reaching its declaration, during which the variable exists but cannot be accessed (throws `ReferenceError`).

# Core Definition

"The time between entering the scope of a variable and executing its declaration is called the *temporal dead zone* (TDZ) of that variable." (Ch. 13, &sect;13.8.1.2). During the TDZ, the variable is "uninitialized": accessing it throws `ReferenceError`. Once the declaration is reached, the variable is set to the initializer value or `undefined`. The TDZ is "truly *temporal* (related to time)" -- a function defined in the TDZ can use the variable if called after the declaration.

# Prerequisites

- **variable-scope** -- TDZ relates to scope entry
- **let-declaration** -- let variables have TDZ
- **const-declaration** -- const variables have TDZ

# Key Properties

1. Applies to `const`, `let`, and `class` declarations
2. Starts when scope is entered; ends at declaration
3. Accessing during TDZ throws `ReferenceError`
4. Temporal, not spatial: a function defined in TDZ can use the variable if called later
5. Prevents `const` from having two different values (undefined then initialized)
6. `let` uses the same approach as `const` for consistency

# Construction / Recognition

```js
if (true) { // TDZ for `tmp` starts
  // `tmp` is uninitialized:
  // assert.throws(() => (tmp = 'abc'), ReferenceError);

  let tmp; // TDZ ends
  assert.equal(tmp, undefined);
}
```

# Context & Application

TDZ prevents using variables before they are properly initialized, catching bugs early. It's especially important when refactoring code or when declarations are not at the top of their scope.

# Examples

From the source text (Ch. 13, &sect;13.8.1.2):
```js
if (true) { // entering scope of `tmp`, TDZ starts
  assert.throws(() => (tmp = 'abc'), ReferenceError);
  assert.throws(() => console.log(tmp), ReferenceError);

  let tmp; // TDZ ends
  assert.equal(tmp, undefined);
}
```

Temporal nature:
```js
if (true) { // TDZ for myVar starts
  const func = () => {
    console.log(myVar); // defined in TDZ, but called later
  };

  let myVar = 3; // TDZ ends
  func(); // OK, called outside TDZ
}
```

# Relationships

## Builds Upon
- **variable-scope** -- TDZ is a scope-entry phenomenon
- **let-declaration** -- subject to TDZ
- **const-declaration** -- subject to TDZ

## Enables
- Safe variable initialization patterns

## Related
- **early-activation** -- function declarations avoid TDZ via early activation

## Contrasts With
- **hoisting** -- var is partially hoisted (initialized to undefined), not subject to TDZ

# Common Errors

- **Error**: Accessing a `let`/`const` variable before its declaration.
  **Correction**: Move the declaration before the access, or restructure code.

# Common Confusions

- **Confusion**: Thinking TDZ means the variable doesn't exist yet.
  **Clarification**: The variable exists (is in scope) but is *uninitialized*. Accessing an uninitialized variable throws `ReferenceError`.

# Source Reference

Chapter 13: Variables and assignment, Section 13.8.1, lines 805-884.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed with two code examples showing spatial and temporal aspects
- Cross-reference status: verified
