---
concept: Compile-Time Error
slug: compile-time-error
category: error-handling
subcategory: error-classes
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Exceptions"
chapter_number: 7
pdf_page: null
section: "Compile-Time Errors"
extraction_confidence: high
aliases:
  - "compilation error"
  - "syntax error"
prerequisites:
  - compiling-erlang-code
extends: []
related:
  - logical-error
  - runtime-error
contrasts_with:
  - logical-error
  - runtime-error
answers_questions:
  - "What distinguishes errors, exits, and throws?"
---

# Compile-Time Error

## Quick Definition

A compile-time error is a mistake — usually syntactic — caught by the compiler before the program can run, such as a mismatched module name or unclosed parenthesis.

## Core Definition

Compile-time errors are often syntactic mistakes — wrong function names, mismatched tokens (brackets, parentheses, periods, commas), wrong arity, and so on. The compiler reports them, sometimes as warnings and sometimes as hard errors, before the code can run. Common messages include "Module name does not match file name," "function ... undefined," "syntax error before: ...," "head mismatch," "this expression will fail with a 'badarith' exception," and "variable ... is unused." It is best to resolve compiler errors in the order reported, since one error can cascade into many misleading ones (Hébert, ch. 7, "Compile-Time Errors").

## Prerequisites

- **Compiling Erlang code** — Compile-time errors arise during compilation

## Key Properties

1. Caught by the compiler before the program runs.
2. Usually syntactic: wrong tokens, names, arity.
3. May appear as warnings (e.g., unused variable) or hard errors.
4. The compiler can pre-detect some failures like a `badarith`.
5. One real error often cascades into many spurious follow-on errors.

## Construction / Recognition

To diagnose compile-time errors:

1. Read the first reported error and its line number.
2. Fix it (check tokens, names, arity).
3. Recompile; later errors may have been cascades of the first.

## Context & Application

Compile-time errors are the easiest class to fix because the compiler points at them. The main challenge is finding the root error among a cascade of follow-on messages.

## Examples

**Example** (ch. 7): `Module name 'madule' does not match file name 'module'` — the `-module` attribute does not match the filename.

**Example** (ch. 7): `syntax error before: 'SomeCharacterOrWord'` — commonly an unclosed parenthesis or wrong expression terminator.

## Relationships

### Prerequisites

- **Compiling Erlang code** — These errors occur at compile time

### Related

- **Logical error** — A different error class, not caught by the compiler
- **Runtime error** — A different error class, caught only when the code runs

### Contrasts With

- **Logical error** — Logical errors compile fine and produce wrong behavior
- **Runtime error** — Runtime errors compile fine and crash during execution

## Common Errors

- **Error**: Fixing later cascade errors first
  **Correction**: Resolve errors in reported order; later ones may vanish once the first is fixed

## Common Confusions

- **Confusion**: Treating every compiler warning as harmless
  **Clarification**: Warnings (e.g., unused variable) may indicate real bugs; investigate them

## Source Reference

Chapter 7: "Errors and Exceptions," section "Compile-Time Errors."

## Verification Notes

- Definition: Adapted from the "Compile-Time Errors" section
- Confidence: HIGH — explicit section with message list
- Uncertainties: None
