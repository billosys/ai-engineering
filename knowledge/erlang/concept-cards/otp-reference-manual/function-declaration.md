---
# === CORE IDENTIFICATION ===
concept: Function Declaration
slug: function-declaration

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
  - "function definition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - function-clause
  - function-arity
  - function-evaluation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare a function in Erlang?"
  - "What is the syntax for an Erlang function?"
  - "What is a module in Erlang?"
---

# Quick Definition

A function declaration is a sequence of function clauses separated by semicolons and terminated by a period. Each clause has a head (name, argument patterns, optional guard) and a body (sequence of expressions).

# Core Definition

The Erlang Reference Manual defines: "A _function declaration_ is a sequence of function clauses separated by semicolons, and terminated by a period (`.`)." The general syntax is:

```erlang
Name(Pattern11,...,Pattern1N) [when GuardSeq1] ->
    Body1;
...;
Name(PatternK1,...,PatternKN) [when GuardSeqK] ->
    BodyK.
```

"The function name is an atom. Each argument is a pattern." (Erlang Reference Manual, "Functions", "Function Declaration Syntax").

# Prerequisites

- **pattern-matching** -- Function arguments are patterns, and clause selection uses pattern matching

# Key Properties

1. A function declaration is a sequence of one or more function clauses
2. Clauses are separated by semicolons (`;`)
3. The declaration is terminated by a period (`.`)
4. All clauses must have the same function name
5. All clauses must have the same number of arguments (arity)
6. The function name is an atom
7. Each argument is a pattern, not just a variable
8. The clause body is a sequence of expressions separated by commas

# Construction / Recognition

## To Construct/Create:
1. Choose a function name (an atom)
2. Define one or more clauses with the same name and arity
3. For each clause, write argument patterns, optional guard with `when`, then `->` followed by the body
4. Separate clauses with `;`
5. End the last clause with `.`

## To Identify/Recognize:
1. An atom followed by parenthesized argument patterns
2. `->` separating the clause head from the body
3. Multiple clauses with the same name separated by `;`
4. Terminated by `.`

# Context & Application

Function declarations are the primary unit of code organization in Erlang modules. Multi-clause functions provide a natural way to handle different cases through pattern matching, replacing if-else chains common in other languages. The requirement that function names are atoms and arguments are patterns is fundamental to Erlang's pattern-matching dispatch model.

# Examples

**Example 1** (Function Declaration Syntax section): A two-clause factorial function:
```erlang
fact(N) when N > 0 ->  % first clause head
    N * fact(N-1);     % first clause body

fact(0) ->             % second clause head
    1.                 % second clause body
```

# Relationships

## Builds Upon
- **pattern-matching** -- Arguments are patterns matched against call arguments

## Enables
- **function-evaluation** -- Declarations define what gets evaluated when a function is called
- **function-clause** -- Declarations consist of clauses
- **tail-recursion** -- Tail recursion applies to function body structure

## Related
- **function-arity** -- Arity is part of the function's unique identity

# Common Errors

- **Error**: Using different names across clauses intended to be part of the same function
  **Correction**: All clauses in a function declaration must have the same name; different names define different functions

- **Error**: Ending intermediate clauses with `.` instead of `;`
  **Correction**: Use `;` between clauses and `.` only after the final clause

# Common Confusions

- **Confusion**: Thinking clauses with different arities are part of the same function
  **Clarification**: Functions with the same name but different arities are completely different functions; `f/1` and `f/2` are unrelated

# Source Reference

"Functions" chapter, section "Function Declaration Syntax", including the syntax template and factorial example.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit syntax definition with example
- Uncertainties: None
- Cross-reference status: Related slugs planned for extraction
