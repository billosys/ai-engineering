---
# === CORE IDENTIFICATION ===
concept: Expression Sequence
slug: expression-sequence

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
section: "Expressions and Expression Sequences"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - expression
  - sequence of expressions

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - block-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an expression in Erlang?"
  - "What is an expression sequence and what is its value?"
---

# Quick Definition

In Erlang, anything that can be evaluated to produce a value is an expression; an expression sequence is comma-separated expressions whose value is that of the last expression.

# Core Definition

"In Erlang, anything that can be evaluated to produce a value is called an *expression*. This means things such as `catch`, `if`, and `try...catch` are expressions. Things such as record declarations and module attributes cannot be evaluated, so they are not expressions" ("The Rest of Sequential Erlang", *Expressions and Expression Sequences*). "*Expression sequences* are sequences of expressions separated by commas. They are found all over the place immediately following an `->` arrow. The value of the expression sequence `E1, E2, ..., En` is defined to be the value of the last expression in the sequence." This is computed using any bindings created when evaluating earlier expressions; the book notes it "is equivalent to `progn` in LISP."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. An expression is anything that evaluates to a value.
2. `catch`, `if`, and `try...catch` are all expressions.
3. Record declarations and module attributes are not expressions — they cannot be evaluated.
4. An expression sequence is comma-separated expressions.
5. Expression sequences appear immediately after `->` arrows.
6. The value of `E1, ..., En` is the value of `En`, computed with bindings from earlier expressions.

# Construction / Recognition

## To Construct/Create:
1. Write expressions separated by commas: `E1, E2, ..., En`.

## To Identify/Recognize:
1. The code following a `->` arrow (function clause body, `case` clause, etc.) is an expression sequence.

# Context & Application

- **Typical contexts**: function clause bodies and the bodies of `case`, `if`, `try`, and similar clauses.
- **Common applications**: chaining steps where earlier bindings feed later expressions.
- **Historical/stylistic notes**: the book likens an expression sequence to LISP's `progn`.

# Examples

**Example 1** (*Expressions and Expression Sequences*): the value of `E1, E2, ..., En` is the value of the last expression `En`, evaluated using bindings created by `E1`, `E2`, and so on.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Block expression** — A `begin ... end` block wraps an expression sequence into a single expression.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Expecting an expression sequence to yield the value of an earlier expression.
  **Correction**: The value is always that of the last expression in the sequence.

# Common Confusions

- **Confusion**: Believing record declarations or module attributes are expressions.
  **Clarification**: They cannot be evaluated to a value, so they are not expressions.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Expressions and Expression Sequences".

# Verification Notes

- Definition source: Direct quotation from *Expressions and Expression Sequences*.
- Confidence rationale: HIGH — the source explicitly defines both terms.
- Uncertainties: None.
- Cross-reference status: Slug `block-expression` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
