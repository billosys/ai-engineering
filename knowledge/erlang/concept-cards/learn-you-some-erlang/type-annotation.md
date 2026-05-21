---
concept: Type Annotation
slug: type-annotation
category: data-types
subcategory: typespecs
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Type Specifications and Dialyzer"
chapter_number: 30
pdf_page: null
section: "Typing Functions"
extraction_confidence: high
aliases:
  - "type signature"
  - "-spec"
  - "function spec"
prerequisites:
  - type-specification
  - dialyzer
related:
  - success-typing
  - dialyzer-warning
  - polymorphic-type
contrasts_with: []
answers_questions:
  - "How do I write type specs for Dialyzer?"
  - "What is an Erlang -spec function signature?"
---

# Type Annotation

## Quick Definition

A type annotation (`-spec`) is a function type signature that declares a function's argument and return types, bridging declared types to functions so Dialyzer can use them.

## Core Definition

Declaring types alone does not make Dialyzer use them — there is an additional step: peppering *type signature declarations* over the functions you want augmented. A type signature has the form `-spec FunctionName(ArgumentTypes) -> ReturnTypes.`, placed directly before the function. Once a `-spec` is present, Dialyzer treats it as a reliable type definition for that function and checks all callers against it. Signatures may have multiple alternative clauses (`-spec convert(tuple()) -> list(); (list()) -> tuple().`) to express dependencies between input and output types that a single union could not (Chapter 30, "Typing Functions").

## Prerequisites

- **Type specification** — The types referenced in a signature must be built-in or declared via `-type`
- **Dialyzer** — Type annotations exist to feed Dialyzer's analysis

## Key Properties

1. Written as `-spec FunctionName(ArgumentTypes) -> ReturnTypes.` before the function
2. Without a `-spec`, Dialyzer infers types itself and may miss errors; with one, it checks callers against it
3. Dialyzer assumes a `-spec` is reliable and propagates contract violations to callers
4. Multiple alternative clauses can be given, separated by `;`, to tie return types to argument types
5. Argument and return types may use variable-name annotations as comments (`In::list()`)
6. The `none()` / `no_return()` return type need not be declared — it is always assumed; `Type() | none()` equals `Type()`
7. Dialyzer infers success typing for a function *before* taking its `-spec` into account

## Construction / Recognition

## To Annotate a Function

1. Identify the function's argument and return types
2. Write `-spec name(ArgType1, ...) -> RetType.` immediately before the definition
3. If the return type depends on which argument types are given, use multiple `;`-separated clauses
4. Run Dialyzer to verify callers respect the contract

## Context & Application

Type annotations turn type declarations from mere documentation into checkable contracts. The chapter shows that `discrep3.erl` passes Dialyzer clean until `discrep4.erl` adds `-spec` clauses for `item/2`, after which Dialyzer can track return values and find the error. Likewise, `cards.erl`'s bad `rubies` call goes undetected until `-spec kind(card()) -> 'face' | 'number'.` is added.

## Examples

**Example** (Chapter 30, "Typing Functions"): `-spec convert(tuple()) -> list(); (list()) -> tuple().` — alternative clauses let Dialyzer detect that expecting a tuple from a tuple is wrong.

**Example** (Chapter 30, "Typed Behaviors"): the R15B `gen_server` uses `-callback` attributes, which have a `-spec`-like syntax, so Dialyzer can check callback module return types.

## Relationships

## Builds Upon

- **Type specification** — Annotations reference the types declared with `-type`
- **Dialyzer** — Annotations exist so Dialyzer can check function contracts

## Related

- **Success typing** — Dialyzer infers success typing first, then reconciles it with the `-spec`
- **Dialyzer warning** — A "breaks the contract" warning arises when a call violates a `-spec`
- **Polymorphic type** — Annotations may reference parameterized types

## Common Errors

- **Error**: Writing overloaded `-spec` clauses with overlapping input domains
  **Correction**: Overlapping domains are unsupported and ignored; make the clauses' input sets disjoint (e.g., `nonempty_list()` vs `[]`)

- **Error**: Adding `none()` to a function's return union
  **Correction**: `none()` is always assumed; `Type() | none()` is just `Type()` — only specify `no_return()` for functions that always fail

## Common Confusions

- **Confusion**: Thinking declaring `-type` types is enough for Dialyzer to check them
  **Clarification**: Types must be attached to functions with `-spec` for Dialyzer to use them in checking callers

## Source Reference

Chapter 30: Type Specifications and Dialyzer, sections "Typing Functions," "Typing Practice," and "Typed Behaviors."

## Verification Notes

- Definition: Direct adaptation from "Typing Functions"
- Key Properties: All explicit in the chapter, including the `none()` sidebar
- Confidence: HIGH — explicitly defined with multiple examples
- Cross-references: verified against planned cards in this extraction
