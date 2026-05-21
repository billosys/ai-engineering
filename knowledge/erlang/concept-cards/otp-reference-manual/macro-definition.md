---
# === CORE IDENTIFICATION ===
concept: Macro Definition
slug: macro-definition

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
  - "-define"
  - "Erlang macro"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - preprocessor-directives
extends: []
related:
  - constant-vs-function-macros
  - predefined-macros
  - macro-overloading
  - macro-removal
  - macro-stringification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a macro in Erlang?"
  - "What is the -define directive?"
  - "How are macros expanded in Erlang?"
---

# Quick Definition
The `-define` directive creates a macro that is textually expanded during compilation. Macros can be simple constants or parameterized with arguments.

# Core Definition
The Erlang Reference Manual states: "A macro is defined as follows: `-define(Const, Replacement).` `-define(Func(Var1,...,VarN), Replacement).`" It further explains: "A macro definition can be placed anywhere among the attributes and function declarations of a module, but the definition must come before any usage of the macro." Macros are used with the `?` prefix: "`?Const`" or "`?Func(Arg1,...,ArgN)`". "Macros are expanded during compilation. A simple macro `?Const` is replaced with `Replacement`." For function macros, "all occurrences of a variable `Var` from the macro definition are replaced with the corresponding argument `Arg`." (Preprocessor, "Defining and Using Macros" section).

# Prerequisites
- **erlang-module** -- Macros are defined and used within modules
- **preprocessor-directives** -- Macro definition is a preprocessor directive

# Key Properties
1. Two forms: constant macros (`-define(Const, Replacement).`) and function macros (`-define(Func(Var1,...,VarN), Replacement).`)
2. Invoked with `?` prefix: `?Const` or `?Func(Arg1,...,ArgN)`
3. Expanded during compilation -- pure textual substitution
4. Must be defined before use
5. If used in several modules, recommended to place in an include file
6. Good practice to ensure macro definitions are valid Erlang syntactic forms (not mandatory)
7. Use compiler option `'P'` to view macro expansion results: `compile:file(File, ['P'])`

# Construction / Recognition
## To Construct/Create:
1. Constant macro: `-define(TIMEOUT, 200).`
2. Function macro: `-define(MACRO1(X, Y), {a, X, b, Y}).`
3. Use: `?TIMEOUT` or `?MACRO1(a, b)`

## To Identify/Recognize:
1. The `-define(Name, ...)` directive
2. Usage via `?Name` or `?Name(Args)` syntax

# Context & Application
Macros provide compile-time code generation and constant definitions. They are commonly used for: defining constants (timeouts, magic numbers), creating debugging/logging utilities that include `?MODULE` and `?LINE` information, and abstracting repetitive patterns. Unlike functions, macros have no runtime overhead since they are expanded at compile time.

# Examples
**Example 1** (Defining and Using Macros section, constant macro):
```erlang
-define(TIMEOUT, 200).
...
call(Request) ->
    server:call(refserver, Request, ?TIMEOUT).
```
This is expanded to:
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
This is expanded to:
```erlang
bar(X) ->
    {a,a,b,b},
    {a,X,b,123}.
```

# Relationships
## Builds Upon
- **preprocessor-directives** -- Macro definition is a preprocessor directive

## Enables
- **constant-vs-function-macros** -- The two forms of macros
- **macro-overloading** -- Macros can be overloaded by arity
- **macro-removal** -- Defined macros can be undefined with `-undef`
- **macro-stringification** -- Macro arguments can be stringified with `??`
- **conditional-compilation** -- Macros enable conditional code paths

## Related
- **predefined-macros** -- Built-in macros available without `-define`
- **file-inclusion** -- Shared macros are placed in include files

## Contrasts With
None.

# Common Errors
- **Error**: Using a macro before it is defined
  **Correction**: The `-define` must appear before any usage of the macro in the source file

- **Error**: Forgetting the `?` prefix when using a macro
  **Correction**: Macros are always invoked as `?Name` or `?Name(Args)`

# Common Confusions
- **Confusion**: Thinking macros are like functions with scoping rules
  **Clarification**: Macros are purely textual substitution at compile time. They have no scope, no closures, and no runtime overhead.

- **Confusion**: Expecting macro arguments to be evaluated before substitution
  **Clarification**: Macro expansion is textual -- arguments are substituted as-is, not evaluated first. This can lead to unexpected multiple evaluation if an argument expression has side effects.

# Source Reference
"Preprocessor" chapter, "Defining and Using Macros" section.

# Verification Notes
- Definition source: Direct quotes from source with examples
- Confidence rationale: High -- explicit definition with detailed expansion examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
