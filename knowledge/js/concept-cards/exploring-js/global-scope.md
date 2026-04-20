---
# === CORE IDENTIFICATION ===
concept: Global Scope
slug: global-scope

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
section: "13.7 The scopes of JavaScript's global variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - global variables
  - top-level scope

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable-scope
extends:
  - variable-scope
related:
  - global-object
  - let-declaration
  - global-object
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare and use variables with proper scoping?"
---

# Quick Definition

The global scope is JavaScript's outermost scope (the root of the scope tree), containing two kinds of global variables: declarative variables (created with `const`/`let`/`class`) and object variables (created with `var`/`function`, stored on the global object).

# Core Definition

"The root is also called the *global scope*." (Ch. 13, &sect;13.7). In browsers, the global scope is at the top level of scripts. Global variables come in two kinds: *global declarative variables* (created via `const`, `let`, and class declarations at script top level) and *global object variables* (created via `var` and function declarations, stored as properties of the global object). Module scopes are direct children of the global scope but not themselves global.

# Prerequisites

- **variable-scope** -- global scope is the outermost scope

# Key Properties

1. Outermost scope, root of the scope tree
2. Two kinds: declarative variables and object variables
3. Declarative variables: `const`, `let`, `class` -- not on global object
4. Object variables: `var`, `function` -- stored as properties of global object
5. Module scopes are children of global scope, not global themselves
6. All scripts share the same global scope

# Construction / Recognition

```html
<script>
  const declarativeVariable = 'd';  // global declarative
  var objectVariable = 'o';          // global object variable
</script>
<script>
  console.log(declarativeVariable);   // 'd' (accessible)
  console.log(globalThis.declarativeVariable);  // undefined (not on global object)
  console.log(globalThis.objectVariable);       // 'o' (on global object)
</script>
```

# Context & Application

Understanding global scope is important for avoiding global namespace pollution and understanding how scripts share state.

# Examples

From the source text (Ch. 13, &sect;13.7):
```html
<script>
  const declarativeVariable = 'd';
  var objectVariable = 'o';
</script>
<script>
  console.log(declarativeVariable); // 'd'
  console.log(objectVariable); // 'o'
  console.log(globalThis.declarativeVariable); // undefined
  console.log(globalThis.objectVariable); // 'o'
</script>
```

# Relationships

## Builds Upon
- **variable-scope** -- global scope is the outermost scope

## Enables
- **global-object** -- the object that stores global object variables

## Related
- **global-declarative-variables** -- one type of global variable
- **global-object-variables** -- other type of global variable

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Assuming module-level variables are global.
  **Correction**: Each module has its own scope; module variables are not global.

# Common Confusions

- **Confusion**: Thinking `const` in global scope creates a property on `window`/`globalThis`.
  **Clarification**: Only `var` and `function` declarations create global object properties. `const`/`let`/`class` create declarative variables.

# Source Reference

Chapter 13: Variables and assignment, Section 13.7, lines 336-404.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed with HTML example and diagram reference
- Cross-reference status: verified
