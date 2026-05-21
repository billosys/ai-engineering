---
# === CORE IDENTIFICATION ===
concept: Tuple Module
slug: tuple-module

# === CLASSIFICATION ===
category: core-idioms
subcategory: dynamic-dispatch
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Tuple Modules"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - stateful module
  - parameterized module

# === TYPED RELATIONSHIPS ===
prerequisites:
  - apply
extends: []
related:
  - adapter-pattern
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a tuple module?"
  - "How does calling a function on a tuple module work?"
---

# Quick Definition

A tuple module is a tuple of the form `{Mod, X1, ..., Xn}` used in place of a module name; calling a function on it invokes the named module's function with the tuple passed as an extra last argument.

# Core Definition

"When we call `M:f(Arg1, Arg2, ..., ArgN)`, we have assumed that `M` is a module name. But `M` can also be a tuple of the form `{Mod1, X1, X2, ... Xn}`, in which case the function `Mod1:f(Arg1, Arg2, ..., Arg3, M)` is called" ("The Rest of Sequential Erlang", *Tuple Modules*). That is, the entire tuple is appended as the final argument to the call. "This mechanism can be used to create 'stateful modules'... and to create 'adapter patterns.'"

# Prerequisites

- **apply** — The tuple-module mechanism is the case where `apply`'s (or `M:f`'s) `Mod` argument is a tuple.

# Key Properties

1. A tuple module is a tuple `{Mod, X1, ..., Xn}` used where a module name is expected.
2. Calling `{Mod, X1, ..., Xn}:f(A1, ..., An)` invokes `Mod:f(A1, ..., An, {Mod, X1, ..., Xn})`.
3. The whole tuple becomes the function's extra last argument.
4. The mechanism underpins "stateful modules" and "adapter patterns."

# Construction / Recognition

## To Construct/Create:
1. Build a tuple `{Mod, X1, ..., Xn}` and call `TupleMod:f(Args)` on it.

## To Identify/Recognize:
1. A `M:f(...)` call where `M` is bound to a tuple rather than an atom uses the tuple-module mechanism.

# Context & Application

- **Typical contexts**: simulating modules that carry state, or adapting one interface to another.
- **Common applications**: "stateful modules" and "adapter patterns" (both discussed later in the book).
- **Historical/stylistic notes**: this generalizes the rule that `apply`'s `Mod` argument may be a tuple.

# Examples

**Example 1** (*Tuple Modules* / *apply*): calling `{Mod, P1, P2, ..., Pn}:Func(A1, A2, ..., An)` actually invokes `Mod:Func(A1, A2, ..., An, {Mod, P1, P2, ..., Pn})` — the tuple is passed as the extra final argument.

# Relationships

## Builds Upon
- **apply** — Tuple modules are the tuple-`Mod` case of dynamic dispatch.

## Enables
- This concept does not have downstream cards in scope within these chapters.

## Related
- **Adapter pattern** — Tuple modules are one mechanism for building adapter patterns.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Forgetting that the function called via a tuple module receives an extra argument.
  **Correction**: The target function must have arity one greater than the visible call, to accept the tuple as the last argument.

# Common Confusions

- **Confusion**: Thinking `M` in `M:f(...)` must always be an atom.
  **Clarification**: `M` may be a tuple; then the tuple is passed as an additional final argument to the call.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Tuple Modules".

# Verification Notes

- Definition source: Direct quotation from *Tuple Modules*.
- Confidence rationale: MEDIUM — the source describes the mechanism concisely but defers full treatment ("Stateful Modules", "Adapter Patterns") to later chapters.
- Uncertainties: The detailed use cases are developed outside these chapters and are not carded here.
- Cross-reference status: Slug `apply` extracted in this chapter; `adapter-pattern` exists.
- Re-extraction notes: Fresh extraction; overwrote prior card of the same slug.
