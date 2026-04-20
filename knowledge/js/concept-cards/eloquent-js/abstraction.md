---
# === CORE IDENTIFICATION ===
concept: Abstraction
slug: abstraction

# === CLASSIFICATION ===
category: higher-order-programming
subcategory: design-principles
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Higher-Order Functions"
chapter_number: 5
pdf_page: null
section: "Abstraction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - abstractions
  - abstracting

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
extends: []
related:
  - higher-order-function
  - composability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a higher-order function?"
  - "What must I know before understanding higher-order functions?"
---

# Quick Definition

Abstractions are vocabularies that allow us to talk about problems at a higher level without getting sidetracked by uninteresting details, primarily implemented through functions in programming.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 5, lines 88-92 of 05-higher-order-functions.md): "In the context of programming, these kinds of vocabularies are usually called *abstractions*. Abstractions give us the ability to talk about problems at a higher (or more abstract) level, without getting sidetracked by uninteresting details."

# Prerequisites

- **function-definition**: Functions are the primary mechanism for creating abstractions.

# Key Properties

1. Abstractions hide implementation details behind meaningful names.
2. Functions are the primary way to create abstractions in JavaScript.
3. Good abstractions correspond to the vocabulary of the problem being solved.
4. "It is a useful skill, in programming, to notice when you are working at too low a level of abstraction" (line 137).

# Construction / Recognition

## To Construct/Create:
Define functions that express meaningful concepts rather than low-level operations:
```javascript
console.log(sum(range(1, 10)));
// Instead of:
let total = 0, count = 1;
while (count <= 10) { total += count; count += 1; }
```

## To Identify/Recognize:
- Code that expresses "what" rather than "how."
- Named functions that represent domain concepts.

# Context & Application

Abstraction is the organizing principle behind all of Chapter 5. Higher-order functions are a powerful form of abstraction that abstract over actions, not just values.

# Examples

**Example 1** (Ch 5, lines 46-59 of 05-higher-order-functions.md):
Two programs that compute the sum of 1..10:
```javascript
// Low abstraction:
let total = 0, count = 1;
while (count <= 10) { total += count; count += 1; }

// High abstraction:
console.log(sum(range(1, 10)));
```
"The solution is expressed in a vocabulary that corresponds to the problem being solved. Summing a range of numbers isn't about loops and counters. It is about ranges and sums."

**Example 2** (Ch 5, lines 95-126) -- pea soup recipes: the first recipe gives step-by-step instructions; the second uses abstract terms like "soak", "simmer", "chop." The second is shorter and clearer.

# Relationships

## Builds Upon
- **function-definition** -- Functions create abstractions.

## Enables
- **higher-order-function** -- Higher-order functions abstract over actions.
- **composability** -- Abstractions compose to solve complex problems.

## Related
- Better code organization and readability.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Creating abstractions prematurely (over-engineering).
  **Correction**: Abstract when you see repeated patterns or when the abstraction clarifies the code.

# Common Confusions

- **Confusion**: Abstraction always means adding more code.
  **Clarification**: While the definitions of `sum` and `range` add code, the calling code becomes clearer and more likely to be correct.

# Source Reference

Chapter 5: Higher-Order Functions, Section "Abstraction", lines 85-138 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 88-92)
- Confidence rationale: Explicit definition with italicized term "abstractions"
- Cross-reference status: verified within chapter
