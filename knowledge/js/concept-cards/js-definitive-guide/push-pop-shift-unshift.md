---
# === CORE IDENTIFICATION ===
concept: push(), pop(), shift(), and unshift()
slug: push-pop-shift-unshift

# === CLASSIFICATION ===
category: arrays
subcategory: array methods
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 188
section: "7.8.4 Stacks and Queues with push(), pop(), shift(), and unshift()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "stack and queue methods"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - array-length
extends: []
related:
  - splice-method
  - spread-operator-in-arrays
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add and remove elements from the beginning or end of an array?"
---

# Quick Definition

`push()` and `pop()` add/remove elements at the end of an array (stack behavior); `unshift()` and `shift()` add/remove elements at the beginning (enabling queue behavior with `push()`).

# Core Definition

"The push() and pop() methods allow you to work with arrays as if they were stacks." push() appends elements to the end and returns the new length; pop() removes and returns the last element. "The unshift() and shift() methods behave much like push() and pop(), except that they insert and remove elements from the beginning of an array." All four methods modify the array in place. (Flanagan, p. 188-189)

# Prerequisites

- **array-fundamentals** — Must understand array structure
- **array-length** — These methods modify the length property

# Key Properties

1. All four methods mutate the array in place
2. `push()` returns new length; `pop()` returns removed element
3. `unshift()` returns new length; `shift()` returns removed element
4. `push()`+`pop()` = stack (LIFO); `push()`+`shift()` = queue (FIFO)
5. `unshift()` with multiple args inserts all at once (preserving argument order)
6. `push()` does not flatten array arguments (use `push(...values)` for that)

# Construction / Recognition

```javascript
let stack = [];
stack.push(1,2);    // stack == [1,2]; returns 2
stack.pop();        // stack == [1]; returns 2

let q = [];
q.push(1,2);        // q == [1,2]
q.shift();           // q == [2]; returns 1
```

# Context & Application

Essential for implementing stack and queue data structures. Among the most commonly used array methods.

# Examples

```javascript
let stack = [];
stack.push(1,2);     // stack == [1,2];
stack.pop();         // stack == [1]; returns 2
stack.push([4,5]);   // stack == [1,[4,5]]  (push does not flatten)
stack.pop()          // stack == [1]; returns [4,5]

// unshift inserts all at once, preserving order:
let a = [];
a.unshift(1);        // a == [1]
a.unshift(2);        // a == [2, 1]
a = [];
a.unshift(1,2);      // a == [1, 2]  (different from inserting one at a time!)
```
(Flanagan, p. 188-189)

# Relationships

## Builds Upon
- **array-fundamentals** — Operates on arrays
- **array-length** — Modifies the length property

## Enables
- Stack and queue implementations
- Dynamic array building

## Related
- **splice-method** — General-purpose insertion/removal
- **spread-operator-in-arrays** — `push(...values)` to flatten

## Contrasts With
- None specific (these methods complement each other)

# Common Errors

- **Error**: Expecting `unshift(1,2)` to produce the same result as `unshift(1); unshift(2)`.
  **Correction**: Multiple arguments to `unshift()` are inserted all at once, so the order differs from inserting one at a time.

# Common Confusions

- **Confusion**: `push()` flattens array arguments like `concat()`.
  **Clarification**: `push([4,5])` adds the array as a single element. Use `push(...values)` to flatten.

# Source Reference

Chapter 7: Arrays, Section 7.8.4, pages 188-189.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with clear examples
- Uncertainties: None
- Cross-reference status: Verified
