---
# === CORE IDENTIFICATION ===
concept: Constant Macros vs Function Macros
slug: constant-vs-function-macros

# === CLASSIFICATION ===
category: core-idioms
subcategory: preprocessor
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Preprocessor"
chapter_number: null
pdf_page: null
section: "Defining and Using Macros"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "simple macros vs parameterized macros"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro-definition
extends: []
related:
  - macro-overloading
  - predefined-macros
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the two forms of Erlang macros?"
  - "What is the difference between a constant macro and a function macro?"
  - "How does argument substitution work in Erlang macros?"
---

# Quick Definition
Erlang macros come in two forms: constant macros (no arguments, simple replacement) and function macros (parameterized with arguments that are substituted into the replacement text).

# Core Definition
The Erlang Reference Manual defines the two forms:
- Constant macro: `-define(Const, Replacement).` -- Used as `?Const`, replaced with `Replacement`.
- Function macro: `-define(Func(Var1,...,VarN), Replacement).` -- Used as `?Func(Arg1,...,ArgN)`, replaced with `Replacement` where "all occurrences of a variable `Var` from the macro definition are replaced with the corresponding argument `Arg`."
(Preprocessor, "Defining and Using Macros" section).

# Prerequisites
- **macro-definition** -- Both forms are created with `-define`

# Key Properties
1. Constant macros have no parentheses in their definition: `-define(TIMEOUT, 200).`
2. Function macros have parenthesized parameters: `-define(MACRO(X, Y), {X, Y}).`
3. Constant macros are invoked without arguments: `?TIMEOUT`
4. Function macros are invoked with arguments: `?MACRO(a, b)`
5. In function macros, each occurrence of a parameter variable in the replacement is substituted with the corresponding argument
6. A constant macro name followed by `()` is valid -- it is not a function macro call, but the macro expansion followed by empty parentheses

# Construction / Recognition
## To Construct/Create:
1. Constant: `-define(PI, 3.14159).` -- use as `?PI`
2. Function: `-define(SQUARE(X), (X) * (X)).` -- use as `?SQUARE(5)`

## To Identify/Recognize:
1. Constant: `-define(Name, Replacement).` without parenthesized parameters
2. Function: `-define(Name(Vars...), Replacement).` with parenthesized parameters

# Context & Application
Constant macros are commonly used for named constants (timeouts, sizes, configuration values) and for conditional compilation flags. Function macros are used for code patterns that need parameterization, such as logging macros that embed `?MODULE` and `?LINE`, or assertion macros in test frameworks. The distinction matters for macro overloading, where the same name can have both constant and function macro definitions.

# Examples
**Example 1** (Defining and Using Macros section, constant macro):
```erlang
-define(TIMEOUT, 200).
...
call(Request) ->
    server:call(refserver, Request, ?TIMEOUT).
```
Expanded to:
```erlang
call(Request) ->
    server:call(refserver, Request, 200).
```

**Example 2** (Defining and Using Macros section, function macro):
```erlang
-define(MACRO1(X, Y), {a, X, b, Y}).
...
bar(X) ->
    ?MACRO1(a, b),
    ?MACRO1(X, 123)
```
Expanded to:
```erlang
bar(X) ->
    {a,a,b,b},
    {a,X,b,123}.
```

# Relationships
## Builds Upon
- **macro-definition** -- Both forms use `-define`

## Enables
- **macro-overloading** -- Same name can have constant and function variants

## Related
- **predefined-macros** -- Some predefined macros are constant (`?MODULE`), some are function-like (`?FEATURE_ENABLED(Feature)`)

## Contrasts With
None -- the two forms complement each other rather than contrasting.

# Common Errors
- **Error**: Invoking a function macro without arguments or with the wrong number of arguments
  **Correction**: A function macro `?F(A)` requires exactly one argument; see macro overloading for same-name macros with different arities

- **Error**: Not wrapping macro parameters in parentheses in the replacement to avoid operator precedence issues
  **Correction**: Use `-define(DOUBLE(X), ((X) + (X))).` to avoid surprises with complex argument expressions

# Common Confusions
- **Confusion**: Thinking `?C()` on a constant macro `C` calls it as a function macro
  **Clarification**: As shown in the source, if `-define(C, m:f).` then `?C()` expands to `m:f()` -- the `()` is part of the expanded code, not a macro call with zero arguments. This only causes an error if there is a function-macro definition of `C` but none with zero arguments.

# Source Reference
"Preprocessor" chapter, "Defining and Using Macros" section.

# Verification Notes
- Definition source: Direct quotes from source with expansion examples
- Confidence rationale: High -- explicit definition with clear examples of both forms
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
