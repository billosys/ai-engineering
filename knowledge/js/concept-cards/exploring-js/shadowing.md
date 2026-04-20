---
# === CORE IDENTIFICATION ===
concept: Variable Shadowing
slug: shadowing

# === CLASSIFICATION ===
category: variables-scope
subcategory: scoping
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.4.1 Shadowing variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - variable shadowing
  - name shadowing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable-scope
  - block-scoping
extends: []
related:
  - closures
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare and use variables with proper scoping?"
---

# Quick Definition

Shadowing occurs when an inner scope declares a variable with the same name as an outer scope variable, making the outer variable temporarily inaccessible within the inner scope.

# Core Definition

"Inside the block, the inner `x` is the only accessible variable with that name. The inner `x` is said to *shadow* the outer `x`. Once we leave the block, we can access the old value again." (Ch. 13, &sect;13.4.1). Same-name variables cannot be declared twice in the same scope, but nesting a block allows reuse of the name.

# Prerequisites

- **variable-scope** -- shadowing occurs between nested scopes
- **block-scoping** -- the mechanism that creates the inner scope

# Key Properties

1. Inner variable hides (shadows) the outer variable of the same name
2. Cannot declare the same variable twice at the same level (SyntaxError)
3. After leaving the inner block, the outer variable is accessible again
4. Each scope has its own independent binding for the shadowed name

# Construction / Recognition

```js
const x = 1;
assert.equal(x, 1);
{
  const x = 2;   // shadows outer x
  assert.equal(x, 2);
}
assert.equal(x, 1); // outer x is back
```

# Context & Application

Shadowing is common in nested functions and blocks. While sometimes useful, it can cause confusion. Linters can warn about shadowed variables.

# Examples

From the source text (Ch. 13, &sect;13.4.1):
```js
const x = 1;
assert.equal(x, 1);
{
  const x = 2;
  assert.equal(x, 2);
}
assert.equal(x, 1);
```

Duplicate declaration error:
```js
eval('let x = 1; let x = 2;');
// SyntaxError: Identifier 'x' has already been declared
```

# Relationships

## Builds Upon
- **variable-scope** -- shadowing is a scope interaction
- **block-scoping** -- blocks create the inner scope

## Enables
- Independent variable naming in nested scopes

## Related
- **closures** -- closures interact with shadowed variables

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Accidentally shadowing a variable and losing access to the outer one.
  **Correction**: Use distinct names, or rely on linter warnings for shadowed variables.

# Common Confusions

- **Confusion**: Thinking shadowing modifies the outer variable.
  **Clarification**: Shadowing creates a completely independent variable; the outer one is untouched.

# Source Reference

Chapter 13: Variables and assignment, Section 13.4.1, lines 235-284.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with code demonstration
- Cross-reference status: verified
