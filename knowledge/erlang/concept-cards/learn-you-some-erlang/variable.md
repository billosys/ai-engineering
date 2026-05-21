---
concept: Variable
slug: variable
category: core-idioms
subcategory: bindings
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Invariable Variables"
extraction_confidence: high
aliases:
  - "invariable variable"
  - "single assignment"
  - "immutable variable"
  - "bound variable"
  - "unbound variable"
prerequisites: []
extends: []
related:
  - pattern-matching
  - atom
contrasts_with: []
answers_questions:
  - "What are the basic data types in Erlang?"
---

# Variable

## Quick Definition

An Erlang variable is a name (beginning with an uppercase letter) that can be bound to a value exactly once; it cannot be reassigned afterward. Variables are immutable, in keeping with functional programming.

## Core Definition

In Erlang, variables begin with an uppercase letter by definition and can be assigned a value exactly once. The `=` operator (not the variable) compares both sides: if the left variable is unbound, `=` binds the right-hand value to it; if it is already bound, `=` succeeds only when the values match, and otherwise raises a no-match exception. This binding-and-comparing behavior of `=` is the basis of pattern matching (Hébert, ch. 1, "Invariable Variables").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. Variable names must begin with an uppercase letter (or an underscore).
2. A variable can be bound only once; rebinding to a different value raises an exception.
3. An unbound variable has no value; using it raises "variable is unbound."
4. The `=` operator binds an unbound variable, or compares an already-bound one.
5. Variables starting with `_` are conventionally for values you do not care about.
6. `f(Variable)` clears one variable and `f()` clears all — but only in the shell, never in compiled code.

## Construction / Recognition

To bind a variable:

1. Place an unbound variable on the left of `=`.
2. Place a value (or expression) on the right.
3. Erlang binds the variable to the right-hand value and the comparison succeeds.

## Context & Application

Single-assignment variables make Erlang code referentially transparent and are essential for safe concurrency and code hot-loading. In long-running industrial systems a shell may run for years, so variables can be reused across that time.

## Examples

**Example** (ch. 1): `One = 1.` binds `One`; later `One.` returns `1`. `Two = Two + 1.` raises `** exception error: no match of right hand side value 3`.

**Example** (ch. 1): `Un = Uno = One = 1.` binds all three variables to `1`.

## Relationships

### Related

- **Pattern matching** — The binding/comparing behavior of `=` is the foundation of pattern matching
- **Atom** — Lowercase names are atoms; uppercase names are variables, which is why the distinction by case exists

## Common Errors

- **Error**: Reassigning a variable to a new value
  **Correction**: Use a new variable name; values cannot be mutated

## Common Confusions

- **Confusion**: Thinking `=` is an assignment operator
  **Clarification**: `=` is a match operator; it binds only when the left side is unbound, and otherwise compares

## Source Reference

Chapter 1: "Starting Out," section "Invariable Variables."

## Verification Notes

- Definition: Adapted from "Invariable Variables" with the six-expression worked example
- Confidence: HIGH — explicit and detailed treatment in source
- Uncertainties: None
