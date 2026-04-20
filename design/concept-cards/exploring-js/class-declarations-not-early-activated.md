---
# === CORE IDENTIFICATION ===
concept: Class Declarations Not Early-Activated
slug: class-declarations-not-early-activated

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
section: "13.8.3 Class declarations are not activated early"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - temporal-dead-zone
  - early-activation
extends: []
related:
  - function-declarations
contrasts_with:
  - early-activation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

Unlike function declarations, class declarations are not early-activated: they are subject to the temporal dead zone and cannot be used before their declaration in source code.

# Core Definition

"Even though they are similar to function declarations in some ways, class declarations are not activated early." (Ch. 13, &sect;13.8.3). Using a class before its declaration throws `ReferenceError`. The reason: "The operand of `extends` is an expression" that must be evaluated at the declaration point; early activation would be confusing for expressions like `class MyClass extends identity(Object) {}`.

# Prerequisites

- **temporal-dead-zone** -- class declarations are subject to TDZ
- **early-activation** -- contrasts with function declarations

# Key Properties

1. Class declarations are subject to TDZ
2. Using before declaration throws ReferenceError
3. Reason: `extends` operand is an expression that must be evaluated in place
4. Consistent with `const` and `let` behavior
5. Block-scoped (like const/let)

# Construction / Recognition

```js
assert.throws(() => new MyClass(), ReferenceError);

class MyClass {}

assert.equal(new MyClass() instanceof MyClass, true);
```

# Context & Application

This means classes must be declared before use, unlike function declarations which can be called before their declaration.

# Examples

From the source text (Ch. 13, &sect;13.8.3):
```js
assert.throws(
  () => new MyClass(),
  ReferenceError
);

class MyClass {}

assert.equal(new MyClass() instanceof MyClass, true);
```

Why not early-activated:
```js
const identity = x => x;
class MyClass extends identity(Object) {}
// The extends expression must be evaluated at this point
```

# Relationships

## Builds Upon
- **temporal-dead-zone** -- classes are in TDZ before declaration
- **early-activation** -- classes are NOT early-activated (unlike functions)

## Enables
- Understanding class declaration ordering requirements

## Related
- **function-declarations** -- functions ARE early-activated

## Contrasts With
- **early-activation** -- function declarations have this; class declarations don't

# Common Errors

- **Error**: Trying to instantiate a class before its declaration.
  **Correction**: Move the class declaration before its first use, or use a function declaration pattern.

# Common Confusions

- **Confusion**: Expecting classes to be hoisted like functions.
  **Clarification**: Classes are in the TDZ before their declaration, similar to `let`/`const`.

# Source Reference

Chapter 13: Variables and assignment, Section 13.8.3, lines 987-1022.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with rationale for the design decision
- Cross-reference status: verified
