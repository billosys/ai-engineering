---
# === CORE IDENTIFICATION ===
concept: Pass by Identity vs. Pass by Reference
slug: pass-by-identity-vs-pass-by-reference

# === CLASSIFICATION ===
category: types-values
subcategory: objects
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.6.4 Passing by reference vs. passing by identity (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - pass by sharing
  - call by sharing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-passed-by-identity
extends:
  - objects-passed-by-identity
related:
  - primitives-passed-by-value
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

JavaScript uses "pass by identity" (also called "pass by sharing"), where object identities are passed by value. Unlike true "pass by reference" (as in C++), assigning to a parameter in JavaScript only has a local effect and does not change the caller's variable.

# Core Definition

"If a parameter is *passed by reference*, it points to a variable and assigning to the parameter changes the variable." In contrast, "If a parameter is *passed by identity*, the identity of an object (a transparent reference) is passed by value. Assigning to the parameter only has a local effect." (Ch. 14, &sect;14.6.4). The term was suggested by Allen Wirfs-Brock in 2019. Also called "passing by sharing."

# Prerequisites

- **objects-passed-by-identity** -- the base concept this refines

# Key Properties

1. JavaScript: pass by identity (not pass by reference)
2. Object identities are passed by value
3. Assigning to a parameter only has local effect
4. Mutating the object through a parameter IS visible to the caller
5. Reassigning the parameter IS NOT visible to the caller
6. Term coined by Allen Wirfs-Brock (2019)

# Construction / Recognition

```js
function modify(obj) {
  obj.x = 1;    // mutation: visible to caller
  obj = {};     // reassignment: NOT visible to caller
}
const a = {};
modify(a);
// a.x is 1 (mutation visible)
// a is not {} (reassignment not visible)
```

# Context & Application

This distinction matters when discussing JavaScript's evaluation strategy. Calling it "pass by reference" is technically incorrect.

# Examples

From the source text (Ch. 14, &sect;14.6.4), C++ pass-by-reference example for contrast:
```cpp
void swap_ints(int &x, int &y) {
  int temp = x; x = y; y = temp;
}
// In JavaScript, this swap is impossible -- reassignment is local
```

# Relationships

## Builds Upon
- **objects-passed-by-identity** -- refines the passing mechanism

## Enables
- Precise understanding of JavaScript's evaluation strategy

## Related
- **primitives-passed-by-value** -- the other passing mechanism

## Contrasts With
- No direct contrast (but contrasts with C++ pass-by-reference)

# Common Errors

- **Error**: Calling JavaScript's mechanism "pass by reference."
  **Correction**: It's pass by identity (or pass by sharing). True pass-by-reference would allow swapping caller variables.

# Common Confusions

- **Confusion**: Thinking mutating an object through a parameter proves pass-by-reference.
  **Clarification**: Mutation works because both caller and callee share the same object identity. But reassigning the parameter doesn't affect the caller -- proof it's not pass-by-reference.

# Source Reference

Chapter 14: Values, Section 14.6.4, lines 329-363.

# Verification Notes

- Definition source: direct from source with C++ comparison
- Confidence rationale: Explicit distinction with credited terminology
- Cross-reference status: verified
