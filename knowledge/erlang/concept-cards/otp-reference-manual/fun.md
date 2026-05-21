---
# === CORE IDENTIFICATION ===
concept: Fun
slug: fun

# === CLASSIFICATION ===
category: data-types
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "Fun"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - functional object
  - anonymous function
  - lambda

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-term
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
---

# Quick Definition
A fun is a functional object that allows creating an anonymous function and passing the function itself -- not its name -- as an argument to other functions.

# Core Definition
The Erlang Reference Manual defines a fun as "a functional object. Funs make it possible to create an anonymous function and pass the function itself -- not its name -- as an argument to other functions." Funs are tested with `is_function/1` (tests if a term is a fun) and `is_function/2` (tests if a term is a fun with a specific arity). Funs are first-class values in Erlang (Data Types, "Fun" section).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. A functional object -- can be stored in variables, passed as arguments, returned from functions
2. Creates anonymous functions using `fun (Args) -> Body end` syntax
3. Can also capture named functions: `fun Module:Function/Arity`
4. Tested with `is_function/1` (is it a fun?) and `is_function/2` (is it a fun of arity N?)
5. Printed representation: `#Fun<...>`
6. Closures -- funs capture bindings from their enclosing scope

# Construction / Recognition
## To Construct/Create:
1. Anonymous fun: `fun (X) -> X + 1 end`
2. Named function capture: `fun lists:map/2`
3. Multi-clause fun: `fun (0) -> zero; (N) -> N end`

## To Identify/Recognize:
1. Use `is_function/1` to test if a term is a fun
2. Use `is_function(F, Arity)` to test for a fun with specific arity
3. Funs print as `#Fun<...>`

# Context & Application
Funs are essential for functional programming in Erlang. They are used with higher-order functions like `lists:map/2`, `lists:filter/2`, `lists:foldl/3`, and for callback-based APIs. Funs enable passing behavior as data, which is a core pattern in Erlang's functional style.

# Examples
**Example 1** (Data Types, "Fun" section):
```erlang
1> Fun1 = fun (X) -> X+1 end.
#Fun<erl_eval.6.39074546>
2> Fun1(2).
3
```

**Example 2** (Data Types, "Fun" section): Arity testing:
```erlang
1> F = fun() -> ok end.
#Fun<erl_eval.43.105768164>
2> is_function(F).
true
3> is_function(F, 0).
true
4> is_function(F, 1).
false
```

# Relationships
## Builds Upon
This is a foundational type with no prerequisites.

## Enables
No direct dependents within this extraction scope.

## Related
- **erlang-term** -- Funs are a kind of term

## Contrasts With
No direct contrasts within this source.

# Common Errors
- **Error**: Calling a fun with the wrong number of arguments
  **Correction**: Use `is_function(F, Arity)` to verify arity before calling, or rely on pattern matching to handle errors

# Common Confusions
- **Confusion**: Believing funs and named functions are different types of values
  **Clarification**: A captured named function (`fun Module:Function/Arity`) is also a fun and passes `is_function/1`. Both anonymous and captured funs are the same type.

# Source Reference
Data Types chapter, "Fun" section.

# Verification Notes
- Definition source: Direct quote from source ("a functional object")
- Confidence rationale: High -- explicit definition with examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
