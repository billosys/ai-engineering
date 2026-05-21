---
# === CORE IDENTIFICATION ===
concept: Variables
slug: variables

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
section: "Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "variable binding"
  - "Erlang variables"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - single-assignment
  - anonymous-variable
  - underscore-prefixed-variables
  - variable-scope
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do variables work in Erlang?"
  - "What characters can a variable name contain?"
  - "What is single assignment in Erlang?"
---

# Quick Definition

An Erlang variable is an expression that starts with an uppercase letter or underscore, is bound to a value through pattern matching, and uses single assignment (can only be bound once). When evaluated, a bound variable returns its value.

# Core Definition

The Erlang Reference Manual states: "A variable is an expression. If a variable is bound to a value, the return value is this value. Unbound variables are only allowed in patterns." Variable naming rules: "Variables start with an uppercase letter or underscore (`_`). Variables can contain alphanumeric characters, underscore, and `@`." The binding mechanism: "Variables are bound to values using pattern matching. Erlang uses _single assignment_, that is, a variable can only be bound once." (Erlang Reference Manual, "Expressions", "Variables").

# Prerequisites

- **pattern-matching** -- Variables are bound through pattern matching

# Key Properties

1. Variables are expressions
2. Bound variables return their value when evaluated
3. Unbound variables are only allowed in patterns
4. Variable names start with uppercase letter or underscore (`_`)
5. Variable names can contain alphanumeric characters, underscore, and `@`
6. Erlang uses single assignment: a variable can only be bound once
7. Variables are bound through pattern matching

# Construction / Recognition

## To Construct/Create:
1. Start the name with an uppercase letter or underscore
2. Use alphanumeric characters, underscores, and `@` for the rest
3. Bind the variable through pattern matching (e.g., `X = 42`)

## To Identify/Recognize:
1. Identifiers starting with uppercase letters: `X`, `Name1`, `PhoneNumber`
2. Identifiers starting with underscore: `_`, `_Height`
3. Names containing `@`: `name@node`

# Context & Application

Variables are the primary mechanism for holding and passing values in Erlang. The single-assignment rule means variables act as named constants once bound, which enables equational reasoning and simplifies concurrent programming (no shared mutable state). The naming convention (uppercase start) visually distinguishes variables from atoms (lowercase start).

# Examples

**Example 1** (Variables section): Valid variable names:
```
X
Name1
PhoneNumber
Phone_number
_
_Height
name@node
```

**Example 2** (Variables section): Binding a variable: `[H|_] = [1,2,3]` -- `H` becomes bound to `1`.

# Relationships

## Builds Upon
- **pattern-matching** -- Variables are bound through pattern matching

## Enables
- **anonymous-variable** -- The anonymous variable `_` is a special variable
- **underscore-prefixed-variables** -- Variables starting with `_` have special compiler behavior
- **variable-scope** -- Variables have clause-level scope

## Related
- **single-assignment** -- The binding model for variables
- **terms** -- Bound variables evaluate to terms

# Common Errors

- **Error**: Starting a variable name with a lowercase letter
  **Correction**: Lowercase-starting identifiers are atoms, not variables. Use uppercase or underscore to start variable names.

# Common Confusions

- **Confusion**: Thinking variables can be reassigned like in imperative languages
  **Clarification**: Erlang uses single assignment; once bound, a variable's value cannot change. Attempting to match a bound variable against a different value raises an exception.

# Source Reference

"Expressions" chapter, section "Variables."

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
