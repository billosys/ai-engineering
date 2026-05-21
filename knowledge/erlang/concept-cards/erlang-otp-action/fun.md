---
# === CORE IDENTIFICATION ===
concept: Fun
slug: fun

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: higher-order-functions
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.7 Funs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - lambda expression
  - closure
  - anonymous function
  - function as data

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-function
  - function-clause-selection
extends:
  - erlang-term
related:
  - functional-programming
  - remote-call
  - single-assignment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a fun in Erlang?"
  - "What is the difference between an alias fun and an anonymous fun?"
  - "What is a closure?"
  - "What is a higher-order function?"
---

# Quick Definition

A fun is a function treated as data: a value you can pass, return, store, and later call. Funs may be aliases for named functions or anonymous lambda expressions, and may capture surrounding variables as closures.

# Core Definition

"In Erlang, such a function-as-data object is called a *fun* (or sometimes a *lambda expression* or *closure*)" (Chapter 2, section 2.2.8). You can pass a function as input, return one as a result, store one in a data structure, and call one you obtained that way. There are several forms: an **alias fun** for an existing function — `fun either_or_both/2` (local) or `fun other_module:some_function/2` (remote) — and an **anonymous fun**, written with `fun ... end` and looking like function clauses without a name (section 2.7). A **closure** is the case where a `fun ... end` accesses variables bound *outside* the fun; the fun value then captures a snapshot of those variables' current values. A function that takes or returns a fun is a *higher-order function*.

# Prerequisites

- **Erlang function** — funs are functions used as values.
- **Function clause selection** — anonymous funs are written as one or more clauses.

# Key Properties

1. A fun is a function treated as data — it can be passed, returned, stored, and called.
2. An alias fun refers to a named function: `fun name/Arity` or `fun module:name/Arity`.
3. An anonymous fun is written `fun ... end` and has clauses but no name.
4. A closure captures a snapshot of variables bound outside the fun.
5. Local/anonymous funs are tied to a specific version of the module's code.
6. Remote alias funs (`fun module:name/Arity`) always call the latest version of the function.
7. A higher-order function takes a fun as input or returns one as a result.

# Construction / Recognition

## To Construct/Create:
1. Alias: `F = fun either_or_both/2` or `fun other_module:some_function/2`.
2. Anonymous: `fun (Args) -> Body end`, with one or more clauses.
3. Closure: reference an outer variable inside `fun ... end`.
4. Call a fun value `F` like any function: `F(Arg1, Arg2)`.

# Context & Application

- **Typical contexts**: Parameterizing behavior; callbacks; higher-order functions.
- **Common applications**: Funs serve the roles delegates, adapters, commands, and strategies serve in object-oriented languages.
- **Historical/stylistic notes**: Local funs "have a short expiration date" — reloading the owning module breaks them; remote alias funs are better for long-lived or cross-system use.

# Examples

**Example 1** (section 2.7.1): `yesno(fun either_or_both/2)` passes an alias fun; the receiving `yesno/1` calls it as `F(true, false)` — `yesno/1` is a higher-order function.

**Example 2** (section 2.7.2, Closures): `render(Items, Em)` calls `to_html(Items, fun (Text) -> "<" ++ Em ++ ">" ++ Text ++ "</" ++ Em ++ ">" end)` — the fun is a closure capturing the outer variable `Em`.

# Relationships

## Builds Upon
- **Erlang function** — a fun is a function value.
- **Erlang term** — a fun is a kind of term (function as data).

## Enables
- Higher-order functions and behavior parameterization.

## Related
- **Functional programming** — "functions are data" is a core functional idea.
- **Remote call** — remote alias funs reference functions in other modules.
- **Single assignment** — closures rely on captured variables being immutable.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Storing a local or anonymous fun in a database for long-term use.
  **Correction**: Local/anonymous funs are tied to a code version and break on module reload; use remote alias funs for long-lived storage.

- **Error**: Writing `hello/2` as an expression expecting a fun.
  **Correction**: `name/Arity` is a function name only where the language expects one; as an expression it is interpreted as division. Use `fun name/Arity`.

# Common Confusions

- **Confusion**: Believing "fun," "lambda expression," and "closure" are different things.
  **Clarification**: The terms are often used interchangeably; "closure" specifically emphasizes capturing externally bound variables.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.8 "Functions as data: funs" and section 2.7 "Funs" (2.7.1 alias funs, 2.7.2 anonymous funs and closures).

# Verification Notes

- Definition source: Direct adaptation from sections 2.2.8 and 2.7.
- Confidence rationale: HIGH — funs, alias/anonymous forms, closures, and higher-order functions are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card. Merged the 2.2.8 introduction with the full 2.7 treatment (alias funs, anonymous funs, closures, higher-order functions) into one card per progressive-elaboration guidance.
