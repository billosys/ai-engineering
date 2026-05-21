---
concept: Numbers in Erlang
slug: number-erlang
category: data-types
subcategory: primitive-types
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Numbers"
extraction_confidence: high
aliases:
  - "integers"
  - "floats"
  - "floating-point numbers"
prerequisites: []
extends: []
related:
  - boolean-and-comparison-operators
  - type-conversion
contrasts_with: []
answers_questions:
  - "What are the basic data types in Erlang?"
---

# Numbers in Erlang

## Quick Definition

Erlang supports two numeric types — integers and floating-point numbers — and handles arithmetic over both without requiring you to declare which is which. Integers can be written in bases 2 through 36.

## Core Definition

Erlang has integers and floats as built-in numeric types. Arithmetic operators work on both interchangeably, but integer-specific operators exist: `div` for integer-to-integer division and `rem` for the remainder (modulo) of an integer division. Integers in bases other than 10 are written in the form `Base#Value`, where `Base` is in the range 2 through 36 (Hébert, ch. 1, "Numbers").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. Two numeric types: integers and floats.
2. Standard arithmetic operators (`+`, `-`, `*`, `/`) accept both types; `/` always yields a float.
3. `div` performs integer division; `rem` gives the remainder of an integer division.
4. Mathematical operations obey normal precedence rules.
5. Integers in another base use `Base#Value` notation, with `Base` from 2 to 36.
6. Arithmetic with a non-number argument raises a `badarith` error.

## Construction / Recognition

To write an integer in a non-decimal base:

1. Write the base (2–36).
2. Follow it with `#`.
3. Follow that with the digits in that base.

## Context & Application

Numbers are the most basic data type and are typically the first thing tested in the shell. Base notation is useful for working with binary, octal, and hexadecimal values (e.g., color codes).

## Examples

**Example** (ch. 1): `5 / 2.` returns `2.5`; `5 div 2.` returns `2`; `5 rem 2.` returns `1`.

**Example** (ch. 1): `2#101010.` returns `42`, `8#0677.` returns `447`, and `16#AE.` returns `174`.

## Relationships

### Related

- **Boolean and comparison operators** — Erlang distinguishes integers from floats when comparing, even though arithmetic treats them alike
- **Type conversion** — BIFs convert between integers, floats, and other types

## Common Errors

- **Error**: Using `/` and expecting an integer result
  **Correction**: Use `div` for integer division when an integer result is required

## Common Confusions

- **Confusion**: Believing Erlang distinguishes integers and floats in arithmetic
  **Clarification**: Arithmetic treats them identically; only comparison operators (`=:=` vs `==`) distinguish them

## Source Reference

Chapter 1: "Starting Out," section "Numbers."

## Verification Notes

- Definition: Adapted from the "Numbers" section with worked shell examples
- Confidence: HIGH — explicit section with examples
- Uncertainties: None
