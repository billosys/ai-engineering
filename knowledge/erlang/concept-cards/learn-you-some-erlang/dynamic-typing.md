---
concept: Dynamic Typing
slug: dynamic-typing
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
  - "dynamic type system"
prerequisites: []
extends: []
related:
  - strong-typing
  - type-test-bif
contrasts_with:
  - strong-typing
answers_questions:
  - "What distinguishes dynamic typing from static typing?"
---

# Dynamic Typing

## Quick Definition

Erlang is dynamically typed: variable and function types are never declared, and every type error is caught at runtime rather than at compile time.

## Core Definition

Erlang is dynamically typed — every error is caught at runtime, and the compiler will not always reject modules where things may fail (as in the `5 + llama` example). You never need to specify the type of a variable or a function; a tuple `{X,Y}` can be matched against anything at all. Dynamic typing was chosen historically because Erlang's first implementers came from dynamic languages, and it also proved the simplest way to allow hot code reloading: doing static type checking on a system whose components may be replaced at any time is difficult compared to checking dynamically (Hébert, ch. 4, "Dynamite-Strong Typing").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. Types of variables and functions are never declared.
2. Type errors are caught at runtime, not compile time.
3. The compiler catches only some failures (e.g., obvious `badarith`).
4. Chosen historically and because it eases hot code reloading.
5. Erlang assumes errors will happen and provides features to handle them smoothly.

## Construction / Recognition

To recognize dynamic typing: code can pattern match a structure against any data without type annotations, and mismatches fail only when the code runs.

## Context & Application

Despite dynamic typing, Erlang has a strong reliability record (e.g., the nine nines of availability on the Ericsson AXD 301 switches). Erlang's safety comes not from preventing all errors at compile time but from handling errors gracefully at runtime.

## Examples

**Example** (ch. 4): The `5 + llama` expression from chapter 1 compiles but fails only at runtime, illustrating runtime type checking.

## Relationships

### Related

- **Strong typing** — Erlang is both dynamically and strongly typed
- **Type-test BIF** — Type-test BIFs check types at runtime

### Contrasts With

- **Strong typing** — A separate property (no implicit conversions); dynamic vs. static is the orthogonal axis

## Common Errors

- **Error**: Expecting the compiler to catch all type mismatches
  **Correction**: Most type errors surface only at runtime; testing is the main defense

## Common Confusions

- **Confusion**: Equating dynamic typing with weak typing
  **Clarification**: Dynamic (when types are checked) is independent of strong/weak (whether implicit conversions occur); Erlang is dynamic *and* strong

## Source Reference

Chapter 4: "Types (or Lack Thereof)," section "Dynamite-Strong Typing."

## Verification Notes

- Definition: Adapted from the "Dynamite-Strong Typing" section
- Confidence: HIGH — explicit treatment
- Uncertainties: None
