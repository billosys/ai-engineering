---
# === CORE IDENTIFICATION ===
concept: Patterns in Expressions
slug: patterns-in-expressions

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "expression patterns"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
  - terms
extends:
  - pattern-matching
related:
  - compound-pattern-operator
  - string-prefix-in-patterns
  - expressions-in-patterns
  - match-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a pattern in Erlang?"
  - "Where are patterns allowed in Erlang expressions?"
  - "What is the structure of a pattern?"
---

# Quick Definition

A pattern has the same structure as a term but can contain unbound variables. Patterns are allowed in clause heads, case expressions, receive expressions, and match expressions.

# Core Definition

The Erlang Reference Manual states: "A pattern has the same structure as a term but can contain unbound variables." Patterns "are allowed in clause heads, case expressions, receive expressions, and match expressions." (Erlang Reference Manual, "Expressions", "Patterns").

# Prerequisites

- **pattern-matching** -- Patterns are the mechanism through which matching operates
- **terms** -- Patterns have the same structure as terms

# Key Properties

1. A pattern has the same structure as a term
2. Patterns can contain unbound variables (terms cannot)
3. Patterns are allowed in: clause heads, case expressions, receive expressions, and match expressions
4. Patterns can be composed using the compound pattern operator
5. String prefix matching is syntactic sugar available in patterns
6. Arithmetic expressions are allowed in patterns if they use only numeric/bitwise operators and can be evaluated to a constant at compile time

# Construction / Recognition

## To Construct/Create:
1. Write a term-like structure
2. Replace positions where values should be extracted with unbound variables
3. Use literal values where specific values are required

## To Identify/Recognize:
1. Appears on the left side of `=` (match operator)
2. Appears in clause heads after the function name
3. Appears after `case ... of`
4. Appears after `receive`

# Context & Application

Patterns are the core mechanism for both data destructuring and conditional dispatch in Erlang. They combine the role of conditionals and variable binding into a single construct.

# Examples

**Example 1** (Patterns section): Basic patterns:
```
Name1
[H|T]
{error,Reason}
```

**Example 2** (Expressions in Patterns section): Arithmetic in patterns:
```erlang
case {Value, Result} of
    {?THRESHOLD+1, ok} -> ...
```

# Relationships

## Builds Upon
- **pattern-matching** -- Patterns are used in pattern matching
- **terms** -- Patterns have term structure

## Enables
- **compound-pattern-operator** -- Combines two patterns
- **string-prefix-in-patterns** -- Syntactic sugar for matching string prefixes
- **expressions-in-patterns** -- Compile-time constant expressions in patterns

## Related
- **match-operator** -- One of the contexts where patterns are used

# Common Errors

- **Error**: Using a non-constant expression in a pattern (e.g., a function call)
  **Correction**: Only arithmetic/bitwise expressions that can be evaluated to a constant at compile time are allowed in patterns

# Common Confusions

- **Confusion**: Thinking patterns and expressions are interchangeable
  **Clarification**: Patterns can contain unbound variables and appear in specific contexts (left of `=`, clause heads); expressions are evaluated and return values

# Source Reference

"Expressions" chapter, section "Patterns."

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
