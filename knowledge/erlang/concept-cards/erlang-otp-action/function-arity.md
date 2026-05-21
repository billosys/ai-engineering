---
# === CORE IDENTIFICATION ===
concept: Function Arity
slug: function-arity

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-definition
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.3.2 Functions of different arity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - arity
  - "name/arity"
  - nullary
  - unary

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-function
extends: []
related:
  - remote-call
  - erlang-module
  - fun
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the arity of a function?"
  - "Why is arity part of a function's identity in Erlang?"
  - "How do you write a function's full name?"
---

# Quick Definition

Arity is the number of arguments a function takes. In Erlang a function's full identity is its name plus its arity; functions of the same name but different arity are completely separate.

# Core Definition

"The number of arguments a function takes is referred to as its *arity*" (Chapter 2, section 2.3.2). A function taking one argument is *unary*, two is *binary*, three is *ternary*; one taking no arguments (like `self()`) is *nullary*. Arity matters more in Erlang than in most languages: "Erlang doesn't have function overloading as such; instead, it treats functions of different arities as completely separate even if they have the same atom as identifier." The full name of a function must always include the arity, written with a slash: `reverse/1`, or `lists:reverse/1` to also specify the module. This `name/arity` syntax may only be used where the language expects a function name; written as an expression, `hello/2` is interpreted as dividing the atom `'hello'` by 2.

# Prerequisites

- **Erlang function** — arity is a property of a function.

# Key Properties

1. Arity is the number of arguments a function takes.
2. Functions of the same name but different arity are completely separate functions.
3. Erlang has no function overloading; arity distinguishes functions instead.
4. A function's full name is `name/arity` (e.g. `reverse/1`).
5. Within a module, qualify further as `module:name/arity`.
6. The `name/arity` form is valid only where a function name is expected.

# Construction / Recognition

## To Identify/Recognize:
1. Count the parenthesized arguments in the function head.
2. Write the function's identity as `name/arity`.
3. Recognize that `foo/1` and `foo/2` are different functions.

# Context & Application

- **Typical contexts**: Export lists, function references, error messages.
- **Common applications**: `-export([name/arity, ...])`; `fun name/arity`; identifying functions in `undefined function` errors.
- **Historical/stylistic notes**: The book warns against abusing same-name/different-arity functions to produce wildly different results; when in doubt, give functions clearly different names.

# Examples

**Example 1** (section 2.3.2): `lists:reverse/1` reverses a list; `lists:reverse/2` reverses a list and appends a second list — `lists:reverse([10,11,12], [9,8,7])` yields `[12,11,10,9,8,7]`. Same name, different arity, separate functions.

**Example 2** (section 2.3.2): Writing `hello/2` as an expression makes Erlang try to divide the atom `'hello'` by 2 — the `name/arity` syntax is only valid where a function name is expected.

# Relationships

## Builds Upon
- **Erlang function** — arity is part of a function.

## Enables
- Precise identification of functions in exports, references, and errors.

## Related
- **Remote call** / **Erlang module** — fully identifying a function uses `module:name/arity`.
- **Fun** — a fun alias is written `fun name/arity`.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Assuming a function name alone uniquely identifies a function.
  **Correction**: Always include the arity; `name/arity` is the identity.

- **Error**: Using `name/arity` as a value in an expression.
  **Correction**: It is valid only where a function name is expected; otherwise it parses as division.

# Common Confusions

- **Confusion**: Expecting function overloading where same-name functions cooperate.
  **Clarification**: Erlang has no overloading; different-arity functions of the same name are entirely separate.

# Source Reference

Chapter 2: Erlang language essentials, section 2.3.2 "Functions of different arity."

# Verification Notes

- Definition source: Direct adaptation from section 2.3.2.
- Confidence rationale: HIGH — arity and its role in function identity are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
