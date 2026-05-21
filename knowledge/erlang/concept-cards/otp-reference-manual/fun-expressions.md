---
# === CORE IDENTIFICATION ===
concept: Fun Expressions
slug: fun-expressions

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: anonymous-functions
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Fun Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "anonymous function"
  - "lambda"
  - "fun"
  - "closure"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - fun-capture
  - guard-sequences
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a fun (anonymous function)?"
  - "How do I create an anonymous function in Erlang?"
  - "Can anonymous functions be recursive?"
---

# Quick Definition

A fun expression creates an anonymous function using the `fun ... end` syntax. Funs can have multiple clauses with pattern matching and guards, and an optional name for self-recursion.

# Core Definition

A fun expression begins with the keyword `fun` and ends with `end`, containing a function declaration similar to a regular function declaration except that the function name is optional and, if present, must be a variable. Variables in a fun head shadow the function name, and both shadow variables in the surrounding function clause. Variables bound in a fun body are local to the fun body. The return value of the expression is the resulting fun (Erlang Reference Manual, "Fun Expressions" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Syntax: `fun (Pattern1,...,PatternN) [when GuardSeq] -> Body end`.
2. Multiple clauses are separated by semicolons, similar to regular functions.
3. An optional name (a variable) can be provided for recursive funs.
4. All clauses must have the same arity.
5. Variables in the fun head shadow both the fun name and surrounding variables.
6. Variables bound in the fun body are local to the fun body.
7. Funs are closures — they capture variables from the enclosing scope.
8. The return value of the fun expression is the fun itself (a callable value).

# Construction / Recognition

## To Create an Anonymous Function:
1. Write `fun`.
2. Add one or more clauses: `(Patterns) [when Guards] -> Body`.
3. Separate multiple clauses with `;`.
4. End with `end`.
5. Optionally add a name variable for recursion: `fun Name(Patterns) -> Body end`.

## To Recognize:
1. Look for the `fun ... end` block.
2. Contains pattern-matching clauses like regular functions but without a module-level function name.

# Context & Application

Funs are central to higher-order programming in Erlang. They are passed to functions like `lists:map/2`, `lists:filter/2`, and `lists:foldl/3`. Named funs enable direct recursion within anonymous functions without needing external references. Funs capture their lexical environment (closure semantics), making them useful for callbacks, event handlers, and deferred execution.

# Examples

**Example 1** (Fun Expressions section): Simple fun:

```erlang
1> Fun1 = fun (X) -> X+1 end.
#Fun<erl_eval.6.39074546>
2> Fun1(2).
3
```

**Example 2** (Fun Expressions section): Fun with multiple clauses and guard:

```erlang
3> Fun2 = fun (X) when X>=5 -> gt; (X) -> lt end.
#Fun<erl_eval.6.39074546>
4> Fun2(7).
gt
```

**Example 3** (Fun Expressions section): Named fun for recursion:

```erlang
5> Fun3 = fun Fact(1) -> 1; Fact(X) when X > 1 -> X * Fact(X - 1) end.
#Fun<erl_eval.6.39074546>
6> Fun3(4).
24
```

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **fun-capture** — The `fun M:F/A` syntax provides an alternative way to create funs from existing functions.

## Related
- **guard-sequences** — Guards can be used in fun clauses.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Trying to use the fun name from outside the fun body for recursion.
  **Correction**: The name variable in a named fun is only in scope within the fun body. To call the fun externally, use the variable it is bound to.

- **Error**: Mixing arities across fun clauses.
  **Correction**: All clauses in a fun must have the same arity.

# Common Confusions

- **Confusion**: Thinking variables bound in a fun body are visible outside the fun.
  **Clarification**: Variables bound in a fun body are local to that fun. They do not affect the enclosing scope.

- **Confusion**: Thinking named funs are equivalent to module-level function definitions.
  **Clarification**: Named funs use a variable name (not an atom) and exist only within the scope of the expression. The name is for self-reference only.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Fun Expressions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit syntax, scoping rules, and examples
- Uncertainties: None
- Cross-reference status: Related concepts verified
