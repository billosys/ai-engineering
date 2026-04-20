---
concept: Spread Into Function Calls
slug: spread-into-function-calls
category: functions
subcategory: parameters
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.6.8 Spreading (`...`) into function calls"
extraction_confidence: high
aliases:
  - "spread arguments"
  - "spread operator in calls"
prerequisites:
  - rest-parameters
extends: []
related:
  - rest-parameters
contrasts_with:
  - rest-parameters
answers_questions:
  - "How do I pass array elements as individual arguments?"
---

# Quick Definition

Spreading (`...`) in a function call expands an iterable into individual arguments.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, placing `...` before an argument in a function call spreads the iterable into individual arguments. The argument must be an iterable object. Spreading and rest parameters use the same `...` syntax but serve opposite purposes: rest collects, spread expands. Introduced in ES6.

# Prerequisites

- Rest parameters (complementary concept)

# Key Properties

1. Introduced in ES6.
2. The spread argument must be an iterable.
3. Can be combined with regular arguments.
4. Opposite of rest parameters: spread expands, rest collects.

# Construction / Recognition

```js
func(...someIterable);
Math.max(...[-1, 5, 11, 3]); // 11
```

# Context & Application

Commonly used with `Math.max()`, `Array.prototype.push()`, and anywhere an array needs to be passed as individual arguments.

# Examples

From the source text (Ch. 27, section 27.6.8.2):

```js
const arr1 = ['a', 'b'];
const arr2 = ['c', 'd'];
arr1.push(...arr2);
assert.deepEqual(arr1, ['a', 'b', 'c', 'd']);
```

# Relationships

## Contrasts With
- **Rest Parameters** -- rest collects arguments into an Array; spread expands an iterable into arguments

# Common Confusions

- **Confusion**: Thinking spread and rest are the same thing.
  **Clarification**: Same syntax (`...`), opposite purposes: rest in function definitions collects; spread in function calls expands.

# Source Reference

Chapter 27: Callable values, Section 27.6.8, lines 1394-1458.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
