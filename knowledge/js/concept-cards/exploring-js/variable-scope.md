---
# === CORE IDENTIFICATION ===
concept: Variable Scope
slug: variable-scope

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
section: "13.4 The scope of a variable"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - scope
  - lexical scope

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - block-scoping
  - shadowing
  - static-vs-dynamic
  - closures
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare and use variables with proper scoping?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

The scope of a variable is the region of a program where it can be accessed. Scopes nest hierarchically: a variable is accessible in its direct scope and all inner (nested) scopes.

# Core Definition

"The *scope* of a variable is the region of a program where it can be accessed." (Ch. 13, &sect;13.4). JavaScript has three scope-related concepts: *direct scope* (where the variable is declared), *inner scopes* (scopes nested within the direct scope), and *outer scopes* (scopes containing the current scope). "Each variable is accessible in its direct scope and all scopes nested within that scope." Variables declared via `const` and `let` are *block-scoped*.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Scope = region where a variable can be accessed
2. Scopes nest hierarchically (tree structure)
3. Variables accessible in direct scope and all inner scopes
4. `const` and `let` are block-scoped (innermost surrounding block)
5. Scope is a static (lexical) phenomenon
6. Variable scopes form a static tree via nesting

# Construction / Recognition

```js
{ // Scope A. Accessible: x
  const x = 0;
  { // Scope B. Accessible: x, y
    const y = 1;
    { // Scope C. Accessible: x, y, z
      const z = 2;
    }
  }
}
// Outside. Not accessible: x, y, z
```

# Context & Application

Scope determines variable visibility and lifetime. Understanding scope is essential for closures, avoiding name collisions, and writing maintainable code.

# Examples

From the source text (Ch. 13, &sect;13.4):
```js
{ // Scope A
  const x = 0;
  assert.equal(x, 0);
  { // Scope B
    const y = 1;
    assert.equal(x, 0);
    assert.equal(y, 1);
    { // Scope C
      const z = 2;
      assert.equal(x, 0);
      assert.equal(y, 1);
      assert.equal(z, 2);
    }
  }
}
// x is not accessible here:
assert.throws(
  () => console.log(x),
  { name: 'ReferenceError', message: 'x is not defined' }
);
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **block-scoping** -- specific scope type for let/const
- **shadowing** -- variables in inner scopes can shadow outer ones
- **closures** -- functions retain access to their birth scope

## Related
- **static-vs-dynamic** -- scope is a static phenomenon

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Accessing a variable outside its scope.
  **Correction**: Variables are only accessible in their direct scope and nested inner scopes.

# Common Confusions

- **Confusion**: Thinking scope is determined at runtime.
  **Clarification**: Scope is static (lexical) -- determined by code structure, not execution.

# Source Reference

Chapter 13: Variables and assignment, Section 13.4, lines 191-233.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with nested scope example
- Cross-reference status: verified
