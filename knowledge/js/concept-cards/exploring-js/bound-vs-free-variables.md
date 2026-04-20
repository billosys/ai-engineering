---
# === CORE IDENTIFICATION ===
concept: Bound Variables vs. Free Variables
slug: bound-vs-free-variables

# === CLASSIFICATION ===
category: variables-scope
subcategory: closures
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.9.1 Bound variables vs. free variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - local variables vs non-local variables

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable-scope
extends: []
related:
  - closures
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

Bound variables are declared within a scope (parameters and local variables); free variables are declared externally (non-local variables) and their values are provided by closures.

# Core Definition

"Per scope, there is a set of variables that are mentioned. Among these variables we distinguish: *Bound variables* are declared within the scope. They are parameters and local variables. *Free variables* are declared externally. They are also called *non-local variables*." (Ch. 13, &sect;13.9.1).

# Prerequisites

- **variable-scope** -- bound/free distinction is about where variables are declared relative to a scope

# Key Properties

1. Bound variables: parameters + local variables (declared in the scope)
2. Free variables: declared in an enclosing scope (non-local)
3. Closures provide the values for free variables
4. A variable is bound or free relative to a specific scope

# Construction / Recognition

```js
function func(x) {       // x is bound (parameter)
  const y = 123;          // y is bound (local variable)
  console.log(z);         // z is free (declared externally)
}
```

# Context & Application

Understanding bound vs. free variables is the prerequisite for understanding closures. Closures exist to provide values for free variables.

# Examples

From the source text (Ch. 13, &sect;13.9.1):
```js
function func(x) {
  const y = 123;
  console.log(z);
}
```
- `x` and `y` are bound variables
- `z` is a free variable

# Relationships

## Builds Upon
- **variable-scope** -- the scope determines which variables are bound vs. free

## Enables
- **closures** -- closures exist to resolve free variables

## Related
- No additional

## Contrasts With
- No direct contrast (bound and free are complementary)

# Common Errors

- **Error**: Thinking free variables are always global variables.
  **Correction**: Free variables are simply declared in an *enclosing* scope, which may be any outer scope.

# Common Confusions

- **Confusion**: Not understanding that "bound" and "free" are relative to a specific scope.
  **Clarification**: A variable can be bound in one scope and free in a nested scope.

# Source Reference

Chapter 13: Variables and assignment, Section 13.9.1, lines 1069-1093.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with categorized example
- Cross-reference status: verified
