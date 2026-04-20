---
concept: Destructuring Locations
slug: destructuring-locations
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.3 Where can we destructure?"
extraction_confidence: high
aliases: []
prerequisites:
  - destructuring
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I use destructuring to extract values from objects and arrays?"
---

# Quick Definition

Destructuring patterns can appear in three "data sink" locations: variable declarations (`const`/`let`), assignments, and function parameter definitions (including for-of loop variables).

# Core Definition

Destructuring patterns can be used at "data sink locations": variable declarations (`const [a] = ['x']`), assignments (`[b] = ['z']`), and parameter definitions (`const f = ([x]) => x`). Variable declarations include `const` and `let` in for-of loops.

# Prerequisites

- **destructuring** -- basic concept

# Key Properties

1. Variable declarations: `const [a] = ...` or `let {b} = ...`
2. Assignments: `[a] = ...` or `({b} = ...)`
3. Parameter definitions: `function f([a], {b}) { }`
4. For-of loop variables: `for (const [i, e] of arr.entries())`

# Construction / Recognition

```js
// Declaration
const [a] = ['x'];
let {b} = {b: 'y'};

// Assignment
let c;
[c] = ['z'];

// Parameter
const f = ([x]) => x;
f(['a']); // 'a'

// For-of
for (const [index, elem] of arr.entries()) { }
```

# Context & Application

Knowing the three locations prevents syntactic errors, especially the object destructuring assignment pitfall with curly braces.

# Examples

```js
const arr = ['a', 'b'];
for (const [index, element] of arr.entries()) {
  console.log(index, element);
}
// 0 a
// 1 b
```

(Chapter 40, Section 40.3, lines 158-210)

# Relationships

## Builds Upon
- **destructuring** -- where to apply it

## Enables
- Correct destructuring usage in all contexts

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Starting a statement with `{prop} = value` (parsed as block).
  **Correction**: Wrap in parentheses: `({prop} = value)`.

# Common Confusions

- **Confusion**: Destructuring only works with `const`.
  **Clarification**: Works with `const`, `let`, assignments, and parameters.

# Source Reference

Chapter 40: Destructuring, Section 40.3, lines 158-210.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly enumerated
- Cross-reference status: verified
