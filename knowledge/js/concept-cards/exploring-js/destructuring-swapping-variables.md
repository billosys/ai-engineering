---
concept: Swapping Variables with Destructuring
slug: destructuring-swapping-variables
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.6.1 Array-destructuring: swapping variable values"
extraction_confidence: high
aliases: []
prerequisites:
  - array-destructuring
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I use destructuring to extract values from objects and arrays?"
---

# Quick Definition

Array destructuring enables swapping two variables without a temporary variable: `[x, y] = [y, x]`.

# Core Definition

We can use Array-destructuring to swap the values of two variables without needing a temporary variable. The pattern `[x, y] = [y, x]` creates a temporary array `[y, x]` on the right and destructures it into `x` and `y` on the left.

# Prerequisites

- **array-destructuring** -- uses array pattern assignment

# Key Properties

1. No temporary variable needed
2. Concise one-liner
3. Works with any number of variables
4. Uses destructuring assignment (not declaration)

# Construction / Recognition

```js
let x = 'a';
let y = 'b';
[x, y] = [y, x];
// x === 'b', y === 'a'
```

# Context & Application

Useful in sorting algorithms, state toggling, and any situation where two values need to be exchanged.

# Examples

```js
let x = 'a';
let y = 'b';
[x, y] = [y, x];
assert.equal(x, 'b');
assert.equal(y, 'a');
```

(Chapter 40, Section 40.6.1, lines 424-438)

# Relationships

## Builds Upon
- **array-destructuring** -- assignment form

## Enables
- Concise variable swapping

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Using `const` instead of `let` for swap targets.
  **Correction**: Swapping requires assignment, not declaration. Variables must be `let`.

# Common Confusions

- **Confusion**: `[x, y] = [y, x]` creates a persistent array.
  **Clarification**: The temporary array `[y, x]` is created and immediately destructured; it is not stored.

# Source Reference

Chapter 40: Destructuring, Section 40.6.1, lines 424-438.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified
