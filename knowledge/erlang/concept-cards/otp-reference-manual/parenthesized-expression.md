---
# === CORE IDENTIFICATION ===
concept: Parenthesized Expression
slug: parenthesized-expression

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Parenthesized Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "grouped expression"
  - "expression grouping"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression-evaluation
  - operator-precedence
extends: []
related:
  - block-expression
  - arithmetic-expressions
contrasts_with:
  - block-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I override operator precedence in Erlang?"
  - "What do parentheses do in Erlang expressions?"
---

# Quick Definition

Parenthesized expressions `(Expr)` override operator precedence, forcing the enclosed expression to be evaluated first. The return value is the value of the enclosed expression.

# Core Definition

Parenthesized expressions are useful to override operator precedences. The expression `(Expr)` evaluates `Expr` and returns its value. They do not change semantics beyond controlling evaluation order as determined by the operator precedence table (Erlang Reference Manual, "Parenthesized Expressions" section).

# Prerequisites

- **expression-evaluation** — Understanding basic expression evaluation.
- **operator-precedence** — Parentheses are used to override default precedence.

# Key Properties

1. Syntax: `(Expr)`.
2. Forces the enclosed expression to be evaluated as a unit.
3. Overrides the default operator precedence.
4. The return value is the value of `Expr`.
5. Can also change the interpretation of `=` from match operator to compound pattern operator (when used in a pattern context).

# Construction / Recognition

## To Construct:
```erlang
(1 + 2) * 3
```

## To Recognize:
1. Look for expressions enclosed in `(` and `)`.

# Context & Application

Parenthesized expressions are used in arithmetic and other operator expressions to enforce a specific evaluation order that differs from the default precedence. They can also clarify intent in complex expressions, even when not strictly necessary.

# Examples

**Example 1** (Parenthesized Expressions section): Overriding arithmetic precedence:

```erlang
1> 1 + 2 * 3.
7
2> (1 + 2) * 3.
9
```

**Example 2** (Match Operator section): Parentheses affecting pattern vs. expression context:

```erlang
%% Without parentheses: two sequential match operations
f(Key), #{Key := Value} = #{key := Key} = M, Value.

%% With parentheses around inner part: same behavior (redundant)
f(Key), #{Key := Value} = (#{key := Key} = M), Value.

%% With parentheses forcing compound pattern: fails (Key not bound)
f(Key), (#{Key := Value} = #{key := Key}) = M, Value.
%% * variable 'Key' is unbound
```

# Relationships

## Builds Upon
- **expression-evaluation** — Standard evaluation of the enclosed expression.
- **operator-precedence** — Parentheses override the precedence table.

## Related
- **block-expression** — Also groups expressions, but for sequences.
- **arithmetic-expressions** — Commonly used with arithmetic to control precedence.

## Contrasts With
- **block-expression** — Parentheses group a single expression; `begin...end` groups a sequence of expressions.

# Common Errors

- **Error**: Using parentheses around patterns in a way that changes the meaning of `=` from match operator to compound pattern operator.
  **Correction**: Be aware that parentheses around `Pattern1 = Pattern2` create a compound pattern where both must match simultaneously, rather than sequential match operations.

# Common Confusions

- **Confusion**: Thinking parentheses create a new scope or block.
  **Clarification**: Parentheses only affect evaluation order and operator grouping. For a sequence of expressions, use `begin...end`.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Parenthesized Expressions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clear definition and examples from source
- Uncertainties: None
- Cross-reference status: Interaction with compound pattern operator verified in source
