---
# === CORE IDENTIFICATION ===
concept: Closure Use Cases
slug: closure-use-cases

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
section: "13.9.4 Use cases for closures"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - closures
extends:
  - closures
related:
  - arrow-function-expressions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

Closures have three main use cases: providing context data for callbacks (static scoping), storing persistent state across function calls, and providing private data for objects.

# Core Definition

"What are closures good for? For starters, they are simply an implementation of static scoping. As such, they provide context data for callbacks. They can also be used by functions to store state that persists across function calls. And they can provide private data for objects." (Ch. 13, &sect;13.9.4).

# Prerequisites

- **closures** -- must understand what closures are

# Key Properties

1. Context data for callbacks (static scoping implementation)
2. Persistent state across function calls (factory pattern)
3. Private data for objects (encapsulation)

# Construction / Recognition

Callback context:
```js
const factor = 2;
[1, 2, 3].map(x => x * factor); // factor is a free variable
```

State persistence:
```js
function createInc(startValue) {
  return (step) => { startValue += step; return startValue; };
}
```

# Context & Application

These three use cases cover the majority of closure usage in practical JavaScript programming.

# Examples

From the source text (Ch. 13, &sect;13.9.3-13.9.4):

State persistence with multiple storage slots:
```js
function createInc(startValue) {
  let index = -1;
  return (step) => {
    startValue += step;
    index++;
    return [index, startValue];
  };
}
const inc = createInc(5);
assert.deepEqual(inc(2), [0, 7]);
assert.deepEqual(inc(2), [1, 9]);
assert.deepEqual(inc(2), [2, 11]);
```

# Relationships

## Builds Upon
- **closures** -- these are practical applications of closures

## Enables
- Factory patterns
- Module patterns
- Callback-based APIs

## Related
- **arrow-function-expressions** -- commonly used to create closures

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Creating closures in loops with `var` and expecting each to capture a different value.
  **Correction**: Use `let` (which creates a fresh binding per iteration) instead of `var`.

# Common Confusions

- **Confusion**: Thinking closures are a special pattern you opt into.
  **Clarification**: Every function is a closure. The "use cases" describe when the closure's scope capture is practically useful.

# Source Reference

Chapter 13: Variables and assignment, Section 13.9.4, lines 1174-1188.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Three use cases explicitly listed
- Cross-reference status: verified
