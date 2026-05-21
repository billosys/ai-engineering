---
# === CORE IDENTIFICATION ===
concept: Compile-Time Errors
slug: compile-time-errors

# === CLASSIFICATION ===
category: error-handling
subcategory: error-types
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Errors and Error Handling"
chapter_number: null
pdf_page: null
section: "Terminology"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "compilation errors"
  - "syntax errors"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - logical-errors
  - runtime-errors
contrasts_with:
  - runtime-errors
  - logical-errors

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a compile-time error in Erlang?"
  - "When do compile-time errors occur?"
  - "What is an example of a compile-time error?"
---

# Quick Definition

Compile-time errors occur when the compiler fails to compile the program, such as syntax errors. They are detected before the program runs.

# Core Definition

Compile-time errors are one of four error types in Erlang. They occur when the compiler fails to compile the program. An example is a syntax error. Unlike runtime errors, compile-time errors prevent the program from being loaded and executed at all (Erlang Reference Manual, "Errors and Error Handling" chapter, "Terminology" section).

# Prerequisites

None.

# Key Properties

1. Detected by the compiler before program execution.
2. Prevent the module from being compiled and loaded.
3. Include syntax errors, undefined function references, type mismatches detectable at compile time, and malformed module attributes.
4. Not exceptions — they are a distinct category from runtime errors.

# Construction / Recognition

## To Recognize:
1. The compiler reports errors and refuses to produce a `.beam` file.
2. Error messages include file name, line number, and description.

## Common Examples:
- Missing closing parenthesis, bracket, or `end` keyword.
- Misspelled keywords.
- Missing function clauses or export declarations.

# Context & Application

Compile-time errors are the earliest feedback a developer receives. They are caught by the compiler (`erlc`, `c(Module)` in the shell, or build tools like rebar3) and must be fixed before the code can run. Erlang's compiler provides descriptive error messages to help locate the issue.

# Examples

**Example 1**: Syntax error — missing `end`:

```erlang
f(X) ->
    case X of
        1 -> one
    %% missing 'end'
```

**Example 2**: Undefined function warning/error:

```erlang
-export([foo/1]).
%% foo/1 is exported but not defined — compile error
```

# Relationships

## Related
- **logical-errors** — Another category of errors, but detected by the programmer, not the compiler.
- **runtime-errors** — Errors that occur during execution, not compilation.

## Contrasts With
- **runtime-errors** — Runtime errors occur during execution; compile-time errors prevent execution.
- **logical-errors** — Logical errors are semantically wrong but syntactically valid code.

# Common Errors

- **Error**: Confusing a compile-time warning with a compile-time error.
  **Correction**: Warnings (e.g., unused variables) allow compilation to proceed; errors prevent it.

# Common Confusions

- **Confusion**: Thinking all errors can be caught with `try`/`catch`.
  **Clarification**: Compile-time errors cannot be caught at runtime — they prevent the module from loading. Only runtime errors can be caught with `try`/`catch`.

# Source Reference

Erlang Reference Manual, "Errors and Error Handling" chapter, "Terminology" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — directly defined in source
- Uncertainties: None
- Cross-reference status: Part of four-category error taxonomy in source
