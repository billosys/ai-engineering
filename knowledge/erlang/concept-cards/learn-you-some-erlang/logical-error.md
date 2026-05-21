---
concept: Logical Error
slug: logical-error
category: error-handling
subcategory: error-classes
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Exceptions"
chapter_number: 7
pdf_page: null
section: "No, YOUR Logic Is Wrong!"
extraction_confidence: high
aliases:
  - "logic error"
  - "semantic error"
prerequisites: []
extends: []
related:
  - compile-time-error
  - runtime-error
contrasts_with:
  - compile-time-error
  - runtime-error
answers_questions:
  - "What distinguishes errors, exits, and throws?"
---

# Logical Error

## Quick Definition

A logical error is a mistake in the program's logic that does not crash it, but causes wrong results or unintended behavior. It is the hardest kind of error to find.

## Core Definition

Logical errors are the hardest kind of error to find and debug. They come from the programmer — branches of `if`s and `case`s that don't consider all cases, a multiplication that should have been a division, and so on. They do not make programs crash, but lead to unseen bad data or programs working in unintended ways. Erlang offers facilities to help — test frameworks, the TypEr and Dialyzer tools, a debugger and tracing module — but testing is the best defense (Hébert, ch. 7, "No, YOUR Logic Is Wrong!").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. A mistake in the program's logic, not its syntax.
2. Does not crash the program.
3. Produces wrong data or unintended behavior.
4. The hardest class of error to find and debug.
5. Best defended against with testing; tools include TypEr, Dialyzer, debuggers, tracing.

## Construction / Recognition

To recognize a logical error: the program runs without crashing, but produces results that are wrong or behaves in ways not intended.

## Context & Application

Logical errors are largely the programmer's own responsibility. The book focuses instead on crashing errors, noting logical errors are the origin of the "let it crash" ideal — it is better for problems to crash visibly than to silently bubble up through many levels.

## Examples

**Example** (ch. 7): Using a multiplication where a division was intended — the program runs but produces incorrect values.

## Relationships

### Related

- **Compile-time error** — Caught by the compiler; logical errors are not
- **Runtime error** — Crashes the program; logical errors do not

### Contrasts With

- **Compile-time error** — Compile-time errors are detected before running; logical errors never are
- **Runtime error** — Runtime errors crash; logical errors run silently with wrong results

## Common Errors

- **Error**: Not considering all branches of an `if` or `case`
  **Correction**: Cover all logical cases; test thoroughly

## Common Confusions

- **Confusion**: Assuming a non-crashing program is correct
  **Clarification**: A logical error produces wrong output without any crash

## Source Reference

Chapter 7: "Errors and Exceptions," section "No, YOUR Logic Is Wrong!"

## Verification Notes

- Definition: Adapted from the "No, YOUR Logic Is Wrong!" section
- Confidence: HIGH — explicit section
- Uncertainties: None
