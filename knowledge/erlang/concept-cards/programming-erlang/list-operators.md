---
# === CORE IDENTIFICATION ===
concept: List Addition and Subtraction Operators
slug: list-operators

# === CLASSIFICATION ===
category: data-types
subcategory: lists
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "List Operations ++ and - -"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "++"
  - "--"
  - list append
  - list subtraction

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - operator-precedence
  - pattern-matching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What do the ++ and -- operators do?"
  - "How does list subtraction handle repeated elements?"
  - "Can ++ be used in patterns?"
---

# Quick Definition

`++` and `--` are infix operators for list addition and subtraction: `A ++ B` appends `B` to `A`, and `A -- B` removes the elements of `B` from `A`.

# Core Definition

"`++` and `--` are infix operators for list addition and subtraction" ("The Rest of Sequential Erlang", *List Operations ++ and - -*). "`A ++ B` adds (that is, appends) `A` and `B`. `A -- B` subtracts the list `B` from the list `A`. Subtraction means that every element in `B` is removed from `A`. Note that if some symbol `X` occurs only `K` times in `B`, then only the first `K` occurrences of `X` in `A` will be removed." `++` can also be used in patterns: when matching strings, a pattern like `f("begin" ++ T) -> ...` is legal — the literal-string prefix is expanded into the list `[$b,$e,$g,$i,$n|T]`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `++` appends one list onto another.
2. `--` removes from the left list every element appearing in the right list.
3. If an element occurs `K` times in the right list, only the first `K` occurrences are removed from the left list.
4. `++` can be used in patterns when the left operand is a literal string (or list).
5. A string `++` pattern expands to a `[...|Tail]` cons pattern.
6. Both are right associative.

# Construction / Recognition

## To Construct/Create:
1. Append: `[1,2,3] ++ [4,5,6]`.
2. Subtract: `[a,b,c,1,d,e,1] -- [1,1]`.

## To Identify/Recognize:
1. A literal-string-prefixed `++` pattern in a function head matches a string with that prefix.

# Context & Application

- **Typical contexts**: list concatenation and element removal.
- **Common applications**: prefix matching of strings, e.g. distinguishing `"begin"` from `"end"` prefixes.
- **Historical/stylistic notes**: `++` and `--` are right associative in the operator precedence table.

# Examples

**Example 1** (*List Operations ++ and - -*): append and subtraction with repeats:

```erlang
1> [1,2,3] ++ [4,5,6].
[1,2,3,4,5,6]
2> [a,b,c,1,d,e,1,x,y,1] -- [1].
[a,b,c,d,e,1,x,y,1]
3> [a,b,c,1,d,e,1,x,y,1] -- [1,1].
[a,b,c,d,e,x,y,1]
5> [a,b,c,1,d,e,1,x,y,1] -- [1,1,1,1].
[a,b,c,d,e,x,y]
```

**Example 2** (*List Operations ++ and - -*): `++` in a pattern — `f("begin" ++ T) -> ...` expands to `[$b,$e,$g,$i,$n|T]`.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Operator precedence** — `++` and `--` appear in the precedence table as right-associative operators.
- **Pattern matching** — `++` can appear in patterns to match a list prefix.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Expecting `A -- B` to remove all occurrences of an element appearing fewer times in `B`.
  **Correction**: Only the first `K` occurrences are removed, where `K` is the count of that element in `B`.

# Common Confusions

- **Confusion**: Thinking `--` removes every matching element regardless of multiplicity.
  **Clarification**: Removal is count-limited — an element removed `K` times only if it appears `K` times in the right list.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "List Operations ++ and - -".

# Verification Notes

- Definition source: Direct quotation and adaptation from *List Operations ++ and - -*.
- Confidence rationale: HIGH — the source defines both operators precisely with multiple worked examples.
- Uncertainties: None.
- Cross-reference status: Slug `operator-precedence` extracted in this chapter; `pattern-matching` assumed canonical.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
