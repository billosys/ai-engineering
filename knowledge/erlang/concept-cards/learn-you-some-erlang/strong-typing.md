---
concept: Strong Typing
slug: strong-typing
category: data-types
subcategory: type-system
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Types (or Lack Thereof)"
chapter_number: 4
pdf_page: null
section: "Dynamite-Strong Typing"
extraction_confidence: high
aliases:
  - "strong type system"
prerequisites: []
extends: []
related:
  - dynamic-typing
  - type-conversion
contrasts_with:
  - dynamic-typing
answers_questions:
  - "What distinguishes dynamic typing from static typing?"
---

# Strong Typing

## Quick Definition

Erlang is strongly typed: it never performs implicit type conversions between terms, so mixing incompatible types raises an exception rather than silently coercing values.

## Core Definition

Erlang is strongly typed, meaning it does not do implicit type conversions between terms. A weakly typed language might allow `6 = 5 + "1"` by silently coercing the string; because of Erlang's strong typing, trying `6 + "1"` raises a `badarith` "bad argument" exception. When conversion between types is genuinely needed, the standard library provides explicit conversion BIFs (Hébert, ch. 4, "Dynamite-Strong Typing").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. No implicit type conversions occur between terms.
2. Mixing incompatible types in an operation raises an exception.
3. Strong typing is independent of dynamic/static typing.
4. Explicit conversion BIFs are provided for deliberate type changes.

## Construction / Recognition

To recognize strong typing: an operation on mismatched types (e.g., a number plus a string) raises an exception instead of coercing.

## Context & Application

Strong typing forces conversions to be explicit and deliberate, preventing the subtle bugs that silent coercion causes. It works alongside dynamic typing — Erlang is both strong and dynamic.

## Examples

**Example** (ch. 4): `6 + "1".` raises `** exception error: bad argument in an arithmetic expression`, because Erlang will not coerce the string `"1"`.

## Relationships

### Related

- **Dynamic typing** — Erlang is both strongly and dynamically typed
- **Type conversion** — Explicit conversion BIFs exist precisely because no implicit coercion happens

### Contrasts With

- **Dynamic typing** — Strong/weak (coercion) is a different axis from dynamic/static (when checked)

## Common Errors

- **Error**: Expecting a number and a string to combine via coercion
  **Correction**: Convert types explicitly with conversion BIFs first

## Common Confusions

- **Confusion**: Thinking "dynamic" implies "weak"
  **Clarification**: Erlang is dynamically typed yet strongly typed — it checks at runtime but never coerces

## Source Reference

Chapter 4: "Types (or Lack Thereof)," section "Dynamite-Strong Typing."

## Verification Notes

- Definition: Adapted from the strong-typing discussion
- Confidence: HIGH — explicit treatment with example
- Uncertainties: None
