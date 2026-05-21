---
# === CORE IDENTIFICATION ===
concept: apply
slug: apply

# === CLASSIFICATION ===
category: core-idioms
subcategory: dynamic-dispatch
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "apply"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "apply/3"
  - dynamic function call

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arity
extends: []
related:
  - function-reference
  - tuple-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the apply BIF do?"
  - "How do I call a function whose name is computed at runtime?"
  - "Why should apply be used sparingly?"
---

# Quick Definition

`apply(Mod, Func, [Arg1, ..., ArgN])` calls function `Func` in module `Mod` with the given argument list; it is used when the module or function name is computed dynamically.

# Core Definition

"The BIF `apply(Mod, Func, [Arg1, Arg2, ..., ArgN])` applies the function `Func` in the module `Mod` to the arguments `Arg1, Arg2, ... ArgN`. It is equivalent to calling `Mod:Func(Arg1, Arg2, ..., ArgN)`" ("The Rest of Sequential Erlang", *apply*). What makes `apply` different from a direct call "is that the module name and/or the function name can be computed dynamically." All Erlang BIFs can also be called via `apply` by assuming they belong to module `erlang`. The book warns: "The use of `apply` should be avoided if possible" — when the number of arguments is known in advance, a direct `M:F(...)` call is much better, because `apply` defeats many analysis tools and certain compiler optimizations.

# Prerequisites

- **Arity** — `apply` takes an argument *list* whose length is the function's arity, so understanding arity is needed.

# Key Properties

1. `apply(Mod, Func, ArgList)` is equivalent to `Mod:Func(ArgList...)`.
2. The module and/or function name may be computed at runtime.
3. BIFs are callable via `apply` by treating them as belonging to module `erlang`.
4. Should be used sparingly — it defeats analysis tools and compiler optimizations.
5. The `Mod` argument may also be a tuple, invoking the tuple-module mechanism.

# Construction / Recognition

## To Construct/Create:
1. Build a dynamic call: `apply(Mod, Func, [Arg1, ..., ArgN])`.
2. Call a BIF dynamically: `apply(erlang, atom_to_list, [hello])`.

## To Identify/Recognize:
1. An `apply/3` call signals that the target function is selected dynamically.

# Context & Application

- **Typical contexts**: dispatching to a function whose module or name is decided at runtime.
- **Common applications**: dynamic BIF invocation via `apply(erlang, ...)`.
- **Historical/stylistic notes**: when `Mod` is a tuple `{Mod, P1, ..., Pn}`, the tuple itself is passed as an extra last argument — the basis of "stateful modules."

# Examples

**Example 1** (*apply*): a dynamic BIF call:

```erlang
1> apply(erlang, atom_to_list, [hello]).
"hello"
```

**Example 2** (*apply*): when `M` is a tuple, calling `{Mod, P1, P2, ..., Pn}:Func(A1, ..., An)` actually invokes `Mod:Func(A1, ..., An, {Mod, P1, P2, ..., Pn})`.

# Relationships

## Builds Upon
- This is a small dispatch concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Function reference** — Both concern referring to / calling functions indirectly.
- **Tuple module** — `apply` with a tuple `Mod` triggers the tuple-module mechanism.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Using `apply` when the function and arity are known at compile time.
  **Correction**: Use a direct `M:F(Arg1, ..., ArgN)` call — it is clearer and allows compiler optimizations.

- **Error**: Passing arguments to `apply` as separate parameters.
  **Correction**: The arguments must be supplied as a single list, `[Arg1, ..., ArgN]`.

# Common Confusions

- **Confusion**: Believing `apply` is just stylistically different from a direct call.
  **Clarification**: It is functionally equivalent but defeats static analysis and some optimizations; reserve it for genuinely dynamic dispatch.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "apply".

# Verification Notes

- Definition source: Direct quotation and adaptation from *apply*.
- Confidence rationale: HIGH — the source explicitly defines `apply`, its equivalence, and its caveats.
- Uncertainties: None.
- Cross-reference status: Slugs `arity`, `function-reference`, `tuple-module` extracted/exist in scope.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
