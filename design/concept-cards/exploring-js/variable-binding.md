---
# === CORE IDENTIFICATION ===
concept: Variable Binding
slug: variable-binding

# === CLASSIFICATION ===
category: variables-scope
subcategory: variable-declarations
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.2.1 const and immutability"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - binding
  - variable association

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - const-declaration
  - let-declaration
  - const-immutability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a variable in JavaScript and how do `let`, `const`, and `var` differ?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

A variable binding is the association between a variable name and a variable value. `const` creates immutable bindings (can't reassign); `let` creates mutable bindings (can reassign).

# Core Definition

"In JavaScript, `const` only means that the *binding* (the association between variable name and variable value) is immutable." (Ch. 13, &sect;13.2.1). A binding connects a name in a scope to a value. The binding's mutability determines whether the variable can be reassigned, distinct from whether the value itself is mutable.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Binding = association between variable name and value
2. Immutable binding (const): name always points to the same value
3. Mutable binding (let): name can be reassigned to a different value
4. Binding mutability is separate from value mutability
5. Understanding bindings is essential for closures

# Construction / Recognition

```js
const x = 8;   // immutable binding: x always refers to 8
let y = 3;     // mutable binding: y can be reassigned
y = 5;         // binding changed to refer to 5
```

# Context & Application

The binding concept is fundamental to understanding variables, closures, and scope. Closures capture bindings (not values), which is why closures can observe changes to mutable variables.

# Examples

From the source text (Ch. 13, &sect;13.2.1):
```js
const obj = { prop: 0 };
// The binding (obj -> the object) is immutable
// But the object itself is mutable:
obj.prop = 1;  // OK
// obj = {};   // TypeError -- can't change the binding
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **const-immutability** -- understanding what const actually freezes
- **closures** -- closures capture bindings

## Related
- **const-declaration** -- creates immutable bindings
- **let-declaration** -- creates mutable bindings

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Confusing binding immutability with value immutability.
  **Correction**: `const` freezes the binding (the variable name's target), not the value.

# Common Confusions

- **Confusion**: Thinking "immutable variable" means "immutable value."
  **Clarification**: An immutable variable means the binding cannot be changed; the value pointed to may still be mutable.

# Source Reference

Chapter 13: Variables and assignment, Section 13.2.1, lines 117-139.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicitly defined as part of const explanation
- Cross-reference status: verified
