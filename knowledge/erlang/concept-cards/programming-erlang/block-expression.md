---
# === CORE IDENTIFICATION ===
concept: Block Expression
slug: block-expression

# === CLASSIFICATION ===
category: core-idioms
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Block Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "begin ... end"
  - begin-end block

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression-sequence
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a block expression?"
  - "When do I need a begin...end block?"
---

# Quick Definition

A block expression, written `begin ... end`, groups a sequence of expressions into a single expression; its value is the value of the last expression in the block.

# Core Definition

"Block expressions are used when the Erlang syntax requires a single expression, but we want to have a sequence of expressions at this point in the code" ("The Rest of Sequential Erlang", *Block Expressions*). For example, in a list comprehension `[E || ...]` the syntax requires `E` to be a single expression, but `begin Expr1, ..., ExprN end` lets several things happen there. "You can use block expressions to group a sequence of expressions, similar to a clause body. The value of a `begin ... end` block is the value of the last expression in the block."

# Prerequisites

- **Expression sequence** — A block wraps an expression sequence, so that concept comes first.

# Key Properties

1. Written `begin Expr1, ..., ExprN end`.
2. Turns a sequence of expressions into a single expression.
3. Its value is the value of the last expression in the block.
4. Behaves like a clause body.
5. Used wherever the grammar demands a single expression but several are wanted.

# Construction / Recognition

## To Construct/Create:
1. Wrap a comma-separated expression sequence in `begin` and `end`.

## To Identify/Recognize:
1. A `begin ... end` form appears where exactly one expression is grammatically allowed.

# Context & Application

- **Typical contexts**: inside a list comprehension's result expression, or anywhere a single expression is required.
- **Common applications**: doing several steps in the `E` position of `[E || ...]`.
- **Historical/stylistic notes**: analogous to a clause body — a grouping device, not a control-flow construct.

# Examples

**Example 1** (*Block Expressions*): the general form:

```erlang
begin
    Expr1,
    ...,
    ExprN
end
```

The value of the whole block is the value of `ExprN`.

# Relationships

## Builds Upon
- **Expression sequence** — A block is a parenthesized expression sequence.

## Enables
- This concept does not have downstream cards in scope.

## Related
- No directly related concept in scope.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Expecting the block's value to be the first or some middle expression.
  **Correction**: The value of a `begin ... end` block is always the value of its last expression.

# Common Confusions

- **Confusion**: Thinking `begin ... end` is a control-flow construct like `if` or `case`.
  **Clarification**: It is purely a grouping device that makes a sequence usable where one expression is required.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Block Expressions".

# Verification Notes

- Definition source: Direct quotation from *Block Expressions*.
- Confidence rationale: HIGH — the source explicitly defines block expressions and their value.
- Uncertainties: None.
- Cross-reference status: Slug `expression-sequence` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
