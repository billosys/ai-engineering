---
# === CORE IDENTIFICATION ===
concept: List Operations
slug: list-operations

# === CLASSIFICATION ===
category: data-types
subcategory: list-operators
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "List Operations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "++ operator"
  - "-- operator"
  - "list concatenation"
  - "list subtraction"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - list-comprehensions
  - operator-precedence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I concatenate lists in Erlang?"
  - "How do I subtract elements from a list in Erlang?"
  - "What do the ++ and -- operators do?"
---

# Quick Definition

The `++` operator concatenates two lists, and the `--` operator removes the first occurrence of each element in the second list from the first list. Both are right-associative operators.

# Core Definition

The list concatenation operator `++` appends its second argument to its first and returns the resulting list. The list subtraction operator `--` produces a list that is a copy of the first argument, with the following procedure: for each element in the second argument, the first occurrence of this element (if any) is removed (Erlang Reference Manual, "List Operations" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `++` appends the second list to the first list.
2. `--` removes the first occurrence of each element of the second list from the first list.
3. Both operators are right-associative.
4. `--` removes only the *first* occurrence per element in the subtraction list.
5. If an element in the subtraction list does not exist in the first list, it is ignored.

# Construction / Recognition

## To Construct:
1. List concatenation: `List1 ++ List2`.
2. List subtraction: `List1 -- List2`.

## To Recognize:
1. Look for `++` or `--` between two list expressions.

# Context & Application

List concatenation with `++` is commonly used to build lists by appending elements. However, since `++` copies its first argument, repeated concatenation to the front of a list is O(N) per call. The `--` operator is useful for removing known elements from a list. Both operators are valid in guard expressions (as part of constant expressions) and in patterns (as string prefix matching).

# Examples

**Example 1** (List Operations section): List concatenation:

```erlang
1> [1,2,3] ++ [4,5].
[1,2,3,4,5]
```

**Example 2** (List Operations section): List subtraction removes first occurrences:

```erlang
2> [1,2,3,2,1,2] -- [2,1,2].
[3,1,2]
```

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **list-comprehensions** — List comprehensions provide an alternative way to construct lists.

## Related
- **operator-precedence** — `++` and `--` are right-associative and sit between arithmetic and comparison operators in precedence.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Using `++` to prepend a single element (e.g., `[X] ++ List` instead of `[X | List]`).
  **Correction**: Use the cons operator `[X | List]` for prepending a single element, which is O(1).

- **Error**: Expecting `--` to remove all occurrences of an element.
  **Correction**: `--` removes only the first occurrence per element in the subtraction list. To remove all occurrences, use a list comprehension or `lists:filter/2`.

# Common Confusions

- **Confusion**: Thinking `--` performs set difference.
  **Clarification**: `--` removes individual occurrences, not all instances. `[1,1,2] -- [1]` returns `[1,2]`, not `[2]`.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "List Operations" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit definition and examples in source
- Uncertainties: None
- Cross-reference status: Related concepts verified against planned extractions
