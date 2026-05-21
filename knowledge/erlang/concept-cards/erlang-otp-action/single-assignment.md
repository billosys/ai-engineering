---
# === CORE IDENTIFICATION ===
concept: Single Assignment
slug: single-assignment

# === CLASSIFICATION ===
category: core-idioms
subcategory: variables
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.4.2 Single assignment"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - single-assignment variables
  - immutable variables
  - binding
  - variable scope

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable
extends: []
related:
  - pattern-matching
  - functional-programming
  - referential-transparency
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is single assignment in Erlang?"
  - "Can you change the value of an Erlang variable?"
  - "How do you compute a new value from an old one without mutation?"
---

# Quick Definition

Single assignment means an Erlang variable, once bound to a value, holds that same value throughout its entire scope. Variables cannot be updated in place.

# Core Definition

"Erlang's variables are strictly *single assignment*. This means that when you assign a value to a variable — or, as we say in Erlang country, *bind* the variable to a value — that variable will hold the same value throughout its entire *scope*" (Chapter 2, section 2.4.2). The same variable name may be reused elsewhere, but that is a different variable with a distinct, non-overlapping scope. Unlike the named "boxes" of most languages, Erlang's variables are like variables in mathematics: a name for a value that does not change behind your back. To track a new value, you give it another name — for example `X1 = X + 1`. In the shell, variable bindings last "as long as the shell is still running, unless I say otherwise"; `f()` forgets all bindings and `f(X)` forgets just `X`. Within a module, scopes are tied to function definitions and bindings cannot be forgotten prematurely.

# Prerequisites

- **Variable** — single assignment is a rule governing variables.

# Key Properties

1. A bound variable holds the same value throughout its scope.
2. Variables cannot be updated in place.
3. The same name in a different scope is a different variable.
4. Binding via `=` to an already-bound variable succeeds only if the value matches; otherwise it fails.
5. To track a changed value, introduce a new name (e.g. `X1`).
6. In the shell, `f()` forgets all bindings; `f(X)` forgets only `X`.
7. In a module, scopes are tied to function definitions; bindings cannot be forgotten prematurely.

# Construction / Recognition

## To Construct/Create:
1. Bind a variable once with `=`, e.g. `X = 42`.
2. To compute a derived value, bind a new name: `X1 = X + 1`.
3. Reusing `X` for a different value requires it to be out of scope (or forgotten in the shell with `f(X)`).

# Context & Application

- **Typical contexts**: All Erlang code.
- **Common applications**: Functional-style computation without mutable state; closures rely on captured values being immutable.
- **Historical/stylistic notes**: The book advises splitting code into separate functions — each with its own `X` — rather than accumulating many almost-the-same variables.

# Examples

**Example 1** (section 2.4.2): `X = 42.` binds `X`; later `X = 101.` raises an exception ("no match of right hand side value 101") because single assignment is enforced, while re-binding `X = 17.` to its existing value succeeds.

**Example 2** (section 2.4.2): To name the value of `X` plus 1, you write `X1 = X + 1` — giving the new value a new name rather than updating `X`.

# Relationships

## Builds Upon
- **Variable** — single assignment is the rule that governs variables.

## Enables
- **Functional programming** — values are never updated in place.
- **Referential transparency** — a name reliably denotes one value.

## Related
- **Pattern matching** — `=` is a match; re-binding to an unequal value fails the match.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Trying to reassign a bound variable to a different value.
  **Correction**: Single assignment forbids this; introduce a new name (e.g. `X1`).

- **Error**: Reusing the same variable name within one clause for "almost the same" values.
  **Correction**: Either name them `X1`, `X2`, ... or, better, split the code into separate functions.

# Common Confusions

- **Confusion**: Thinking an Erlang variable is a mutable box like in C or Java.
  **Clarification**: An Erlang variable is a mathematical name for one fixed value, not a container whose contents change.

# Source Reference

Chapter 2: Erlang language essentials, section 2.4.2 "Single assignment" (including "The = operator and using variables in the shell" and "Variables and updates" subsections).

# Verification Notes

- Definition source: Direct adaptation from section 2.4.2.
- Confidence rationale: HIGH — single assignment is explicitly defined and demonstrated.
- Uncertainties: None.
- Cross-reference status: `referential-transparency` is a planned card in this source.
- Re-extraction notes: Fresh extraction; no prior card.
