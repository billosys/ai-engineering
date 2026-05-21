---
# === CORE IDENTIFICATION ===
concept: Block Expression
slug: block-expression

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: control-flow
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Block Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "begin...end block"
  - "begin block"
  - "begin-end expression"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression-evaluation
extends: []
related:
  - parenthesized-expression
  - variable-scope
contrasts_with:
  - parenthesized-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a begin...end block in Erlang?"
  - "How do I group multiple expressions into a single expression?"
  - "What does a block expression return?"
---

# Quick Definition

A block expression `begin Expr1, ..., ExprN end` groups a sequence of expressions into a single expression. The return value is the value of the last expression `ExprN`.

# Core Definition

Block expressions provide a way to group a sequence of expressions, similar to a clause body. The expressions `Expr1` through `ExprN` are evaluated sequentially, separated by commas. The return value is the value of the last expression `ExprN` (Erlang Reference Manual, "Block Expressions" section).

# Prerequisites

- **expression-evaluation** — Understanding how expressions are evaluated sequentially.

# Key Properties

1. Syntax: `begin Expr1, ..., ExprN end`.
2. Expressions are evaluated sequentially from left to right.
3. The return value is the value of the last expression.
4. Variables bound in earlier expressions are available in later ones within the block.
5. Useful where a single expression is syntactically required but multiple expressions are needed.

# Construction / Recognition

## To Construct:
```erlang
begin
    Expr1,
    ...,
    ExprN
end
```

## To Recognize:
1. Look for `begin ... end` delimiters.
2. Contains a comma-separated sequence of expressions.

# Context & Application

Block expressions are used when the syntax requires a single expression but you need to evaluate multiple expressions in sequence. Common use cases include complex expressions in match operator right-hand sides, embedding sequences where only one expression is expected (such as in bit syntax size expressions), and providing intermediate bindings within an expression context.

# Examples

**Example 1** (Block Expressions section): Grouping expressions:

```erlang
begin
    X = 1,
    Y = 2,
    X + Y
end
```

**Example 2** (Match Operator section): Using a block to compute a value before matching:

```erlang
<<X:Y>> = begin Y = 8, <<42:8>> end, X.
```

This evaluates the block first (binding `Y` to 8 and creating a binary), then matches the binary against the pattern `<<X:Y>>`.

# Relationships

## Builds Upon
- **expression-evaluation** — Expressions in the block follow standard evaluation rules.

## Enables
- Complex single-expression contexts where multiple sub-expressions are needed.

## Related
- **parenthesized-expression** — Also groups expressions, but for a single expression only (precedence override).
- **variable-scope** — Variables bound in the block are visible after it (same function clause scope).

## Contrasts With
- **parenthesized-expression** — Parentheses override precedence for a single expression; `begin...end` groups a sequence of expressions.

# Common Errors

- **Error**: Using `begin...end` unnecessarily when a comma-separated body is already allowed (e.g., in function clause bodies).
  **Correction**: Block expressions are only needed where the syntax expects a single expression. In clause bodies, multiple expressions separated by commas are already allowed.

# Common Confusions

- **Confusion**: Thinking block expressions create a new scope that isolates variables.
  **Clarification**: Variables bound inside a `begin...end` block are visible in the surrounding function clause scope, just like any other expression.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Block Expressions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clear definition from source
- Uncertainties: None
- Cross-reference status: Verified usage example from "Match Operator" section
