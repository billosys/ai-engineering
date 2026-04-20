---
# === CORE IDENTIFICATION ===
concept: Update Operators
slug: update-operators

# === CLASSIFICATION ===
category: fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Program Structure"
chapter_number: 2
pdf_page: null
section: "Updating bindings succinctly"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - compound assignment operators
  - increment/decrement operators

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binding
  - arithmetic-operator
extends: []
related:
  - for-loop
  - while-loop
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a binding (variable)?"
---

# Quick Definition

Update operators (`+=`, `-=`, `*=`, `++`, `--`) provide shorthand for modifying a binding's value based on its current value.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 724-725 of 02-program-structure.md): "JavaScript provides a shortcut for this" (updating a binding based on its previous value). The shortcut `counter += 1` is equivalent to `counter = counter + 1`. "Similar shortcuts work for many other operators, such as `result *= 2` to double `result` or `counter -= 1` to count downward" (lines 732-734). Additionally: "For `counter += 1` and `counter -= 1`, there are even shorter equivalents: `counter++` and `counter--`" (lines 747-749).

# Prerequisites

- **Binding** -- Update operators modify bindings.
- **Arithmetic Operator** -- Update operators combine assignment with arithmetic.

# Key Properties

1. `+=` adds and assigns: `counter += 1` is `counter = counter + 1` (line 728).
2. `-=` subtracts and assigns (line 734).
3. `*=` multiplies and assigns (line 733).
4. `++` increments by 1: `counter++` is `counter += 1` (line 748).
5. `--` decrements by 1: `counter--` is `counter -= 1` (line 749).
6. Commonly used in **loop update** expressions (lines 741-744).

# Construction / Recognition

## To Construct/Create:
1. `counter += 1;` instead of `counter = counter + 1;`.
2. `result *= 2;` instead of `result = result * 2;`.
3. `counter++;` instead of `counter += 1;`.

## To Identify/Recognize:
1. Operators `+=`, `-=`, `*=`, `/=`, `++`, `--`.

# Context & Application

Update operators are used extensively in loops for incrementing counters and accumulators. They make code more concise and are part of idiomatic JavaScript.

# Examples

**Example 1** (Ch 2, lines 741-744): For loop with update operator:
```js
for (let number = 0; number <= 12; number += 2) {
  console.log(number);
}
```

**Example 2** (Ch 2, lines 719-728): Longhand vs. shorthand:
```js
// Longhand:
counter = counter + 1;
// Shorthand:
counter += 1;
```

# Relationships

## Builds Upon
- **Binding** -- Update operators modify bindings.
- **Arithmetic Operator** -- Combined with assignment.

## Enables
- Concise loop update expressions.
- Idiomatic JavaScript patterns.

## Related
- **For Loop** -- Commonly uses `++` or `+=` in the update part.
- **While Loop** -- Often uses update operators in the body.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Confusing `=+` with `+=`.
  **Correction**: `x =+ 1` assigns positive 1 to x (unary plus). `x += 1` adds 1 to x's current value.

# Common Confusions

- **Confusion**: `++` and `+= 1` differ in behavior.
  **Clarification**: For simple statements like `counter++;` and `counter += 1;`, they are equivalent. Differences in prefix vs. postfix `++` are not covered in this chapter.

# Source Reference

Chapter 2: Program Structure, Section "Updating bindings succinctly", lines 712-749 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (paraphrased from source)
- Confidence rationale: Dedicated section with clear examples
- Cross-reference status: verified within chapter
