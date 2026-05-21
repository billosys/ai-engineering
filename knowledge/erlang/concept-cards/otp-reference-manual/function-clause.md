---
# === CORE IDENTIFICATION ===
concept: Function Clause
slug: function-clause

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-declarations
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Functions"
chapter_number: null
pdf_page: null
section: "Function Declaration Syntax"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "clause"
  - "function clause head and body"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - function-declaration
  - function-evaluation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function clause in Erlang?"
  - "What are the parts of a function clause?"
  - "How are function clause heads and bodies structured?"
---

# Quick Definition

A function clause consists of a clause head and a clause body separated by `->`. The head contains the function name, argument patterns, and an optional guard sequence; the body is a sequence of expressions.

# Core Definition

The Erlang Reference Manual states: "A _function clause_ consists of a _clause head_ and a _clause body_, separated by `->`. A clause _head_ consists of the function name, an argument list, and an optional guard sequence beginning with the keyword `when`." A clause _body_ "consists of a sequence of expressions separated by comma (`,`)" (Erlang Reference Manual, "Functions", "Function Declaration Syntax").

# Prerequisites

- **pattern-matching** -- Clause head arguments are patterns matched during evaluation

# Key Properties

1. A clause has two parts: head and body, separated by `->`
2. The head contains: function name (atom), argument patterns, and optional `when GuardSeq`
3. The body contains: a sequence (one or more) of expressions separated by commas
4. The value of the last expression in the body is the return value
5. Multiple clauses of the same function are separated by `;`

# Construction / Recognition

## To Construct/Create:
1. Write the function name followed by argument patterns in parentheses
2. Optionally add `when` followed by a guard sequence
3. Write `->` to separate head from body
4. Write one or more expressions separated by `,` as the body

## To Identify/Recognize:
1. The `->` token separates the clause head from the clause body
2. The clause head starts with an atom (function name) followed by `(`
3. The clause body ends with either `;` (more clauses follow) or `.` (last clause)

# Context & Application

Function clauses are the building blocks of function declarations. Each clause handles a specific case based on the argument patterns and guard conditions. Clauses are evaluated sequentially, providing a declarative way to express conditional logic through pattern matching rather than nested if-else statements.

# Examples

**Example 1** (Function Declaration Syntax section): The factorial function has two clauses:
```erlang
fact(N) when N > 0 ->  % first clause: head is "fact(N) when N > 0"
    N * fact(N-1);     % first clause: body is "N * fact(N-1)"

fact(0) ->             % second clause: head is "fact(0)"
    1.                 % second clause: body is "1"
```

# Relationships

## Builds Upon
- **pattern-matching** -- Arguments in clause heads are patterns

## Enables
- **function-declaration** -- Declarations are composed of clauses
- **function-evaluation** -- Evaluation proceeds by scanning clauses sequentially

## Related
- **variables** -- Variables scoped to the clause

# Common Errors

- **Error**: Omitting the body of a clause (empty body)
  **Correction**: A clause body is a _sequence_ of expressions and must contain at least one expression

- **Error**: Using a comma instead of semicolon between clauses
  **Correction**: Clauses are separated by `;`, expressions within a body are separated by `,`

# Common Confusions

- **Confusion**: Thinking clause order does not matter
  **Clarification**: Clauses are scanned sequentially during evaluation; order determines which clause matches first

# Source Reference

"Functions" chapter, section "Function Declaration Syntax", syntax template and factorial example.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit structural definition in source
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
