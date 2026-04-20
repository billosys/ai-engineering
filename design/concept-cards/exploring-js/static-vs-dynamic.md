---
# === CORE IDENTIFICATION ===
concept: Static vs. Dynamic
slug: static-vs-dynamic

# === CLASSIFICATION ===
category: variables-scope
subcategory: terminology
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.6 Terminology: static vs. dynamic"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - lexical vs runtime
  - compile time vs runtime

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - variable-scope
  - closures
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

In programming languages, *static* means related to source code and determinable without execution; *dynamic* means related to runtime behavior. Variable scopes are static; function calls are dynamic.

# Core Definition

"*Static* means that something is related to source code and can be determined without executing code. *Dynamic* means at runtime." (Ch. 13, &sect;13.6). Variable scopes are static (lexical): "its scope is fixed and doesn't change at runtime." Function calls are dynamic: whether a call happens depends on runtime conditions. "Variable scopes form a static tree (via static nesting)." "Function calls form a dynamic tree (via dynamic calls)."

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Static = determined from source code, without execution
2. Dynamic = determined at runtime
3. Scopes are static (also called lexical)
4. Function calls are dynamic
5. Static tree of scopes vs. dynamic tree of calls

# Construction / Recognition

```js
function f() {
  const x = 3; // x is statically (lexically) scoped
}

function g(x) {}
function h(y) {
  if (Math.random()) g(y); // dynamic: call depends on runtime
}
```

# Context & Application

The static/dynamic distinction is foundational for understanding closures (static scoping), hoisting (static property of declarations), and call stacks (dynamic).

# Examples

From the source text (Ch. 13, &sect;13.6.1-13.6.2):
```js
// Static: scope of x is fixed
function f() {
  const x = 3;
}

// Dynamic: whether g(y) is called depends on runtime
function h(y) {
  if (Math.random()) g(y);
}
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **closures** -- closures implement static scoping
- **variable-scope** -- scopes are a static phenomenon

## Related
- No additional

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Thinking variable scope changes at runtime.
  **Correction**: Scope is static/lexical; it is fixed by the code structure.

# Common Confusions

- **Confusion**: Confusing static scope with static typing.
  **Clarification**: "Static" in "static scope" means determined by code structure. "Static typing" means type checking at compile time. They use "static" differently.

# Source Reference

Chapter 13: Variables and assignment, Section 13.6, lines 290-334.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definitions with examples of each
- Cross-reference status: verified
