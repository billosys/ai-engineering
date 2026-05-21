---
# === CORE IDENTIFICATION ===
concept: Macro Overloading
slug: macro-overloading

# === CLASSIFICATION ===
category: core-idioms
subcategory: preprocessor
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Preprocessor"
chapter_number: null
pdf_page: null
section: "Macro Overloading"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro-definition
  - constant-vs-function-macros
extends: []
related:
  - function-arity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can Erlang macros be overloaded?"
  - "Can the same macro name have different arities?"
  - "What happens when a macro is called with the wrong number of arguments?"
---

# Quick Definition
Erlang macros can be overloaded by arity: the same macro name can have multiple definitions with different numbers of arguments. Predefined macros cannot be overloaded.

# Core Definition
The Erlang Reference Manual states: "It is possible to overload macros, except for predefined macros. An overloaded macro has more than one definition, each with a different number of arguments." It further specifies: "A macro `?Func(Arg1,...,ArgN)` with a (possibly empty) list of arguments results in an error message if there is at least one definition of `Func` with arguments, but none with N arguments." (Preprocessor, "Macro Overloading" section).

# Prerequisites
- **macro-definition** -- Overloading requires understanding basic macro definition
- **constant-vs-function-macros** -- Overloading interacts with the distinction between constant and function macros

# Key Properties
1. Same macro name can have multiple definitions with different numbers of arguments
2. Predefined macros cannot be overloaded
3. A constant macro (no args) and a function macro (with args) of the same name are distinct
4. Error if a function macro is called with a number of arguments that has no matching definition
5. A constant macro `?C` and a function macro call `?C()` (zero-argument function macro) are different
6. Introduced in Erlang 5.7.5/OTP R13B04

# Construction / Recognition
## To Construct/Create:
1. Define multiple macros with the same name but different arities:
```erlang
-define(F0(), c).
-define(F1(A), A).
```

## To Identify/Recognize:
1. Multiple `-define` directives with the same macro name but different parameter counts

# Context & Application
Macro overloading is useful when a macro has a common case with fewer arguments and specialized cases with more. For example, a logging macro might have a zero-argument form that logs a default message and a one-argument form that logs a specific message. The interaction between constant macros and zero-argument function macros requires careful attention.

# Examples
**Example 1** (Macro Overloading section): Given these definitions:
```erlang
-define(F0(), c).
-define(F1(A), A).
-define(C, m:f).
```

The following does NOT work:
```erlang
f0() ->
    ?F0. % No, an empty list of arguments expected.

f1(A) ->
    ?F1(A, A). % No, exactly one argument expected.
```

But this works:
```text
f() ->
    ?C().
```
It expands to:
```erlang
f() ->
    m:f().
```
Here `?C` is a constant macro expanding to `m:f`, and `()` is part of the resulting expression, not a macro argument list.

# Relationships
## Builds Upon
- **macro-definition** -- Overloading extends the basic `-define` mechanism
- **constant-vs-function-macros** -- Overloading interacts with the constant vs function distinction

## Enables
None directly.

## Related
- **function-arity** -- Like functions, macros are distinguished by name and arity

## Contrasts With
None.

# Common Errors
- **Error**: Calling an overloaded macro with the wrong number of arguments
  **Correction**: Use the exact number of arguments matching one of the macro's definitions

- **Error**: Expecting `?F0` (without parentheses) to work when only `-define(F0(), c).` is defined
  **Correction**: If the macro is defined with `()`, it must be called with `()`: `?F0()`

# Common Confusions
- **Confusion**: Confusing `?C()` (constant macro expansion + parentheses in code) with a zero-argument function macro call
  **Clarification**: If `C` is defined as a constant macro (`-define(C, m:f).`), then `?C()` expands `C` to `m:f` and the `()` becomes part of the expression: `m:f()`. This is different from a zero-argument function macro `?F0()`.

# Source Reference
"Preprocessor" chapter, "Macro Overloading" section.

# Verification Notes
- Definition source: Direct quotes from source with error examples
- Confidence rationale: High -- explicit definition with clear examples of valid and invalid usage
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
